#!/usr/bin/env python3
"""
gen_T8.py — Genera les figures de T8 (A8): memòria virtual.

    python3 25_scripts/gen_T8.py [--output-dir 22_figs_originals] [--comprova]

Escriu els SVG natius de T8 a `22_figs_originals/`, un per figura d'A8
(i els fotogrames de la figura dinàmica):

- `T8_mv_espais.svg` (`#fig-mv-espais`): els espais lògics de dos processos,
  la MMU, la memòria física i el disc.
- `T8_mv_jerarquia.svg` (`#fig-mv-jerarquia`): la piràmide de la jerarquia
  de memòria amb el disc, i els temps d'accés orientatius (figura 7.2 del tema
  antic, amb la geometria de `T7_jerarquia_piramide.svg`).
- `T8_mv_adreca_exemple.svg` (figura sense caption de §Pàgines i marcs):
  l'adreça 0x10010004 descomposta en VPN i desplaçament, com al tema antic.
- `T8_mv_traduccio.svg` (`#fig-mv-traduccio`): la traducció d'una adreça
  lògica de 32 bits a una de física de 14 (figura 7.4 del tema antic).
- `T8_mv_pagines_marcs.svg` (`#fig-mv-pagines-marcs`): pàgines de dos
  processos assignades a marcs, i una que és al disc.
- `T8_mv_taula_pagines.svg` (`#fig-mv-taula-pagines`): la figura 7.5 del tema
  antic, amb el bit E: l'adreça lògica, el registre de taula de pàgines, la
  taula indexada pel VPN i l'adreça física.
- `T8_mv_traduccio_exemple.svg` (`#fig-mv-traduccio-exemple`): la figura 7.6
  del tema antic, la traducció de 0x00001801 amb la taula del procés 2.
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
- `T8_mv_exemple_tlb.svg` (`#fig-mv-tlb-exemple`): la traça dels cinc accessos
  de `#tip-mv-tlb-exemple`, simulats per `simula_exemple()`, i els fotogrames
  `T8_mv_exemple_tlb_pas<k>.svg` (k = 0, l'estat inicial) de la figura
  dinàmica de l'HTML (`figures_dinamiques.html`), amb el TLB, la taula de
  pàgines i la memòria física després de cada accés.

El model del TLB és el del tema (RISC-V, `A8.qmd §Traducció ràpida: el TLB`):
el TLB només conté PTE vàlides, la fallada de TLB la resol la MMU i, en
expulsar una pàgina, el SO n'invalida l'entrada del TLB.

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
         ('0x00004', '0', '0', '1', '—'),
         ('0x00005', '0', '0', '1', '—')]
# Entrades del TLB: (V, VPN, D, E, PPN). La quarta és lliure (V = 0): el TLB només conté PTE vàlides.
TLB = [('1', '0x00003', '1', '1', '0x00'),
       ('1', '0x00000', '0', '1', '0x01'),
       ('1', '0x00002', '0', '1', '0x02'),
       ('0', '—', '—', '—', '—')]
# Accessos de l'exemple (#tip-mv-tlb-exemple): (L/E, adreça lògica).
EX_ACCESSOS = [('E', 0x00002A0B), ('L', 0x00001F21), ('L', 0x0000420C), ('L', 0x00003001), ('L', 0x00005120)]


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
    """Com la figura 7.1 del tema antic: els espais lògics de dos processos amb l'adreça inicial i final de
    cada pàgina, la MMU, una memòria física de 16 KiB (quatre marcs, amb les adreces) i el disc, on només es
    dibuixen les pàgines que no són a la memòria física. Mateixa assignació que `pagines_marcs`."""
    o = []
    H = 26                                   # alçada d'una pàgina o d'un marc
    # Pàgines de cada procés: (lletra, fila), amb fila 0 i 1 les dues primeres i 'ultima' la darrera.
    pagines = {'1': [('A', 0), ('B', 1), ('C', 'ultima')], '2': [('X', 0), ('Y', 1)]}
    marcs = [('X', '2'), ('A', '1'), ('Y', '2'), ('C', '1')]        # PPN 0 a 3
    nomes_disc = [('B', '1')]
    Y0 = 56
    files = {0: Y0, 1: Y0 + H, 'ultima': Y0 + 2 * H + 44}          # y de cada fila de pàgina
    H_COL = files['ultima'] + H - Y0
    adreces = {0: ('0x00000000', '0x00000FFF'), 1: ('0x00001000', '0x00001FFF'),
               'ultima': ('0xFFFFF000', '0xFFFFFFFF')}
    for p, x, (f, sk), costat in (('1', 110, (P1_F, P1_S), 'end'), ('2', 500, (P2_F, P2_S), 'start')):
        cx = x + 45
        o.append(t(cx, 22, f'Procés {p}', 12, sk, bold=True))
        o.append(t(cx, 36, 'espai lògic', 10, GRIS, italic=True))
        o.append(cel(x, Y0, 90, H_COL, NEUTRE, TRAC))
        # Les tres files de pàgines (amb buit i punts suspensius entre la segona i la darrera).
        for fila, (ini, fi) in adreces.items():
            y = files[fila]
            o.append(f'<line x1="{x}" y1="{y}" x2="{x + 90}" y2="{y}" stroke="{TRAC}" stroke-width="1"/>')
            o.append(f'<line x1="{x}" y1="{y + H}" x2="{x + 90}" y2="{y + H}" stroke="{TRAC}" stroke-width="1"/>')
            xa = x - 6 if costat == 'end' else x + 96
            o.append(t(xa, y + 8, ini, 8, GRIS, costat, mono=True))
            o.append(t(xa, y + H - 2, fi, 8, GRIS, costat, mono=True))
        o.append(t(cx, files[1] + H + 28, '⋮', 14, GRIS))
        for lletra, fila in pagines[p]:
            o.append(cel(x, files[fila], 90, H, f, sk, lletra, sk, 12, mono=False))
    # MMU i memòria física.
    o.append(caixa(290, Y0, 100, 40, NEUTRE, GRIS, 'MMU', 13))
    o.append(fletxa(201, Y0 + 20, 288, Y0 + 20, INK, doble=False))
    o.append(fletxa(499, Y0 + 20, 392, Y0 + 20, INK, doble=False))
    o.append(t(245, Y0 + 12, 'adreça lògica', 9, GRIS))
    o.append(t(445, Y0 + 12, 'adreça lògica', 9, GRIS))
    YM = Y0 + 70
    o.append(fletxa(340, Y0 + 40, 340, YM - 18, INK, doble=False))
    o.append(t(334, Y0 + 54, 'adreça física', 9, GRIS, 'end'))
    o.append(t(340, YM - 5, 'Memòria física', 11, INK, bold=True))
    for k, (lletra, p) in enumerate(marcs):
        y = YM + k * H
        f, sk = (P1_F, P1_S) if p == '1' else (P2_F, P2_S)
        o.append(cel(290, y, 100, H, f, sk, lletra, sk, 12, mono=False))
        o.append(t(284, y + 8, f'0x{k:X}000', 8, GRIS, 'end', mono=True))
        o.append(t(284, y + H - 2, f'0x{k:X}FFF', 8, GRIS, 'end', mono=True))
        o.append(t(396, y + H / 2 + 3, f'PPN {k}', 9, GRIS, 'start', mono=True))
    # Disc: només les pàgines que no són a la memòria física.
    YD = YM + 4 * H + 20
    XD = 180                                 # el disc, a sota a l'esquerra, perquè la fletxa no travessi els marcs
    o.append(disc(XD, YD, 100, 66))
    o.append(t(XD + 108, YD + 40, 'Disc', 11, INK, 'start', bold=True))
    for k, (lletra, p) in enumerate(nomes_disc):
        f, sk = (P1_F, P1_S) if p == '1' else (P2_F, P2_S)
        o.append(cel(XD + 36 + k * 30, YD + 26, 28, 22, f, sk, lletra, sk, 11, mono=False))
    # Fletxes de les pàgines als marcs (contínues) i al disc (discontínua).
    for k, (lletra, p) in enumerate(marcs):
        x = 110 if p == '1' else 500
        fila = next(fi for l, fi in pagines[p] if l == lletra)
        y = files[fila] + H / 2
        xa = x + 90 if p == '1' else x
        o.append(cami([(xa, y), (290 if p == '1' else 390, YM + k * H + H / 2)],
                      P1_S if p == '1' else P2_S, 1))
    for lletra, p in nomes_disc:
        x = 110 if p == '1' else 500
        fila = next(fi for l, fi in pagines[p] if l == lletra)
        o.append(cami([(x + 90, files[fila] + H / 2), (XD + 50, YD + 24)], P1_S, 1, dash='5,3'))
    o += llegenda(110, YD + 90, [(P1_F, P1_S, 'pàgina del procés 1'), (P2_F, P2_S, 'pàgina del procés 2'),
                                 (NEUTRE, TRAC, 'espai lògic sense ús')])
    return svg(680, YD + 100, "Espais d'adreçament lògic i físic",
               "A banda i banda, l'espai lògic de dos processos, de 0x00000000 a 0xFFFFFFFF, amb l'adreça inicial "
               "i final de cada pàgina de 4 KiB: el procés 1, en blau, usa les pàgines A (0x00000000) i B "
               "(0x00001000) i la darrera, C (0xFFFFF000); el procés 2, en verd, usa X (0x00000000) i Y "
               "(0x00001000). Les dues columnes envien adreces lògiques a la MMU, al centre, que les tradueix a "
               "adreces físiques. A sota, la memòria física de 16 KiB, amb quatre marcs: X a 0x0000, A a 0x1000, "
               "Y a 0x2000 i C a 0x3000, en un ordre que no és el dels espais lògics. A sota, el disc, amb la "
               "pàgina B, que no és a la memòria física i hi arriba amb una fletxa discontínua.", o)


# ── Jerarquia de memòria amb el disc ─────────────────────────

def jerarquia():
    """La piràmide de la figura 7.2 del tema antic, amb la geometria i els colors de la de T7
    (`T7_jerarquia_piramide.svg`), les anotacions originals (proper, ràpid, car, petit / llunyà, lent, barat,
    gran) i, a la dreta, el temps d'accés orientatiu de cada nivell."""
    o = []
    nivells = [('Registres', P1_F, P1_S, '~0,25 ns'),
               ('Memòria cau (SRAM)', P2_F, P2_S, '0,5 – 5 ns'),
               ('Memòria principal (DRAM)', TLB_F, TLB_S, '50 – 100 ns'),
               ('Disc (SSD)', DISC_F, DISC_S, '0,05 – 0,1 ms')]
    cx, y0, h, pend = 300, 20, 52, 0.83          # centre, y del vèrtex, alçada de nivell, mig-amplada per px
    for k, (nom, f, sk, temps) in enumerate(nivells):
        ya, yb = y0 + k * (h + 4), y0 + k * (h + 4) + h
        wa, wb = (ya - y0) * pend, (yb - y0) * pend
        if k == 0:
            pts = f'{cx},{ya} {cx + wb},{yb} {cx - wb},{yb}'
        else:
            pts = f'{cx - wa},{ya} {cx + wa},{ya} {cx + wb},{yb} {cx - wb},{yb}'
        o.append(f'<polygon points="{pts}" fill="{f}" stroke="{sk}" stroke-width="1"/>')
        o.append(t(cx, (ya + yb) / 2 + 4 + (6 if k == 0 else 0), nom if k else 'Regs.', 12, sk, bold=True))
        xt = cx + (y0 + 4 * (h + 4) - 4 - y0) * pend + 56    # els temps, alineats en una sola columna
        o.append(t(xt, (ya + yb) / 2 + 4, temps, 11, INK, 'start', mono=True))
        o.append(f'<line x1="{cx + wb + 8}" y1="{(ya + yb) / 2}" x2="{xt - 8}" y2="{(ya + yb) / 2}" '
                 f'stroke="{TRAC}" stroke-width="1" stroke-dasharray="3,3"/>')
    yb = y0 + 4 * (h + 4) - 4
    o.append(t(cx + (yb - y0) * pend + 56, y0 - 4, "temps d'accés", 11, GRIS, 'start', italic=True))
    # Anotacions de la figura antiga: a l'esquerra, cap amunt; a la dreta... totes dues a l'esquerra, com a 7.2.
    xa = 60
    o.append(f'<line x1="{xa}" y1="{yb}" x2="{xa}" y2="{y0 + 8}" stroke="{GRIS}" stroke-width="1"/>')
    o.append(f'<polygon points="{xa},{y0} {xa - 4},{y0 + 12} {xa + 4},{y0 + 12}" fill="{GRIS}"/>')
    o.append(linies(xa + 26, y0 + 40, [('proper', 11, GRIS), ('ràpid', 11, GRIS), ('car', 11, GRIS), ('petit', 11, GRIS)], 11))
    xb = 60
    o.append(linies(xb + 26, yb - 38, [('llunyà', 11, GRIS), ('lent', 11, GRIS), ('barat', 11, GRIS), ('gran', 11, GRIS)], 11))
    o.append(f'<polygon points="{xb},{yb + 8} {xb - 4},{yb - 4} {xb + 4},{yb - 4}" fill="{GRIS}"/>')
    return svg(680, yb + 24, 'Jerarquia de memòria en un computador amb memòria virtual',
               "Piràmide de quatre nivells, de dalt a baix: registres, memòria cau (SRAM), memòria principal "
               "(DRAM) i disc (SSD). A la dreta de cada nivell, el temps d'accés orientatiu: 0,25 ns, de 0,5 a 5 "
               "ns, de 50 a 100 ns i de 0,05 a 0,1 ms. A l'esquerra, una fletxa vertical: cap amunt, els nivells "
               "són més propers, ràpids, cars i petits; cap avall, més llunyans, lents, barats i grans.", o)


# ── Exemple d'adreça lògica: VPN i desplaçament ─────────────

def adreca_exemple():
    """Figura sense caption de §Pàgines i marcs (la del tema antic): l'adreça 0x10010004 descomposta en
    VPN (20 bits) i desplaçament (12 bits), en binari."""
    o = []
    X, Y, H = 196, 30, 40
    o.append(t(X - 10, Y + H / 2 + 5, '<tspan font-style="italic">A</tspan> = 0x10010004 =', 13, INK, 'end'))
    o.append(cel(X, Y, 300, H, NEUTRE, INK, '', sw=1.2))
    o.append(cel(X + 300, Y, 180, H, NEUTRE, INK, '', sw=1.2))
    o.append(t(X + 150, Y + H / 2 + 5, '0001 0000 0000 0001 0000', 15, INK, mono=True))
    o.append(t(X + 390, Y + H / 2 + 5, '0000 0000 0100', 15, INK, mono=True))
    o.append(t(X + 150, Y - 8, 'VPN', 11, INK, bold=True))
    o.append(t(X + 390, Y - 8, 'desplaçament', 11, INK, bold=True))
    o.append(t(X + 150, Y + H + 14, '20 bits', 10, GRIS))
    o.append(t(X + 390, Y + H + 14, '12 bits', 10, GRIS))
    return svg(680, Y + H + 22, "Descomposició de l'adreça lògica 0x10010004 en VPN i desplaçament",
               "L'adreça lògica A = 0x10010004, escrita en binari dins de dues caselles: a l'esquerra, els 20 bits "
               "de més pes, 0001 0000 0000 0001 0000, que són el VPN, i a la dreta, els 12 bits de menys pes, "
               "0000 0000 0100, que són el desplaçament dins la pàgina.", o)


# ── Pàgines i marcs ──────────────────────────────────────────

def pagines_marcs():
    """Com la figura 7.3 del tema antic, amb el format dels espais lògics de `espais`: les dues columnes
    senceres (de 0x00000000 a 0xFFFFFFFF) amb VPN 0 i VPN 1 de cada procés, la memòria física de 16 KiB amb
    les adreces de cada marc i el PPN, i el disc, on només hi ha la pàgina que no és a la memòria."""
    o = []
    H = 26
    Y0 = 56
    files = {0: Y0, 1: Y0 + H, 'ultima': Y0 + 2 * H + 44}
    H_COL = files['ultima'] + H - Y0
    adreces = {0: ('0x00000000', '0x00000FFF'), 1: ('0x00001000', '0x00001FFF'),
               'ultima': ('0xFFFFF000', '0xFFFFFFFF')}
    for p, x, (f, sk), costat in (('1', 110, (P1_F, P1_S), 'end'), ('2', 500, (P2_F, P2_S), 'start')):
        cx = x + 45
        o.append(t(cx, 22, f'Procés {p}', 12, sk, bold=True))
        o.append(t(cx, 36, 'espai lògic', 10, GRIS, italic=True))
        o.append(cel(x, Y0, 90, H_COL, NEUTRE, TRAC))
        for fila, (ini, fi) in adreces.items():
            y = files[fila]
            o.append(f'<line x1="{x}" y1="{y}" x2="{x + 90}" y2="{y}" stroke="{TRAC}" stroke-width="1"/>')
            o.append(f'<line x1="{x}" y1="{y + H}" x2="{x + 90}" y2="{y + H}" stroke="{TRAC}" stroke-width="1"/>')
            xa = x - 6 if costat == 'end' else x + 96
            o.append(t(xa, y + 8, ini, 8, GRIS, costat, mono=True))
            o.append(t(xa, y + H - 2, fi, 8, GRIS, costat, mono=True))
        o.append(t(cx, files[1] + H + 28, '⋮', 14, GRIS))
        for k in range(2):
            o.append(cel(x, files[k], 90, H, f, sk, f'VPN {k}', sk, 11, mono=False))
    # Memòria física de 16 KiB: quatre marcs amb les adreces i el PPN.
    XM, YM = 290, Y0 + 8
    o.append(t(XM + 50, YM - 10, 'Memòria física', 12, INK, bold=True))
    marcs = [('P2 · VPN 0', P2_F, P2_S), ('P1 · VPN 0', P1_F, P1_S), ('P2 · VPN 1', P2_F, P2_S), None]
    for k, m in enumerate(marcs):
        y = YM + k * H
        if m:
            o.append(cel(XM, y, 100, H, m[1], m[2], m[0], m[2], 10, mono=False))
        else:
            o.append(cel(XM, y, 100, H, NEUTRE, TRAC))
            o.append(t(XM + 50, y + 17, 'lliure', 10, GRIS, italic=True))
        o.append(t(XM - 6, y + 8, f'0x{k:X}000', 8, GRIS, 'end', mono=True))
        o.append(t(XM - 6, y + H - 2, f'0x{k:X}FFF', 8, GRIS, 'end', mono=True))
        o.append(t(XM + 106, y + H - 3, f'PPN {k}', 9, GRIS, 'start', mono=True))
    # Disc: només la pàgina que no és a la memòria física.
    YD = YM + 4 * H + 30
    o.append(disc(XM, YD, 100, 66))
    o.append(cel(XM + 12, YD + 26, 76, 22, P1_F, P1_S, 'P1 · VPN 1', P1_S, 10, mono=False))
    o.append(t(XM + 108, YD + 40, 'Disc', 12, INK, 'start', bold=True))
    # Fletxes: VPN 0 de P1 → PPN 1; VPN 0 de P2 → PPN 0; VPN 1 de P2 → PPN 2; VPN 1 de P1 → disc.
    o.append(cami([(200, files[0] + H / 2), (XM - 2, YM + 1 * H + H / 2)], P1_S))
    o.append(cami([(500, files[0] + H / 2), (XM + 102, YM + 0 * H + H / 2)], P2_S))
    o.append(cami([(500, files[1] + H / 2), (XM + 102, YM + 2 * H + H / 2)], P2_S))
    o.append(cami([(200, files[1] + H / 2), (216, files[1] + H / 2), (216, YD + 37), (XM - 2, YD + 37)], P1_S, dash='5,3'))
    return svg(680, YD + 80, 'Pàgines i marcs de pàgina',
               "A banda i banda, l'espai lògic de dos processos, de 0x00000000 a 0xFFFFFFFF, amb l'adreça inicial i "
               "final de cada pàgina de 4 KiB; el procés 1, en blau, i el procés 2, en verd, fan servir VPN 0 i VPN 1 "
               "cadascun. Al centre, la memòria física de 16 KiB, amb quatre marcs de 0x0000 a 0x3FFF i els seus "
               "PPN: PPN 0 conté VPN 0 del procés 2, PPN 1 conté VPN 0 del procés 1, PPN 2 conté VPN 1 del procés 2 "
               "i PPN 3 és lliure. A sota, el disc, amb VPN 1 del procés 1, que no és a la memòria física i hi arriba "
               "amb una fletxa discontínua que baixa per l'esquerra de la memòria.", o)


# ── Traducció d'una adreça lògica a una de física ───────────

def traduccio():
    """La figura 7.4 del tema antic: l'adreça lògica de 32 bits (VPN de 20 bits i desplaçament de 12), el
    bloc de traducció, i l'adreça física de 14 bits (PPN de 2 bits i el mateix desplaçament)."""
    o = []
    B = 13                                   # amplada d'un bit
    XL, YL = 160, 40                         # adreça lògica
    H = 30
    wv, wo = 20 * B, 12 * B
    o.append(t(XL - 10, YL + H / 2 + 5, 'Adreça lògica', 12, INK, 'end', bold=True))
    o.append(cel(XL, YL, wv, H, NEUTRE, INK, 'VPN', INK, 12, mono=False, sw=1.2))
    o.append(cel(XL + wv, YL, wo, H, NEUTRE, INK, 'desplaçament', INK, 12, mono=False, sw=1.2))
    for k in range(32):                      # números de bit, de 31 a 0
        o.append(t(XL + (31 - k) * B + B / 2, YL - 4, str(k), 7, GRIS, mono=True))
    o.append(t(XL + wv / 2, YL - 18, '20 bits', 9, GRIS))
    o.append(t(XL + wv + wo / 2, YL - 18, '12 bits', 9, GRIS))
    # Bloc de traducció i adreça física, alineada per la dreta.
    YT = YL + H + 26
    XT = XL + wv - 70
    o.append(caixa(XT, YT, 110, 36, TLB_F, TLB_S, 'traducció', 12))
    YF = YT + 36 + 26
    wp = 2 * B
    XP = XL + wv - wp
    o.append(t(XP - 10, YF + H / 2 + 5, 'Adreça física', 12, INK, 'end', bold=True))
    o.append(cel(XP, YF, wp, H, NEUTRE, INK, 'PPN', INK, 10, mono=False, sw=1.2))
    o.append(cel(XL + wv, YF, wo, H, NEUTRE, INK, 'desplaçament', INK, 12, mono=False, sw=1.2))
    for k in range(14):
        o.append(t(XL + wv + wo - (k + 1) * B + B / 2, YF + H + 10, str(k), 7, GRIS, mono=True))
    o.append(t(XP + wp / 2, YF + H + 22, '2 bits', 9, GRIS))
    o.append(t(XL + wv + wo / 2, YF + H + 22, '12 bits', 9, GRIS))
    # Fletxes: VPN → traducció → PPN; desplaçament → desplaçament.
    o.append(fletxa(XT + 55, YL + H, XT + 55, YT - 2, INK, doble=False))
    o.append(fletxa(XT + 55, YT + 36, XT + 55, YF - 2, INK, doble=False))
    o.append(fletxa(XL + wv + wo / 2, YL + H, XL + wv + wo / 2, YF - 2, INK, doble=False))
    return svg(680, YF + H + 30, "Traducció d'una adreça lògica a una adreça física",
               "A dalt, l'adreça lògica de 32 bits, amb els números de bit de 31 a 0: el VPN ocupa els 20 bits de "
               "més pes i el desplaçament els 12 de menys pes. El VPN entra a un bloc de traducció, que en treu el "
               "PPN, de 2 bits; el desplaçament baixa sense canvis. A sota, l'adreça física de 14 bits: el PPN i el "
               "mateix desplaçament, amb els números de bit de 13 a 0.", o)


# ── Taula de pàgines ─────────────────────────────────────────

def files_taula(x=None):
    files = [((v, d, e, ppn), P1_F if v == '1' else NEUTRE, P1_S if v == '1' else TRAC)
             for _, v, d, e, ppn in TAULA]
    files += [(('⋮',) * 4, NEUTRE, TRAC), (('0', '0', '1', '—'), NEUTRE, TRAC)]
    return files, [vpn for vpn, *_ in TAULA] + ['⋮', '0xFFFFF']


def taula_pagines(exemple=False):
    """La figura 7.5 del tema antic, amb el bit E: l'adreça lògica (VPN i desplaçament), el registre de taula
    de pàgines, que n'apunta la base, la taula indexada pel VPN amb els bits V, D i E i el PPN, i l'adreça
    física, formada pel PPN de l'entrada i el mateix desplaçament. Amb `exemple`, la figura 7.6: la traducció
    de 0x00001801 amb la taula de pàgines del procés 2 de `pagines_marcs` (VPN 1 → PPN 2 → 0x2801)."""
    o = []
    B, H = 13, 28
    XL, YL = 200, 40                          # adreça lògica: VPN (20 bits) i desplaçament (12 bits)
    wv, wo = 20 * B, 12 * B
    if exemple:
        vpn_s, off_s, ppn_s = '0000 0000 0000 0000 0001', '1000 0000 0001', '10'
    else:
        vpn_s, off_s, ppn_s = 'VPN', 'desplaçament', 'PPN'
    mono = exemple
    o.append(t(XL - 10, YL + H / 2 + (0 if exemple else 5), 'Adreça lògica', 12, INK, 'end', bold=True))
    if exemple:
        o.append(t(XL - 10, YL + H / 2 + 14, '0x00001801', 10, GRIS, 'end', mono=True))
    o.append(cel(XL, YL, wv, H, NEUTRE, INK, vpn_s, INK, 12, mono=mono, sw=1.2))
    o.append(cel(XL + wv, YL, wo, H, NEUTRE, INK, off_s, INK, 12, mono=mono, sw=1.2))
    for k in range(32):
        o.append(t(XL + (31 - k) * B + B / 2, YL - 4, str(k), 7, GRIS, mono=True))
    o.append(t(XL + wv / 2, YL - 18, 'VPN (20 bits)' if exemple else '20 bits', 9, GRIS))
    o.append(t(XL + wv + wo / 2, YL - 18, 'desplaçament (12 bits)' if exemple else '12 bits', 9, GRIS))
    # Taula de pàgines.
    XT, YT, h = 230, 112, 22
    cols = [('V', 34), ('D', 34), ('E', 34), ('PPN', 70)]
    wt = sum(w for _, w in cols)
    xx = XT
    for nom, w in cols:
        o.append(t(xx + w / 2, YT - 8, nom, 11, INK, bold=True))
        xx += w
    if exemple:                                # (índex, valors, seleccionada)
        files = [('0', ('1', '0', '1', '00'), False), ('1', ('1', '0', '1', '10'), True),
                 ('⋮', ('⋮',) * 4, False), ('fi', ('0', '0', '1', '—'), False)]
    else:
        files = [('0', ('',) * 4, False), ('1', ('',) * 4, False), ('⋮', ('⋮',) * 4, False),
                 ('', ('',) * 4, True), ('⋮', ('⋮',) * 4, False), ('fi', ('',) * 4, False)]
    ysel = None
    for r, (f, vals, sel) in enumerate(files):
        y = YT + r * h
        xx = XT
        for (nom, w), v in zip(cols, vals):
            o.append(cel(xx, y, w, h, P1_F if sel else NEUTRE, P1_S if sel else TRAC, v,
                         P1_S if sel else GRIS))
            xx += w
        if f == 'fi':
            o.append(t(XT - 8, y + h / 2 + 4, '2<tspan dy="-4" font-size="8">20</tspan><tspan dy="4"> − 1</tspan>',
                       11, GRIS, 'end', mono=True))
        elif f:
            o.append(idx(XT - 8, y + h / 2 + 4, f))
        if sel:
            ysel = y + h / 2
    yb = YT + len(files) * h
    o.append(t(XT + wt / 2, yb + 18, 'Taula de pàgines de P2' if exemple else 'Taula de pàgines', 11 if exemple else 12,
               INK, bold=True))   # entre els camins de V i del PPN
    if exemple:                                # els camins surten de la vora de les cel·les, no del valor
        xv, xppn, y0 = XT + 7, XT + wt - 10, ysel + h / 2
    else:
        xv, xppn, y0 = XT + 17, XT + 102 + 35, ysel
        o.append(figlib.dot(xv, ysel, P1_S))
        o.append(figlib.dot(xppn, ysel, P1_S))
    # Registre de taula de pàgines: n'apunta la base.
    o.append(caixa(20, 78, 150, 40, NEUTRE, GRIS, '', 11))
    o.append(linies(95, 98, ['Registre de', 'taula de pàgines'], 11))
    o.append(cami([(170, 98), (XT, 98), (XT, YT - 2)], INK))
    o.append(t(190, 92, 'adreça base', 9, GRIS, 'start', italic=True))
    # El VPN indexa la taula: entra per la dreta a la fila seleccionada.
    xi = XL + wv - 30
    o.append(cami([(xi, YL + H), (xi, ysel), (XT + wt + 2, ysel)], INK))
    o.append(t(xi + 6, YT + 40, 'índex', 10, GRIS, 'start', italic=True))
    # Adreça física: PPN (2 bits) i desplaçament (12 bits), alineada amb el desplaçament lògic.
    YF = yb + 64
    wp = 2 * B
    XP = XL + wv - wp
    o.append(t(XP - 10, YF + H / 2 + (0 if exemple else 5), 'Adreça física', 12, INK, 'end', bold=True))
    if exemple:
        o.append(t(XP - 10, YF + H / 2 + 14, '0x2801', 10, GRIS, 'end', mono=True))
    o.append(cel(XP, YF, wp, H, NEUTRE, INK, ppn_s, INK, 10 if not exemple else 12, mono=mono, sw=1.2))
    o.append(cel(XL + wv, YF, wo, H, NEUTRE, INK, off_s, INK, 12, mono=mono, sw=1.2))
    for k in range(14):
        o.append(t(XL + wv + wo - (k + 1) * B + B / 2, YF + H + 10, str(k), 7, GRIS, mono=True))
    o.append(t(XP + wp / 2, YF + H + 22, 'PPN' if exemple else '2 bits', 9, GRIS))
    o.append(t(XL + wv + wo / 2, YF + H + 22, 'desplaçament' if exemple else '12 bits', 9, GRIS))
    o.append(cami([(xppn, y0), (xppn, yb + 30), (XP + wp / 2, yb + 30), (XP + wp / 2, YF - 2)], P1_S))
    o.append(fletxa(XL + wv + wo / 2, YL + H, XL + wv + wo / 2, YF - 2, INK, doble=False))
    # El bit V: anotació a l'esquerra.
    o.append(cami([(xv, y0), (XT + 7, y0), (XT + 7, yb + 30), (178, yb + 30)], P1_S))   # per dins de la columna V
    if exemple:
        o.append(linies(95, yb + 30, [('V = 1:', 10, P1_S), ('la pàgina és a la', 10, GRIS),
                                      ('memòria física', 10, GRIS)], 10))
        return svg(680, YF + H + 30, "Exemple de traducció d'una adreça amb la taula de pàgines",
                   "Traducció de l'adreça lògica 0x00001801 amb la taula de pàgines del procés 2. A dalt, l'adreça en "
                   "binari: VPN 0000 0000 0000 0000 0001, és a dir, 1, i desplaçament 1000 0000 0001. El registre de "
                   "taula de pàgines apunta a la base de la taula, amb columnes V, D, E i PPN: l'entrada 0 té V = 1 i "
                   "PPN 00, l'entrada 1, destacada en blau, té V = 1 i PPN 10, i la darrera, 2 elevat a 20 menys 1, té "
                   "V = 0. El VPN 1 selecciona l'entrada 1; el seu bit V = 1 indica que la pàgina és a la memòria "
                   "física, i el seu PPN, 10, baixa a l'adreça física, on s'ajunta amb el desplaçament 1000 0000 0001: "
                   "l'adreça física és 0x2801.", o)
    o.append(linies(95, yb + 30, [('Bit de validesa (V):', 10, P1_S), ('si és 0, la pàgina no és', 10, GRIS),
                                  ('a la memòria física;', 10, GRIS), ('si és 1, hi és', 10, GRIS)], 10))
    return svg(680, YF + H + 30, 'La taula de pàgines',
               "A dalt, l'adreça lògica de 32 bits: VPN, de 20 bits, i desplaçament, de 12. El registre de taula de "
               "pàgines, a l'esquerra, apunta a l'adreça base de la taula de pàgines, que té 2 elevat a 20 entrades, "
               "de 0 a 2 elevat a 20 menys 1, amb columnes V, D, E i PPN. El VPN fa d'índex i selecciona una "
               "entrada, destacada en blau. Del bit V de l'entrada surt una anotació: si és 0, la pàgina no és a "
               "la memòria física; si és 1, hi és. El PPN de l'entrada baixa fins a l'adreça física, de 14 bits, "
               "on s'ajunta amb el desplaçament de l'adreça lògica, que es conserva.", o)


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
    ftlb = [((v, vpn if v == '1' else '', d, e, ppn), TLB_F if v == '1' else NEUTRE, TLB_S if v == '1' else TRAC)
            for v, vpn, d, e, ppn in TLB]
    ctlb = [('V', 34), ('VPN', 76), ('D', 34), ('E', 34), ('PPN', 56)]
    o += taula(XT, Y, ctlb, ftlb)
    o.append(t(XT + 117, 22, 'TLB', 12, INK, bold=True))
    o.append(t(XT + 117, 36, '(a la MMU)', 10, GRIS))
    o.append(t(XT + 72, Y + 3 * 22 + 15, 'lliure', 10, GRIS, italic=True))
    xa, xb = XP + 158, XT - 2
    fila = {vpn: k for k, (vpn, *_) in enumerate(TAULA)}
    for k, (v, vpn, *_r) in enumerate(TLB):
        if vpn in fila:
            o.append(cami([(xa, Y + fila[vpn] * 22 + 11), (xb, Y + k * 22 + 11)], TLB_S, dash='5,3'))
    o.append(t((xa + xb) / 2, 54, 'còpia', 10, GRIS, italic=True))
    return svg(680, Y + len(files) * 22 + 20, 'La taula de pàgines i el TLB',
               "A l'esquerra, la taula de pàgines, a la memòria principal, amb columnes V, D, E i PPN i el VPN a fora "
               "com a índex, de 0x00000 a 0x00005 i 0xFFFFF; les entrades vàlides, en blau. A la dreta, el TLB, a la "
               "MMU, amb quatre entrades i columnes V, VPN, D, E i PPN: tres entrades vàlides, en groc, amb els VPN "
               "0x00003, 0x00000 i 0x00002, i una quarta entrada lliure, amb V = 0, en gris. Tres fletxes "
               "discontínues porten cada PTE vàlida de la taula a l'entrada del TLB que n'és còpia. Són les dades "
               "inicials de l'exemple de traducció amb TLB.", o)


# ── Diagrama de flux de la traducció ─────────────────────────

def flux():
    """Flux de la traducció al model del tema (RISC-V): a l'esquerra, l'encert de TLB; al centre, la fallada
    de TLB, que resol la MMU sense interrompre el programa; a la dreta, la fallada de pàgina, que és una
    excepció i la resol el SO. Els dos camins que no acaben a la dada tornen a la cerca al TLB."""
    o = []
    C, L, R = 300, 560, 790          # columnes: encert, fallada de TLB, fallada de pàgina
    E = 95                           # sortides laterals de l'encert (excepció de protecció, bit D)
    r = [50, 130, 210, 290, 370, 440, 510, 580, 650, 720]
    yl = r[4] + 50                   # el retorn de la fallada de TLB passa per sota de l'accés a la dada
    ab_f, ab_s = NEUTRE, GRIS
    # Fletxes primer, perquè els nodes les tapin.
    o.append(cami([(C, 72), (C, 97)]))                                     # cerca → encert?
    o.append(cami([(C, 162), (C, 177)]))                                   # encert? sí → E = 0?
    o.append(cami([(395, r[1]), (443, r[1])]))                              # encert? no → llegeix la PTE
    o.append(cami([(205, r[2]), (172, r[2])]))                              # E = 0? sí → excepció de protecció
    o.append(cami([(C, 242), (C, 257)]))                                   # E = 0? no → D = 0?
    o.append(cami([(205, r[3]), (172, r[3])]))                              # D = 0? sí → posa D = 1
    o.append(cami([(E, r[3] + 22), (E, r[4]), (168, r[4])]))                # posa D = 1 → accés a la dada
    o.append(cami([(C, 322), (C, 347)]))                                   # D = 0? no → accés a la dada
    o.append(cami([(L, 163), (L, 177)]))                                   # llegeix la PTE → V = 1?
    o.append(cami([(L, 242), (L, 257)]))                                   # V = 1? sí → copia la PTE al TLB
    o.append(cami([(655, r[2]), (713, r[2])]))                              # V = 1? no → adreça vàlida?
    o.append(cami([(L, r[3] + 33), (L, yl), (15, yl), (15, r[0]), (188, r[0])], TLB_S))  # → cerca
    o.append(cami([(865, r[2]), (872, r[2])]))                              # adreça vàlida? no → el SO avorta
    o.append(cami([(R, 242), (R, 257)]))                                   # adreça vàlida? sí → marc lliure?
    o.append(cami([(715, r[3]), (690, r[3]), (690, r[7]), (703, r[7])]))    # marc lliure? sí → carrega
    o.append(cami([(R, 322), (R, 341)]))                                   # marc lliure? no → tria la víctima
    o.append(cami([(R, r[4] + 29), (R, r[5] - 33)]))                        # víctima → D = 1?
    o.append(cami([(R, r[5] + 32), (R, r[6] - 23)]))                        # D = 1? sí → escriu al disc
    ym = (r[6] + r[7]) / 2
    o.append(cami([(865, r[5]), (895, r[5]), (895, ym), (R, ym)], cap=False))  # D = 1? no → carrega
    o.append(figlib.dot(R, ym))
    o.append(cami([(R, r[6] + 22), (R, r[7] - 23)]))                        # escriu → carrega
    o.append(cami([(R, r[7] + 22), (R, r[8] - 23)]))                        # carrega → actualitza la PTE
    o.append(cami([(R, r[8] + 22), (R, r[9] - 23)]))                        # actualitza → reexecuta
    o.append(cami([(875, r[9]), (955, r[9]), (955, r[0]), (412, r[0])], MISS_S))  # reexecuta → cerca
    # Rètols de les branques.
    for x, y, s, a in ((C + 6, 174, 'sí', 'start'), (419, r[1] - 6, 'no', 'middle'),
                       (188, r[2] - 6, 'sí', 'middle'), (C + 6, 254, 'no', 'start'),
                       (188, r[3] - 6, 'sí', 'middle'), (C + 6, 338, 'no', 'start'),
                       (L + 6, 254, 'sí', 'start'), (684, r[2] - 6, 'no', 'middle'),
                       (R + 6, 254, 'sí', 'start'), (868, r[2] - 6, 'no', 'end'),
                       (702, r[3] - 6, 'sí', 'middle'), (R + 6, 336, 'no', 'start'),
                       (R + 6, r[5] + 43, 'sí', 'start'), (880, r[5] - 6, 'no', 'middle')):
        o.append(t(x, y, s, 12, INK, a, italic=True))
    # Nodes.
    o.append(node(C, r[0], 220, 44, ['Cerca el VPN al TLB'], HIT_F, HIT_S))
    o.append(node(C, r[1], 190, 64, ['Encert de TLB?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[2], 190, 64, ['Escriptura', 'i E = 0?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[3], 190, 64, ['Escriptura', 'i D = 0?'], HIT_F, HIT_S, 'rombe'))
    o.append(node(C, r[4], 260, 44, ["Accés a la dada amb l'adreça", 'física (PPN i desplaçament)'],
                  HIT_F, HIT_S, 'terminal'))
    o.append(node(E, r[2], 150, 56, ['Excepció de', 'protecció: el SO', 'avorta el procés'], ab_f, ab_s, 'terminal', 12))
    o.append(node(E, r[3], 150, 44, ['Posa D = 1 al', 'TLB i a la PTE'], HIT_F, HIT_S))
    o.append(node(L, r[1], 230, 66, ['Llegeix la PTE de la', 'taula de pàgines',
                                     ('(recorregut per maquinari,', 10, GRIS),
                                     ('sense interrompre el programa)', 10, GRIS)], TLB_F, TLB_S))
    o.append(node(L, r[2], 190, 64, ['V = 1?'], TLB_F, TLB_S, 'rombe'))
    o.append(node(L, r[3], 230, 66, ['Copia la PTE al TLB', ('(a una entrada lliure o,', 10, GRIS),
                                     ('si no n’hi ha, a la LRU)', 10, GRIS)], TLB_F, TLB_S))
    o.append(node(R, r[2], 150, 64, ['Adreça', 'vàlida?'], MISS_F, MISS_S, 'rombe'))
    o.append(node(912, r[2], 78, 44, ['El SO avorta', 'el procés'], ab_f, ab_s, 'terminal', 10))
    o.append(node(R, r[3], 150, 64, ['Hi ha cap', 'marc lliure?'], MISS_F, MISS_S, 'rombe'))
    o.append(node(R, r[4], 170, 58, ['Tria la víctima (LRU):', 'V = 0 a la seva PTE', 'i invalida-la del TLB'],
                  MISS_F, MISS_S, size=12))
    o.append(node(R, r[5], 150, 64, ['D = 1?'], MISS_F, MISS_S, 'rombe'))
    o.append(node(R, r[6], 170, 44, ['Escriu la víctima', 'al disc'], MISS_F, MISS_S))
    o.append(node(R, r[7], 170, 44, ['Carrega la pàgina', 'del disc al marc'], MISS_F, MISS_S))
    o.append(node(R, r[8], 170, 44, ['Actualitza la PTE', '(V = 1, D = 0 i PPN)'], MISS_F, MISS_S))
    o.append(node(R, r[9], 170, 44, ['Reexecuta', 'la instrucció'], MISS_F, MISS_S))
    o.append(t(L, 86, 'Fallada de TLB (la resol la MMU)', 13, TLB_S, bold=True))
    o.append(t(R, 166, 'Fallada de pàgina (la resol el SO)', 13, MISS_S, bold=True))
    o.append(t(C, 20, 'Encert de TLB', 13, HIT_S, bold=True))
    return svg(960, r[9] + 50, "Flux complet de traducció d'una adreça",
               "Diagrama de flux en tres columnes. A l'esquerra, en verd, el camí de l'encert: es cerca el VPN al "
               "TLB; si hi és, es comprova si és una escriptura amb E = 0, que provoca una excepció de protecció i "
               "el SO avorta el procés, i si és una escriptura amb D = 0, que posa D = 1 al TLB i a la PTE; s'acaba "
               "accedint a la dada amb l'adreça física. Al centre, en groc, la fallada de TLB, que resol la MMU: "
               "llegeix la PTE de la taula de pàgines i, si V = 1, la copia al TLB i torna a la cerca, que ara "
               "encerta. A la dreta, en vermell, la fallada de pàgina, quan la PTE té V = 0, que resol el SO: si "
               "l'adreça no és vàlida, avorta el procés; si ho és i no hi ha cap marc lliure, tria una víctima, "
               "posa V = 0 a la seva PTE i n'invalida l'entrada del TLB, i l'escriu al disc si D = 1; després "
               "carrega la pàgina, actualitza la PTE amb V = 1, D = 0 i el PPN, i reexecuta la instrucció, que "
               "torna a la cerca al TLB.", o)


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


# ── Exemple de traducció amb TLB: simulació i figures ───────

def simula_exemple():
    """Simula els accessos de #tip-mv-tlb-exemple al model del tema: TLB completament associatiu amb LRU
    que només conté PTE vàlides, recorregut per maquinari, i invalidació de l'entrada del TLB de la pàgina
    víctima. Retorna els estats (inicial i després de cada accés) amb l'esdeveniment que els ha produït."""
    import copy
    t_bits = 12
    tp = {0: dict(v=1, d=0, ppn=1), 1: dict(v=0, d=0, ppn=None), 2: dict(v=1, d=0, ppn=2),
          3: dict(v=1, d=1, ppn=0), 4: dict(v=0, d=0, ppn=None), 5: dict(v=0, d=0, ppn=None)}
    tlb = [dict(v=1, vpn=3, d=1, ppn=0), dict(v=1, vpn=0, d=0, ppn=1), dict(v=1, vpn=2, d=0, ppn=2),
           dict(v=0, vpn=None, d=0, ppn=None)]
    marcs = {0: 3, 1: 0, 2: 2, 3: None}
    lru_pag = [3, 0, 2]          # de més antic a més recent
    lru_tlb = [3, 0, 2]

    def foto(k, ev):
        return dict(k=k, ev=ev, tp=copy.deepcopy(tp), tlb=copy.deepcopy(tlb), marcs=dict(marcs),
                    lru=list(lru_pag))
    estats = [foto(0, None)]
    for k, (op, adr) in enumerate(EX_ACCESSOS, 1):
        vpn, off = adr >> t_bits, adr & ((1 << t_bits) - 1)
        ev = dict(op=op, adr=adr, vpn=vpn, tlb_miss=False, pf=False, victima=None, disc=False, d=False,
                  canvi_tlb=set(), canvi_tp=set(), canvi_marcs=set())
        hit = any(e['v'] and e['vpn'] == vpn for e in tlb)
        if not hit:
            ev['tlb_miss'] = True
            if not tp[vpn]['v']:                       # fallada de pàgina: la resol el SO
                ev['pf'] = True
                lliures = [p for p, v in marcs.items() if v is None]
                if lliures:
                    ppn = lliures[0]
                else:
                    victima = lru_pag.pop(0)
                    ppn = tp[victima]['ppn']
                    ev['victima'], ev['disc'] = victima, tp[victima]['d'] == 1
                    tp[victima] = dict(v=0, d=0, ppn=None)
                    ev['canvi_tp'].add(victima)
                    for n, e in enumerate(tlb):        # invalidació de l'entrada del TLB de la víctima
                        if e['v'] and e['vpn'] == victima:
                            tlb[n] = dict(v=0, vpn=None, d=0, ppn=None)
                            ev['canvi_tlb'].add(n)
                    lru_tlb.remove(victima)
                marcs[ppn] = vpn
                tp[vpn] = dict(v=1, d=0, ppn=ppn)
                ev['canvi_tp'].add(vpn)
                ev['canvi_marcs'].add(ppn)
            # Recorregut per maquinari: la PTE (ara vàlida) es copia al TLB.
            n = next((n for n, e in enumerate(tlb) if not e['v']), None)
            if n is None:
                vell = lru_tlb.pop(0)
                n = next(n for n, e in enumerate(tlb) if e['v'] and e['vpn'] == vell)
            tlb[n] = dict(v=1, vpn=vpn, d=tp[vpn]['d'], ppn=tp[vpn]['ppn'])
            ev['canvi_tlb'].add(n)
        if op == 'E' and tp[vpn]['d'] == 0:            # primera escriptura: D = 1 al TLB i a la PTE
            tp[vpn]['d'] = 1
            for n, e in enumerate(tlb):
                if e['v'] and e['vpn'] == vpn:
                    e['d'] = 1
                    ev['canvi_tlb'].add(n)
            ev['canvi_tp'].add(vpn)
            ev['d'] = True
        lru_pag = [x for x in lru_pag if x != vpn] + [vpn]
        lru_tlb = [x for x in lru_tlb if x != vpn] + [vpn]
        ev['ppn'] = tp[vpn]['ppn']
        ev['fisica'] = (ev['ppn'] << t_bits) | off
        estats.append(foto(k, ev))
    return estats


def ex_text(ev):
    """Les línies d'explicació d'un accés, per a la traça i els fotogrames."""
    op = 'Escriptura' if ev['op'] == 'E' else 'Lectura'
    l1 = f"{op} a 0x{ev['adr']:08X} → VPN 0x{ev['vpn']:05X}"
    if not ev['tlb_miss']:
        l2 = 'Encert de TLB.' + (' Primera escriptura: D = 1 al TLB i a la PTE.' if ev['d'] else '')
    elif not ev['pf']:
        l2 = 'Fallada de TLB; la PTE té V = 1 i es copia al TLB.'
    elif ev['victima'] is None:
        l2 = 'Fallada de TLB i de pàgina: es carrega la pàgina al marc lliure.'
    else:
        l2 = (f"Fallada de TLB i de pàgina: víctima VPN {ev['victima']}"
              + (', escrita al disc (D = 1)' if ev['disc'] else ' (D = 0, no cal escriure-la)')
              + '; se n’invalida l’entrada del TLB.')
    l3 = f"PPN 0x{ev['ppn']:02X} → adreça física 0x{ev['fisica']:04X}"
    return l1, l2, l3


def ex_tlb(o, x, y, est, cols_vpn=True, h=20, canvis=()):
    """El TLB d'un estat: columnes V, VPN, D, (E,) PPN; les entrades canviades en aquest pas, amb vora gruixuda."""
    cols = [('V', 24), ('VPN', 64), ('D', 24)] + ([('E', 24)] if cols_vpn else []) + [('PPN', 44)]
    files = []
    for n, e in enumerate(est['tlb']):
        if e['v']:
            vals = ['1', f"0x{e['vpn']:05X}", str(e['d'])] + (['1'] if cols_vpn else []) + [f"0x{e['ppn']:02X}"]
            files.append((tuple(vals), TLB_F, TLB_S))
        else:
            files.append((('0', '', '—') + (('—',) if cols_vpn else ()) + ('—',), NEUTRE, TRAC))
    o += taula(x, y, cols, files, h=h)
    w = sum(wc for _, wc in cols)
    for n, e in enumerate(est['tlb']):
        if not e['v']:
            o.append(t(x + 24 + 32, y + n * h + h / 2 + 4, 'lliure', 10, GRIS, italic=True))
        if n in canvis:
            o.append(f'<rect x="{x}" y="{y + n * h}" width="{w}" height="{h}" fill="none" stroke="{INK}" stroke-width="2"/>')
    return w


def ex_tp(o, x, y, est, h=20, canvis=()):
    """La taula de pàgines d'un estat (VPN 0 a 5), amb l'índex a fora."""
    cols = [('V', 24), ('D', 24), ('E', 24), ('PPN', 44)]
    files, index = [], []
    for vpn in range(6):
        e = est['tp'][vpn]
        if e['v']:
            files.append((('1', str(e['d']), '1', f"0x{e['ppn']:02X}"), P1_F, P1_S))
        else:
            files.append((('0', '0', '1', '—'), NEUTRE, TRAC))
        index.append(f'0x{vpn:05X}')
    o += taula(x, y, cols, files, h=h, index=index, cap='VPN')
    w = sum(wc for _, wc in cols)
    for vpn in canvis:
        o.append(f'<rect x="{x}" y="{y + vpn * h}" width="{w}" height="{h}" fill="none" stroke="{INK}" stroke-width="2"/>')
    return w


def ex_marcs(o, x, y, est, h=20, canvis=(), w=96):
    """La memòria física d'un estat: quatre marcs amb la pàgina que contenen i si és modificada."""
    o.append(t(x + w / 2, y - 8, 'Memòria física', 11, INK, bold=True))
    for ppn in range(4):
        vpn = est['marcs'][ppn]
        yy = y + ppn * h
        if vpn is None:
            o.append(cel(x, yy, w, h, NEUTRE, TRAC))
            o.append(t(x + w / 2, yy + h / 2 + 4, 'lliure', 10, GRIS, italic=True))
        else:
            d = est['tp'][vpn]['d']
            o.append(cel(x, yy, w, h, P1_F, P1_S, f'VPN {vpn}' + (' · D = 1' if d else ''), P1_S, 10, mono=False))
        o.append(t(x - 6, yy + h / 2 + 4, f'0x{ppn:02X}', 10, GRIS, 'end', mono=True))
        if ppn in canvis:
            o.append(f'<rect x="{x}" y="{yy}" width="{w}" height="{h}" fill="none" stroke="{INK}" stroke-width="2"/>')
    o.append(t(x - 6, y - 8, 'PPN', 10, GRIS, 'end', bold=True))


def ex_lru(est):
    return 'Ordre LRU (de més antic a més recent): ' + ', '.join(f'VPN {v}' for v in est['lru'])


def exemple_tlb_pas(k):
    """Fotograma k de la figura dinàmica: l'estat després de l'accés k (0 = estat inicial)."""
    estats = simula_exemple()
    est = estats[k]
    o = []
    H = 22
    if k == 0:
        o.append(t(20, 24, 'Estat inicial', 14, INK, 'start', bold=True))
        o.append(t(20, 44, 'Tres pàgines residents, un marc lliure i una entrada del TLB lliure.', 11, GRIS, 'start'))
        canvis_tlb, canvis_tp, canvis_marcs = (), (), ()
    else:
        ev = est['ev']
        l1, l2, l3 = ex_text(ev)
        o.append(t(20, 24, f'Accés {k}: {l1}', 14, INK, 'start', bold=True))
        o.append(t(20, 44, l2, 11, INK, 'start'))
        o.append(t(20, 60, l3, 11, INK, 'start'))
        canvis_tlb, canvis_tp, canvis_marcs = ev['canvi_tlb'], ev['canvi_tp'], ev['canvi_marcs']
    Y = 112
    o.append(t(20 + 90, Y - 26, 'TLB', 11, INK, bold=True))
    ex_tlb(o, 20, Y, est, True, H, canvis_tlb)
    o.append(t(290 + 58, Y - 26, 'Taula de pàgines', 11, INK, bold=True))
    ex_tp(o, 290, Y, est, H, canvis_tp)
    ex_marcs(o, 500, Y, est, H, canvis_marcs, w=110)
    o.append(t(20, Y + 6 * H + 26, ex_lru(est), 11, GRIS, 'start', italic=True))
    desc = ('Estat inicial del TLB, la taula de pàgines i la memòria física de l’exemple de traducció amb TLB.'
            if k == 0 else f'Accés {k} de l’exemple: {l1}. {l2} {l3}.')
    return svg(680, Y + 6 * H + 40, f'Exemple de traducció amb TLB, pas {k}', desc, o)


def exemple_tlb():
    """Figura estàtica (PDF i sense JavaScript): l’estat inicial i la traça dels cinc accessos, amb l’estat del
    TLB i de la memòria física després de cadascun."""
    estats = simula_exemple()
    o = []
    H = 18
    y = 30
    o.append(t(20, y, 'Estat inicial', 13, INK, 'start', bold=True))
    o.append(t(20, y + 16, ex_lru(estats[0]), 10, GRIS, 'start', italic=True))
    o.append(t(360 + 90, y - 2, 'TLB', 10, INK, bold=True))
    ex_tlb(o, 360, y + 22, estats[0], True, H)
    ex_marcs(o, 590, y + 22, estats[0], H, w=80)
    y += 22 + 4 * H + 26
    for est in estats[1:]:
        ev = est['ev']
        l1, l2, l3 = ex_text(ev)
        o.append(f'<line x1="20" y1="{y - 14}" x2="660" y2="{y - 14}" stroke="{TRAC}" stroke-width="1"/>')
        o.append(t(20, y, f'Accés {ev["k"] if "k" in ev else est["k"]}: {l1}', 12, INK, 'start', bold=True))
        for n, lin in enumerate(parteix(l2, 62)):
            o.append(t(20, y + 16 + 13 * n, lin, 10, INK, 'start'))
        nl = len(parteix(l2, 62))
        o.append(t(20, y + 16 + 13 * nl, l3, 10, INK, 'start'))
        o.append(t(20, y + 30 + 13 * nl, ex_lru(est), 9, GRIS, 'start', italic=True))
        ex_tlb(o, 360, y + 4, est, True, H, ev['canvi_tlb'])
        ex_marcs(o, 590, y + 4, est, H, ev['canvi_marcs'], w=80)
        y += 4 + 4 * H + 30
    return svg(680, y, 'Exemple de traducció amb TLB: traça dels cinc accessos',
               "A dalt, l'estat inicial: el TLB, amb tres entrades vàlides (VPN 3, 0 i 2) i una de lliure, i la "
               "memòria física, amb VPN 3 (modificada) al marc 0x00, VPN 0 al 0x01, VPN 2 al 0x02 i el marc 0x03 "
               "lliure. A sota, una fila per accés, amb l'explicació a l'esquerra i, a la dreta, el TLB i la memòria "
               "física després de l'accés, amb les entrades i els marcs que han canviat amb vora gruixuda. "
               "Accés 1: escriptura a 0x00002A0B, encert de TLB, D = 1 a VPN 2, adreça física 0x2A0B. Accés 2: "
               "lectura a 0x00001F21, fallada de TLB i de pàgina, VPN 1 al marc lliure 0x03, adreça 0x3F21. Accés 3: "
               "lectura a 0x0000420C, fallada de TLB i de pàgina, víctima VPN 3, escrita al disc, VPN 4 al marc 0x00, "
               "adreça 0x020C. Accés 4: lectura a 0x00003001, víctima VPN 0 sense escriptura al disc, VPN 3 al marc "
               "0x01, adreça 0x1001. Accés 5: lectura a 0x00005120, víctima VPN 2, escrita al disc, VPN 5 al marc "
               "0x02, adreça 0x2120.", o)


def parteix(text, n):
    """Parteix un text en línies de com a màxim n caràcters, per espais."""
    linies, actual = [], ''
    for mot in text.split():
        if len(actual) + len(mot) + 1 > n and actual:
            linies.append(actual)
            actual = mot
        else:
            actual = f'{actual} {mot}'.strip()
    if actual:
        linies.append(actual)
    return linies


FIGURES = {
    'T8_mv_espais.svg': espais,
    'T8_mv_jerarquia.svg': jerarquia,
    'T8_mv_adreca_exemple.svg': adreca_exemple,
    'T8_mv_traduccio.svg': traduccio,
    'T8_mv_pagines_marcs.svg': pagines_marcs,
    'T8_mv_taula_pagines.svg': taula_pagines,
    'T8_mv_traduccio_exemple.svg': lambda: taula_pagines(exemple=True),
    'T8_mv_taula_multinivell.svg': taula_multinivell,
    'T8_mv_tlb_estructura.svg': tlb_estructura,
    'T8_mv_flux_traduccio.svg': flux,
    'T8_mv_comparticio.svg': comparticio,
    'T8_mv_pipt.svg': pipt,
    'T8_mv_vipt.svg': vipt,
    'T8_mv_exemple_tlb.svg': exemple_tlb,
}
# Fotogrames de la figura dinàmica de l'exemple (figures_dinamiques.html): <nom>_pas<k>.svg, k = 0 l'estat inicial.
for _k in range(len(EX_ACCESSOS) + 1):
    FIGURES[f'T8_mv_exemple_tlb_pas{_k}.svg'] = (lambda k: lambda: exemple_tlb_pas(k))(_k)


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
