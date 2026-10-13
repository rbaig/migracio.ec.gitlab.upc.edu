#!/usr/bin/env python3
"""Glossari anglès → català (secció «Termes» de 12_sigles_simbols.qmd), generat a
partir de 24_specs/termes.toml, i comprovació de les presentacions del text.

Petició de l'usuari (2026-10-05; TODO.md, «Glossari de termes català–anglès»).
La font de veritat del lèxic és 24_specs/termes.toml (D-115, que inverteix D-100):
per a cada terme anglès, la forma catalana, les observacions d'ús i, si es manté
en anglès, el motiu. El text només hi posa on es presenta cada terme: la columna
«Tema» és la del capítol de la primera presentació «**terme català** (*english*)»
o «**terme català** (***english***)», en l'ordre del llibre (`chapters:` de
`_quarto.yml`; teoria, problemes, solucions i laboratori). Només compten les
presentacions amb el terme català en negreta: sense negreta no se sap on comença
el terme català.

La comprovació (--comprova, i també en generar) troba:
  - una presentació d'un terme que no és a termes.toml (un terme nou: s'hi afegeix);
  - una presentació amb una forma catalana que no és la de termes.toml, ni el seu
    plural, ni una de les formes de `presentacio` del terme;
  - una presentació en català d'un terme que el llibre manté en anglès;
  - un terme de termes.toml sense cap presentació al text, que no tindria tema;
  - i, com a avís, un terme que sembla en plural i no és a `nombre` (D-108).

S'exclouen les sigles (terme «català» tot en majúscules: van a §Sigles), les
expansions de sigla que ja són a §Sigles (l'anglès és l'expansió d'una sigla, com
«**NaN** (*Not a Number*)»: no és una traducció) i el contingut dels blocs de codi,
dels comentaris HTML i de la capçalera YAML.

Ús:
    python3 25_scripts/gen_glossari.py               # escriu auto_termes/glossari.qmd i glossari_angles.qmd
    python3 25_scripts/gen_glossari.py --comprova    # 1 si el text no coincideix amb termes.toml

La secció la inclou 12_sigles_simbols.qmd amb dos {{< include auto_termes/… >}}, un per taula.
Com auto_riscv/ (D-3), el fitxer ha d'existir abans d'invocar `quarto`, perquè Quarto
resol els include abans del pre-render: `make render` i `make taules` el generen. No
es versiona (D-104).
"""

import re
import sys
import tomllib
from pathlib import Path

from taula_md import majuscula, taula

ARREL = Path(__file__).resolve().parent.parent
SIGLES = ARREL / "12_sigles_simbols.qmd"
DADES = ARREL / "24_specs" / "termes.toml"
SORTIDA = ARREL / "auto_termes" / "glossari.qmd"
SORTIDA_ANGLES = ARREL / "auto_termes" / "glossari_angles.qmd"

PRESENTACIO = re.compile(
    r"\*\*([^*\n]{2,60}?)\*\*\s*\((?:\*\*\*|\*)([^*()\n]{2,60}?)(?:\*\*\*|\*)\)")
CODI = re.compile(r"^```.*?^```", re.S | re.M)
COMENTARI = re.compile(r"<!--.*?-->", re.S)
YAML = re.compile(r"\A---\n.*?\n---\n", re.S)
PREPOSICIO = {"de", "a", "en", "per", "amb", "sense", "del", "al"}


def capitols():
    """Fitxers del llibre en ordre (només teoria, problemes, solucions i laboratori)."""
    cfg = (ARREL / "_quarto.yml").read_text(encoding="utf-8")
    fitxers = re.findall(r"^\s*file:\s*(\S+)\s*$", cfg, re.M)
    return [f for f in fitxers if re.match(r"0[1-4]_[a-z]+/[APSL]\d\.qmd$", f)]


def tema(fitxer):
    nom = Path(fitxer).stem
    return f"T{nom[1]}" if nom[0] in "APS" else f"L{nom[1]}"


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


def normalitza(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_]", "", s)).strip().lower()


def expansions_de_sigles():
    """Les expansions de la taula de §Sigles de 12_sigles_simbols.qmd, normalitzades."""
    text = SIGLES.read_text(encoding="utf-8")
    seccio = text.split("\n## Sigles", 1)[1].split("\n## ", 1)[0]
    return {normalitza(m.group(1)) for m in re.finditer(r"^\| \*\*[^|]+\*\* \| ([^|]+) \|", seccio, re.M)}


def recull():
    """[(anglès, català, fitxer, línia)] de les presentacions del text, en l'ordre del llibre."""
    sigles = expansions_de_sigles()
    return [p for p in presentacions() if normalitza(p[0]) not in sigles]


def dades():
    return tomllib.loads(DADES.read_text(encoding="utf-8"))


def plural_mot(m):
    """El plural d'un mot català, per a les formes regulars dels termes."""
    if m.endswith("ió"):
        return m[:-2] + "ions"
    for sing, plur in (("ca", "ques"), ("ga", "gues"), ("ja", "ges"), ("ça", "ces"),
                       ("qua", "qües"), ("gua", "gües"), ("a", "es")):
        if m.endswith(sing):
            return m[:-len(sing)] + plur
    return m + "s"


def plural(forma):
    """El plural d'una forma catalana: cada mot fins a la primera preposició («fil d'execució»)."""
    mots = forma.split(" ")
    for i, m in enumerate(mots):
        if m.lower() in PREPOSICIO or re.match(r"[dl]['’]", m.lower()):
            break
        mots[i] = "/".join(plural_mot(p) for p in m.split("/"))
    return " ".join(mots)


def clau_angles(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def index_termes(d):
    """{clau anglesa: (clau de termes.toml, estat)}, amb el plural anglès (-s, -es) de cada terme."""
    index = {}
    for clau in d.get("termes", {}):
        k = clau_angles(clau)
        for variant in (k, k + "s", k + "es"):
            index.setdefault(variant, (clau, "catala"))
    for clau in d.get("en_angles", {}):
        for part in clau.split(","):
            index[clau_angles(part)] = (clau, "angles")
    return index


def admeses(entrada):
    """Les formes catalanes que pot tenir la presentació d'un terme, en minúscules."""
    ca = entrada["ca"]
    return {f.lower() for f in [ca, plural(ca), *entrada.get("presentacio", [])]}


def comprova(pres, d):
    """(errors, avisos, {clau: tema}) de les presentacions del text contra termes.toml."""
    termes, index = d.get("termes", {}), index_termes(d)
    errors, avisos, temes = [], [], {}
    for angles, catala, f, linia in pres:
        lloc = f"{f}:{linia}"
        trobat = index.get(clau_angles(angles))
        if not trobat:
            errors.append(f"{lloc}: «**{catala}** (*{angles}*)»: *{angles}* no és a {DADES.name}; "
                          f"si és un terme nou, afegiu-hi a [termes]: \"{angles}\" = {{ ca = \"{catala}\" }}")
            continue
        clau, estat = trobat
        if estat == "angles":
            errors.append(f"{lloc}: «**{catala}** (*{angles}*)»: el llibre manté *{angles}* en anglès "
                          f"([en_angles] de {DADES.name})")
            continue
        if catala.lower() not in admeses(termes[clau]):
            errors.append(f"{lloc}: «**{catala}** (*{angles}*)»: {DADES.name} diu «{termes[clau]['ca']}»; "
                          f"corregiu el text o, si la forma és bona, poseu-la a `presentacio` del terme")
        temes.setdefault(clau, tema(f))
    for clau in termes:
        if clau not in temes:
            errors.append(f"{DADES.name}: «{clau}» no té cap presentació «**…** (*{clau}*)» al text")
    for clau, entrada in termes.items():
        if entrada.get("nombre"):
            continue
        if clau.lower().endswith("s") or entrada["ca"].split()[0].lower().endswith("s"):
            avisos.append(f"sembla un plural (13_contrib.qmd §Glossari, D-108): *{clau}* | {entrada['ca']}; "
                          f"poseu-ne el singular a {DADES.name}, o `nombre` al terme")
    return errors, avisos, temes


def taula_termes(d, temes):
    files = []
    for clau in sorted(d.get("termes", {}), key=str.lower):
        e = d["termes"][clau]
        files.append([f"*{majuscula(clau)}*", majuscula(e["ca"]), temes.get(clau, ""), majuscula(e.get("obs", ""))])
    return taula([("Anglès", ":---"), ("Català", ":---"), ("Tema", ":---:"), ("Observacions", ":---")], files,
                 'Termes anglesos i la forma catalana que fa servir el llibre. {#tbl-termes tbl-colwidths="[24,24,8,44]" .striped}')


def taula_angles(en_angles):
    files = []
    for clau in sorted(en_angles, key=str.lower):
        angles = majuscula(", ".join(f"*{a.strip()}*" for a in clau.split(",")))
        files.append([angles, majuscula(en_angles[clau]["ca"]), majuscula(en_angles[clau]["motiu"])])
    return taula([("Anglès", ":---"), ("Terme català", ":---"), ("Motiu", ":---")], files,
                 'Termes mantinguts en anglès. {#tbl-termes-angles tbl-colwidths="[18,28,54]" .striped}')


def sortides(d, temes):
    """{fitxer: contingut}: una taula per fitxer, perquè verifica_taules.py, que llegeix un include
    sense les línies en blanc, no ajunti el peu de la primera amb la segona."""
    marca = "<!-- generat per 25_scripts/gen_glossari.py a partir de 24_specs/termes.toml; no l'editeu a mà -->\n"
    return {SORTIDA: f"{marca}{taula_termes(d, temes)}\n",
            SORTIDA_ANGLES: f"{marca}{taula_angles(d.get('en_angles', {}))}\n"}


def main():
    if set(sys.argv[1:]) - {"--comprova"}:
        print(__doc__.split("Ús:")[1].split("La secció")[0].rstrip(), file=sys.stderr)
        return 2
    d = dades()
    pres = recull()
    errors, avisos, temes = comprova(pres, d)
    for a in avisos:
        print(f"[gen-glossari] avís: {a}", file=sys.stderr)
    for e in errors:
        print(f"[gen-glossari] {e}", file=sys.stderr)
    n = len(d.get("termes", {}))
    if "--comprova" in sys.argv:
        if errors or avisos:
            print(f"[gen-glossari] el text no coincideix amb {DADES.name} (13_contrib.qmd §Anglicismes)", file=sys.stderr)
            return 1
        print(f"[gen-glossari] al dia: {n} termes, {len(pres)} presentacions")
        return 0
    SORTIDA.parent.mkdir(exist_ok=True)
    for fitxer, nou in sortides(d, temes).items():
        if not fitxer.exists() or fitxer.read_text(encoding="utf-8") != nou:
            fitxer.write_text(nou, encoding="utf-8")
    print(f"[gen-glossari] {SORTIDA.parent.relative_to(ARREL)}/: {n} termes, {len(pres)} presentacions"
          + (f", {len(errors)} errors (--comprova)" if errors else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
