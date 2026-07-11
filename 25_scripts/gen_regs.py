#!/usr/bin/env python3
"""
gen_regs.py — Generador de figures SVG de registres de bits per al projecte EC.

Ús com a pre-render de Quarto (_quarto.yml):
    project:
      pre-render:
        - bash -c "rm -rf auto_figs && mkdir auto_figs"
        - 25_scripts/norm_font.py 24_specs/svg.md "22_figs_originals/[^/]+[.]svg" "__original_light" --output-dir="auto_figs/"
        - 25_scripts/norm_font.py 24_specs/svg.md "23_figs_externes/[^/]+[.]svg"  "__extern_light"   --output-dir="auto_figs/"
        - 25_scripts/gen_regs.py  24_specs/registres.toml                         "__registre_light" --output-dir="auto_figs/"
        - 25_scripts/gen_dark.py  24_specs/svg.md "auto_figs/[^/]+_light[.]svg"                      --output-dir="auto_figs/"

Ús manual:
    python3 25_scripts/gen_regs.py <specs_file> <output_sufix> [--output-dir DIR] [--force] [--preview] [--verbosity N]

Arguments posicionals:
    specs_file      Fitxer de definicions de registres (p. ex. 24_specs/registres.toml).
    output_sufix    Sufix afegit al nom base de cada fitxer de sortida.
                    Exemple: __registre_light  ⇒  T2_instruccio_tipus_R__registre_light.svg

Arguments opcionals:
    --output-dir    Directori on es desen els SVG generats (per defecte: auto_figs/).
                    La sortida és plana: no es preserva l'estructura de subdirectoris.
    --force         Regenera tots els SVG ignorant timestamps.
    --preview       Genera preview_regs.html (a --output-dir) amb tots els SVG incrustats inline.
    --verbosity 0|1|2
                    Nivell de detall del log (per defecte: 1).
                      0  Només errors i resum final.
                      1  Errors + avisos + resum.
                      2  Tot l'anterior + una línia per fitxer processat.

No modifiqueu les definicions de registres aquí: editeu 24_specs/registres.toml.
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
# Constants i helpers per a formats d'instrucció
# ═══════════════════════════════════════════════════════════

# Patró per detectar entrades de formats d'instrucció al TOML
INSTRUCCIO_PREFIX = 'instruccio_tipus_'

# Ordre canònic per al compendi (sufixos després del prefix)
INSTRUCCIO_ORDER = ['R', 'I', 'S', 'B', 'U', 'J', 'R4']

# Nom del fitxer de sortida del compendi (sense sufix ni extensió)
COMPENDI_FNAME = 'compendi_registres'

# Geometria pròpia dels formats d'instrucció
INS_W_TOTAL  = 680
INS_MARGIN_R = 8
INS_LABEL_W  = 58    # amplada columna etiqueta "X-Type" (figura combinada)
INS_ROW_H    = 26
INS_BIT_H    = 14
INS_BITS_ROW = 14    # alçada fila de bits inferiors
INS_TICK_H   = 4
INS_FONT     = "'Liberation Sans', Arial, Helvetica, sans-serif"

# Paleta per a formats d'instrucció (mapatge de claus TOML → colors)
# Reutilitza COLORS però amb les claus existents:
# G=opcode (verd), B=rd/rs/fd/fs (blau), A=funct/imm (ambre)
INS_COLORS = COLORS  # reutilitza la mateixa taula


def _ins_bit_w(label_w: float = 0) -> float:
    """Amplada per bit en funció de l'espai disponible."""
    return (INS_W_TOTAL - label_w - INS_MARGIN_R) / 32


def _ins_bit_x(bit: int, bw: float) -> float:
    return (31 - bit) * bw


def _ins_field_cx(hi: int, lo: int, bw: float) -> float:
    return (_ins_bit_x(hi, bw) + _ins_bit_x(lo, bw) + bw) / 2


def _ins_field_w(hi: int, lo: int, bw: float) -> float:
    return (hi - lo + 1) * bw


def _ins_bits_label(n: int, fw: float) -> str:
    """Etiqueta de nombre de bits si hi cap."""
    if n <= 1:
        return ""
    full, short = f"{n} bits", f"{n}b"
    if fw >= len(full)  * 6.5: return full
    if fw >= len(short) * 6.5: return short
    return ""


def _ins_ticks(y_top: float, y_bot: float, bw: float) -> list[str]:
    """33 ticks cap a l'interior del rectangle (31 interns + 2 extrems)."""
    lines = []
    for i in range(33):
        x = i * bw
        lines.append(
            f'<line x1="{x:.2f}" y1="{y_top:.2f}" '
            f'x2="{x:.2f}" y2="{y_top + INS_TICK_H:.2f}" '
            f'stroke="{COLORS["R"]["stroke"]}" stroke-width="0.5"/>'
        )
        lines.append(
            f'<line x1="{x:.2f}" y1="{y_bot:.2f}" '
            f'x2="{x:.2f}" y2="{y_bot - INS_TICK_H:.2f}" '
            f'stroke="{COLORS["R"]["stroke"]}" stroke-width="0.5"/>'
        )
    return lines


def _ins_bit_numbers(fields: list, y: float, bw: float) -> list[str]:
    """Etiquetes numèriques als extrems de cada camp."""
    shown: set[int] = set()
    for _, nbits, _ in fields:
        pass  # calculem hi/lo a continuació
    # reconstruïm hi/lo a partir de nbits
    bit = 31
    shown = set()
    for _, nbits, _ in fields:
        hi = bit
        lo = bit - nbits + 1
        shown.add(hi)
        shown.add(lo)
        bit -= nbits

    lines = []
    for b in sorted(shown, reverse=True):
        if b == 31:
            anchor, x = "start", _ins_bit_x(31, bw)
        elif b == 0:
            anchor, x = "end", _ins_bit_x(0, bw) + bw
        else:
            anchor, x = "middle", _ins_bit_x(b, bw) + bw
        lines.append(
            f'<text x="{x:.2f}" y="{y:.1f}" '
            f'font-family="{INS_FONT}" font-size="9" '
            f'text-anchor="{anchor}" dominant-baseline="auto" '
            f'fill="{COLORS["R"]["text"]}">{b}</text>'
        )
    return lines


def _ins_fields_with_bits(fields: list) -> list[tuple]:
    """Converteix llista de (nom, nbits, ckey) en (nom, hi, lo, ckey)."""
    result = []
    bit = 31
    for name, nbits, ckey in fields:
        hi = bit
        lo = bit - nbits + 1
        result.append((name, hi, lo, ckey))
        bit -= nbits
    return result


def _ins_type_label(fname: str) -> str:
    """Extreu l'etiqueta de tipus ('R', 'I', ..., 'R4') del nom de fitxer."""
    idx = fname.find(INSTRUCCIO_PREFIX)
    if idx == -1:
        return ''
    suffix = fname[idx + len(INSTRUCCIO_PREFIX):]
    # elimina prefix de tema (T2_, T3_, T5_) si n'hi ha
    # el suffix ja és el tipus (R, I, S, B, U, J, R4)
    return suffix


def _is_instruccio(fname: str) -> bool:
    return INSTRUCCIO_PREFIX in fname


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
# Generació SVG per a formats d'instrucció (figura individual)
# ═══════════════════════════════════════════════════════════

def make_svg_instruccio(fname: str, fields_raw: list, title_ca: str, desc_ca: str) -> str:
    """
    Genera el SVG d'un format d'instrucció individual.
    Geometria: 680px, bits dalt, rectangle amb ticks, bits inferiors sota.
    """
    bw     = _ins_bit_w()
    fields = _ins_fields_with_bits(fields_raw)
    H      = INS_BIT_H + INS_ROW_H + INS_BITS_ROW + 6
    y_row  = INS_BIT_H + 2
    y_bot  = y_row + INS_ROW_H + 2

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{INS_W_TOTAL}" height="{H}" '
        f'viewBox="0 0 {INS_W_TOTAL} {H}" role="img">',
        f'<title>{title_ca}</title>',
        f'<desc>{desc_ca}</desc>',
    ]

    # Rectangles i noms de camp
    for name, hi, lo, ckey in fields:
        c   = INS_COLORS[ckey]
        x   = _ins_bit_x(hi, bw)
        w   = _ins_field_w(hi, lo, bw)
        cx  = _ins_field_cx(hi, lo, bw)
        cy  = y_row + INS_ROW_H / 2
        sw  = "1" if ckey != 'R' else "0.5"
        lines.append(
            f'<rect x="{x:.2f}" y="{y_row}" width="{w:.2f}" height="{INS_ROW_H}" '
            f'fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="{sw}"/>'
        )
        lines.append(
            f'<text x="{cx:.2f}" y="{cy:.1f}" '
            f'font-family="{INS_FONT}" font-size="11" '
            f'text-anchor="middle" dominant-baseline="middle" '
            f'fill="{c["text"]}">{name}</text>'
        )

    # Ticks (cap a l'interior)
    lines += _ins_ticks(y_row, y_row + INS_ROW_H, bw)

    # Numeració de bits superior
    lines += _ins_bit_numbers(fields_raw, INS_BIT_H - 2, bw)

    # Bits inferiors (nombre de bits de cada camp)
    for name, hi, lo, ckey in fields:
        n  = hi - lo + 1
        fw = _ins_field_w(hi, lo, bw)
        cx = _ins_field_cx(hi, lo, bw)
        bl = _ins_bits_label(n, fw)
        if bl:
            lines.append(
                f'<text x="{cx:.2f}" y="{y_bot + INS_BITS_ROW / 2:.1f}" '
                f'font-family="{INS_FONT}" font-size="9" '
                f'text-anchor="middle" dominant-baseline="middle" '
                f'fill="{INS_COLORS[ckey]["text"]}">{bl}</text>'
            )

    lines.append('</svg>')
    return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════
# Generació SVG per al compendi de formats d'instrucció
# ═══════════════════════════════════════════════════════════

def make_svg_compendi(registers: dict) -> str:
    """
    Genera automàticament la figura combinada de tots els formats d'instrucció
    en l'ordre canònic INSTRUCCIO_ORDER. La figura no té entrada al TOML.
    """
    # Recull els registres d'instrucció en ordre canònic
    ordered: list[tuple[str, str, list]] = []  # (tipus, title, fields_raw)
    for tipus in INSTRUCCIO_ORDER:
        # Cerca l'entrada al TOML que contingui el tipus
        for fname, spec in registers.items():
            if not _is_instruccio(fname):
                continue
            label = _ins_type_label(fname)
            if label.upper() == tipus.upper():
                ordered.append((tipus, spec['title'], spec['rows'][0][0]))
                break

    if not ordered:
        return ''

    bw_comb = _ins_bit_w(INS_LABEL_W)
    n_rows  = len(ordered)
    y_first = INS_BIT_H + 2
    H_est   = y_first + n_rows * INS_ROW_H + INS_BITS_ROW + 6

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{INS_W_TOTAL}" height="{H_est}" '
        f'viewBox="0 0 {INS_W_TOTAL} {H_est}" role="img">',
        '<title>Compendi dels formats d\'instrucció RV32I/M/F</title>',
        '<desc>Formats d\'instrucció R, I, S, B, U, J i R4 de RISC-V RV32 en un sol diagrama.</desc>',
    ]

    # Numeració de bits superior (unió de tots els límits)
    all_bits: set[int] = set()
    for _, _, fields_raw in ordered:
        fields = _ins_fields_with_bits(fields_raw)
        for _, hi, lo, _ in fields:
            all_bits.add(hi)
            all_bits.add(lo)

    for b in sorted(all_bits, reverse=True):
        if b == 31:
            anchor, x = "start", _ins_bit_x(31, bw_comb)
        elif b == 0:
            anchor, x = "end", _ins_bit_x(0, bw_comb) + bw_comb
        else:
            anchor, x = "middle", _ins_bit_x(b, bw_comb) + bw_comb
        lines.append(
            f'<text x="{x:.2f}" y="{INS_BIT_H - 2}" '
            f'font-family="{INS_FONT}" font-size="9" '
            f'text-anchor="{anchor}" dominant-baseline="auto" '
            f'fill="{COLORS["R"]["text"]}">{b}</text>'
        )

    # Files de camps
    for row_i, (tipus, _, fields_raw) in enumerate(ordered):
        fields = _ins_fields_with_bits(fields_raw)
        y_row  = y_first + row_i * INS_ROW_H

        for name, hi, lo, ckey in fields:
            c   = INS_COLORS[ckey]
            x   = _ins_bit_x(hi, bw_comb)
            w   = _ins_field_w(hi, lo, bw_comb)
            cx  = _ins_field_cx(hi, lo, bw_comb)
            cy  = y_row + INS_ROW_H / 2
            sw  = "1" if ckey != 'R' else "0.5"
            lines.append(
                f'<rect x="{x:.2f}" y="{y_row}" width="{w:.2f}" height="{INS_ROW_H}" '
                f'fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="{sw}"/>'
            )
            lines.append(
                f'<text x="{cx:.2f}" y="{cy:.1f}" '
                f'font-family="{INS_FONT}" font-size="11" '
                f'text-anchor="middle" dominant-baseline="middle" '
                f'fill="{c["text"]}">{name}</text>'
            )

        # Ticks cap a l'interior d'aquesta fila
        lines += _ins_ticks(y_row, y_row + INS_ROW_H, bw_comb)

        # Etiqueta tipus (dreta)
        lx = INS_W_TOTAL - INS_MARGIN_R
        ly = y_row + INS_ROW_H / 2
        lines.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" '
            f'font-family="{INS_FONT}" font-size="11" font-weight="bold" '
            f'text-anchor="end" dominant-baseline="middle" '
            f'fill="{COLORS["B"]["text"]}">{tipus}-Type</text>'
        )

    # Bits inferiors (referència: R4, la descomposició més fina)
    y_bottom = y_first + n_rows * INS_ROW_H + 2
    _, _, fields_raw_r4 = ordered[-1]  # R4 és l'últim en ordre canònic
    for name, hi, lo, ckey in _ins_fields_with_bits(fields_raw_r4):
        n  = hi - lo + 1
        fw = _ins_field_w(hi, lo, bw_comb)
        cx = _ins_field_cx(hi, lo, bw_comb)
        bl = _ins_bits_label(n, fw)
        if bl:
            lines.append(
                f'<text x="{cx:.2f}" y="{y_bottom + INS_BITS_ROW / 2:.1f}" '
                f'font-family="{INS_FONT}" font-size="9" '
                f'text-anchor="middle" dominant-baseline="middle" '
                f'fill="{INS_COLORS[ckey]["text"]}">{bl}</text>'
            )

    H_real = y_bottom + INS_BITS_ROW + 2
    lines[0] = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{INS_W_TOTAL}" height="{H_real}" '
        f'viewBox="0 0 {INS_W_TOTAL} {H_real}" role="img">'
    )
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

def make_preview(registers: dict, out_dir: Path, output_suffix: str) -> None:
    """Genera preview_regs.html a out_dir amb tots els SVG incrustats inline."""
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
<p class="meta">22 px/bit · ticks per bit · marge 1% · {out_dir}/</p>
<div class="palette">
  {chips_html}
</div>
{''.join(blocks)}
</body>
</html>"""

    preview_path = out_dir / 'preview_regs.html'
    preview_path.parent.mkdir(parents=True, exist_ok=True)
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
            "Exemple: __registre_light  ⇒  T2_instruccio_tipus_R__registre_light.svg"
        ),
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('auto_figs'),
        metavar='DIR',
        help='Directori de sortida (per defecte: auto_figs/).',
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Regenera tots els SVG ignorant timestamps.',
    )
    parser.add_argument(
        '--preview',
        action='store_true',
        help='Genera preview_regs.html (a --output-dir) amb tots els SVG incrustats inline.',
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
            if _is_instruccio(fname):
                svg = make_svg_instruccio(
                    fname,
                    spec['rows'][0][0],
                    spec['title'],
                    spec['desc'],
                )
            else:
                svg = make_svg(fname, spec['rows'], spec['title'], spec['desc'])
            out_path.write_text(svg, encoding='utf-8')
            generated += 1
            if verbosity >= 2:
                print(f'[gen-regs] GENERAT  {out_path.name}')
        except Exception as exc:  # noqa: BLE001
            print(f'[gen-regs] ERROR {out_path.name}: {exc}', file=sys.stderr)
            errors += 1

    # Compendi automàtic (sempre que hi hagi almenys un format d'instrucció)
    has_instruccio = any(_is_instruccio(f) for f in registers)
    if has_instruccio:
        compendi_path = output_dir / (COMPENDI_FNAME + output_suffix + '.svg')
        regenerate = args.force or not compendi_path.exists() or \
            compendi_path.stat().st_mtime <= script_mtime
        if regenerate:
            try:
                svg = make_svg_compendi(registers)
                if svg:
                    compendi_path.write_text(svg, encoding='utf-8')
                    generated += 1
                    if verbosity >= 2:
                        print(f'[gen-regs] GENERAT  {compendi_path.name}')
            except Exception as exc:  # noqa: BLE001
                print(f'[gen-regs] ERROR {compendi_path.name}: {exc}', file=sys.stderr)
                errors += 1
        else:
            skipped += 1
            if verbosity >= 2:
                print(f'[gen-regs] SALTA (vigent)  {compendi_path.name}')

    if args.preview:
        make_preview(registers, output_dir, output_suffix)

    if verbosity >= 1:
        print(
            f'[gen-regs] Resum: {generated} generats, {skipped} vigents, {errors} errors. '
            f'Directori: {output_dir}'
        )

    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
