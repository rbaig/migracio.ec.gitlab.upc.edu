#!/usr/bin/env python3
"""comprova_vores.py — Vores que depenen de l'ordre de dibuix (`24_specs/svg.md §7`, D-99).

Un `<rect>` dibuixat després tapa part del traç d'un d'anterior: amb el farciment,
o amb un traç d'un altre color que s'hi sobreposa. És el que `vores_compartides()`
(`figlib.py`) evita a les zones que es toquen, i el que la mesura geomètrica de la
fase 7h no veia (els ressalts sense farciment dibuixats abans de la fila següent).

No compten com a conflicte:
  - un rect que en tapa un altre sencer (una cel·la que en substitueix una altra);
  - un rect dibuixat a sobre d'un contenidor, a dins (el contingut d'una columna);
  - un farciment posterior que només tapa la part del traç que el seu propi traç,
    igual o més gruixut, torna a dibuixar.

Revisa els SVG del llibre: els de `22_figs_originals/` (natius i de model (a); no
els de `conservats/`, D-68) i els que generen `gen_regs.py` i `gen_MC.py`, que
escriu en un directori temporal.

Ús:
    python3 25_scripts/comprova_vores.py            # surt amb 1 si en troba
    python3 25_scripts/comprova_vores.py -v         # amb els parells de cada figura
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
E = 1e-3
VISIBLE = 0.1                       # px: un solapament més prim no es veu


def rects(text):
    for m in re.finditer(r'<rect\b([^>]*)>', text):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        if 'transform' in a or not all(k in a for k in ('x', 'y', 'width', 'height')):
            continue
        s = a.get('stroke', 'none').lower()
        yield (float(a['x']), float(a['y']), float(a['width']), float(a['height']),
               s, float(a.get('stroke-width', '1')) if s != 'none' else 0, a.get('fill', '#000').lower())


def banda(r):
    """Les quatre franges del traç d'un rect, centrat a la vora."""
    x, y, w, h, _, sw, _ = r
    e = sw / 2
    return [(x - e, y - e, w + sw, sw), (x - e, y + h - e, w + sw, sw), (x - e, y - e, sw, h + sw), (x + w - e, y - e, sw, h + sw)]


def inter(p, q):
    return (min(p[0] + p[2], q[0] + q[2]) - max(p[0], q[0]) > VISIBLE
            and min(p[1] + p[3], q[1] + q[3]) - max(p[1], q[1]) > VISIBLE)


def dins(q, r):
    return (q[0] >= r[0] - E and q[1] >= r[1] - E and q[0] + q[2] <= r[0] + r[2] + E and q[1] + q[3] <= r[1] + r[3] + E)


def tall(p, q):
    x, y = max(p[0], q[0]), max(p[1], q[1])
    return x, y, min(p[0] + p[2], q[0] + q[2]) - x, min(p[1] + p[3], q[1] + q[3]) - y


def ple(r):
    return r[6] not in ('none', 'transparent')


def conflicte(a, b):
    """a, dibuixat abans que b: b en tapa part del traç?"""
    if a[4] == 'none' or dins(a[:4], b[:4]) or dins(b[:4], a[:4]):
        return False
    if ple(b):
        for p in banda(a):
            if inter(p, b[:4]):
                q = tall(p, b[:4])
                if not (b[4] != 'none' and b[5] >= a[5] and any(dins(q, r) for r in banda(b))):
                    return True
        if b[4] not in ('none', a[4]) and any(inter(p, q) for p in banda(a) for q in banda(b)):
            return True
    return False


def revisa(fitxer):
    R = list(rects(Path(fitxer).read_text(encoding='utf-8')))
    return [(a, b) for i, a in enumerate(R) for b in R[i + 1:] if conflicte(a, b)]


def main():
    verb = '-v' in sys.argv[1:]
    fitxers = sorted(p for p in (ARREL / '22_figs_originals').glob('*.svg'))
    with tempfile.TemporaryDirectory() as tmp:
        for gen, toml, suf in (('gen_regs.py', 'registres.toml', '__registre_light'), ('gen_MC.py', 'MC.toml', '__MC_light')):
            args = [sys.executable, str(ARREL / '25_scripts' / gen), str(ARREL / '24_specs' / toml), suf, f'--output-dir={tmp}/']
            if gen == 'gen_regs.py':
                args += ['--force', '--verbosity', '0']
            subprocess.run(args, cwd=ARREL, check=True, capture_output=True)
        fitxers += sorted(Path(tmp).glob('*.svg'))
        trobades = [(f, revisa(f)) for f in fitxers]
        trobades = [(f, c) for f, c in trobades if c]
        for f, c in trobades:
            print(f'[vores] {f.name}: {len(c)} traç tapat per un rect posterior (svg.md §7)')
            if verb:
                for a, b in c:
                    print(f'    {a}\n  → {b}')
    if trobades:
        print(f'[vores] {len(trobades)} figures; vegeu `vores_compartides()` de figlib.py (D-99)')
    return 1 if trobades else 0


if __name__ == '__main__':
    sys.exit(main())
