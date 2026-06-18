# T2.qmd — Llista de tasques de revisió interna

> **Estats:** ✅ aplicada · ⏸️ decisió pendent · 🔍 verificació pendent · 📌 heads-up (altres fitxers) · ⏳ execució posterior

## 1. Bloquejants del render

| # | Estat | Línia | Tasca |
| :--- | :---: | :--- | :--- |
| 1.1d | ⏸️ D1(c) | 696/712 | `#nte-programa-esquelet` dup: la 2a és al bloc comentat de `startup.s`. Marcat `TODO(startup.s)`. |
| **4.x** | **📌** | **T3** | **Col·lisió REAL T2↔T3: `#cau-instruccions-no-lwu`.** A T2 és correcte (lwu); a **T3 l.106 està mal etiquetada** (parla de `sla`/`slai`). Cal reanomenar la de T3 → `#cau-instruccions-no-sla` (a la revisió de T3). |

## 2. Rigor tècnic / ISA

| # | Estat | Línia | Tasca |
| :--- | :---: | :--- | :--- |
| 2.6/2.7 | ⏸️ D1(c) | 742-772 | `__start`/`a7,10` (bloc comentat): marcat `TODO(startup.s)` amb la correcció a fer si es manté. |
| 2.12 | 🔍 | 2082 | `.byte 0101` octal a RARS → marcat `TODO(RARS-verif)`. |
| 2.13 | 🔍 | 1112 | `.byte/.half/...` sense operands → marcat `TODO(RARS-verif)`. |
| 2.14 | 🔍 | 524 | `li` amb `lo₁₂==0` "No a RARS" → marcat `TODO(RARS-verif)`. |

## 4. Coherència i referències creuades (verificat amb index/T3/T4)

| # | Estat | Resultat |
| :--- | :---: | :--- |
| 4.21 | 📌 | `sec-extraccio-invariants` es defineix a **T2** (l.1916) i T4 l'usa. La nota de `contrib.qmd` (§T2/T4) que diu "es defineixen totes a T4" és imprecisa → **actualitzar contrib**. Sense col·lisió d'etiquetes. |

## 5. Format Quarto

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 5.29 | 🔍 | `#tbl-` sense caption (p. ex. `#tbl-tipus-alineacio`). |

## 6. Llengua / català normatiu

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 6.41 | ⏳ | Redundància "modularitat" (57/69/86): editorial, pendent. |

## 7. Figures / SVG (⏳ Tasca D, xat a part)

| # | Estat | Tasca |
| :--- | :---: | :--- |
| 7.42 | ✅ | SVG *light* dels formats renombrats a `T2_typeR/S/I_light.svg`; refs actualitzades. Fitxers a `outputs/figures/`. |
| 7.43 | ✅ | Creat `T2_acces_vector_light.svg` + `_dark.svg` (verificats); etiqueta `#fig-acces-vector`, integració light/dark al `.qmd`. |
