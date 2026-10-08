#!/usr/bin/env python3
"""Glossari anglès → català, generat a partir del corpus (secció «Termes» de
12_sigles_simbols.qmd).

Petició de l'usuari (2026-10-05; TODO.md, «Glossari de termes català–anglès»).
La font de veritat és el text: el glossari recull les presentacions
«**terme català** (*english*)» i «**terme català** (***english***)» dels capítols
de teoria, problemes, solucions i laboratori, en l'ordre del llibre
(`chapters:` de `_quarto.yml`), i per a cada terme anglès dona la forma catalana
i el tema de la primera presentació. Només compten les presentacions amb el terme
català en negreta: sense negreta no se sap on comença el terme català.

Avisa de les TRADUCCIONS DIVERGENTS (un mateix terme anglès presentat amb més
d'una forma catalana) i no en corregeix cap: decidir-les és de l'usuari. El
glossari en mostra la forma de la primera presentació.

S'exclouen les sigles (terme «català» tot en majúscules: van a §Sigles) i el
contingut dels blocs de codi, dels comentaris HTML i de la capçalera YAML.

Ús:
    python3 25_scripts/gen_glossari.py               # reescriu la secció
    python3 25_scripts/gen_glossari.py --comprova    # 1 si la secció no és al dia
    python3 25_scripts/gen_glossari.py --divergencies   # només la llista d'avisos

La secció és entre els marcadors <!-- glossari:inici … --> i <!-- glossari:fi -->
de 12_sigles_simbols.qmd. Com els generadors de model (a) de les figures, la
sortida és versionada: cal tornar-lo a executar quan una presentació canvia.
"""

import re
import sys
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
DESTI = ARREL / "12_sigles_simbols.qmd"
INICI = "<!-- glossari:inici"
FI = "<!-- glossari:fi -->"

PRESENTACIO = re.compile(
    r"\*\*([^*\n]{2,60}?)\*\*\s*\((?:\*\*\*|\*)([^*()\n]{2,60}?)(?:\*\*\*|\*)\)")
CODI = re.compile(r"^```.*?^```", re.S | re.M)
COMENTARI = re.compile(r"<!--.*?-->", re.S)
YAML = re.compile(r"\A---\n.*?\n---\n", re.S)


def capitols():
    """Fitxers del llibre en ordre (només teoria, problemes, solucions i laboratori)."""
    cfg = (ARREL / "_quarto.yml").read_text(encoding="utf-8")
    fitxers = re.findall(r"^\s*file:\s*(\S+)\s*$", cfg, re.M)
    return [f for f in fitxers if re.match(r"0[1-4]_[a-z]+/[APSL]\d\.qmd$", f)]


def tema(fitxer):
    nom = Path(fitxer).stem
    return f"T{nom[1]}" if nom[0] in "APS" else f"Lab. {nom[1]}"


def presentacions():
    for f in capitols():
        text = (ARREL / f).read_text(encoding="utf-8")
        # Els trossos exclosos es buiden però conserven els salts de línia, perquè
        # el número de línia dels avisos sigui el del fitxer.
        for exclos in (YAML, CODI, COMENTARI):
            text = exclos.sub(lambda m: "\n" * m.group(0).count("\n"), text)
        for m in PRESENTACIO.finditer(text):
            catala, angles = m.group(1).strip(), m.group(2).strip()
            if catala.upper() == catala:     # sigla: és a §Sigles
                continue
            if "`" in catala:                # nom de codi (`ecall`, `fcsr`): no és una traducció
                continue
            linia = text[:m.start()].count("\n") + 1
            yield angles, catala, f, linia


def recull():
    termes = {}
    for angles, catala, f, linia in presentacions():
        clau = re.sub(r"\s+", " ", angles.lower())
        termes.setdefault(clau, []).append((angles, catala, f, linia))
    return termes


def divergencies(termes):
    """Termes anglesos amb més d'una forma catalana (sense distingir majúscules)."""
    return {k: v for k, v in termes.items()
            if len({c.lower() for _, c, _, _ in v}) > 1}


def taula(termes):
    files = ["| Anglès | Català | Tema |", "| :--- | :--- | :---: |"]
    for clau in sorted(termes, key=lambda k: k.lower()):
        angles, catala, f, _ = termes[clau][0]
        if catala[:1].isupper() and catala[1:] == catala[1:].lower():
            catala = catala[0].lower() + catala[1:]   # majúscula d'inici de frase, no d'un nom («NaN»)
        files.append(f"| *{angles}* | {catala} | {tema(f)} |")
    files.append(': {tbl-colwidths="[40,45,15]" .striped}')
    return "\n".join(files)


def seccio(termes):
    return (f"{INICI} (generat per 25_scripts/gen_glossari.py a partir del corpus; no l'editeu a mà) -->\n"
            f"{taula(termes)}\n\n{FI}")   # la línia en blanc: si no, Pandoc ajunta el comentari al peu i n'escriu els atributs


def informe(div):
    linies = []
    for clau in sorted(div):
        formes = {}
        for _, catala, f, linia in div[clau]:
            formes.setdefault(catala, []).append(f"{Path(f).name}:{linia}")
        detall = "; ".join(f"«{c}» ({', '.join(llocs)})" for c, llocs in formes.items())
        linies.append(f"- *{div[clau][0][0]}*: {detall}")
    return "\n".join(linies)


def main():
    termes = recull()
    div = divergencies(termes)
    n = sum(len(v) for v in termes.values())
    if "--divergencies" in sys.argv:
        print(informe(div))
        return 0
    text = DESTI.read_text(encoding="utf-8")
    i, j = text.find(INICI), text.find(FI)
    if i < 0 or j < 0:
        print(f"ERROR: falten els marcadors {INICI} … {FI} a {DESTI.name}", file=sys.stderr)
        return 2
    nou = text[:i] + seccio(termes) + text[j + len(FI):]
    if "--comprova" in sys.argv:
        if nou != text:
            print(f"[gen-glossari] {DESTI.name}: la secció «Termes» no és al dia", file=sys.stderr)
            return 1
        print(f"[gen-glossari] al dia: {len(termes)} termes, {n} presentacions")
        return 0
    if nou != text:
        DESTI.write_text(nou, encoding="utf-8")
    print(f"[gen-glossari] {len(termes)} termes, {n} presentacions, "
          f"{len(div)} amb traduccions divergents (--divergencies)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
