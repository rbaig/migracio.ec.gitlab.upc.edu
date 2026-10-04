"""
figlib.py — Primitives compartides dels generadors de figures d'EC.

Portes lògiques i fils segons la convenció de `24_specs/svg.md §16` (forma
distintiva ANSI/IEEE 91, traç de 1,5 px, unions amb un punt ple i terminals
amb un cercle buit). Cada funció retorna el fragment SVG com a cadena: qui la
crida decideix on l'afegeix.

La fan servir `gen_T4_sumador.py` (les figures del sumador de T4) i
`gen_MC.py` (els diagrames de blocs de la lectura de la memòria cau, T7).
Només fa servir la biblioteca estàndard.
"""

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
