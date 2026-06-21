#!/usr/bin/env python3
"""
gen_dark.py
====================
Script de pre-render de Quarto. Genera automàticament les variants dark de
les figures SVG light del projecte EC que coincideixen amb la regex d'entrada.

Ús
--
Com a pre-render de Quarto (_quarto.yml):

    project:
      pre-render:
        - scripts/gen_dark.py svg_specs.md "extern/.*_light\\.svg"
        - scripts/gen_dark.py svg_specs.md "figures/.*_light\\.svg"

Ús manual:

    python3 scripts/gen_dark.py <specs_file> <regex_entrada> [opcions]

Arguments posicionals
---------------------
specs_file    Fitxer svg_specs.md amb el bloc #svg-dark-replacements.
regex_entrada Expressió regular aplicada sobre les rutes relatives al CWD.
              Exemple: "figures/.*_light\\.svg"
              Exemple: "(extern|figures)/.*_light\\.svg"

La taula de substitució de colors és la font de veritat única definida a
svg_specs.md, dins el bloc etiquetat `#svg-dark-replacements`.
Per modificar la paleta dark, editeu només aquell bloc.

Lògica de regeneració
---------------------
Per a cada fitxer *_light.svg que coincideix amb la regex:
  1. Si el nom base és a `dark_exclusions.txt` → SALTA (dark manual).
  2. Si la dark ja existeix i és més nova que la light → SALTA (vigent).
  3. En cas contrari → GENERA la dark aplicant la taula de substitució.

El fitxer de sortida substitueix el sufix `_light` per `_dark` i es desa
al mateix directori que el fitxer d'entrada.

Colors no reconeguts
--------------------
Després de la generació, l'script reporta els colors trobats als SVG que
no estan a la taula REPLACEMENTS ni a la llista de colors acceptables
(none, transparent, currentColor). El comportament es controla amb:

  --on-unknown-color report   (per defecte) Reporta i no modifica.
  --on-unknown-color invert   Inverteix la lluminositat HSL automàticament.
  --on-unknown-color #RRGGBB  Substitueix per un color fix.

Fitxer d'exclusions
-------------------
`dark_exclusions.txt` (al CWD): un patró regex per línia.
Les línies que comencen per `#` s'ignoren (comentaris).
"""

import ast
import colorsys
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Colors acceptables (no es reporten com a desconeguts)
# ---------------------------------------------------------------------------

def _build_known_colors(replacements: list[tuple[str, str]]) -> frozenset[str]:
    """Colors de la taula REPLACEMENTS (light i dark) + valors CSS especials."""
    known = set()
    for src, dst in replacements:
        known.add(src.lower())
        known.add(dst.lower())
    known.update({'none', 'transparent', 'currentcolor'})
    return frozenset(known)


# ---------------------------------------------------------------------------
# Inversió HSL
# ---------------------------------------------------------------------------

def _invert_hsl(hex_color: str) -> str:
    """
    Inverteix la lluminositat d'un color hexadecimal (HSL: L → 1-L).
    Retorna el color en format #RRGGBB.
    """
    h = hex_color.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    if len(h) != 6:
        return hex_color  # format no reconegut, no toca
    r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    hh, s, l = colorsys.rgb_to_hls(r, g, b)
    r2, g2, b2 = colorsys.hls_to_rgb(hh, 1.0 - l, s)
    return '#{:02x}{:02x}{:02x}'.format(
        round(r2 * 255), round(g2 * 255), round(b2 * 255)
    )


# ---------------------------------------------------------------------------
# Lectura de la taula de substitució des de svg_specs.md
# ---------------------------------------------------------------------------

def _load_replacements(specs_file: Path) -> list[tuple[str, str]]:
    """
    Extreu la variable REPLACEMENTS del bloc `{.python #svg-dark-replacements}`
    de svg_specs.md i la retorna com a llista de tuples (light, dark).

    Llança ValueError si el bloc no es troba o no es pot parsejar.
    """
    content = specs_file.read_text(encoding='utf-8')

    pattern = re.compile(
        r'```\{\.python\s+#svg-dark-replacements\}(.*?)```',
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        raise ValueError(
            f"Bloc '#svg-dark-replacements' no trobat a {specs_file}.\n"
            "Afegiu un bloc ```{.python #svg-dark-replacements} amb REPLACEMENTS = [...]"
        )

    block = match.group(1).strip()

    try:
        tree = ast.parse(block, mode='exec')
    except SyntaxError as exc:
        raise ValueError(f"Error de sintaxi al bloc de substitució: {exc}") from exc

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == 'REPLACEMENTS'
                for t in node.targets
            )
        ):
            try:
                replacements = ast.literal_eval(node.value)
            except ValueError as exc:
                raise ValueError(
                    f"No s'ha pogut avaluar REPLACEMENTS: {exc}"
                ) from exc
            if not isinstance(replacements, list):
                raise ValueError("REPLACEMENTS ha de ser una llista.")
            return [(str(a), str(b)) for a, b in replacements]

    raise ValueError(
        f"Variable REPLACEMENTS no trobada al bloc '#svg-dark-replacements' de {specs_file}."
    )


# ---------------------------------------------------------------------------
# Substitució de colors
# ---------------------------------------------------------------------------

_COLOR_RE = re.compile(
    r'(?:fill|stroke|stop-color|color)\s*[=:]\s*["\']?\s*(#[0-9a-fA-F]{3,8}|'
    r'none|transparent|currentColor|rgb\([^)]+\))\s*["\']?',
    re.IGNORECASE,
)

_HEX_RE = re.compile(r'^#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?$')


def _build_substituter(replacements: list[tuple[str, str]]):
    """Retorna una funció de substitució compilada per a la taula donada."""
    pattern = re.compile(
        '|'.join(re.escape(src) for src, _ in replacements),
        flags=re.IGNORECASE,
    )
    mapping = {src.lower(): dst for src, dst in replacements}
    return lambda content: pattern.sub(
        lambda m: mapping[m.group(0).lower()], content
    )


def _apply_unknown_color_policy(
    content: str,
    unknown_colors: list[str],
    policy: str,
) -> str:
    """
    Aplica la política per a colors desconeguts sobre el contingut SVG.
    policy: 'report' (no toca) | 'invert' | '#RRGGBB' (color fix)
    """
    if policy == 'report' or not unknown_colors:
        return content

    for color in unknown_colors:
        if not _HEX_RE.match(color):
            continue  # rgb(), etc. no els transformem
        if policy == 'invert':
            replacement = _invert_hsl(color)
        else:
            replacement = policy  # color fix

        # Substituïm el color (case-insensitive, només valors hexadecimals)
        content = re.sub(re.escape(color), replacement, content, flags=re.IGNORECASE)

    return content


def _find_unknown_colors(
    content: str,
    known_colors: frozenset[str],
) -> list[str]:
    """Retorna els colors del SVG que no són a known_colors."""
    found = [m.group(1).lower() for m in _COLOR_RE.finditer(content)]
    unknown = [c for c in found if c not in known_colors]
    return list(dict.fromkeys(unknown))


# ---------------------------------------------------------------------------
# Fitxer d'exclusions
# ---------------------------------------------------------------------------

def _load_exclusions(exclusions_file: Path) -> list[re.Pattern]:
    """Carrega els patrons d'exclusió com a expressions regulars compilades."""
    if not exclusions_file.exists():
        return []
    lines = exclusions_file.read_text(encoding='utf-8').splitlines()
    patterns = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            patterns.append(re.compile(line))
        except re.error as exc:
            print(
                f'[dark-svg] AVÍS: patró d\'exclusió invàlid {line!r}: {exc}',
                file=sys.stderr,
            )
    return patterns


def _is_excluded(dark_name: str, exclusions: list[re.Pattern]) -> bool:
    return any(p.search(dark_name) for p in exclusions)


# ---------------------------------------------------------------------------
# Lògica principal
# ---------------------------------------------------------------------------

def generate_dark_svgs(
    input_regex: re.Pattern,
    specs_file: Path,
    exclusions_file: Path,
    unknown_color_policy: str = 'report',
    verbose: bool = True,
) -> None:

    # Carrega la taula des de svg_specs.md
    try:
        replacements = _load_replacements(specs_file)
    except ValueError as exc:
        print(f'[dark-svg] ERROR carregant taula de substitució: {exc}', file=sys.stderr)
        sys.exit(1)

    known_colors = _build_known_colors(replacements)

    if verbose:
        print(
            f'[dark-svg] Taula carregada des de {specs_file} '
            f'({len(replacements)} substitucions)'
        )
        if unknown_color_policy != 'report':
            print(f'[dark-svg] Política colors desconeguts: {unknown_color_policy!r}')

    apply_dark = _build_substituter(replacements)

    # Troba tots els *_light.svg que coincideixen amb la regex
    root = Path.cwd()
    light_files = sorted(
        p for p in root.rglob('*_light.svg')
        if input_regex.search(str(p.relative_to(root)))
    )

    if not light_files:
        if verbose:
            print(f'[dark-svg] Cap fitxer trobat per la regex {input_regex.pattern!r}')
        return

    exclusions = _load_exclusions(exclusions_file)
    if verbose and exclusions:
        print(
            f'[dark-svg] Exclusions ({len(exclusions)} patrons): '
            f'{[p.pattern for p in exclusions]}'
        )

    generated = skipped_manual = skipped_fresh = errors = 0
    unknown_report: dict[str, list[str]] = {}

    for light_path in light_files:
        dark_name = light_path.name.replace('_light.svg', '_dark.svg')
        dark_path = light_path.parent / dark_name
        rel_light = str(light_path.relative_to(root))

        # 1. Exclusió manual (regex)
        if _is_excluded(dark_name, exclusions):
            if verbose:
                print(f'[dark-svg] SALTA (manual)  {rel_light}')
            skipped_manual += 1
            continue

        # 2. Dark vigent (més nova que light)
        if (
            dark_path.exists()
            and dark_path.stat().st_mtime > light_path.stat().st_mtime
        ):
            if verbose:
                print(f'[dark-svg] SALTA (vigent)  {rel_light}')
            skipped_fresh += 1
            continue

        # 3. Generació
        try:
            content = light_path.read_text(encoding='utf-8')

            # Detecció de colors no reconeguts (sobre el contingut LIGHT)
            unknowns = _find_unknown_colors(content, known_colors)
            for c in unknowns:
                unknown_report.setdefault(c, []).append(rel_light)

            # Aplicació de la política per a colors desconeguts
            content = _apply_unknown_color_policy(content, unknowns, unknown_color_policy)

            dark_content = apply_dark(content)
            dark_path.write_text(dark_content, encoding='utf-8')
            if verbose:
                print(f'[dark-svg] GENERAT         {rel_light}')
            generated += 1

        except Exception as exc:  # noqa: BLE001
            print(f'[dark-svg] ERROR  {rel_light}: {exc}', file=sys.stderr)
            errors += 1

    if verbose:
        print(
            f'[dark-svg] Resum: {generated} generats, '
            f'{skipped_fresh} vigents, '
            f'{skipped_manual} manuals, '
            f'{errors} errors.'
        )

    if unknown_report:
        if unknown_color_policy == 'report':
            print(
                '\n[dark-svg] AVÍS — colors no reconeguts '
                '(no modificats per política "report"):'
            )
        else:
            print(
                f'\n[dark-svg] AVÍS — colors no reconeguts '
                f'(transformats per política {unknown_color_policy!r}):'
            )
        for color, files in sorted(unknown_report.items()):
            print(f'  Color: {color!r}')
            for fn in sorted(files):
                print(f'    {fn}')
        if unknown_color_policy == 'report':
            print(
                '\n[dark-svg] Passa la llista de colors no reconeguts a Claude perquè '
                'els incorpori a svg_specs.md (bloc #svg-dark-replacements) i torna a '
                'executar l\'script. Hauria de reportar 0 colors no reconeguts.'
            )

    if errors:
        sys.exit(1)


# ---------------------------------------------------------------------------
# Punt d'entrada
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Genera les variants dark dels fitxers *_light.svg "
            "del projecte EC que coincideixen amb la regex d'entrada."
        )
    )
    parser.add_argument(
        'specs_file',
        type=Path,
        metavar='specs_file',
        help="Fitxer svg_specs.md amb el bloc #svg-dark-replacements.",
    )
    parser.add_argument(
        'regex_entrada',
        metavar='regex_entrada',
        help=(
            "Expressió regular aplicada sobre rutes relatives al CWD. "
            "Exemple: \"figures/.*_light\\\\.svg\""
        ),
    )
    parser.add_argument(
        '--exclusions-file',
        type=Path,
        default=Path('dark_exclusions.txt'),
        metavar='FILE',
        help="Fitxer d'exclusions (per defecte: ./dark_exclusions.txt)",
    )
    parser.add_argument(
        '--on-unknown-color',
        default='report',
        metavar='POLÍTICA',
        help=(
            "Comportament davant colors no reconeguts: "
            "'report' (per defecte, no modifica), "
            "'invert' (inverteix lluminositat HSL), "
            "o '#RRGGBB' (substitueix per color fix)."
        ),
    )
    args = parser.parse_args()

    # Validació de la política de color
    policy = args.on_unknown_color
    if policy not in ('report', 'invert') and not _HEX_RE.match(policy):
        print(
            f'[dark-svg] ERROR: --on-unknown-color ha de ser "report", "invert" '
            f'o un color hexadecimal (#RRGGBB). Valor rebut: {policy!r}',
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        input_regex = re.compile(args.regex_entrada)
    except re.error as exc:
        print(
            f'[dark-svg] ERROR: regex invàlida {args.regex_entrada!r}: {exc}',
            file=sys.stderr,
        )
        sys.exit(1)

    generate_dark_svgs(
        input_regex=input_regex,
        specs_file=args.specs_file,
        exclusions_file=args.exclusions_file,
        unknown_color_policy=policy,
        verbose=True,
    )
