#!/usr/bin/env python3
"""
gen_regs.py — Generador de figures SVG de registres de bits per al projecte EC.

Ús com a pre-render de Quarto (_quarto.yml):
    project:
      pre-render:
        - scripts/gen_regs.py  specs/registres.toml "__registre_light" --output-dir="figs_auto/"
        - scripts/gen_dark.py  specs/svg.md "figs_auto/[^/]+_light[.]svg" --output-dir="figs_auto/"

Ús manual:
    python3 22_scripts/gen_regs.py <specs_file> <output_sufix> [--output-dir DIR] [--force] [--verbosity N]

Arguments posicionals:
    specs_file      Fitxer de definicions de registres (p. ex. specs/registres.toml).
    output_sufix    Sufix afegit al nom base de cada fitxer de sortida.
                    Exemple: __registre_light  →  T2_instruccio_tipus_R__registre_light.svg

Arguments opcionals:
    --output-dir    Directori on es desen els SVG generats (per defecte: figs_auto/).
    --force         Regenera tots els SVG ignorant timestamps.
    --verbosity 0|1|2
                    Nivell de detall del log (per defecte: 1).
                      0  Només errors i resum final.
                      1  Errors + resum.
                      2  Tot l'anterior + una línia per fitxer processat.

No modifiqueu les definicions de registres aquí: editeu specs/registres.toml.
"""

import tomllib
import sys
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# Paleta i constants de dibuix
# ═══════════════════════════════════════════════════════════

COLORS = {
    'R': {'fill': '#f8f9fa', 'stroke': '#adb5bd', 'text': '#6c757d'},
    'B': {'fill': '#cfe2ff', 'stroke': '#084298', 'text': '#084298'},
    'G': {'fill': '#d1e7dd', 'stroke': '#0a3622', 'text': '#0a3622'},
    'A': {'fill': '#fff3cd', 'stroke': '#664d03', 'text': '#664d03'},
    'V': {'fill': '#f8d7da', 'stroke': '#842029', 'text': '#842029'},
}

FONT_SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
FONT_MONO = "'Liberation Mono', 'Courier New', Courier, monospace"

PX_PER_BIT  = 22
ROW_H       = 44
BIT_NUM_H   = 16
TICK_H      = 5
MARGIN_L    = 2
MARGIN_R    = 2
TEXT_MARGIN = 0.01

FONT_SIZE_BASE      = 12
FONT_SIZE_BASE_VERT = 11
CHAR_W_PER_FS       = 0.60
CHAR_H_PER_FS       = 1.20


# ═══════════════════════════════════════════════════════════
# Càlcul de font-size (criteri de marges)
# ═══════════════════════════════════════════════════════════

def _fs_horizontal(name: str, field_w_px: float) -> float:
    avail = field_w_px * (1.0 - TEXT_MARGIN)
    return min(avail / (max(len(name), 1) * CHAR_W_PER_FS), FONT_SIZE_BASE)


def _fs_vertical(name: str, field_h_px: float) -> float:
    avail = field_h_px * (1.0 - TEXT_MARGIN)
    return min(avail / (max(len(name), 1) * CHAR_H_PER_FS), FONT_SIZE_BASE_VERT)


# ═══════════════════════════════════════════════════════════
# Generació SVG
# ═══════════════════════════════════════════════════════════

def _canvas_w(total_bits: int) -> int:
    return MARGIN_L + total_bits * PX_PER_BIT + MARGIN_R


def _generate_row(fields, row_y: int, total_bits: int, bit_msb_of_row: int) -> str:
    lines = []
    box_y = row_y + BIT_NUM_H
    box_h = ROW_H
    bits_from_left = 0

    for name, nbits, ckey in fields:
        c   = COLORS[ckey]
        x0  = MARGIN_L + bits_from_left * PX_PER_BIT
        w   = nbits * PX_PER_BIT
        xm  = x0 + w / 2
        ym  = box_y + box_h / 2
        bit_msb = bit_msb_of_row - bits_from_left
        bit_lsb = bit_msb - nbits + 1

        lines.append(
            f'<rect x="{x0}" y="{box_y}" width="{w}" height="{box_h}" '
            f'fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="1"/>'
        )

        for i in range(1, nbits):
            tx = x0 + i * PX_PER_BIT
            lines.append(
                f'<line x1="{tx}" y1="{box_y}" x2="{tx}" y2="{box_y + TICK_H}" '
                f'stroke="{c["stroke"]}" stroke-width="0.75"/>'
            )
            lines.append(
                f'<line x1="{tx}" y1="{box_y + box_h}" '
                f'x2="{tx}" y2="{box_y + box_h - TICK_H}" '
                f'stroke="{c["stroke"]}" stroke-width="0.75"/>'
            )

        lines.append(
            f'<text x="{x0 + 1}" y="{row_y + BIT_NUM_H - 3}" '
            f'font-family="{FONT_MONO}" font-size="10" fill="#6c757d" '
            f'text-anchor="start">{bit_msb}</text>'
        )
        if bit_lsb != bit_msb:
            lines.append(
                f'<text x="{x0 + w - 1}" y="{row_y + BIT_NUM_H - 3}" '
                f'font-family="{FONT_MONO}" font-size="10" fill="#6c757d" '
                f'text-anchor="end">{bit_lsb}</text>'
            )

        fs_h = _fs_horizontal(name, w)
        fs_v = _fs_vertical(name, box_h)
        use_vertical = (nbits == 1) or (fs_h < fs_v)

        if use_vertical:
            fs = round(fs_v, 2)
            lines.append(
                f'<text transform="rotate(-90,{xm},{ym})" '
                f'x="{xm}" y="{ym}" '
                f'font-family="{FONT_SANS}" font-size="{fs}" fill="{c["text"]}" '
                f'text-anchor="middle" dominant-baseline="middle">{name}</text>'
            )
        else:
            fs = round(fs_h, 2)
            lines.append(
                f'<text x="{xm}" y="{ym}" '
                f'font-family="{FONT_SANS}" font-size="{fs}" fill="{c["text"]}" '
                f'text-anchor="middle" dominant-baseline="middle">{name}</text>'
            )

        bits_from_left += nbits

    return '\n'.join(lines)


def make_svg(fname: str, rows_data: list, title_ca: str, desc_ca: str) -> str:
    total_bits = sum(nb for _, nb, _ in rows_data[0][0])
    n_rows     = len(rows_data)
    cw         = _canvas_w(total_bits)
    total_h    = n_rows * (ROW_H + BIT_NUM_H) + 4

    lines = [
        f'<svg width="100%" viewBox="0 0 {cw} {total_h}" '
        f'xmlns="http://www.w3.org/2000/svg" role="img">',
        f'<title>{title_ca}</title>',
        f'<desc>{desc_ca}</desc>',
    ]
    for idx, (fields, bit_msb) in enumerate(rows_data):
        row_y = idx * (ROW_H + BIT_NUM_H)
        lines.append(_generate_row(fields, row_y, total_bits, bit_msb))
    lines.append('</svg>')
    return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════
# Càrrega de registres.toml
# ═══════════════════════════════════════════════════════════

def _load_registers(specs_path: Path) -> dict:
    if not specs_path.exists():
        print(f'[gen-regs] ERROR: no es troba {specs_path}', file=sys.stderr)
        sys.exit(1)
    try:
        with open(specs_path, 'rb') as f:
            data = tomllib.load(f)
    except tomllib.TOMLDecodeError as exc:
        print(f'[gen-regs] ERROR parsejant {specs_path}: {exc}', file=sys.stderr)
        sys.exit(1)

    if 'registers' not in data:
        print(
            f'[gen-regs] ERROR: {specs_path} no conté la secció [registers].',
            file=sys.stderr,
        )
        sys.exit(1)

    registers = {}
    for fname, spec in data['registers'].items():
        rows = []
        for row in spec['rows']:
            fields = [tuple(f) for f in row['fields']]
            rows.append((fields, row['bit_msb']))
        registers[fname] = {
            'rows':  rows,
            'title': spec['title'],
            'desc':  spec['desc'],
        }
    return registers


# ═══════════════════════════════════════════════════════════
# Validació
# ═══════════════════════════════════════════════════════════

def _validate(registers: dict) -> list[str]:
    errors = []
    for fname, spec in registers.items():
        for row_idx, (fields, bit_msb) in enumerate(spec['rows']):
            total    = sum(nb for _, nb, _ in fields)
            expected = bit_msb + 1
            if total != expected:
                errors.append(
                    f'  {fname} fila {row_idx}: {total} bits \u2260 {expected} '
                    f'esperats (MSB={bit_msb})'
                )
    return errors


# ═══════════════════════════════════════════════════════════
# Preview HTML
# ═══════════════════════════════════════════════════════════

def make_preview(registers: dict, out_dir: Path, output_suffix: str, preview_path: Path) -> None:
    """Genera docs/preview_regs.html amb tots els SVG incrustats inline."""
    palette_chips = [
        ('#f8f9fa', '#adb5bd', '#6c757d', 'Reservat/WPRI'),
        ('#cfe2ff', '#084298', '#084298', 'Blau · habilitació'),
        ('#d1e7dd', '#0a3622', '#0a3622', 'Verd · mode/control'),
        ('#fff3cd', '#664d03', '#664d03', 'Ambre · adreça/codi'),
        ('#f8d7da', '#842029', '#842029', 'Vermell · CF/estat'),
    ]
    chips_html = '\n  '.join(
        f'<span class="chip" style="background:{bg};border-color:{bd};color:{tc}">'
        f'{label}</span>'
        for bg, bd, tc, label in palette_chips
    )

    blocks = []
    for fname, spec in registers.items():
        svg_path = out_dir / (fname + output_suffix + '.svg')
        if not svg_path.exists():
            continue
        svg_content = svg_path.read_text(encoding='utf-8')
        blocks.append(
            f'<div class="fig-block">'
            f'<div class="fig-header">'
            f'<p class="fig-title">{spec["title"]}</p>'
            f'<p class="fig-name">{fname}{output_suffix}.svg</p>'
            f'</div>'
            f'{svg_content}'
            f'</div>'
        )

    html = f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview registres EC</title>
<style>
  body {{ font-family: 'Liberation Sans', Arial, sans-serif; background: #f8f9fa;
         max-width: 860px; margin: 0 auto; padding: 24px; }}
  h1 {{ font-size: 16px; color: #343a40; }}
  .meta {{ font-size: 12px; color: #6c757d; margin: 4px 0 20px; }}
  .palette {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 28px; }}
  .chip {{ padding: 3px 9px; border-radius: 4px; font-size: 11px; border: 1px solid; }}
  .fig-block {{ background: white; border: 1px solid #dee2e6; border-radius: 6px;
               padding: 14px 14px 10px; margin-bottom: 18px; }}
  .fig-header {{ display: flex; justify-content: space-between; align-items: baseline;
                margin: 0 0 10px; gap: 16px; }}
  .fig-title {{ font-size: 13px; color: #212529; margin: 0; flex: 1; }}
  .fig-name  {{ font-size: 11px; color: #6c757d; font-family: monospace;
               white-space: nowrap; margin: 0; }}
  svg {{ display: block; width: 100%; }}
</style>
</head>
<body>
<h1>Preview registres EC — mode clar</h1>
<p class="meta">22 px/bit · ticks per bit · marge 1% · figs_auto/</p>
<div class="palette">
  {chips_html}
</div>
{''.join(blocks)}
</body>
</html>"""

    preview_path.parent.mkdir(exist_ok=True)
    preview_path.write_text(html, encoding='utf-8')
    print(f'[gen-regs] PREVIEW  {preview_path}')


# ═══════════════════════════════════════════════════════════
# Punt d'entrada
# ═══════════════════════════════════════════════════════════

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description='Genera els SVG de registres de bits per al projecte EC.'
    )
    parser.add_argument(
        'specs_file',
        type=Path,
        help='Fitxer de definicions (p. ex. specs/registres.toml)',
    )
    parser.add_argument(
        'output_sufix',
        help=(
            "Sufix afegit al nom base de cada fitxer de sortida. "
            "Exemple: __registre_light  →  T2_instruccio_tipus_R__registre_light.svg"
        ),
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('figs_auto'),
        metavar='DIR',
        help='Directori de sortida (per defecte: figs_auto/).',
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Regenera tots els SVG ignorant timestamps.',
    )
    parser.add_argument(
        '--verbosity',
        type=int,
        default=1,
        choices=[0, 1, 2],
        metavar='N',
        help=(
            "Nivell de detall del log (per defecte: 1). "
            "0: només errors; 1: errors + resum; 2: tot (una línia per fitxer)."
        ),
    )
    args = parser.parse_args()

    specs_path    = args.specs_file
    output_suffix = args.output_sufix
    output_dir    = args.output_dir
    verbosity     = args.verbosity

    registers = _load_registers(specs_path)

    errors_val = _validate(registers)
    if errors_val:
        print('[gen-regs] ERRORS DE VALIDACIÓ:', file=sys.stderr)
        for e in errors_val:
            print(e, file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    preview_path = Path.cwd() / 'docs' / 'preview_regs.html'
    script_mtime = Path(__file__).stat().st_mtime

    generated = skipped = errors = 0
    for fname, spec in registers.items():
        out_path = output_dir / (fname + output_suffix + '.svg')

        if not args.force and out_path.exists():
            if out_path.stat().st_mtime > script_mtime:
                if verbosity >= 2:
                    print(f'[gen-regs] SALTA (vigent)  {out_path.name}')
                skipped += 1
                continue

        try:
            svg = make_svg(fname, spec['rows'], spec['title'], spec['desc'])
            out_path.write_text(svg, encoding='utf-8')
            generated += 1
            if verbosity >= 2:
                print(f'[gen-regs] GENERAT  {out_path.name}')
        except Exception as exc:  # noqa: BLE001
            print(f'[gen-regs] ERROR {out_path.name}: {exc}', file=sys.stderr)
            errors += 1

    make_preview(registers, output_dir, output_suffix, preview_path)

    if verbosity >= 1:
        print(
            f'[gen-regs] Resum: {generated} generats, {skipped} vigents, {errors} errors. '
            f'Directori: {output_dir}'
        )

    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
