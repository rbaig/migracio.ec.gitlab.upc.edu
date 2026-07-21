# L5 — Registre de tasques de la revisió interna

Data: 2026-07-20.

# Estat

- **Fase A (exploració i comprensió): completada.** Mapa validat per l'usuari.
- **Fase B (verificació numèrica dirigida i anàlisi profund): completada.** Verificació amb aritmètica exacta (Python, `fractions`) i simulació RV32I dels tres programes (100 010 casos de prova per a `descompon`, asm ≡ C confirmat).
- **Fase C (execució): completada.** Els 22 ítems [D] i els 2 ítems [U] (decisions de l'usuari) aplicats a `L5.qmd`.
- **Revisió final en 3 passades: completada (2026-07-21)**, feta al xat `EC L5 Revisió final (3 passades)`. Vegeu detall més avall.

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

---

# Revisió final en 3 passades (2026-07-21)

Feta al xat `EC L5 Revisió final (3 passades)`, configuració Fable 5 High per a les passades d'anàlisi, Sonnet High sense Thinking per a l'execució de les decisions.

## Passada 1 — Contrast tècnic amb la font de veritat (RISC-V International)

Cap error trobat: totes les instruccions RV32I, pseudoinstruccions i directives usades a L5 verificades contra el manual oficial (`riscv-non-isa/riscv-asm-manual`) i el capítol RV32I (`riscv/riscv-isa-manual`). Verificació numèrica completa de la taula de casos límit i de les traces amb simulació Python exacta. 2 punts acumulats per a decisió (D1, D2).

## Passada 2 — Comparació didàctica L4→L5→L6

**Correcció crítica trobada i aplicada**: `s5_3_1.s` (programa complet) tenia `compon` definida abans de `_start` al `.text`; com que RARS sempre comença a executar la primera instrucció del `.text` combinat, el programa petava en executar-se i la Comprovació pràctica era irrealitzable. Reordenat (`_start` primer) i reverificat a RARS 1.6 amb els 5 valors de prova (`0x87D18A00`, `0x00000000`, `0x80000000`, `0x0000CC00`, `0x7FFFFFFF`): tots coincideixen amb els valors documentats. També restituïda la frase introductòria de «Lliuraments» (present a L1/L2/L3/L4/L6, absent només a L5). 4 punts acumulats per a decisió (D3–D6).

## Passada 3 — Lingüística dedicada

3 correccions aplicades: calc sintàctic «prou... com per»; terminologia fracció/mantissa harmonitzada amb la convenció del projecte (2 ocurrències). 3 punts acumulats per a decisió (D7–D9).

## Decisions D1–D9 (totes resoltes amb opció recomanada acceptada)

| # | Contingut | Resolució |
|---|---|---|
| D1 | Nota sobre `<<` en C estricte (P1 precisió) | Aplicada — nota inline |
| D2 | Notació mixta P2 precisió (`cf` vs. `t0`) | Aplicada — reescrita en termes de `cf`/`exp` |
| D3 | Callout `.globl _start` | Aplicada — regla general separada de la convenció d'entrada |
| D4 | Avís sobre l'arrencada de RARS | Aplicada — nou callout `#wrn-arrencada-rars` |
| D5 | Tipografia d'UI a L6 (negreta vs. cursiva) | Sense canvis a L5 — tasca afegida a `TODO/TODO.md` §Laboratori |
| D6 | `.eqv` per a constants IEEE 754 | Sense canvis — literals sense repetició, no calen |
| D7 | «el camí `bge` és cert per a zero» | Aplicada |
| D8 | «fent el rol combinat» | Aplicada — «assumint la funció combinada d'» |
| D9 | «la mantissa ja ocupa els bits 22–0» | Aplicada — «la fracció (paràmetre `mantissa`)» |

## Troballa addicional (post-revisió, arran de l'actualització del mirror amb la revisió de L4, 2026-07-21)

La revisió interna de L4 (commit `3cae913`) va confirmar independentment el mateix problema d'ordre de `_start` detectat a la Passada 2, i hi va afegir una convenció nova (decisió d'assignatura, 2026-07-19): `_start` no ha de tenir pròleg/epíleg (desar/restaurar `ra` i registres segurs és codi mort, ja que `_start` mai no torna a cap invocant), tot i que sí ha d'usar registres segurs per a dades que travessen crides. El `TODO.md` llistava L5 explícitament com a pendent en aquest punt.

**Aplicat als tres `_start` de L5** (exercici 1 `abs`, exercici 2 `descompon` sol, exercici 3 programa complet): eliminat el pròleg/epíleg (desat/restauració de `ra` i, a l'exercici 3, de `s0`–`s2`), mantenint l'ús dels registres segurs `s0`–`s2` a l'exercici 3 per a les dades que travessen les dues crides. Actualitzades en coherència les dues taules d'anàlisi de registres segurs i bloc d'activació que en depenien (exercici 1 i exercici 3), que altrament haurien quedat inconsistents amb el codi. Reverificat a RARS 1.6 als tres exercicis: execució correcta, valors coincidents amb els documentats.

`TODO/TODO.md` actualitzat en conseqüència: L5 ja no consta com a pendent en aquest punt (només queda L3). La regla encara no s'ha afegit a `13_contrib.qmd`, tal com indica el mateix TODO, perquè la consolidació de la convenció està supeditada a completar també la revisió de L3.

# Fitxer final (actualitzat)

`04_laboratori/L5.qmd` — versió amb els 24 canvis de la Fase C més les correccions de la revisió final en 3 passades (D1–D9) i la correcció del pròleg/epíleg de `_start` (blocs Quarto verificats equilibrats; 20/20 referències creuades resoltes).
