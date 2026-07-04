Nom d'aquest xat: `EC Bloc F — Solucionaris pendents T2 i T3`

Objectiu d'aquest xat: revisió profunda des de diversos punts de vista
Intensitat: Profunda
Fitxers a revisar:

- Principals: `02_PE/PE_T2.qmd`, `03_PS/PS_T2.qmd`, `02_PE/PE_T3.qmd`, `03_PS/PS_T3.qmd`
- Addicionalment: `01_T/T2.qmd`, `01_T/T3.qmd` (teoria de referència), qualsevol altre que processis

Aspectes a revisar:

- Completar el solucionari amb detall **pas a pas** (excepte passos trivials) per als exercicis següents, actualment sense solució:
    - **T2** (a `PS_T2.qmd`):
        - `exr-p3-memoria-endianness` — *Little-endian*, ordre de bytes.
        - `exr-p3-vectors-cerca` — Cerca en vector, retorn −1.
        - `exr-p3-vectors-punter-aritm` — Aritmètica de punters sobre `short`.
        - `exr-p3-strings-copia` — Còpia de string.
    - **T3** (a `PS_T3.qmd`):
        - `exr-p4-compilacio-auipc` — expansió de `la`, rang ±2 GiB.
        - `exr-p4-memoria-jalr` — tracing de `jalr` (resposta esperada: 3 vegades).
        - `exr-p4-logica-rotacio`, apartat b) — rotació de 16 posicions.
- Correcció tècnica
    - Font de veritat: tots els documents de l'autor «RISC-V International» de `09_bibliografia.bib`.
    - Les versions més recents d'altres documents del repositori oficial de «RISC-V International».
    - Molta atenció en la revisió dels càlculs.
- Coherència entre Teoria, Problemes enunciats i Problemes solució.
- Eficiència pedagògica: no emprar cap concepte no introduït encara; ordre de presentació lineal; coherència estilística amb la resta de `PS_T2.qmd`/`PS_T3.qmd` (ús de callouts, referències creuades, freqüència d'exemples).
- Català normatiu: evitar anglicismes; ús dels termes especificats a `07_contrib.qmd` (inclou el criteri de codi/matemàtiques/cursiva del bloc D, ja aplicat).

Context previ rellevant (ja resolt, no cal repassar-ho):

- `PE_T3.qmd`/`PS_T3.qmd` ja tenen la revisió interna general completada; aquest xat només afegeix les solucions que faltaven.
- Slugs `{#sec-}`, criteri d'estil (bloc D) i crossrefs trencades ja resolts als fitxers de teoria.
- Pendent (fora d'abast d'aquest xat, `TODO.md §T3`): encaix T2↔T3 de terminologia caller-saved/callee-saved.

Model i effortness:

- Ara estàs en Fable 5 High amb Thinking. Confirma'm **explícitament** si t'està bé aquesta configuració o si vols que et canviï de model, effortness o Thinking, digues-m'ho i para perquè pugui fer el canvi de configuració. Quan l'hagi fet te n'informaré i et demanaré que continuïs a partir d'aquest punt.
- Hi ha molts càlculs a fer en aquest xat (aritmètica de punters, rangs d'adreçament, rotacions de bits); si detectes que cal Thinking addicional o un canvi d'effortness a mesura que avances, atura't i digues-m'ho.

Canvis:

- Fes els canvis a tots els fitxers que creguis oportú. Al final, ofereix-me tots els fitxers que hagis modificat.

Comença:
0. Explora el repositori.
1. Llegeix `CLAUDE.md`, `07_contrib.qmd` i `PS_criteris.qmd`.
2. Llegeix `PE_T2.qmd`, `PS_T2.qmd`, `PE_T3.qmd`, `PS_T3.qmd` i la teoria corresponent (`T2.qmd`, `T3.qmd`).
3. Demana'm o busca al repositori els fitxers que necessitis (p. ex. `09_bibliografia.bib` i els PDFs de referència de RISC-V International).
4. Fes un anàlisi profund de cada exercici pendent abans de redactar la solució.
5. Genera la llista d'accions a realitzar; guarda-la a fitxer `F_tasques.md` i ofereix-me-la per descarregar.
6. Comença a realitzar les accions que no necessitin la meva aprovació. Fes una llista de les tasques que requereixin decisió meva i, quan hagis acabat la tasca anterior (6.), atura't i presenta'm la llista i les opcions de cada ítem que conté.
