#!/usr/bin/env python3
"""
norm_font.py
====================
Normalitza les fonts dels fitxers SVG del projecte EC que coincideixen amb la
regex d'entrada, desant el resultat amb el sufix especificat.

Ús
--
    python3 25_scripts/norm_font.py <specs_file> <regex_entrada> <sufix_sortida> [opcions]

Arguments posicionals
---------------------
specs_file      Fitxer 24_specs/svg.md amb el bloc #svg-font-map.
regex_entrada   Expressió regular aplicada sobre rutes relatives al CWD.
                Exemple: "figs_externes/[^/]+[.]svg"
sufix_sortida   Sufix que s'afegeix al nom base del fitxer de sortida.
                Exemple: __extern_light  +  T2_fig.svg  ⇒  T2_fig__extern_light.svg

Arguments opcionals
-------------------
--output-dir    Directori on es desen els fitxers de sortida (per defecte: .).
                La sortida és plana: no es preserva l'estructura de subdirectoris.
                Exemple: --output-dir="auto_figs/"
--on-unknown-font `report`|`normalize`
                Comportament davant fonts no reconegudes:
                  `report`     (per defecte) Reporta i no modifica.
                  `normalize`  Substitueix per la font SANS estàndard del projecte.
--verbosity 0|1|2
                Nivell de detall del log (per defecte: 1).
                  0  Només errors i resum final.
                  1  Errors + avisos (fonts desconegudes) + resum.
                  2  Tot l'anterior + una línia per fitxer processat.

La configuració de fonts és la font de veritat única definida a
24_specs/svg.md, dins el bloc etiquetat `#svg-font-map`. Per afegir suport
a noves fonts, editeu només aquell bloc i torneu a executar l'script.
"""

import ast
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Càrrega del FONT_MAP i KNOWN_NORMALIZED des de 24_specs/svg.md
# ---------------------------------------------------------------------------

def _load_font_config(specs_file: Path) -> tuple[dict[str, str], frozenset[str], str]:
    """
    Extreu FONT_MAP, KNOWN_NORMALIZED i SANS del bloc `{.python #svg-font-map}`
    de 24_specs/svg.md. Retorna (font_map_normalitzat, known_normalized, sans_default).

    Llança ValueError si el bloc no es troba o no es pot avaluar.
    """
    content = specs_file.read_text(encoding='utf-8')

    pattern = re.compile(
        r'```\{\.python\s+#svg-font-map\}(.*?)```',
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        raise ValueError(
            f"Bloc '#svg-font-map' no trobat a {specs_file}.\n"
            "Afegiu un bloc ```{.python #svg-font-map} amb FONT_MAP i KNOWN_NORMALIZED."
        )

    block = match.group(1).strip()

    try:
        tree = ast.parse(block, mode='exec')
    except SyntaxError as exc:
        raise ValueError(f"Error de sintaxi al bloc #svg-font-map: {exc}") from exc

    namespace: dict = {}
    try:
        exec(compile(tree, '<svg-font-map>', 'exec'), namespace)  # noqa: S102
    except Exception as exc:
        raise ValueError(f"Error avaluant el bloc #svg-font-map: {exc}") from exc

    font_map = namespace.get('FONT_MAP')
    known = namespace.get('KNOWN_NORMALIZED')
    sans = namespace.get('SANS', '')

    if not isinstance(font_map, dict):
        raise ValueError("FONT_MAP ha de ser un dict al bloc #svg-font-map.")
    if not isinstance(known, (set, frozenset)):
        raise ValueError("KNOWN_NORMALIZED ha de ser un set al bloc #svg-font-map.")

    def norm(v: str) -> str:
        return re.sub(r'\s+', ' ', v.strip().lower())

    normalized_map = {norm(k): v for k, v in font_map.items()}
    normalized_known = frozenset(norm(v) for v in known)

    return normalized_map, normalized_known, sans


# ---------------------------------------------------------------------------
# Processament d'un SVG
# ---------------------------------------------------------------------------

def _normalize(val: str) -> str:
    return re.sub(r'\s+', ' ', val.strip().lower())


def _process_svg(
    content: str,
    font_map: dict[str, str],
    known_normalized: frozenset[str],
) -> tuple[str, dict[str, int], list[str]]:
    """
    Substitueix els valors de font-family al contingut SVG.
    Retorna (nou_contingut, {font_original: recompte}, fonts_desconegudes).
    """
    counts: dict[str, int] = {}
    unknown: list[str] = []

    def _replace_attr(m: re.Match) -> str:
        outer_quote, val = m.group(1), m.group(2)
        key = _normalize(val)
        if key in font_map:
            counts[val] = counts.get(val, 0) + 1
            return f'font-family={outer_quote}{font_map[key]}{outer_quote}'
        if key not in known_normalized:
            unknown.append(val)
        return m.group(0)

    def _replace_style(m: re.Match) -> str:
        val = m.group(1).strip()
        key = _normalize(val)
        if key in font_map:
            label = f'(style) {val}'
            counts[label] = counts.get(label, 0) + 1
            return f'font-family:{font_map[key]}'
        if key not in known_normalized:
            unknown.append(val)
        return m.group(0)

    new_content = re.sub(
        r"font-family=([\"'])([^\"']*(?:'[^\"']*'[^\"']*)*)\1",
        _replace_attr, content,
    )
    new_content = re.sub(
        r"font-family:\s*([^;{}<>\"']+)",
        _replace_style, new_content,
    )

    return new_content, counts, list(dict.fromkeys(unknown))


# ---------------------------------------------------------------------------
# Lògica principal
# ---------------------------------------------------------------------------

def migrate_fonts(
    input_regex: re.Pattern,
    output_suffix: str,
    specs_file: Path,
    output_dir: Path,
    unknown_font_policy: str = 'report',
    verbosity: int = 1,
) -> None:

    # Càrrega de la configuració des de 24_specs/svg.md
    try:
        font_map, known_normalized, sans_default = _load_font_config(specs_file)
    except ValueError as exc:
        print(f'[norm-font] ERROR carregant configuració: {exc}', file=sys.stderr)
        sys.exit(1)

    if verbosity >= 2:
        print(
            f'[norm-font] Configuració carregada des de {specs_file} '
            f'({len(font_map)} substitucions, {len(known_normalized)} fonts acceptades)'
        )
        print('[norm-font] Fonts que es substituiran:')
        for orig, dest in sorted(font_map.items()):
            print(f'  {orig!r}  \u2192  {dest!r}')
        print('[norm-font] Fonts acceptades sense substitució:')
        for f in sorted(known_normalized):
            print(f'  {f!r}')
        if unknown_font_policy != 'report':
            default_font = sans_default or '(SANS no definit)'
            print(f'[norm-font] Política `--on-unknown-font normalize`: substituir per {default_font!r}')

    output_dir.mkdir(parents=True, exist_ok=True)

    # Troba tots els fitxers SVG que coincideixen amb la regex
    root = Path.cwd()
    input_files = sorted(
        p for p in root.rglob('*.svg')
        if input_regex.search(str(p.relative_to(root)))
    )

    if not input_files:
        if verbosity >= 1:
            print(
                f'[norm-font] Cap fitxer trobat per la regex '
                f'{input_regex.pattern!r}'
            )
        return

    written = written_sub = errors = 0
    unknown_report: dict[str, list[str]] = {}

    for svg_path in input_files:
        rel_path = str(svg_path.relative_to(root))
        stem = svg_path.stem
        out_path = output_dir / f'{stem}{output_suffix}.svg'

        try:
            original = svg_path.read_text(encoding='utf-8')
            new_content, counts, unknowns = _process_svg(
                original, font_map, known_normalized
            )

            for uf in unknowns:
                unknown_report.setdefault(uf, []).append(rel_path)

            # Aplica política per a fonts desconegudes
            if unknown_font_policy == 'normalize' and unknowns and sans_default:
                for uf in unknowns:
                    new_content = new_content.replace(uf, sans_default)
                    new_content = re.sub(
                        re.escape(uf), sans_default, new_content, flags=re.IGNORECASE
                    )

            # Sempre escriu el fitxer de sortida (gen_dark.py necessita tots els _light)
            out_path.write_text(new_content, encoding='utf-8')
            if counts or (unknown_font_policy == 'normalize' and unknowns):
                written_sub += 1
                if verbosity >= 2:
                    detail = ', '.join(f'{n}× {f!r}' for f, n in counts.items())
                    print(f'[norm-font] GENERAT (sub)  {out_path}  [{detail}]')
            else:
                written += 1
                if verbosity >= 2:
                    print(f'[norm-font] GENERAT        {out_path}')

        except Exception as exc:  # noqa: BLE001
            print(f'[norm-font] ERROR {rel_path}: {exc}', file=sys.stderr)
            errors += 1

    if verbosity >= 1:
        print(
            f'[norm-font] Resum: {written_sub} generats amb substitució, '
            f'{written} generats sense canvi de font, {errors} errors.'
        )

    if unknown_report:
        if verbosity >= 1:
            if unknown_font_policy == 'report':
                print(
                    '\n[norm-font] AVÍS — fonts desconegudes '
                    '(no modificades per política `--on-unknown-font report`):'
                )
            else:
                print(
                    '\n[norm-font] AVÍS — fonts desconegudes '
                    f'(substituïdes per `--on-unknown-font normalize` → {sans_default!r}):'
                )
            for font, files in sorted(unknown_report.items()):
                print(f'  Font: {font!r}')
                for fn in sorted(files):
                    print(f'    {fn}')
            if unknown_font_policy == 'report':
                print(
                    '\n[norm-font] Per resoldre les fonts desconegudes: corregiu la font '
                    "al fitxer SVG original, o useu `--on-unknown-font normalize` per substituir-les "
                    'per la font SANS estàndard del projecte.'
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
            "Normalitza les fonts dels fitxers SVG del projecte EC "
            "que coincideixen amb la regex d'entrada."
        )
    )
    parser.add_argument(
        'specs_file',
        type=Path,
        metavar='specs_file',
        help="Fitxer 24_specs/svg.md amb el bloc #svg-font-map.",
    )
    parser.add_argument(
        'regex_entrada',
        metavar='regex_entrada',
        help=(
            "Expressió regular aplicada sobre rutes relatives al CWD. "
            "Exemple: \"figs_externes/[^/]+[.]svg\""
        ),
    )
    parser.add_argument(
        'sufix_sortida',
        metavar='sufix_sortida',
        help=(
            "Sufix afegit al nom base del fitxer de sortida. "
            "Exemple: __extern_light  +  T2_fig.svg  ⇒  T2_fig__extern_light.svg"
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
        '--on-unknown-font',
        default='report',
        metavar='POLÍTICA',
        choices=['report', 'normalize'],
        help=(
            'Comportament davant fonts no reconegudes: '
            '\'report\' (per defecte, no modifica) o '
            '\'normalize\' (substitueix per la font SANS estàndard del projecte).'
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

    try:
        input_regex = re.compile(args.regex_entrada)
    except re.error as exc:
        print(
            f'[norm-font] ERROR: regex invàlida {args.regex_entrada!r}: {exc}',
            file=sys.stderr,
        )
        sys.exit(1)

    migrate_fonts(
        input_regex=input_regex,
        output_suffix=args.sufix_sortida,
        specs_file=args.specs_file,
        output_dir=args.output_dir,
        unknown_font_policy=args.on_unknown_font,
        verbosity=args.verbosity,
    )
