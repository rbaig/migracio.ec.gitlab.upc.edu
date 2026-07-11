# Tasca per a Claude Code: unificació notacional `=` → `\leftarrow` a `11_riscv/`

## Context

Projecte EC (Estructura de Computadors, FIB-UPC). Llibre Quarto amb fitxers `.qmd`. Llegeix primer
`CLAUDE.md` i `07_contrib.qmd` (arrel del projecte) per al context general de convencions.

## Objectiu

Unificar la notació de les operacions RTL (*register transfer level*) a totes les taules
d'instruccions de `11_riscv/`: el símbol d'**assignació** (transferència de valor a un registre o
posició de memòria) ha de ser sempre `\leftarrow`, mai `=`. El símbol `=` es reserva exclusivament
per a la **comparació d'igualtat** (mai per a assignació).

A més, unificar `off` → `offset` (sencer, sense abreujar) allà on aparegui com a nom de camp/operand,
per coherència amb la resta del projecte (`07_contrib.qmd` estableix `offset` sencer com a terme
normatiu quan apareix com a operand o nom de camp en fórmules RTL i codi).

## Abast — fitxers i canvis exactes

**Ja corregits (NO tocar)**, ja usen `\leftarrow` correctament:
- `RV32F_instruccions_carrega_emmagatzemament.qmd` (`flw`/`fsw`) — **però aquí cal encara canviar
  `off` → `offset`** (2 ocurrències: `rd, off(rs1)` → `rd, offset(rs1)`; i dins les fórmules
  `SignExt(off)` → `SignExt(offset)`).
- `RV32F_instruccions_moviment_bits.qmd` (`fmv.w.x`, `fmv.x.w`) — ja usa `\leftarrow`, sense `off`, no
  cal tocar.

**A canviar (`=` d'assignació → `\leftarrow`)**:

1. `RV32F_instruccions_aritmetiques.qmd` (7 ocurrències): `fadd.s`, `fsub.s`, `fmul.s`, `fdiv.s`,
   `fsqrt.s`, `fmin.s`, `fmax.s`. Tots els `$rd = ...$` són assignacions → `$rd \leftarrow ...$`.
2. `RV32F_instruccions_comparacio.qmd` (3 ocurrències): `feq.s`, `flt.s`, `fle.s`. **Atenció**: aquí
   cada fórmula té DOS símbols `=`: el de dins del parèntesi és comparació (`rs1 = rs2` → es manté
   `=`), el de fora és assignació (`rd = (...)  ?  1 : 0` → `rd \leftarrow (...) ? 1 : 0`). Exemple
   concret: `$rd = (rs1 = rs2)\ ?\ 1 : 0$` → `$rd \leftarrow (rs1 = rs2)\ ?\ 1 : 0$` (només canvia el
   primer `=`, el de dins del parèntesi es queda igual perquè és una comparació real).
3. `RV32F_instruccions_conversio.qmd` (4 ocurrències): `fcvt.s.w`, `fcvt.s.wu`, `fcvt.w.s`,
   `fcvt.wu.s`. Tots `$rd = (float)\ rs1$` etc. → `$rd \leftarrow (float)\ rs1$` etc.
4. `RV32F_instruccions_moviment.qmd` (1 ocurrència): `fmv.s`. `$rd = rs1$` → `$rd \leftarrow rs1$`.

**Fora d'abast d'aquesta tasca (NO tocar ara)**: els fitxers `RV32I_*.qmd` i `RV32M_*.qmd` que
també usen `=` d'assignació (`RV32I_instruccions_comparacio.qmd`,
`RV32I_instruccions_desplacament_bits_aritmetics.qmd`,
`RV32I_instruccions_desplacament_bits_logics.qmd`, `RV32I_instruccions_lectura_escriptura.qmd`,
`RV32I_instruccions_logiques_bit_a_bit.qmd`, `RV32I_instruccions_salt_incondicional.qmd`,
`RV32I_instruccions_salt_incondicional_indirecte.qmd`, `RV32I_pseudo_mv.qmd`). Aquesta ampliació a
RV32I es farà en una tasca separada perquè aquests fitxers s'inclouen també des de T2/T3/T4/T9, que
requereixen revisió pròpia abans de tocar-los. **Confirma-ho amb l'usuari abans de tocar cap
d'aquests fitxers, encara que et sembli una extensió natural de la tasca.**

## Verificació abans de fer canvis

Per a cada fitxer de la llista "A canviar", `grep` primer totes les ocurrències de `= ` per
distingir manualment assignació de comparació (el cas de `RV32F_instruccions_comparacio.qmd` és el
més delicat: NO canviïs el `=` intern d'una comparació d'igualtat).

## Després dels canvis

1. Comprova que `05_riscv.qmd` (que inclou aquests mateixos fitxers via `{{< include >}}`) es
   renderitza sense error (`quarto render --to html`).
2. Comprova visualment que `T5.qmd` (que també inclou aquests fitxers a les seccions
   `#nte-instruccions-*-f`) mostra les fórmules correctament.
3. **Actualitza `TODO.md` §T5**: elimina l'entrada "Harmonització notacional RV32I ↔ RV32F" un cop
   fet, ja que quedarà resolta pel que fa a RV32F (la unificació amb RV32I resta pendent com a nova
   entrada, vegeu punt següent).
4. **Afegeix una entrada nova a `TODO.md`** (secció "Tasques globals" o una secció nova, no dins de
   §T5 perquè afecta transversalment T2/T3/T4/T9): "Unificar notació RTL `=`→`\leftarrow` també a
   RV32I/RV32M (`RV32I_instruccions_comparacio.qmd`,
   `RV32I_instruccions_desplacament_bits_aritmetics.qmd`,
   `RV32I_instruccions_desplacament_bits_logics.qmd`, `RV32I_instruccions_lectura_escriptura.qmd`,
   `RV32I_instruccions_logiques_bit_a_bit.qmd`, `RV32I_instruccions_salt_incondicional.qmd`,
   `RV32I_instruccions_salt_incondicional_indirecte.qmd`, `RV32I_pseudo_mv.qmd`; 8 fitxers, ~27
   ocurrències). Afecta T2/T3/T4/T9: cal fer-ho en un xat propi de revisió d'aquests temes, no com a
   tasca operativa aïllada, perquè pot requerir revisar la coherència de cada fórmula amb el seu
   context narratiu."
5. **No toquis res més**: cap canvi de contingut tècnic, només notació.

## Recorda

- Fes només canvis locals (Claude Code no actualitza el repositori remot).
- Un cop acabat, informa quins fitxers has modificat.
