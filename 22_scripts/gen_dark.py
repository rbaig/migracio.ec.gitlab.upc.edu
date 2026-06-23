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
        - bash -c "rm -rf figs_auto && mkdir figs_auto"
        - scripts/gen_regs.py  specs/registres.toml "__registre_light" --output-dir="figs_auto/"
        - scripts/norm_font.py specs/svg.md "figs_externes/[^/]+[.]svg"  "__extern_light"   --output-dir="figs_auto/"
        - scripts/norm_font.py specs/svg.md "figs_originals/[^/]+[.]svg" "__original_light" --output-dir="figs_auto/"
        - scripts/gen_dark.py  specs/svg.md "figs_auto/[^/]+_light[.]svg" --output-dir="figs_auto/"

Ús manual:

    python3 22_scripts/gen_dark.py <specs_file> <regex_entrada> [opcions]

Arguments posicionals
---------------------
specs_file    Fitxer 21_specs/svg.md amb el bloc #svg-dark-replacements.
regex_entrada Expressió regular aplicada sobre les rutes relatives al CWD.
              Exemple: "figs_auto/[^/]+_light[.]svg"

Arguments opcionals
-------------------
--output-dir        Directori on es desen els fitxers dark generats (per defecte: .).
                    La sortida és plana: no es preserva l'estructura de subdirectoris.
                    El nom de sortida substitueix el sufix `_light` per `_dark`.
--on-unknown-color  `report`|`invert`|`#RRGGBB`
                    Comportament davant colors no reconeguts:
                      `report`   (per defecte) Reporta i no modifica.
                      `invert`   Inverteix la lluminositat HSL automàticament.
                      `#RRGGBB`  Substitueix per un color fix.
--verbosity 0|1|2
                    Nivell de detall del log (per defecte: 1).
                      0  Només errors i resum final.
                      1  Errors + avisos (colors desconeguts) + resum.
                      2  Tot l'anterior + una línia per fitxer processat.

La taula de substitució de colors és la font de veritat única definida a
21_specs/svg.md, dins el bloc etiquetat `#svg-dark-replacements`.
Per modificar la paleta dark, editeu només aquell bloc.
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
        return hex_color
    r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    hh, s, l = colorsys.rgb_to_hls(r, g, b)
    r2, g2, b2 = colorsys.hls_to_rgb(hh, 1.0 - l, s)
    return '#{:02x}{:02x}{:02x}'.format(
        round(r2 * 255), round(g2 * 255), round(b2 * 255)
    )


# ---------------------------------------------------------------------------
# Lectura de la taula de substitució des de 21_specs/svg.md
# ---------------------------------------------------------------------------

def _load_replacements(specs_file: Path) -> list[tuple[str, str]]:
    """
    Extreu la variable REPLACEMENTS del bloc `{.python #svg-dark-replacements}`
    de 21_specs/svg.md i la retorna com a llista de tuples (light, dark).

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
            continue
        replacement = _invert_hsl(color) if policy == 'invert' else policy
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
# Lògica principal
# ---------------------------------------------------------------------------

def generate_dark_svgs(
    input_regex: re.Pattern,
    specs_file: Path,
    output_dir: Path,
    unknown_color_policy: str = 'report',
    verbosity: int = 1,
) -> None:

    try:
        replacements = _load_replacements(specs_file)
    except ValueError as exc:
        print(f'[gen-dark] ERROR carregant taula de substitució: {exc}', file=sys.stderr)
        sys.exit(1)

    known_colors = _build_known_colors(replacements)

    if verbosity >= 2:
        print(
            f'[gen-dark] Taula carregada des de {specs_file} '
            f'({len(replacements)} substitucions, {len(known_colors)} colors acceptats)'
        )
        print('[gen-dark] Substitucions light \u2192 dark:')
        for src, dst in replacements:
            print(f'  {src!r}  \u2192  {dst!r}')
        extra = sorted(
            known_colors
            - {s.lower() for s, _ in replacements}
            - {d.lower() for _, d in replacements}
        )
        if extra:
            print('[gen-dark] Colors addicionals acceptats sense substitució:')
            for c in extra:
                print(f'  {c!r}')
        if unknown_color_policy != 'report':
            print(f'[gen-dark] Política `--on-unknown-color`: {unknown_color_policy!r}')

    apply_dark = _build_substituter(replacements)
    output_dir.mkdir(parents=True, exist_ok=True)

    root = Path.cwd()
    light_files = sorted(
        p for p in root.rglob('*_light.svg')
        if input_regex.search(str(p.relative_to(root)))
    )

    if not light_files:
        if verbosity >= 1:
            print(f'[gen-dark] Cap fitxer trobat per la regex {input_regex.pattern!r}')
        return

    generated = errors = 0
    unknown_report: dict[str, list[str]] = {}

    for light_path in light_files:
        dark_name = light_path.stem.replace('_light', '_dark') + '.svg'
        dark_path = output_dir / dark_name
        rel_light = str(light_path.relative_to(root))

        try:
            content = light_path.read_text(encoding='utf-8')

            unknowns = _find_unknown_colors(content, known_colors)
            for c in unknowns:
                unknown_report.setdefault(c, []).append(rel_light)

            content = _apply_unknown_color_policy(content, unknowns, unknown_color_policy)
            dark_content = apply_dark(content)
            dark_path.write_text(dark_content, encoding='utf-8')
            generated += 1
            if verbosity >= 2:
                print(f'[gen-dark] GENERAT  {rel_light}  \u2192  {dark_path.name}')

        except Exception as exc:  # noqa: BLE001
            print(f'[gen-dark] ERROR  {rel_light}: {exc}', file=sys.stderr)
            errors += 1

    if verbosity >= 1:
        print(f'[gen-dark] Resum: {generated} generats, {errors} errors.')

    if unknown_report:
        if verbosity >= 1:
            if unknown_color_policy == 'report':
                print(
                    '\n[gen-dark] AVÍS — colors no reconeguts '
                    '(no modificats per política `--on-unknown-color report`):'
                )
            else:
                print(
                    f'\n[gen-dark] AVÍS — colors no reconeguts '
                    f'(transformats per `--on-unknown-color {unknown_color_policy}`):'
                )
            for color, files in sorted(unknown_report.items()):
                print(f'  Color: {color!r}')
                for fn in sorted(files):
                    print(f'    {fn}')
            if unknown_color_policy == 'report':
                print(
                    '\n[gen-dark] Passa la llista de colors no reconeguts a Claude perquè '
                    "els incorpori a 21_specs/svg.md (bloc `#svg-dark-replacements`) i torna a "
                    "executar l'script. Hauria de reportar 0 colors no reconeguts."
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
        help="Fitxer 21_specs/svg.md amb el bloc #svg-dark-replacements.",
    )
    parser.add_argument(
        'regex_entrada',
        metavar='regex_entrada',
        help=(
            "Expressió regular aplicada sobre rutes relatives al CWD. "
            "Exemple: \"figs_auto/[^/]+_light[.]svg\""
        ),
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('.'),
        metavar='DIR',
        help=(
            "Directori de sortida (per defecte: .). "
            "La sortida és plana: no es preserva l'estructura de subdirectoris."
        ),
    )
    parser.add_argument(
        '--on-unknown-color',
        default='report',
        metavar='POLÍTICA',
        help=(
            "Comportament davant colors no reconeguts: "
            "'report' (per defecte, no modifica), "
            "'invert' (inverteix lluminositat HSL), "
            "o '#RRGGBB' (color fix hexadecimal)."
        ),
    )
    parser.add_argument(
        '--verbosity',
        type=int,
        default=1,
        choices=[0, 1, 2],
        metavar='N',
        help=(
            "Nivell de detall del log (per defecte: 1). "
            "0: només errors; 1: errors + avisos + resum; 2: tot (una línia per fitxer)."
        ),
    )
    args = parser.parse_args()

    policy = args.on_unknown_color
    if policy not in ('report', 'invert') and not _HEX_RE.match(policy):
        print(
            f'[gen-dark] ERROR: `--on-unknown-color` ha de ser `report`, `invert` '
            f'o un color hexadecimal `#RRGGBB`. Valor rebut: {policy!r}',
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        input_regex = re.compile(args.regex_entrada)
    except re.error as exc:
        print(
            f'[gen-dark] ERROR: regex invàlida {args.regex_entrada!r}: {exc}',
            file=sys.stderr,
        )
        sys.exit(1)

    generate_dark_svgs(
        input_regex=input_regex,
        specs_file=args.specs_file,
        output_dir=args.output_dir,
        unknown_color_policy=policy,
        verbosity=args.verbosity,
    )
