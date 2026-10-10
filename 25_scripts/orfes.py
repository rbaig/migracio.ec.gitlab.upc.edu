#!/usr/bin/env python3
"""Fitxers versionats que cap altre fitxer no cita (orfes).

Ús:
    python3 25_scripts/orfes.py     # llista els orfes; surt amb 1 si n'hi ha

Un fitxer és orfe si cap altre fitxer versionat (o nou, encara no versionat) no en
cita el nom o l'arrel. Per a les figures, el criteri és el de la sortida del
pre-render: un SVG de `22_figs_originals/` es consumeix si algun fitxer cita
`<arrel>__original` (o `<arrel>__extern`, als de `23_figs_externes/`), i un
fotograma d'una figura dinàmica (`<arrel>_pas<k>.svg`) si es consumeix la figura.

Quins fitxers queden fora i quins no compten com a cites ho diuen les etiquetes de
la classificació de 25_scripts/comprova.py (CLASSES), que és l'única del projecte:
- `fora_orfes`: no són mai orfes. Els originals de `22_figs_originals/conservats/`,
  que el llibre ja no consumeix i es conserven a posta, per a les diapositives
  (D-68), i la configuració de les eines (`.github/`, `.githooks/`, `.vscode/`,
  `.claude/`);
- `no_cita`: hi consten fitxers pel nom sense fer-los servir. El `TODO.md`, el seu
  arxiu i el registre de decisions citen fitxers retirats i orfes (regla 12 de la
  skill `escombrada`), i l'arbre del `README.md` els llista tots.

Petició de l'usuari (2026-10-08) i proposta de Claude Code acceptada el 2026-10-09
(D-98). El passa 25_scripts/comprova.py a cada commit, i avisa si n'hi ha cap.
"""
import re
import subprocess
import sys
from pathlib import Path

from comprova import classifica

ROOT = Path(__file__).resolve().parent.parent


def fitxers():
    sortida = subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard'],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return sorted({f for f in sortida.split('\n') if f and (ROOT / f).is_file()})


def claus(f):
    """Les cadenes que, si un altre fitxer les conté, fan que f no sigui orfe."""
    p = Path(f)
    if f.startswith(('22_figs_originals/', '23_figs_externes/')):
        m = re.match(r'(.+)_pas\d+$', p.stem)
        arrel = m.group(1) if m else p.stem
        return [f'{arrel}__original', f'{arrel}__extern'] + ([] if m else [p.name])
    return [p.name, p.stem]


def main():
    tots = fitxers()
    textos = {}
    for f in tots:
        if 'no_cita' in classifica(f)[1]:
            continue
        try:
            textos[f] = (ROOT / f).read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            pass
    orfes = [f for f in tots if 'fora_orfes' not in classifica(f)[1]
             and not any(k in text for g, text in textos.items() if g != f for k in claus(f))]
    for f in orfes:
        print(f)
    return 1 if orfes else 0


if __name__ == '__main__':
    sys.exit(main())
