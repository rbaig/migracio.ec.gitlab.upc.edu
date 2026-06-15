# T2.qmd — Llista de tasques de revisió interna

> Generat des de l'anàlisi profunda (Tasca A) i actualitzat amb les decisions i els fitxers del repo.
> Referències de línia segons el `T2.qmd` original.
>
> **Estats:** ✅ aplicada · ⏸️ decisió pendent · 🔍 verificació pendent · 📌 heads-up (altres fitxers) · ⏳ execució posterior

---

## 1. Bloquejants del render

| # | Estat | Línia | Tasca |
| :--- | :---: | :--- | :--- |
| 1.1a | ✅ | 441/445 | `#imp-zeroext-signext` dup → 2a a `#imp-ext-esquerra`. |
| 1.1b | ✅ | 586/592 | `#wrn-pseudoinstruccions-no-ratificades` dup → 2a a `#wrn-godbolt`. |
| 1.1c | ✅ | 1408/1596 | `#cau-punters-naturals` dup → 2a a `#cau-punters-aritmetica`. |
| 1.1d | ⏸️ D1(c) | 696/712 | `#nte-programa-esquelet` dup: la 2a és al bloc comentat de `startup.s`. Marcat `TODO(startup.s)`. |
| 1.2 | ✅ | 1092 | Referència buida `(@)` eliminada. |
| 1.3 | ✅ | 887/899/901/1301 | `$` solts i `M~b[adreça]` sense `~` corregits. |
| **4.x** | **📌** | **T3** | **Col·lisió REAL T2↔T3: `#cau-instruccions-no-lwu`.** A T2 és correcte (lwu); a **T3 l.106 està mal etiquetada** (parla de `sla`/`slai`). Cal reanomenar la de T3 → `#cau-instruccions-no-sla` (a la revisió de T3). |

## 2. Rigor tècnic / ISA

| # | Estat | Línia | Tasca |
| :--- | :---: | :--- | :--- |
| 2.4 | ✅ | 1239 | `ori`: `ZeroExt` → `SignExt`. **Validar.** |
| 2.5 | ✅ D5(a) | 152 | Recompte: **42 → 41** (coherent amb la llista i amb l'ISA, `fence.tso` inclòs). |
| 2.8 | ✅ | 1314 | `Mbu` → `Mb`. |
| 2.9 | ✅ | 1329/1371 | "registre font" → "registre destinació" (loads). |
| 2.10 | ✅ | 1791 | `sizeof(mat[2][3])` → `sizeof(int[2][3])`. |
| 2.11 | ✅ | 1874 | `*p = vec;` → `p = vec;`. |
| 2.6/2.7 | ⏸️ D1(c) | 742-772 | `__start`/`a7,10` (bloc comentat): marcat `TODO(startup.s)` amb la correcció a fer si es manté. |
| 2.12 | 🔍 | 2082 | `.byte 0101` octal a RARS → marcat `TODO(RARS-verif)`. |
| 2.13 | 🔍 | 1112 | `.byte/.half/...` sense operands → marcat `TODO(RARS-verif)`. |
| 2.14 | 🔍 | 524 | `li` amb `lo₁₂==0` "No a RARS" → marcat `TODO(RARS-verif)`. |

## 3. Decisions

| # | Estat | Decisió presa |
| :--- | :---: | :--- |
| D1 | ✅ (c) | `startup.s`: marcat tot amb `TODO(startup.s)` per a consens amb els professors. Bloc i prosa anotats. |
| D2 | ✅ (b) | Zifencei: es manté a T2; TODO recordant actualitzar `contrib.qmd` §Extensions. |
| D3 | ✅ (a) | MIPS (l.257): reescrit sense esment a MIPS. |
| D4 | ✅ (b) | Llistes completes M/F a T2: es mantenen com a visió general. |
| D5 | ✅ (a) | 42 → 41. |
| D6 | ✅ | `.default filename="C"` per a plantilles: es manté. |
| D7a | ✅ (a) | `.data`/`.text` estàndard aclarit; adreces inicials = específiques de RARS. TODO eliminat. |
| D7b | ✅ (b) | Model relaxat/`FENCE`: afegit aprofundiment `wrn-model-memoria-relaxat` (no avaluable); TODO eliminat. |
| D7c | ✅ (T8) | Mem. virtual: aprofundiment Sv32 mogut a **T8** (`wrn-mv-sv32`); a T2 es manté el bullet "és virtual" amb ref a `@sec-mv-espais`. |
| D7d | ✅ (a) | `cau-long-long-2-regs`: es manté `.callout-caution` (Essencial); TODO eliminat. |
| D7e | ✅ (a) | Punters a funcions: afegit aprofundiment `wrn-punters-funcions` (pont cap a `jalr`/`@sec-subrutines`). |

## 4. Coherència i referències creuades (verificat amb index/T3/T4)

| # | Estat | Resultat |
| :--- | :---: | :--- |
| 4.20 | ✅ | §Matrius és a **T4** (`sec-matrius*`, `eq-acces-aleatori-matriu` existeixen). Forward-refs de T2 vàlides. *Nota pedagògica:* T2 (vectors) referencia `@sec-matrius-acces-aleatori` (T4); és per disseny (T2 introdueix, T4 formalitza). |
| 4.21 | 📌 | `sec-extraccio-invariants` es defineix a **T2** (l.1916) i T4 l'usa. La nota de `contrib.qmd` (§T2/T4) que diu "es defineixen totes a T4" és imprecisa → **actualitzar contrib**. Sense col·lisió d'etiquetes. |
| 4.22 | ✅ | `@sec-opt-acces-sequencial` i `@sec-optimitzacions-bucle` existeixen a T4. |
| 4.23 | ✅ | Totes les forward-refs resolen: `@imp-llenguatges-de-referencia` (index.qmd), `@nte-la-auipc` (T3), `@sec-ecall` (T9), `@sec-von-neumann` (T8), `@sec-mv-espais` (T8), `@sec-compilacio` (T3), `@sec-multinivell-pila` (T3), `@sec-instruccions-logiques-bit-a-bit` (T3), `#sec-tema-*` (index). |
| 4.24 | ✅ | Etiquetes accentuades a ASCII: `#imp-arrova-adreça-memoria` → `#imp-operador-adreca-de`; `#tip-alineació-incorrecte` → `#tip-alineacio-incorrecte`. |

## 5. Format Quarto

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 5.25 | ✅ | `{.C filename=…}` → `{.c filename=…}` (26×). |
| 5.26 | ✅ | `filename="RISC-V"` → `filename="RV32I"`. |
| 5.30 | ✅ | `` .`space n` `` → `` `.space n` ``. |
| 5.31 | ✅ | Títol callout incomplet completat. |
| 5.32 | ✅ | `.global` → `.globl`. |
| 5.33 | ✅ | `$*p1$…` → `` `*p1` ``; comentaris `int *p1 = &x;`. |
| 5.28 | ✅ | `@tbl-codi-ascii`: convertida de *div* a *caption* estàndard `: Rangs de codis ASCII {#tbl-codi-ascii}`. |
| 5.29 | 🔍 | `#tbl-` sense caption (p. ex. `#tbl-tipus-alineacio`). |

## 6. Llengua / català normatiu

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 6.34–6.39 | ✅ | Frases truncades/agramaticals, "No s'ha **de**", "l'**ús**", concordances, "a**dd**ició", punts finals, coma sobrera, majúscula "A RARS", «» al títol. |
| 6.40 | ✅ | Passada completa de dobles espais: §Intro/ISA + l.19/21/22, espai abans de coma (l.257), marcador `-  ` (l.1879/1880). Codi intacte. |
| 6.41 | ⏳ | Redundància "modularitat" (57/69/86): editorial, pendent. |

## 7. Figures / SVG (⏳ Tasca D, xat a part)

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 7.42 | ✅ | SVG *light* dels formats renombrats a `T2_typeR/S/I_light.svg`; refs actualitzades. Fitxers a `outputs/figures/`. |
| 7.43 | ✅ | Creat `T2_acces_vector_light.svg` + `_dark.svg` (verificats); etiqueta `#fig-acces-vector`, integració light/dark al `.qmd`. |

## 8. Sigles (🔍 requereix `sigles.md`)

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 8.44 | ✅ | `sigles.qmd`: **CISC, ELF, GCC, MSB, RISC, LSb, MSb, RVA20/22/23**. Descartades: ARM/SPARC/PowerPC/Alpha, GNU. **SISP**: eliminat el parèntesi a T2 l.9. |

## Correccions aplicades a T3.qmd (amb permís)

- ✅ `#cau-instruccions-no-lwu` (l.106, contingut sla/slai) → `#cau-instruccions-no-sla`. **Resol la col·lisió T2↔T3.**
- ✅ `#cau-salts-condicionals-relatius-pc` (2a, l.560, contingut incondicionals) → `#cau-salts-incondicionals-indirectes` (+ doble espai).
- ✅ `#nte-pseudoinstruccions-comparacio-zero` (2a, l.427) → `#nte-pseudoinstruccions-salt-condicional-zero`.
- ✅ `#tip-exemple-suma2` (l.1077) → `#tip-crida-dos-punts`; (l.1198) → `#tip-pas-referencia-punters`; es manté el de l.1129 (suma2).
- ℹ️ **Fals positiu**: `#imp-ec-alineacio-pila` (l.1337) té una sola definició real (l.1336 és un comentari) → cap canvi.

## 📌 Pendents en altres fitxers

- ✅ **T3 — DRY**: taula `beqz/bnez/…` fusionada. Es manté a §Salts condicionals (`@nte-pseudoinstruccions-salt-condicional-zero`); a la secció de comparació s'hi ha posat una referència creuada.
- **T4.qmd** — sense duplicats ni col·lisions. Cap canvi necessari.
- ✅ **contrib.qmd** — nota d'optimitzacions corregida (extracció d'invariants és a T2, referenciada des de T4) + **Zifencei** afegit a la taula d'extensions (T9).
