#!/usr/bin/env python3
"""Les sigles del text, contra [sigles] de 24_specs/termes.toml (13_contrib.qmd §Sigles, símbols i
notació; D-89, D-118).

El format únic de l'expansió, el de la guia:

    forma catalana (*expansió anglesa*, SIGLA)    «unitat d'estat sòlid (*solid-state drive*, SSD)»
    *expansió anglesa* (SIGLA)                    «*not a number* (NaN)», sense forma catalana
    forma catalana (SIGLA)                        «sistema operatiu (SO)», sense expansió anglesa

amb les formes `ca` i `en` de la sigla. L'anglès, en cursiva, amb les majúscules del fitxer (la
primera lletra pot anar en majúscula, a l'inici d'una frase) i, si cal, en plural; la sigla, en
rodona; la forma catalana, amb negreta o sense i, si cal, en plural.

La comprovació (--comprova) llegeix el llibre en l'ordre de `chapters:` de _quarto.yml, amb la
Presentació (index.qmd) al principi i el compendi (11_riscv.qmd) al final, i els fragments de
21_riscv/ al lloc on s'inclouen; no llegeix 10_continguts.qmd, 12_sigles_simbols.qmd, la guia ni
14_LICENSE.qmd. Atura el commit amb:
  - una sigla de la taula que no s'expandeix, en el format únic, a la primera aparició del llibre
    fora dels aprofundiments; si aquesta aparició és en un títol, en una taula o en una fórmula,
    l'expansió pot anar al paràgraf següent (en una fórmula, també a la resta del paràgraf);
  - una expansió que no segueix el format únic, on sigui, també als aprofundiments: la sigla dins
    d'un parèntesi que va darrere de la forma catalana o de l'expansió anglesa, o que les conté, o la
    sigla seguida d'un parèntesi que les conté («**NaN** (*Not a Number*)»);
  - una sigla del text, fora dels aprofundiments, que no és a la taula ni a [no_sigles]: un mot de
    dues majúscules o més, sense minúscules, fora del codi, de les fórmules i de les cursives (les
    parts d'un compost amb barra, per separat), tret de les unitats (KB, GB), els noms de les
    variants de RISC-V (RV32I, RVA23) i les operacions lògiques (AND, OR, XOR, NOT);
  - una sigla de la taula en plural (D-79), com «PTEs»;
  - una sigla de la taula sense cap aparició fora dels aprofundiments;
  - una sigla amb l'expansió anglesa d'un terme de [termes] i una forma catalana que no és la del terme.
Les sigles amb `excepcio` no es comproven al text. Les cursives no compten com a aparició: una
sigla dins d'una expansió anglesa («*Advanced RISC Machines*») no és una aparició de RISC.

Ús:
    python3 25_scripts/sigles.py --comprova   # 1 si troba res
    python3 25_scripts/sigles.py --llista     # la primera aparició de cada sigla, per revisar-la
"""

import re
import sys
import tomllib
from pathlib import Path

import gen_glossari

ARREL = Path(__file__).resolve().parent.parent
DADES = ARREL / "24_specs" / "termes.toml"
FORA = {"10_continguts.qmd", "12_sigles_simbols.qmd", "13_contrib.qmd", "14_LICENSE.qmd"}
INCLUDE = re.compile(r"^\{\{< include (\S+) >\}\}\s*$")
FENCE = re.compile(r"^\s*(?:(?:[-*+]|\d+[.)])\s+)?(`{3,}|~{3,})")
DIV_TANCA = re.compile(r"^\s*:{3,}\s*$")
DIV_OBRE = re.compile(r"^\s*:{3,}\s*\S")
MOT = re.compile(r"(?<![\w-])([A-Za-z0-9][A-Za-z0-9&]*(?:/[A-Za-z0-9&]+)*)(?![\w-])")
CURSIVA = re.compile(r"(?<![\w*])(\*{1,3})(?!\s)[^*\n]+?(?<!\s)\1(?![\w*])")
MATES = re.compile(r"(?<!\\)\$\$?[^$]+?(?<!\\)\$\$?")
TEXT_MATES = re.compile(r"\\text\{([^{}]*)\}")
UNITATS = re.compile(r"[KMGTPE]B")
RISCV = re.compile(r"RV\d+[A-Z]*|RV[A-Z]+\d+[A-Z0-9]*")
LOGIQUES = {"AND", "OR", "XOR", "NOT", "NAND", "NOR", "XNOR"}


def capitols():
    """Els fitxers del llibre en l'ordre de `chapters:`, també els comentats (CLAUDE.md), sense
    els que no són text del llibre (FORA)."""
    cfg = (ARREL / "_quarto.yml").read_text(encoding="utf-8")
    return [f for f in re.findall(r"^[\s#]*file:\s*(\S+)\s*$", cfg, re.M) if f not in FORA]


def linies(f, fus, vist):
    """(fitxer, línia, text) en ordre de lectura, amb els include al seu lloc."""
    vist.add(f)
    for n, l in enumerate((ARREL / f).read_text(encoding="utf-8").split("\n"), 1):
        m = INCLUDE.match(l.strip())
        if not m:
            yield f, n, l
            continue
        ruta = m.group(1)
        if ruta.startswith("auto_riscv/"):
            incl = fus.get(Path(ruta).name, [])
        elif ruta.startswith("auto_"):
            incl = []
        else:
            incl = [str(((ARREL / f).parent / ruta).resolve().relative_to(ARREL))]
        for g in incl:
            if g not in vist and (ARREL / g).exists():
                yield from linies(g, fus, vist)


def neteja(l, literals):
    """La línia sense el que no és text (el codi, els enllaços, els atributs…), amb la negreta, la
    cursiva i els parèntesis; i les sigles de les fórmules (\\text{…}), a part."""
    mates = [t for m in MATES.finditer(l) for t in TEXT_MATES.findall(m.group(0))]
    l = re.sub(r"<!--.*?-->", " ", l)
    l = re.sub(r"(`+).+?\1", "\x00", l)
    l = MATES.sub("\x00", l)
    l = re.sub(r"\{\{<.*?>\}\}", "\x00", l)
    l = re.sub(r"!\[(?:[^\[\]]|\[[^\[\]]*\])*\]\((?:[^()]|\([^()]*\))*\)", "\x00", l)
    l = re.sub(r"\[-?@[^\[\]]*\]", "\x00", l)
    l = re.sub(r"\[\^[^\]]*\]:?", " ", l)
    for _ in range(2):
        l = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\{[^{}]*\}", r"\1", l)
        l = re.sub(r"(?<!!)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\((?:[^()]|\([^()]*\))*\)", r"\1", l)
    l = re.sub(r"https?://\S+", "\x00", l)
    l = re.sub(r"(?<![\w.])-?@[A-Za-z][\w:.-]*\w", "\x00", l)
    l = re.sub(r"\{[^{}]*\}", "\x00", l)
    l = re.sub(r"<[^<>]*>", "\x00", l)
    for t in literals:
        l = l.replace(t, "\x00")
    return l, mates


def unitats(literals):
    """[(fitxer, línia, tipus, text, wrn, bloc, mates)] del llibre, en ordre: tipus és «titol»,
    «taula», «formula» o «text»; bloc, el número del paràgraf (una taula, un títol o una fórmula
    destacada en són un de sencer; una llista, també)."""
    fus = gen_glossari.fusions()
    res = []
    bloc = 0
    for cap in capitols():
        fence = None
        math = coment = False
        pila = []
        yaml = False
        for k, (f, n, l) in enumerate(linies(cap, fus, set())):
            s = l.strip()
            if k == 0 and s == "---":
                yaml = True
                continue
            if yaml:
                yaml = s not in ("---", "...")
                continue
            if fence:
                m = FENCE.match(l)
                if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] and not l[m.end():].strip():
                    fence = None
                continue
            m = FENCE.match(l)
            if m:
                fence = (m.group(1)[0], len(m.group(1)))
                bloc += 1
                continue
            if coment:
                coment = "-->" not in l
                continue
            if "<!--" in l and "-->" not in l.split("<!--", 1)[1]:
                coment = True
                l = l.split("<!--", 1)[0]
                s = l.strip()
            wrn = any(pila)
            if math:
                math = "$$" not in s
                res.append((f, n, "formula", "", wrn, bloc, TEXT_MATES.findall(l)))
                if not math:
                    bloc += 1
                continue
            if s.startswith("$$") and s.count("$$") == 1:
                math = True
                bloc += 1
                res.append((f, n, "formula", "", wrn, bloc, TEXT_MATES.findall(l)))
                continue
            if DIV_TANCA.match(l):
                if pila:
                    pila.pop()
                bloc += 1
                continue
            if DIV_OBRE.match(l):
                pila.append("callout-warning" in l or "#wrn-" in l)
                bloc += 1
                continue
            if not s:
                bloc += 1
                continue
            text, mates = neteja(l, literals)
            if s.startswith("#"):
                bloc += 1
                res.append((f, n, "titol", text, wrn, bloc, mates))
                bloc += 1
            elif s.startswith("$$"):
                bloc += 1
                res.append((f, n, "formula", "", wrn, bloc, mates))
                bloc += 1
            elif s.startswith("|") or (s.startswith(": ") and res and res[-1][2] == "taula" and res[-1][5] == bloc):
                if not (res and res[-1][2] == "taula" and res[-1][5] == bloc):
                    bloc += 1
                res.append((f, n, "taula", text, wrn, bloc, mates))
            else:
                if res and res[-1][2] == "taula" and res[-1][5] == bloc:
                    bloc += 1
                res.append((f, n, "text", text, wrn, bloc, mates))
    return res


def italiques(text):
    """Els intervals de les cursives (simples o amb negreta) del text."""
    return [(m.start(), m.end()) for m in CURSIVA.finditer(text) if len(m.group(1)) != 2]


def mots(text):
    """(posició, sigla o mot) dels mots candidats del text, fora de les cursives; els compostos
    amb barra, per parts, tret dels que són sencers a la taula (E/S)."""
    curs = italiques(text)
    for m in MOT.finditer(text):
        if any(a <= m.start() < b for a, b in curs):
            continue
        yield m.start(), m.group(1)


class Sigles:
    def __init__(self):
        d = tomllib.loads(DADES.read_text(encoding="utf-8"))
        self.d = d
        self.sigles = d.get("sigles", {})
        self.no = d.get("no_sigles", {})
        self.literals = [k for k in self.no if not re.fullmatch(r"[A-Za-z0-9&/]+", k)]
        self.mots_no = {k for k in self.no if k not in self.literals}

    def parts(self, mot):
        if mot in self.sigles or "/" not in mot:
            return [mot]
        return mot.split("/")

    # --- el format de l'expansió ---------------------------------------------------------

    def acaba_amb_ca(self, prefix, ca):
        p = re.sub(r"\*\*|[«»]", "", prefix).rstrip().lower()
        for forma in {ca.lower(), gen_glossari.plural(ca).lower()}:
            if p.endswith(forma) and (len(p) == len(forma) or not re.match(r"\w", p[-len(forma) - 1])):
                return True
        return False

    def pat_en(self, en):
        return f"[{en[0].upper()}{en[0].lower()}]{re.escape(en[1:])}s?"

    def canonica(self, s, prefix, dins):
        e = self.sigles[s]
        ca, en = e.get("ca"), e.get("en")
        if ca and en:
            return bool(re.fullmatch(rf"\*{self.pat_en(en)}\*, {re.escape(s)}", dins)) and self.acaba_amb_ca(prefix, ca)
        if dins != s:
            return False
        if en:
            return bool(re.search(rf"(?<!\*)\*{self.pat_en(en)}\*\s*$", prefix))
        return self.acaba_amb_ca(prefix, ca)

    def intent(self, s, text, pos):
        """(canònica, fragment) si l'aparició de `s` a `pos` és una expansió, o None."""
        e = self.sigles[s]
        formes = [norm(x) for x in (e.get("ca"), e.get("en"), e.get("ca") and gen_glossari.plural(e["ca"]),
                                    e.get("en") and e["en"] + "s") if x]
        # la sigla dins d'un parèntesi
        obre, fond = None, 0
        for i in range(pos - 1, -1, -1):
            if text[i] == ")":
                fond += 1
            elif text[i] == "(":
                if fond == 0:
                    obre = i
                    break
                fond -= 1
        if obre is not None:
            tanca, fond = None, 0
            for i in range(pos, len(text)):
                if text[i] == "(":
                    fond += 1
                elif text[i] == ")":
                    if fond == 0:
                        tanca = i
                        break
                    fond -= 1
            if tanca is not None:
                prefix, dins = text[:obre], text[obre + 1:tanca].strip()
                np_ = norm(prefix)
                if any(np_.endswith(x) for x in formes) or any(x in norm(dins) for x in formes):
                    # el parèntesi no pot anar dins d'una negreta («**interfície d'usuari (UI)**»)
                    negreta = re.sub(r"(?<!\*)\*(?!\*)|\*{3}", "", text[:obre]).count("**") % 2 == 1
                    return (not negreta and self.canonica(s, prefix, dins)), text[max(0, obre - 60):tanca + 1]
        # la sigla seguida d'un parèntesi que conté l'expansió
        m = re.compile(r"\**\s*\(([^()]*)\)").match(text, pos + len(s))
        if m and any(x in norm(m.group(1)) for x in formes):
            return False, text[pos:m.end()]
        return None

    # --- la comprovació ---------------------------------------------------------------------

    def recorre(self):
        u = unitats(self.literals)
        primera, aparicions, errors, intents = {}, {}, [], []
        for idx, (f, n, tipus, text, wrn, bloc, mates) in enumerate(u):
            trobats = [(p, w, "mot") for p, w in mots(text)] + [(None, w, "formula")
                                                                 for t in mates for w in MOT.findall(t)]
            for pos, mot, on in trobats:
                for part in self.parts(mot):
                    lloc = f"{f}:{n}"
                    if part in self.sigles:
                        if self.sigles[part].get("excepcio"):
                            continue
                        if not wrn:
                            aparicions.setdefault(part, []).append(idx)
                        if on == "mot":
                            r = self.intent(part, text, pos + mot.find(part))
                            if r:
                                intents.append((part, idx, r[0]))
                                if not r[0]:
                                    errors.append(f"{lloc}: {part}: l'expansió no segueix el format únic "
                                                  f"(«{self.forma(part)}»): …{r[1]}…")
                        if not wrn and part not in primera:
                            primera[part] = (idx, on)
                    elif part in self.mots_no or wrn or on == "formula":
                        continue
                    elif part.endswith("s") and part[:-1] in self.sigles:
                        errors.append(f"{lloc}: «{part}»: les sigles no porten plural (D-79)")
                    elif re.fullmatch(r"[A-Z0-9&]+", part) and sum(c.isupper() for c in part) >= 2 \
                            and not (UNITATS.fullmatch(part) or RISCV.fullmatch(part) or part in LOGIQUES):
                        errors.append(f"{lloc}: «{part}»: no és a [sigles] de termes.toml; si és una sigla, "
                                      f"afegiu-l'hi i expandiu-la a la primera aparició; si no, a [no_sigles]")
        return u, primera, aparicions, errors, intents

    def forma(self, s):
        e = self.sigles[s]
        if e.get("ca") and e.get("en"):
            return f"{e['ca']} (*{e['en']}*, {s})"
        return f"*{e['en']}* ({s})" if e.get("en") else f"{e['ca']} ({s})"

    def comprova(self):
        u, primera, aparicions, errors, intents = self.recorre()
        bons = {(s, idx) for s, idx, ok in intents if ok}
        for s, e in self.sigles.items():
            if e.get("excepcio"):
                continue
            if s not in primera:
                errors.append(f"{DADES.name}: {s}: cap aparició al text fora dels aprofundiments "
                              f"(13_contrib.qmd §Sigles, criteri d'inclusió)")
                continue
            idx, on = primera[s]
            f, n, tipus, text, wrn, bloc, mates = u[idx]
            if (s, idx) in bons:
                continue
            if tipus in ("titol", "taula", "formula") or on == "formula":
                if self.expandida_despres(s, u, idx, bons, tipus == "formula" or on == "formula"):
                    continue
            errors.append(f"{f}:{n}: {s}: la primera aparició del llibre no s'expandeix "
                          f"(«{self.forma(s)}»){' ni al paràgraf següent' if tipus != 'text' or on == 'formula' else ''}")
        termes = self.d.get("termes", {})
        for s, e in self.sigles.items():
            t = termes.get((e.get("en") or "").lower())
            if t and e.get("ca", "").lower() != t["ca"].lower():
                errors.append(f"{DADES.name}: {s}: l'expansió anglesa és el terme *{e['en']}*, que [termes] "
                              f"diu «{t['ca']}», i la forma catalana de la sigla és «{e.get('ca')}»")
        return errors

    def expandida_despres(self, s, u, idx, bons, mateix_bloc):
        """Si la sigla s'expandeix al paràgraf següent (o, si `mateix_bloc`, a la resta del paràgraf)."""
        bloc = u[idx][5]
        seguent = None
        for j in range(idx + 1, len(u)):
            if u[j][4]:
                continue
            if u[j][5] == bloc:
                if mateix_bloc and (s, j) in bons:
                    return True
                continue
            if u[j][2] != "text":
                if seguent is None:
                    continue
            if seguent is None:
                seguent = u[j][5]
            if u[j][5] != seguent:
                return False
            if (s, j) in bons:
                return True
        return False


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_«»\x00]", "", s)).strip().lower()


def main():
    if sys.argv[1:] not in (["--comprova"], ["--llista"]):
        print(__doc__.split("Ús:")[1].rstrip(), file=sys.stderr)
        return 2
    S = Sigles()
    if sys.argv[1] == "--llista":
        u, primera, aparicions, errors, intents = S.recorre()
        for s in sorted(S.sigles, key=gen_glossari.clau_sigla):
            if s in primera:
                f, n, tipus, text, *_ = u[primera[s][0]]
                print(f"{s}\t{f}:{n}\t{tipus}\t{text.strip()[:140]}")
            else:
                print(f"{s}\t—")
        return 0
    errors = S.comprova()
    for e in errors:
        print(f"[sigles] {e}", file=sys.stderr)
    if errors:
        print(f"[sigles] {len(errors)} errors (13_contrib.qmd §Sigles, símbols i notació; D-118)", file=sys.stderr)
        return 1
    print(f"[sigles] al dia: {len(S.sigles)} sigles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
