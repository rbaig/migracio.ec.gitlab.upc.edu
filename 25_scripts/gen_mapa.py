#!/usr/bin/env python3
"""
gen_mapa.py — Genera els mapes de memòria a partir de `24_specs/mapa.toml`.

Ús, com a pas del pre-render de Quarto (`_quarto.yml`):

    25_scripts/gen_mapa.py 24_specs/mapa.toml "__mapa_light" --output-dir="auto_figs/"

Escriu `auto_figs/<nom>__mapa_light.svg` per a cada `[mapa.<nom>]` del TOML;
la variant fosca la fa després `gen_dark.py`. És el generador germà de
`gen_BA.py`, i en comparteix les primitives (`columna_memoria.py`) i la
geometria de `24_specs/svg.md §2–§11`. Dos tipus de figura:

- `regions`: una columna de regions de memòria amb text lliure, l'adreça
  d'inici de cada regió a la columna esquerra (svg.md §9) i les fletxes de
  creixement (§11). És el mapa de memòria de RARS.
- `piles`: la pila en diversos moments d'una crida, una columna per moment,
  amb els BA que hi ha a cada moment, la pila ocupada de sota i `sp` al cim. La
  línia i el rètol de `sp` van del color de la zona del cim (svg.md §9), de
  manera que diuen quin BA és actiu.

Model (b) de la fase 7c (`24_specs/svg.md §17`): la definició és el font i
l'SVG no es versiona. Només fa servir la biblioteca estàndard.
"""
import argparse
import sys
import tomllib
from pathlib import Path

from columna_memoria import (CLASSES, GRIS, M_INF, M_SUP, MONO, ROLS, TRAC, W_RECT, X_RECT,
                             color_text, etiqueta, fletxa, linies_lliures, marcat, rect, separadors, svg,
                             text, text_zona, vlines, vores)


def regions(spec):
    """Mapa de memòria: una columna de regions, d'adreces baixes (a dalt) a altes (a baix)."""
    w = CLASSES[spec.get('classe', 'estreta')]
    o, y, fronteres, ys = [], M_SUP, [M_SUP], {}
    for r in spec['regions']:
        rol, hh = r['rol'], r['alcada']
        fill, stroke = ROLS[rol]
        if rol == 'lliure':
            rect(o, y, hh, fill)
            vlines(o, y, y + hh, TRAC, discontinua=True)
        else:
            rect(o, y, hh, fill)
            vlines(o, y, y + hh, stroke)                      # les vores horitzontals, al final (svg.md §7)
        linies = linies_lliures(r['text']) if rol not in ('reservada', 'lliure') \
            else [(marcat(t), 11, False) for t in r['text']]
        text_zona(o, y + hh / 2, linies, color_text(rol))
        if 'adr' in r:
            etiqueta(o, y, r['adr'], color_text(rol))
        ys[rol] = (y, y + hh)
        y += hh
        fronteres.append(y)
    vores(o, fronteres, [None if r['rol'] == 'lliure' else ROLS[r['rol']][1] for r in spec['regions']])
    if 'adr_final' in spec:                                   # l'adreça de la vora inferior (el fons de pila)
        etiqueta(o, y, spec['adr_final'], color_text(spec['regions'][-1]['rol']))
    separadors(o, fronteres)
    for r in spec['regions']:                                 # svg.md §11: de la zona cap a l'espai lliure
        y0, y1 = ys[r['rol']]
        if r.get('fletxa') == 'avall':
            fletxa(o, X_RECT + W_RECT - 22, y1 - 15, y1 + 35, ROLS[r['rol']][1], costat=1)
        elif r.get('fletxa') == 'amunt':
            fletxa(o, X_RECT + 22, y0 + 15, y0 - 35, ROLS[r['rol']][1], costat=-1)
    return svg(w, y + M_INF, spec['title'], spec['desc'], o)


X_PILES = 80                               # vora esquerra de la primera pila
W_COL = 60                                 # amplada de cada pila
Y_PILA = 70                                # vora superior de les piles, sota els rètols de columna


def piles(spec):
    """La pila en diversos moments: una columna per moment, amb sp al cim."""
    w = CLASSES[spec.get('classe', 'estreta')]
    cols = spec['columnes']
    n = len(cols)
    lliure = w - X_PILES - 10 - n * W_COL                      # espai per als n - 1 buits entre piles
    buit = (lliure // (n - 1)) // 5 * 5 if n > 1 else 0
    alc, ocup = spec['alcada'], spec['ocupada']
    o = []
    y_fons = Y_PILA + alc
    for k, c in enumerate(cols):
        x = X_PILES + k * (W_COL + buit)
        for i, linia in enumerate(c['titol']):                # rètol de la columna, de tres línies
            text(o, x + W_COL / 2, 22 + 14 * i, marcat(linia), 11, GRIS)
        # les zones, de dalt a baix: l'espai lliure, els BA (el més recent, a dalt) i la pila ocupada
        alcada_blocs = sum(b['alcada'] for b in c.get('blocs', []))
        zones = [('lliure', None, alc - ocup - alcada_blocs)]
        zones += [(b['rol'], b['nom'], b['alcada']) for b in reversed(c.get('blocs', []))]
        zones.append(('ocupada', None, ocup))
        y, fronteres, colors = Y_PILA, [Y_PILA], []
        for rol, nom, hh in zones:
            fill, stroke = ROLS[rol]
            rect(o, y, hh, fill, x=x, w=W_COL)
            if rol == 'lliure':                               # com l'espai lliure del mapa: discontinu, sense vores
                vlines(o, y, y + hh, TRAC, discontinua=True, x=x, w=W_COL)
                colors.append(None)
            else:
                vlines(o, y, y + hh, stroke, x=x, w=W_COL)
                colors.append(stroke)
            if nom:
                text(o, x + W_COL / 2, y + hh / 2 + 4, marcat(nom), 11, stroke, cursiva=True)
            y += hh
            fronteres.append(y)
        vores(o, fronteres, colors, x=x, w=W_COL)              # svg.md §7
        y = fronteres[1]                                      # el cim: on apunta sp
        cim = colors[1]
        o.append(f'<line x1="{x}" y1="{y}" x2="{x + W_COL}" y2="{y}" stroke="{cim}" stroke-width="2"/>')
        text(o, x - 4, y + 4, 'sp →', 11, cim, 'end', negreta=True, familia=MONO)
    for i, mot in enumerate(('adr.', 'baixes')):              # a l'esquerra de la primera pila, en dues línies
        text(o, X_PILES - 30, Y_PILA + 8 + 12 * i, mot, 10, GRIS, 'end')
    for i, mot in enumerate(('adr.', 'altes')):
        text(o, X_PILES - 30, y_fons - 14 + 12 * i, mot, 10, GRIS, 'end')
    return svg(w, y_fons + M_INF, spec['title'], spec['desc'], o)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('specs', type=Path, help='24_specs/mapa.toml')
    ap.add_argument('sufix', help='sufix del fitxer de sortida, p. ex. "__mapa_light"')
    ap.add_argument('--output-dir', type=Path, default=Path('.'))
    args = ap.parse_args()
    dades = tomllib.loads(args.specs.read_text(encoding='utf-8')).get('mapa', {})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    errors = 0
    for nom, spec in dades.items():
        try:
            fer = {'regions': regions, 'piles': piles}[spec['tipus']]
            (args.output_dir / f'{nom}{args.sufix}.svg').write_text(fer(spec), encoding='utf-8')
        except (KeyError, TypeError, ValueError) as e:
            print(f'[gen-mapa] ERROR {nom}: {e!r}', file=sys.stderr)
            errors += 1
    print(f'[gen-mapa] Resum: {len(dades) - errors} generats, {errors} errors. Directori: {args.output_dir}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
