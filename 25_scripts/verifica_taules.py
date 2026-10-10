#!/usr/bin/env python3
"""Verificació de la distribució de les columnes de les taules al PDF.

TODO.md, «Revisar la distribució de les columnes de totes les taules» (petició
de l'usuari, 2026-10-03). Tres criteris, mesurats sobre el font i no sobre el
PDF, perquè el PDF no diu de quina taula és cada mot:

  1. DESBORDAMENT: cap element que no es pot partir (un mot de codi, una
     fórmula curta) no ha de ser més ample que la seva columna, perquè surt per
     la dreta i trepitja la columna del costat o el marge.
  2. CEL·LA CURTA PARTIDA: cap mot no s'ha de partir amb guionet perquè no
     cap a la columna («Mnemò-nic», «Ti-pus»), i una cel·la que és un sol
     element de codi (`rd, offset(rs1)`) no s'ha de partir per dins. Que una
     capçalera o un text de diverses paraules passi a dues línies pels espais
     és la composició normal d'una taula, i no compta.
  3. SUMA: cada `tbl-colwidths` ha de sumar 100 i tenir tantes amplades com
     columnes (13_contrib.qmd §Taules).

I un quart, trobat en fer-lo servir: un PEU seguit d'una línia no buida (un
comentari HTML, per exemple) surt literal, «{tbl-colwidths=…}», perquè Pandoc
ajunta les dues línies i els atributs ja no són al final.

I un cinquè (2026-10-10, petició de l'usuari): una taula amb etiqueta `#tbl-` i SENSE
PEU, al peu de la taula («: {#tbl-…}») o dins del div que la porta («::: {#tbl-…}»).
Quarto la numera igualment, i en deixa el peu buit: «Taula 6.1» sola a l'HTML i al PDF.

L'amplada natural de cada cel·la es calcula amb les mètriques reals de les fonts
del PDF (Latin Modern Roman a 11 pt, i DejaVu Sans Mono amb
Scale=MatchLowercase per al codi; _quarto.yml), amb fontTools. Les fórmules
s'aproximen (cursiva per a les lletres, un espai per operador), i per això es
dona un marge del 3 %. L'amplada de cada columna és la que escriu Pandoc:
(L − 2·n·\\tabcolsep) · w, amb L l'amplada del text (481,9 pt) o la de dins
d'un callout (468 pt, mesurada amb pdftotext -bbox).

Sense `tbl-colwidths`, Pandoc fa servir les amplades dels guions de la línia
separadora si alguna línia de la taula passa de 72 caràcters, i amplades
naturals (columnes l/c/r, sense partir) si no; en aquest darrer cas l'únic
risc és que la taula sencera no hi càpiga.

Ús:
    python3 25_scripts/verifica_taules.py            # resum per fitxer i taules amb avisos
    python3 25_scripts/verifica_taules.py --detall   # cada cel·la que falla
    python3 25_scripts/verifica_taules.py --proposa  # amb una proposta de tbl-colwidths
    python3 25_scripts/verifica_taules.py --aplica   # i l'escriu al font (al peu de la taula)

No mira els fitxers que no arriben al PDF: 13_contrib.qmd (HTML) ni els blocs
`.content-visible when-format="html"` o `unless-format="pdf"` (el calendari del laboratori). Els fitxers comentats a _quarto.yml, sí:
són del projecte i arribaran al PDF quan es descomentin.
"""

import re
import subprocess
import sys
from pathlib import Path

from fontTools.ttLib import TTFont

ARREL = Path(__file__).resolve().parent.parent
PT = 11.0                       # cos del text (_quarto.yml, fontsize)
L_PAGINA = 481.89               # 17 cm: A4 menys els marges de 2 cm
L_CALLOUT = 468.0               # dins d'un tcolorbox (mesurat)
TABCOLSEP = 6.0
MARGE = 1.03                    # tolerància de l'estimació

FONTS = {
    "roman": "/usr/share/texmf/fonts/opentype/public/lm/lmroman10-regular.otf",
    "italic": "/usr/share/texmf/fonts/opentype/public/lm/lmroman10-italic.otf",
    "bold": "/usr/share/texmf/fonts/opentype/public/lm/lmroman10-bold.otf",
    "mono": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
}


class Font:
    def __init__(self, ruta, escala=1.0):
        t = TTFont(ruta)
        self.upm = t["head"].unitsPerEm
        self.cmap = t.getBestCmap()
        self.hmtx = t["hmtx"]
        self.escala = escala
        xh = getattr(t["OS/2"], "sxHeight", 0)
        if not xh and "glyf" in t:              # OS/2 antic: l'altura de la «x»
            g = t["glyf"][self.cmap[ord("x")]]
            g.recalcBounds(t["glyf"])
            xh = g.yMax
        self.xh = xh / self.upm
        self.defecte = self.hmtx[self.cmap[ord("n")]][0]

    def amplada(self, text):
        u = sum(self.hmtx[self.cmap[ord(c)]][0] if ord(c) in self.cmap else self.defecte
                for c in text)
        return u / self.upm * PT * self.escala


F = {k: Font(v) for k, v in FONTS.items()}
F["mono"].escala = F["roman"].xh / F["mono"].xh      # Scale=MatchLowercase

# ---------------------------------------------------------------------------
# Amplada natural d'una cel·la
# ---------------------------------------------------------------------------

MATH_SIMBOLS = {
    r"\leftarrow": "←", r"\gets": "←", r"\rightarrow": "→", r"\to": "→",
    r"\land": "∧", r"\lor": "∨", r"\oplus": "⊕", r"\times": "×", r"\cdot": "·",
    r"\ll": "≪", r"\gg": "≫", r"\leq": "≤", r"\geq": "≥", r"\neq": "≠",
    r"\ldots": "…", r"\dots": "…", r"\pm": "±", r"\infty": "∞",
}
OPERADORS = "=+−-←→∧∨⊕×·≤≥≠<>"


def amplada_math(expr):
    """Aproximació de l'amplada d'una fórmula en línia."""
    regles = re.findall(r"\\rule\{([\d.]+)pt\}", expr)
    if regles:                                   # quadrets de color (index.qmd)
        return sum(float(r) for r in regles)
    e = expr
    for k, v in MATH_SIMBOLS.items():
        e = e.replace(k, v)
    e = re.sub(r"\\(text|texttt|mathrm|mathit|mathbf|operatorname)\{([^{}]*)\}", r"\2", e)
    e = re.sub(r"\\overline\{([^{}]*)\}", r"\1", e)
    e = re.sub(r"\\[a-zA-Z]+", "", e)
    sub = re.findall(r"[_^]\{([^{}]*)\}|[_^](.)", e)
    e = re.sub(r"[_^]\{[^{}]*\}|[_^].", "", e)
    e = e.replace("{", "").replace("}", "").replace("\\", "")
    w = 0.0
    for c in e:
        if c == " ":
            continue
        if c.isalpha():
            w += F["italic"].amplada(c)
        else:
            w += F["roman"].amplada(c)
        if c in OPERADORS:
            w += 2 * 0.22 * PT          # \medmuskip/\thickmuskip als dos costats
    for a, b in sub:
        w += 0.7 * F["italic"].amplada(a or b)
    return w


TOKEN = re.compile(
    r"(?P<code>`[^`]+`(?:\{=[a-z]+\})?)|(?P<math>\$[^$]+\$)|(?P<bi>\*\*\*[^*]+\*\*\*)"
    r"|(?P<b>\*\*[^*]+\*\*)|(?P<i>\*[^*]+\*)|(?P<cita>\[@[^\]]+\])|(?P<link>\[[^\]]*\]\([^)]*\))"
    r"|(?P<icona>\\fa[A-Za-z]+)|(?P<ref>@[\w-]+)"
    r"|(?P<sup>\^[^^]+\^)|(?P<text>[^`$*\[@^]+|.)")


def amplada_tokens(text):
    """Amplada d'un tros de cel·la sense espais per on partir, i el seu tipus:
    «text» si només és text (es pot partir amb guionet), «math» si només és una
    fórmula, «codi» si hi ha codi (enganxat a res, no es pot partir)."""
    w, tipus = 0.0, set()
    for m in TOKEN.finditer(text):
        g, t = m.lastgroup, m.group(0)
        if g == "code":
            if t.endswith("{=html}") or t.endswith("{=latex}"):
                continue
            w += F["mono"].amplada(t.strip("`").replace("\x00", " "))
            tipus.add("codi")
        elif g == "math":
            w += amplada_math(t.strip("$").replace("\x01", " "))
            tipus.add("math")
        elif g in ("b", "bi"):
            w += F["bold"].amplada(t.strip("*"))
            tipus.add("text")
        elif g == "i":
            w += F["italic"].amplada(t.strip("*"))
            tipus.add("text")
        elif g == "cita":                   # estil IEEE: [10]
            w += F["roman"].amplada("[10]")
            tipus.add("text")
        elif g == "icona":                  # fontawesome5
            w += PT
            tipus.add("text")
        elif g == "link":
            w += F["roman"].amplada(re.match(r"\[([^\]]*)\]", t).group(1))
            tipus.add("text")
        elif g == "ref":
            w += F["roman"].amplada("Taula 10.10")
            tipus.add("text")
        elif g == "sup":
            w += 0.7 * F["roman"].amplada(t.strip("^"))
            tipus.add("text")
        else:
            w += F["roman"].amplada(re.sub(r"\\(.)", r"\1", t))
            tipus.add("text")
    if "codi" in tipus:
        return w, "codi"
    if tipus == {"math"}:
        return w, "math"
    return w, "text"


def trossos_math(expr):
    """TeX parteix una fórmula en línia després d'una relació o d'un operador
    binari del nivell superior: els trossos que en queden."""
    for k, v in MATH_SIMBOLS.items():
        expr = expr.replace(k, v)
    trossos, act, nivell = [], "", 0
    for c in expr:
        act += c
        nivell += (c == "{") - (c == "}")
        if nivell == 0 and c in "=+<>←→≤≥≠∧∨⊕×":
            trossos.append(act)
            act = ""
    if act:
        trossos.append(act)
    return trossos


def unitats(cel):
    """Unitats (amplada, tipus, text) entre les quals LaTeX pot partir la línia,
    per a cada línia forçada (\\newline) de la cel·la. Tot el que va enganxat sense
    cap espai al font és una sola unitat: «(`malloc()`/`free()`)» no es pot partir."""
    linies = re.split(r"`<br\s*/?>`\{=html\}`\\newline`\{=latex\}|<br\s*/?>", cel)
    res = []
    for li in linies:
        li = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", li)     # d'un enllaç només es veu el text
        # els espais de dins del codi són punts de tall; els de dins d'una fórmula, no
        li = re.sub(r"`[^`]*`", lambda m: m.group(0).replace(" ", "\x00"), li)
        li = re.sub(r"\$[^$]*\$", lambda m: m.group(0).replace(" ", "\x01"), li)
        u = []
        for mot in li.split():
            for tros in mot.split("\x00"):
                if not tros or tros == "`":
                    continue
                fm = re.fullmatch(r"([^$\w]{0,2})\$([^$]+)\$([^$\w]{0,3})", tros)
                if fm:                              # una fórmula, amb la puntuació enganxada
                    parts = trossos_math(fm.group(2).replace("\x01", " "))
                    for k, part in enumerate(parts):
                        w = amplada_math(part)
                        if k == 0:
                            w += F["roman"].amplada(fm.group(1))
                        if k == len(parts) - 1:
                            w += F["roman"].amplada(fm.group(3))
                        u.append((w, "math", tros if k == 0 else "…"))
                    continue
                w, tipus = amplada_tokens(tros if tros.count("`") % 2 == 0 else tros.replace("`", ""))
                if tros.count("`") % 2:
                    tipus = "codi"
                u.append((w, tipus, tros.replace("\x01", " ")))
        res.append(u)
    return res


ESPAI = F["roman"].amplada(" ")


def natural(cel):
    """Amplada natural (una sola línia) de la cel·la, la de l'element més ample
    que no es pot partir (codi, tros de fórmula) i la del mot més ample."""
    lin = unitats(cel)
    nat = max((sum(w for w, _, _ in u) + ESPAI * max(len(u) - 1, 0) for u in lin), default=0)
    indivisible = max((w for u in lin for w, tipus, _ in u if tipus in ("codi", "math")), default=0)
    mot = max((w for u in lin for w, tipus, _ in u if tipus == "text"), default=0)
    return nat, indivisible, mot


CODI_SOL = re.compile(r"^`[^`]+`$")


def minim(cel):
    """Amplada mínima perquè la cel·la no desbordi ni es parteixi malament: el
    seu element indivisible més ample, el mot més ample i, si és un sol element
    de codi, tot el codi."""
    nat, indiv, mot = natural(cel)
    return max(indiv, mot, nat if CODI_SOL.match(cel.strip()) else 0)


# ---------------------------------------------------------------------------
# Lectura de les taules
# ---------------------------------------------------------------------------

SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
INCLUDE = re.compile(r"\{\{<\s*include\s+(\S+)\s*>\}\}")
DIV_OBRE = re.compile(r"^(:{3,})\s*\{(.*)\}\s*$")
DIV_OBRE_NOM = re.compile(r"^:{3,}\s*\S")
DIV_TANCA = re.compile(r"^:{3,}\s*$")
COLW = re.compile(r'tbl-colwidths="\[([^\]]*)\]"')


def fitxers():
    sortida = subprocess.run(["git", "ls-files", "*.qmd"], cwd=ARREL,
                             capture_output=True, text=True).stdout.split()
    return [f for f in sortida if not f.startswith("21_riscv/") and f != "13_contrib.qmd"]


def expandeix(fitxer):
    """Línies del fitxer amb els includes expandits; cada línia porta el número
    de la línia original."""
    base = (ARREL / fitxer).parent
    res = []
    for n, linia in enumerate((ARREL / fitxer).read_text(encoding="utf-8").split("\n"), 1):
        m = INCLUDE.search(linia)
        if m:
            ruta = m.group(1)
            p = (base / ruta) if ruta.startswith("..") else (ARREL / ruta)
            if not p.exists():
                p = base / ruta
            if p.exists():
                for l2 in p.read_text(encoding="utf-8").split("\n"):
                    if l2.strip():
                        res.append((n, l2))
                continue
        res.append((n, linia))
    return res


def celles(linia):
    s = linia.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    parts, act, codi = [], "", False
    i = 0
    while i < len(s):
        c = s[i]
        if c == "`":
            codi = not codi
        if c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            act += "|"
            i += 2
            continue
        if c == "|" and not codi:
            parts.append(act.strip())
            act = ""
        else:
            act += c
        i += 1
    parts.append(act.strip())
    return parts


def taules(fitxer):
    lin = expandeix(fitxer)
    pila = []            # atributs dels divs oberts
    codi = False
    i = 0
    while i < len(lin):
        n, l = lin[i]
        if l.startswith("```"):
            codi = not codi
            i += 1
            continue
        if codi:
            i += 1
            continue
        m = DIV_OBRE.match(l)
        if m:
            pila.append((m.group(2), n))
        elif DIV_OBRE_NOM.match(l) and not DIV_TANCA.match(l):
            pila.append((l, n))
        elif DIV_TANCA.match(l) and pila:
            pila.pop()
        if l.lstrip().startswith("|") and i + 1 < len(lin) and SEP.match(lin[i + 1][1]):
            cap = celles(l)
            sep = celles(lin[i + 1][1])
            files = []
            j = i + 2
            while j < len(lin) and lin[j][1].lstrip().startswith("|"):
                files.append(celles(lin[j][1]))
                j += 1
            peu, n_peu, k_peu = "", None, None
            if j < len(lin) and lin[j][1].startswith(": "):
                peu, n_peu, k_peu = lin[j][1], lin[j][0], j
            elif j + 1 < len(lin) and not lin[j][1].strip() and lin[j + 1][1].startswith(": "):
                peu, n_peu, k_peu = lin[j + 1][1], lin[j + 1][0], j + 1
            # un peu seguit d'una línia no buida: Pandoc les ajunta, i els atributs surten literals
            peu_enganxat = (k_peu is not None and k_peu + 1 < len(lin)
                            and lin[k_peu + 1][1].strip() != "" and not DIV_TANCA.match(lin[k_peu + 1][1]))
            html = any('when-format="html"' in a or 'unless-format="pdf"' in a for a, _ in pila)
            callout = any(".callout" in a for a, _ in pila)
            colw = COLW.search(peu)
            n_colw = n_peu if colw else None
            if not colw:
                for a, na in reversed(pila):
                    colw = COLW.search(a)
                    if colw:
                        n_colw = na
                        break
            llarga = any(len(lin[k][1]) > 72 for k in range(i, j))
            # etiqueta sense peu: al peu («: {#tbl-x …}», sense text davant) o al div que porta la taula
            sense_peu = bool(re.match(r"^:\s*\{[^}]*#tbl-", peu))
            if not peu and pila and "#tbl-" in pila[-1][0]:
                k = j
                while k < len(lin) and not lin[k][1].strip():
                    k += 1
                sense_peu = k >= len(lin) or bool(DIV_TANCA.match(lin[k][1]))
            yield {
                "fitxer": fitxer, "linia": n, "cap": cap, "sep": sep, "files": files,
                "colw": [float(x) for x in colw.group(1).split(",")] if colw else None,
                "n_colw": n_colw, "n_peu": n_peu, "n_fi": lin[j - 1][0], "peu_enganxat": peu_enganxat,
                "callout": callout, "html": html, "llarga": llarga, "peu": peu, "sense_peu": sense_peu,
            }
            i = j
            continue
        i += 1


# ---------------------------------------------------------------------------
# Comprovacions
# ---------------------------------------------------------------------------

def comprova(t):
    n = len(t["sep"])
    L = L_CALLOUT if t["callout"] else L_PAGINA
    avisos = []
    files = [t["cap"]] + t["files"]
    if t["sense_peu"]:
        avisos.append(("peu", "té etiqueta #tbl- i no té peu: Quarto la numera i en deixa el peu buit"))
    if t["peu_enganxat"]:
        avisos.append(("peu", "la línia de després del peu no és buida: Pandoc les ajunta i els atributs surten literals"))
    if t["colw"] is not None:
        if len(t["colw"]) != n:
            avisos.append(("suma", f"tbl-colwidths té {len(t['colw'])} amplades i la taula {n} columnes"))
        if abs(sum(t["colw"]) - 100) > 0.5:
            avisos.append(("suma", f"tbl-colwidths suma {sum(t['colw']):g}"))
        pesos = t["colw"]
    elif t["llarga"]:
        guions = [len(re.sub(r"[^-]", "", c)) for c in t["sep"]]
        pesos = [100 * g / sum(guions) for g in guions]
    else:
        pesos = None
    if pesos is not None and len(pesos) == n:
        tot = sum(pesos)
        for k in range(n):
            W = (L - 2 * n * TABCOLSEP) * pesos[k] / tot
            for r, fila in enumerate(files):
                if k >= len(fila):
                    continue
                cel = fila[k]
                nat, indiv, mot = natural(cel)
                if indiv > W * MARGE:
                    avisos.append(("desborda", f"col. {k + 1}, fila {r}: «{cel[:40]}» necessita {indiv:.0f} pt i en té {W:.0f}"))
                elif mot > W * MARGE:
                    avisos.append(("partida", f"col. {k + 1}, fila {r}: un mot de «{cel[:40]}» fa {mot:.0f} pt i en té {W:.0f}"))
                elif CODI_SOL.match(cel.strip()) and nat > W * MARGE:
                    avisos.append(("partida", f"col. {k + 1}, fila {r}: el codi «{cel[:40]}» fa {nat:.0f} pt i en té {W:.0f}"))
    else:
        total = sum(max((natural(f[k])[0] for f in files if k < len(f)), default=0) + 2 * TABCOLSEP
                    for k in range(n))
        if total > L * MARGE:
            avisos.append(("desborda", f"amplades naturals: la taula fa {total:.0f} pt i n'hi caben {L:.0f}"))
    return avisos, pesos


def minims_percent(t):
    n = len(t["sep"])
    L = L_CALLOUT if t["callout"] else L_PAGINA
    util = L - 2 * n * TABCOLSEP
    files = [t["cap"]] + t["files"]
    return [max((minim(f[k]) for f in files if k < len(f)), default=0) * 1.02 / util * 100
            for k in range(n)]


def proposa(t, pesos):
    """Ajust mínim de les amplades: cada columna que no arriba al seu mínim (el de
    `minim`) s'eixampla fins al mínim, i l'espai es treu de les columnes que en
    tenen de sobres, en proporció al que els sobra. Les altres no canvien.
    None si no hi ha prou espai."""
    n = len(t["sep"])
    if pesos is None or len(pesos) != n:
        return None
    tot = sum(pesos)
    w = [100 * p / tot for p in pesos]
    m = minims_percent(t)
    deficit = sum(max(mk - wk, 0) for mk, wk in zip(m, w))
    sobra = [max(wk - mk, 0) for mk, wk in zip(m, w)]
    if deficit > sum(sobra):
        return None
    nou = [max(wk, mk) - (deficit * sk / sum(sobra) if sum(sobra) else 0)
           for wk, mk, sk in zip(w, m, sobra)]
    enters = [max(int(x), int(mk) + 1 if mk > int(mk) else int(mk)) for x, mk in zip(nou, m)]
    # quadra a 100 traient o posant unitats a les columnes amb més marge
    while sum(enters) != 100:
        if sum(enters) > 100:
            # es treu d'una columna que, amb una unitat menys, encara arribi al mínim estricte
            cand = [k for k in range(n) if enters[k] - 1 >= m[k] / 1.02]
            if not cand:
                return None
            k = max(cand, key=lambda k: enters[k] - m[k])
            enters[k] -= 1
        else:
            k = max(range(n), key=lambda k: nou[k] - enters[k])
            enters[k] += 1
    if any(e < mk / 1.02 for e, mk in zip(enters, m)):   # mk porta un 2 % de marge: basta el mínim estricte
        return None
    return enters


def aplica(canvis):
    """Escriu les amplades proposades al font. `canvis`: {fitxer: [(taula, amplades)]}."""
    for f, llista in canvis.items():
        ruta = ARREL / f
        linies = ruta.read_text(encoding="utf-8").split("\n")
        insercions = []
        for t, w in llista:
            nou = "[" + ",".join(map(str, w)) + "]"
            if t["n_colw"] is not None:
                k = t["n_colw"] - 1
                linies[k] = COLW.sub(f'tbl-colwidths="{nou}"', linies[k], count=1)
            elif t["n_peu"] is not None:
                k = t["n_peu"] - 1
                if re.search(r"\{[^{}]*\}\s*$", linies[k]):
                    linies[k] = re.sub(r"\}\s*$", f' tbl-colwidths="{nou}"}}', linies[k])
                else:
                    linies[k] = linies[k].rstrip() + f' {{tbl-colwidths="{nou}"}}'
            else:
                insercions.append((t["n_fi"], f': {{tbl-colwidths="{nou}"}}'))
        for n, text in sorted(insercions, reverse=True):
            linies.insert(n, text)
        ruta.write_text("\n".join(linies), encoding="utf-8")


def main():
    detall = "--detall" in sys.argv
    amb_proposta = "--proposa" in sys.argv or "--aplica" in sys.argv
    canvis = {}
    n_taules, n_avisos, per_fitxer = 0, 0, {}
    for f in fitxers():
        for t in taules(f):
            if t["html"]:
                continue
            n_taules += 1
            avisos, _ = comprova(t)
            per_fitxer.setdefault(f, [0, 0])
            per_fitxer[f][0] += 1
            if avisos:
                per_fitxer[f][1] += 1
                n_avisos += 1
                tipus = sorted({a for a, _ in avisos})
                colw = "[" + ",".join(f"{x:g}" for x in t["colw"]) + "]" if t["colw"] else (
                    "guions" if t["llarga"] else "natural")
                linia = f"{f}:{t['linia']}  {len(t['sep'])} col.  {colw}  {'callout' if t['callout'] else 'pàgina'}  {', '.join(tipus)}"
                if amb_proposta:
                    p = proposa(t, comprova(t)[1])
                    if p:
                        canvis.setdefault(f, []).append((t, p))
                    linia += f"  → {('[' + ','.join(map(str, p)) + ']') if p else 'no hi cap'}"
                print(linia)
                if detall:
                    for a, msg in avisos:
                        print(f"    {a}: {msg}")
    if "--aplica" in sys.argv:
        aplica(canvis)
        print(f"\nAmplades escrites a {sum(map(len, canvis.values()))} taules de {len(canvis)} fitxers")
    print(f"\n{n_taules} taules al PDF, {n_avisos} amb avisos")
    for f, (nt, na) in sorted(per_fitxer.items()):
        if na:
            print(f"  {f}: {na} de {nt}")
    return 1 if n_avisos else 0


if __name__ == "__main__":
    sys.exit(main())
