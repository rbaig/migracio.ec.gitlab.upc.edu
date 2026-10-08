#!/usr/bin/env python3
"""Comprovacions mecàniques del calendari del laboratori (04_laboratori/Lcalendari.qmd).

El calendari canvia cada quadrimestre i s'escriu a mà; aquest script en mira el que
es pot mirar sense judici (fase 7g, 2026-10-08; 13_contrib.qmd §IAs):

  1. El quadrimestre: la línia «**Quadrimestre <primavera|tardor> AAAA-BB**» hi és i
     en dona l'any de les dates (primavera: 20BB; tardor: AAAA).
  2. Cada data (DD/MM) cau en el dia de la setmana de la columna «Dia».
  3. Les columnes de sessió remeten, en ordre, a les seccions #sec-sessio-* de
     L1.qmd–L6.qmd, i n'hi ha tantes com sessions de laboratori a _quarto.yml.
  4. Dins de cada fila, les dates són creixents.

El que demana judici (festius, si el quadrimestre és el vigent, l'examen) és feina de
l'agent verificador-calendari (.claude/agents/), que fa servir aquest script.

Ús:
    python3 25_scripts/verifica_calendari.py     # surt amb 1 si troba res
"""

import datetime
import re
import sys
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
CALENDARI = ARREL / "04_laboratori" / "Lcalendari.qmd"
DIES = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]


def sessions_del_laboratori():
    """Els identificadors #sec-sessio-* de L1.qmd–L6.qmd, en l'ordre dels chapters."""
    quarto = (ARREL / "_quarto.yml").read_text(encoding="utf-8")
    fitxers = re.findall(r"^\s+file:\s+(04_laboratori/L\d+\.qmd)", quarto, re.M)
    ids = []
    for f in fitxers:
        m = re.search(r"\{#(sec-sessio-[\w-]+)\}", (ARREL / f).read_text(encoding="utf-8"))
        ids.append(m.group(1) if m else f"(cap #sec-sessio- a {f})")
    return ids


def main():
    text = CALENDARI.read_text(encoding="utf-8")
    errors = []

    m = re.search(r"\*\*Quadrimestre (primavera|tardor) (\d{4})-(\d{2})\*\*", text)
    if not m:
        print("✗ No hi ha la línia «**Quadrimestre <primavera|tardor> AAAA-BB**».")
        return 1
    estacio, any1, any2 = m.group(1), int(m.group(2)), 2000 + int(m.group(3))
    if any2 != any1 + 1:
        errors.append(f"curs {any1}-{m.group(3)}: el segon any no és el següent del primer")
    any_dates = any2 if estacio == "primavera" else any1

    files = [l for l in text.split("\n") if l.startswith("|")]
    capcalera = [c.strip() for c in files[0].strip("|").split("|")]
    sessions = [re.search(r"\(#([\w-]+)\)", c).group(1) for c in capcalera if re.search(r"\(#sec-sessio-", c)]
    esperades = sessions_del_laboratori()
    if sessions != esperades:
        errors.append(f"columnes de sessió {sessions} ≠ seccions de L1–L6 {esperades}")

    try:
        col_dia = capcalera.index("Dia")
    except ValueError:
        print("✗ La taula no té cap columna «Dia».")
        return 1

    for fila in files[2:]:
        if fila.startswith("|:") or fila.startswith("| :"):
            continue
        cel = [c.strip() for c in fila.strip("|").split("|")]
        dia = cel[col_dia]
        if dia not in DIES:
            errors.append(f"fila «{cel[0]}»: dia «{dia}» desconegut")
            continue
        anteriors = []
        for c in cel[col_dia + 1:]:
            d = re.search(r"(\d{2})/(\d{2})", c)
            if not d:
                continue
            data = datetime.date(any_dates, int(d.group(2)), int(d.group(1)))
            real = DIES[data.weekday()]
            if real != dia:
                errors.append(f"fila «{cel[0]}»: {d.group(0)}/{any_dates} és {real.lower()}, no {dia.lower()}")
            if anteriors and data <= anteriors[-1]:
                errors.append(f"fila «{cel[0]}»: {d.group(0)} no és posterior a la data anterior")
            anteriors.append(data)

    print(f"Quadrimestre de {estacio} {any1}-{m.group(3)}: dates de {any_dates}, "
          f"{len(sessions)} sessions, {len(files) - 2} files.")
    for e in errors:
        print(f"✗ {e}")
    if not errors:
        print("✓ Cap discrepància mecànica.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
