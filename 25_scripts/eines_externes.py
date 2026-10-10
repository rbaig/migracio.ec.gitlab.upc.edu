#!/usr/bin/env python3
"""On es guarden les eines que el projecte fa servir i no versiona: RARS i LanguageTool.

Al directori `.cache/` de l'arrel del clon, que git ignora (`.gitignore`), i
no a cap directori de la màquina fora del clon: el projecte se'n porta tot el
que necessita, i cada eina es baixa un sol cop. Totes les còpies de treball
d'un mateix clon (els *worktrees* de `git worktree add`) comparteixen el
`.cache/` del clon principal, que és el pare del directori de git comú. Les
variables d'entorn de cada eina (RARS_JAR, LANGUAGETOOL_DIR) hi passen al
davant: són la manera de fer servir una còpia que ja és al sistema (D-62).

Ús, des d'un altre script de 25_scripts:
    import eines_externes
    cau = eines_externes.directori()      # Path('<clon>/.cache'), sense crear-lo

Executat sol, escriu el directori.
"""

import subprocess
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent


def directori():
    """El `.cache/` de l'arrel del clon principal (el de qualsevol worktree, el mateix)."""
    try:
        comu = subprocess.run(['git', '-C', str(ARREL), 'rev-parse', '--path-format=absolute',
                               '--git-common-dir'], capture_output=True, text=True, check=True).stdout.strip()
        return Path(comu).parent / '.cache'
    except (OSError, subprocess.CalledProcessError):
        return ARREL / '.cache'                                      # sense git: el del directori mateix


if __name__ == '__main__':
    print(directori())
