#!/usr/bin/env python3
"""Autoproves de les comprovacions del llibre (13_contrib.qmd §Autoproves de les comprovacions; D-120).

Una comprovació que no detecta el que ha de detectar és pitjor que no tenir-ne: dona per bo el que
no ho és. Les autoproves ho vigilen. Cada bateria fa passar una comprovació real per uns casos
coneguts: un text correcte, en què no ha de trobar res, i un text per cada error que ha d'aturar,
en què ha de trobar exactament aquest error. Si una eina canvia i deixa de veure un error, o en
comença a veure on no n'hi ha, l'autoprova falla.

No toquen el llibre: cada cas munta un llibre mínim en un directori temporal (amb `_quarto.yml`,
els fitxers del cas i el seu `24_specs/termes.toml`) i hi executa l'eina, com a procés a part (una
còpia de l'script al directori temporal) o important-ne les funcions amb l'arrel apuntant-hi.
Només fan servir Python (3.11 o posterior) i git: cap xarxa, cap render ni cap eina externa.

Bateries (els casos de cadascuna: --llista, i la taula de la guia):
  sigles        25_scripts/sigles.py --comprova
  lexic         25_scripts/gen_glossari.py --comprova
  prosa         lint_prosa.check()
  format_codi   verifica_format_codi.comprova_linia()
  callouts      verifica_callouts.revisa()
  calendari     25_scripts/verifica_calendari.py
  decisions     comprova.c_decisions() i comprova.c_exr_sol()
  classificacio comprova.autotest(), la classificació dels fitxers del repositori

Ús:
    python3 25_scripts/autoproves.py                  # totes; surt amb 1 si en falla algun cas
    python3 25_scripts/autoproves.py sigles prosa     # només aquestes bateries
    python3 25_scripts/autoproves.py --llista         # els casos de cada bateria
    python3 25_scripts/autoproves.py --taula          # escriu la taula de 13_contrib.qmd (make registres)
    python3 25_scripts/autoproves.py --taula --comprova   # 1 si la taula no és al dia

Les fa córrer comprova.py (la comprovació «Autoproves») quan canvia una de les eines provades o
aquest fitxer, i sempre amb `make comprova-tot`; `make autoproves` les passa totes. Un cas nou
s'afegeix al seu lloc de BATERIES, en el mateix commit que canvia la regla o l'eina, i
`make registres` en posa al dia la taula de la guia.
"""

import importlib
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
ESCRIPTS = ARREL / "25_scripts"
GUIA = ARREL / "13_contrib.qmd"
MARCA_INICI = "<!-- autoproves:inici — la genera 25_scripts/autoproves.py --taula; no l'editeu a mà -->"
MARCA_FI = "<!-- autoproves:fi -->"


@dataclass
class Cas:
    """Un cas: què prova, els canvis sobre la base de la bateria i l'esperat. `subst`, substitucions
    (fitxer, text d'ara, text nou), la primera ocurrència; `afegeix`, {fitxer: text}, al final del
    fitxer (o un fitxer nou); `espera`, els fragments que la sortida ha de contenir, o cap si la
    comprovació no hi ha de trobar res."""
    que: str
    subst: list = field(default_factory=list)
    afegeix: dict = field(default_factory=dict)
    espera: list = field(default_factory=list)


@dataclass
class Bateria:
    nom: str
    eina: str
    regla: str
    base: dict
    executa: object          # (directori) -> (neta, sortida)
    casos: list


# ---------------------------------------------------------------------------
# El llibre mínim
# ---------------------------------------------------------------------------
QUARTO = """book:
  chapters:
    - text: "Presentació"
      file: index.qmd
    - part: "Apunts"
      chapters:
        - text: "A1"
          file: 01_apunts/A1.qmd
"""


def munta(dir_, base, cas):
    fitxers = dict(base)
    for f, vell, nou in cas.subst:
        if vell not in fitxers[f]:
            raise ValueError(f"cas «{cas.que}»: «{vell}» no és a {f}")
        fitxers[f] = fitxers[f].replace(vell, nou, 1)
    for f, text in cas.afegeix.items():
        fitxers[f] = fitxers.get(f, "") + text
    for f, text in fitxers.items():
        p = dir_ / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")


def copia_escripts(dir_, *noms):
    (dir_ / "25_scripts").mkdir(exist_ok=True)
    for nom in noms:
        shutil.copy(ESCRIPTS / nom, dir_ / "25_scripts" / nom)


def procés(dir_, script, *args):
    r = subprocess.run([sys.executable, str(dir_ / "25_scripts" / script), *args], cwd=dir_,
                       capture_output=True, text=True)
    return r.returncode == 0, r.stdout + r.stderr


def amb_arrel(modul, dir_):
    """El mòdul de 25_scripts, importat, amb `ARREL` apuntant al llibre mínim."""
    m = importlib.import_module(modul)
    m.ARREL = dir_
    return m


# ---------------------------------------------------------------------------
# sigles: 25_scripts/sigles.py --comprova
# ---------------------------------------------------------------------------
TERMES_SIGLES = """[termes]
"stack frame" = { ca = "bloc d'activació", fonts = ["sintagma"] }

[sigles]
"SSD" = { ca = "unitat d'estat sòlid", en = "solid-state drive" }
"NaN" = { en = "not a number" }
"SO" = { ca = "sistema operatiu" }
"BA" = { ca = "bloc d'activació", en = "stack frame" }
"L1" = { ca = "memòria cau de primer nivell", excepcio = "Prova." }

[no_sigles]
"GNU" = { perque = "Prova." }
"ISO/IEC 9899:2024" = { perque = "Prova." }
"""
A1_SIGLES = """# A1 {#sec-a1}

Una **unitat d'estat sòlid** (*solid-state drive*, SSD) és ràpida. Les unitats d'estat sòlid (*solid-state drives*, SSD) no tenen parts mòbils.

El valor *not a number* (NaN) és especial, i el sistema operatiu (SO) el tracta.

Aquest espai s'anomena **bloc d'activació** (*stack frame*, BA). El GNU fa servir la SSD, el BA, la L1 i l'estàndard ISO/IEC 9899:2024, amb 32 KB, l'RV32IM i la porta AND.
"""
BASE_SIGLES = {"_quarto.yml": QUARTO, "index.qmd": "# Presentació {.unnumbered}\n\nAquest és el llibre.\n",
               "01_apunts/A1.qmd": A1_SIGLES, "24_specs/termes.toml": TERMES_SIGLES, "24_specs/taules_fusio.toml": ""}
A1 = "01_apunts/A1.qmd"
EXP_SSD = "(*solid-state drive*, SSD) és ràpida"


def executa_sigles(dir_):
    copia_escripts(dir_, "sigles.py", "gen_glossari.py", "taula_md.py")
    return procés(dir_, "sigles.py", "--comprova")


CASOS_SIGLES = [
    Cas("Text correcte: les tres variants del format, la negreta a la forma catalana, el plural, la presentació "
        "d'un terme a l'expansió (BA), una sigla amb `excepcio` (L1) i els mots que no són sigles (GNU i un text "
        "literal de `[no_sigles]`, KB, RV32IM, AND)"),
    Cas("La sigla, en negreta dins de l'expansió", subst=[(A1, EXP_SSD, "(*solid-state drive*, **SSD**) és ràpida")],
        espera=["SSD: l'expansió no segueix el format únic", "la sigla, en negreta dins del parèntesi"]),
    Cas("L'anglès, amb majúscules que `termes.toml` no té", subst=[(A1, EXP_SSD, "(*Solid-State Drive*, SSD) és ràpida")],
        espera=["SSD: l'expansió no segueix el format únic"]),
    Cas("L'anglès, en negreta i cursiva", subst=[(A1, EXP_SSD, "(***solid-state drive***, SSD) és ràpida")],
        espera=["SSD: l'expansió no segueix el format únic", "en negreta i cursiva"]),
    Cas("«(*anglès* o SIGLA)»", subst=[(A1, EXP_SSD, "(*solid-state drive* o SSD) és ràpida")],
        espera=["SSD: l'expansió no segueix el format únic"]),
    Cas("«SIGLA (*anglès*)», l'expansió darrere de la sigla",
        subst=[(A1, "El valor *not a number* (NaN)", "El valor **NaN** (*not a number*)")],
        espera=["NaN: l'expansió no segueix el format únic", "NaN: la primera aparició del llibre no s'expandeix"]),
    Cas("La forma catalana sense l'anglès, en una sigla que en té", subst=[(A1, EXP_SSD, "(SSD) és ràpida")],
        espera=["SSD: l'expansió no segueix el format únic"]),
    Cas("El parèntesi dins de la negreta", subst=[(A1, "el sistema operatiu (SO)", "el **sistema operatiu (SO)**")],
        espera=["SO: l'expansió no segueix el format únic"]),
    Cas("La primera aparició, sense expansió", subst=[(A1, "Una **unitat", "La SSD és nova.\n\nUna **unitat")],
        espera=["SSD: la primera aparició del llibre no s'expandeix"]),
    Cas("La primera aparició, a la Presentació, que es llegeix abans que els apunts",
        afegeix={"index.qmd": "\nLa SSD és nova.\n"}, espera=["index.qmd:", "SSD: la primera aparició"]),
    Cas("La primera aparició, en un aprofundiment, que no compta",
        subst=[(A1, "Una **unitat", "::: {.callout-warning}\n## Més\nLa SSD és nova.\n:::\n\nUna **unitat")]),
    Cas("La primera aparició, en un títol, i l'expansió al paràgraf següent",
        subst=[(A1, "Una **unitat", "## La SSD {#sec-ssd}\n\nUna **unitat")]),
    Cas("La primera aparició, en un títol, i el paràgraf següent sense expansió",
        subst=[(A1, "Una **unitat", "## La SSD {#sec-ssd}\n\nUn paràgraf sense la sigla.\n\nUna **unitat")],
        espera=["SSD: la primera aparició del llibre no s'expandeix", "ni al paràgraf següent"]),
    Cas("La primera aparició, en una fórmula, i l'expansió al paràgraf següent",
        subst=[(A1, "Una **unitat", "$$t = 1\\ \\text{SSD}$$\n\nUna **unitat")]),
    Cas("Una sigla dins d'una cursiva (una expansió anglesa) no és una aparició",
        subst=[(A1, "Una **unitat", "L'empresa *Advanced SSD Machines* les fabrica.\n\nUna **unitat")]),
    Cas("Una sigla en plural (D-79)", afegeix={A1: "\nHi ha dues SSDs.\n"}, espera=["«SSDs»: les sigles no porten plural"]),
    Cas("Una sigla del text que no és a la taula ni a `[no_sigles]`", afegeix={A1: "\nLa XYZ és nova.\n"},
        espera=["«XYZ»: no és a [sigles]"]),
    Cas("Una sigla de la taula sense cap aparició fora dels aprofundiments",
        afegeix={"24_specs/termes.toml": '\n[sigles.MP]\nca = "memòria principal"\n',
                 A1: "\n::: {.callout-warning}\n## Més\nLa memòria principal (MP).\n:::\n"},
        espera=["MP: cap aparició al text fora dels aprofundiments"]),
    Cas("L'expansió anglesa d'un terme de `[termes]`, amb una forma catalana diferent de la del terme",
        subst=[("24_specs/termes.toml", "\"BA\" = { ca = \"bloc d'activació\"", "\"BA\" = { ca = \"marc de pila\"")],
        espera=["BA: l'expansió anglesa és el terme *stack frame*"]),
    Cas("Una variant del format en una sigla que no és a la taula, dins d'un aprofundiment",
        afegeix={A1: "\n::: {.callout-warning}\n## Més\nUn **ZQ** (*zeta quux*).\n:::\n"},
        espera=["una variant del format únic de l'expansió («**SIGLA** (*anglès*)»)"]),
]


# ---------------------------------------------------------------------------
# lexic: 25_scripts/gen_glossari.py --comprova
# ---------------------------------------------------------------------------
TERMES_LEXIC = """[termes]
"cache" = { ca = "memòria cau", fonts = ["Termcat"] }
"stack frame" = { ca = "bloc d'activació", fonts = ["sintagma"] }

[en_angles]
"heap" = { ca = "—", motiu = "Prova." }

[no_presentacions]
"Registers" = { perque = "Prova." }

[sigles]
"BA" = { ca = "bloc d'activació", en = "stack frame" }
"NaN" = { en = "not a number" }
"""
A1_LEXIC = """# A1 {#sec-a1}

La **memòria cau** (*cache*) és ràpida. Aquest espai s'anomena **bloc d'activació** (*stack frame*, BA).

El panell **Registres** (*Registers*) els mostra, un **valor especial** (*not a number*, NaN) no és un terme, i el *heap* creix.
"""
BASE_LEXIC = {"_quarto.yml": QUARTO, "index.qmd": "# Presentació {.unnumbered}\n", "01_apunts/A1.qmd": A1_LEXIC,
              "24_specs/termes.toml": TERMES_LEXIC, "24_specs/taules_fusio.toml": ""}


def executa_lexic(dir_):
    copia_escripts(dir_, "gen_glossari.py", "taula_md.py")
    return procés(dir_, "gen_glossari.py", "--comprova")


CASOS_LEXIC = [
    Cas("Text correcte: una presentació, la d'un terme a l'expansió d'una sigla (*stack frame*, BA), una glossa de "
        "`[no_presentacions]` i l'expansió d'una sigla que no és un terme (NaN)"),
    Cas("Una forma catalana que no és la de `termes.toml`",
        subst=[(A1, "**memòria cau** (*cache*)", "**memòria oculta** (*cache*)")], espera=["termes.toml diu «memòria cau»"]),
    Cas("El plural regular (cada mot fins a la primera preposició) és una presentació del mateix terme",
        afegeix={A1: "\nEls **blocs d'activació** (*stack frames*) s'apilen.\n"}),
    Cas("Un plural que no és el regular («memòries cau», no «memòries caus») demana `presentacio`",
        subst=[(A1, "La **memòria cau** (*cache*) és ràpida", "Les **memòries cau** (*caches*) són ràpides")],
        espera=["termes.toml diu «memòria cau»"]),
    Cas("Un terme presentat que no és a `termes.toml`", afegeix={A1: "\nUn **fil** (*thread*) s'executa.\n"},
        espera=["*thread* no és a termes.toml"]),
    Cas("Un terme de `termes.toml` sense cap presentació",
        afegeix={"24_specs/termes.toml": '\n[termes.bus]\nca = "bus"\nfonts = ["DIEC"]\n'},
        espera=["«bus» no té cap presentació"]),
    Cas("Un terme que el llibre manté en anglès, presentat en català", afegeix={A1: "\nEl **monticle** (*heap*) creix.\n"},
        espera=["el llibre manté *heap* en anglès"]),
    Cas("Una presentació dins d'un bloc de codi no compta",
        subst=[(A1, "Aquest espai s'anomena **bloc d'activació** (*stack frame*, BA).",
                "\n\n```\n**bloc d'activació** (*stack frame*)\n```\n")],
        espera=["«stack frame» no té cap presentació"]),
    Cas("Un terme sense `fonts`", subst=[("24_specs/termes.toml", ', fonts = ["Termcat"]', "")],
        espera=["«cache» no té `fonts`"]),
]


# ---------------------------------------------------------------------------
# prosa: lint_prosa.check()
# ---------------------------------------------------------------------------
TERMES_PROSA = """[termes]
"array" = { ca = "vector", fonts = ["DIEC"] }

[en_angles]
"heap" = { ca = "—", motiu = "Prova." }

[no_admeses]
"tamany" = { si = "mida" }

[angles_en_pla]
"Array Toolkit" = { perque = "Prova." }
"""
TAULA = "| Concepte | Valor |\n| :--- | :--- |\n"


def executa_prosa(dir_):
    lp = importlib.import_module("lint_prosa")
    formes, angles = lp.formes_no_admeses(dir_), lp.termes_anglesos(dir_)
    trobat = lp.check(dir_ / "prova.qmd", None, formes, angles)
    return not trobat, "\n".join(t for _, _, t in trobat)


def prosa(que, text, espera=()):
    return Cas(que, afegeix={"prova.qmd": text}, espera=list(espera))


CASOS_PROSA = [
    prosa("Prosa correcta: el terme català, la glossa en cursiva, el codi i un text de `[angles_en_pla]`",
          "La mida del vector (*array*), la variable `array` i l'eina Array Toolkit.\n"),
    prosa("Una forma que no s'ha de fer servir, a la prosa", "El tamany del vector.\n", ["forma no admesa: «tamany»"]),
    prosa("Una forma que no s'ha de fer servir, a una cel·la", TAULA + "| tamany | 4 |\n", ["forma no admesa: «tamany»"]),
    prosa("Un terme de `[termes]` en pla, a la prosa", "Un array de dades.\n", ["«array»: terme anglès en pla"]),
    prosa("Un terme de `[termes]` en pla i en plural", "Dos arrays.\n", ["«arrays»: terme anglès en pla"]),
    prosa("Un terme de `[termes]` en pla, a una cel·la", TAULA + "| array local | 4 |\n", ["«array»: terme anglès en pla"]),
    prosa("Un terme de `[en_angles]` sense cursiva", "El heap creix.\n", ["terme anglès sense cursiva: *heap*"]),
    prosa("Un doble espai, a la prosa", "Dos  espais.\n", ["doble espai"]),
    prosa("Un doble espai, a una cel·la, que és permès", TAULA + "| dos  espais | 4 |\n"),
    prosa("Unes cometes rectes", 'Unes "cometes".\n', ["cometa recta"]),
    prosa("Dins d'un bloc de codi, res", "```\narray tamany  \"x\"\n```\n"),
]


# ---------------------------------------------------------------------------
# format_codi: verifica_format_codi.comprova_linia()
# ---------------------------------------------------------------------------
def executa_codi(dir_):
    v = importlib.import_module("verifica_format_codi")
    linia = (dir_ / "linia.txt").read_text(encoding="utf-8")
    regles = v.comprova_linia(linia)
    return not regles, ",".join(regles)


def codi(que, linia, regles=()):
    return Cas(que, afegeix={"linia.txt": linia}, espera=list(regles))


CASOS_CODI = [
    codi("Una instrucció ben sagnada i alineada", "        addi    t0, t0, 1"),
    codi("Una etiqueta amb una instrucció, a la columna 8", "bucle:  addi    t0, t0, 1"),
    codi("Directives de segment i de visibilitat, a la columna 0", ".globl  main"),
    codi("F1: una directiva de segment sagnada", "    .text", ["F1"]),
    codi("F2: una etiqueta sagnada", "  bucle:", ["F2"]),
    codi("F3: un sagnat que no és de 8 espais", "    addi    t0, t0, 1", ["F3"]),
    codi("F4: un tabulador (i, per tant, el sagnat)", "\taddi    t0, t0, 1", ["F4", "F3"]),
    codi("F5: els operands, fora de la columna 16", "        addi t0, t0, 1", ["F5"]),
    codi("F6: una etiqueta `b`", "b:", ["F6"]),
    codi("F6: una constant `B`", ".eqv    B, 4", ["F6"]),
]


# ---------------------------------------------------------------------------
# callouts: verifica_callouts.revisa()
# ---------------------------------------------------------------------------
def executa_callouts(dir_):
    v = amb_arrel("verifica_callouts", dir_)
    trobat = v.revisa("prova.qmd")
    return not trobat, "\n".join(trobat)


CASOS_CALLOUTS = [
    Cas("Un div que no és un callout, dins d'un callout",
        afegeix={"prova.qmd": "::: {.callout-note}\n::: {.content-visible when-format=\"html\"}\nx\n:::\n:::\n"}),
    Cas("Un callout dins d'un altre (D-110)",
        afegeix={"prova.qmd": "::: {.callout-note}\n::: {.callout-tip}\nx\n:::\n:::\n"},
        espera=["callout dins del callout de la línia 1"]),
    Cas("Un include, dins d'un callout, d'un fragment que porta un callout",
        afegeix={"prova.qmd": "::: {.callout-note}\n{{< include frag.qmd >}}\n:::\n",
                 "frag.qmd": "::: {.callout-tip}\nx\n:::\n"},
        espera=["l'include de frag.qmd porta un callout"]),
    Cas("Un callout dins d'un bloc de codi no compta",
        afegeix={"prova.qmd": "::: {.callout-note}\n```\n::: {.callout-tip}\n```\n:::\n"}),
]


# ---------------------------------------------------------------------------
# calendari: 25_scripts/verifica_calendari.py
# ---------------------------------------------------------------------------
QUARTO_LAB = """book:
  chapters:
    - part: "Laboratori"
      chapters:
        - text: "L1"
          file: 04_laboratori/L1.qmd
        - text: "L2"
          file: 04_laboratori/L2.qmd
"""
CAL = "04_laboratori/Lcalendari.qmd"
CALENDARI = """# Calendari {.unnumbered}

**Quadrimestre primavera 2025-26**

| Subgrups | Dia | [L1](#sec-sessio-u) | [L2](#sec-sessio-dos) |
| :--- | :--- | :---: | :---: |
| 11, 12 | Dimarts | 17/02 | 03/03 |
| 21 | Dijous | 19/02 | 05/03 |
: {tbl-colwidths="[40,20,20,20]"}
"""
BASE_CALENDARI = {"_quarto.yml": QUARTO_LAB, CAL: CALENDARI,
                  "04_laboratori/L1.qmd": "# L1\n\n## Sessió {#sec-sessio-u}\n",
                  "04_laboratori/L2.qmd": "# L2\n\n## Sessió {#sec-sessio-dos}\n"}


def executa_calendari(dir_):
    copia_escripts(dir_, "verifica_calendari.py")
    return procés(dir_, "verifica_calendari.py")


CASOS_CALENDARI = [
    Cas("Un calendari correcte: les dates, al dia de la fila, creixents, i les columnes, les sessions del laboratori"),
    Cas("Una data que no cau en el dia de la fila", subst=[(CAL, "| Dimarts | 17/02 |", "| Dimarts | 18/02 |")],
        espera=["18/02/2026 és dimecres, no dimarts"]),
    Cas("Dues dates d'una fila que no són creixents",
        subst=[(CAL, "| Dimarts | 17/02 | 03/03 |", "| Dimarts | 03/03 | 17/02 |")], espera=["no és posterior"]),
    Cas("Un canvi de dia (D-74) ben marcat, amb la seva nota «†»",
        subst=[(CAL, "| Dimarts | 17/02 |", "| Dimarts | [18/02 †]{.canvi-dia} |")],
        afegeix={CAL: "\n[†]{.canvi-dia} El 18/02 és dimecres.\n"}),
    Cas("Un canvi de dia marcat sense la nota «†»",
        subst=[(CAL, "| Dimarts | 17/02 |", "| Dimarts | [18/02 †]{.canvi-dia} |")], espera=["cap nota"]),
    Cas("Un canvi de dia marcat en una data que és del dia de la fila",
        subst=[(CAL, "| Dimarts | 17/02 |", "| Dimarts | [17/02 †]{.canvi-dia} |")],
        espera=["és marcat com a canvi de dia"]),
    Cas("Unes columnes de sessió que no són les seccions del laboratori",
        subst=[(CAL, "[L2](#sec-sessio-dos)", "[L2](#sec-sessio-tres)")], espera=["columnes de sessió"]),
    Cas("Sense la línia del quadrimestre", subst=[(CAL, "**Quadrimestre primavera 2025-26**", "")],
        espera=["No hi ha la línia"]),
]


# ---------------------------------------------------------------------------
# decisions: comprova.c_decisions() i comprova.c_exr_sol()
# ---------------------------------------------------------------------------
def executa_decisions(dir_):
    # Un hook de git (el pre-commit de .githooks/) hi posa GIT_DIR, GIT_INDEX_FILE…: amb aquestes
    # variables, el git del llibre mínim seria el del repositori del llibre, i el `git init`, el seu.
    vells = {k: os.environ.pop(k) for k in list(os.environ) if k.startswith("GIT_")}
    c = importlib.import_module("comprova")
    vella = c.ARREL
    c.ARREL = dir_
    try:
        subprocess.run(["git", "init", "-q"], cwd=dir_, check=True)
        trobat = c.c_decisions(None) + c.c_exr_sol(None)
    finally:
        c.ARREL = vella
        os.environ.update(vells)
    return not trobat, "\n".join(m for _, m in trobat)


BASE_DECISIONS = {"24_specs/registre_de_decisions.md": "# Registre\n\n### D-1\n\nUna decisió.\n",
                  "A1.qmd": "Segons la regla (D-1).\n", "P1.qmd": "::: {#exr-t1-a}\n:::\n", "S1.qmd": "::: {#sol-t1-a}\n:::\n"}
CASOS_DECISIONS = [
    Cas("Cada decisió citada és al registre, i cada solució té el seu enunciat"),
    Cas("Una decisió citada que no és al registre", afegeix={"A1.qmd": "I l'altra (D-7).\n"},
        espera=["D-7, citat a A1.qmd"]),
    Cas("Una solució sense el seu enunciat (D-22)", afegeix={"S1.qmd": "::: {#sol-t1-b}\n:::\n"},
        espera=["#sol-t1-b no té el seu #exr-t1-b"]),
]


# ---------------------------------------------------------------------------
# classificacio: comprova.autotest()
# ---------------------------------------------------------------------------
def executa_classificacio(dir_):
    errors = importlib.import_module("comprova").autotest()
    return not errors, "\n".join(errors)


# ---------------------------------------------------------------------------
# llistats: verifica_llistats.revisa() i verifica_llistats.sortida() (D-117, D-121)
# ---------------------------------------------------------------------------
A1_LLISTATS = """# A1 {#sec-a1}

El @lst-suma suma dos registres.

::: {#lst-suma}
```{.s filename="RV32I"}
        add     t0, t1, t2
```
Suma de dos registres.
:::

Un bloc sense remissió, que no és un llistat:

```{.s filename="RV32I"}
        nop
```
"""
A1 = "01_apunts/A1.qmd"
BLOC = '\n```{.s filename="RV32I"}\n        sub     t0, t1, t2\n```\n'


def executa_llistats(dir_):
    v = amb_arrel("verifica_llistats", dir_)
    trobat = [str(t) for t in v.revisa(dir_)]
    return not trobat, "\n".join(trobat)


CASOS_LLISTATS = [
    Cas("Un llistat en forma de div, amb el peu i la remissió, i un bloc que no és un llistat"),
    Cas("L1: la forma d'atribut (`lst-cap`), que dins d'un callout dona dos números al PDF",
        afegeix={A1: '\nEl @lst-attr.\n\n```{#lst-attr .s filename="RV32I" lst-cap="Peu."}\n        nop\n```\n'},
        espera=["L1 forma d'atribut"]),
    Cas("L2: un div `#lst-` sense bloc de codi", afegeix={A1: "\nEl @lst-buit.\n\n::: {#lst-buit}\nNomés text.\n:::\n"},
        espera=["L2 #lst-buit sense bloc de codi"]),
    Cas("L2: un div `#lst-` sense peu", subst=[(A1, "```\nSuma de dos registres.\n:::", "```\n:::")],
        espera=["L2 #lst-suma sense peu"]),
    Cas("L3: un peu que no acaba en punt", subst=[(A1, "Suma de dos registres.", "Suma de dos registres")],
        espera=["L3 el peu de #lst-suma"]),
    Cas("L4: un llistat dins d'un bloc `when-format`",
        afegeix={A1: '\nEl @lst-html.\n\n::: {.content-visible when-format="html"}\n::: {#lst-html}\n```\nx\n```\nPeu.\n:::\n:::\n'},
        espera=["L4 #lst-html dins d'un bloc when-format"]),
    Cas("L5: un llistat sense cap remissió", subst=[(A1, "El @lst-suma suma", "El codi suma")],
        espera=["L5 #lst-suma sense cap remissió"]),
    Cas("L6: una remissió a un llistat que no existeix", afegeix={A1: "\nVegeu el @lst-cap.\n"},
        espera=["L6 @lst-cap: no hi ha cap llistat"]),
    Cas("L7: «el codi següent», al paràgraf de davant d'un bloc", afegeix={A1: "\nEl codi següent resta:\n" + BLOC},
        espera=["L7 remissió per posició", "«codi següent»"]),
    Cas("L7: «la funció C anterior», al paràgraf de davant", afegeix={A1: "\nTradueix la funció C anterior:\n" + BLOC},
        espera=["«funció C anterior»"]),
    Cas("L7: «aquest programa», al paràgraf de darrere", afegeix={A1: BLOC + "\nCarregueu aquest programa a RARS.\n"},
        espera=["«aquest programa»"]),
    Cas("L7: «el codi següent», davant del div d'un llistat (el paràgraf de davant és el del div, no el del bloc)",
        afegeix={A1: '\nEl codi següent multiplica:\n\n::: {#lst-mul}\n```{.s filename="RV32I"}\n        mul     t0, t1, t2\n```\n'
                     'Producte.\n:::\n'},
        espera=["«codi següent»"]),
    Cas("L7: un mot de codi, «el `for` anterior»", afegeix={A1: "\nEn el `for` anterior, el punter avança:\n" + BLOC},
        espera=["«`for` anterior»"]),
    Cas("Un «següents» al paràgraf de darrere apunta al que ve després, no al bloc",
        afegeix={A1: BLOC + "\nTraduïu les sentències següents:\n\na) `x = 1;`\n"}),
    Cas("Una presentació adverbial no és una remissió (D-117)",
        afegeix={A1: "\nEs declara de la manera següent:\n" + BLOC + "\nI en C es declara així:\n" + BLOC}),
    Cas("Una remissió per posició dins d'un bloc de codi no compta",
        afegeix={A1: '\n```{.s filename="RV32I"}\n        nop             # el codi següent\n```\n'}),
]

HTML_LLISTATS = ('<div id="lst-suma" class="s listing quarto-float">\n<figure class="quarto-float">\n'
                 '<figcaption class="quarto-float-caption">\nCodi&nbsp;1.1: Suma de dos registres.\n</figcaption>\n')
BASE_LLISTATS_SORTIDA = {A1: A1_LLISTATS, "_book/01_apunts/A1.html": HTML_LLISTATS,
                         "Estructura-de-computadors.tex": "\\caption{\\label{lst-suma}\\protect\\ecfitxer{RV32I}Suma.}\n",
                         "pdf.txt": "Codi 1.1: Suma de dos registres.\nRV32I\n        add     t0, t1, t2\nRV32I\n"}


def executa_llistats_sortida(dir_):
    v = amb_arrel("verifica_llistats", dir_)
    trobat = v.sortida(dir_, text_pdf=(dir_ / "pdf.txt").read_text(encoding="utf-8"))
    return not trobat, "\n".join(trobat)


CASOS_LLISTATS_SORTIDA = [
    Cas("El llistat, amb la mateixa posició a l'HTML i al PDF, i cap bloc més numerat"),
    Cas("Una posició diferent a l'HTML i al PDF",
        subst=[("_book/01_apunts/A1.html", "Codi&nbsp;1.1", "Codi&nbsp;1.2")], espera=["la posició dins del capítol"]),
    Cas("El mateix número de posició amb un altre número de capítol, com P2 (11 a l'HTML, 2 al PDF), és bo",
        subst=[("_book/01_apunts/A1.html", "Codi&nbsp;1.1", "Codi&nbsp;11.1")]),
    Cas("Un llistat que no és a l'HTML", subst=[("_book/01_apunts/A1.html", 'id="lst-suma"', 'id="lst-altre"')],
        espera=["#lst-suma: no és a l'HTML"]),
    Cas("Un bloc numerat al PDF que no és un llistat (preamble.tex o llistats.lua espatllats)",
        afegeix={"pdf.txt": "Codi 1.2: RV32I\n"}, espera=["el PDF numera 1 blocs més"]),
]

BATERIES = [
    Bateria("sigles", "`sigles.py --comprova`", "§Sigles, símbols i notació (D-89, D-118)", BASE_SIGLES,
            executa_sigles, CASOS_SIGLES),
    Bateria("lexic", "`gen_glossari.py --comprova`", "§Anglicismes i terminologia obligatòria (D-115, D-116)",
            BASE_LEXIC, executa_lexic, CASOS_LEXIC),
    Bateria("prosa", "`lint_prosa.py`", "§Anglicismes, §Formes que no s'han de fer servir, §Commits (D-105, D-116)",
            {"24_specs/termes.toml": TERMES_PROSA}, executa_prosa, CASOS_PROSA),
    Bateria("format_codi", "`verifica_format_codi.py`", "§Estil de codi RISC-V (D-50, D-111)", {}, executa_codi, CASOS_CODI),
    Bateria("callouts", "`verifica_callouts.py`", "§Imbricacions (D-110)", {}, executa_callouts, CASOS_CALLOUTS),
    Bateria("calendari", "`verifica_calendari.py`", "§Convencions globals del laboratori (D-74)", BASE_CALENDARI,
            executa_calendari, CASOS_CALENDARI),
    Bateria("decisions", "`comprova.py` (decisions citades, enunciats i solucions)", "Registre de decisions; "
            "§Problemes i solucions (D-22)", BASE_DECISIONS, executa_decisions, CASOS_DECISIONS),
    Bateria("classificacio", "`comprova.py` (`autotest()`)", "§Comprovacions per nivells (D-103)", {},
            executa_classificacio, [Cas("Els fitxers d'exemple, a la classe i al nivell que els toca, i les taules de la "
                                        "guia, generades")]),
    Bateria("llistats", "`verifica_llistats.py`", "§Referències creuades (D-117, D-121)", {A1: A1_LLISTATS},
            executa_llistats, CASOS_LLISTATS),
    Bateria("llistats_sortida", "`verifica_llistats.py --sortida`", "§Referències creuades (D-117, D-121)",
            BASE_LLISTATS_SORTIDA, executa_llistats_sortida, CASOS_LLISTATS_SORTIDA),
]


# ---------------------------------------------------------------------------
# Execució
# ---------------------------------------------------------------------------
def passa(b, cas):
    """Una llista buida si el cas passa; si no, el que falla."""
    with tempfile.TemporaryDirectory(prefix=f"autoprova_{b.nom}_") as tmp:
        dir_ = Path(tmp)
        try:
            munta(dir_, b.base, cas)
            neta, sortida = b.executa(dir_)
        except Exception as e:                      # noqa: BLE001 — una eina que peta és un cas que falla
            return [f"l'execució ha fallat: {type(e).__name__}: {e}"]
    if b.nom == "format_codi":
        return [] if sortida == ",".join(cas.espera) else [f"esperava «{','.join(cas.espera)}» i ha trobat «{sortida}»"]
    if not cas.espera:
        return [] if neta else [f"no hi havia de trobar res, i ha trobat:\n{sortida.strip()}"]
    if neta:
        return ["no hi ha trobat res, i hi havia de trobar: " + "; ".join(cas.espera)]
    return [f"no hi ha trobat «{e}»; ha trobat:\n{sortida.strip()}" for e in cas.espera if e not in sortida]


def taula():
    files = ["| Bateria | Eina | Regla | Casos |", "| :--- | :--- | :--- | :--- |"]
    for b in BATERIES:
        casos = "; ".join(f"{c.que}{'' if c.espera else ' (cap troballa)'}" for c in b.casos)
        files.append(f"| `{b.nom}` | {b.eina} | {b.regla} | {len(b.casos)}: {casos} |".replace("\n", " "))
    return "\n".join(files)


def escriu_taula(comprova):
    text = GUIA.read_text(encoding="utf-8")
    if MARCA_INICI not in text or MARCA_FI not in text:
        print("[autoproves] no trobo les marques de la taula a 13_contrib.qmd", file=sys.stderr)
        return 1
    abans, resta = text.split(MARCA_INICI, 1)
    nou = abans + MARCA_INICI + "\n" + taula() + "\n" + MARCA_FI + resta.split(MARCA_FI, 1)[1]
    if comprova:
        if nou != text:
            print("[autoproves] la taula de 13_contrib.qmd §Autoproves no és al dia (make registres)", file=sys.stderr)
            return 1
        return 0
    if nou != text:
        GUIA.write_text(nou, encoding="utf-8")
    print("[autoproves] taula de 13_contrib.qmd §Autoproves de les comprovacions al dia")
    return 0


def main(args):
    sys.path.insert(0, str(ESCRIPTS))
    if "--taula" in args:
        return escriu_taula("--comprova" in args)
    noms = {b.nom for b in BATERIES}
    triades = [a for a in args if not a.startswith("--")]
    if set(triades) - noms or set(args) - noms - {"--llista"}:
        print(__doc__.split("Ús:")[1].split("Les fa córrer")[0].rstrip(), file=sys.stderr)
        return 2
    bateries = [b for b in BATERIES if not triades or b.nom in triades]
    if "--llista" in args:
        for b in bateries:
            print(f"{b.nom} ({b.eina}; {b.regla})")
            for c in b.casos:
                print(f"  - {c.que}: {', '.join(c.espera) if c.espera else 'cap troballa'}")
        return 0
    errors, n = [], 0
    for b in bateries:
        for cas in b.casos:
            n += 1
            for e in passa(b, cas):
                errors.append(f"{b.nom}: «{cas.que}»: {e}")
    for e in errors:
        print(f"[autoproves] {e}", file=sys.stderr)
    if errors:
        print(f"[autoproves] {len(errors)} errors en {n} casos (13_contrib.qmd §Autoproves de les comprovacions)",
              file=sys.stderr)
        return 1
    print(f"[autoproves] {n} casos de {len(bateries)} bateries, tots bé")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
