#!/usr/bin/env python3
"""
gen_crops.py — Generador de retalls (crops) SVG a partir d'una figura font única.

Motivació
---------
Quan una figura "detall" o "zoom" mostra literalment un subconjunt visual
d'una figura "global" ja existent (mateixes coordenades, mateix contingut,
sense redibuixar ni afegir informació nova), mantenir dos fitxers SVG
independents és una font de veritat duplicada: qualsevol canvi a la figura
global s'ha de repetir manualment al retall, i és fàcil que es desincronitzin.

Aquest script permet definir el retall com una simple finestra
(min-x, min-y, width, height) sobre el `viewBox` d'un SVG font ja existent.
El contingut intern del SVG no es toca: només es reescriuen `viewBox`,
`width` i `height` de l'element arrel. La font de veritat continua sent
un sol fitxer.

**Nota important:** això només és aplicable quan el retall és geomètricament
un subconjunt net de la figura font (cap element tallat a mig camí que calgui
amagar, cap etiqueta que quedi "penjant" sense el element que assenyalava).
Si el "zoom" necessita mostrar contingut que no hi és a la figura font
(més etiquetes, més detall, redisseny), continua calent un SVG independent.

Ús com a pas de pre-render de Quarto (_quarto.yml), després de norm_font.py
i abans de gen_dark.py:
    project:
      pre-render:
        - 25_scripts/norm_font.py 24_specs/svg.md "22_figs_originals/[^/]+[.]svg" "__original_light" --output-dir="auto_figs/"
        - 25_scripts/gen_crops.py 24_specs/retalls.toml "auto_figs/" --output-dir="auto_figs/"
        - 25_scripts/gen_dark.py  24_specs/svg.md "auto_figs/[^/]+_light[.]svg" --output-dir="auto_figs/"

Ús manual:
    python3 25_scripts/gen_crops.py <specs_file> <source_dir> [--output-dir DIR] [--force] [--verbosity N]

Arguments posicionals
---------------------
specs_file      Fitxer de definicions de retalls (p. ex. 24_specs/retalls.toml).
source_dir      Directori on cercar els SVG font (p. ex. auto_figs/, ja amb
                les fonts normalitzades per norm_font.py).

Arguments opcionals
--------------------
--output-dir    Directori on es desen els SVG retallats (per defecte: .).
--force         Regenera tots els retalls ignorant timestamps.
--verbosity 0|1|2
                0  Només errors i resum final.
                1  Errors + avisos + resum (per defecte).
                2  Tot l'anterior + una línia per fitxer processat.

Format de 24_specs/retalls.toml
--------------------------------
    [crops.nom_fitxer_sortida_sense_extensio]
    source = "nom_fitxer_font_sense_extensio__original_light"  # ha d'existir a source_dir
    title  = "Títol descriptiu del retall (opcional; si no es dona, es reutilitza el <title> de la font)"
    x      = 54     # min-x del retall, en coordenades del viewBox de la font
    y      = 60     # min-y del retall
    w      = 300    # amplada del retall
    h      = 250    # alçada del retall

No modifiqueu les definicions aquí: editeu 24_specs/retalls.toml.
"""

import re
import sys
import tomllib
from pathlib import Path


# ═══════════════════════════════════════════════════════════
# Càrrega de les especificacions
# ═══════════════════════════════════════════════════════════

def _load_crops(specs_file: Path) -> dict:
    if not specs_file.exists():
        return {}
    with specs_file.open('rb') as f:
        data = tomllib.load(f)
    return data.get('crops', {})


# ═══════════════════════════════════════════════════════════
# Validació
# ═══════════════════════════════════════════════════════════

def _validate(crops: dict, source_dir: Path) -> list[str]:
    errors = []
    for name, spec in crops.items():
        for key in ('source', 'x', 'y', 'w', 'h'):
            if key not in spec:
                errors.append(f'  {name}: falta la clau obligatòria "{key}"')
        if 'w' in spec and spec['w'] <= 0:
            errors.append(f'  {name}: "w" ha de ser positiu (rebut {spec["w"]})')
        if 'h' in spec and spec['h'] <= 0:
            errors.append(f'  {name}: "h" ha de ser positiu (rebut {spec["h"]})')
        if 'source' in spec:
            src_path = source_dir / (spec['source'] + '.svg')
            if not src_path.exists():
                errors.append(
                    f'  {name}: fitxer font "{src_path}" no existeix '
                    f'(ha d\'estar ja generat, p. ex. per norm_font.py)'
                )
    return errors


# ═══════════════════════════════════════════════════════════
# Retall d'un SVG
# ═══════════════════════════════════════════════════════════

_SVG_TAG_RE = re.compile(r'<svg\b[^>]*>', re.IGNORECASE)
_VIEWBOX_RE = re.compile(r'viewBox\s*=\s*"[^"]*"', re.IGNORECASE)
_WIDTH_RE = re.compile(r'\bwidth\s*=\s*"[^"]*"', re.IGNORECASE)
_HEIGHT_RE = re.compile(r'\bheight\s*=\s*"[^"]*"', re.IGNORECASE)
_TITLE_RE = re.compile(r'<title>.*?</title>', re.IGNORECASE | re.DOTALL)


def make_crop_svg(source_svg: str, x: float, y: float, w: float, h: float,
                   title: str | None = None) -> str:
    """
    Retorna una còpia de source_svg amb el viewBox/width/height substituïts
    per la finestra de retall (x, y, w, h). No toca cap altre contingut.
    """
    tag_match = _SVG_TAG_RE.search(source_svg)
    if not tag_match:
        raise ValueError('No s\'ha trobat cap element <svg> a la font')

    old_tag = tag_match.group(0)
    new_tag = old_tag

    new_viewbox = f'viewBox="{x:g} {y:g} {w:g} {h:g}"'
    if _VIEWBOX_RE.search(new_tag):
        new_tag = _VIEWBOX_RE.sub(new_viewbox, new_tag)
    else:
        new_tag = new_tag[:-1] + f' {new_viewbox}>'

    if _WIDTH_RE.search(new_tag):
        new_tag = _WIDTH_RE.sub('width="100%"', new_tag)
    else:
        new_tag = new_tag[:-1] + ' width="100%">'

    # L'alçada final (píxels) del retall és proporcional a `h`, no a l'alçada
    # original de la font: es descarta l'atribut height (width="100%" +
    # viewBox ja fixen l'aspect ratio correctament).
    new_tag = _HEIGHT_RE.sub('', new_tag)
    new_tag = re.sub(r'\s{2,}', ' ', new_tag).replace(' >', '>')

    result = source_svg[:tag_match.start()] + new_tag + source_svg[tag_match.end():]

    if title is not None:
        if _TITLE_RE.search(result):
            result = _TITLE_RE.sub(f'<title>{title}</title>', result, count=1)
        else:
            insert_at = result.find('>', result.find('<svg')) + 1
            result = result[:insert_at] + f'\n<title>{title}</title>' + result[insert_at:]

    return result


# ═══════════════════════════════════════════════════════════
# Punt d'entrada
# ═══════════════════════════════════════════════════════════

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description='Genera retalls SVG (crops) a partir de figures font existents.'
    )
    parser.add_argument('specs_file', type=Path,
                         help='Fitxer de definicions (p. ex. 24_specs/retalls.toml)')
    parser.add_argument('source_dir', type=Path,
                         help='Directori on cercar els SVG font')
    parser.add_argument('--output-dir', type=Path, default=Path('.'), metavar='DIR',
                         help='Directori de sortida (per defecte: directori actual).')
    parser.add_argument('--force', action='store_true',
                         help='Regenera tots els retalls ignorant timestamps.')
    parser.add_argument('--verbosity', type=int, default=1, choices=[0, 1, 2], metavar='N',
                         help='0: només errors; 1: errors+avisos+resum; 2: tot.')
    args = parser.parse_args()

    crops = _load_crops(args.specs_file)

    errors_val = _validate(crops, args.source_dir)
    if errors_val:
        print('[gen-crops] ERRORS DE VALIDACIÓ:', file=sys.stderr)
        for e in errors_val:
            print(e, file=sys.stderr)
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    script_mtime = Path(__file__).stat().st_mtime

    generated = skipped = errors = 0
    for name, spec in crops.items():
        src_path = args.source_dir / (spec['source'] + '.svg')
        out_path = args.output_dir / (name + '.svg')

        if not args.force and out_path.exists():
            newest_dep = max(src_path.stat().st_mtime, script_mtime)
            if out_path.stat().st_mtime > newest_dep:
                if args.verbosity >= 2:
                    print(f'[gen-crops] SALTA (vigent)  {out_path.name}')
                skipped += 1
                continue

        try:
            source_svg = src_path.read_text(encoding='utf-8')
            svg = make_crop_svg(
                source_svg,
                x=spec['x'], y=spec['y'], w=spec['w'], h=spec['h'],
                title=spec.get('title'),
            )
            out_path.write_text(svg, encoding='utf-8')
            generated += 1
            if args.verbosity >= 2:
                print(f'[gen-crops] GENERAT  {out_path.name}  (font: {src_path.name})')
        except Exception as exc:  # noqa: BLE001
            print(f'[gen-crops] ERROR {out_path.name}: {exc}', file=sys.stderr)
            errors += 1

    if args.verbosity >= 1:
        print(
            f'[gen-crops] Resum: {generated} generats, {skipped} vigents, {errors} errors. '
            f'Directori: {args.output_dir}'
        )

    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
