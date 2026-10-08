"""
columna_memoria.py — Primitives compartides de les figures de memòria (`24_specs/svg.md §2–§11`).

No és cap generador: en fan servir les peces `gen_BA.py` (blocs d'activació) i
`gen_mapa.py` (mapa de memòria i piles en fila), perquè les dues famílies
dibuixin les zones, les ratlles indicadores, les etiquetes de la columna
esquerra i les fletxes de creixement de la mateixa manera.

Geometria de la columna (classe `estreta`, svg.md §2 i §5): columna d'etiquetes
de 76 px, rectangles a x = 86 i de 244 px d'amplada, i marges de 10 px; W = 340.
"""

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"
INK, GRIS, TRAC, NEUTRE = "#343a40", "#6c757d", "#adb5bd", "#f8f9fa"

ROLS = {                                   # svg.md §10: (fill, stroke i text)
    'local':     ("#cfe2ff", "#084298"),   # variables locals (BA)
    'segur':     ("#d1e7dd", "#0a3622"),   # registres segurs desats (BA)
    'ra':        ("#fff3cd", "#664d03"),   # ra desat (BA)
    'reservada': (NEUTRE, TRAC),           # zona reservada (el text, en GRIS)
    'lliure':    (NEUTRE, TRAC),           # espai lliure (el text, en GRIS)
    'text':      ("#f8d7da", "#842029"),   # .text
    'data':      ("#cfe2ff", "#084298"),   # .data
    'heap':      ("#d1e7dd", "#0a3622"),   # heap
    'pila':      ("#fff3cd", "#664d03"),   # pila
    'ocupada':   (TRAC, GRIS),             # pila ocupada abans de la crida (piles en fila)
}

CLASSES = {'estreta': 340, 'estandard': 680, 'ampla': 960}   # svg.md §2
M_SUP = M_INF = 10
X_ETIQ = 74                                # svg.md §9: etiquetes de la columna esquerra (text-anchor end)
X_RECT, W_RECT = 86, 244                   # svg.md §5


def color_text(rol):
    """Color del text d'una zona: el del traç, tret de les neutres, que van en gris de text."""
    return GRIS if rol in ('reservada', 'lliure', 'ocupada') else ROLS[rol][1]


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def mono(t, negreta=False):
    pes = ' font-weight="bold"' if negreta else ''
    return f'<tspan font-family="{MONO}"{pes}>{esc(t)}</tspan>'


def marcat(t):
    """Text amb `codi` (monoespaiat) i *cursiva*, en <tspan>; la resta, escapat."""
    out, i = [], 0
    while i < len(t):
        c = t[i]
        if c in '`*':
            j = t.index(c, i + 1)
            dins = esc(t[i + 1:j])
            out.append(f'<tspan font-family="{MONO}">{dins}</tspan>' if c == '`'
                       else f'<tspan font-style="italic">{dins}</tspan>')
            i = j + 1
        else:
            j = min([k for k in (t.find('`', i), t.find('*', i)) if k >= 0] or [len(t)])
            out.append(esc(t[i:j]))
            i = j
    return ''.join(out)


def text(o, x, y, contingut, mida=11, color=INK, anchor='middle', negreta=False, cursiva=False, familia=SANS):
    a = f'font-family="{familia}" font-size="{mida}" fill="{color}" text-anchor="{anchor}"'
    a += ' font-weight="bold"' if negreta else ''
    a += ' font-style="italic"' if cursiva else ''
    o.append(f'<text x="{x}" y="{y}" {a}>{contingut}</text>')


def ticks(o, y, h, curtes, color, x=X_RECT, w=W_RECT):
    """Ratlles indicadores de svg.md §6, als dos costats d'un rectangle sòlid."""
    xe, xd = x + 1, x + w - 1
    for frac in (0.25, 0.5, 0.75):
        lon = 6 if (curtes or frac != 0.5) else 12
        yy = y + h * frac
        o.append(f'<line x1="{xe}" y1="{yy}" x2="{xe + lon}" y2="{yy}" stroke="{color}" stroke-width="1"/>')
        o.append(f'<line x1="{xd}" y1="{yy}" x2="{xd - lon}" y2="{yy}" stroke="{color}" stroke-width="1"/>')


def hline(o, y, color, gruix, x=X_RECT, w=W_RECT):
    o.append(f'<line x1="{x}" y1="{y}" x2="{x + w}" y2="{y}" stroke="{color}" stroke-width="{gruix}"/>')


def vlines(o, y1, y2, color, discontinua=False, x=X_RECT, w=W_RECT):
    estil = ' stroke-dasharray="4,3"' if discontinua else ''
    for xx in (x, x + w):
        o.append(f'<line x1="{xx}" y1="{y1}" x2="{xx}" y2="{y2}" stroke="{color}" stroke-width="1"{estil}/>')


def vlines_elidides(o, y1, y2, color, byte, x=X_RECT, w=W_RECT):
    """svg.md §4: vores verticals d'un tram elidit (el mig d'un vector o d'una zona genèrica).

    Contínues durant un byte a cada extrem i discontínues entre mig, perquè es vegi que el tram
    continua sense tall el que té a sobre i a sota; si fa menys de 3 bytes, contínues."""
    if y2 - y1 < 3 * byte:
        vlines(o, y1, y2, color, x=x, w=w)
        return
    vlines(o, y1, y1 + byte, color, x=x, w=w)
    vlines(o, y1 + byte, y2 - byte, color, discontinua=True, x=x, w=w)
    vlines(o, y2 - byte, y2, color, x=x, w=w)


def vores(o, fronteres, colors, x=X_RECT, w=W_RECT):
    """svg.md §7: les vores horitzontals de les zones, cadascuna per dins de la seva àrea.

    `fronteres` són les y de les n + 1 vores, i `colors`, el traç de cada una de les n zones, o
    None si no en té (alineació, espai lliure). Entre dues zones de color diferent, dues línies
    d'1 px, una de cada color; entre dues del mateix color, una de sola, compartida; i al costat
    d'una zona sense traç, la de l'altra, sencera. El resultat no depèn de l'ordre de dibuix."""
    for k, y in enumerate(fronteres):
        a = colors[k - 1] if k > 0 else None
        b = colors[k] if k < len(colors) else None
        if a and a == b:
            hline(o, y, a, 1, x, w)
            continue
        if a:
            hline(o, y - 0.5, a, 1, x, w)
        if b:
            hline(o, y + 0.5, b, 1, x, w)


def rect(o, y, h, fill, stroke=None, x=X_RECT, w=W_RECT):
    traç = f'stroke="{stroke}" stroke-width="1"' if stroke else 'stroke="none"'
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {traç}/>')


def text_zona(o, cy, linies, color, x=X_RECT, w=W_RECT):
    """svg.md §8: línies centrades verticalment, a 16 px d'interlineat.

    Cada línia és (contingut ja marcat, mida, negreta)."""
    n = len(linies)
    for i, (contingut, mida, negreta) in enumerate(linies):
        y = round(cy - (n - 1) * 16 / 2 + i * 16 + mida / 3, 1)
        text(o, x + w / 2, y, contingut, mida, color, negreta=negreta)


def linies_lliures(llista):
    """Text lliure d'una zona (svg.md §8): la primera línia, títol en negreta a 12 px; la resta, a 11 px."""
    return [(marcat(t), 12 if i == 0 else 11, i == 0) for i, t in enumerate(llista)]


def separadors(o, ys):
    """svg.md §7: una línia grisa fina a cada frontera, només a la columna d'etiquetes."""
    for y in ys:
        o.append(f'<line x1="{X_ETIQ + 2}" y1="{y}" x2="{X_RECT}" y2="{y}" stroke="{TRAC}" stroke-width="0.5"/>')


def etiqueta(o, y, contingut, color, mida=11, negreta=False, familia=MONO):
    """svg.md §9: etiqueta de la columna esquerra, centrada sobre la frontera y."""
    text(o, X_ETIQ, y + 3, contingut, mida, color, 'end', negreta, familia=familia)


def adreces_extrems(o, h):
    """svg.md §9: «adr. baixes» a dalt i «adr. altes» a baix."""
    text(o, X_ETIQ, M_SUP + 3, 'adr. baixes', 10, GRIS, 'end')
    text(o, X_ETIQ, h - M_INF + 3, 'adr. altes', 10, GRIS, 'end')


def fletxa(o, x, y1, y2, color, rotul='creix', costat=1):
    """svg.md §11: fletxa de creixement vertical de y1 a y2, amb el rètol girat al costat.

    El rètol va centrat a la meitat de la fletxa i desplaçat 6 px cap a la punta, perquè la
    primera lletra no toqui la vora de la zona d'on surt la fletxa."""
    amunt = y2 < y1
    o.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 + (8 if amunt else -8)}" stroke="{color}" stroke-width="1.5"/>')
    if amunt:
        o.append(f'<polygon points="{x - 4},{y2 + 8} {x},{y2} {x + 4},{y2 + 8}" fill="{color}"/>')
    else:
        o.append(f'<polygon points="{x - 4},{y2 - 8} {x},{y2} {x + 4},{y2 - 8}" fill="{color}"/>')
    cy = (y1 + y2) / 2 + (-6 if amunt else 6)
    if costat > 0:   # a la dreta de la fletxa, llegint de dalt a baix
        o.append(f'<text x="{cy}" y="{-(x + 8)}" transform="rotate(90)" font-family="{SANS}" font-size="11" '
                 f'fill="{color}" text-anchor="middle">{rotul}</text>')
    else:            # a l'esquerra de la fletxa, llegint de baix a dalt
        o.append(f'<text x="{-cy}" y="{x - 8}" transform="rotate(-90)" font-family="{SANS}" font-size="11" '
                 f'fill="{color}" text-anchor="middle">{rotul}</text>')


def svg(w, h, title, desc, cos):
    """L'amplada i l'alçada van en px, i no width="100%" (svg.md §2, «Figures estretes generades»)."""
    return '\n'.join([f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">',
                      f'<title>{esc(title)}</title>', f'<desc>{esc(desc)}</desc>', *cos, '</svg>']) + '\n'
