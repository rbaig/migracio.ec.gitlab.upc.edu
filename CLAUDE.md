# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), amb sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte.
2. `index.qmd` — fitxers que componen el llibre.
3. `07_contrib.qmd` — convencions d'estil, callouts, terminologia, SVG, laboratori i decisions per tema.
4. `TODO.md` — tasques pendents i decisions obertes.

Per a tasques que impliquin figures SVG, llegeix també:

- `21_specs/svg.md` — paleta de colors, mapes de fonts i taula de substitució dark.
- `21_specs/registres.toml` — definicions dels registres de bits (font de veritat).

Repartiment de responsabilitats entre fitxers:

- `07_contrib.qmd` és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol decisió de format, estil, terminologia o convenció.
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació a claude.ai. Qualsevol altre aspecte va a `07_contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO.md` només conté contingut transitori; al final ha de quedar buit.

Altres fitxers transversals: `05_riscv.qmd` (compendi de referència RISC-V, inclòs via `{{< include >}}`) i `sigles.md` (glossari de sigles).

## Abast del projecte

### Estructura de fitxers `.qmd`

Convenció de noms (x = número de tema, 1–9; y = sessió de laboratori):

- `Tx.qmd`: teoria del tema x.
- `PE_Tx.qmd`: enunciats dels problemes del tema x.
- `PS_Tx.qmd`: solucions d'una selecció de problemes del tema x.
- `PS_criteris.qmd`: criteris de selecció dels problemes a solucionar.
- `Ly.qmd`: laboratori, sessió y.

### Volum

| Material | Fitxers `.qmd` |
| :--- | :--- |
| Teoria | `T1.qmd`–`T9.qmd` |
| Enunciats | `PE_Tx.qmd` (x = 1–9) |
| Solucions | `PS_Tx.qmd` (x = 2–9), `PS_criteris.qmd` |
| Laboratori | `L1.qmd`–`L6.qmd` |

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

- Preparats per a revisió externa: `T1.qmd`–`T9.qmd`.

#### Enunciats (`PE_Tx.qmd`) i Solucionaris (`PS_Tx.qmd`)

- **`PE_T1.qmd` i `PS_T1.qmd`** — **revisió interna completada**. Inclou: secció de naturals (traslladada de PE_T2), secció nova d'aritmètica Ca2 (suma, resta, multiplicació), exercicis nous (`exr-p1-naturals`, `exr-p1-enters-extensio-signe`, `exr-p1-aritm-*`), i 14 solucions cobertes a `PS_T1.qmd`.
- **`PE_T2.qmd` i `PS_T2.qmd`** — revisió interna completada. Pendent: 4 solucions noves (`exr-p3-memoria-endianness`, `exr-p3-vectors-cerca`, `exr-p3-vectors-punter-aritm`, `exr-p3-strings-copia`; vegeu `TODO.md §Solucionaris pendents`).
- **`PE_T3.qmd` i `PS_T3.qmd`** — revisió interna completada. Pendent: afegir solucions a `PS_T3.qmd` per als exercicis sense cobertura (vegeu `TODO.md §Solucionaris pendents`).
- **La resta de fitxers** (`PE_T4.qmd`–`PE_T9.qmd` i `PS_T4.qmd`–`PS_T9.qmd`) estan pendents d'un **pas combinat**: adaptació als `Tx.qmd` resultants de la revisió interna + revisió interna pròpia. Es fa en un sol xat per fitxer, en ordre temàtic.
- Tasca prèvia opcional (Claude Code): substitució global de terminologia revisada als fitxers PE/PS abans de la revisió web.

#### Laboratori (`L1`–`L6`)

- Pendents de revisió interna: `L1.qmd`–`L6.qmd`.

### Etiquetes `{#sec-}` a les capçaleres

Totes les capçaleres `##`, `###` i `####` dels fitxers `Tx.qmd` han de tenir un identificador `{#sec-nom}` per ser referenciables amb `@sec-nom`.

**Estat:**
- `T3.qmd`, `T4.qmd`, `T6.qmd`–`T9.qmd` — **complet** (`T4` és la referència; `T6`–`T8` amb prefixos propis; `T9` amb prefix `ei-`; `T3` completat en la revisió interna d'aquest tema).
- `T1.qmd` — **complet** (45 slugs únics; completat en la revisió interna de T1).
- `T2.qmd`, `T5.qmd` — **pendent** (tasca sistemàtica: Claude Code, pas 1 de la seqüència de revisió).

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

### Seqüència de revisió pendent

1. **Slugs T2, T5** (Claude Code): prefixat sistemàtic `{#sec-}` + verificació de refs creuades globals. *(T1 completat en la revisió interna; T3 completat en la revisió interna de T3; T4, T6–T9 ja estaven complerts.)*
2. **PE_T1–PE_T9, PS_T1–PS_T9** (1 xat per fitxer, ordre temàtic): pas combinat adaptació + revisió interna. *(T1, T2 i T3 completats.)*
3. **L1–L6** (2 xats: L1–L3 i L4–L6): revisió interna laboratori.

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

| Tasca | Model | Effortness |
| :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet 4.6 | Normal |
| Solucionari (`PS_Tx.qmd`) | Opus 4.8 | High |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet 4.6 | Low |

- Si la tasca canvia, indica-ho explícitament.
- Si vols que et canviï la configuració, digues-m'ho.

### Figures SVG: política de generació

**La prioritat és sempre generar el SVG des de zero** amb elements natius (`<rect>`, `<line>`, `<text>`, etc.), seguint `21_specs/svg.md`. El PDF original es pot usar com a referència visual, però la figura es reprodueix com a SVG natiu.

**Figures de nova creació (opció per defecte, tots els temes):**
- Construïdes des de zero amb elements SVG (`<rect>`, `<line>`, `<text>`, etc.).
- Fonts i colors de la paleta del projecte (vegeu `21_specs/svg.md`).
- Es desen a `12_figs_originals/`; la variant dark es genera automàticament pel pre-render (`22_scripts/gen_dark.py`).

**Figures extretes de PDFs originals (reservat per a figures complexes):**

L'extracció via `pymupdf` (`text_as_path=True`) és el recurs per a figures que no és viable reproduir com a SVG natiu en un temps raonable (gràfics multisèrie, circuits detallats, geometria molt densa). La decisió es pren conjuntament amb l'usuari. Es desen a `13_figs_externes/`; vegeu `21_specs/svg.md §15` per als detalls tècnics i la llista de figures existents.

**Figures de registres de bits:**
- Definides a `21_specs/registres.toml` (font de veritat).
- Generades automàticament pel pre-render (`22_scripts/gen_regs.py`).

**Flux de pre-render** (`_quarto.yml`):

El pipeline de pre-render és a `_quarto.yml` (clau `project.pre-render`). La font de veritat és sempre `_quarto.yml`; no es duplica aquí.

En tots els casos, la font de veritat per a fonts i colors és `21_specs/svg.md`.

### Text d'obertura (web)

Plantilla per encetar un xat de revisió (omple els camps entre claudàtors):

Nom d'aquest xat: `EC T3, PE_T3 i PS_T3 Revisió interna`

Objectiu d'aquest xat: revisió profunda des de diversos punts de vista
Intensitat: Profunda
Fitxers a revisar:

- Principals: els especificats al "Nom d'aquest xat"
- Addicionalment: qualsevol que processis

Aspectes a revisar:

- Correcció tècnica
    - Font de veritat: tots els documents de l'autor "RISC-V International" de `09_bibliografia.bib`
    - Les versions més recents d'altres documents del repositori oficial de "RISC-V International"
    - Molta atenció en la revisió dels càlculs
- Coherència entre Teoria, Problemes enunciats i Problemes solució
- Eficiència pedagògica
    - Ordre de presentació de la matèria autocontingut: presentació lineal de continguts (no emprar cap concepte que no s'hagi introduït encara, dificultat creixent, etc.)
    - Coherència estilística del llenguatge, dels recursos didàctics (ús de callouts, de referències creuades, freqüència dels exemples, ús consistent de termes, etc.)
- Català normatiu
    - Evitar anglicismes
    - Ús dels termes especificats a 

Model i effortness:

- Ara estàs en Sonnet 4.6 Medium sense Thinking. Confirma'm **explícitament** si t'esta bé aquesta configuració o si vols que et canviï de model, effortness o Thinking, digues-m'ho i para perquè pugui fer el canvi de configuració. Quan l'hagi fet te n'informaré i et demanaré que continuïs a partir d'aquest punt.
- En aquesta revisió hi ha molts càlculs a fer. Suposo que quan hagis llegit tota la documentació em demanaràs que et passi a Opus High Thinking. Quan ho necessitis, para i digues-m'ho tan aviat com ho necessitis.
- Has d'interrompre l'execució sempre que vulguis que et canviï la configuració.

Canvis:

- Fes els canvis a tots els fitxers que creguis oportú. Al final, ofereix-me tots els fitxers que hagis modificat

Comença:
0. Explora els fitxers que t'he passat
1. Llegeix `CLAUDE.md`, `07_contrib.qmd` i `21_specs/svg.md`
2. Llegeix els fitxers principals a revisar
3. Demana'm o busca al repositori els fitxers que necessitis
4. Fes un anàlisi profund del contingut
5. Genera la llista d'accions a realitzar; guarda-la a fitxer T2_P_tasques.md i ofereix-me-la per descarregar.
6. Comença a realitzar les accions que no necessiten la meva aprovació. Fes una llista les tasques que requereixi decisió meva i quan hagis acabat la tasca anterior (6.) atura't i presenta'm la llista i les opcions de cada ítem que conté.
```
Mirror públic del repositori: https://github.com/rbaig/migracio.ec.gitlab.upc.edu
Renderització HTML: https://loi.ac.upc.edu/ec