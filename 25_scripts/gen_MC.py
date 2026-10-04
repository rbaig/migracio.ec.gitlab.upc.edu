#!/usr/bin/env python3
"""
gen_MC.py — Genera les figures de memòria cau (T7) a partir de `24_specs/mc.toml`, simulant la MC.

Ús, com a pas del pre-render de Quarto (`_quarto.yml`):

    25_scripts/gen_MC.py 24_specs/mc.toml "__MC_light" --output-dir="auto_figs/"

Per a cada `[mc.<nom>]` del TOML, el generador **simula** la memòria cau sobre la
seqüència d'accessos (emplaçament, reemplaçament LRU, escriptura immediata o
retardada, amb assignació o sense) i en dibuixa el resultat. Els encerts, les
fallades, el tipus de fallada (obligatòria, de capacitat o de conflicte), el
bloc expulsat i el bit D no els escriu ningú a mà: surten de la simulació. Les
fallades es classifiquen amb el mètode de les tres C: obligatòria si el bloc no
s'havia accedit mai; de capacitat si també fallaria en una MC completament
associativa LRU de les mateixes línies; i de conflicte, si no.

Estils (`estil`):

- `"sequencia"`: la MP, la seqüència d'accessos i l'estat de la MC després de
  cada accés. Escriu `<nom>__MC_light.svg`.
- `"traca"`: una taula amb una fila per accés (accés, bloc, línia o conjunt,
  resultat i el bloc que conté cada línia després de l'accés). És la forma
  compacta, pensada per al PDF.

Amb `fotogrames = true`, escriu a més un fotograma per pas,
`<nom>_pas<k>__MC_light.svg` (k = 0 és l'estat inicial), per a la figura
dinàmica de l'HTML; la seqüència estàtica equivalent és la mateixa figura en
estil `sequencia` o `traca` (decisió de l'usuari 4 de la fase 7c).

La terminologia és la de `13_contrib.qmd` (decisió de l'usuari 11 de la fase
7c): «Lectura», «Escriptura», «Encert», «Fallada» i fallades «obligatòria», «de
capacitat» i «de conflicte». Model (b) de la fase 7c (`24_specs/svg.md §17`):
la definició és el font i l'SVG no es versiona. Només fa servir la biblioteca
estàndard.
"""
import argparse
import sys
import tomllib
from pathlib import Path

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"
INK, GRIS, TRAC, NEUTRE, BLANC = "#343a40", "#6c757d", "#adb5bd", "#f8f9fa", "#ffffff"
ENCERT, FALLADA = "#198754", "#dc3545"
COLORS = [("#cfe2ff", "#084298"), ("#d1e7dd", "#0a3622"), ("#fff3cd", "#664d03"), ("#f8d7da", "#842029")]
FS = 11          # mida de lletra base
H = 22           # alçada d'una fila de la MC


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def text(x, y, t, size=FS, color=INK, anchor='middle', mono=False, bold=False, italic=False):
    attrs = f'font-family="{MONO if mono else SANS}" font-size="{size}" fill="{color}" text-anchor="{anchor}"'
    if bold:
        attrs += ' font-weight="bold"'
    if italic:
        attrs += ' font-style="italic"'
    return f'<text x="{round(x, 1)}" y="{round(y, 1)}" {attrs}>{t}</text>'


def rect(x, y, w, h, fill, stroke, sw=1):
    return f'<rect x="{round(x, 1)}" y="{round(y, 1)}" width="{round(w, 1)}" height="{round(h, 1)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


# ═══════════════════════════════════════════════════════════
# Simulació
# ═══════════════════════════════════════════════════════════

class MC:
    def __init__(self, spec):
        self.B = spec['bloc']
        self.NL = spec['linies']
        self.N = spec.get('vies', 1)
        self.NC = self.NL // self.N
        self.retardada = spec.get('escriptura', 'immediata') == 'retardada'
        self.assignacio = spec.get('assignacio', True)
        self.sets = [[None] * self.N for _ in range(self.NC)]   # via → {'bloc', 'D'}
        self.lru = [list(range(self.N)) for _ in range(self.NC)]  # de menys a més recent
        self.vistos = set()
        self.ombra = []                                          # MC completament associativa LRU

    def ocupacio(self):
        return [[dict(v) if v else None for v in s] for s in self.sets]

    def acces(self, op, adr):
        bloc = adr // self.B
        c = bloc % self.NC
        etiq = bloc // self.NC
        res = {'op': op, 'adr': adr, 'bloc': bloc, 'conj': c, 'etiq': etiq}
        # MC de referència per classificar les fallades
        encert_ombra = bloc in self.ombra
        if encert_ombra:
            self.ombra.remove(bloc)
        self.ombra.append(bloc)
        if len(self.ombra) > self.NL:
            self.ombra.pop(0)
        via = next((v for v, l in enumerate(self.sets[c]) if l and l['bloc'] == bloc), None)
        if via is not None:
            res.update(encert=True, via=via)
            if op == 'E' and self.retardada:
                self.sets[c][via]['D'] = 1
            self.toca(c, via)
        else:
            res['encert'] = False
            res['tipus'] = ('obligatoria' if bloc not in self.vistos else
                            'capacitat' if not encert_ombra else 'conflicte')
            if op == 'L' or self.assignacio:
                lliure = next((v for v, l in enumerate(self.sets[c]) if l is None), None)
                via = lliure if lliure is not None else self.lru[c][0]
                vell = self.sets[c][via]
                res.update(via=via, lliure=lliure is not None,
                           expulsat=vell['bloc'] if vell else None,
                           expulsat_D=bool(vell and vell['D']))
                self.sets[c][via] = {'bloc': bloc, 'D': 1 if (op == 'E' and self.retardada) else 0}
                self.toca(c, via)
            else:
                res['via'] = None
        self.vistos.add(bloc)
        res['lru'] = self.lru_visible()
        return res

    def lru_visible(self):
        """Via LRU de cada conjunt ple; «—» si el conjunt té alguna via lliure (no n'hi ha cap a triar)."""
        if self.N == 1:
            return None
        return [str(self.lru[c][0]) if all(self.sets[c]) else '—' for c in range(self.NC)]

    def toca(self, c, via):
        self.lru[c].remove(via)
        self.lru[c].append(via)


def nom_tipus(t):
    return {'obligatoria': 'Fallada obligatòria', 'capacitat': 'Fallada de capacitat',
            'conflicte': 'Fallada de conflicte'}[t]


def explicacio(r, mc, spec, desti):
    """Text automàtic de què passa en un accés (es pot substituir amb `nota`)."""
    linia = desti(r['conj'], r.get('via'))
    if r['encert']:
        if r['op'] == 'L':
            return 'Llegeix de la MC'
        return 'Escriu només a la MC (D ← 1)' if mc.retardada else 'Escriu a la MC i a la MP'
    if r.get('via') is None:
        return 'Escriu només a la MP; la MC no canvia'
    parts = []
    if r.get('expulsat') is not None and r['expulsat_D']:
        parts.append(f"Escriu el bloc {r['expulsat']} (modificat) a la MP")
    accio = f"copia el bloc {r['bloc']} a {linia}"
    if r.get('expulsat') is not None:
        accio += f" (expulsa el bloc {r['expulsat']})"
    elif mc.N > 1:
        accio += ', lliure'
    parts.append(accio[0].upper() + accio[1:] if not parts else accio)
    if r['op'] == 'E':
        parts.append('hi escriu (D ← 1)' if mc.retardada else 'escriu a la MC i a la MP')
    return '; '.join(parts)


def etiqueta_cel(adr, spec):
    """Rètol d'una cel·la de dades: element d'un vector, si n'hi ha, o «byte k»."""
    for v in spec.get('vectors', []):
        if v['base'] <= adr < v['base'] + v['n'] * v['mida']:
            return f"{v['nom']}[{(adr - v['base']) // v['mida']}]"
    return f'byte {adr}'


def bits(v, n):
    return format(v, f'0{n}b') if n > 0 else ''


# ═══════════════════════════════════════════════════════════
# Estil «sequencia»: MP, accessos i estat de la MC a cada pas
# ═══════════════════════════════════════════════════════════

class Geometria:
    def __init__(self, spec):
        self.spec = spec
        self.B = spec['bloc']
        self.u = spec.get('unitat', 1)                 # bytes per cel·la de dades
        self.ncel = self.B // self.u
        self.N = spec.get('vies', 1)
        self.NL = spec['linies']
        self.NC = self.NL // self.N
        self.w_adr = spec.get('adreca_bits', 0)
        self.b = (self.B - 1).bit_length()
        self.c = (self.NC - 1).bit_length()
        self.t = self.w_adr - self.b - self.c if self.w_adr else 0
        self.D = spec.get('escriptura', 'immediata') == 'retardada'
        self.w_dada = 56 if self.u == 1 else 54
        self.col_via = 26 + (26 if self.D else 0) + 54 + self.ncel * self.w_dada  # V, D, etiq, dades

    def color_bloc(self, bloc):
        """Un color per vector (`color = "vector"`) o per bloc, en l'ordre en què surten a la MP: així
        dos blocs que es veuen alhora no comparteixen color (el mòdul 4 donava el mateix a 1, 9 i 13)."""
        if self.spec.get('color') == 'vector':
            adr = bloc * self.B
            for k, v in enumerate(self.spec.get('vectors', [])):
                if v['base'] <= adr < v['base'] + v['n'] * v['mida']:
                    return COLORS[k % len(COLORS)]
        ordre = [b for a, z in self.spec.get('mp', []) for b in range(a, z + 1)]
        return COLORS[(ordre.index(bloc) if bloc in ordre else bloc) % len(COLORS)]

    def etiq_text(self, bloc):
        e = bloc // self.NC
        return bits(e, self.t) if self.spec.get('format_etiqueta', 'binari') == 'binari' and self.t else str(e)


def dibuixa_mc(o, g, x0, y0, estat, ressalt=None, lru=None, mostra_cap=True):
    """Taula de la MC: una fila per conjunt (línia), i les vies una al costat de l'altra."""
    y = y0
    if mostra_cap:
        for v in range(g.N):
            xv = x0 + 24 + v * (g.col_via + 12)
            if g.N > 1:
                o.append(text(xv + g.col_via / 2, y - 22, f'Via {v}', 12, INK, bold=True))
            cx = xv
            for nom, w in [('V', 26)] + ([('D', 26)] if g.D else []) + [('Etiq', 54)]:
                o.append(text(cx + w / 2, y - 6, nom, 10, INK, bold=True))
                cx += w
            o.append(text(cx + g.ncel * g.w_dada / 2, y - 6, f'Dades ({g.B} bytes)', 10, INK, bold=True))
        o.append(text(x0 + 10, y - 6, '#' if g.N == 1 else 'Conj', 10, INK, bold=True))
        if lru is not None:
            o.append(text(x0 + 24 + g.N * (g.col_via + 12) + 14, y - 6, 'LRU', 10, INK, bold=True))
    for c in range(g.NC):
        yy = y + c * H
        o.append(text(x0 + 10, yy + 15, c, FS, GRIS, bold=True))
        for v in range(g.N):
            l = estat[c][v]
            xv = x0 + 24 + v * (g.col_via + 12)
            fill, stroke = g.color_bloc(l['bloc']) if l else (NEUTRE, TRAC)
            tc = stroke if l else GRIS
            cx = xv
            cells = [('1' if l else '0', 26)] + ([(str(l['D']) if l else '0', 26)] if g.D else []) + \
                    [(g.etiq_text(l['bloc']) if l else '—', 54)]
            for t, w in cells:
                o.append(rect(cx, yy, w, H, fill, stroke if l else TRAC, 0.75))
                o.append(text(cx + w / 2, yy + 15, esc(t), FS, tc, mono=True))
                cx += w
            for k in range(g.ncel):
                o.append(rect(cx, yy, g.w_dada, H, fill, stroke if l else TRAC, 0.75))
                if l:
                    adr = l['bloc'] * g.B + k * g.u
                    o.append(text(cx + g.w_dada / 2, yy + 15, esc(etiqueta_cel(adr, g.spec)), 10, tc, mono=True))
                    if ressalt == (c, v, k):
                        o.append(rect(cx + 2, yy + 2, g.w_dada - 4, H - 4, 'none', stroke, 2))
                cx += g.w_dada
        if lru is not None:
            o.append(text(x0 + 24 + g.N * (g.col_via + 12) + 14, yy + 15, lru[c], FS, GRIS, mono=True))
    return y + g.NC * H


def dibuixa_mp(o, g, x0, y0):
    """Columna de la MP: adreça en binari (o element), contingut i número de bloc."""
    spec = g.spec
    y = y0
    files = []
    blocs = []
    for a, b in spec['mp']:
        if blocs and a != blocs[-1] + 1:
            blocs.append(None)
        blocs.extend(range(a, b + 1))
    xa, xc, xb = x0, x0 + (96 if g.w_adr else 40), x0 + (96 if g.w_adr else 40) + 80
    o.append(text((x0 + xb + 20) / 2, y0 - 34, 'MP', 14, INK, bold=True))
    if g.w_adr:
        o.append(text(xa + 44, y0 - 18, 'Adreça (bin)', 10, INK, bold=True))
        o.append(text(xa + 44, y0 - 6, 'etiq idx off' if g.c else 'etiq off', 9, GRIS, mono=True))
    o.append(text(xc + 38, y0 - 6, 'Contingut', 10, INK, bold=True))
    o.append(text(xb + 16, y0 - 6, 'bloc', 9, GRIS))
    for bloc in blocs:
        if bloc is None:
            o.append(text(xc + 38, y + 12, '· · ·', 12, GRIS))
            y += 18
            continue
        fill, stroke = g.color_bloc(bloc)
        for k in range(g.ncel):
            adr = bloc * g.B + k * g.u
            if g.w_adr:
                e, ix, off = adr >> (g.b + g.c), (adr >> g.b) & ((1 << g.c) - 1), adr & ((1 << g.b) - 1)
                t = f'{bits(e, g.t)} {bits(ix, g.c)} {bits(off, g.b)}'.replace('  ', ' ')
                o.append(text(xa + 44, y + 14, t, 10, stroke, mono=True))
            else:
                for v in spec.get('vectors', []):
                    if adr == v['base']:
                        o.append(text(xc - 6, y + 14, f"{v['nom']}:", 11, INK, anchor='end', bold=True))
            o.append(rect(xc, y, 76, 20, fill, stroke, 0.75))
            o.append(text(xc + 38, y + 14, esc(etiqueta_cel(adr, spec)), 10, stroke, mono=True))
            if k == 0:
                o.append(text(xb + 16, y + 14, bloc, 10, stroke, mono=True))
            y += 20
    return y


def ordinal(n):
    return {1: '1r', 2: '2n', 3: '3r', 4: '4t'}.get(n, f'{n}è')


def sequencia(spec, pas=None):
    """Estil «sequencia». Amb `pas` = k, només el pas k (fotograma de la figura dinàmica)."""
    g = Geometria(spec)
    mc = MC(spec)
    for a in spec.get('inicial', []):
        mc.acces(a['op'], a['adr'])
    passos = [('inicial', None, mc.ocupacio(), {'lru': mc.lru_visible()}, None)]
    for k, a in enumerate(spec['accessos'], 1):
        r = mc.acces(a['op'], a['adr'])
        ressalt = (r['conj'], r['via'], (a['adr'] % g.B) // g.u) if r.get('via') is not None else None
        passos.append((k, a, mc.ocupacio(), r, ressalt))
    desti = (lambda c, v: f'la línia {c}') if g.N == 1 else (lambda c, v: f'la via {v} del conjunt {c}')
    if g.N == g.NL:
        desti = lambda c, v: f'la línia {v}'
    x_mp = 10
    x_seq = 10 + (96 if g.w_adr else 40) + 80 + 50 if spec.get('mostra_mp', True) else 10
    w_seq = spec.get('amplada_seq', 250)
    x_mc = x_seq + w_seq
    w = x_mc + 24 + g.N * (g.col_via + 12) + (30 if g.N > 1 else 0) + 6
    y0 = 70 if g.N > 1 else 56
    sel = passos if pas is None else [passos[pas]]

    def notes(k, a, r):
        return [] if k == 'inicial' else parteix(a.get('nota') or explicacio(r, mc, spec, desti), 40)

    def alcada(k, a, r):
        text_h = 20 if k == 'inicial' else 46 + 13 * len(notes(k, a, r))
        return max(g.NC * H, text_h) + 26
    h_total = y0 + sum(alcada(k, a, r) for k, a, _, r, _ in sel) + 10
    o = []
    y_mp_fi = dibuixa_mp(o, g, x_mp, y0) if spec.get('mostra_mp', True) else 0
    o.append(text(x_seq + w_seq / 2, y0 - 34 - (14 if g.N > 1 else 0), "Seqüència d'accessos", 14, INK, bold=True))
    o.append(text(x_mc + (w - x_mc) / 2, y0 - 34 - (14 if g.N > 1 else 0), 'MC', 14, INK, bold=True))
    y = y0
    for i, (k, a, estat, r, ressalt) in enumerate(sel):
        if i > 0:
            o.append(f'<line x1="{x_seq}" y1="{y - 10}" x2="{w - 6}" y2="{y - 10}" stroke="{TRAC}" stroke-width="1"/>')
        dibuixa_mc(o, g, x_mc, y, estat, ressalt, r['lru'], mostra_cap=(i == 0))
        ty = y + 14
        if k == 'inicial':
            o.append(text(x_seq, ty + 4, 'Estat inicial', 12, INK, anchor='start', bold=True))
            if spec.get('nota_inicial'):
                o.append(text(x_seq, ty + 20, esc(spec['nota_inicial']), 10, GRIS, anchor='start', italic=True))
        else:
            fill, stroke = g.color_bloc(r['bloc'])
            grup = a.get('grup')
            cap = grup if grup else f'{ordinal(k)} accés'
            o.append(text(x_seq, ty, esc(cap), 11, INK, anchor='start', bold=True))
            nom_op = 'Lectura' if a['op'] == 'L' else 'Escriptura'
            if g.w_adr and not spec.get('vectors'):
                e, ix, off = a['adr'] >> (g.b + g.c), (a['adr'] >> g.b) & ((1 << g.c) - 1), a['adr'] & ((1 << g.b) - 1)
                adr_bin = f'{bits(e, g.t)} <tspan font-weight="bold">{bits(ix, g.c)}</tspan> {bits(off, g.b)}' if g.c else \
                          f'{bits(e, g.t)} {bits(off, g.b)}'
                o.append(text(x_seq, ty + 16, f'{nom_op} @{a["adr"]}', 11, INK, anchor='start'))
                o.append(f'<text x="{x_seq + 100}" y="{ty + 16}" font-family="{MONO}" font-size="11" fill="{stroke}">{adr_bin}</text>')
                o.append(text(x_seq, ty + 31, f"bloc {r['bloc']}, {'conjunt' if g.N > 1 else 'línia'} {r['conj']}" if g.N < g.NL
                              else f"bloc {r['bloc']}", 10, GRIS, anchor='start'))
            else:
                o.append(text(x_seq, ty + 16, f'{nom_op} {esc(etiqueta_cel(a["adr"], spec))}', 11, stroke, anchor='start', mono=True))
                o.append(text(x_seq, ty + 31, f"bloc {r['bloc']}" + (f", línia {r['conj']}" if g.N == 1 else
                              (f", conjunt {r['conj']}" if g.N < g.NL else '')), 10, GRIS, anchor='start'))
            res = 'Encert' if r['encert'] else (nom_tipus(r['tipus']) if spec.get('classifica') else 'Fallada')
            o.append(text(x_mc - 10, ty + 1, res + ' →', 11, ENCERT if r['encert'] else FALLADA, anchor='end', bold=True))
            for j, tros in enumerate(notes(k, a, r)):
                o.append(text(x_seq, ty + 46 + j * 13, esc(tros), 10, GRIS, anchor='start', italic=True))
        y += alcada(k, a, r)
    h_total = max(h_total, y_mp_fi + 10, y + 4)
    return w, h_total, o


def parteix(t, n):
    paraules, linies, cur = t.split(), [], ''
    for p in paraules:
        if cur and len(cur) + 1 + len(p) > n:
            linies.append(cur)
            cur = p
        else:
            cur = f'{cur} {p}'.strip()
    if cur:
        linies.append(cur)
    return linies


# ═══════════════════════════════════════════════════════════
# Estil «traca»: una fila per accés
# ═══════════════════════════════════════════════════════════

def traca(spec):
    g = Geometria(spec)
    mc = MC(spec)
    for a in spec.get('inicial', []):
        mc.acces(a['op'], a['adr'])
    inicial = mc.ocupacio() if (spec.get('inicial') or spec.get('fila_inicial')) else None
    files = []
    for a in spec['accessos']:
        r = mc.acces(a['op'], a['adr'])
        files.append((a, r, mc.ocupacio()))
    cols_mc = [(c, v) for c in range(g.NC) for v in range(g.N)]
    fa = g.NC == 1 and g.N > 1                         # completament associativa: les vies són les línies
    nom_cols = [f'{c}' if g.N == 1 else (f'{v}' if fa else f'{c}·{v}') for c, v in cols_mc]
    w_acc = spec.get('amplada_acces', 130)
    w_res = 160 if spec.get('classifica') else 70
    cols = [('Accés', w_acc), ('Bloc', 44), ('Línia' if (g.N == 1 or fa) else 'Conj', 44), ('Resultat', w_res)]
    w_mcc = 46 if not g.D else 54
    x = 10
    titol_mc = 'MC: bloc de cada línia' if (g.N == 1 or fa) else 'MC: bloc de cada conjunt·via'
    if g.D:
        titol_mc += ' (* = D)'
    w = x + sum(c[1] for c in cols) + 10 + max(len(cols_mc) * w_mcc, len(titol_mc) * 6.6) + 10
    o = []
    y0 = 44
    cx = x
    for nom, wc in cols:
        o.append(text(cx + wc / 2, y0 - 6, nom, 10, INK, bold=True))
        cx += wc
    x_mcc = cx + 10
    o.append(text(x_mcc + len(cols_mc) * w_mcc / 2, y0 - 22, titol_mc, 10, INK, bold=True))
    for j, n in enumerate(nom_cols):
        o.append(text(x_mcc + j * w_mcc + w_mcc / 2, y0 - 6, n, 10, GRIS, bold=True, mono=True))
    y = y0

    def cel_mc(xx, y, l, canvia, gruixut):
        if l:
            f_, s_ = g.color_bloc(l['bloc'])
            o.append(rect(xx + 2, y + 2, w_mcc - 4, H - 4, f_ if canvia else BLANC, s_, 1.5 if gruixut else 0.5))
            o.append(text(xx + w_mcc / 2, y + 15, f"{l['bloc']}{'*' if l['D'] else ''}", 10, s_, mono=True, bold=canvia))
        else:
            o.append(text(xx + w_mcc / 2, y + 15, '—', 10, TRAC))

    previ = inicial
    if inicial is not None:
        o.append(text(x + 6, y + 15, 'Estat inicial', 10, INK, anchor='start', bold=True))
        for j, (c, v) in enumerate(cols_mc):
            cel_mc(x_mcc + j * w_mcc, y, inicial[c][v], False, False)
        y += H
    for i, (a, r, estat) in enumerate(files):
        if a.get('grup'):
            o.append(f'<line x1="{x}" y1="{y}" x2="{w - 10}" y2="{y}" stroke="{TRAC}" stroke-width="1"/>')
            o.append(text(x + 6, y + 15, esc(a['grup']), 10, INK, anchor='start', bold=True))
            y += H
        if i % 2 == 0:
            o.append(rect(x, y, w - 20, H, NEUTRE, 'none', 0))
        fill, stroke = g.color_bloc(r['bloc'])
        cx = x
        acc = ('Lectura ' if a['op'] == 'L' else 'Escriptura ') + (etiqueta_cel(a['adr'], spec) if spec.get('vectors') else f"@{a['adr']}")
        res = 'Encert' if r['encert'] else (nom_tipus(r['tipus']) if spec.get('classifica') else 'Fallada')
        valors = [(acc, INK, False), (r['bloc'], stroke, True), (r['conj'] if not fa else r.get('via', '—'), INK, True),
                  (res, ENCERT if r['encert'] else FALLADA, False)]
        for (t, col, mono), (_, wc) in zip(valors, cols):
            o.append(text(cx + (6 if t is acc else wc / 2), y + 15, esc(t), 10, col, anchor='start' if t is acc else 'middle', mono=mono))
            cx += wc
        for j, (c, v) in enumerate(cols_mc):
            canvia = previ is None or previ[c][v] != estat[c][v]
            cel_mc(x_mcc + j * w_mcc, y, estat[c][v], canvia, r.get('via') == v and r['conj'] == c)
        previ = estat
        y += H
    return w, y + 10, o


def svg(spec, w, h, cos):
    return '\n'.join([f'<svg width="100%" viewBox="0 0 {round(w)} {round(h)}" xmlns="http://www.w3.org/2000/svg" role="img">',
                      f'<title>{esc(spec["title"])}</title>', f'<desc>{esc(spec["desc"])}</desc>', *cos, '</svg>']) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('specs', type=Path, help='24_specs/mc.toml')
    ap.add_argument('sufix', help='sufix del fitxer de sortida, p. ex. "__MC_light"')
    ap.add_argument('--output-dir', type=Path, default=Path('.'))
    args = ap.parse_args()
    dades = tomllib.loads(args.specs.read_text(encoding='utf-8')).get('mc', {})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    n = errors = 0
    for nom, spec in dades.items():
        try:
            estil = spec.get('estil', 'sequencia')
            w, h, cos = traca(spec) if estil == 'traca' else sequencia(spec)
            (args.output_dir / f'{nom}{args.sufix}.svg').write_text(svg(spec, w, h, cos), encoding='utf-8')
            n += 1
            if spec.get('fotogrames'):
                for k in range(len(spec['accessos']) + 1):
                    w, h, cos = sequencia(spec, pas=k)
                    (args.output_dir / f'{nom}_pas{k}{args.sufix}.svg').write_text(svg(spec, w, h, cos), encoding='utf-8')
                    n += 1
        except (KeyError, TypeError, ValueError, ZeroDivisionError) as e:
            print(f'[gen-MC] ERROR {nom}: {e!r}', file=sys.stderr)
            errors += 1
    print(f'[gen-MC] Resum: {n} generats, {errors} errors. Directori: {args.output_dir}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
