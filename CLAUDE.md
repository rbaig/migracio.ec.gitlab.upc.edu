# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Objectius

- Migració de la documentació existent (PDF, fins 31/12/2025) a fitxers `.qmd`.
- Migració de l'arquitectura de referència: MIPS32 → RISC-V (RV32I + extensions M, F).
- Ordre de migració: apunts → pràctiques → problemes → solucionari.

## Abast del projecte

Els adjectius "existent" i "actual" referits a materials fan referència
a la documentació generada fins a 31/12/2025, disponible només en PDF.

### Estructura nova (fitxers .qmd) vs. PDFs originals

La nova estructura **no és un mapatge 1:1** dels PDFs originals:
- El PDF T1 s'ha dividit: la introducció resta a T1.qmd; Rendiment, Amdahl
  i Potència s'han separat en un tema nou, T2.qmd.
- Els PDFs T2–T8 corresponen a T3.qmd–T9.qmd (desplaçats un).

### Volum

| Material    | Fitxers .qmd   | PDFs originals          |
| :---------- | :------------- | :---------------------- |
| Apunts      | T1–T9          | 8 PDFs, ~200 pàgines    |
| Problemes   | PE.qmd, PS.qmd | 2 PDFs                  |
| Laboratori  | L0–L5          | 6 PDFs + plantilles     |

### Fitxers transversals

- `riscv.qmd`: compendi de referència RISC-V (inclòs via `{{< include >}}`).
- `sigles.md`: glossari de sigles.
- `contrib.qmd`: convencions i normes (llegir abans de generar contingut).

## Convencions

Abans de generar qualsevol contingut, llegeix `contrib.qmd`. Conté:
- El sistema de callouts i prefixos d'etiquetes.
- Les normes d'estil (veu, puntuació, negretes, anglicismes, sigles).
- Els criteris de format (mermaid, taules, figures, blocs de codi, aniuaments).
- Les substitucions terminològiques obligatòries.

## Flux de treball

- Mostrar sempre el contingut generat en blocs de codi markdown (` ```markdown `).
- No editar fitxers directament: l'usuari fa el copy-paste manualment.
- En cas de dubte: atura't, exposa el dubte i, si és possible, proposa una solució.