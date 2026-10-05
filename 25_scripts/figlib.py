"""
figlib.py — Primitives compartides dels generadors de figures d'EC.

Portes lògiques i fils segons la convenció de `24_specs/svg.md §16` (forma
distintiva ANSI/IEEE 91, traç de 1,5 px, unions amb un punt ple i terminals
amb un cercle buit). Cada funció retorna el fragment SVG com a cadena: qui la
crida decideix on l'afegeix.

La fan servir `gen_T4_sumador.py` (les figures del sumador de T4) i
`gen_MC.py` (els diagrames de blocs de la lectura de la memòria cau, T7).
El text, les caixes i les fletxes, del final, són de `gen_T7.py` i
`gen_T8.py` (les figures soltes de T7 i T8).
Només fa servir la biblioteca estàndard.
"""
import math

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
    return '\n'.join([f'<svg width="100%" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">',
                      f'<title>{titol}</title>', f'<desc>{desc}</desc>', *cos, '</svg>']) + '\n'
