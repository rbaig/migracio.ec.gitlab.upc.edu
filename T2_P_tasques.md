# Tasques de revisió: T2.qmd, PE_T2.qmd, PS_T2.qmd

## Estat: COMPLETAT (xat `EC T2, PE_T2 i PS_T2 Revisió interna`)

Totes les tasques accionables han estat aplicades. Decisions D1–D13 resoltes.

---

## Tasques aplicades

### T2.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| T2-T12 | Taula little/big-endian invertida (error crític) | ✅ |
| T2-T2 | `0xFFFFF800` → `-2048` com a immediat d'`addi` | ✅ |
| T2-T3 | Coma incorrecta a la comanda GCC | ✅ |
| T2-T4 | `la`/`li` "macros" → "pseudoinstruccions" | ✅ |
| T2-T5 | `#wrn-punters-x86` afegit `collapse=true` | ✅ |
| T2-T6/7/8 | Espais i puntuació menors (`vec` es; l'opció; coma) | ✅ |
| T2-T9 | Etiqueta `{#sec-opt-acces-sequencial}` afegida | ✅ |
| T2-T10 | TODO octal eliminat (0101₈=65 ✓) | ✅ |
| T2-T11 | Nota `.byte` sense operands corregida + TODO eliminat | ✅ |
| T2-T13..T30 | 20+ cometes rectes → guillemets/cursiva | ✅ |
| T2-T24 | Redundància "modularitat" L.86 reformulada | ✅ |
| T2-T25 | `*data **type***` → `*data type*` | ✅ |
| T2-T26 | Caption afegit a `#tbl-tipus-alineacio` | ✅ |
| T2-T27 | Notació `lo~12~`/`hi~20~` → LaTeX | ✅ |
| T2-T28/29 | Format interior callout `#tip-codificacio-instruccions` | ✅ |
| D3 | «mode memòria» → «mode base+desplaçament»; callout `#cau-mode-base-desplacament` | ✅ |
| D13 | 4 títols `## RARS —` → `## Directives —` | ✅ |
| P1 | Nota mitigació ref. anticipada `@nte-registres-proposit-general` | ✅ |
| P4 | Macros mogudes al final de §Instruccions/pseudoinstruccions/macros | ✅ |

### PE_T2.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| PE-C1 | 36 blocs de codi amb `filename=` afegit | ✅ |
| PE-C6 | Nota `la+offset` + excepció d'alineació | ✅ |
| PE-C7 | Enunciat rang `addi` precisat | ✅ |
| PE-C8 | Columna «Excés» → «Excés a 7» | ✅ |
| PE-C9 | Format resultat `d3` especificat (binari natural) | ✅ |
| D7 | «bytes» → «byte ... a cada una de les adreces» | ✅ |
| Nou | Exercici `#exr-p3-memoria-lb-lh` afegit (lb/lh/lbu/lhu/sb) | ✅ |
| Reordre | «Constants i immediats» ara és la 2a secció (T2.qmd-consistent) | ✅ |
| Trasllat | Secció «Representació de naturals i enters» → PE_T1 (nota remissió) | ✅ |

### PS_T2.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| PS-C1 | Reformulació extensió de signe ($lo_{12} - \texttt{0x1000}$) | ✅ |
| PS-C2 | Comentari `# t2 = punter` → `# t2 = valor de punter` | ✅ |
| PS-C3 | Nota `a0`/`a1` caller-saved en context de subrutines | ✅ |
| PS-C4 | «bloc d'activació» → terminologia de T2 | ✅ |
| Nou | `sol-p3-registre-ctorv` (C→assemblador, 2 apartats) | ✅ |
| Nou | `sol-p3-memoria-lb-lh` (lb/lh/lbu/lhu + sb seqüencial) | ✅ |
| Trasllat | `sol-p3-enters-taules` → PS_T1 (nota remissió) | ✅ |

### 07_contrib.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| D1 | Zifencei afegit a la taula d'extensions d'EC | ✅ |
| D10 | Decisió `.globl` documentada | ✅ |
| D3 | «mode base+desplaçament» com a terme canònic documentat | ✅ |

### TODO.md

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| T2 (6 punts) | Tots els punts de T2 tancats | ✅ |
| D10–D13 | `.globl`, `ret`, adreces, `Directives` documentats | ✅ |
| Solucionaris | Taula ampliada amb T1 (6 entrades) i T2 (4 entrades) | ✅ |
| Trasllat Ca1/Ca2 | Documentat com a completat | ✅ |
| Duplicat adreces | Eliminat | ✅ |

---

## Tasques pendents

### PS_T2.qmd — Solucionaris nous (Opus High Thinking, xat separat)

| Ítem | Exercici | Descripció |
| :--- | :--- | :--- |
| PS-NOU-1 | `#exr-p3-memoria-endianness` | *Little-endian*, ordre de bytes |
| PS-NOU-2 | `#exr-p3-vectors-cerca` | Cerca en vector, retorn −1 |
| PS-NOU-3 | `#exr-p3-vectors-punter-aritm` | Aritmètica de punters sobre `short` |
| PS-NOU-4 | `#exr-p3-strings-copia` | Còpia de cadena amb `'\0'` |

### Decisions obertes

| Decisió | Estat |
| :--- | :--- |
| D2 `startup.s` | Pendent consens professorat |
| D4 `@sec-von-neumann` | Pendent revisió T1 |
| D5 `@nte-la-auipc` | Resolt quan T3 revisat ✓ |
| D6 `@sec-optimitzacions-bucle` | Confirmat a T4 ✓ |
| D11 `ret` vs `jalr` | Pendent consens; provisional: `ret` |
| D12 format adreces | Pendent decisió global; provisional: sense espais |
