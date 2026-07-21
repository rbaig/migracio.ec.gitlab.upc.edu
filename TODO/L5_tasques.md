# L5 — Registre de tasques de la revisió interna

Data: 2026-07-20.

# Estat

- **Fase A (exploració i comprensió): completada.** Mapa validat per l'usuari.
- **Fase B (verificació numèrica dirigida i anàlisi profund): completada.** Verificació amb aritmètica exacta (Python, `fractions`) i simulació RV32I dels tres programes (100 010 casos de prova per a `descompon`, asm ≡ C confirmat).
- **Fase C (execució): completada.** Els 22 ítems [D] i els 2 ítems [U] (decisions de l'usuari) aplicats a `L5.qmd`.
- **Pendent**: revisió final en 3 passades (contrast tècnic amb la font de veritat RISC-V International, comparació didàctica L4→L5→L6, passada lingüística dedicada), a fer en un xat separat (`EC L5 Revisió final (3 passades)`), configuració Fable 5 High amb Thinking.

# Correccions aplicades (Fase C)

## A. Errors numèrics (crítics)

1. Taula de casos límit §5.3: `cfixa` corregit a `0x0000CC00` (coherent amb $12{,}75$ i `0x414C0000`).
2. Traça de `#sol-precisio` P2 (`cfixa = 0x7FFFFFFF`): `t0`/`mantissa`/`cflotant` corregits de `…FE` a `…FF` (`srli 0xFFFFFFFE >> 8 = 0x00FFFFFF`).
3. Frase dels bits descartats a P2 reformulada en coherència amb la correcció núm. 2.

## B. Errors conceptuals i pedagògics

4. «bit 13 és ara el primer bit fraccionari» → bit 12.
5. Lectura prèvia: `slt` reclassificat com a «operacions lògiques bit a bit i de comparació».
6. `#exr-descompon` punt 2: `cf` ja no apareix duplicat com a variable local i paràmetre.
7. `#sol-descompon` Pas 3: «sense variables locals» → «totes les variables s'assignen a registres».

## C. Decisió d'usuari — tipus C de `compon`/`cflotant` (ítem 8)

**Opció aplicada: (a)** — `compon` i `cflotant` canviats de `float` a `int` a `main.c` i `compon.c`, amb frase afegida aclarint que el valor és el patró de bits IEEE 754, no un nombre a convertir.

## D. Harmonització

9. «IEEE-754» → «IEEE 754» (9 ocurrències).
10. «IEEE-754 SP» → «IEEE 754 de simple precisió» (3 ocurrències; sigla SP no introduïda ni al glossari).
11. Elements d'UI de RARS: negreta → cursiva (6 línies), coherent amb L1 i `13_contrib.qmd`.
12. «arrodoniment cap a zero» → «arrodoniment a zero» (nom del mode a @sec-arrodoniment d'A5); eliminada repetició de «truncament» i doble espai.

## E. Millores menors d'estil

13. Dobles parèntesis eliminats (exponent esbiaixat amb biaix 127).
14. Redundància eliminada a `#sol-compilacio-separada`.
15. `#sol-descompon` Pas 2: fila `@s`/`@e`/`@m` precisada («paràmetres: adreces de destinació dels resultats»).

## F. Decisió d'usuari — condició exacta de pèrdua de precisió, P1 (ítem 16)

**Opció aplicada**: condició exacta afegida (substituint/complementant l'explicació qualitativa): pèrdua de precisió ⟺ distància entre el bit `1` més alt i el més baix de la magnitud ≥ 25. Verificada empíricament en 200 000 casos aleatoris (0 discrepàncies).

# Verificacions superades (constància)

- Traça `0x87D18A00 → 0xC6FA3140`; casos límit `0x00000000`, `0x80000000`.
- Equivalència assemblador ≡ C de `descompon` en 100 010 casos simulats; `compon` i `abs` correctes.
- P5: màxim de coma fixa $= 2^{19}-2^{-12}$ exacte.
- Comentari `srli` vs. `srai` de `#sol-descompon`: correcte.
- 17 àncores de referència creuada (A5, A3) resolen; cap col·lisió.
- Convencions de laboratori (sortida, `.data`/`.text`, callouts, BA múltiples de 4, veu, `neg`/`beqz` ja introduïts abans de L5): totes conformes.

# Fitxer final

`04_laboratori/L5.qmd` — versió amb els 24 canvis aplicats (blocs Quarto verificats equilibrats).
