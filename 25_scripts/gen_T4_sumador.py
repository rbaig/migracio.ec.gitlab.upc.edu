#!/usr/bin/env python3
"""
gen_T4_sumador.py — Genera les figures del sumador de T4 (A4, #wrn-sobreeiximent-maquinari).

    25_scripts/gen_T4_sumador.py [--output-dir 22_figs_originals] [--comprova]

Escriu dos SVG natius a `22_figs_originals/`:

- `T4_semisumador_sumador_complet.svg`: (a) semisumador (XOR i AND) i
  (b) sumador complet fet amb dos semisumadors i una OR.
- `T4_sumador_propagacio_rossec.svg`: cadena de sumadors complets amb la
  XOR que dona el sobreeiximent, v = c_{n-1} xor c_n.

No forma part del pre-render: el font versionat és l'SVG, i aquest script
és l'eina per regenerar-lo. Convencions (portes, colors, subíndexs i
operadors): `24_specs/svg.md §16`.
"""
import argparse
import os
import sys


SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
INK = "#343a40"      # fils i portes
GRAY = "#6c757d"     # etiquetes de senyals intermedis
BF, BS = "#cfe2ff", "#084298"   # caixes de semisumador
W = 1.5
out = []


def line(pts, color=INK):
    d = " ".join(f"{x},{y}" for x, y in pts)
    out.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{W}" stroke-linejoin="round"/>')


def dot(x, y, color=INK):
    out.append(f'<circle cx="{x}" cy="{y}" r="2.5" fill="{color}"/>')


def term(x, y, color=INK):
    out.append(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#ffffff" stroke="{color}" stroke-width="{W}"/>')


def sig(x, y, parts, size=13, color=INK, anchor="start", weight=None):
    """parts: llista de (text, mode); mode 'v' variable en cursiva, 's' subíndex, 'r' recte."""
    sub = round(size * 0.72)
    dy = round(size * 0.28)
    fw = f' font-weight="{weight}"' if weight else ""
    s = [f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" fill="{color}" text-anchor="{anchor}"{fw}>']
    low = False
    pend = False
    for txt, mode in parts:
        attrs = []
        if mode == "o" or pend:
            attrs.append('dx="3"')
        pend = mode == "o"
        if mode == "s" and not low:
            attrs.append(f'dy="{dy}"'); low = True
        elif mode != "s" and low:
            attrs.append(f'dy="-{dy}"'); low = False
        if mode == "s":
            attrs.append(f'font-size="{sub}"')
        if mode in ("v", "s"):
            attrs.append('font-style="italic"')
        s.append(f'<tspan {" ".join(attrs)}>{txt}</tspan>' if attrs else f'<tspan>{txt}</tspan>')
    s.append("</text>")
    out.append("".join(s))


def and_gate(x, cy):
    out.append(f'<path d="M{x},{cy-16} h20 a16,16 0 0 1 0,32 h-20 z" fill="none" stroke="{INK}" stroke-width="{W}" stroke-linejoin="round"/>')
    return x + 36


def or_gate(x, cy, color=INK, fill="none"):
    out.append(f'<path d="M{x},{cy-16} Q{x+10},{cy} {x},{cy+16} Q{x+28},{cy+16} {x+40},{cy} Q{x+28},{cy-16} {x},{cy-16} z" fill="{fill}" stroke="{color}" stroke-width="{W}" stroke-linejoin="round"/>')
    return x + 40


def xor_gate(x, cy, color=INK, fill="none"):
    out.append(f'<path d="M{x},{cy-16} Q{x+10},{cy} {x},{cy+16}" fill="none" stroke="{color}" stroke-width="{W}"/>')
    return or_gate(x + 6, cy, color, fill)


def box(x, y, w, h, ports):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{BF}" stroke="{BS}" stroke-width="1"/>')
    out.append(f'<text x="{x+w/2}" y="{y+h/2+4}" font-family="{SANS}" font-size="11" fill="{BS}" text-anchor="middle">semisumador</text>')
    for px, py, name, anchor in ports:
        out.append(f'<text x="{px}" y="{py+4}" font-family="{SANS}" font-size="11" font-style="italic" fill="{BS}" text-anchor="{anchor}">{name}</text>')


RF, RS = "#f8d7da", "#842029"   # ressaltat: detecció del sobreeiximent


def adder(x, y, w, h):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{BF}" stroke="{BS}" stroke-width="1"/>')
    for k, word in enumerate(("sumador", "complet")):
        out.append(f'<text x="{x+w/2}" y="{y+h/2-2+k*13}" font-family="{SANS}" font-size="11" fill="{BS}" text-anchor="middle">{word}</text>')


def fig_semisumador_sumador_complet():
    out.clear()
    # ---------------- (a) semisumador ----------------
    sig(10, 22, [("(a) semisumador", "r")], weight="bold")
    XA, YA, YB = 60, 55, 75
    term(XA, YA); term(XA, YB)
    sig(XA - 8, YA + 4, [("a", "v")], anchor="end")
    sig(XA - 8, YB + 4, [("b", "v")], anchor="end")
    GX = 200
    xo = xor_gate(GX, 65)
    an = and_gate(GX, 115)
    line([(XA + 2.5, YA), (GX + 3, YA)])
    line([(XA + 2.5, YB), (GX + 3, YB)])
    dot(110, YA); line([(110, YA), (110, 105), (GX, 105)])
    dot(140, YB); line([(140, YB), (140, 125), (GX, 125)])
    for y, out_x, name in ((65, xo, "s"), (115, an, "c")):
        line([(out_x, y), (300, y)]); term(302.5, y)
        sig(312, y + 4, [(name, "v")])

    # ---------------- (b) sumador complet ----------------
    sig(10, 172, [("(b) sumador complet", "r")], weight="bold")
    X1, Y1 = 110, 190            # semisumador 1: 90 x 70
    X2, Y2 = 270, 230            # semisumador 2
    BW, BH = 90, 70
    pa1, pb1 = Y1 + 15, Y1 + 55  # ports d'entrada/sortida
    pa2, pb2 = Y2 + 15, Y2 + 55
    box(X1, Y1, BW, BH, [(X1 + 6, pa1, "a", "start"), (X1 + 6, pb1, "b", "start"),
                         (X1 + BW - 6, pa1, "c", "end"), (X1 + BW - 6, pb1, "s", "end")])
    box(X2, Y2, BW, BH, [(X2 + 6, pa2, "a", "start"), (X2 + 6, pb2, "b", "start"),
                         (X2 + BW - 6, pa2, "c", "end"), (X2 + BW - 6, pb2, "s", "end")])
    XI = 60
    for y, parts in ((pa1, [("a", "v"), ("i", "s")]), (pb1, [("b", "v"), ("i", "s")]), (pb2, [("c", "v"), ("i", "s")])):
        term(XI, y)
        sig(XI - 8, y + 4, parts, anchor="end")
    line([(XI + 2.5, pa1), (X1, pa1)])
    line([(XI + 2.5, pb1), (X1, pb1)])
    line([(XI + 2.5, pb2), (X2, pb2)])
    # s del primer -> a del segon (pb1 == pa2)
    assert pb1 == pa2
    line([(X1 + BW, pb1), (X2, pa2)])
    sig((X1 + BW + X2) / 2, pb1 - 6, [("a", "v"), ("i", "s"), ("⊕", "o"), ("b", "v"), ("i", "s")], size=11, color=GRAY, anchor="middle")
    # porta OR
    OX, OC = 450, 225
    oo = or_gate(OX, OC)
    line([(X1 + BW, pa1), (420, pa1), (420, OC - 10), (OX + 3, OC - 10)])
    sig(310, pa1 - 6, [("a", "v"), ("i", "s"), ("∧", "o"), ("b", "v"), ("i", "s")], size=11, color=GRAY, anchor="middle")
    line([(X2 + BW, pa2), (OX + 3, OC + 10)]) if pa2 == OC + 10 else line([(X2 + BW, pa2), (435, pa2), (435, OC + 10), (OX + 3, OC + 10)])
    sig(X2 + BW + 6, pa2 + 17, [("(", "r"), ("a", "v"), ("i", "s"), ("⊕", "o"), ("b", "v"), ("i", "s"), (")", "r"), ("∧", "o"), ("c", "v"), ("i", "s")], size=11, color=GRAY)
    line([(oo, OC), (530, OC)]); term(532.5, OC)
    sig(542, OC + 4, [("c", "v"), ("i+1", "s")])
    line([(X2 + BW, pb2), (530, pb2)]); term(532.5, pb2)
    sig(542, pb2 + 4, [("s", "v"), ("i", "s")])

    W_, H_ = 590, 320
    svg = [f'<svg width="{W_}" height="{H_}" viewBox="0 0 {W_} {H_}" xmlns="http://www.w3.org/2000/svg" role="img">',
           '<title>Semisumador i sumador complet (mode clar)</title>',
           '<desc>(a) Semisumador: una porta XOR dona el bit de suma s = a xor b i una porta AND dona el bit de ròssec c = a and b. '
           '(b) Sumador complet fet amb dos semisumadors i una porta OR: el primer suma a_i i b_i; el segon suma el resultat, a_i xor b_i, amb el ròssec d\'entrada c_i i dona s_i; '
           'la OR combina a_i and b_i i (a_i xor b_i) and c_i en el ròssec de sortida c_(i+1).</desc>']
    svg += out + ["</svg>", ""]
    return "\n".join(svg)


def fig_sumador_propagacio_rossec():
    out.clear()
    BW, BH, BY = 80, 56, 80
    CY = BY + BH / 2                       # fil del ròssec
    cols = [(130, "n-1"), (270, "n-2"), (470, "1"), (610, "0")]
    for x, i in cols:
        adder(x, BY, BW, BH)
        for dx, v in ((25, "a"), (55, "b")):
            line([(x + dx, 52), (x + dx, BY)]); term(x + dx, 49.5)
            sig(x + dx, 40, [(v, "v"), (i, "s")], anchor="middle")
        xs = x + BW / 2
        line([(xs, BY + BH), (xs, BY + BH + 28)]); term(xs, BY + BH + 30.5)
        sig(xs, BY + BH + 50, [("s", "v"), (i, "s")], anchor="middle")

    # ròssecs entre caixes (de dreta a esquerra)
    line([(730, CY), (690, CY)]); term(732.5, CY)
    sig(734, CY - 8, [("c", "v"), ("0", "s")], anchor="end")
    line([(610, CY), (550, CY)])
    sig(580, CY - 8, [("c", "v"), ("1", "s")], anchor="middle")
    line([(470, CY), (440, CY)])
    sig(456, CY - 8, [("c", "v"), ("2", "s")], anchor="middle")
    out.append(f'<text x="413" y="{CY+5}" font-family="{SANS}" font-size="16" fill="{INK}" text-anchor="middle">···</text>')
    line([(388, CY), (350, CY)])
    sig(371, CY - 8, [("c", "v"), ("n-2", "s")], anchor="middle")

    # c_{n-1}: entre les dues caixes de més pes, amb derivació a la XOR
    line([(270, CY), (210, CY)], RS)
    sig(240, CY - 8, [("c", "v"), ("n-1", "s")], anchor="middle", color=RS)
    # c_n: surt de la caixa de més pes
    line([(130, CY), (22.5, CY)], RS); term(20, CY, RS)
    sig(22, CY - 8, [("c", "v"), ("n", "s")], color=RS)

    # porta XOR del sobreeiximent
    XX, XC = 60, 215
    xo = xor_gate(XX, XC, RS, RF)
    dot(40, CY, RS); line([(40, CY), (40, XC - 10), (XX + 3, XC - 10)], RS)
    dot(240, CY, RS); line([(240, CY), (240, 250), (48, 250), (48, XC + 10), (XX + 3, XC + 10)], RS)
    line([(xo, XC), (132.5, XC)], RS); term(135, XC, RS)
    sig(145, XC + 5, [("v", "v")], color=RS)

    W_, H_ = 750, 265
    svg = [f'<svg width="{W_}" height="{H_}" viewBox="0 0 {W_} {H_}" xmlns="http://www.w3.org/2000/svg" role="img">',
           '<title>Sumador amb propagació del ròssec i detecció del sobreeiximent (mode clar)</title>',
           '<desc>Cadena de n sumadors complets, del bit de més pes (n-1, a l\'esquerra) al de menys pes (0, a la dreta). '
           'Cada sumador complet rep a_i, b_i i el ròssec c_i del sumador de la seva dreta, i dona s_i i el ròssec c_(i+1) al de la seva esquerra. '
           'Una porta XOR rep el ròssec d\'entrada c_(n-1) i el de sortida c_n del darrer sumador i dona el bit de sobreeiximent v.</desc>']
    svg += out + ["</svg>", ""]
    return "\n".join(svg)



FIGURES = {
    "T4_semisumador_sumador_complet.svg": fig_semisumador_sumador_complet,
    "T4_sumador_propagacio_rossec.svg": fig_sumador_propagacio_rossec,
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--output-dir", default="22_figs_originals")
    ap.add_argument("--comprova", action="store_true",
                    help="compara amb els SVG versionats; no escriu res")
    args = ap.parse_args()
    dif = 0
    for name, fig in FIGURES.items():
        path = os.path.join(args.output_dir, name)
        if args.comprova:
            actual = open(path).read() if os.path.exists(path) else None
            if actual != fig():
                print(f"DIFEREIX: {path}", file=sys.stderr)
                dif += 1
            continue
        with open(path, "w") as f:
            f.write(fig())
        print(path)
    sys.exit(1 if dif else 0)
