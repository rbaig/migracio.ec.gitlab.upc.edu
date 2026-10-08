#!/usr/bin/env python3
"""
gen_BA.py — Genera les figures de blocs d'activació (BA) a partir de `24_specs/BA.toml`.

Ús, com a pas del pre-render de Quarto (`_quarto.yml`):

    25_scripts/gen_BA.py 24_specs/BA.toml "__BA_light" --output-dir="auto_figs/"

Escriu `auto_figs/<nom>__BA_light.svg` per a cada `[BA.<nom>]` del TOML; la
variant fosca la fa després `gen_dark.py`, com amb la resta de figures. La
geometria, els colors i el text segueixen `24_specs/svg.md §2–§11`, amb les
primitives de `columna_memoria.py`, que comparteix amb `gen_mapa.py`: classe
`estreta` (340 px), columna d'etiquetes de 76 px, rectangles de 244 px a x = 86,
ratlles indicadores curta·llarga·curta a les dades de mida múltiple de 4 i
totes curtes a la resta, i «adr. baixes», «sp →» i «adr. altes» a la columna
esquerra.

Cada zona és un escalar (un sol rectangle), un vector (el primer element, un
mig discontinu i el darrer element, rotulats amb el seu índex), un farciment
d'alineació (contorn continu gris, sense ratlles) o una zona genèrica (sòlid,
mig discontinu i sòlid, amb text lliure), per als BA que no són d'una
subrutina concreta. Les vores horitzontals de cada zona van per dins de la seva
àrea (svg.md §7), i el mig discontinu té un byte continu a cada extrem (§4). Les vores entre
elements d'un vector són fines (0,5 px); les de les zones, d'1 px. Amb
`desplacaments = true`, la columna esquerra porta el desplaçament des de `sp`
de cada zona.

Model (b) de la fase 7c (`24_specs/svg.md §17`): la definició és el font i
l'SVG no es versiona. Només fa servir la biblioteca estàndard.
"""
import argparse
import sys
import tomllib
from pathlib import Path

from columna_memoria import (CLASSES, GRIS, M_INF, M_SUP, MONO, NEUTRE, ROLS, TRAC, W_RECT, X_RECT,
                             adreces_extrems, esc, etiqueta, hline, linies_lliures, marcat, mono, rect,
                             separadors, svg, text, text_zona, ticks, vlines, vlines_elidides, vores)


def zona(o, z, y, esc_px):
    """Dibuixa una zona a partir de y i en retorna l'alçada.

    La vora superior i la inferior de la zona no les dibuixa la zona: les dibuixa `vores()` al
    final, quan ja se saben els colors de les dues zones de cada frontera (svg.md §7)."""
    tipus = z['tipus']
    if tipus == 'alineacio':
        h = z['bytes'] * esc_px
        rect(o, y, h, NEUTRE)
        vlines(o, y, y + h, TRAC)                            # contorn continu: els bytes són del BA (svg.md §4)
        text_zona(o, y + h / 2, [(marcat(z.get('text', f"Alineació ({z['bytes']} bytes)")), 11, False)], GRIS)
        return h
    fill, stroke = ROLS[z['rol']]
    if tipus == 'escalar':
        h = z['bytes'] * esc_px
        rect(o, y, h, fill)
        vlines(o, y, y + h, stroke)
        if h >= 40:                                          # svg.md §6: en un de més petit no hi caben
            ticks(o, y, h, z['bytes'] % 4 != 0, stroke)
        linies = [(mono(z['nom'], True), 12, False)] if 'nom' in z else linies_lliures(z['text'])
        text_zona(o, y + h / 2, linies, stroke)
        return h
    if tipus == 'generica':
        # sòlid superior, mig discontinu i sòlid inferior (svg.md §4), amb text lliure al mig
        hs, hm, hi = (b * esc_px for b in z['bytes'])
        h = hs + hm + hi
        curtes = z.get('ratlles', 'mixtes') == 'curtes'
        rect(o, y, h, fill)
        vlines(o, y, y + hs, stroke)
        hline(o, y + hs, stroke, 1)
        vlines_elidides(o, y + hs, y + hs + hm, stroke, esc_px)
        hline(o, y + hs + hm, stroke, 1)
        vlines(o, y + hs + hm, y + h, stroke)
        for yy, hh in ((y, hs), (y + hs + hm, hi)):
            if hh >= 40:
                ticks(o, yy, hh, curtes, stroke)
        text_zona(o, y + hs + hm / 2, linies_lliures(z['text']), stroke)
        return h
    # vector: primer element, mig discontinu i darrer element
    he = z['element'] * esc_px
    n = z['n']
    h = alcada(z) * esc_px
    nom = z['nom']
    rect(o, y, h, fill)
    vlines(o, y, y + he, stroke)                             # primer element, sòlid
    vlines_elidides(o, y + he, y + h - he, stroke, esc_px)   # mig: un byte sòlid a cada extrem
    vlines(o, y + h - he, y + h, stroke)                     # darrer element, sòlid
    hline(o, y + he, stroke, 0.5)                            # vores fines entre elements
    hline(o, y + h - he, stroke, 0.5)
    if he >= 40:                                             # svg.md §6: en un de més petit no hi caben
        ticks(o, y, he, z['element'] % 4 != 0, stroke)
        ticks(o, y + h - he, he, z['element'] % 4 != 0, stroke)
    mida_el = 8 if he < 16 else 10
    for yy, idx in ((y, 0), (y + h - he, n - 1)):
        text(o, X_RECT + W_RECT / 2, round(yy + he / 2 + mida_el / 3, 1), f'{esc(nom)}[{idx}]',
             mida_el, stroke, familia=MONO)
    text_zona(o, y + h / 2,
              [(mono(f'{nom}[0]–{nom}[{n - 1}]', True), 12, False),
               (mono(z['ctype'], True) + f' ({mida(z)} bytes)', 11, False)], stroke)
    return h


def mida(z):
    if z['tipus'] == 'vector':
        return z['element'] * z['n']
    if z['tipus'] == 'generica':
        return sum(z['bytes'])
    return z['bytes']


def alcada(z):
    """L'alçada dibuixada, en bytes de l'escala. Un vector amb `mig` (massa llarg per a la
    figura) en dibuixa el tram elidit amb aquesta alçada fixa; la mida i els desplaçaments
    que s'hi rotulen continuen sent els reals (`mida`)."""
    if z['tipus'] == 'vector' and 'mig' in z:
        return 2 * z['element'] + z['mig']
    return mida(z)


def color_zona(z):
    return GRIS if z['tipus'] == 'alineacio' else ROLS[z['rol']][1]


def color_vora(z):
    """El traç de les vores horitzontals de la zona: el de l'alineació és el gris de traç (svg.md §10)."""
    return TRAC if z['tipus'] == 'alineacio' else ROLS[z['rol']][1]


def make_svg(spec):
    esc_px = spec['escala']
    w = CLASSES[spec.get('classe', 'estreta')]
    total = sum(alcada(z) for z in spec['zones'])
    h = M_SUP + total * esc_px + M_INF
    o = []
    y, despl = M_SUP, 0
    fronteres = [y]
    for k, z in enumerate(spec['zones']):
        if spec.get('desplacaments') and k > 0:              # svg.md §9: a la vora superior de la zona
            etiqueta(o, y, f'+{despl}', color_zona(z))
        y += zona(o, z, y, esc_px)
        despl += mida(z)
        fronteres.append(y)
    vores(o, fronteres, [color_vora(z) for z in spec['zones']])
    separadors(o, fronteres)
    adreces_extrems(o, h)
    text(o, 74, M_SUP + 12, 'sp →', 11, color_zona(spec['zones'][0]), 'end', negreta=True, familia=MONO)
    return svg(w, h, spec['title'], spec['desc'], o)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('specs', type=Path, help='24_specs/BA.toml')
    ap.add_argument('sufix', help='sufix del fitxer de sortida, p. ex. "__BA_light"')
    ap.add_argument('--output-dir', type=Path, default=Path('.'))
    args = ap.parse_args()
    dades = tomllib.loads(args.specs.read_text(encoding='utf-8')).get('BA', {})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    errors = 0
    for nom, spec in dades.items():
        try:
            (args.output_dir / f'{nom}{args.sufix}.svg').write_text(make_svg(spec), encoding='utf-8')
        except (KeyError, TypeError, ValueError) as e:
            print(f'[gen-BA] ERROR {nom}: {e!r}', file=sys.stderr)
            errors += 1
    print(f'[gen-BA] Resum: {len(dades) - errors} generats, {errors} errors. Directori: {args.output_dir}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
