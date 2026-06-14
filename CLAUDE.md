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

## Fase actual: Revisió interna

ontingut a revisar de teoria (T1–T9), laboratori (L1–L6) i solucionari (PS_T2–PS_T8) està generat. La fase actual és de **revisió** (tècnica i lingüística).

## Revisió interna: Planificació i estat

- Estat actual: **Revisió interna** (la faig només jo)
    - La següent serà: **Revisió externa** (amb altres professors de l'assignatura)
- Per web
    - Text d'obertura:

```
Objectiu d'aquest xat: Revisió `T1.qmd`

Intensitat: Profunda.

Model effortness actual: Sonnet 4.6 Low
- Sempre que necessitis canviar de model o effortness: digues-m'ho

Repositori (només lectura): https://github.com/rbaig/migracio.ec.gitlab.upc.edu/tree/problemes-enunciats-separats
	- Branch `problemes-enunciats-separats`

Regles generals:
- Fitxers d'operació
    - `CLAUDE.md` vs. `contrib.qmd`
        - `contrib.qmd` és el fitxer de referència. Cal que sempre estigui actualitzat.
        - `CLAUDE.md` només per a l'operació de claude.ai. Qualsevol altre especte va a `contrib.qmd`.
    - `README.md`
        - Fitxer de presentació del repositori.
        - Continguts habituals en aquest tipus de projectes (documentació, Quart book).
    - `TODO.md`
        - Només contingut transitori.
        - Al final ha de quedar buit.
- Pots fer canvis d'ordre, crear/reanomenar/eliminar seccions, figures, taules, llistes, etc.
- Interromp l'execució només si tens un dubte que hagi de resoldre jo. Mostra'm les opcions disponibles.
- Sortida: Quarto book (HTML + PDF).
- Prioritats màximes:
    - Coherència pedagògica
    - Rigor tècnic en tot el contingut
- Revisió tècnica profunda.
- Revisió lingüística: català normatiu.
- Solucionaris: Nivell de detall de les solucions: pas a pas, excepte passos trivials.
- Tots els fitxers `.qmd` de `index.qmd` formen part del projecte, encara que estiguin comentats. Si ho estan, és per escurçar el temps de renderització en rederitzacions de prova.
- Els PDFs originals estan al directori `/PDF_originals` (MIPS) per conéixer-ne els continguts. Consulta'ls en cas de dubte.
- Claude Code: Fes només canvis locals. Actualitzaré jo manualment el repositori.
- Comença sempre
    1. Explorant el repositori. Si hi ha fitxers als quals no tens accés, demana-me'ls.
    2. Llegint a fons els fitxers `_quarto.yml`, `index.qmd`, `contrib.qmd` i la resta que creguis convenient per fer el que et demani en cada cas.
    3. Presentant-me la llista exhaustiva de tasques que proposes fer
    4. Dient si cal que faci canvis en el model o l'effortness

Algunes tasques a fer:
- Dir quin model vols que configuri
- Identificar quins fitxers cal actualitzar i les tasques a fer-hi
- Proposta d'acció
- `README.md`
    - Els fitxers (x número de tema 1--9):
        - `Tx.qmd`: Teoria del Tema x
        - `PE_Tx.qmd`: Problemes, enunciats del Tema x
        - `PS_Tx.qmd`: Problemes, solucions d'una selecció dels problemes del Tema x
        - `Ly.qmd`: Laboratori, sessió y
        - `PS_criteris.qmd` conté els criteris de selecció de problemes a solucionar
    - Altra informació rellevant de l'estructura de l'arbre de directoris
    - Altra informació habitual en projectes similars a Quarto tipus book
```

### Teoria (T1–T9)

- Pendents de revisió interna: `T2.qmd`–`T9.qmd`.
- WiP: `T1.qmd`
- Preparats per a revisió externa: 

### Enunciats (PE_Tx.qmd)

- Pendents de revisió interna: `PE_T1.qmd`–`PE_T5.qmd`.
- WiP: 
- Preparats per a revisió externa: `PE_T6.qmd`–`PE_T9.qmd`.

### Solucionaris (PS_Tx.qmd)

- Pendents de revisió interna: `PS_T1.qmd`–`PS_T5.qmd`.
- WiP: 
- Preparats per a revisió externa: `PE_T6.qmd`–`PE_T9.qmd`.

### Laboratori (L1–L6)

- Preparats per a revisió interna: `L1.qmd`–`L6.qmd`.
- WiP: 
- Preparats per a revisió externa: 
### Flux de treball

1. Llegir el fitxer a revisar i identificar tots els problemes (tècnics, lingüístics, de format).
2. Presentar la llista exhaustiva de problemes trobats abans de fer cap canvi.
3. Esperar confirmació per procedir.
4. En cas de dubte: atura't, exposa el dubte i, si és possible, proposa solucions.

### Model i effortness

| Tasca | Model | Effortness |
| :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet 4.6 | Normal |
| Solucionari (`PS_Tx.qmd`) | Opus 4.8 | High |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet 4.6 | Low |

- Si la tasca canvia, indica-ho explícitament.
- Si vols que et canviï de configuració, digues-m'ho

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
