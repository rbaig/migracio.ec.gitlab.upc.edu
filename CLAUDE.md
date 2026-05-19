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
  i Potència s'han separat en un tema nou, T6.qmd.
- Els PDFs T2–T5 corresponen a T2.qmd–T5.qmd
- Els PDFs T6–T8 corresponen a T7.qmd–T9.qmd

### Volum

| Material    | Fitxers .qmd   | PDFs originals          |
| :---------- | :------------- | :---------------------- |
| Apunts      | T1–T9          | 8 PDFs, ~200 pàgines    |
| Problemes   | PE.qmd, PS.qmd | 2 PDFs                  |
| Laboratori  | L0–L5          | 6 PDFs + plantilles     |

### Fitxers transversals

- `riscv.qmd`: compendi de referència RISC-V (inclòs via `{{< include >}}`).
- `sigles.md`: glossari de sigles.
- `contrib.qmd`: convencions i normes (cal llegir-lo detalladament abans de generar contingut).

## Convencions

Abans de generar qualsevol contingut, llegeix `contrib.qmd`. Conté:
- El sistema de callouts i prefixos d'etiquetes.
- Les normes d'estil (veu, puntuació, negretes, anglicismes, sigles).
- Els criteris de format (mermaid, taules, figures, blocs de codi, aniuaments).
- Les substitucions terminològiques obligatòries.

### Figures

#### Format i variants
Les figures es generen com a fitxers SVG estàtics amb colors absoluts (sense
variables CSS de l'entorn del visualitzador). Cada figura té dues variants:

- `nom_figura_light.svg` — mode clar (cosmo) i PDF
- `nom_figura_dark.svg` — mode fosc (darkly)

Els fitxers van al directori `figures/`. La convenció de noms usa `_` en lloc
de `-`.

#### Inserció al .qmd
```markdown
::: {#fig-nom-figura}
:::{.light-content}
![](figures/nom_figura_light.svg)
:::
:::{.dark-content}
![](figures/nom_figura_dark.svg)
:::
Caption de la figura
:::
```

#### Paleta de colors

| Element | Light (fill / stroke) | Dark (fill / stroke) |
| :--- | :--- | :--- |
| Cel·la neutra | `#f8f9fa` / `#adb5bd` | `#3d3d3d` / `#888` |
| Text secundari | `#6c757d` | `#adb5bd` |
| Text principal | `#343a40` | `#fff` |
| Destacat blau | `#cfe2ff` / `#084298` | `#1a3a5c` / `#90bfff` |
| Destacat verd | `#d1e7dd` / `#0a3622` | `#1a3a2a` / `#90d4aa` |
| Destacat groc | `#fff3cd` / `#664d03` | `#3a2e00` / `#ffd966` |
| Destacat vermell | `#f8d7da` / `#842029` | `#3a1a1e` / `#f1a8ae` |

#### Convencions de dibuix SVG
- `width="680"`, `viewBox="0 0 680 H"` on H = contingut + 20px buffer.
- `font-family="'Source Sans Pro', sans-serif"`, `font-size="11"` per a
  etiquetes de cel·la, `font-size="12"` per a text secundari, `font-size="13"`
  per a títols de quadrant.
- Cel·les destacades es dibuixen **sempre al damunt** de les grises (ordre
  de dibuix: grises primer, destacades després) per evitar solapaments de
  vores.
- Cel·les grises: `stroke-width="0.5"`. Cel·les destacades: `stroke-width="1"`.
- No s'usen línies separadores entre quadrants: només espai buit.

#### CSS mode fosc
A `custom_dark.scss`, secció `/*-- scss:rules --*/`:
```scss
figcaption,
caption,
.footnotes,
h1, h2, h3, h4,
.callout-title-container {
  code {
    color: #e8e6e3 !important;
    background-color: #2b2d2f !important;
  }
}
```

## Flux de treball

- Mostrar sempre el contingut generat en blocs de codi markdown (` ```markdown `).
- No editar fitxers directament: l'usuari fa el copy-paste manualment.
- En cas de dubte: atura't, exposa el dubte i, si és possible, proposa una solució.

## Planificació i progress

1. Tota la teoria (T1--19)
1.1 Temes preparats per a revisió externa:  `T1.qmd`, `T2.qmd`, `T3.qmd`, `T4.qmd`, 
1.2 Temes WiP: `T5.qmd` 
2. Laboratori
3. Problemes
4. Solucionari