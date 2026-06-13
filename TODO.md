# TODO

## Contingut

- "" -> «»
- Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir
- Lab: Decidir si Estudi previ és els fitxers 
- **T1**: Indicar explícitament que RISC-V és l'ISA de referència a EC.
- **T2**: Introduir el concepte de directiva al cos del text (ara només és a `#cau-directives`). Decidir si les directives es presenten com a part de RISC-V, de RARS o d'assemblador en general.
- eliminar els ****:
- afegir que s'ha elaborat amb Quarto i Claude
- captions contrast de `code`
- Decidir si `startup.s` (Roger: Fora i obligar `li a0, 0` + syscall `93`)
- Decidir si 2 registres de retorn `a1` (Roger: Sí)
- Pseudoinstruccions: Totes a taula estàndard:
- PDF ancoratge de les seccions`{.unnumbered}`: <!-- Esmena del problema clàssic de hyperref amb seccions no numerades ({.unnumbered}). Per a \section*{}, Pandoc genera \addcontentsline però sense \phantomsection previ, de manera que el marcador del PDF (outline) s'ancora a la pàgina anterior en lloc de la de la secció. L'índex (TOC) queda bé perquè el seu hipervincle apunta a l'àncora \hypertarget, però el marcador de l'outline s'ancora en el punt on es crida \addcontentsline. -->
```{=latex}
\phantomsection
```

```
::: {#nte-pseudoinstruccions-neg .callout-note}
## RV32I ISA — Instruccions de desplaçament lògic
| Mnemònic | Operands | Operació | Nom | Expansió |
| :--- | :--- | :--- | :--- | :---: |
| `neg` | `rd, rs` | `rd` ← -`rs` | *Negate* | `sub rd, x0, rs` |
: {tbl-colwidths="[5,20,35,35,5]"}
:::
```

## Criteris pendents de documentar a `contrib.qmd`

- **Adreces de memòria**: `0x00000000` o `0x0000 0000` (amb espai cada 4 nibbles)?
- **Directives**: quin títol de callout? `## Directives —` o `## RARS —`?
- **`.globl` vs `.global`**: quin usar als exemples?
- **`.section`**: usar o no? si sí, amb quin criteri?
- **ISA/ABI**: on posar la informació de l'ABI de RV? `{.callout-note}` amb `## RV32I ABI —`? `{.callout-important}` amb criteri EC? callout addicional?
- **Syntax highlighting**: confirmar que `.s` és correcte per a totes les instruccions, macros i directives de RARS.

## Quarto / Infraestructura

- **Error SVG en PDF (T3, T4)**:
```
Package svg Error: File `svg-5d875942584dea27_svg-tex.pdf' is missing.
```
- **Subtítol**: el subtítol HTML (`<br>`) vs. PDF (`\linebreak`) no es pot unificar a `_quarto.yml`; cal mantenir la solució actual per `format: pdf: header-includes`.
- **`README.md`**: actualitzar l'arbre de fitxers.
- **Laboratori**: decidir com mostrar el contingut de `laboratori/` per poder fer download (codi encastat per C&P vs. fitxers descarregables).