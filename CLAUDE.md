# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Abast del projecte

### Estructura (fitxers .qmd)

La nova estructura **no és un mapatge 1:1** dels PDFs originals:

- El PDF T1 s'ha dividit: la introducció resta a T1.qmd; Rendiment, Amdahl i Potència s'han separat en T6.qmd.
- Els PDFs T2–T5 corresponen a T2.qmd–T5.qmd.
- Els PDFs T6–T8 corresponen a T7.qmd–T9.qmd.

### Volum

| Material | Fitxers .qmd | PDFs originals |
| :--- | :--- | :--- |
| Apunts | T1–T9 | 8 PDFs, ~200 pàgines |
| Problemes | PE.qmd, PS.qmd | 2 PDFs |
| Laboratori | L0–L5 | 6 PDFs + plantilles |

### Fitxers transversals

- `riscv.qmd`: compendi de referència RISC-V (inclòs via `{{< include >}}`).
- `sigles.md`: glossari de sigles.
- `contrib.qmd`: convencions i normes. **Cal llegir-lo detalladament abans de generar contingut.**

## Convencions

Abans de generar qualsevol contingut, llegeix `contrib.qmd`. Conté:

- El sistema de callouts i prefixos d'etiquetes.
- Les normes d'estil (veu, puntuació, negretes, anglicismes, sigles).
- Els criteris de format (taules, figures SVG, blocs de codi, aniuaments).
- Les substitucions terminològiques obligatòries.
- La paleta de colors SVG i les convencions de dibuix.
- Les decisions per tema (T2–T9).

### CSS mode fosc

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

### Inici d'un tema o pràctica

**Primer prompt**

- Fitxers: `CLAUDE.md`, `_quarto.yml`, `contrib.qmd`.
- Objectiu: descriure el tema a generar i el context.
- Tasques:
    - Confirmar si s'ha entès l'objectiu.
    - Identificar quina informació addicional cal per poder començar.

**Segon prompt**

- Fitxers: PDF original, fitxers `.qmd` de referència, `sigles.md`.
- Confirmar si es té tota la informació necessària.
- Proposar continguts i estructura (seccions, subseccions, callouts):
    - No és obligatori seguir l'estructura del PDF: preval el criteri pedagògic, el rigor i l'actualitat tecnològica.
    - Cal incorporar tot el contingut rellevant del PDF.
    - Ser honest sobre reestructuracions necessàries (continguts obsolets, nous a incorporar).
- Per a canvis importants, demanar validació explícita.
- No generar contingut fins que no s'hagi acordat l'estructura.

**Tercer prompt**

- Estructura confirmada. Avançar secció a secció al ritme que calgui.
- **Figures (prioritat descendent):**
    - **Taula:** quan el contingut és essencialment dades tabulars.
    - **SVG:** quan la figura aporta valor visual que una taula no pot donar (diagrames de blocs, jerarquies, evolució d'estats, descomposició de bits).
    - ~~Mermaid~~: tots els diagrames nous es fan en SVG.
- **Figures SVG:**
    - Les generem al final, un cop hi hagi tot el text al `.qmd`.
    - Sempre una per una. Flux: Claude proposa la versió `light` → l'usuari retoca manualment → Claude genera la versió `dark`.
    - Nom de fitxers: `T<N>_nom_figura_light.svg` / `T<N>_nom_figura_dark.svg`.
    - Markdown d'integració: vegeu `contrib.qmd` (secció "Integració al .qmd").
    - Deixar comentaris HTML descriptius per a cada figura: `<!-- fig-...: descripció detallada -->`.
    - Proposar la llista completa de SVGs per validar-la abans de generar-ne cap.

### En finalitzar un tema, pràctica, etc.

1. Revisió completa de la darrera versió del `.qmd`.
2. Revisió tècnica profunda.
3. Revisió lingüística profunda.
4. Generar `sigles.md` actualitzat amb les sigles noves del tema (criteri: vegeu `contrib.qmd`).
5. Actualitzar `contrib.qmd` amb decisions de format o estil preses durant el tema.
6. Actualitzar `CLAUDE.md` (planificació i progress).
7. Elaborar el missatge d'inici per al xat del tema següent.

## Planificació i progress

### Teoria (T1–T9)

Temes preparats per a revisió externa: `T1.qmd`, `T2.qmd`, `T3.qmd`, `T4.qmd` (ampliat: aritmètica entera + matrius), `T5.qmd`, `T6.qmd` (segregat de T1), `T7.qmd`, `T8.qmd`, `T9.qmd`.

### Laboratori (L0–L5)

Convencions globals del laboratori (acordades durant L0 i L1):

- **Punt d'entrada:** `_start` (no `main`). Directiva `.global _start` al principi del fitxer.
- **Sortida del programa:** `li a7, 93` + `ecall` (syscall `exit`). No es fa servir `startup.s`.
- **Directives de segment:** `.data` i `.text` (sense `.section`), sense indentar, a columna 0.
- **Codi dels exercicis:** integrat al `.qmd` (no hi ha fitxers `.s` separats). Els alumnes fan copy-paste.
- **Estructura de cada exercici:** enunciat en `{#exr-...}` + solució en `{#sol-...}`.
- **Lectura prèvia:** primera secció de cada sessió; taula amb columnes "Concepte" i "On trobar-ho".
- **Lliurament:** última secció de cada sessió; taula amb els exercicis i el tipus de lliurable.
- **Nom de figura SVG:** `L<N>_nom_figura_light.svg` / `L<N>_nom_figura_dark.svg`.

Sessions preparades per a revisió externa: `L1.qmd` (TODO secció Pseudoinstruccions), `L2.qmd`, `L3.qmd`

En curs: `L4.qmd`
Pendent: `L5.qmd`, `L0.qmd`

#### Problemes/Solucionari
Pendent: `PE.qmd`, `PS.qmd`