---
title: "L1 — Registre de tasques de la revisió interna"
date: 2026-07-13
---

<!-- Fitxer transitori: s'esborra en tancar la revisió interna de L1. -->

# Estat

- **Fase A (exploració i comprensió): completada** (2026-07-13). Mapa validat per l'usuari.
- **Fase B (verificació numèrica dirigida i anàlisi profund): completada** (2026-07-13).
- **Fase C (execució): completada** (2026-07-13). Totes les tasques (T1–T7, T9) fetes. T8 eliminada (ja resolta manualment per l'usuari a L3.qmd).

Decisió de l'usuari ja presa: **L1 ha de tenir blocs `{#sol-...}`** per als 7 exercicis (vegeu T1).

# Context (per a represa en xat nou)

- Fitxer principal: `04_laboratori/L1.qmd` (316 línies, sense figures SVG). Repositori: `raw.githubusercontent.com/rbaig/migracio.ec.gitlab.upc.edu/main/`.
- Fitxers de referència llegits: `CLAUDE.md`, `13_contrib.qmd`, `24_specs/svg.md`, `index.qmd`, `_quarto.yml`, `_variables.yml`, `A2.qmd`, `A9.qmd`, `L2.qmd`–`L6.qmd`, `11_riscv.qmd`. Font de veritat del simulador: codi font de RARS v1.6 (`github.com/TheThirdOne/rars`, tag `v1.6`).
- Estructura de L1: `# {{< var sessio1 >}} {#sec-sessio-introduccio}` → `### Lliuraments {.unnumbered}` i `### Lectura prèvia {.unnumbered}` (H3 pel *dirty hack* de la capçalera PDF) → 5 seccions: 1. El primer programa (sense `{#sec-}`); 2. Exploració del simulador `{#sec-rars-exploracio}` (exr `s1_2_1`, `s1_2_2`); 3. Execució i inspecció `{#sec-rars-execucio}` (exr `s1_3_1`, `s1_3_2`); 4. Punts d'aturada `{#sec-rars-breakpoints}` (exr `s1_4_1`); 5. Depuració `{#sec-rars-depuracio}` (exr `s1_5_1`, `s1_5_2`).
- Referències creuades sortints verificades: `@imp-codi-format-criteris` (A2), `@nte-programa-esquelet` (A2; el duplicat és en bloc comentat), `@sec-ei-ecall` (A9), `#sec-presentacio-eines-rars` (index.qmd, enllaç trencat — T2).
- Coherent amb la decisió viva **sense `startup.s`** (`_start` + syscall 93); els blocs `startup.s` d'A2/index estan comentats.
- Patró dels blocs de solució als altres labs (L2–L6, tots en tenen; L1 és l'únic sense): `::: {#sol-nom}` immediatament després del `{#exr-nom}` corresponent (separats per `---`), **sense capçalera pròpia**, amb codi (`filename="sN_S_E.s"`) i/o explicació; «Comprovació pràctica» com a `{.callout-tip title="Comprovació pràctica"}` dins el `{#sol-}` quan escau.

# Resultats de la verificació (Fase B) — tot verificat correcte llevat de V1

Verificació feta amb simulació Python i contra el codi font de RARS v1.6.

- **`hola.s`**: correcte. S'executen **7 instruccions reals** (6 línies font): `la a0, msg` → `auipc a0, 0xfc10` + `addi a0, a0, 0` (PC-relatiu; `msg` = 0x10010000, `la` a PC = 0x00400000); després `addi a7` (li), `ecall`, `addi a7`, `addi a0`, `ecall`.
- **Expansions** (RARS `PseudoOps.txt`): `la` → `auipc` + `addi` (sempre 2); `li` amb imm ∈ [−2048, 2047] → `addi` (1); `li` gran → `lui` + `addi` (2). `li t2, 100000` → `lui t2, 0x18` + `addi t2, t2, 1696` (98304 + 1696 = 100000). ✓ Indicació del rang −2048..2047 a `s1_2_2` correcta.
- **`suma.s`**: correcte; `t0` final = **−55**. `la t3, V` (a PC = 0x0040000C) → `auipc t3, 0xfc10` + `addi t3, t3, −12`. Breakpoint a `add t0, t0, t4`: 10 aturades; 1a aturada = iteració 1 amb `t0` = 0 i `t4` = −1 (el `lw` ja s'ha executat); `t4` pren −1..−10 en ordre.
- **`s1_3_2`**: `V` comença a **0x10010000** (`.data` per defecte de RARS); `V[3]` a **0x1001000C** = **0xFFFFFFFC** (−4); `V[0]` = **0xFFFFFFFF** (complement a 2 de −1); RV32I és **little-endian**. Enunciats correctes.
- **`s1_5_1`**: únic error = `li t1, 9` (hauria de ser `li t1, 0`); resta idèntic a `suma.s` (sense comentaris — vegeu T7d). Resultat erroni: només s'acumula `V[9]` ⇒ `t0` = **−10**. El comportament incorrecte és observable des de la **1a iteració** (`slli` dona 36; `lw` carrega −10). Correcció d'una línia ⇒ −55. ✓
- **`s1_5_2`**: únic error = `sub t0, t6, t0` (hauria de ser `sub t0, t0, t6`). Primera fase: `t0` = 55 (suma 1..10) ✓ (punt b: a l'aturada sobre `blt`, `t0` = 55, `t6` = 10 ✓). Amb error: 10 − 55 = **−45** després del `sub` (punt c ✓); −45 < 10 ⇒ surt amb `t5` = **1**. Corregit: 55→45→35→25→15→5; surt amb `t5` = **5**, `t0` final = 5. Enunciat coherent (⌊55/10⌋ = 5). ✓
- **Interfície RARS (v1.6, codi font)**: PC **sí** que apareix al panell de registres (fila `pc`, `RegistersWindow`). Dreceres: Assemble = F3, Go = F5, Step = F7, Reset = F12 (Backstep = F8) ✓. Syscalls: `PrintInt` = 1, `PrintString` = 4, `Exit` = 10, `Exit2` = 93 ✓ (taula de L1 i A9 correctes). Columnes del panell de codi: Bkpt, Address, Code, Basic, Source — coherent amb «tres columnes de valors» + casella de breakpoint (la columna Source també hi és; matís per a la solució de `s1_2_1` c).
- **V1 — ÚNIC PROBLEMA TÈCNIC DETECTAT**: RARS **no** mostra automàticament el nombre d'instruccions executades. Cal l'eina **Tools → Instruction Counter**, oberta i amb *Connect to Program* **abans** d'executar. Afecta `s1_2_1` b) («On es mostra el nombre d'instruccions executades...») i `s1_3_1` a)/c) («Quin nombre... reporta RARS?»). Vegeu T9.

# Tasques

Prioritat: A = executar a la Fase C sense aprovació addicional; B = requereix decisió de l'usuari (presentar opcions al final de la Fase C); C = harmonització fora de L1.

## T1 (A, contingut validat) — Redactar els 7 blocs `{#sol-...}` de L1

Seguir el patró de L2–L6 (vegeu §Context). Contingut verificat per a cada solució:

- `#sol-rars-panells` (`s1_2_1`): a) fila `pc` del panell de registres; b) **depèn de T9** (eina Instruction Counter); c) Address (adreça), Code (codificació en hexadecimal), Basic (instrucció real descodificada, amb registres `x`); esmentar que també hi ha la casella de breakpoint i la columna Source (línia font).
- `#sol-rars-pseudoinstruccio` (`s1_2_2`): a) `auipc t3, 0xfc10` + `addi t3, t3, -12` (mostrats amb `x28` al panell); b) una adreça de 32 bits no cap a l'immediat de 12 bits: `auipc` aporta els 20 bits alts relatius al PC i `addi` els 12 baixos; c) 10 ∈ [−2048, 2047] ⇒ 1 sola `addi`; 100000 no hi cap ⇒ `lui` + `addi` (2 instruccions).
- `#sol-recompte-instruccions` (`s1_3_1`): a) **depèn de T9**; b) llista de 7 instruccions reals (la→2: `auipc`+`addi`; `li a7,4`→1; `ecall`; `li a7,93`→1; `li a0,0`→1; `ecall`); c) coincideixen (7 = 7); la discrepància amb el recompte de línies font (6) l'explica l'expansió de `la`.
- `#sol-rars-memoria` (`s1_3_2`): a) 0x10010000; b) 0x1001000C, 0xFFFFFFFC; c) 0xFFFFFFFF, complement a 2 (2³² − 1); d) little-endian (el byte de menys pes a l'adreça més baixa).
- `#sol-rars-breakpoints` (`s1_4_1`): a) 1a iteració, `t0` = 0, `t4` = −1; b) `t4` = −1, −2, ..., −10 (10 aturades); c) `t0` = −55 = Σ(−1..−10). Afegir «Comprovació pràctica».
- `#sol-depuracio-pas-a-pas` (`s1_5_1`): error = `li t1, 9`; `t0` erroni = −10 (només V[9]); incorrecte des de la 1a iteració; correcció `li t1, 0` ⇒ −55.
- `#sol-depuracio-breakpoints` (`s1_5_2`): error = `sub t0, t6, t0` (operands invertits); a l'aturada `t0` = 55, `t6` = 10; després del `sub`, `t0` = −45 (confirma el diagnòstic); correcció `sub t0, t0, t6` ⇒ `t5` = 5.

## T2 (A) — Corregir l'enllaç trencat a la Lectura prèvia

`[Presentació del curs](#sec-presentacio-eines-rars)` → enllaç amb camí relatiu (`[Presentació del curs](../index.qmd#sec-presentacio-eines-rars)`). No usar `@sec-`: les capçaleres d'`index.qmd` no són numerades i renderitzaria «??».

## T3 (A) — Afegir `{#sec-}` a `## El primer programa`

Proposta: `{#sec-rars-primer-programa}`.

## T4 (C) — Contradiccions internes de `13_contrib.qmd` §Convencions globals del laboratori

a) «**Lliurament**: última secció» → corregir (la pràctica real i l'«ordre fix» és al principi: Lliuraments, després Lectura prèvia).
b) «Directiva `.global _start`» → «`.globl _start`» (coherent amb §`.globl` vs. `.global`).
c) «(syscall `exit`)» per al codi 93 → «(syscall `exit2`)» (10 = `exit`, segons A9 i RARS).
d) Documentar el *dirty hack* H3 (`###` en lloc de `##` per a Lliuraments/Lectura prèvia, per la capçalera de pàgina del PDF).

## T5 (C) — `A2.qmd`, callout viu `#nte-programa-esquelet`

Comentari `# syscall 93: exit` → `# syscall 93: exit2`.

## T6 (A) — Correccions lingüístiques i d'estil a L1

a) `s1_5_2` e): «com la heu corregit» → «com **l'heu** corregit».
b) `s1_5_2` a): «**Quin** hauria de fer la instrucció errònia?» → «**Què** hauria de fer la instrucció errònia?».
c) «Les syscall s'estudien» i «la sortida de les syscall» → plural «**syscalls**» (2 ocurrències; A9 usa «crides al sistema» en prosa, però L1 ja ha definit el terme «syscall» al mateix callout).
d) «Quin és el valor de `t0` i `t4`» (`s1_4_1` a) → «**Quins són els valors** de `t0` i `t4`».
e) «el punt d'aturada s'atura just abans» (`s1_4_1` a) → «**l'execució** s'atura just abans» (qui s'atura és l'execució).
f) `s1_5_2` c): «Confirma el vostre diagnòstic del punt a)?» → «**Es confirma** el diagnòstic del punt a)?» (o «Aquest valor confirma...?»).
g) «El programa següent és el mínim executable a RARS» → «és el **programa mínim** executable a RARS».
h) «Número de servei» (text del callout i capçalera de la taula de syscalls) → «**codi de servei**» (terme d'A9), 2 ocurrències.
i) «cal haver instal·lat **i configurat** RARS» → «cal haver instal·lat RARS» (el pas de configuració — `startup.s` — està desactivat a `index.qmd`).

## T7 (fet) — Millores tècniques/pedagògiques

a) Rang de paràmetres: `a0`–`a2` (explícit).
b) Panell de memòria: reformulat («cada word com a valor hexadecimal»).
c) *Backstep* (F8) afegit al pas 4 del procediment de depuració.
d) Comentaris de codi: deixats tal qual (recomanat, mantingut).
e) Lectura prèvia: afegida fila amb referència a @sec-acces-paraula-lw-sw (A2), @sec-desplacaments-logics i @sec-salts-condicionals (A3).
f) Noms reals de finestres RARS afegits als 4 panells (*Text Segment*, *Registers*, *Data Segment*, *Run I/O*).

## T9 (B, **decisió prèvia a T1**) — Recompte d'instruccions: RARS no el mostra automàticament

Verificat al codi font: el recompte és l'eina **Tools → Instruction Counter** (cal obrir-la i prémer *Connect to Program* abans d'executar; F12 no la reinicia, cal *Reset* de l'eina). Tal com estan redactats, `s1_2_1` b) i `s1_3_1` a)/c) suposen que RARS «reporta» el nombre d'instruccions. Opcions:

1. **Adaptar els enunciats a l'eina** (recomanada): a `s1_2_1` b) preguntar «Amb quina eina de RARS es pot comptar el nombre d'instruccions executades?» (resposta: Tools → Instruction Counter) i a `s1_3_1` a) afegir la instrucció d'obrir i connectar l'eina abans d'executar.
2. **Eliminar la dependència**: reformular `s1_2_1` b) i `s1_3_1` a) perquè el recompte sigui només manual (pas a pas amb F7), i c) es reformula o s'elimina.
3. Una altra formulació que proposi l'usuari.

# Ordre d'execució proposat per a la Fase C

1. Resoldre T9 amb l'usuari (condiciona T1).
2. T6, T2, T3 (canvis directes a L1).
3. T1 (redacció de solucions amb els valors verificats).
4. T4, T5 (fitxers externs: `13_contrib.qmd`, `A2.qmd`).
5. Presentar la llista B pendent (T7, i T9 si no s'ha resolt) amb opcions.
