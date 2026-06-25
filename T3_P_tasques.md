# Revisió interna T3.qmd, PE_T3.qmd, PS_T3.qmd — Registre de tasques

Xat: `EC T3-PE_T3-PS_T3` · Model: Sonnet 4.6

---

## Estat general

La revisió interna de T3, PE_T3 i PS_T3 s'ha completat en aquest xat. Els fitxers modificats i descarregables son: `T3.qmd`, `PE_T3.qmd`, `TODO.md`, `CLAUDE.md`, `07_contrib.qmd`.

`PS_T3.qmd` no ha rebut canvis de format (cap error detectat), però té solucionaris pendents de generar (vegeu §Pendent).

---

## Canvis aplicats

### T3.qmd

| Ítem | Descripció |
| :--- | :--- |
| T3-TIP1 | L. 1336: doble parèntesi sobreant `.)` → `.` |
| T3-L1 | L. 112: `"desplaçament a l'esquerra"` → `*desplaçament a l'esquerra*` |
| T3-L2 | L. 1071: `"reubicable"` → `*reubicable*` |
| T3-L3 | L. 1124: `"Qui el guarda (*Saver*)"` → `«Qui el guarda (*Saver*)»` |
| T3-L4 | L. 1380: `"adreça de"` → `*adreça de*` |
| T3-L5 | L. 1834: `"compilar"` → `«compilar»` |
| T3-C4 | 30 capçaleres `###`/`####` sense `{#sec-}` etiquetades (inclou `### RARS — Mapa de memòria`) |
| T3-ABI | `{#nte-abi-alineacio-pila}`: reescrit per dir ×4 a EC, amb nota que l'ABI estàndard exigeix ×16 |
| T3-REF | `{#tip-salt-llunya}`: afegida referència `(@nte-la-auipc)` a la primera aparició de `la` |

### PE_T3.qmd

| Ítem | Descripció |
| :--- | :--- |
| PE3-C1 | 39 blocs `` ```s `` i `` ```c `` sense `filename=` → `` ```{.s filename="RV32I"} `` i `` ```{.c filename="C"} `` |
| PE3-ORD1 | `exr-p4-memoria-jalr` mogut de `## Estructura de la memòria` (eliminada) a `## Subrutines: introducció` |
| PE3-ORD2 | `## Sentències condicionals i bucles`: reordenat de menor a major complexitat (`if` pur → bucles simples → bucles complexos amb memòria) |
| PE3-ORD3 | `## Subrutines: introducció`: reordenat de menor a major complexitat (uninivell simple → multinivell → recursives → tracing avançat → `long long`) |

### Decisions tancades

| Decisió | Resolució |
| :--- | :--- |
| Alineació de la pila | ×4 a EC (relaxació pedagògica); ×16 documentat a `{#nte-abi-alineacio-pila}` i a `07_contrib.qmd` |
| Retorn de resultats (`a0`/`a1`) | `a0` i `a1` (fins a dos resultats). Ja implementat a `{#nte-abi-pas-parametres}`. Documentat a `07_contrib.qmd` |
| `exr-p4-memoria-jalr` ubicació | Mogut a `## Subrutines: introducció` (on pertany temàticament) |
| `#cau-instruccions-no-sla` slug | Correcte; el TODO.md era imprecís. Tancat |
| `#wrn-rars-mapa-memoria` `collapse` | 1 sola línia → sense `collapse=true` per regla. Correcte tal com estava |

### Verificació tècnica — tot correcte

- Exemple `auipc` (offset, `hi_20`, `lo_12`) ✓
- BAs de `func`, `multi`, `exemple` (aritmètica interna coherent) ✓
- Accessos a vectors `v[e+q]` i `w[d+c]` a l'exemple `exemple` ✓
- Solucions PS_T3: cost de bucles (a–f), desplaçaments 64 bits, lògica bit a bit ✓
- `exr-p4-memoria-jalr`: `jalr` s'executa 3 vegades (resposta c) ✓
- `exr-p4-logica-rotacio` b): efecte = rotació de 16 posicions a la dreta ✓

---

## Pendent

### Decisions obertes (a resoldre en sessió futura)

| Decisió | On afecta |
| :--- | :--- |
| TODOs d'Adrià: integració del patch i terminologia «unes expressions» | T3, L. 154–159 i L. 253 |
| Verificació ABI sobre el BA (psABI §18.2) | T3, callout `{#nte-bloc-activacio}` |
| `gp` al mapa de memòria: incloure o esmentar de passada | T3 |
| Pseudoinstrucció `lla`: incloure o no | T3 |
| Terminologia *leaf*/*non-leaf*: eliminar o restituir com a `{.callout-warning}` | T3 |

### Solucionaris nous a PS_T3 (Opus High Thinking)

| Prioritat | Exercici | Nota |
| :--- | :--- | :--- |
| Alta | `exr-p4-compilacio-auipc` | Expansió `la` → `auipc`+`addi`, rang ±2 GiB |
| Alta | `exr-p4-memoria-jalr` | Tracing; resposta verificada: 3 vegades |
| Alta | `exr-p4-logica-rotacio` apartat b) | Resultat verificat: rotació 16 posicions |
| Mitjana | `exr-p4-subrutines-strlen` | Uninivell simple; bona referència |
| Mitjana | `exr-p4-ba-subr1` | Multinivell introductori |
| Baixa | `exr-p4-subrutines-swap` | Dos nivells, pas per referència |

### Figures pendents de retoc manual (Roger)

- `figs_auto/T3_ba_exemple__original_light.svg`
- `figs_auto/T3_deps_multi__original_light.svg`
- `figs_auto/T3_deps_exemple__original_light.svg`
