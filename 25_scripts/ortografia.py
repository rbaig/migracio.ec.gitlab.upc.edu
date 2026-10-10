#!/usr/bin/env python3
"""Ortografia de la prosa dels .qmd amb hunspell (català i anglès) i el diccionari del projecte.

Passa la prosa per `hunspell` amb els diccionaris `ca_ES` i `en_US` (un mot és
bo si és a qualsevol dels dos: els termes anglesos van en cursiva, però en
català i en anglès s'escriuen igual molts mots) i amb el diccionari del
projecte, `24_specs/diccionari.txt` (un mot per línia), que és el mateix que fa
servir el corrector de VS Code (`.vscode/settings.json`). La prosa és la de
`lint_prosa.py`: sense la capçalera YAML, els blocs de codi, les matemàtiques,
les taules ni el codi en línia. No es miren les sigles (dues o més majúscules,
també apostrofades: «l'MC») ni els mots amb xifres.

Només avisa: un mot desconegut pot ser un error o un mot legítim que cal afegir
al diccionari del projecte, en el mateix commit que el fa servir. Les regles de
la guia que són mecàniques (les formes que no s'han de fer servir) no són aquí,
sinó a `lint_prosa.py`, que les atura.

Ús:
    python3 25_scripts/ortografia.py               # només les línies afegides respecte d'HEAD,
                                                   # més els .qmd nous encara no versionats
    python3 25_scripts/ortografia.py FITXER.qmd…   # fitxers sencers
    python3 25_scripts/ortografia.py --resum FITXER.qmd…   # només els mots, amb les ocurrències

Surt amb 1 si troba res, amb 0 si no i amb 3 si no hi ha `hunspell` o el
diccionari català (paquets `hunspell` i `hunspell-ca` a Debian i Ubuntu).
"""

import collections
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import lint_prosa

ARREL = Path(__file__).resolve().parent.parent
DICCIONARI = ARREL / '24_specs' / 'diccionari.txt'
DICCIONARIS = 'ca_ES,en_US'

NETEJA = [
    (re.compile(r'https?://\S+'), ' '),            # URL soltes
    (re.compile(r'\S*/\S*\.[A-Za-z]{2,4}\b\S*'), ' '),   # rutes amb extensió (X04_laboratori/Lcalendari.html)
    (re.compile(r'\bX-\w+'), ' X '),               # un sufix enganxat a una fórmula: «$i$-èsima»
    (re.compile(r'@[\w:-]+'), ' X '),              # referències creuades
    (re.compile(r'\[([^\[\]]*?)X'), r' \1 '),       # text d'un enllaç: lint_prosa en canvia «](URL)» per X
    (re.compile(r'\b[\w-]+(?:\.[\w-]+)*\.(?:com|org|net|io|cat|edu|es|eu)\b'), ' '),   # dominis
    (re.compile(r"\b[ldsmtnLDSMTN]['’](?=\*|X\b)"), ''),   # l'*stride*, d'`addi` (ja X): l'article fora
    (re.compile(r'[*_#>\[\]\ufe0f]'), ' '),        # marcatge, i el selector de variant dels emojis
]
SIGLA = re.compile(r"^[A-Z][A-Z0-9-]*s?$")         # MC, RV32I, Xs; amb l'elisió treta abans
ELISIO = re.compile(r"^[ldsmtnLDSMTN]['’]")


def disponible():
    """None si hunspell i el diccionari català hi són; si no, el motiu."""
    if not shutil.which('hunspell'):
        return 'falta hunspell (paquets hunspell i hunspell-ca)'
    prova = subprocess.run(['hunspell', '-d', DICCIONARIS, '-l'], input='casa',
                           capture_output=True, text=True)
    if prova.returncode != 0 or 'Can\'t open' in prova.stderr:
        return 'falta el diccionari català de hunspell (paquet hunspell-ca)'
    return None


def net(linia):
    for rx, substitut in NETEJA:
        linia = rx.sub(substitut, linia)
    return linia


def hunspell(text):
    """Els mots de text que hunspell no coneix. `-l` només els llista; `-a` en
    calcularia els suggeriments, que amb un mot llarg poden trigar minuts."""
    ordre = ['hunspell', '-l', '-i', 'utf-8', '-d', DICCIONARIS]
    if DICCIONARI.exists():
        ordre += ['-p', str(DICCIONARI)]
    return set(subprocess.run(ordre, input=text, capture_output=True, text=True,
                              check=True).stdout.split())


def ignora(mot):
    """Sigles, xifres, el marcador X de lint_prosa i el que no porta cap lletra."""
    return bool(len(mot) < 2 or SIGLA.match(mot) or re.search(r'\d', mot) or not re.search(r'[^\W\d_]', mot))


def desconeguts(linies):
    """[(clau, mot)] dels mots que hunspell no coneix, per a {clau: línia de prosa}."""
    if not linies:
        return []
    netes = {k: net(l) for k, l in linies.items()}
    # Segona passada, per parts: hunspell no aplica l'elisió als mots del diccionari
    # del projecte («d'Amdahl») i mira sencer un compost amb guionet («big-endian»).
    parts = {m: [p for p in ELISIO.sub('', m).strip('-').split('-') if p and not ignora(p)]
             for m in hunspell('\n'.join(netes.values())) if not ignora(ELISIO.sub('', m))}
    dolentes = hunspell('\n'.join({p for ps in parts.values() for p in ps}))
    mots = {m for m, ps in parts.items() if any(p in dolentes for p in ps)}
    if not mots:
        return []
    patro = re.compile(r"(?<![\w'’·-])(" + '|'.join(re.escape(m) for m in sorted(mots, key=len, reverse=True))
                       + r")(?![\w'’·-])")
    return [(k, m.group(1)) for k, l in netes.items() for m in patro.finditer(l)]


def prosa(path, only=None):
    """{(fitxer, línia): prosa} d'un .qmd, totes les línies o només les d'only."""
    text = (ARREL / path).read_text(encoding='utf-8')
    return {(path, n): l for n, l in lint_prosa.prose_lines(text).items()
            if only is None or n in only}


def main(argv):
    resum = '--resum' in argv
    argv = [a for a in argv if a != '--resum']
    motiu = disponible()
    if motiu:
        print(f'[ortografia] omesa: {motiu}', file=sys.stderr)
        return 3
    if argv:
        objectius = {os.path.relpath(Path(p).resolve(), ARREL): None for p in argv}
    else:
        os.chdir(ARREL)
        objectius = lint_prosa.added_lines()
    linies = {}
    for path, only in sorted(objectius.items()):
        if only is not None and not only:
            continue
        linies.update(prosa(path, only))
    trobats = desconeguts(linies)
    if resum:
        for mot, n in collections.Counter(m for _, m in trobats).most_common():
            print(f'{n:5d} {mot}')
    else:
        for (path, n), mot in trobats:
            print(f'{path}:{n}: «{mot}»')
    return 1 if trobats else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
