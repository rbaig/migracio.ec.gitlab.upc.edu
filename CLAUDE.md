# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), amb sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte.
2. `index.qmd` — fitxers que componen el llibre.
3. `13_contrib.qmd` — convencions d'estil, callouts, terminologia, SVG, laboratori i decisions per tema.
4. `TODO/TODO.md` — tasques pendents i decisions obertes.

Per a tasques que impliquin figures SVG, llegeix també:

- `24_specs/svg.md` — paleta de colors, mapes de fonts i taula de substitució dark.
- `24_specs/registres.toml` — definicions dels registres de bits (font de veritat).

Repartiment de responsabilitats entre fitxers:

- `13_contrib.qmd` és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol decisió de format, estil, terminologia o convenció.
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació a claude.ai. Qualsevol altre aspecte va a `13_contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO/TODO.md` només conté contingut transitori; al final ha de quedar buit.

Altres fitxers transversals: `11_riscv.qmd` (compendi de referència RISC-V, inclòs via `{{< include >}}`) i `12_sigles_simbols.qmd` (glossari de sigles i símbols).

## Abast del projecte

### Estructura de fitxers `.qmd`

Convenció de noms (x = número de tema, 1–9; y = sessió de laboratori):

- `Ax.qmd`: teoria del tema x.
- `Ex.qmd`: enunciats dels problemes del tema x.
- `Sx.qmd`: solucions d'una selecció de problemes del tema x.
- `S_criteris_seleccio.qmd`: criteris de selecció dels problemes a solucionar.
- `Ly.qmd`: laboratori, sessió y.

### Volum

| Material | Fitxers `.qmd` |
| :--- | :--- |
| Teoria | `A1.qmd`–`A9.qmd` |
| Enunciats | `Ex.qmd` (x = 1–9) |
| Solucions | `Sx.qmd` (x = 2–9), `S_criteris_seleccio.qmd` |
| Laboratori | `L1.qmd`–`L6.qmd` |

Tots els fitxers `.qmd` de `index.qmd` formen part del projecte, encara que estiguin comentats (es comenten per escurçar el temps de renderització en proves).

Els PDFs originals (MIPS) són al directori `/PDF_originals`; consulta'ls en cas de dubte sobre els continguts.

## Revisió interna

Fase actual del projecte. El contingut de teoria (T1–T9), laboratori (L1–L6) i solucionari (S2–S8) ja està generat; ara es fa la **revisió** (tècnica i lingüística), només per l'usuari. La fase següent serà la **revisió externa**, amb altres professors de l'assignatura.

### Prioritats de la revisió

- Prioritats màximes: **coherència pedagògica** i **rigor tècnic** en tot el contingut.
- Revisió tècnica profunda i revisió lingüística en **català normatiu**.
- Solucionaris: detall **pas a pas**, excepte els passos trivials.
- **Harmonització abans de la revisió externa**: «Preparat per a revisió externa» no vol dir tancat a canvis profunds, especialment els d'harmonització (terminologia, estil, convencions transversals). Tot el que es pugui detectar i corregir abans que comenci la revisió externa s'ha de fer ara, encara que impliqui tocar fitxers ja marcats com a preparats: un cop entrin altres professors en la revisió, qualsevol canvi transversal té un cost de coordinació molt més alt. Si detectes una inconsistència que afecta múltiples fitxers (per exemple, terminologia o notació aplicada de manera desigual), proposa'n la correcció sistemàtica encara que surti de l'abast estricte del xat en curs.

### Estat dels materials

El fitxer en curs (WiP) l'indica l'usuari a l'inici de cada xat.

#### Teoria (T1–T9)

- Preparats per a revisió externa: `A1.qmd`–`A9.qmd`.

#### Enunciats (`Ex.qmd`) i Solucionaris (`Sx.qmd`)

- **`E3.qmd` i `S3.qmd`** — revisió interna completada. Encaix T2↔T3 en terminologia caller-saved/callee-saved (vegeu `TODO.md §T3`).
- **La resta de fitxers** (`E1.qmd`–`E2.qmd`, `E4.qmd`–`E9.qmd` i `S1.qmd`–`S2.qmd`, `S4.qmd`–`S9.qmd`) estan pendents d'un **pas combinat**: adaptació als `Ax.qmd` resultants de la revisió interna + revisió interna pròpia. Es fa en un sol xat per fitxer, en ordre temàtic. Tasques vives pendents: zobacz `TODO.md`.
- Tasca prèvia opcional (Claude Code): substitució global de terminologia revisada als fitxers PE/PS abans de la revisió web.

#### Laboratori (`L1`–`L6`)

- Pendents de revisió interna: `L1.qmd`–`L6.qmd`.

### Etiquetes `{#sec-}` a les capçaleres

Totes les capçaleres `##`, `###` i `####` dels fitxers `Ax.qmd` han de tenir un identificador `{#sec-nom}` per ser referenciables amb `@sec-nom`.

**Estat:**
- Tots els fitxers `A1.qmd`–`A9.qmd` tenen les capçaleres etiquetades: **complet**.

**Criteris de generació de l'slug**: vegeu `13_contrib.qmd §Etiquetes `{#sec-}` a les capçaleres`.

### Seqüència de revisió pendent

Estat actual (2026-07-12):

- **Teoria (A1–A9)**: Preparats per a revisió externa. T1 tancat de facto (Fase C executada); T2/T3/T8 amb Fase C pendent; T4/T6/T7 quasi tancats.
- **Enunciats (E1–E9) i Solucionaris (S1–S9)**: Pas combinat adaptació + revisió interna, 1 xat per fitxer, en ordre temàtic (E3/S3 completats).
- **Laboratori (L1–L6)**: Pendents de revisió interna (2 xats: L1–L3 i L4–L6).

Detalls transversals i decisions obertes: vegeu `TODO.md`.

### Flux de treball

En començar un xat:

1. Explora el repositori. Si hi ha fitxers als quals no tens accés, demana'ls.
2. Llegeix els fitxers de referència obligatòria (vegeu §Fitxers de referència obligatòria) i la resta de fitxers necessaris per a la tasca.
3. Presenta'm la llista exhaustiva de tasques o problemes que proposes **abans de fer cap canvi**, i digues si cal que canviï el model o l'effortness.
4. Espera confirmació per procedir.
5. En cas de dubte, atura't, exposa el dubte i, si pots, proposa solucions.

Regles operatives:

- Pots fer canvis d'ordre i crear, reanomenar o eliminar seccions, figures, taules, llistes, etc.
- Interromp l'execució només si tens un dubte que hagi de resoldre l'usuari; mostra-li les opcions disponibles.
- Claude Code: fes només canvis locals. L'usuari actualitza el repositori manualment.

### Model i effortness

| Tasca | Model | Effortness | Thinking |
| :--- | :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet | Normal | No |
| Solucionari (`Sx.qmd`) | Opus | High | No |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet | Low | No |
| Neteja de warnings del render | Sonnet | Low–Medium | No |

- Si la tasca canvia, indica-ho explícitament.
- Si vols que et canviï la configuració, digues-m'ho.

### Figures SVG: política de generació

Política de generació SVG (prioritat, tipus de figures, fonts i colors): vegeu `13_contrib.qmd §Figures i material gràfic`.

Mirror públic del repositori: https://github.com/rbaig/migracio.ec.gitlab.upc.edu
Renderització HTML (pot estar desactualitzada): https://loi.ac.upc.edu/ec