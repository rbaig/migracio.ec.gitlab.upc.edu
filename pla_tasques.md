# Pla de tasques — neteja del render i assumptes pendents

Generat el 2026-07-04 a partir de `log.log` (últim `quarto render`), `TODO.md` i la conversa amb Claude Code (Fable 5).

Fitxer operatiu i transitori: cada tasca s'esborra quan es completa; les decisions de criteri que en surtin aterren a `07_contrib.qmd`.

**Llegenda de configuració recomanada:** Model / Effortness / Thinking.

---

## Bloc A — Neteja de warnings del render (prioritat 1)

### A1. Slugs `{#sec-}` a T1, T2 i T5

**Config:** Sonnet 4.6 (o Fable) / Low–Medium / No

Pas 1 de la seqüència de revisió de `CLAUDE.md`. Aplicar els criteris de generació d'slug documentats a `CLAUDE.md §Etiquetes {#sec-}` (referència: `T4.qmd`).

- [ ] `01_T/T1.qmd` — afegir `{#sec-}` a totes les capçaleres `##`–`####` (⚠ hi ha canvis locals pendents i un `T1_.qmd` no versionat: aclarir primer quin és el fitxer bo).
- [ ] `01_T/T2.qmd` — ídem.
- [ ] `01_T/T5.qmd` — ídem.
- [ ] Excloure capçaleres dins de callouts.
- [ ] Verificació global de col·lisions d'slugs entre temes (vegeu A2).

### A2. Identificador duplicat `sec-opt-acces-sequencial`

**Config:** Sonnet 4.6 (o Fable) / Low / No

Definit dues vegades: `01_T/T2.qmd:2028` i `01_T/T4.qmd:450`. Referenciat des de `01_T/T2.qmd:1966`, `02_PE/PE_T4.qmd:525`, `04_L/L4.qmd:30,304`, `04_L/L6.qmd:47`.

- [ ] Decidir quin dels dos és el canònic (probablement T4, «Optimització #1 — Accés seqüencial») i reanomenar l'altre (p. ex. `#sec-acces-sequencial-intro` a T2).
- [ ] Reapuntar les referències segons a quin dels dos conceptes es refereixen realment.

### A3. Div sense tancar a `T7.qmd`

**Config:** Sonnet 4.6 (o Fable) / Low / No

`[WARNING] Div at line 168 column 1 unclosed at line 1981` — un `:::` desaparellat prop de la línia 168 de `01_T/T7.qmd`.

- [ ] Localitzar el `:::` desaparellat i tancar-lo (o eliminar-lo).

### A4. Referències creuades no resoltes (reparables)

**Config:** Sonnet 4.6 (o Fable) / Medium / No

La majoria depenen d'A1 (els destins són a T2/T5/T9 sense slug) o de decisions ja documentades a `TODO.md`.

- [ ] `@sec-ecall` (T2, T3 ×2, L1) — el destí és la secció d'`ecall`; probablement quedarà resolt amb els slugs de T2 o cal crear-lo a T9 (que usa prefix `ei-`). Verificar a quin tema ha d'apuntar.
- [ ] `@sec-operands-memoria` (L2) — destí a T2; es resol amb A1.
- [ ] `@imp-ec-alineacio-pila` (L3, L4 ×2, L5 ×2) — el callout no existeix (`TODO.md` diu «si existeix»). Crear el callout `{#imp-ec-alineacio-pila}` a T3 amb la decisió presa (pila múltiple de 4 a EC) o reapuntar a `@nte-abi-alineacio-pila`.
- [ ] `@imp-exception-handler` (T3) — destí inexistent; probablement ha d'apuntar a un callout de T9. Verificar i reparar.
- [ ] `@sec-politica-reemplacement` (L6 ×2) — destí a T7; comprovar l'slug real (possible errada d'escriptura: *reemplacement* vs. *reemplaçament*).
- [ ] `07_contrib.qmd`: `@sec-nom`, `@sec-llicencia-figures-externes`, `@sec-contrib-callout-aprofundiment` — refs internes trencades del propi fitxer; reparar o eliminar.
- [ ] **No reparables sense figura** (no tocar; ja consten a `TODO.md §T7/§T8`): `@fig-cd-diagrama`, `@fig-assoc-conjunts-diagrama`, `@fig-ca-diagrama`, `@fig-texe-diagrama`, `@fig-mv-flux-traduccio`.

---

## Bloc B — Figures: fonts i colors (prioritat 2; assumpte 3.3)

### B1. Colors sense equivalent dark a `21_specs/svg.md`

**Config:** Fable / Medium / No

`gen_dark.py` reporta ~30 colors no reconeguts (llista completa a `log.log:91-274`). Cal criteri de contrast per triar cada equivalent dark.

- [ ] Colors «legacy» de figures natives (`#d1d1d1`, `#999999`, `#dee2e6`, `#333333`, `#4d4d4d`, `#cc0000`, `#185fa5`, `#1a5276`, `#4a90b8`, `#e8f4f8`, `#e6f1fb`, `#888780`, `#0b449a`, `#7d6d6c`, `#0099e5`, `rgb(0, 0, 0)`…): decidir per a cadascun si (a) s'afegeix a `#svg-dark-replacements` o (b) es normalitza el SVG original a la paleta del projecte (preferible segons `21_specs/svg.md`).
- [ ] Paleta LO Draw de les figures externes de T7 (`#0000ff`, `#8080ff`, `#80ff80`, `#ffff00`, `#ff8080`…): afegir al bloc de substitucions (aquestes no es toquen al SVG original).
- [ ] Re-executar `quarto render` (o només el pre-render) i comprovar `0 colors no reconeguts`.

### B2. Fonts desconegudes a les figures externes de T7

**Config:** Sonnet 4.6 / Low / No

`norm_font.py` reporta Arial/Courier/Symbol/TimesNewRoman (incrustades i CSS) a 16 fitxers `13_figs_externes/T7_*.svg`.

- [ ] Decidir política: afegir aquestes fonts al mapa de `21_specs/svg.md`, o passar a `--on-unknown-font normalize` per a les externes (canvi a `_quarto.yml`).
- [ ] Aplicar i verificar `0 avisos` al pre-render.

---

## Bloc C — Equacions en HTML per a dispositius petits (assumpte 3.1)

**Config:** Fable / Medium / No

El LaTeX de display desborda per la dreta en pantalles petites i «embruta» les taules.

- [ ] Diagnosticar: quin motor s'usa (MathJax per defecte a Quarto) i quins contenidors desborden (equacions display, equacions dins de cel·les de taula, o totes dues).
- [ ] Proposar i aplicar solució CSS a `styles.css` (p. ex. `overflow-x: auto` als contenidors `mjx-container[display="true"]` / `.math.display`, i tractament específic per a taules amb math).
- [ ] Valorar si algunes equacions llargues s'han de partir (`aligned`/`split`) en lloc de fer scroll.
- [ ] Relació amb `TODO.md §Tasques globals`: «Equacions a MathML» — si es migra a MathML, revalidar el comportament responsive després.
- [ ] Provar a viewport estret (p. ex. 360 px) abans de donar per tancat.

---

## Bloc D — Criteri backticks / LaTeX math / cursiva (assumpte 3.2)

**Config:** Fable / High / **Sí**

Decisió de disseny transversal, ja oberta a `TODO.md §Decisions obertes` i com a TODO a `07_contrib.qmd:480-481`. Dues fases:

- [ ] **Fase 1 — proposta**: auditar l'ús actual als 27 fitxers principals (Tx, PE, PS, Lx) i redactar una proposta de criteri per context: cos del text, títols de secció, títols de callout, cel·les de taula, captions, blocs de codi. Inclou els subcasos oberts de `TODO.md`: noms de registres CSR amb/sense backtick, negretes dins de callouts, numeració d'equacions.
- [ ] **Aprovació de l'usuari** (i, si escau, del professorat). El criteri aprovat aterra a `07_contrib.qmd`.
- [ ] **Fase 2 — aplicació global**: substitució sistemàtica als fitxers segons el criteri (aquesta fase pot baixar a Sonnet / Low, és mecànica).

---

## Bloc E — Ús pedagògic de les referències creuades (assumpte 3.4)

**Config:** Fable / High / **Sí**

Revisió tema a tema (un xat per tema o per parells de temes) de:

- [ ] Densitat: ni seccions òrfenes de referències ni paràgrafs saturats.
- [ ] Direccionalitat: evitar referències cap endavant a conceptes no introduïts (excepte les documentades, p. ex. `fcsr` → `@nte-zicsr`, vegeu `TODO.md §T5 P8`).
- [ ] Coherència Tx ↔ PE_Tx ↔ PS_Tx ↔ Lx: que problemes i laboratori remetin a la secció de teoria pertinent.
- [ ] Convencions de `07_contrib.qmd §referències creuades` (ordre tema → secció → … → equació).

Recomanació: fer-ho **després** dels blocs A i D, perquè els slugs i el criteri d'estil ja estiguin estables.

---

## Bloc F — Solucionaris pendents (de `TODO.md §Solucionaris pendents`)

**Config:** Fable / High / **Sí** (el TODO els marcava «Opus High Thinking»; Fable hi és superior)

Un xat per tema, seguint `PS_criteris.qmd`:

- [ ] T2: `exr-p3-memoria-endianness`, `exr-p3-vectors-cerca`, `exr-p3-vectors-punter-aritm`, `exr-p3-strings-copia` → `PS_T2.qmd`.
- [ ] T3: `exr-p4-compilacio-auipc`, `exr-p4-memoria-jalr`, `exr-p4-logica-rotacio` (apartat b) → `PS_T3.qmd`.

---

## Ordre d'execució recomanat

| # | Bloc | Model | Effortness | Thinking |
| :--- | :--- | :--- | :--- | :--- |
| 1 | A (warnings del render) | Sonnet 4.6 o Fable | Low–Medium | No |
| 2 | B (fonts i colors de figures) | B1: Fable · B2: Sonnet 4.6 | Medium · Low | No |
| 3 | C (equacions responsive) | Fable | Medium | No |
| 4 | D (criteri backticks/math/cursiva) | Fable | High | Sí |
| 5 | E (crossrefs pedagògiques) | Fable | High | Sí |
| 6 | F (solucionaris pendents) | Fable | High | Sí |

Notes:

- Els blocs A–B són mecànics: Fable amb effort baix també serveix (no cal canviar de model si ja hi ets; simplement no cal Thinking).
- Els blocs D, E i F són els que justifiquen Fable High + Thinking: judici d'estil transversal, judici pedagògic i càlcul pas a pas, respectivament.
- Qüestió prèvia al bloc A: aclarir l'estat de `01_T/T1_.qmd` (no versionat) i dels canvis locals a `T1.qmd`/`T7.qmd` abans de tocar aquests fitxers.
