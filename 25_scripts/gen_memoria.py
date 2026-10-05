#!/usr/bin/env python3
"""
gen_memoria.py — Genera les figures de memòria per bytes a partir de `24_specs/memoria.toml`.

Ús, com a pas del pre-render de Quarto (`_quarto.yml`):

    25_scripts/gen_memoria.py 24_specs/memoria.toml "__memoria_light" --output-dir="auto_figs/"

Escriu `auto_figs/<nom>__memoria_light.svg` per a cada `[memoria.<nom>]` del
TOML; la variant fosca la fa després `gen_dark.py`. És el generador mínim de la
decisió 13 de la fase 7c: una columna d'un byte per fila, amb l'adreça a
l'esquerra (`24_specs/svg.md §9`, sense espais, i centrada a la fila, perquè
cada fila és una sola adreça), la dada a la cel·la i, a la dreta, una nota per
fila (MSB, LSB) o una fletxa de creixement de les adreces. Classe `estreta`
(340 px, `svg.md §2`): columna d'etiquetes de 76 px i cel·les a x = 86.
L'amplada i l'alçada van en px, i no `width="100%"`, perquè a l'HTML la figura
es mostri a la mida natural en lloc d'estirar-se a tota la columna.

Cada fila és `{ adr, dada, nota, negreta }` o `{ elipsi = true }`, que dibuixa
els punts suspensius. La zona (`neutre` o `data`) dona el color, de la paleta de
`svg.md §10`.

Model (b) de la fase 7c (`24_specs/svg.md §17`): la definició és el font i
l'SVG no es versiona. Només fa servir la biblioteca estàndard.
"""
import argparse
import sys
import tomllib
from pathlib import Path

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"
INK, GRIS, TRAC = "#343a40", "#6c757d", "#adb5bd"
ZONES = {                                  # svg.md §10: (fill, stroke, text)
    'neutre': ("#f8f9fa", TRAC, GRIS),
    'data':   ("#cfe2ff", "#084298", "#084298"),
}
W = 340                                    # classe estreta (svg.md §2)
X_ADR, X_RECT = 74, 86                     # svg.md §9 i §5
M_SUP, M_INF, H_FILA = 10, 10, 26


def t(x, y, s, size=11, color=INK, anchor='middle', bold=False, mono=False, italic=False):
    a = f'font-family="{MONO if mono else SANS}" font-size="{size}" fill="{color}" text-anchor="{anchor}"'
    a += ' font-weight="bold"' if bold else ''
    a += ' font-style="italic"' if italic else ''
    return f'<text x="{x}" y="{y}" {a}>{s}</text>'


def make_svg(spec):
    fill, stroke, color = ZONES[spec.get('zona', 'neutre')]
    w_rect = spec.get('amplada', 150)
    files = spec['files']
    o = []
    y = M_SUP
    if spec.get('capcalera', True):
        y += 16
        o.append(t(X_ADR, y - 6, 'Adreça', 10, GRIS, 'end', bold=True))
        o.append(t(X_RECT + w_rect / 2, y - 6, 'Dada', 10, GRIS, bold=True))
    y0 = y
    for f in files:
        mig = y + H_FILA / 2
        if f.get('elipsi'):
            o.append(f'<rect x="{X_RECT}" y="{y}" width="{w_rect}" height="{H_FILA}" fill="{fill}" stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>')
            o.append(t(X_ADR - 30, mig + 5, '⋮', 14, GRIS))
            o.append(t(X_RECT + w_rect / 2, mig + 5, '⋮', 14, color))
        else:
            o.append(f'<rect x="{X_RECT}" y="{y}" width="{w_rect}" height="{H_FILA}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
            o.append(t(X_ADR, mig + 4, f['adr'], 11, color, 'end',
                       bold=f.get('negreta', False), mono=True))
            if f.get('dada'):
                o.append(t(X_RECT + w_rect / 2, mig + 4, f['dada'], 11, color, mono=f['dada'].startswith('0x')))
            if f.get('nota'):
                o.append(t(X_RECT + w_rect + 8, mig + 4, f['nota'], 11, INK, 'start', bold=True))
        y += H_FILA
    if spec.get('fletxa'):
        x = X_RECT + w_rect + 16
        o.append(f'<line x1="{x}" y1="{y0 + 4}" x2="{x}" y2="{y - 10}" stroke="{GRIS}" stroke-width="1.2"/>')
        o.append(f'<polygon points="{x},{y - 2} {x - 4},{y - 11} {x + 4},{y - 11}" fill="{GRIS}"/>')
        for k, mot in enumerate(spec['fletxa'].split()):
            o.append(t(x + 8, (y0 + y) / 2 + k * 13 - 2, mot, 10, GRIS, 'start', italic=True))
    h = y + M_INF
    return '\n'.join([f'<svg width="{W}" height="{h}" viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" role="img">',
                      f'<title>{spec["title"]}</title>', f'<desc>{spec["desc"]}</desc>', *o, '</svg>']) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('specs', type=Path, help='24_specs/memoria.toml')
    ap.add_argument('sufix', help='sufix del fitxer de sortida, p. ex. "__memoria_light"')
    ap.add_argument('--output-dir', type=Path, default=Path('.'))
    args = ap.parse_args()
    dades = tomllib.loads(args.specs.read_text(encoding='utf-8')).get('memoria', {})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    errors = 0
    for nom, spec in dades.items():
        try:
            (args.output_dir / f'{nom}{args.sufix}.svg').write_text(make_svg(spec), encoding='utf-8')
        except (KeyError, TypeError) as e:
            print(f'[gen-memoria] ERROR {nom}: {e!r}', file=sys.stderr)
            errors += 1
    print(f'[gen-memoria] Resum: {len(dades) - errors} generats, {errors} errors. Directori: {args.output_dir}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
