#!/usr/bin/env python3
"""
gen_T8.py — Genera les figures de T8 (A8): memòria virtual.

    python3 25_scripts/gen_T8.py [--output-dir 22_figs_originals] [--comprova]

Escriu nou SVG natius a `22_figs_originals/`, un per especificació
`<!-- fig-mv-… -->` d'A8:

- `T8_mv_espais.svg` (`#fig-mv-espais`): els espais lògics de dos processos,
  la MMU, la memòria física i el disc.
- `T8_mv_pagines_marcs.svg` (`#fig-mv-pagines-marcs`): pàgines de dos
  processos assignades a marcs, i una que és al disc.
- `T8_mv_taula_pagines.svg` (`#fig-mv-taula-pagines`): la taula de pàgines,
  indexada pel VPN, i el registre de taula de pàgines.
- `T8_mv_taula_multinivell.svg` (`#fig-mv-taula-multinivell`): la taula de
  dos nivells de Sv32, amb la descomposició de l'adreça lògica.
- `T8_mv_tlb_estructura.svg` (`#fig-mv-tlb-estructura`): el TLB com a còpia
  parcial de la taula de pàgines.
- `T8_mv_flux_traduccio.svg` (`#fig-mv-flux-traduccio`): el diagrama de flux
  de la traducció. Substitueix el placeholder.
- `T8_mv_comparticio.svg` (`#fig-mv-comparticio`): dues taules de pàgines que
  apunten al mateix marc.
- `T8_mv_pipt.svg` i `T8_mv_vipt.svg` (`#fig-mv-pipt`, `#fig-mv-vipt`): la
  integració del TLB i la memòria cau, en sèrie i en paral·lel.

Les dades són les dels exemples d'A8: la taula de pàgines i el TLB de
`#tip-mv-tlb-exemple`, i la compartició de `#tip-mv-comparticio`. Colors de
T8 (`13_contrib.qmd §Paleta de colors`): blau i verd per als processos P1 i
P2, blau per a les PTE vàlides, groc per al TLB, vermell per al disc i la
fallada de pàgina, i, com a T7, blau per a la memòria cau i verd per a la
memòria principal.

Model (a) de la fase 7c (`24_specs/svg.md §17`): el font versionat és l'SVG, i
aquest script el regenera; `--comprova` el compara amb el versionat sense
escriure res.
"""
import argparse
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figlib  # noqa: E402
from figlib import t, caixa, fletxa, svg  # noqa: E402

SANS, MONO, INK, GRIS = figlib.SANS, figlib.MONO, figlib.INK, figlib.GRAY
TRAC, NEUTRE = "#adb5bd", "#f8f9fa"
P1_F, P1_S = "#cfe2ff", "#084298"        # procés 1, PTE vàlides, memòria cau
P2_F, P2_S = "#d1e7dd", "#0a3622"        # procés 2, memòria principal
TLB_F, TLB_S = "#fff3cd", "#664d03"      # TLB i fallada de TLB
DISC_F, DISC_S = "#f8d7da", "#842029"    # disc
HIT_F, HIT_S = "#c8ebd8", "#198754"      # encert (diagrama de flux)
MISS_F, MISS_S = "#f8d0d3", "#dc3545"    # fallada de pàgina (diagrama de flux)

# La taula de pàgines i el TLB de #tip-mv-tlb-exemple (estat inicial).
TAULA = [('0x00000', '1', '0', '1', '0x01'),
         ('0x00001', '0', '0', '1', '—'),
         ('0x00002', '1', '0', '1', '0x02'),
         ('0x00003', '1', '1', '1', '0x00'),
         ('0x00004', '0', '0', '1', '—')]
TLB = [('0x00003', '1', '1', '1', '0x00'),
       ('0x00000', '1', '0', '1', '0x01'),
       ('0x00002', '1', '0', '1', '0x02'),
       ('0x0AFB3', '0', '0', '0', '—')]


# ── Primitives ───────────────────────────────────────────────

def linies(cx, cy, ls, size=13, color=INK, bold=False):
    """Línies centrades verticalment a cy; un element de ls pot ser (text, mida, color)."""
    ls = [l if isinstance(l, tuple) else (l, size, color) for l in ls]
    alt = [round(m * 1.25) for _, m, _ in ls]
    y = cy - sum(alt) / 2
    o = []
    for (s, m, c), h in zip(ls, alt):
        y += h
        o.append(t(cx, round(y - h * 0.3), s, m, c, bold=bold and m == size))
    return '\n'.join(o)


def cel(x, y, w, h, fill, stroke, s='', color=INK, size=11, mono=True, sw=1):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if s == '⋮':
        size, mono = 14, False
    if s:
        o += t(x + w / 2, y + h / 2 + size / 3 + 0.5, s, size, color, mono=mono)
    return o


def idx(x, y, s, size=11):
    """Índex d'una fila, a fora i a l'esquerra; els punts suspensius, en sans."""
    if s == '⋮':
        return t(x, y + 1, s, 14, GRIS, 'end')
    return t(x, y, s, size, GRIS, 'end', mono=True)


def cami(pts, color=INK, w=1.2, dash=None, cap=True):
    """Polilínia amb punta triangular al final (sense marcadors, com figlib.fletxa)."""
    d = ' '.join(f'{x},{y}' for x, y in pts)
    a = f' stroke-dasharray="{dash}"' if dash else ''
    o = [f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round"{a}/>']
    if cap:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - 8 * math.cos(ang - 0.4), y2 - 8 * math.sin(ang - 0.4))
        p2 = (x2 - 8 * math.cos(ang + 0.4), y2 - 8 * math.sin(ang + 0.4))
        o.append(f'<polygon points="{x2},{y2} {round(p1[0], 1)},{round(p1[1], 1)} {round(p2[0], 1)},{round(p2[1], 1)}" fill="{color}"/>')
    return '\n'.join(o)


def disc(x, y, w, h, fill=DISC_F, stroke=DISC_S):
    """Cilindre: el cos i l'el·lipse de dalt."""
    rx, ry = w / 2, 8
    cos = (f'<path d="M{x},{y + ry} v{h - 2 * ry} a{rx},{ry} 0 0 0 {w},0 v{-(h - 2 * ry)}" '
           f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    tapa = f'<ellipse cx="{x + rx}" cy="{y + ry}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
    return cos + '\n' + tapa


def taula(x, y, cols, files, h=22, index=None, cap='VPN'):
    """Taula amb capçalera. cols: [(nom, amplada)]; files: [(valors, fill, stroke)].
    Amb index, els VPN van a fora, a l'esquerra, perquè la taula de pàgines no els desa."""
    o = []
    xx = x
    if index is not None:
        o.append(t(x - 8, y - 8, cap, 11, GRIS, 'end', bold=True))
    for nom, w in cols:
        o.append(t(xx + w / 2, y - 8, nom, 11, INK, bold=True))
        xx += w
    for r, (vals, fill, stroke) in enumerate(files):
        yy = y + r * h
        if index is not None:
            o.append(idx(x - 8, yy + h / 2 + 4, index[r]))
        xx = x
        for (nom, w), v in zip(cols, vals):
            color = GRIS if fill == NEUTRE else stroke
            o.append(cel(xx, yy, w, h, fill, stroke, v, color))
            xx += w
    return o


def node(cx, cy, w, h, ls, fill, stroke, forma='rect', size=13):
    if forma == 'rombe':
        f = (f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
    else:
        rx = h / 2 if forma == 'terminal' else 6
        f = (f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="{rx}" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
    return f + '\n' + linies(cx, cy, ls, size)


def llegenda(x, y, items):
    o = []
    for fill, stroke, s in items:
        o.append(f'<rect x="{x}" y="{y - 9}" width="14" height="11" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        o.append(t(x + 20, y, s, 10, GRIS, 'start'))
        x += 26 + len(s) * 5.4
    return o


# ── Espais d'adreçament ──────────────────────────────────────

def espais():
    o = []
    Y0, H = 56, 240
    pagines = {'1': [('A', 76), ('B', 146), ('C', 236)], '2': [('X', 96), ('Y', 206)]}
    for p, x, (f, s) in (('1', 60, (P1_F, P1_S)), ('2', 530, (P2_F, P2_S))):
        cx = x + 45
        o.append(t(cx, 20, f'Procés {p}', 12, s, bold=True))
        o.append(t(cx, 34, 'espai lògic', 10, GRIS, italic=True))
        o.append(t(cx, Y0 - 6, '0x00000000', 10, GRIS, mono=True))
        o.append(t(cx, Y0 + H + 14, '0xFFFFFFFF', 10, GRIS, mono=True))
        o.append(cel(x, Y0, 90, H, NEUTRE, TRAC))
        for lletra, y in pagines[p]:
            o.append(cel(x, y, 90, 20, f, s, lletra, s, 12, mono=False))
    o.append(caixa(280, Y0, 120, 44, NEUTRE, GRIS, 'MMU', 13))
    o.append(fletxa(156, 78, 278, 78, INK, doble=False))
    o.append(fletxa(524, 78, 402, 78, INK, doble=False))
    o.append(t(216, 70, 'adreça lògica', 10, GRIS))
    o.append(t(464, 70, 'adreça lògica', 10, GRIS))
    o.append(fletxa(340, 100, 340, 128, INK, doble=False))
    o.append(t(348, 119, 'adreça física', 10, GRIS, 'start'))
    marcs = [('A', '1'), ('Y', '2'), None, ('B', '1'), ('X', '2'), None, None]
    for k, m in enumerate(marcs):
        y = 130 + k * 20
        if m:
            f, s = (P1_F, P1_S) if m[1] == '1' else (P2_F, P2_S)
            o.append(cel(290, y, 100, 20, f, s, m[0], s, 12, mono=False))
        else:
            o.append(cel(290, y, 100, 20, NEUTRE, TRAC))
    o.append(t(400, 204, 'Memòria física', 12, INK, 'start', bold=True))
    o.append(fletxa(340, 274, 340, 298, INK))
    o.append(t(348, 290, 'pàgines', 10, GRIS, 'start'))
    o.append(disc(280, 300, 120, 74))
    o.append(t(410, 344, 'Disc', 12, INK, 'start', bold=True))
    for k, (lletra, p) in enumerate([('A', '1'), ('B', '1'), ('C', '1'), ('X', '2'), ('Y', '2')]):
        f, s = (P1_F, P1_S) if p == '1' else (P2_F, P2_S)
        o.append(cel(291 + k * 20, 334, 18, 18, f, s, lletra, s, 10, mono=False))
    o += llegenda(60, 402, [(P1_F, P1_S, 'pàgina del procés 1'), (P2_F, P2_S, 'pàgina del procés 2'),
                            (NEUTRE, TRAC, 'espai sense ús o marc lliure')])
    return svg(680, 414, "Espais d'adreçament lògic i físic",
               "A banda i banda, l'espai lògic de dos processos, cadascun de 0x00000000 a 0xFFFFFFFF, amb poques "
               "pàgines en ús: A, B i C del procés 1 i X i Y del procés 2. Totes dues columnes envien adreces "
               "lògiques a la MMU, al centre, que en tradueix cadascuna en una adreça física. A sota de la MMU, la "
               "memòria física, més petita, té set marcs: A, Y, B i X ocupen quatre marcs, en un ordre que no és el "
               "dels espais lògics, i tres són lliures. A sota, el disc conté les cinc pàgines; C només hi és al "
               "disc.", o)


# ── Pàgines i marcs ──────────────────────────────────────────

def pagines_marcs():
    o = []
    dx = 15
    X, XM = 80 + dx, 420 + dx
    for p, y0, (f, s) in (('1', 36, (P1_F, P1_S)), ('2', 156, (P2_F, P2_S))):
        o.append(t(X + 50, y0 - 10, f'Procés {p}', 12, s, bold=True))
        for k in range(2):
            o.append(cel(X, y0 + k * 26, 100, 26, f, s, f'VPN {k}', s, 11, mono=False))
        o.append(t(X + 50, y0 + 68, '⋮', 14, GRIS))
    o.append(t(XM + 50, 26, 'Memòria física', 12, INK, bold=True))
    marcs = [('P2 · VPN 0', P2_F, P2_S), ('P1 · VPN 0', P1_F, P1_S), ('P2 · VPN 1', P2_F, P2_S), None]
    for k, m in enumerate(marcs):
        y = 36 + k * 26
        if m:
            o.append(cel(XM, y, 100, 26, m[1], m[2], m[0], m[2], 10, mono=False))
        else:
            o.append(cel(XM, y, 100, 26, NEUTRE, TRAC))
            o.append(t(XM + 50, y + 17, 'lliure', 10, GRIS, italic=True))
        o.append(t(XM + 108, y + 17, f'PPN {k}', 10, GRIS, 'start', mono=True))
    o.append(disc(XM, 170, 100, 70))
    o.append(cel(XM + 12, 200, 76, 22, P1_F, P1_S, 'P1 · VPN 1', P1_S, 10, mono=False))
    o.append(t(XM + 108, 215, 'Disc', 12, INK, 'start', bold=True))
    xa, xb = X + 100, XM - 2
    o.append(cami([(xa, 49), (xb, 75)], P1_S))
    o.append(cami([(xa, 75), (XM + 10, 211)], P1_S, dash='5,3'))
    o.append(cami([(xa, 169), (xb, 49)], P2_S))
    o.append(cami([(xa, 195), (xb, 101)], P2_S))
    return svg(680, 256, 'Pàgines i marcs de pàgina',
               "A l'esquerra, les pàgines VPN 0 i VPN 1 del procés 1, en blau, i del procés 2, en verd, amb punts "
               "suspensius per a la resta. A la dreta, la memòria física, amb quatre marcs, de PPN 0 a PPN 3, i el "
               "disc a sota. Les fletxes assignen VPN 0 del procés 1 a PPN 1, VPN 0 del procés 2 a PPN 0 i VPN 1 del "
               "procés 2 a PPN 2; PPN 3 és lliure. VPN 1 del procés 1 no és a la memòria física: una fletxa "
               "discontínua la porta al disc.", o)


# ── Taula de pàgines ─────────────────────────────────────────

def files_taula(x=None):
    files = [((v, d, e, ppn), P1_F if v == '1' else NEUTRE, P1_S if v == '1' else TRAC)
             for _, v, d, e, ppn in TAULA]
    files += [(('⋮',) * 4, NEUTRE, TRAC), (('0', '0', '1', '—'), NEUTRE, TRAC)]
    return files, [vpn for vpn, *_ in TAULA] + ['⋮', '0xFFFFF']


def taula_pagines():
    o = []
    X, Y = 290, 64
    cols = [('V', 40), ('D', 40), ('E', 40), ('PPN', 70)]
    files, index = files_taula()
    o += taula(X, Y, cols, files, index=index, cap='VPN')
    o.append(t(X + 95, 22, 'Taula de pàgines', 12, INK, bold=True))
    o.append(caixa(50, 20, 150, 40, NEUTRE, GRIS, '', 11))
    o.append(linies(125, 40, ['Registre de', 'taula de pàgines'], 11))
    o.append(cami([(200, 40), (X, 40), (X, Y - 2)], INK))
    o.append(t(245, 34, 'adreça base', 10, GRIS))
    yb = Y + len(files) * 22
    xr = X + 190 + 16
    o.append(f'<line x1="{xr}" y1="{Y}" x2="{xr}" y2="{yb}" stroke="{GRIS}" stroke-width="1"/>')
    for yy in (Y, yb):
        o.append(f'<line x1="{xr - 4}" y1="{yy}" x2="{xr + 4}" y2="{yy}" stroke="{GRIS}" stroke-width="1"/>')
    o.append(f'<text x="{xr + 8}" y="{(Y + yb) / 2 + 4}" font-family="{SANS}" font-size="11" fill="{GRIS}" '
             f'text-anchor="start">2<tspan dy="-5" font-size="8">20</tspan><tspan dx="3" dy="5">entrades</tspan></text>')
    return svg(680, yb + 20, 'La taula de pàgines',
               "Una taula de columnes V, D, E i PPN, indexada pel VPN, que s'escriu a fora, a l'esquerra, de 0x00000 "
               "a 0x00004, punts suspensius i 0xFFFFF, amb una cota de 2 elevat a 20 entrades. Les entrades 0x00000, "
               "0x00002 i 0x00003 tenen V = 1 i un PPN, 0x01, 0x02 i 0x00, i són en blau; les altres tenen V = 0, sense "
               "PPN, en gris. El registre de taula de pàgines, a dalt a l'esquerra, apunta amb una fletxa a l'inici "
               "de la taula: l'adreça base.", o)


# ── Taula de pàgines multinivell ─────────────────────────────

def taula_multinivell():
    o = []
    # Adreça lògica de 32 bits, a 10 px per bit.
    for x, w, s, n, mono in ((200, 100, 'VPN[1]', 10, True), (300, 100, 'VPN[0]', 10, True),
                             (400, 120, 'desplaçament', 12, False)):
        o.append(cel(x, 28, w, 26, NEUTRE, GRIS, s, INK, 11, mono=mono))
        o.append(t(x + w / 2, 20, f'{n} bits', 10, GRIS))
    o.append(t(190, 45, 'Adreça lògica', 11, INK, 'end', bold=True))

    def nivell(x, y, index, valides):
        files = []
        for i in index:
            if i == '⋮':
                files.append((('⋮',), NEUTRE, TRAC))
            elif i in valides:
                files.append((('V = 1',), P1_F, P1_S))
            else:
                files.append((('V = 0',), NEUTRE, TRAC))
        r = []
        for k, ((v,), f, s) in enumerate(files):
            r.append(cel(x, y + k * 22, 100, 22, f, s, v, s if f != NEUTRE else GRIS, 11, mono=False))
            r.append(idx(x - 8, y + k * 22 + 15, index[k], 10))
        return r

    index = ['0', '1', '⋮', '1023']
    o += nivell(200, 120, index, {'0', '1023'})
    o.append(t(250, 228, 'Taula de primer nivell', 11, INK, bold=True))
    o.append(t(250, 242, '(directori de pàgines)', 10, GRIS))
    o.append(t(250, 256, '1024 entrades', 10, GRIS))
    o.append(t(308, 157, 'sense taula de segon nivell', 10, GRIS, 'start', italic=True))
    for y, valides in ((120, {'0', '1'}), (290, {'1', '1023'})):
        o += nivell(460, y, index, valides)
        o.append(t(510, y + 108, 'Taula de segon nivell', 11, INK, bold=True))
        o.append(t(510, y + 122, '1024 PTE', 10, GRIS))
    o.append(caixa(40, 100, 110, 40, NEUTRE, GRIS, '', 11))
    o.append(linies(95, 120, ['Registre de', 'taula de pàgines'], 11))
    o.append(fletxa(150, 120, 198, 120, INK, doble=False))
    o.append(fletxa(250, 54, 250, 118, INK, doble=False))
    o.append(t(256, 92, 'índex', 10, GRIS, 'start', italic=True))
    o.append(cami([(350, 54), (350, 96), (510, 96), (510, 118)], INK))
    o.append(t(356, 80, 'índex', 10, GRIS, 'start', italic=True))
    o.append(cami([(300, 131), (458, 120.5)], P1_S))
    o.append(cami([(300, 197), (458, 289)], P1_S))
    return svg(680, 430, 'Taula de pàgines de dos nivells (Sv32)',
               "A dalt, l'adreça lògica de 32 bits dividida en VPN[1], de 10 bits, VPN[0], de 10 bits, i el "
               "desplaçament, de 12 bits. VPN[1] indexa la taula de primer nivell, o directori de pàgines, de 1024 "
               "entrades, a la qual apunta el registre de taula de pàgines. Les entrades 0 i 1023 del directori són "
               "vàlides, V = 1, i apunten cadascuna a una taula de segon nivell, de 1024 PTE, que indexa VPN[0]. "
               "L'entrada 1 té V = 0 i no té taula de segon nivell.", o)


# ── El TLB ───────────────────────────────────────────────────

def tlb_estructura():
    o = []
    cols = [('V', 34), ('D', 34), ('E', 34), ('PPN', 56)]
    files, index = files_taula()
    XP, Y = 120, 62
    o += taula(XP, Y, cols, files, index=index, cap='VPN')
    o.append(t(XP + 79, 22, 'Taula de pàgines', 12, INK, bold=True))
    o.append(t(XP + 79, 36, '(a la memòria principal)', 10, GRIS))
    XT = 400
    ftlb = [((vpn, v, d, e, ppn), TLB_F if v == '1' else NEUTRE, TLB_S if v == '1' else TRAC)
            for vpn, v, d, e, ppn in TLB]
    o += taula(XT, Y, [('VPN', 76)] + cols, ftlb)
    o.append(t(XT + 117, 22, 'TLB', 12, INK, bold=True))
    o.append(t(XT + 117, 36, '(a la MMU)', 10, GRIS))
    xa, xb = XP + 158, XT - 2
    fila = {vpn: k for k, (vpn, *_) in enumerate(TAULA)}
    for k, (vpn, *_r) in enumerate(TLB):
        if vpn in fila:
            o.append(cami([(xa, Y + fila[vpn] * 22 + 11), (xb, Y + k * 22 + 11)], TLB_S, dash='5,3'))
    o.append(t((xa + xb) / 2, 54, 'còpia', 10, GRIS, italic=True))
    return svg(680, Y + len(files) * 22 + 20, 'La taula de pàgines i el TLB',
               "A l'esquerra, la taula de pàgines, a la memòria principal, amb columnes V, D, E i PPN i el VPN a fora "
               "com a índex, de 0x00000 a 0x00004 i 0xFFFFF; les entrades vàlides, en blau. A la dreta, el TLB, a la "
               "MMU, amb quatre entrades i una columna VPN més: 0x00003, 0x00000 i 0x00002, vàlides i en groc, i "
               "0x0AFB3, amb V = 0, en gris. Tres fletxes discontínues porten cada PTE vàlida de la taula a l'entrada "
               "del TLB que n'és còpia. Són les dades de l'exemple de traducció amb TLB.", o)


# ── Diagrama de flux de la traducció ─────────────────────────

def flux():
    o = []
    L, C, R, S = 150, 440, 690, 870
    r = [50, 130, 210, 290, 370, 450, 530, 610]
    ab_f, ab_s = NEUTRE, GRIS
    # Fletxes primer, perquè els nodes les tapin.
    o.append(cami([(C, 72), (C, 97)]))
    o.append(cami([(C, 162), (C, 177)]))
    o.append(cami([(345, r[1]), (267, r[1])]))
    o.append(cami([(L, 163), (L, 187)]))
    o.append(cami([(L - 115, r[2]), (15, r[2]), (15, r[0]), (328, r[0])], TLB_S))
    o.append(cami([(C, 242), (C, 257)]))
    o.append(cami([(535, r[2]), (603, r[2])]))
    o.append(cami([(345, r[3]), (267, r[3])]))
    o.append(cami([(C, 322), (C, 337)]))
    o.append(cami([(345, r[4]), (267, r[4])]))
    o.append(cami([(C, 402), (C, 427)]))
    o.append(cami([(L, 392), (L, r[5]), (308, r[5])]))
    o.append(cami([(775, r[2]), (803, r[2])]))
    o.append(cami([(R, 242), (R, 257)]))
    o.append(cami([(775, r[3]), (803, r[3])]))
    o.append(cami([(R, 322), (R, 427)]))
    o.append(cami([(S, 318), (S, 337)]))
    o.append(cami([(805, r[4]), (R, r[4])], cap=False))
    o.append(figlib.dot(R, r[4]))
    o.append(cami([(S, 402), (S, 421)]))
    o.append(cami([(805, r[5]), (777, r[5])]))
    o.append(cami([(R, 472), (R, 507)]))
    o.append(cami([(R, 552), (R, 587)]))
    o.append(cami([(775, r[7]), (948, r[7]), (948, r[0]), (552, r[0])], MISS_S))
    # Rètols de les branques.
    for x, y, s, a in ((C + 6, 174, 'sí', 'start'), (306, r[1] - 6, 'no', 'middle'),
                       (C + 6, 254, 'sí', 'start'), (569, r[2] - 6, 'no', 'middle'),
                       (306, r[3] - 6, 'sí', 'middle'), (C + 6, 334, 'no', 'start'),
                       (306, r[4] - 6, 'sí', 'middle'), (C + 6, 418, 'no', 'start'),
                       (789, r[2] - 6, 'no', 'middle'), (R + 6, 254, 'sí', 'start'),
                       (789, r[3] - 6, 'no', 'middle'), (R + 6, 340, 'sí', 'start'),
                       (797, r[4] - 6, 'no', 'end'), (S + 6, 416, 'sí', 'start')):
        o.append(t(x, y, s, 12, INK, a, italic=True))
    # Nodes.
    o.append(node(C, r[0], 220, 44, ['Cerca el VPN al TLB'], HIT_F, HIT_S))
    o.append(node(C, r[1], 190, 64, ['Encert de TLB?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[2], 190, 64, ['V = 1?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[3], 190, 64, ['Escriptura', 'i E = 0?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[4], 190, 64, ['Escriptura', 'i D = 0?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[5], 260, 44, ["Accés a la dada amb l'adreça", 'física (PPN i desplaçament)'],
                  HIT_F, HIT_S, 'terminal'))
    o.append(node(L, r[1], 230, 66, ['Llegeix la PTE de la taula', 'de pàgines i copia-la al TLB',
                                     ('(a una entrada amb V = 0 o,', 10, GRIS),
                                     ('si no n’hi ha, a la LRU)', 10, GRIS)],
                  TLB_F, TLB_S))
    o.append(node(L, r[2], 230, 44, ["Reintenta l'accés"], TLB_F, TLB_S))
    o.append(node(L, r[3], 230, 44, ['El SO avorta', 'el procés'], ab_f, ab_s, 'terminal'))
    o.append(node(L, r[4], 230, 44, ['Posa D = 1 al TLB i a la PTE'], HIT_F, HIT_S))
    o.append(node(R, r[2], 170, 64, ['Adreça', 'vàlida?'], MISS_F, MISS_S, 'rombe'))
    o.append(node(S, r[2], 130, 44, ['El SO avorta', 'el procés'], ab_f, ab_s, 'terminal'))
    o.append(node(R, r[3], 170, 64, ['Hi ha cap', 'marc lliure?'], MISS_F, MISS_S, 'rombe'))
    o.append(node(S, r[3], 130, 56, ['Tria una pàgina', 'víctima (LRU):', 'V = 0 a la PTE'], MISS_F, MISS_S))
    o.append(node(S, r[4], 130, 64, ['D = 1?'], MISS_F, MISS_S, 'rombe'))
    o.append(node(S, r[5], 130, 56, ['Escriu la', 'víctima al disc'], MISS_F, MISS_S))
    o.append(node(R, r[5], 170, 44, ['Carrega la pàgina', 'del disc al marc'], MISS_F, MISS_S))
    o.append(node(R, r[6], 170, 44, ['Actualitza la PTE', '(V = 1 i PPN)'], MISS_F, MISS_S))
    o.append(node(R, r[7], 170, 44, ['Reexecuta', 'la instrucció'], MISS_F, MISS_S))
    o.append(t(L, 88, 'Fallada de TLB', 13, TLB_S, bold=True))
    o.append(t(780, 166, 'Fallada de pàgina (la gestiona el SO)', 13, MISS_S, bold=True))
    return svg(960, 650, "Flux complet de traducció d'una adreça",
               "Diagrama de flux en tres columnes. Al centre, en verd, el camí de l'encert: es cerca el VPN al TLB; si "
               "hi és i V = 1, es comprova si és una escriptura amb E = 0, que fa que el SO avorti el procés, i si és "
               "una escriptura amb D = 0, que posa D = 1 al TLB i a la PTE; s'acaba accedint a la dada amb l'adreça "
               "física. A l'esquerra, en groc, la fallada de TLB: es llegeix la PTE, es copia al TLB i es reintenta "
               "l'accés. A la dreta, en vermell, la fallada de pàgina, quan V = 0: si l'adreça no és vàlida, el SO "
               "avorta el procés; si ho és i no hi ha cap marc lliure, es tria una víctima, que s'escriu al disc si "
               "D = 1; després es carrega la pàgina, s'actualitza la PTE i es reexecuta la instrucció. El reintent i "
               "la reexecució tornen a la cerca al TLB.", o)


# ── Compartició ──────────────────────────────────────────────

def comparticio():
    o = []
    cols = [('V', 32), ('D', 32), ('E', 32), ('PPN', 56)]
    taules = (('P1', 52, P1_F, P1_S, [('0x00000', '0x02'), ('0x00001', '0x00')]),
              ('P2', 182, P2_F, P2_S, [('0x00000', '0x03'), ('0x00001', '0x02')]))
    XM = 450
    ymarc = {'0x00': 52, '0x01': 86, '0x02': 120, '0x03': 154}
    for p, y, f, s, valides in taules:
        files = [(('1', '0', '1', ppn), f, s) for _, ppn in valides] + [(('0', '0', '1', '—'), NEUTRE, TRAC)]
        o += taula(80, y, cols, files, index=[v for v, _ in valides] + ['0x00002'], cap='VPN')
        o.append(t(156, y - 30, f'Taula de pàgines de {p}', 12, s, bold=True))
        for k, (_, ppn) in enumerate(valides):
            compartida = ppn == '0x02'
            if compartida:
                o.append(f'<rect x="80" y="{y + k * 22}" width="152" height="22" fill="none" stroke="{s}" stroke-width="2"/>')
            o.append(cami([(232, y + k * 22 + 11), (XM - 2, ymarc[ppn] + 17)], s, 2 if compartida else 1))
    o.append(t(XM + 50, 42, 'Memòria física', 12, INK, bold=True))
    for ppn, y in ymarc.items():
        if ppn == '0x02':
            o.append(f'<rect x="{XM}" y="{y}" width="50" height="34" fill="{P1_F}"/>')
            o.append(f'<rect x="{XM + 50}" y="{y}" width="50" height="34" fill="{P2_F}"/>')
            o.append(f'<rect x="{XM}" y="{y}" width="100" height="34" fill="none" stroke="{INK}" stroke-width="1.5"/>')
            o.append(t(XM + 50, y + 21, 'compartida', 11, INK, bold=True))
        elif ppn == '0x01':
            o.append(cel(XM, y, 100, 34, NEUTRE, TRAC))
            o.append(t(XM + 50, y + 21, 'lliure', 10, GRIS, italic=True))
        else:
            f, s, p = (P1_F, P1_S, 'P1') if ppn == '0x00' else (P2_F, P2_S, 'P2')
            o.append(cel(XM, y, 100, 34, f, s, p, s, 11, mono=False))
        o.append(t(XM + 108, y + 21, f'PPN {ppn}', 10, GRIS, 'start', mono=True))
    return svg(680, 266, 'Compartició de pàgines',
               "A l'esquerra, dues taules de pàgines, de P1 a dalt, en blau, i de P2 a sota, en verd, amb columnes V, "
               "D, E i PPN. A la dreta, la memòria física, amb quatre marcs, de PPN 0x00 a 0x03. A P1, VPN 0x00000 "
               "apunta a PPN 0x02 i VPN 0x00001 a PPN 0x00; a P2, VPN 0x00000 apunta a PPN 0x03 i VPN 0x00001 a "
               "PPN 0x02. Les dues entrades que apunten a PPN 0x02 tenen V = 1 i E = 1, i les seves fletxes, més "
               "gruixudes, convergeixen al marc 0x02, mig blau i mig verd, rotulat «compartida». PPN 0x01 és "
               "lliure.", o)


# ── Integració del TLB i la memòria cau ──────────────────────

def cronograma(y, en_paralel):
    """Cronograma comú a PIPT i VIPT, a la mateixa escala: 90 px per accés."""
    o = [t(20, y + 22, "Temps d'accés", 11, INK, 'start', bold=True)]
    X0 = 160
    if en_paralel:
        o.append(cel(X0, y + 4, 90, 18, TLB_F, TLB_S, 'TLB', TLB_S, 10, mono=False))
        o.append(cel(X0, y + 24, 90, 18, P1_F, P1_S, 'MC', P1_S, 10, mono=False))
        o.append(cel(X0 + 90, y + 14, 24, 18, NEUTRE, GRIS, '=', INK, 11, mono=False))
        o.append(t(X0 + 124, y + 27, 'en paral·lel, i després la comparació', 10, GRIS, 'start', italic=True))
    else:
        o.append(cel(X0, y + 14, 90, 18, TLB_F, TLB_S, 'TLB', TLB_S, 10, mono=False))
        o.append(cel(X0 + 90, y + 14, 90, 18, P1_F, P1_S, 'MC', P1_S, 10, mono=False))
        o.append(t(X0 + 190, y + 27, 'en sèrie', 10, GRIS, 'start', italic=True))
    o.append(fletxa(X0, y + 52, X0 + 400, y + 52, GRIS, doble=False, w=1))
    o.append(t(X0 + 400, y + 66, 'temps', 10, GRIS, 'end', italic=True))
    return o


def pipt():
    o = []
    o.append(caixa(20, 46, 80, 48, NEUTRE, GRIS, 'CPU', 13))
    o.append(caixa(200, 46, 90, 48, TLB_F, TLB_S, 'TLB', 13))
    o.append(caixa(390, 46, 90, 48, P1_F, P1_S, 'MC', 13))
    o.append(caixa(390, 150, 90, 48, P2_F, P2_S, 'MP', 13))
    o.append(fletxa(100, 70, 198, 70, INK, doble=False))
    o.append(t(149, 62, 'adreça lògica', 10, GRIS))
    o.append(fletxa(290, 70, 388, 70, INK, doble=False))
    o.append(t(339, 62, 'adreça física', 10, GRIS))
    o.append(t(339, 86, '(encert de TLB)', 9, GRIS, italic=True))
    o.append(fletxa(480, 70, 578, 70, INK, doble=False))
    o.append(t(529, 62, 'encert', 10, GRIS))
    o.append(t(584, 74, 'dada', 11, INK, 'start', bold=True))
    o.append(fletxa(435, 96, 435, 148, INK))
    o.append(t(443, 126, 'fallada', 10, GRIS, 'start'))
    o += cronograma(222, False)
    return svg(680, 300, 'Memòria cau indexada físicament (PIPT)',
               "Diagrama de blocs en una fila: la CPU envia l'adreça lògica al TLB, en groc; amb un encert de TLB, "
               "l'adreça física passa a la MC, en blau, i amb un encert de MC en surt la dada. Si la MC falla, "
               "accedeix a la MP, en verd, a sota. A sota, el cronograma: l'accés al TLB i el de la MC, un darrere "
               "l'altre, en sèrie.", o)


def vipt():
    o = []
    o.append(caixa(20, 106, 70, 48, NEUTRE, GRIS, 'CPU', 13))
    o.append(fletxa(90, 130, 128, 130, INK, doble=False))
    o.append(t(230, 110, 'adreça lògica', 10, GRIS))
    o.append(cel(130, 117, 100, 26, NEUTRE, GRIS, 'VPN', INK, 11))
    o.append(cel(230, 117, 100, 26, NEUTRE, GRIS, 'desplaçament', INK, 11, mono=False))
    o.append(f'<rect x="400" y="30" width="100" height="60" rx="4" fill="{P1_F}" stroke="{P1_S}" stroke-width="1"/>')
    o.append(linies(450, 60, ['MC', ('(etiquetes i dades)', 9, P1_S)], 13, P1_S, bold=True))
    o.append(caixa(400, 176, 100, 48, TLB_F, TLB_S, 'TLB', 13))
    o.append(cami([(280, 117), (280, 60), (398, 60)]))
    o.append(t(286, 92, 'índex', 10, GRIS, 'start'))
    o.append(cami([(180, 143), (180, 200), (398, 200)]))
    o.append(t(186, 176, 'VPN', 10, GRIS, 'start'))
    o.append(cel(552, 102, 36, 36, NEUTRE, INK, '=', INK, 16, mono=False, sw=1.2))
    o.append(cami([(500, 50), (520, 50), (520, 112), (550, 112)]))
    o.append(t(506, 44, 'etiqueta', 10, GRIS, 'start'))
    o.append(cami([(500, 200), (535, 200), (535, 128), (550, 128)]))
    o.append(t(506, 194, 'PPN', 10, GRIS, 'start'))
    o.append(fletxa(588, 120, 628, 120, INK, doble=False))
    o.append(t(608, 112, 'encert', 10, GRIS))
    o.append(t(634, 124, 'dada', 11, INK, 'start', bold=True))
    o.append(fletxa(570, 138, 570, 250, INK, doble=False))
    o.append(t(576, 200, 'fallada', 10, GRIS, 'start'))
    o.append(caixa(525, 252, 90, 48, P2_F, P2_S, 'MP', 13))
    o += cronograma(322, True)
    return svg(680, 400, 'Memòria cau indexada virtualment i etiquetada físicament (VIPT)',
               "La CPU genera l'adreça lògica, dividida en VPN i desplaçament. Dos camins en paral·lel: a dalt, els "
               "bits del desplaçament indexen la MC, en blau, que en llegeix les etiquetes i les dades; a sota, el VPN "
               "va al TLB, en groc, que dona el PPN. Un comparador, a la dreta, confronta l'etiqueta llegida de la MC "
               "amb el PPN: si coincideixen, encert, i en surt la dada; si no, fallada, i s'accedeix a la MP, en verd. "
               "A sota, el cronograma: el TLB i la MC alhora, i després la comparació.", o)


FIGURES = {
    'T8_mv_espais.svg': espais,
    'T8_mv_pagines_marcs.svg': pagines_marcs,
    'T8_mv_taula_pagines.svg': taula_pagines,
    'T8_mv_taula_multinivell.svg': taula_multinivell,
    'T8_mv_tlb_estructura.svg': tlb_estructura,
    'T8_mv_flux_traduccio.svg': flux,
    'T8_mv_comparticio.svg': comparticio,
    'T8_mv_pipt.svg': pipt,
    'T8_mv_vipt.svg': vipt,
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
                print(f'[gen-T8] DIFEREIX: {ruta}', file=sys.stderr)
                dif += 1
            continue
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contingut)
        print(f'[gen-T8] {ruta}')
    sys.exit(1 if dif else 0)


if __name__ == '__main__':
    main()
