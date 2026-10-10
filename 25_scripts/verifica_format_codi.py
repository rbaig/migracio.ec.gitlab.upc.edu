#!/usr/bin/env python3
"""Format dels blocs d'assemblador dels .qmd, contra @imp-codi-format-criteris.

Els criteris són els del callout `#imp-codi-format-criteris` d'A2 (§Format del
codi). Aquest script en comprova la part mecànica, sobre el font: els blocs
```{.s …}``` de tots els .qmd versionats (menys TODO.md i 13_contrib.qmd), tret
dels marcats amb `codi_erroni` al filename, que són incorrectes a posta.

Regles:
  F1  Directives de segment (.text, .data; també .section, vegeu 13_contrib.qmd)
      i de visibilitat (.globl, .extern), a la columna 0.
  F2  Etiquetes, a la columna 0.
  F3  Instruccions i directives de dades, sagnades amb 8 espais (o, a la
      mateixa línia, darrere d'una etiqueta). Són indistints `.eqv` i `.align`,
      com diu el callout, i també `.set`, que fa el mateix paper que `.eqv`, i
      `.macro`/`.end_macro`, que el callout no regula.
  F4  Cap tabulador.
  F5  Operands alineats en columna: el mnemònic o la directiva ocupen un camp
      de 8 caràcters, i els operands comencen a la columna 16; si el mnemònic
      en té 8 o més, n'hi ha prou amb un espai. Darrere d'una etiqueta, el
      mnemònic comença a la columna 8 (o a un espai de l'etiqueta, si no hi cap).

No mira els comentaris (ni la seva columna) ni les línies que només contenen
una el·lipsi (`...`), que marquen codi omès.

Ús:
    python3 25_scripts/verifica_format_codi.py                 # resum per regla i fitxer
    python3 25_scripts/verifica_format_codi.py --detall        # i cada línia
    python3 25_scripts/verifica_format_codi.py --regles F1,F2 FITXER.qmd…

Surt amb 1 si troba res i amb 0 si no.
"""

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict

BLOC = re.compile(r'^```\{([^}]*\.s\b[^}]*)\}\n(.*?)^```', re.S | re.M)
ETIQUETA = re.compile(r'^(\s*)([A-Za-z_][\w.]*:)(\s*)(.*)$')
SEGMENT = re.compile(r'^\s*\.(text|data|section|globl|global|extern)\b')
INDISTINTES = ('.eqv', '.set', '.align', '.macro', '.end_macro')
REGLES = {
    'F1': 'directiva de segment o de visibilitat sagnada',
    'F2': 'etiqueta sagnada',
    'F3': 'instrucció o dada sense els 8 espais de sagnat',
    'F4': 'tabulador',
    'F5': 'operands o mnemònic fora de columna',
}


def fitxers_per_defecte():
    sortida = subprocess.run(['git', 'ls-files', '*.qmd'], capture_output=True,
                             text=True, check=True).stdout.split()
    return [f for f in sortida if f not in ('TODO.md', '13_contrib.qmd')]


def sense_comentari(linia):
    # Les cadenes de les directives (.asciz "…#…") no contenen `#` al corpus;
    # si mai en contenen, caldrà tenir-les en compte aquí.
    return linia.split('#', 1)[0].rstrip()


def columna_operands(base, resta):
    """Comprova F5 per a `resta` (mnemònic + operands) que comença a `base`."""
    m = re.match(r'(\S+)(\s+)\S', resta)
    if not m:
        return True                       # sense operands: res a alinear
    mnemonic, espais = m.group(1), m.group(2)
    if len(mnemonic) >= 8:
        return espais == ' '
    return base + len(mnemonic) + len(espais) == 16


def comprova_linia(linia):
    """Retorna la llista de regles que la línia incompleix."""
    errors = []
    if '\t' in linia:
        errors.append('F4')
    s = sense_comentari(linia)
    if not s.strip() or s.strip() in ('...', '…'):
        return errors
    e = ETIQUETA.match(s)
    if e:
        if e.group(1):
            errors.append('F2')
        resta = e.group(4)
        if resta:
            col_etiqueta = len(e.group(1)) + len(e.group(2))
            col = col_etiqueta + len(e.group(3))
            esperada = 8 if col_etiqueta < 8 else col_etiqueta + 1
            if col != esperada or not columna_operands(col, resta):
                errors.append('F5')
        return errors
    if SEGMENT.match(s):
        if s[0].isspace():
            errors.append('F1')
        return errors
    paraula = s.split()[0]
    sagnat = len(s) - len(s.lstrip(' '))
    if not paraula.startswith(INDISTINTES):
        if sagnat != 8:
            errors.append('F3')
        elif not columna_operands(8, s[8:]):
            errors.append('F5')
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('fitxers', nargs='*')
    ap.add_argument('--detall', action='store_true', help='llista cada línia')
    ap.add_argument('--regles', default=','.join(REGLES),
                    help='regles a comprovar, separades per comes (per defecte, totes)')
    args = ap.parse_args()
    regles = set(args.regles.split(','))
    fitxers = args.fitxers or fitxers_per_defecte()

    trobades = defaultdict(list)          # regla -> [(fitxer, línia, text)]
    blocs = linies = 0
    for f in fitxers:
        text = open(f, encoding='utf-8').read()
        for m in BLOC.finditer(text):
            if 'codi_erroni' in m.group(1):
                continue
            blocs += 1
            inici = text.count('\n', 0, m.start(2)) + 1
            for i, linia in enumerate(m.group(2).split('\n')):
                if not linia.strip():
                    continue
                linies += 1
                for r in comprova_linia(linia):
                    if r in regles:
                        trobades[r].append((f, inici + i, linia))

    print(f'{blocs} blocs, {linies} línies')
    for r in sorted(REGLES):
        if r not in regles:
            continue
        llista = trobades.get(r, [])
        per_fitxer = Counter(f for f, _, _ in llista)
        detall = ', '.join(f'{f.rsplit("/", 1)[-1]} {n}' for f, n in per_fitxer.most_common())
        print(f'{r} {REGLES[r]}: {len(llista)}' + (f' ({detall})' if llista else ''))
        if args.detall:
            for f, n, linia in llista:
                print(f'    {f}:{n}: {linia}')
    return 1 if any(trobades.values()) else 0


if __name__ == '__main__':
    sys.exit(main())
