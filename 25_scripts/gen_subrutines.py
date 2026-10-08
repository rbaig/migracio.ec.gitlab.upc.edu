#!/usr/bin/env python3
"""
gen_subrutines.py — Genera les figures de dependències de dades de les subrutines a partir de `24_specs/subrutines.toml`.

Ús, com a pas del pre-render de Quarto (`_quarto.yml`):

    25_scripts/gen_subrutines.py 24_specs/subrutines.toml "__subrutina_light" --output-dir="auto_figs/"

Escriu `auto_figs/<nom>__subrutina_light.svg` per a cada `[subrutina.<nom>]`
del TOML; la variant fosca la fa després `gen_dark.py`. Cada figura és el codi
C de la subrutina, amb les crides en franges grises, i una barra per dada, de
l'última escriptura a l'últim ús: blava si travessa alguna crida i grisa si no,
amb el nom de la dada al capdamunt i el registre al peu. Dins del codi, les
dades porten el color de la seva barra.

És la segona representació de les figures `A3_deps_*` d'A3, al costat de la de
fletxes de `22_figs_originals/` (subfigures (a) i (b)). Model (b) de la fase 7c
(`24_specs/svg.md §17`): la definició és el font i l'SVG no es versiona. Només
fa servir la biblioteca estàndard.
"""
import argparse
import sys
import tomllib
from pathlib import Path

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"
INK, GRIS, TRAC, NEUTRE, BLAU = "#343a40", "#6c757d", "#adb5bd", "#f8f9fa", "#084298"
CW = 7.2          # amplada d'un caràcter de Liberation Mono a 12 px
X0 = 14           # x de la columna 0 del codi
PAS = 24          # interlineat
Y_CAP = 18        # fila dels noms de les dades
Y0 = 50           # línia base de la primera línia de codi


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def travessa(d, crides):
    fe, fu, res = d['escriptura'], d['us'], d.get('resultat', False)
    return any(fe < f < fu or (f == fe and not res and f < fu) or (f == fu and fe < f) for f, _ in crides)


def es_paraula(l, i, n):
    """Cert si l[i:i+n] és un identificador sencer (no un tros d'un altre)."""
    abans = i == 0 or not (l[i - 1].isalnum() or l[i - 1] == '_')
    despres = i + n == len(l) or not (l[i + n].isalnum() or l[i + n] == '_')
    return abans and despres


def linia_codi(l, y, color):
    """Una línia de codi: cada fragment a la seva columna, amb les dades acolorides."""
    noms = sorted(color, key=len, reverse=True)
    segs, cur, i = [], '', 0
    while i < len(l):
        tok = next((v for v in noms if l.startswith(v, i) and es_paraula(l, i, len(v))), None)
        if tok:
            if cur:
                segs.append((i - len(cur), cur, None))
                cur = ''
            segs.append((i, tok, color[tok]))
            i += len(tok)
        else:
            cur += l[i]
            i += 1
    if cur:
        segs.append((len(l) - len(cur), cur, None))
    parts = []
    for col, s, c in segs:
        lead = len(s) - len(s.lstrip(' '))
        s = s.strip(' ')
        if s:
            attr = f' fill="{c}" font-weight="bold"' if c else ''
            parts.append(f'<tspan x="{round(X0 + (col + lead) * CW, 1)}"{attr}>{esc(s)}</tspan>')
    return f'<text y="{y}" font-family="{MONO}" font-size="12" fill="{INK}">{"".join(parts)}</text>'


def make_svg(spec):
    codi, crides, dades = spec['codi'], [tuple(c) for c in spec.get('crides', [])], spec['dades']
    amplada = spec.get('amplada', 600)
    n = len(codi)
    base = lambda f: Y0 + f * PAS
    centre = lambda f: base(f) - 4
    h = base(n - 1) + 36
    color = {d['nom']: (BLAU if travessa(d, crides) else GRIS) for d in dades}
    o = [f'<svg width="100%" viewBox="0 0 {amplada} {h}" xmlns="http://www.w3.org/2000/svg" role="img">',
         f'<title>{esc(spec["title"])}</title>', f'<desc>{esc(spec["desc"])}</desc>']
    for f, func in crides:                          # franges de les crides, darrere de tot
        y = centre(f) - PAS / 2
        o.append(f'<rect x="8" y="{y}" width="{amplada - 16}" height="{PAS}" fill="{NEUTRE}"/>')
        for yy in (y, y + PAS):
            o.append(f'<line x1="8" y1="{yy}" x2="{amplada - 8}" y2="{yy}" stroke="{TRAC}" stroke-width="1" stroke-dasharray="6,4"/>')
        o.append(f'<text x="{amplada - 12}" y="{base(f)}" font-family="{SANS}" font-size="10" font-style="italic" '
                 f'fill="{GRIS}" text-anchor="end">crida a <tspan font-family="{MONO}" font-style="normal">{esc(func)}</tspan></text>')
    for f, l in enumerate(codi):
        o.append(linia_codi(l, base(f), color))
    x_ini = X0 + max(len(l) for l in codi) * CW + 30
    for k, d in enumerate(dades):                   # barres de vida, a la dreta del codi
        x = round(x_ini + k * 50, 1)
        c = color[d['nom']]
        y1 = centre(d['escriptura']) + (7 if d.get('resultat') else 0)
        y2 = centre(d['us'])
        o.append(f'<text x="{x}" y="{Y_CAP}" font-family="{MONO}" font-size="12" font-weight="bold" fill="{c}" '
                 f'text-anchor="middle">{esc(d["nom"])}</text>')
        o.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{c}" stroke-width="3" stroke-linecap="round"/>')
        o.append(f'<circle cx="{x}" cy="{y1}" r="4" fill="{c}"/>')
        o.append(f'<path d="M{x - 5},{y2 - 6} L{x},{y2 + 2} L{x + 5},{y2 - 6} z" fill="{c}"/>')
        o.append(f'<text x="{x}" y="{base(n - 1) + 22}" font-family="{MONO}" font-size="12" font-weight="bold" fill="{c}" '
                 f'text-anchor="middle">{esc(d["registre"])}</text>')
    o.append('</svg>')
    return '\n'.join(o) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('specs', type=Path, help='24_specs/subrutines.toml')
    ap.add_argument('sufix', help='sufix del fitxer de sortida, p. ex. "__subrutina_light"')
    ap.add_argument('--output-dir', type=Path, default=Path('.'))
    args = ap.parse_args()
    dades = tomllib.loads(args.specs.read_text(encoding='utf-8')).get('subrutina', {})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    errors = 0
    for nom, spec in dades.items():
        try:
            (args.output_dir / f'{nom}{args.sufix}.svg').write_text(make_svg(spec), encoding='utf-8')
        except (KeyError, TypeError, ValueError) as e:
            print(f'[gen-subrutines] ERROR {nom}: {e!r}', file=sys.stderr)
            errors += 1
    print(f'[gen-subrutines] Resum: {len(dades) - errors} generats, {errors} errors. Directori: {args.output_dir}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
