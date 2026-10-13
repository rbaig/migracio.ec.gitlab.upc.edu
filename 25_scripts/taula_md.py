"""Taules Markdown generades a partir de dades: la capçalera, les files i el peu amb els
atributs de Quarto (D-115). La fan servir els generadors de taules del llibre que
llegeixen un fitxer de dades (gen_glossari.py); no és cap script."""

import re


def majuscula(s):
    """La primera lletra de la cel·la, en majúscula, encara que vagi darrere de `*`, `«` o `(` (D-108)."""
    m = re.search(r"[^\W\d_]", s)
    return s if not m else s[:m.start()] + s[m.start()].upper() + s[m.start() + 1:]


def taula(columnes, files, peu):
    """La taula: columnes, [(títol, alineació)], amb l'alineació en la sintaxi de Markdown
    (`:---`, `:---:`); files, les cel·les ja escrites; peu, el text del peu amb els atributs."""
    linies = ["| " + " | ".join(t for t, _ in columnes) + " |",
              "| " + " | ".join(a for _, a in columnes) + " |"]
    linies += ["| " + " | ".join(f) + " |" for f in files]
    linies.append(f": {peu}")
    return "\n".join(linies)
