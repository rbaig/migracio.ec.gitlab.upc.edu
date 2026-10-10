"""
figlib.py — Primitives compartides dels generadors de figures d'EC.

Portes lògiques i fils segons la convenció de `24_specs/svg.md §16` (forma
distintiva ANSI/IEEE 91, traç de 1,5 px, unions amb un punt ple i terminals
amb un cercle buit). Cada funció retorna el fragment SVG com a cadena: qui la
crida decideix on l'afegeix.

Al final hi ha el text, les caixes i les fletxes de les figures soltes, i les
vores compartides (`vores_compartides`, `24_specs/svg.md §7`). Qui la fa servir:
`git grep -n 'figlib' -- 25_scripts/` (no se'n porta la llista aquí, que es
quedaria enrere; D-104). Només fa servir la biblioteca estàndard.
"""
import math
import re

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"
INK = "#343a40"      # fils i portes
GRAY = "#6c757d"     # text secundari
W = 1.5              # gruix dels fils i de les portes


def line(pts, color=INK, w=W):
    d = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round"/>'


def dot(x, y, color=INK):
    return f'<circle cx="{x}" cy="{y}" r="2.5" fill="{color}"/>'


def term(x, y, color=INK):
    return f'<circle cx="{x}" cy="{y}" r="2.5" fill="#ffffff" stroke="{color}" stroke-width="{W}"/>'


def and_gate(x, cy, color=INK, fill="none"):
    """AND de 36 × 32 amb l'entrada a x i el centre a cy; la sortida és a x + 36."""
    return f'<path d="M{x},{cy-16} h20 a16,16 0 0 1 0,32 h-20 z" fill="{fill}" stroke="{color}" stroke-width="{W}" stroke-linejoin="round"/>'


def or_gate(x, cy, color=INK, fill="none"):
    """OR de 40 × 32; la sortida és a x + 40. Els fils d'entrada s'aturen a x + 3."""
    return f'<path d="M{x},{cy-16} Q{x+10},{cy} {x},{cy+16} Q{x+28},{cy+16} {x+40},{cy} Q{x+28},{cy-16} {x},{cy-16} z" fill="{fill}" stroke="{color}" stroke-width="{W}" stroke-linejoin="round"/>'


def xor_gate(x, cy, color=INK, fill="none"):
    """XOR: l'OR desplaçada 6 px, amb una segona corba al darrere; la sortida és a x + 46."""
    return (f'<path d="M{x},{cy-16} Q{x+10},{cy} {x},{cy+16}" fill="none" stroke="{color}" stroke-width="{W}"/>\n'
            + or_gate(x + 6, cy, color, fill))


# ── Text, caixes i fletxes (gen_T7.py, gen_T8.py) ──────────

def t(x, y, s, size=11, color=INK, anchor="middle", bold=False, italic=False, mono=False):
    a = f'font-family="{MONO if mono else SANS}" font-size="{size}" fill="{color}" text-anchor="{anchor}"'
    a += ' font-weight="bold"' if bold else ''
    a += ' font-style="italic"' if italic else ''
    return f'<text x="{x}" y="{y}" {a}>{s}</text>'


def var(nom, sub, sub2=None):
    """Variable en cursiva amb subíndex (i subsubíndex), amb <tspan dy> (svg.md §16)."""
    s = f'<tspan font-style="italic">{nom}</tspan><tspan dy="3" font-size="8" font-style="italic">{sub}</tspan>'
    if sub2:
        s += f'<tspan dy="2" font-size="7" font-style="italic">{sub2}</tspan><tspan dy="-5"> </tspan>'
    else:
        s += '<tspan dy="-3"> </tspan>'
    return s


def caixa(x, y, w, h, fill, stroke, etiqueta, size=12, bold=True, rx=4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
            + t(x + w / 2, y + h / 2 + size / 3, etiqueta, size, stroke, bold=bold))


def fletxa(x1, y1, x2, y2, color=INK, doble=True, w=1.2):
    """Fletxa (doble per defecte) amb puntes triangulars, sense marcadors (rsvg i el canvi de color al fosc)."""
    o = [f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>']
    ang = math.atan2(y2 - y1, x2 - x1)

    def punta(x, y, a):
        p1 = (x - 8 * math.cos(a - 0.4), y - 8 * math.sin(a - 0.4))
        p2 = (x - 8 * math.cos(a + 0.4), y - 8 * math.sin(a + 0.4))
        return f'<polygon points="{x},{y} {round(p1[0], 1)},{round(p1[1], 1)} {round(p2[0], 1)},{round(p2[1], 1)}" fill="{color}"/>'
    o.append(punta(x2, y2, ang))
    if doble:
        o.append(punta(x1, y1, ang + math.pi))
    return '\n'.join(o)


def svg(w, h, titol, desc, cos):
    return vores_compartides('\n'.join([f'<svg width="100%" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">',
                                        f'<title>{titol}</title>', f'<desc>{desc}</desc>', *cos, '</svg>']) + '\n')


# ── Vores compartides (svg.md §7; gen_regs.py, gen_MC.py, gen_T7.py, gen_T8.py) ──

_RECT = re.compile(r'<rect\b([^>]*?)\s*/>')
_ATTR = re.compile(r'([\w-]+)="([^"]*)"')


def _n(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def _zona(atr):
    """(x, y, w, h, traç) d'un <rect> ple, o None si no és una zona: sense farciment, girat o discontinu.
    El traç és (color, gruix), o None si no en té."""
    if 'transform' in atr or 'stroke-dasharray' in atr or atr.get('fill', '').lower() in ('', 'none', 'transparent'):
        return None
    try:
        x, y, w, h = (float(atr[k]) for k in ('x', 'y', 'width', 'height'))
    except (KeyError, ValueError):
        return None
    s = atr.get('stroke', 'none').lower()
    return x, y, w, h, (None if s == 'none' else (s, float(atr.get('stroke-width', '1'))))


def _costats(z):
    """Els quatre costats d'una zona: (orientació, coordenada, inici, final, sentit cap endins)."""
    x, y, w, h, _ = z
    return [('h', y, x, x + w, 1), ('h', y + h, x, x + w, -1), ('v', x, y, y + h, 1), ('v', x + w, y, y + h, -1)]


def _comparteixen(a, b, e=0.02):
    """Trams (orientació, coordenada, inici, final, sentit de a) de la vora que comparteixen a i b."""
    trams = []
    for oa, ca, ia, fa, sa in _costats(a):
        for ob, cb, ib, fb, sb in _costats(b):
            if oa == ob and sa == -sb and abs(ca - cb) < e and min(fa, fb) - max(ia, ib) > 0.5:
                trams.append((oa, ca, max(ia, ib), min(fa, fb), sa))
    return trams


def vores_compartides(text):
    """svg.md §7: les vores de les zones que es toquen, cadascuna per dins de la seva àrea.

    Una zona és un <rect> ple. Si dues zones comparteixen un tram de vora i no tenen el mateix
    traç (color i gruix), o només una en té, el que surt depèn de l'ordre de dibuix: la segona tapa
    la meitat del traç de la primera. Tot el grup de zones que es toquen es redibuixa, llavors:
    cada zona, el farciment sense traç i les vores per dins, desplaçades mig gruix; entre dues zones
    del mateix traç, una sola línia, centrada a la frontera, que dibuixa la segona. Una zona amb les
    cantonades arrodonides (rx) dibuixa sempre totes les vores per dins. Els grups sense cap
    conflicte, i les zones soltes, no es toquen."""
    elems = [(m, dict(_ATTR.findall(m.group(1)))) for m in _RECT.finditer(text)]
    zs = [(i, z) for i, z in ((i, _zona(a)) for i, (m, a) in enumerate(elems)) if z]
    zona = dict(zs)
    pare = {i: i for i, _ in zs}

    def arrel(i):
        while pare[i] != i:
            pare[i] = pare[pare[i]]
            i = pare[i]
        return i

    trams = {i: [] for i, _ in zs}               # i → [(j, tram)], un per tram compartit amb j
    conflicte = set()
    for k, (i, a) in enumerate(zs):
        for j, b in zs[k + 1:]:
            ts = _comparteixen(a, b)
            if not ts:
                continue
            pare[arrel(i)] = arrel(j)
            trams[i] += [(j, t) for t in ts]
            trams[j] += [(i, (o, c, p, q, -s)) for o, c, p, q, s in ts]
            if a[4] != b[4]:
                conflicte.add(i)
    grups = {arrel(i) for i in conflicte}
    nous = {}
    for i, z in zs:
        if arrel(i) not in grups or z[4] is None:
            continue
        m, atr = elems[i]
        x, y, w, h, (color, sw) = z
        rx = atr.get('rx')
        ple = {k: v for k, v in atr.items() if not k.startswith('stroke')}
        sortida = ['<rect ' + ' '.join(f'{k}="{v}"' for k, v in ple.items()) + '/>']
        iguals = [] if rx else [(j, t) for j, t in trams[i] if zona[j][4] == z[4]]
        if not iguals:
            r = f' rx="{_n(max(float(rx) - sw / 2, 0))}"' if rx else ''
            sortida.append(f'<rect x="{_n(x + sw / 2)}" y="{_n(y + sw / 2)}" width="{_n(w - sw)}" height="{_n(h - sw)}"{r} '
                           f'fill="none" stroke="{atr["stroke"]}" stroke-width="{atr.get("stroke-width", "1")}"/>')
        else:
            d = []
            for o, c, p, q, s in _costats(z):
                comuns = sorted((t[2], t[3], j) for j, t in iguals if t[0] == o and abs(t[1] - c) < 0.02 and t[4] == s)
                pos = p
                for a_, b_, j in comuns:
                    if a_ > pos:
                        d.append((o, c + s * sw / 2, pos, a_))
                    if j < i:                    # la dibuixa la segona zona, la que ja té l'altra a sota
                        d.append((o, c, a_, b_))
                    pos = max(pos, b_)
                if pos < q:
                    d.append((o, c + s * sw / 2, pos, q))
            cami = ' '.join(f'M{_n(p)},{_n(c)}H{_n(q)}' if o == 'h' else f'M{_n(c)},{_n(p)}V{_n(q)}' for o, c, p, q in d)
            sortida.append(f'<path d="{cami}" fill="none" stroke="{atr["stroke"]}" stroke-width="{atr.get("stroke-width", "1")}"/>')
        nous[i] = '\n'.join(sortida)
    if not nous:
        return text
    out, pos = [], 0
    for i, (m, _) in enumerate(elems):
        if i in nous:
            out += [text[pos:m.start()], nous[i]]
            pos = m.end()
    return ''.join(out + [text[pos:]])
