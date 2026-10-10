#!/usr/bin/env python3
"""Comprovacions per nivells: el nivell es dedueix dels fitxers canviats.

Les regles són a 13_contrib.qmd §Comprovacions per nivells, i el perquè, a D-103 i
D-104 del registre de decisions. Les dues taules d'aquella secció (els nivells i
les comprovacions) les escriu aquest script (--taula) a partir de CLASSES i de
COMPROVACIONS, de manera que no poden divergir del que fa. CLASSES és l'única
classificació dels fitxers del projecte: també la fan servir orfes.py i
escombrada.sh (--llista).

Ús:
    python3 25_scripts/comprova.py                     # els canvis respecte d'HEAD (make comprova; el hook de Claude Code)
    python3 25_scripts/comprova.py --base origin/main  # la branca sencera (make comprova-branca; el pre-push de git)
    python3 25_scripts/comprova.py --tot               # totes, sobre el corpus sencer (make comprova-tot)
    python3 25_scripts/comprova.py --sense-render      # sense el render (el pre-commit de git)
    python3 25_scripts/comprova.py --explica           # el nivell i el que faria, sense executar res
    python3 25_scripts/comprova.py --taula             # reescriu les dues taules de la guia (make registres)
    python3 25_scripts/comprova.py --autotest          # la classificació, contra casos coneguts
    python3 25_scripts/comprova.py --llista ETIQUETA   # els fitxers o directoris d'una etiqueta de CLASSES
    python3 25_scripts/comprova.py --historial N [--des-de REF]   # el nivell dels N commits d'abans
    -v                                                 # també les comprovacions netes, amb el temps

Surt amb 2 si alguna comprovació atura el commit, amb 1 si hi ha res a llegir
(avisos, recordatoris o comprovacions omeses per falta d'una dependència) i amb
0 si no hi ha res a dir. Només fa servir la biblioteca estàndard (Python ≥ 3.11).
"""

import argparse
import fnmatch
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
GUIA = ARREL / '13_contrib.qmd'
PY = sys.executable or 'python3'

# ---------------------------------------------------------------------------
# Classificació dels fitxers: (patró, classe, etiquetes). Mana el primer patró
# que coincideix (fnmatch: `*` també travessa `/`).
#
# Classes (el nivell que en surt és a NIVELLS):
#   operatiu      el render no el llegeix
#   eina          una eina de comprovació, o un generador amb la sortida
#                 versionada (que té el seu --comprova): el render tampoc no la llegeix
#   contingut     text del llibre, que el render llegeix
#   figura        una figura o el que la genera al pre-render
#   configuracio  la configuració del render (HTML i PDF)
# Etiquetes:
#   documenta     hi consten casos (tasques, regles, perquès, lliçons): les
#                 escombrades no hi compten les ocurrències (regla 12), i la prosa
#                 hi pot citar les formes que no s'han de fer servir
#   no_cita       cita fitxers pel nom sense fer-los servir: orfes.py no hi compta les cites
#   fora_orfes    no és mai orfe: la configuració de les eines i els originals conservats (D-98, D-68)
#   html          només surt a l'HTML: l'avís de PDF no hi pertoca
# ---------------------------------------------------------------------------
CLASSES = [
    ('TODO.md', 'operatiu', {'documenta', 'no_cita'}),
    ('24_specs/arxiu_todo.md', 'operatiu', {'documenta', 'no_cita'}),
    ('24_specs/registre_de_decisions.md', 'operatiu', {'documenta', 'no_cita'}),
    ('README.md', 'operatiu', {'no_cita'}),
    ('CLAUDE.md', 'operatiu', set()),
    ('.claude/*', 'operatiu', {'documenta', 'fora_orfes'}),
    ('.github/*', 'operatiu', {'fora_orfes'}),
    ('.githooks/*', 'operatiu', {'fora_orfes'}),
    ('.vscode/*', 'operatiu', {'fora_orfes'}),
    ('.gitignore', 'operatiu', set()),
    ('05_diapositives/*', 'operatiu', set()),
    ('22_figs_originals/conservats/*', 'operatiu', {'fora_orfes'}),
    ('24_specs/glossari.toml', 'operatiu', set()),
    ('24_specs/diccionari.txt', 'operatiu', set()),
    ('24_specs/gramatica.toml', 'operatiu', set()),
    ('25_scripts/comprova.py', 'eina', set()),
    ('25_scripts/escombrada.sh', 'eina', set()),
    ('25_scripts/lint_prosa.py', 'eina', set()),
    ('25_scripts/ortografia.py', 'eina', set()),
    ('25_scripts/gramatica.py', 'eina', set()),
    ('25_scripts/eines_externes.py', 'eina', set()),
    ('25_scripts/orfes.py', 'eina', set()),
    ('25_scripts/inventari_figures.py', 'eina', set()),
    ('25_scripts/verifica_*.py', 'eina', set()),
    ('25_scripts/gen_glossari.py', 'eina', set()),
    ('25_scripts/gen_T4_sumador.py', 'eina', set()),
    ('25_scripts/gen_T7.py', 'eina', set()),
    ('25_scripts/gen_T8.py', 'eina', set()),
    ('13_contrib.qmd', 'contingut', {'documenta', 'html'}),
    ('10_continguts.qmd', 'contingut', {'html'}),
    ('*.qmd', 'contingut', set()),
    ('LICENSE.md', 'contingut', set()),
    ('15_bibliografia.bib', 'contingut', set()),
    ('_variables.yml', 'contingut', set()),
    ('22_figs_originals/*', 'figura', set()),
    ('23_figs_externes/*', 'figura', set()),
    ('24_specs/svg.md', 'figura', set()),
    ('24_specs/*.gv', 'figura', set()),
    ('24_specs/registres.toml', 'figura', set()),
    ('24_specs/BA.toml', 'figura', set()),
    ('24_specs/mapa.toml', 'figura', set()),
    ('24_specs/subrutines.toml', 'figura', set()),
    ('24_specs/MC.toml', 'figura', set()),
    ('24_specs/memoria.toml', 'figura', set()),
    ('24_specs/retalls.toml', 'figura', set()),
    ('25_scripts/figlib.py', 'figura', set()),
    ('25_scripts/columna_memoria.py', 'figura', set()),
    ('25_scripts/norm_font.py', 'figura', set()),
    ('25_scripts/gen_*.py', 'figura', set()),          # els del pre-render (els de model (a), a dalt)
    ('_quarto.yml', 'configuracio', set()),
    ('preamble.tex', 'configuracio', set()),
    ('*.scss', 'configuracio', set()),
    ('styles.css', 'configuracio', set()),
    ('figures_dinamiques.html', 'configuracio', set()),
    ('formules_en_linia.html', 'configuracio', set()),
    ('ieee.csl', 'configuracio', set()),
    ('25_scripts/*.lua', 'configuracio', set()),
    ('24_specs/riscv.xml', 'configuracio', set()),
    ('24_specs/taules_fusio.toml', 'configuracio', set()),
    ('Makefile', 'configuracio', set()),
]
# gen_taules_auto.py és un gen_*.py, però és configuració: va abans del patró general.
CLASSES.insert(CLASSES.index(('25_scripts/gen_*.py', 'figura', set())),
               ('25_scripts/gen_taules_auto.py', 'configuracio', set()))

NIVELL_CLASSE = {'operatiu': 0, 'eina': 0, 'contingut': 2, 'figura': 3, 'configuracio': 4}
NIVELLS = {
    0: ('Operatiu', 'Uns segons'),
    1: ('Menor', 'Uns segons'),
    2: ('Contingut', '1–3 min'),
    3: ('Figures', '4–8 min'),
    4: ('Configuració', '4–8 min'),
}
TEMPS_TOT = '5–10 min'

# Una línia canviada d'un .qmd amb marcatge fa que el canvi sigui de nivell 2 i no
# d'1: el marcatge és el que pot trencar el render. Una línia buida, també (separa blocs).
MARCATGE = re.compile(r'[@{}$|\\<]|!\[|^\s*(?::::|---|#|```|~~~|\[\^)|^\s*$')
# Formes de les línies canviades que fan que un canvi de nivell 2 pugui afectar el PDF.
FORMES_PDF = ['when-format', 'tbl-colwidths', '#fig-', '![', '$']
ANSI = re.compile(r'\x1b\[[0-9;]*m')


def git(*args, check=True):
    return subprocess.run(['git', *args], cwd=ARREL, capture_output=True, text=True,
                          check=check).stdout


def classifica(f):
    """(classe, etiquetes) d'un fitxer, o (None, set()) si cap patró no hi coincideix."""
    for patro, classe, etiquetes in CLASSES:
        if fnmatch.fnmatchcase(f, patro):
            return classe, etiquetes
    return None, set()


def llista(etiquetes):
    """Els patrons de CLASSES amb alguna de les etiquetes, com a rutes («.claude/», no «.claude/*»)."""
    return [p[:-1] if p.endswith('/*') else p for p, _, e in CLASSES if e & set(etiquetes)]


def versionats():
    """Els fitxers versionats, més els nous que git no ignora (encara no afegits)."""
    return [f for f in git('ls-files', '--cached', '--others', '--exclude-standard').split('\n')
            if f and (ARREL / f).exists()]


# ---------------------------------------------------------------------------
# Els canvis i el nivell
# ---------------------------------------------------------------------------
class Canvis:
    """Els fitxers canviats respecte d'una referència (HEAD o el merge-base d'una branca),
    més els nous no versionats, i les línies canviades de cadascun."""

    def __init__(self, base=None, tot=False):
        self.tot = tot
        self.ref = 'HEAD' if base is None else git('merge-base', base, 'HEAD').strip()
        noms = git('diff', self.ref, '--name-only', '--no-renames').split('\n')
        self.nous = {f for f in git('ls-files', '--others', '--exclude-standard').split('\n') if f}
        self.fitxers = sorted({f for f in noms if f} | self.nous)
        self._diff = {}

    def diff(self, f):
        """(afegides, canviades): els números de les línies afegides i el text de les afegides i
        les tretes. Un fitxer nou: totes les seves línies."""
        if f not in self._diff:
            if f in self.nous:
                text = (ARREL / f).read_text(encoding='utf-8', errors='replace').split('\n')
                self._diff[f] = (set(range(1, len(text) + 1)), text)
            else:
                afegides, canviades, n = set(), [], None
                for fila in git('diff', self.ref, '-U0', '--no-color', '--', f).split('\n'):
                    m = re.match(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@', fila)
                    if m:
                        n = int(m.group(1))
                    elif n is None:
                        continue            # la capçalera del diff («--- a/…», «+++ b/…»)
                    elif fila.startswith('+'):
                        afegides.add(n)
                        canviades.append(fila[1:])
                        n += 1
                    elif fila.startswith('-'):
                        canviades.append(fila[1:])
                self._diff[f] = (afegides, canviades)
        return self._diff[f]

    def qmd(self):
        """Els .qmd canviats que encara existeixen."""
        return [f for f in self.fitxers if f.endswith('.qmd') and (ARREL / f).exists()]

    def nivell_fitxer(self, f):
        classe, _ = classifica(f)
        if classe is None:
            return 2, 'sense classe a comprova.py'
        n = NIVELL_CLASSE[classe]
        if classe == 'contingut' and f.endswith('.qmd') and f not in self.nous and (ARREL / f).exists():
            marcatge = [l for l in self.diff(f)[1] if MARCATGE.search(l)]
            return (2, 'línies amb marcatge') if marcatge else (1, 'només prosa')
        return n, classe

    def nivell(self):
        if self.tot:
            return 4, []
        nivells = [(self.nivell_fitxer(f)[0], f) for f in self.fitxers]
        if not nivells:
            return 0, []
        n = max(x for x, _ in nivells)
        return n, [f for x, f in nivells if x == n]


# ---------------------------------------------------------------------------
# Resultats
# ---------------------------------------------------------------------------
ERROR, AVIS, INFO, OMESA, OK = 'error', 'avis', 'info', 'omesa', 'ok'
SIGNE = {ERROR: '✗', AVIS: '⚠', INFO: 'ℹ', OMESA: '–', OK: '✓'}


class Omesa(Exception):
    """La comprovació no es pot fer: falta una dependència."""


def executa(*ordre, timeout=900):
    p = subprocess.run([str(x) for x in ordre], cwd=ARREL, capture_output=True, text=True,
                       timeout=timeout)
    return p.returncode, ANSI.sub('', p.stdout + p.stderr).strip()


def retalla(text, n=40):
    linies = text.split('\n')
    return '\n'.join(linies[:n] + ([f'… ({len(linies) - n} línies més)'] if len(linies) > n else []))


# ---------------------------------------------------------------------------
# Les comprovacions. Cadascuna rep el context i retorna una llista de
# (gravetat, missatge); una llista buida vol dir neta.
# ---------------------------------------------------------------------------
def c_registres(ctx):
    r = []
    for ordre, nom in [((PY, '25_scripts/gen_glossari.py', '--comprova'), 'el glossari de termes (make glossari)'),
                       ((PY, '25_scripts/gen_T4_sumador.py', '--comprova'), 'les figures de gen_T4_sumador.py'),
                       ((PY, '25_scripts/gen_T7.py', '--comprova'), 'les figures de gen_T7.py'),
                       ((PY, '25_scripts/gen_T8.py', '--comprova'), 'les figures de gen_T8.py')]:
        rc, sortida = executa(*ordre)
        if rc:
            r.append((ERROR, f'{nom} no és al dia (make registres):\n{retalla(sortida, 15)}'))
    for marca in TAULES_GUIA:
        if bloc_guia(marca) != taula_guia(marca):
            r.append((ERROR, f'la taula «{marca}» de 13_contrib.qmd no és al dia (make registres)'))
    r += recompte_todo()
    r += arbre_readme()
    return r


def recompte_todo():
    text = (ARREL / 'TODO.md').read_text(encoding='utf-8')
    vives = len(re.findall(r'^- ', text, re.M))
    per_seccio, seccio = {}, None
    for l in text.split('\n'):
        if l.startswith('## '):
            seccio = l[3:].strip()
        elif l.startswith('- ') and seccio:
            per_seccio[seccio] = per_seccio.get(seccio, 0) + 1
    r = []
    m = re.search(r'\*\*(\d+) entrades vives\*\*', text)
    if not m or int(m.group(1)) != vives:
        r.append((ERROR, f'TODO.md diu {m.group(1) if m else "?"} entrades vives i en té {vives} '
                         f'(grep -cE \'^- \' TODO.md): cal actualitzar-ne la capçalera'))
    rep = re.search(r'^Repartiment: (.*)$', text, re.M)
    if rep:
        escrit = {s: int(n) for s, n in re.findall(r'`§([^`]+)` (\d+)', rep.group(1))}
        suma = re.search(r'\(suma (\d+)', rep.group(1))
        if escrit != {s: n for s, n in per_seccio.items() if n}:
            r.append((ERROR, f'el repartiment de la capçalera del TODO.md no coincideix amb les seccions: '
                             f'{per_seccio}'))
        if suma and int(suma.group(1)) != vives:
            r.append((ERROR, f'la suma del repartiment del TODO.md ({suma.group(1)}) no és {vives}'))
    return r


def arbre_readme():
    """L'arbre del README.md té una entrada per a cada fitxer i directori versionat de l'arrel, i
    cap més que les generades (marcades «Generat»)."""
    text = (ARREL / 'README.md').read_text(encoding='utf-8')
    m = re.search(r'### Fitxers i directoris\n.*?```\n(.*?)```', text, re.S)
    if not m:
        return [(ERROR, 'no trobo l\'arbre de README.md §Fitxers i directoris')]
    entrades, generades = set(), set()
    for l in m.group(1).split('\n'):
        mm = re.match(r'^[├└]── (\S+)', l)
        if mm:
            (generades if 'Generat' in l else entrades).add(mm.group(1).rstrip('/'))
    arrel = {f.split('/')[0] for f in versionats()}
    r = []
    if arrel - entrades:
        r.append((ERROR, 'l\'arbre de README.md no té ' + ', '.join(sorted(arrel - entrades))))
    if entrades - arrel:
        r.append((ERROR, 'l\'arbre de README.md té entrades que no són versionades (si són generades, '
                         'cal marcar-les «Generat»): ' + ', '.join(sorted(entrades - arrel))))
    return r


def c_classificacio(ctx):
    sense = [f for f in versionats() if classifica(f)[0] is None]
    if sense:
        return [(AVIS, 'fitxers sense classe a CLASSES de comprova.py (es tracten com a nivell 2): '
                       + ', '.join(sense))]
    return []


def c_decisions(ctx):
    registre = (ARREL / '24_specs/registre_de_decisions.md').read_text(encoding='utf-8')
    existents = set(re.findall(r'^### D-(\d+)$', registre, re.M))
    citats = {}
    for l in git('grep', '--untracked', '-n', '-I', '-o', '-E', r'(\bD-[0-9]+\b|#d-[0-9]+\b)', check=False).split('\n'):
        if l:
            lloc, cita = l.rsplit(':', 1)
            citats.setdefault(cita.split('-')[-1], lloc)
    falten = sorted(set(citats) - existents, key=int)
    return [(ERROR, f'D-{d}, citat a {citats[d]}, no és al registre de decisions') for d in falten]


def c_exr_sol(ctx):
    def etiquetes(prefix):
        return set(re.findall(r'\{#' + prefix + r'-([a-z0-9-]+)', git('grep', '--untracked', '-h', '-o', '-E', r'\{#' + prefix + r'-[a-z0-9-]+',
                                                                      '--', '*.qmd', check=False)))
    falten = sorted(etiquetes('sol') - etiquetes('exr'))
    return [(ERROR, f'#sol-{s} no té el seu #exr-{s} (13_contrib.qmd §Problemes i solucions, D-22)') for s in falten]


def objectius_prosa(ctx):
    """{fitxer: línies o None} dels .qmd a mirar: les línies afegides, o tot el corpus amb --tot
    (sense els fitxers que documenten els casos, que citen el que les comprovacions busquen)."""
    if ctx.tot:
        return {f: None for f in versionats() if f.endswith('.qmd') and 'documenta' not in classifica(f)[1]}
    return {f: ctx.canvis.diff(f)[0] for f in ctx.canvis.qmd() if ctx.canvis.diff(f)[0]}


def c_prosa(ctx):
    import lint_prosa
    formes = lint_prosa.formes_no_admeses(ARREL)
    r = []
    for f, linies in objectius_prosa(ctx).items():
        for path, n, tipus in lint_prosa.check(ARREL / f, linies,
                                                None if 'documenta' in classifica(f)[1] else formes):
            r.append((ERROR if tipus.startswith('forma no admesa') else AVIS, f'{f}:{n}: {tipus}'))
    return r


def c_ortografia(ctx):
    import ortografia
    motiu = ortografia.disponible()
    if motiu:
        raise Omesa(motiu)
    linies = {}
    for f, ls in objectius_prosa(ctx).items():
        linies.update(ortografia.prosa(f, ls))
    trobats = ortografia.desconeguts(linies)
    if not trobats:
        return []
    if ctx.tot:
        compte = {}
        for _, m in trobats:
            compte[m] = compte.get(m, 0) + 1
        mots = sorted(compte, key=lambda m: -compte[m])
        return [(AVIS, f'{len(mots)} mots desconeguts al corpus (els més freqüents: '
                       + ', '.join(f'{m} ({compte[m]})' for m in mots[:30])
                       + '). Si són legítims, van a 24_specs/diccionari.txt; la llista sencera: '
                         'python3 25_scripts/ortografia.py --resum $(git ls-files \'*.qmd\')')]
    return [(AVIS, f'{f}:{n}: «{m}» (si és legítim, a 24_specs/diccionari.txt)') for (f, n), m in trobats]


def c_gramatica(ctx):
    rc, sortida = executa(PY, '25_scripts/gramatica.py', '--tot', timeout=1800)
    if rc == 3:
        raise Omesa(sortida.split('\n')[-1].removeprefix('[gramatica] omesa: '))
    return [(AVIS, retalla(sortida))] if rc else []


def c_marques(ctx):
    r = []
    for f in ctx.canvis.qmd():
        if 'documenta' in classifica(f)[1]:
            continue                        # la guia parla de les marques
        afegides = ctx.canvis.diff(f)[0]
        for n, l in enumerate((ARREL / f).read_text(encoding='utf-8').split('\n'), 1):
            if n in afegides and re.search(r'\bTODO\b(?!\.md)', l):
                r.append((AVIS, f'{f}:{n}: marca TODO a una línia afegida (13_contrib.qmd §Commits)'))
    return r


def script(nom, *args, gravetat=AVIS):
    """Una comprovació que és un script de 25_scripts amb el codi de sortida 1 si troba res."""
    def c(ctx):
        rc, sortida = executa(PY, f'25_scripts/{nom}', *args)
        return [(gravetat, retalla(sortida))] if rc else []
    return c


def c_taules(ctx):
    if importlib.util.find_spec('fontTools') is None:
        raise Omesa('falta fontTools (pip install fonttools)')
    rc, sortida = executa(PY, '25_scripts/verifica_taules.py')
    if rc == 3:
        raise Omesa(sortida.split('\n')[-1].removeprefix('[taules] omesa: '))
    return [(AVIS, retalla(sortida))] if rc else []


def c_coherencia(ctx):
    guia = GUIA.read_text(encoding='utf-8')
    quarto = (ARREL / '_quarto.yml').read_text(encoding='utf-8')
    r = []

    def files(despres_de):
        """La primera columna de la primera taula després d'un text de la guia."""
        if despres_de not in guia:
            r.append((AVIS, f'no trobo «{despres_de}» a 13_contrib.qmd'))
            return set()
        celes = []
        for l in guia.split(despres_de, 1)[1].split('\n'):
            if l.startswith('|'):
                celes.append(l.strip('|').split('|')[0].strip())
            elif celes:
                break
        return set(celes[2:])

    def compara(nom, a_la_guia, de_debo):
        if a_la_guia - de_debo:
            r.append((AVIS, f'{nom}: la guia en té que no existeixen: ' + ', '.join(sorted(a_la_guia - de_debo))))
        if de_debo - a_la_guia:
            r.append((AVIS, f'{nom}: en falten a la guia: ' + ', '.join(sorted(de_debo - a_la_guia))))

    peces = {c.strip('`') for c in files('**Peces del render que no són al Makefile**')}
    compara('Peces del render (§Renderitzar el projecte)', peces,
            set(re.findall(r'25_scripts/\w+\.lua', quarto)) | set(re.findall(r'^\s*- (\w+\.html)\b', quarto, re.M))
            | {'preamble.tex'})
    claude = {re.sub(r'^(Hook|Skill|Subagent) `([^`]+)`$', r'\1 \2', c) for c in files('#### Claude Code: el directori `.claude/`')}
    compara('Peces de .claude/ (§IA)', claude,
            {f'Hook {p.name}' for p in (ARREL / '.claude/hooks').glob('*.sh')}
            | {f'Skill {p.parent.name}' for p in (ARREL / '.claude/skills').glob('*/SKILL.md')}
            | {f'Subagent {p.stem}' for p in (ARREL / '.claude/agents').glob('*.md')})
    sufixos = {c.strip('`') for c in files('Els sufixos d\'origen són:')}
    compara('Sufixos d\'origen (§Convencions SVG)', sufixos, {f'__{s}' for s in re.findall(r'"__(\w+?)_light"', quarto)})
    # Els mots del diccionari del projecte que ja no fa servir cap fitxer.
    diccionari = ARREL / '24_specs/diccionari.txt'
    if diccionari.exists():
        mots = [m for m in diccionari.read_text(encoding='utf-8').split('\n') if m]
        text = '\n'.join((ARREL / f).read_text(encoding='utf-8', errors='replace') for f in versionats()
                         if not f.startswith(('.vscode/', '24_specs/diccionari.txt')) and (ARREL / f).is_file()
                         and not f.endswith(('.png', '.jpg', '.pdf')))
        usats = set(re.findall(r"(?<![\w'’])(" + '|'.join(map(re.escape, sorted(mots, key=len, reverse=True)))
                               + r")(?![\w'’])", text, re.I))
        sobren = {m for m in mots if m.lower() not in {u.lower() for u in usats}}
        if sobren:
            r.append((AVIS, '24_specs/diccionari.txt té mots que no fa servir cap fitxer: ' + ', '.join(sorted(sobren))))
    return r


def c_eines(ctx):
    fitxers = versionats() if ctx.tot else [f for f in ctx.canvis.fitxers if (ARREL / f).exists()]
    r = []
    for f in fitxers:
        if f.endswith('.py'):
            try:
                compile((ARREL / f).read_bytes(), f, 'exec')
            except (SyntaxError, ValueError) as e:
                r.append((ERROR, f'{f}: {e}'))
        elif f.endswith('.sh') or f.startswith('.githooks/'):
            rc, sortida = executa('bash', '-n', f)
            if rc:
                r.append((ERROR, f'{f}: {sortida}'))
    if ctx.tot or '25_scripts/comprova.py' in ctx.canvis.fitxers:
        r += [(ERROR, f'autotest: {e}') for e in autotest()]
    return r


def c_calendari(ctx):
    rc, sortida = executa(PY, '25_scripts/verifica_calendari.py')
    r = [(AVIS, retalla(sortida))] if rc else []
    if toca('04_laboratori/Lcalendari.qmd')(ctx):
        r.append((INFO, 'Lcalendari.qmd: abans del commit cal passar l\'agent verificador-calendari '
                        '(Claude Code; 13_contrib.qmd §IA)'))
    return r


def c_laboratoris(ctx):
    rc, sortida = executa(PY, '25_scripts/verifica_laboratoris.py', timeout=1800)
    if rc == 3:
        raise Omesa(sortida.split('\n')[-1])
    return [(ERROR, retalla(sortida))] if rc else []


def c_pdf(ctx):
    motius = []
    for f in ctx.canvis.qmd():
        if 'html' in classifica(f)[1]:
            continue
        linies = '\n'.join(ctx.canvis.diff(f)[1])
        motius += [f'«{forma}» a {f}' for forma in FORMES_PDF if forma in linies]
    if motius:
        return [(AVIS, 'el canvi pot afectar el PDF, que make render no exercita: abans de donar-lo per '
                       'bo, make comprova-tot (13_contrib.qmd §Verificació de l\'entorn). Motius: ' + '; '.join(motius))]
    return []


def c_estetica(ctx):
    return [(INFO, 'revisió estètica: mireu el canvi renderitzat, a l\'HTML en clar i en fosc i al PDF '
                   '(13_contrib.qmd §Comprovacions per nivells; skill render a Claude Code)')]


def c_render(ctx):
    if shutil.which('quarto') is None:
        raise Omesa('falta Quarto')
    objectiu = 'render-complet' if ctx.nivell >= 3 else 'render'
    rc, sortida = executa('make', objectiu, timeout=3600)
    if rc:
        return [(ERROR, f'make {objectiu} ha fallat. Darreres línies:\n' + '\n'.join(sortida.split('\n')[-30:]))]
    avisos = [l.strip() for l in sortida.split('\n') if re.match(r'\s*\[?WARN(ING)?\b', l)]
    if avisos:
        return [(ERROR, f'make {objectiu} ha acabat amb {len(avisos)} WARNING, i el render ha d\'acabar net '
                        f'(13_contrib.qmd §Verificació de l\'entorn):\n' + retalla('\n'.join(avisos), 20))]
    return []


def c_sortida(ctx):
    r = []
    pdf = ARREL / '_book/Estructura-de-computadors.pdf'
    guia = {f'{Path(p).stem}.html' for p in llista({'documenta'}) if p.endswith('.qmd')}
    trobats = []
    for p in (ARREL / '_book').rglob('*'):
        # El JavaScript (anchor.min.js en conté una expressió regular), el cercador, que copia el text de
        # les pàgines, i la guia, que cita la forma.
        if p.is_file() and p.suffix in ('.html', '.json') and p.name not in guia | {'search.json'}:
            if '?@' in p.read_text(encoding='utf-8', errors='replace'):
                trobats.append(str(p.relative_to(ARREL)))
    if trobats:
        r.append((ERROR, 'referències sense resoldre («?@») a: ' + ', '.join(trobats)))
    if not pdf.exists():
        r.append((ERROR, 'no hi ha PDF a _book/ després de make render-complet'))
    elif shutil.which('pdftotext') is None:
        r.append((OMESA, 'la cerca al PDF: falta pdftotext (poppler-utils)'))
    else:
        rc, text = executa('pdftotext', pdf, '-')
        if '?@' in text:
            r.append((ERROR, f'referències sense resoldre («?@») al PDF: {text.count("?@")}'))
    return r


class Comprovacio:
    def __init__(self, id, titol, detecta, quan, quan_text, efecte, fn):
        self.id, self.titol, self.detecta, self.quan, self.quan_text, self.efecte, self.fn = \
            id, titol, detecta, quan, quan_text, efecte, fn


def toca(*patrons):
    return lambda ctx: any(fnmatch.fnmatchcase(f, p) for f in ctx.canvis.fitxers for p in patrons)


SEMPRE = lambda ctx: True                                      # noqa: E731
QMD = lambda ctx: ctx.tot or bool(ctx.canvis.qmd())            # noqa: E731

COMPROVACIONS = [
    Comprovacio('registres', 'Registres', 'Els registres versionats són al dia: el glossari de termes, els SVG de model (a) '
                'i les dues taules d\'aquesta secció (els arregla `make registres`); el recompte de la capçalera del '
                '`TODO.md` i l\'arbre del `README.md` (a mà)', SEMPRE, 'Sempre', 'Atura', c_registres),
    Comprovacio('decisions', 'Decisions citades', 'Cada `D-n` citat en un fitxer versionat existeix al registre de decisions',
                SEMPRE, 'Sempre', 'Atura', c_decisions),
    Comprovacio('exr_sol', 'Enunciats i solucions', 'Cada `#sol-` té el seu `#exr-` amb el mateix slug (D-22)',
                SEMPRE, 'Sempre', 'Atura', c_exr_sol),
    Comprovacio('eines', 'Eines', 'La sintaxi dels `.py` (`compile`) i dels `.sh` (`bash -n`) canviats; si canvia `comprova.py`, '
                'l\'autoprova de la classificació', lambda ctx: ctx.tot or any(
                    f.endswith(('.py', '.sh')) or f.startswith('.githooks/') for f in ctx.canvis.fitxers),
                'En tocar un `.py` o un `.sh`', 'Atura', c_eines),
    Comprovacio('prosa', 'Prosa', 'Les formes que no s\'han de fer servir (§Anglicismes i terminologia obligatòria), que '
                'aturen; i els dobles espais i les cometes, que avisen (`lint_prosa.py`)', QMD,
                'En tocar un `.qmd`: les línies afegides', 'Atura (formes) o avisa', c_prosa),
    Comprovacio('ortografia', 'Ortografia', 'Mots que no són als diccionaris de `hunspell` (català i anglès) ni al '
                'del projecte, `24_specs/diccionari.txt` (`ortografia.py`)', QMD,
                'En tocar un `.qmd`: les línies afegides', 'Avisa', c_ortografia),
    Comprovacio('gramatica', 'Gramàtica', 'Concordances, preposicions, puntuació i la resta de regles de LanguageTool, '
                'sense les que al llibre fan soroll ni les formes correctes que marquen (`gramatica.py`, amb '
                '`24_specs/gramatica.toml`; demana Java 17, i baixa LanguageTool la primera vegada)',
                lambda ctx: ctx.tot, 'Només `comprova-tot` (i `make gramatica`)', 'Avisa', c_gramatica),
    Comprovacio('marques', 'Marques TODO', '`TODO` a les línies afegides dels `.qmd` (§Commits)',
                lambda ctx: not ctx.tot and bool(ctx.canvis.qmd()), 'En tocar un `.qmd`', 'Avisa', c_marques),
    Comprovacio('format_codi', 'Format del codi', 'Els criteris mecànics del format dels blocs d\'assemblador '
                '(`verifica_format_codi.py`)', SEMPRE, 'Sempre', 'Avisa', script('verifica_format_codi.py')),
    Comprovacio('taules', 'Taules al PDF', 'Desbordaments i amplades de les taules del PDF, mesurats sobre el font '
                '(`verifica_taules.py`, amb fontTools i les fonts del PDF)', SEMPRE, 'Sempre', 'Avisa', c_taules),
    Comprovacio('figures', 'Figures', 'Els avisos de l\'inventari de figures: peus, remissions, `<title>` i `<desc>`, '
                'colors, duplicats (`inventari_figures.py --comprova`)', SEMPRE, 'Sempre', 'Avisa',
                script('inventari_figures.py', '--comprova')),
    Comprovacio('orfes', 'Fitxers orfes', 'Fitxers versionats que cap altre no cita (`orfes.py`, D-98)',
                SEMPRE, 'Sempre', 'Avisa', script('orfes.py')),
    Comprovacio('classificacio', 'Classificació', 'Cada fitxer té classe a la taula de `comprova.py`; si no, el canvi '
                'es tracta com a nivell 2', SEMPRE, 'Sempre', 'Avisa', c_classificacio),
    Comprovacio('coherencia', 'Taules explicatives', 'Les taules de la guia que no es poden generar (les peces del '
                'render, el directori `.claude/`, els sufixos d\'origen) tenen una fila per fitxer; el diccionari del '
                'projecte no té mots que ja no s\'usen', SEMPRE, 'Sempre', 'Avisa', c_coherencia),
    Comprovacio('calendari', 'Calendari', '`verifica_calendari.py`, i el recordatori de passar l\'agent '
                '`verificador-calendari`', lambda ctx: ctx.tot or toca('04_laboratori/Lcalendari.qmd')(ctx),
                'En tocar `Lcalendari.qmd`', 'Avisa', c_calendari),
    Comprovacio('laboratoris', 'Programes del laboratori', 'RARS assembla i executa els blocs `.s` de L1–L6 '
                '(`verifica_laboratoris.py`; demana Java)', lambda ctx: ctx.tot or toca('04_laboratori/L[1-6].qmd')(ctx),
                'En tocar `L1.qmd`–`L6.qmd`', 'Atura', c_laboratoris),
    Comprovacio('pdf', 'PDF', 'Formes que afecten el PDF a les línies canviades (`when-format`, `tbl-colwidths`, `#fig-`, '
                '`![`, `$`): cal `make comprova-tot`', lambda ctx: not ctx.tot and ctx.nivell == 2,
                'Nivell 2', 'Avisa', c_pdf),
    Comprovacio('estetica', 'Revisió estètica', 'El recordatori de mirar el canvi renderitzat, a l\'HTML en clar i en '
                'fosc i al PDF', lambda ctx: not ctx.tot and ctx.nivell >= 3, 'Nivells 3 i 4', 'Avisa', c_estetica),
    Comprovacio('render', 'Render', '`make render` (nivell 2) o `make render-complet` (nivells 3 i 4, i `comprova-tot`), '
                'que ha d\'acabar net i sense cap WARNING', lambda ctx: ctx.nivell >= 2 and not ctx.sense_render,
                'Nivells 2, 3 i 4', 'Atura', c_render),
    Comprovacio('sortida', 'Sortida', 'Referències sense resoldre (`?@`) al `_book/` i al PDF, i que hi hagi PDF',
                lambda ctx: ctx.tot and not ctx.sense_render, 'Només `comprova-tot`', 'Atura', c_sortida),
]


# ---------------------------------------------------------------------------
# Les taules de la guia (13_contrib.qmd §Comprovacions per nivells)
# ---------------------------------------------------------------------------
TAULES_GUIA = ['nivells', 'comprovacions']


def patrons(classe):
    """Els patrons d'una classe per a la taula, sense els que un altre de la mateixa classe ja cobreix
    (`13_contrib.qmd` hi és per les etiquetes, però per al nivell n'hi ha prou amb `*.qmd`)."""
    de_la_classe = [p for p, c, _ in CLASSES if c == classe]
    return ', '.join(f'`{p[:-1] if p.endswith("/*") else p}`' for p in de_la_classe
                     if not any(q != p and fnmatch.fnmatchcase(p, q) for q in de_la_classe))


def taula_guia(marca):
    cel = lambda s: s.replace('|', '\\|')                      # noqa: E731
    if marca == 'nivells':
        files = [
            ('0', 'Operatiu', 'Només canvien fitxers que el render no llegeix (' + patrons('operatiu') + '), o eines de '
             'comprovació i generadors amb la sortida versionada (' + patrons('eina') + ')', 'Les comprovacions que diuen '
             '«Sempre» a la taula següent'),
            ('1', 'Menor', 'Només canvien `.qmd`, i cap línia canviada (afegida o treta) no porta marcatge: ni `@`, `{`, '
             '`}`, `$`, `\\`, `<`, `![` o la barra vertical, ni comença amb `:::`, `---`, `#`, una tanca de codi o `[^`, ni és buida. '
             'Hi entra el codi d\'un bloc sense marcatge, que el render no interpreta',
             'Les de la prosa'),
            ('2', 'Contingut', 'Qualsevol altre canvi del text del llibre (' + patrons('contingut') + '), o un fitxer '
             'que no té classe', '`make render`'),
            ('3', 'Figures', patrons('figura'), '`make render-complet`, i el recordatori de la revisió estètica'),
            ('4', 'Configuració', patrons('configuracio'), 'Com al nivell 3'),
        ]
        o = ['| Nivell | Quan | Què s\'hi afegeix | Temps |', '| :--- | :--- | :--- | :--- |']
        o += [f'| **{n} {nom}** | {cel(quan)} | {cel(que)} | {NIVELLS[int(n)][1]} |' for n, nom, quan, que in files]
        o.append(f'| **`make comprova-tot`** | Quan es demana | Totes, sobre el corpus sencer, amb `make render-complet`, '
                 f'RARS i les referències sense resoldre de la sortida | {TEMPS_TOT} |')
    else:
        o = ['| Comprovació | Què mira | Quan | Efecte |', '| :--- | :--- | :--- | :--- |']
        o += [f'| {c.titol} | {cel(c.detecta)} | {cel(c.quan_text)} | {c.efecte} |' for c in COMPROVACIONS]
    return '\n'.join(o)


def marques(marca):
    return (f'<!-- comprova:{marca}:inici — la genera 25_scripts/comprova.py --taula; no l\'editeu a mà -->',
            f'<!-- comprova:{marca}:fi -->')


def bloc_guia(marca):
    inici, fi = marques(marca)
    text = GUIA.read_text(encoding='utf-8')
    if inici not in text or fi not in text:
        return None
    return text.split(inici, 1)[1].split(fi, 1)[0].strip('\n')


def escriu_taules():
    text = GUIA.read_text(encoding='utf-8')
    for marca in TAULES_GUIA:
        inici, fi = marques(marca)
        if inici not in text or fi not in text:
            raise SystemExit(f'comprova: no trobo les marques de la taula «{marca}» a 13_contrib.qmd')
        abans, resta = text.split(inici, 1)
        text = abans + inici + '\n' + taula_guia(marca) + '\n' + fi + resta.split(fi, 1)[1]
    GUIA.write_text(text, encoding='utf-8')
    print('[comprova] taules de 13_contrib.qmd §Comprovacions per nivells al dia')


# ---------------------------------------------------------------------------
# Autoprova de la classificació
# ---------------------------------------------------------------------------
CASOS = [
    ('TODO.md', 'operatiu'), ('24_specs/registre_de_decisions.md', 'operatiu'), ('.claude/hooks/x.sh', 'operatiu'),
    ('22_figs_originals/conservats/A7_x.svg', 'operatiu'), ('24_specs/glossari.toml', 'operatiu'),
    ('25_scripts/orfes.py', 'eina'), ('25_scripts/gen_T7.py', 'eina'), ('25_scripts/verifica_taules.py', 'eina'),
    ('01_apunts/A3.qmd', 'contingut'), ('21_riscv/RV32I_x.qmd', 'contingut'), ('LICENSE.md', 'contingut'),
    ('13_contrib.qmd', 'contingut'),
    ('22_figs_originals/A7_x.svg', 'figura'), ('25_scripts/gen_MC.py', 'figura'), ('24_specs/MC.toml', 'figura'),
    ('24_specs/A7_x__graphviz.gv', 'figura'),
    ('_quarto.yml', 'configuracio'), ('25_scripts/continguts.lua', 'configuracio'),
    ('25_scripts/gen_taules_auto.py', 'configuracio'), ('custom_dark.scss', 'configuracio'), ('Makefile', 'configuracio'),
    ('un_fitxer_nou.xyz', None),
]
LINIES = [('Text de prosa, sense res més.', False), ('Vegeu @sec-x.', True), ('', True), ('::: {.callout-note}', True),
          ('La fórmula $x$.', True), ('## Títol', True), ('```{.s}', True), ('Una «cita» i *cursiva*.', False),
          ('![](auto_figs/x.svg)', True), ('a | b', True)]


def autotest():
    errors = [f'{f}: {classifica(f)[0]} i no {c}' for f, c in CASOS if classifica(f)[0] != c]
    errors += [f'«{l}»: marcatge {not m}' for l, m in LINIES if bool(MARCATGE.search(l)) != m]
    for marca in TAULES_GUIA:
        if not taula_guia(marca).startswith('| '):
            errors.append(f'la taula «{marca}» no es genera')
    return errors


# ---------------------------------------------------------------------------
# Historial: el nivell que haurien tingut els commits d'abans
# ---------------------------------------------------------------------------
def linies_canviades(diff):
    """El text de les línies afegides i tretes d'un diff d'un sol fitxer, sense la capçalera."""
    ls, dins = [], False
    for fila in diff.split('\n'):
        if fila.startswith('@@'):
            dins = True
        elif dins and fila.startswith(('+', '-')):
            ls.append(fila[1:])
    return ls


def historial(n, ref):
    """El repartiment per nivells dels últims n commits sense fusions fins a ref, amb la
    classificació d'avui: per mesurar què costaria cada nivell abans de canviar-lo."""
    compte, pdf = {k: 0 for k in NIVELLS}, 0
    for c in git('rev-list', '--no-merges', '-n', str(n), ref).split():
        nivell, canviades = 0, []
        for fila in git('show', '--format=', '--name-status', '--no-renames', c).split('\n'):
            if not fila:
                continue
            estat, f = fila.split('\t', 1)
            classe, etiquetes = classifica(f)
            if classe is None:
                n_f = 2
            elif classe == 'contingut' and f.endswith('.qmd') and estat == 'M':
                ls = linies_canviades(git('show', '--format=', '-U0', '--no-color', c, '--', f))
                n_f = 2 if any(MARCATGE.search(l) for l in ls) else 1
                if 'html' not in etiquetes:
                    canviades += ls
            else:
                n_f = NIVELL_CLASSE[classe]
            nivell = max(nivell, n_f)
        compte[nivell] += 1
        if nivell == 2 and any(forma in l for l in canviades for forma in FORMES_PDF):
            pdf += 1
    total = sum(compte.values())
    print(f'[comprova] {total} commits sense fusions fins a {ref}: '
          + ', '.join(f'nivell {k}: {v}' for k, v in compte.items())
          + f' (dels de nivell 2, {pdf} amb formes que afecten el PDF). Un fitxer que avui no té classe '
            '(una ruta que ja no existeix) compta com a nivell 2.')


class Context:
    def __init__(self, canvis, nivell, tot, sense_render):
        self.canvis, self.nivell, self.tot, self.sense_render = canvis, nivell, tot, sense_render


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--base', help='la branca sencera, des del merge-base amb aquesta referència')
    ap.add_argument('--tot', action='store_true')
    ap.add_argument('--sense-render', action='store_true')
    ap.add_argument('--explica', action='store_true')
    ap.add_argument('--taula', action='store_true')
    ap.add_argument('--autotest', action='store_true')
    ap.add_argument('--llista')
    ap.add_argument('--historial', type=int, metavar='N')
    ap.add_argument('--des-de', default='HEAD', metavar='REF')
    ap.add_argument('-v', action='store_true')
    a = ap.parse_args()
    sys.path.insert(0, str(ARREL / '25_scripts'))

    if a.llista:
        print('\n'.join(llista(a.llista.split(','))))
        return 0
    if a.taula:
        escriu_taules()
        return 0
    if a.historial:
        historial(a.historial, a.des_de)
        return 0
    if a.autotest:
        errors = autotest()
        print('\n'.join(errors) or f'[comprova] autotest: {len(CASOS)} fitxers i {len(LINIES)} línies, tots bé')
        return 2 if errors else 0

    try:
        canvis = Canvis(a.base, a.tot)
    except subprocess.CalledProcessError as e:
        print(f'[comprova] git ha fallat: {e.stderr.strip()}', file=sys.stderr)
        return 2
    nivell, motiu = canvis.nivell()
    ctx = Context(canvis, nivell, a.tot, a.sense_render)
    actives = [c for c in COMPROVACIONS if c.quan(ctx)]
    nom = 'totes (comprova-tot)' if a.tot else f'nivell {nivell} ({NIVELLS[nivell][0]})'
    cap = f'[comprova] {nom}'
    if not a.tot:
        cap += f': {len(canvis.fitxers)} fitxers canviats respecte de {"HEAD" if a.base is None else a.base}'
        if motiu and nivell > 0:
            cap += ' (el nivell el dona ' + ', '.join(motiu[:3]) + (' …' if len(motiu) > 3 else '') + ')'
    print(cap)

    if a.explica:
        for f in canvis.fitxers:
            n, per = canvis.nivell_fitxer(f)
            print(f'  {f}: nivell {n} ({per})')
        print('Comprovacions: ' + ', '.join(c.id for c in actives))
        if nivell >= 2 and a.sense_render:
            print('El render s\'ometria (--sense-render).')
        return 0

    resultats = []
    inici = time.monotonic()
    for c in actives:
        t = time.monotonic()
        try:
            r = c.fn(ctx)
        except Omesa as e:
            r = [(OMESA, str(e))]
        except subprocess.TimeoutExpired as e:
            r = [(ERROR, f'ha superat el temps màxim ({e.timeout} s)')]
        resultats.append((c, r, time.monotonic() - t))
    if nivell >= 2 and a.sense_render and not a.tot:
        resultats.append((None, [(INFO, f'render omès (--sense-render): el nivell {nivell} demana '
                                        f'{"make render" if nivell == 2 else "make render-complet"}; '
                                        'el fa el pre-push (make comprova-branca)')], 0))

    compte = {g: 0 for g in SIGNE}
    for c, r, t in resultats:
        if not r:
            compte[OK] += 1
            if a.v:
                print(f'{SIGNE[OK]} {c.id} ({t:.1f} s)')
            continue
        for g, missatge in r:
            compte[g] += 1
            print(f'{SIGNE[g]} {c.id if c else "render"}: {missatge}')
    print(f'[comprova] {compte[ERROR]} errors, {compte[AVIS]} avisos, {compte[INFO]} recordatoris, '
          f'{compte[OMESA]} omeses; {len(actives)} comprovacions en {time.monotonic() - inici:.0f} s')
    if compte[ERROR]:
        return 2
    return 1 if compte[AVIS] + compte[INFO] + compte[OMESA] else 0


if __name__ == '__main__':
    sys.exit(main())
