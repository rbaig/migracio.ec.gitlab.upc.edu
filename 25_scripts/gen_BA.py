#!/usr/bin/env python3
"""
gen_BA.py — Genera les figures de blocs d'activació (BA) a partir de `24_specs/ba.toml`.

Ús, com a pas del pre-render de Quarto (`_quarto.yml`):

    25_scripts/gen_BA.py 24_specs/ba.toml "__BA_light" --output-dir="auto_figs/"

Escriu `auto_figs/<nom>__BA_light.svg` per a cada `[ba.<nom>]` del TOML; la
variant fosca la fa després `gen_dark.py`, com amb la resta de figures. La
geometria, els colors i el text segueixen `24_specs/svg.md §3–§11`: marges de
10 px, columna d'etiquetes de 76 px, rectangles de 230 px a x = 86, canvas de
326 px, ratlles indicadores curta·llarga·curta a les dades de mida múltiple de
4 i totes curtes a la resta, i «adr. baixes», «sp →» i «adr. altes» a la
columna esquerra.

Cada zona és un escalar (un sol rectangle), un vector (el primer element, un
mig discontinu i el darrer element, rotulats amb el seu índex) o un farciment
d'alineació. Les vores entre elements d'un vector són fines (0,5 px); les de les
zones, d'1 px.

Model (b) de la fase 7c (`24_specs/svg.md §17`): la definició és el font i
l'SVG no es versiona. Només fa servir la biblioteca estàndard.
"""
import argparse
import sys
import tomllib
from pathlib import Path

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"
GRIS, TRAC, NEUTRE = "#6c757d", "#adb5bd", "#f8f9fa"
ROLS = {                                   # svg.md §10: zones del BA
    'local': ("#cfe2ff", "#084298"),       # variables locals
    'segur': ("#d1e7dd", "#0a3622"),       # registres segurs desats
    'ra':    ("#fff3cd", "#664d03"),       # ra desat
}
M_SUP = M_INF = 10
X_RECT, W_RECT = 86, 230                   # svg.md §5
W = X_RECT + W_RECT + 10                   # 326 px (svg.md §2; migració a `estreta` pendent)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def ticks(o, y, h, curtes, color):
    """Ratlles indicadores de svg.md §6, als dos costats d'un rectangle sòlid."""
    xe, xd = X_RECT + 1, X_RECT + W_RECT - 1
    for frac in (0.25, 0.5, 0.75):
        lon = 6 if (curtes or frac != 0.5) else 12
        yy = y + h * frac
        o.append(f'<line x1="{xe}" y1="{yy}" x2="{xe + lon}" y2="{yy}" stroke="{color}" stroke-width="1"/>')
        o.append(f'<line x1="{xd}" y1="{yy}" x2="{xd - lon}" y2="{yy}" stroke="{color}" stroke-width="1"/>')


def hline(o, y, color, gruix):
    o.append(f'<line x1="{X_RECT}" y1="{y}" x2="{X_RECT + W_RECT}" y2="{y}" stroke="{color}" stroke-width="{gruix}"/>')


def vlines(o, y1, y2, color, discontinua=False):
    estil = ' stroke-dasharray="4,3"' if discontinua else ''
    for x in (X_RECT, X_RECT + W_RECT):
        o.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1"{estil}/>')


def text_zona(o, cy, linies, color):
    """svg.md §8: línies centrades verticalment, a 16 px d'interlineat."""
    n = len(linies)
    for i, (contingut, mida, negreta) in enumerate(linies):
        y = round(cy - (n - 1) * 16 / 2 + i * 16 + mida / 3, 1)
        pes = ' font-weight="bold"' if negreta else ''
        o.append(f'<text x="{X_RECT + W_RECT / 2}" y="{y}" font-family="{SANS}" font-size="{mida}"{pes} '
                 f'fill="{color}" text-anchor="middle">{contingut}</text>')


def mono(t, negreta=False):
    pes = ' font-weight="bold"' if negreta else ''
    return f'<tspan font-family="{MONO}"{pes}>{esc(t)}</tspan>'


def zona(o, z, y, esc_px):
    """Dibuixa una zona a partir de y i en retorna l'alçada."""
    tipus = z['tipus']
    if tipus == 'alineacio':
        h = z['bytes'] * esc_px
        o.append(f'<rect x="{X_RECT}" y="{y}" width="{W_RECT}" height="{h}" fill="{NEUTRE}" stroke="none"/>')
        vlines(o, y, y + h, TRAC, discontinua=True)
        text_zona(o, y + h / 2, [(f"Alineació ({z['bytes']} bytes)", 11, False)], GRIS)
        return h
    fill, stroke = ROLS[z['rol']]
    if tipus == 'escalar':
        h = z['bytes'] * esc_px
        o.append(f'<rect x="{X_RECT}" y="{y}" width="{W_RECT}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        ticks(o, y, h, z['bytes'] % 4 != 0, stroke)
        text_zona(o, y + h / 2, [(mono(z['nom'], True), 12, False)], stroke)
        return h
    # vector: primer element, mig discontinu i darrer element
    he = z['element'] * esc_px
    n = z['n']
    h = he * n
    nom = z['nom']
    o.append(f'<rect x="{X_RECT}" y="{y}" width="{W_RECT}" height="{h}" fill="{fill}" stroke="none"/>')
    hline(o, y, stroke, 1)                                   # vora superior de la zona
    hline(o, y + h, stroke, 1)                               # vora inferior de la zona
    vlines(o, y, y + he, stroke)                             # primer element, sòlid
    vlines(o, y + he, y + h - he, stroke, discontinua=True)  # mig
    vlines(o, y + h - he, y + h, stroke)                     # darrer element, sòlid
    hline(o, y + he, stroke, 0.5)                            # vores fines entre elements
    hline(o, y + h - he, stroke, 0.5)
    if he >= 20:
        ticks(o, y, he, z['element'] % 4 != 0, stroke)
        ticks(o, y + h - he, he, z['element'] % 4 != 0, stroke)
    mida_el = 8 if he < 16 else 10
    for yy, idx in ((y, 0), (y + h - he, n - 1)):
        o.append(f'<text x="{X_RECT + W_RECT / 2}" y="{round(yy + he / 2 + mida_el / 3, 1)}" font-family="{MONO}" '
                 f'font-size="{mida_el}" fill="{stroke}" text-anchor="middle">{esc(nom)}[{idx}]</text>')
    text_zona(o, y + h / 2,
              [(mono(f'{nom}[0]–{nom}[{n - 1}]', True), 12, False),
               (mono(z['ctype'], True) + f' ({h // esc_px} bytes)', 11, False)], stroke)
    return h


def mida(z):
    return z['element'] * z['n'] if z['tipus'] == 'vector' else z['bytes']


def make_svg(spec):
    esc_px = spec['escala']
    total = sum(mida(z) for z in spec['zones'])
    h = M_SUP + total * esc_px + M_INF
    # Amplada i alçada en px, i no width="100%": a l'HTML, una figura estreta es mostra a la mida
    # natural en lloc d'estirar-se a tota la columna (svg.md §2).
    o = [f'<svg width="{W}" height="{h}" viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" role="img">',
         f'<title>{esc(spec["title"])}</title>', f'<desc>{esc(spec["desc"])}</desc>']
    y = M_SUP
    fronteres = [y]
    for z in spec['zones']:
        y += zona(o, z, y, esc_px)
        fronteres.append(y)
    for yy in fronteres:                                      # svg.md §7
        o.append(f'<line x1="76" y1="{yy}" x2="86" y2="{yy}" stroke="{TRAC}" stroke-width="0.5"/>')
    primer = spec['zones'][0]
    color_sp = ROLS[primer['rol']][1] if primer['tipus'] != 'alineacio' else GRIS
    o.append(f'<text x="74" y="{M_SUP + 3}" font-family="{SANS}" font-size="10" fill="{GRIS}" text-anchor="end">adr. baixes</text>')
    o.append(f'<text x="74" y="{M_SUP + 12}" font-family="{MONO}" font-size="11" font-weight="bold" fill="{color_sp}" '
             f'text-anchor="end">sp →</text>')
    o.append(f'<text x="74" y="{h - M_INF + 3}" font-family="{SANS}" font-size="10" fill="{GRIS}" text-anchor="end">adr. altes</text>')
    o.append('</svg>')
    return '\n'.join(o) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('specs', type=Path, help='24_specs/ba.toml')
    ap.add_argument('sufix', help='sufix del fitxer de sortida, p. ex. "__BA_light"')
    ap.add_argument('--output-dir', type=Path, default=Path('.'))
    args = ap.parse_args()
    dades = tomllib.loads(args.specs.read_text(encoding='utf-8')).get('ba', {})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    errors = 0
    for nom, spec in dades.items():
        try:
            (args.output_dir / f'{nom}{args.sufix}.svg').write_text(make_svg(spec), encoding='utf-8')
        except (KeyError, TypeError) as e:
            print(f'[gen-BA] ERROR {nom}: {e!r}', file=sys.stderr)
            errors += 1
    print(f'[gen-BA] Resum: {len(dades) - errors} generats, {errors} errors. Directori: {args.output_dir}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
