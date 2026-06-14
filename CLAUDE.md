# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte.
2. `contrib.qmd` — convencions d'estil, callouts, terminologia, SVG, laboratori, decisions per tema.
3. `TODO.md` — llista de tasques pendents i decisions obertes.

## Abast del projecte

### Estructura de fitxers `.qmd`

La nova estructura **no és un mapatge 1:1** dels Temes originals (MIPS). MIPS: 8 temes; RISC-V: 9 temes:

- T1 dividit:
    - "Introducció" → T1
    - "Rendiment, Amdahl i potència" → T6.
- T2–T5 → T2–T5.
- T6–T8 → T7–T9.
- Laboratoris (només +1): L0 → L1, L1 → L2, etc.

### Volum

| Material | Fitxers `.qmd` | PDFs originals |
| :--- | :--- | :--- |
| Teoria | `T1.qmd`–`T9.qmd` | 8 PDFs, ~200 pàgines |
| Enunciats | `PE_Tx.qmd` (x = 1–9) | |
| Solucions | `PS_Tx.qmd` (x = 2–9), `PS_criteris.qmd` | |
| Laboratori | `L1.qmd`–`L6.qmd` | 6 PDFs + plantilles |

Tots els fitxers `.qmd` de `index.qmd` formen part del projecte, encara que estiguin comentats (s'usa per escurçar el temps de renderització en proves).

### Fitxers transversals

- `riscv.qmd`: compendi de referència RISC-V (inclòs via `{{< include >}}`).
- `sigles.md`: glossari de sigles.
- `contrib.qmd`: convencions i normes.
- `TODO.md`: tasques pendents i decisions obertes.

## Fase actual: Revisió

El contingut de teoria (T1–T9), laboratori (L1–L6) i solucionari (PS_T2–PS_T8) està generat. La fase actual és de **revisió** (tècnica i lingüística).

### Flux de treball en fase de revisió

1. Llegir el fitxer a revisar i identificar tots els problemes (tècnics, lingüístics, de format).
2. Presentar la llista exhaustiva de problemes trobats abans de fer cap canvi.
3. Esperar confirmació per procedir.
4. En cas de dubte: atura't, exposa el dubte i, si és possible, proposa solucions.

### Model i effortness per a tasques de revisió

| Tasca | Model | Effortness |
| :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet 4.6 | Normal |
| Solucionari (`PS_Tx.qmd`) | Opus 4.8 | High |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet 4.6 | Low |

Si la tasca canvia, indica-ho explícitament.

## Planificació i estat

### Teoria (T1–T9)

Preparats per a revisió de conjunt: `T1.qmd`–`T9.qmd`.

### Enunciats (PE_Tx.qmd)

Preparats per a revisió externa: `PE_T6.qmd`–`PE_T9.qmd`.

Pendents de revisió interna: `PE_T1.qmd`–`PE_T5.qmd`.

Si cal fer esmenes a `PE_Tx.qmd` (reordenar, corregir), baixa el fitxer del repositori, actualitza'l i passa'l a l'usuari perquè el descarregui i l'actualitzi al repositori.

### Solucionaris (PS_Tx.qmd)

Preparats per a revisió externa: `PS_T2.qmd`–`PS_T8.qmd`.

Pendents de creació: `PS_T9.qmd`, `PS_T1.qmd` (ordre previst: T9, T1).

### Laboratori (L1–L6)

Preparats per a revisió externa: `L1.qmd`–`L6.qmd`.

Pendent de creació: `L0.qmd`.

## Convencions CSS (mode fosc)

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
