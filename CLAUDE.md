# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), amb sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte.
2. `index.qmd` — fitxers que componen el llibre.
3. `contrib.qmd` — convencions d'estil, callouts, terminologia, SVG, laboratori i decisions per tema.
4. `TODO.md` — tasques pendents i decisions obertes.

Repartiment de responsabilitats entre fitxers:

- `contrib.qmd` és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol decisió de format, estil, terminologia o convenció.
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació a claude.ai. Qualsevol altre aspecte va a `contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO.md` només conté contingut transitori; al final ha de quedar buit.

Altres fitxers transversals: `riscv.qmd` (compendi de referència RISC-V, inclòs via `{{< include >}}`) i `sigles.md` (glossari de sigles).

## Abast del projecte

### Estructura de fitxers `.qmd`

La nova estructura **no és un mapatge 1:1** dels temes originals (MIPS). MIPS: 8 temes; RISC-V: 9 temes:

- T1 dividit: «Introducció» → T1; «Rendiment, Amdahl i potència» → T6.
- T2–T5 → T2–T5.
- T6–T8 → T7–T9.
- Laboratoris (només +1): L0 → L1, L1 → L2, etc.

Convenció de noms (x = número de tema, 1–9; y = sessió de laboratori):

- `Tx.qmd`: teoria del tema x.
- `PE_Tx.qmd`: enunciats dels problemes del tema x.
- `PS_Tx.qmd`: solucions d'una selecció de problemes del tema x.
- `PS_criteris.qmd`: criteris de selecció dels problemes a solucionar.
- `Ly.qmd`: laboratori, sessió y.

### Volum

| Material | Fitxers `.qmd` | PDFs originals |
| :--- | :--- | :--- |
| Teoria | `T1.qmd`–`T9.qmd` | 8 PDFs, ~200 pàgines |
| Enunciats | `PE_Tx.qmd` (x = 1–9) | |
| Solucions | `PS_Tx.qmd` (x = 2–9), `PS_criteris.qmd` | |
| Laboratori | `L1.qmd`–`L6.qmd` | 6 PDFs + plantilles |

Tots els fitxers `.qmd` de `index.qmd` formen part del projecte, encara que estiguin comentats (es comenten per escurçar el temps de renderització en proves).

Els PDFs originals (MIPS) són al directori `/PDF_originals`; consulta'ls en cas de dubte sobre els continguts.

## Revisió interna

Fase actual del projecte. El contingut de teoria (T1–T9), laboratori (L1–L6) i solucionari (PS_T2–PS_T8) ja està generat; ara es fa la **revisió** (tècnica i lingüística), només per l'usuari. La fase següent serà la **revisió externa**, amb altres professors de l'assignatura.

### Prioritats de la revisió

- Prioritats màximes: **coherència pedagògica** i **rigor tècnic** en tot el contingut.
- Revisió tècnica profunda i revisió lingüística en **català normatiu**.
- Solucionaris: detall **pas a pas**, excepte els passos trivials.

### Estat dels materials

El fitxer en curs (WiP) l'indica l'usuari a l'inici de cada xat.

#### Teoria (T1–T9)

- Pendents de revisió interna: `T5.qmd`–`T9.qmd`.
- Preparats per a revisió externa: `T1.qmd`–`T4.qmd`.

#### Enunciats (`PE_Tx.qmd`)

- Pendents de revisió interna: `PE_T1.qmd`–`PE_T5.qmd`.
- Preparats per a revisió externa: `PE_T6.qmd`–`PE_T9.qmd`.

#### Solucionaris (`PS_Tx.qmd`)

- Preparats per a revisió externa: `PS_T1.qmd`–`PS_T9.qmd`.

#### Laboratori (`L1`–`L6`)

- Preparats per a revisió interna: `L1.qmd`–`L6.qmd`.

### Etiquetes `{#sec-}` a les capçaleres

Totes les capçaleres `##`, `###` i `####` dels fitxers `Tx.qmd` han de tenir un identificador `{#sec-nom}` per ser referenciables amb `@sec-nom`.

**Estat:**
- `T4.qmd` — **complet** (referència per a la resta). Pot servir com a model.
- `T1.qmd`–`T3.qmd`, `T5.qmd`–`T9.qmd` — **pendent** (tasca sistemàtica futura).

**Criteris de generació de l'slug** (aplicats a `T4.qmd`):

1. Parteix del text de la capçalera en minúscules.
2. Transliteració de caràcters catalans: `à→a`, `á→a`, `è→e`, `é→e`, `í→i`, `ï→i`, `ò→o`, `ó→o`, `ú→u`, `ü→u`, `ç→c`, `l·l→ll`, `·→` (eliminat).
3. Elimina: `` ` `` (backticks), `*`, `#`, `(`, `)`, `,`, `'`, `/`.
4. Substitueix ` — ` i `—` per ` ` o `-`.
5. Tota seqüència de caràcters no alfanumèrics → un sol guió `-`.
6. Elimina guions inicials i finals.
7. Si el slug resultant ja existeix al fitxer, afegeix `-1`, `-2`… per unicitat. **Millor solució:** fer el títol de la capçalera prou descriptiu perquè el slug sigui únic sense sufix numèric (p. ex. `### Algorisme {#sec-algorisme-multiplicacio}` en lloc de `{#sec-algorisme}`).

**Excepcions:**
- Les capçaleres dins callouts (`## Títol del callout`) **no** reben `{#sec-}` (són títols visuals, no seccions del document).
- Les capçaleres `#` de nivell superior (títol del tema) ja solen tenir el tag de tema (`{#sec-tema-x}`); revisar que sigui consistent.

### Flux de treball

En començar un xat:

1. Explora el repositori. Si hi ha fitxers als quals no tens accés, demana'ls.
2. Llegeix a fons `_quarto.yml`, `index.qmd`, `contrib.qmd` i la resta de fitxers necessaris per a la tasca.
3. Presenta'm la llista exhaustiva de tasques o problemes que proposes **abans de fer cap canvi**, i digues si cal que canviï el model o l'effortness.
4. Espera confirmació per procedir.
5. En cas de dubte, atura't, exposa el dubte i, si pots, proposa solucions.

Regles operatives:

- Pots fer canvis d'ordre i crear, reanomenar o eliminar seccions, figures, taules, llistes, etc.
- Interromp l'execució només si tens un dubte que hagi de resoldre l'usuari; mostra-li les opcions disponibles.
- Claude Code: fes només canvis locals. L'usuari actualitza el repositori manualment.

### Model i effortness

| Tasca | Model | Effortness |
| :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet 4.6 | Normal |
| Solucionari (`PS_Tx.qmd`) | Opus 4.8 | High |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet 4.6 | Low |

- Si la tasca canvia, indica-ho explícitament.
- Si vols que et canviï la configuració, digues-m'ho.

### Text d'obertura (web)

Plantilla per encetar un xat de revisió (omple els camps entre claudàtors):

```
Nom del xat: `Revisió interna T5.qmd`

Objectiu d'aquest xat: T5.qmd
Intensitat: Profunda
Model i effortness: [p. ex. Opus 4.8 / High]. Si convé canviar-los durant el xat, digues-m'ho.

Seqüència de tasques a realitzar durant la sessió:
- Tasca A: Exploració dels fitxers subministrats
- Tasca B: Revisió tècnica (formats d'instrucció, codificació, rigor ISA)
- Tasca C: Revisió pedagògica: ordre de presentació dels conceptes (no emprar conceptes que encara no s'han presentat, nivell de detall), ús dels recursos discursius (quarto callouts, llistes de vinyetes, paràgrafs), etc.
- Tasca D: Revisió lingüística
- Tasca E: Revisió format Quarto
- Tasca F: Figures SVG

Repositori (només lectura) per SVGs, `include`, taules d'instruccions, etc.: https://github.com/rbaig/migracio.ec.gitlab.upc.edu/tree/problemes-enunciats-separats

Tens permisos per fer modificacions tots els arxius que et passi. Si fas modificacions a qualsevol arxiu, ofereix-me la versió final per descarregar.

Comencem la tasca A:

1. Llegeix `CLAUDE.md`, `contrib.qmd` 
2. Llegeix `T4.qmd`, `T5.qmd` i `instruccions_figures_memoria.md`
3. Demana'm o busca al repositori els fitxers que necessitis
4. Fes un anàlisi profund del contingut
5. Genera la llista d'accions a realitzar; guarda-la a fitxer T3_tasques.md​ a outputs. 
6. Comença a realitzar les accions que no necessiten la meva aprovació. Per cada tasca que requereixi decisió meva, atura't i presenta'm les opcions.
```
