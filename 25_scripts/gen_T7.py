#!/usr/bin/env python3
"""
gen_T7.py — Genera les figures soltes de T7 (A7): temps d'execució, memòries cau multinivell i multinucli.

    python3 25_scripts/gen_T7.py [--output-dir 22_figs_originals] [--comprova]

Escriu tres SVG natius a `22_figs_originals/`:

- `A7_texe_diagrama.svg` (`#fig-texe-diagrama`): tres instruccions (`lw`,
  `add`, `lw`) etapa per etapa, amb una MC ideal i amb una fallada al segon
  `lw`, que hi afegeix la penalització. Substitueix el placeholder.
- `A7_multinivell_diagrama.svg` (`#fig-multinivell-diagrama`): (a) la CPU
  connectada a l’MP, (b) amb una MC i (c) amb L1 i L2, amb els temps de cada
  enllaç.
- `A7_multinivell_multicore.svg` (`#fig-multinivell-multicore`): xip de quatre
  nuclis amb L1i, L1d i L2 privades, L3 compartida i l’MP (DRAM) fora del xip.
- `A7_tipus_fallades.svg` (`#fig-tipus-fallades`): gràfica qualitativa de la
  taxa de fallades segons la mida i l'associativitat, amb les àrees de cada tipus
  de fallada (figura 6.27 del PDF original).

Referències: les figures de les pàgines 24, 29 i 30 de
`PDF_originals/01_apunts/T6_Memoria_cache.pdf`, i les especificacions dels
comentaris d'A7. Colors de T7 (`13_contrib.qmd §Paleta de colors`): blau per a
la memòria cau i verd per a la memòria principal.

Model (a) de la fase 7c (`24_specs/svg.md §17`): el font versionat és l'SVG, i
aquest script el regenera; `--comprova` el compara amb el versionat sense
escriure res.
"""
import argparse
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figlib  # noqa: E402
from figlib import t, var, caixa, fletxa, svg  # noqa: E402

SANS, MONO, INK, GRIS = figlib.SANS, figlib.MONO, figlib.INK, figlib.GRAY
TRAC, NEUTRE = "#adb5bd", "#f8f9fa"
MC_F, MC_S = "#cfe2ff", "#084298"        # memòria cau
MP_F, MP_S = "#d1e7dd", "#0a3622"        # memòria principal
PEN_F, PEN_S = "#f8d7da", "#842029"      # penalització
NUC_F, NUC_S = "#fff3cd", "#664d03"      # nuclis (CPU)


# ── Temps d'execució ─────────────────────────────────────────

def texe():
    o = []
    B = 24                       # amplada d'una etapa (un cicle)
    x0 = 190
    instr = [('lw', 'FDRAMW'), ('add', 'FDRAW'), ('lw', 'FDRAMW')]
    PEN = 7                      # cicles de penalització dibuixats
    files = [('MC ideal', 'tots els accessos són encerts', False), ('MC real', 'fallada en la dada del segon lw', True)]
    y0 = 40
    for r, (nom, sub, falla) in enumerate(files):
        y = y0 + r * 90
        o.append(t(14, y + 16, nom, 12, INK, 'start', bold=True))
        o.append(t(14, y + 31, sub, 9, GRIS, 'start', italic=True))
        x = x0
        for k, (mn, etapes) in enumerate(instr):
            o.append(t(x, y - 6, mn, 11, INK, 'start', mono=True))
            for e in etapes:
                if falla and k == 2 and e == 'W':
                    o.append(f'<rect x="{x}" y="{y}" width="{PEN * B}" height="22" fill="{PEN_F}" stroke="{PEN_S}" stroke-width="1"/>')
                    o.append(t(x + PEN * B / 2, y + 15, 'penalització', 11, PEN_S, italic=True))
                    o.append(fletxa(x + 2, y + 34, x + PEN * B - 2, y + 34, PEN_S))
                    o.append(f'<text x="{x + PEN * B / 2}" y="{y + 50}" font-family="{SANS}" font-size="11" fill="{PEN_S}" text-anchor="middle">{var("t", "p")}</text>')
                    x += PEN * B
                memoria = e in 'FM'
                o.append(f'<rect x="{x}" y="{y}" width="{B}" height="22" fill="{MC_F if memoria else "#ffffff"}" stroke="{INK}" stroke-width="1"/>')
                o.append(t(x + B / 2, y + 15, e, 11, MC_S if memoria else INK))
                if memoria:
                    o.append(fletxa(x + 2, y + 30, x + B - 2, y + 30, MC_S, w=1))
                    o.append(f'<text x="{x + B / 2}" y="{y + 44}" font-family="{SANS}" font-size="10" fill="{MC_S}" text-anchor="middle">{var("t", "h")}</text>')
                x += B
            x += 8
    x_fi = x0 + sum(len(e) for _, e in instr) * B + 16 + PEN * B
    yy = y0 + 2 * 90 - 10
    o.append(fletxa(x0, yy, x_fi, yy, GRIS, doble=False, w=1))
    o.append(t(x_fi, yy + 16, 'temps', 10, GRIS, 'end', italic=True))
    llegenda = ('F: captura de la instrucció · D: descodificació · R: lectura de registres · '
                'A: ALU · M: accés a la dada · W: escriptura del registre')
    o.append(t(x0, yy + 34, llegenda, 10, GRIS, 'start'))
    o.append(f'<rect x="{x0}" y="{yy + 44}" width="12" height="10" fill="{MC_F}" stroke="{INK}" stroke-width="0.75"/>')
    o.append(t(x0 + 18, yy + 53, 'accés a la memòria cau (encert: <tspan font-style="italic">t</tspan><tspan dy="3" font-size="8" font-style="italic">h</tspan><tspan dy="-3">)</tspan>', 10, GRIS, 'start'))
    w = x_fi + 20
    return svg(w, yy + 66, "Impacte d'una fallada de memòria cau en el temps d'execució",
               "Dues files de tres instruccions (lw, add, lw) etapa per etapa: F, D, R, A, M i W, un cicle cadascuna. "
               "Les etapes F i M accedeixen a la memòria cau. A la primera fila tots els accessos són encerts. A la "
               "segona, la dada del segon lw falla, i entre la seva etapa M i la W s'afegeixen els cicles de "
               "penalització, t sub p; la resta d'etapes són iguals a les dues files.", o)


# ── Memòries cau multinivell ─────────────────────────────────

def multinivell():
    o = []
    yy = 26
    files = [
        ('(a)', "Problema: el temps d'accés a l’MP limita el rendiment", [('CPU', None), ('MP', ('t', 'acc', None))]),
        ('(b)', 'Solució: una MC explota la localitat; el temps llarg només es paga a les fallades',
         [('CPU', None), ('MC', ('t', 'h', None)), ('MP', ('t', 'p', None))]),
        ('(c)', 'Les fallades de L1 que encerten a L2 paguen el temps d’encert de L2, no el de l’MP',
         [('CPU', None), ('L1', ('t', 'h', 'L1')), ('L2', ('t', 'h', 'L2')), ('MP', ('t', 'p', None))]),
    ]
    W = 660
    for etiq, frase, elems in files:
        o.append(t(14, yy + 4, etiq, 12, INK, 'start', bold=True))
        o.append(t(44, yy + 4, frase, 11, INK, 'start'))
        y = yy + 22
        xs = {'CPU': 44, 'MC': 230, 'L1': 200, 'L2': 360, 'MP': 560}
        prev = None
        for nom, temps in elems:
            x = xs[nom]
            fill, stroke = (NUC_F, NUC_S) if nom == 'CPU' else ((MP_F, MP_S) if nom == 'MP' else (MC_F, MC_S))
            o.append(caixa(x, y, 70, 30, fill, stroke, nom))
            if prev is not None:
                o.append(fletxa(prev + 74, y + 15, x - 4, y + 15, INK))
                nom_t, sub, sub2 = temps
                o.append(f'<text x="{(prev + 70 + x) / 2}" y="{y + 8}" font-family="{SANS}" font-size="11" fill="{INK}" text-anchor="middle">{var(nom_t, sub, sub2)}</text>')
            prev = x
        if etiq == '(c)':
            o.append(f'<rect x="34" y="{y - 10}" width="246" height="50" fill="none" stroke="{GRIS}" stroke-width="1" stroke-dasharray="5,3"/>')
            o.append(t(157, y + 52, 'per a L2, la «CPU» és el conjunt CPU + L1', 9, GRIS, italic=True))
        yy += 92
    return svg(W, yy - 6, "Memòries cau multinivell",
               "Tres configuracions: (a) la CPU connectada a l’MP, amb un temps d'accés llarg; (b) una MC entre la "
               "CPU i l’MP, amb temps d'encert t sub h i penalització t sub p a les fallades; (c) L1 i L2 entre la "
               "CPU i l’MP: les fallades de L1 que encerten a L2 paguen t sub h sub L2, i només les que també fallen "
               "a L2 paguen t sub p.", o)


# ── Jerarquia multinucli ─────────────────────────────────────

def multicore():
    o = []
    W, n = 660, 4
    o.append(caixa(150, 14, 360, 32, MP_F, MP_S, 'Memòria principal (DRAM)'))
    o.append(f'<rect x="20" y="66" width="{W - 40}" height="284" rx="6" fill="none" stroke="{GRIS}" stroke-width="1" stroke-dasharray="6,4"/>')
    o.append(t(30, 82, 'xip', 10, GRIS, 'start', italic=True))
    o.append(fletxa(330, 50, 330, 78, INK))
    o.append(caixa(60, 82, W - 120, 30, MC_F, MC_S, 'L3 (compartida)'))
    amp = (W - 80) / n
    for k in range(n):
        cx = 40 + amp * k + amp / 2
        o.append(fletxa(cx, 116, cx, 142, INK))
        o.append(caixa(cx - 55, 146, 110, 30, MC_F, MC_S, 'L2'))
        o.append(fletxa(cx - 26, 180, cx - 26, 206, INK))
        o.append(fletxa(cx + 26, 180, cx + 26, 206, INK))
        o.append(caixa(cx - 55, 210, 52, 30, MC_F, MC_S, 'L1i', 11))
        o.append(caixa(cx + 3, 210, 52, 30, MC_F, MC_S, 'L1d', 11))
        o.append(fletxa(cx - 26, 244, cx - 26, 274, INK))
        o.append(fletxa(cx + 26, 244, cx + 26, 274, INK))
        o.append(caixa(cx - 55, 278, 110, 34, NUC_F, NUC_S, f'nucli {k}'))
    o.append(t(W / 2, 334, 'L1i, L1d i L2: privades de cada nucli', 10, GRIS, italic=True))
    return svg(W, 362, "Jerarquia de memòries cau d'un processador multinucli",
               "Xip de quatre nuclis. Cada nucli té una L1 d'instruccions (L1i), una L1 de dades (L1d) i una L2 "
               "privades; tots comparteixen una L3, que es connecta a la memòria principal (DRAM), fora del xip.", o)


# ── Tipus de fallades segons la mida i l'associativitat ──────

def tipus_fallades():
    """Gràfica qualitativa (figura 6.27 del PDF original): taxa de fallades en funció de la mida de la
    MC per a quatre graus d'associativitat, amb les àrees de cada tipus de fallada."""
    o = []
    X0, X1, Y0, Y1 = 150, 600, 40, 300            # eix x de X0 a X1; eix y de Y1 (0) a Y0 (màxim)
    COLD = 0.06
    corbes = [('correspondència directa', 1.00), ('associativa de 2 vies', 0.80), ('associativa de 4 vies', 0.70),
              ('completament associativa', 0.58)]

    def y_de(a, u):                               # u ∈ [0, 1]: mida de l’MC, de petita a gran
        v = COLD + a * 0.9 / (1 + 7 * u)
        return Y1 - v * (Y1 - Y0)

    def punts(a, n=40):
        return [(round(X0 + (X1 - X0) * k / n, 1), round(y_de(a, k / n), 1)) for k in range(n + 1)]
    y_cold = round(Y1 - COLD * (Y1 - Y0), 1)
    fa = punts(corbes[-1][1])
    cd = punts(corbes[0][1])
    # àrees: capacitat (entre l'arrencada en fred i la completament associativa) i conflicte (entre aquesta i la directa)
    o.append(f'<polygon points="{X0},{y_cold} ' + ' '.join(f'{x},{y}' for x, y in fa) + f' {X1},{y_cold}" fill="#fff3cd" stroke="none"/>')
    o.append('<polygon points="' + ' '.join(f'{x},{y}' for x, y in fa) + ' ' + ' '.join(f'{x},{y}' for x, y in reversed(cd)) + '" fill="#f8d7da" stroke="none"/>')
    o.append(f'<rect x="{X0}" y="{y_cold}" width="{X1 - X0}" height="{Y1 - y_cold}" fill="#cfe2ff" stroke="none"/>')
    for k, (nom, a) in enumerate(corbes):
        pts = punts(a)
        o.append(figlib.line(pts, INK, 1.4 if k in (0, 3) else 0.9))
        o.append(t(X0 - 8, pts[0][1] + 4, nom, 10, INK, 'end'))
    o.append(t(330, y_cold + 13, "fallades d'arrencada en fred", 10, MC_S, bold=True))
    o.append(t(222, 266, 'fallades de capacitat', 10, NUC_S, bold=True))
    o.append(f'<line x1="470" y1="214" x2="470" y2="250" stroke="{PEN_S}" stroke-width="1"/>')
    o.append(f'<circle cx="470" cy="252" r="2" fill="{PEN_S}"/>')
    o.append(t(470, 208, 'fallades de conflicte', 10, PEN_S, bold=True))
    xm = 300
    o.append(f'<line x1="{xm}" y1="{Y0 - 6}" x2="{xm}" y2="{Y1}" stroke="{GRIS}" stroke-width="1" stroke-dasharray="4,3"/>')
    o.append(t(xm + 4, Y0 - 10, 'una mida donada', 9, GRIS, 'start', italic=True))
    o.append(fletxa(X0, Y1, X1 + 20, Y1, INK, doble=False, w=1))
    o.append(fletxa(X0, Y1, X0, Y0 - 20, INK, doble=False, w=1))
    o.append(t(X1 + 20, Y1 + 18, 'mida de la memòria cau', 10, INK, 'end'))
    o.append(t(X0 + 6, Y0 - 14, 'taxa de fallades', 10, INK, 'start'))
    return svg(X1 + 40, Y1 + 30, "Tipus de fallades segons la mida i l'associativitat de la memòria cau",
               "Gràfica qualitativa de la taxa de fallades en funció de la mida de la memòria cau, per a un "
               "programa donat, amb quatre corbes decreixents: correspondència directa (la més alta), associativa "
               "de 2 vies, de 4 vies i completament associativa (la més baixa). Les fallades d'arrencada en fred "
               "són una franja constant a baix. Entre aquesta franja i la corba completament associativa, les "
               "fallades de capacitat, que només disminueixen si augmenta la mida. Entre la completament "
               "associativa i la de correspondència directa, les de conflicte, que disminueixen en augmentar "
               "l'associativitat.", o)


FIGURES = {
    'A7_texe_diagrama.svg': texe,
    'A7_multinivell_diagrama.svg': multinivell,
    'A7_multinivell_multicore.svg': multicore,
    'A7_tipus_fallades.svg': tipus_fallades,
}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--output-dir', default='22_figs_originals')
    ap.add_argument('--comprova', action='store_true', help='compara amb els SVG versionats; no escriu res')
    args = ap.parse_args()
    dif = 0
    for nom, fig in FIGURES.items():
        ruta = os.path.join(args.output_dir, nom)
        contingut = fig()
        if args.comprova:
            actual = open(ruta, encoding='utf-8').read() if os.path.exists(ruta) else None
            if actual != contingut:
                print(f'[gen-T7] DIFEREIX: {ruta}', file=sys.stderr)
                dif += 1
            continue
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contingut)
        print(f'[gen-T7] {ruta}')
    sys.exit(1 if dif else 0)


if __name__ == '__main__':
    main()
