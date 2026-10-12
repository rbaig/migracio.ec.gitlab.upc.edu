#!/usr/bin/env python3
"""verifica_callouts.py — Cap callout dins d'un altre callout (13_contrib.qmd §Imbricacions, D-110).

Recorre els `.qmd` versionats i segueix els divs de tres o més `:`; fora dels
blocs de codi, un div amb una classe `.callout-*` dins d'un altre és una
imbricació. També compta el que porta un `{{< include >}}` fet dins d'un callout.
Els divs que no són callouts (`.content-visible`, `.light-content`, `.resposta`…)
sí que s'hi poden imbricar.

Ús:
    python3 25_scripts/verifica_callouts.py      # surt amb 1 si en troba
"""

import re
import subprocess
import sys
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
FENCE = re.compile(r'^\s*(:{3,})\s*(.*)$')
CODI = re.compile(r'^\s*(?:(?:[-*+]|\d+\.)\s+)?(```|~~~)')   # també «- ```», dins d'una llista
INCLUDE = re.compile(r'\{\{<\s*include\s+(\S+)\s*>\}\}')


def te_callout(fitxer):
    """Si un fitxer inclòs obre algun callout (fora del codi)."""
    dins_codi = False
    for linia in fitxer.read_text(encoding='utf-8').split('\n'):
        if CODI.match(linia):
            dins_codi = not dins_codi
        elif not dins_codi and (m := FENCE.match(linia)) and '.callout' in m.group(2):
            return True
    return False


def revisa(rel):
    fitxer = ARREL / rel
    troballes, pila, dins_codi = [], [], False
    for n, linia in enumerate(fitxer.read_text(encoding='utf-8').split('\n'), 1):
        if CODI.match(linia):
            dins_codi = not dins_codi
            continue
        if dins_codi:
            continue
        de_callout = [lloc for es, lloc in pila if es]
        m = FENCE.match(linia)
        if not m:
            inc = INCLUDE.search(linia)
            if inc and de_callout and te_callout((fitxer.parent / inc.group(1)).resolve()):
                troballes.append(f'{rel}:{n}: l\'include de {inc.group(1)} porta un callout dins del de la línia {de_callout[-1]}')
            continue
        if not m.group(2).strip():
            if pila:
                pila.pop()
            continue
        es_callout = '.callout' in m.group(2)
        if es_callout and de_callout:
            troballes.append(f'{rel}:{n}: callout dins del callout de la línia {de_callout[-1]}')
        pila.append((es_callout, n))
    return troballes


def main():
    fitxers = subprocess.run(['git', 'ls-files', '*.qmd'], cwd=ARREL, capture_output=True, text=True, check=True).stdout.split()
    troballes = [t for f in fitxers for t in revisa(f)]
    for t in troballes:
        print(f'[callouts] {t} (13_contrib.qmd §Imbricacions, D-110)')
    return 1 if troballes else 0


if __name__ == '__main__':
    sys.exit(main())
