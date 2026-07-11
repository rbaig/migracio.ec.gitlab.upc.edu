# Pla de tasques — neteja del render i assumptes pendents

Generat el 2026-07-04 a partir de `log.log` (últim `quarto render`), `TODO.md` i la conversa amb Claude Code (Fable 5).

Fitxer operatiu i transitori: cada tasca s'esborra quan es completa; les decisions de criteri que en surtin aterren a `13_contrib.qmd`.

**Llegenda de configuració recomanada:** Model / Effortness / Thinking.

---

## Bloc A — Neteja de warnings del render (prioritat 1)

### A1. Slugs `{#sec-}` a T1, T2 i T5

**Config:** Sonnet 4.6 (o Fable) / Low–Medium / No

Pas 1 de la seqüència de revisió de `CLAUDE.md`. Aplicar els criteris de generació d'slug documentats a `CLAUDE.md §Etiquetes {#sec-}` (referència: `A4.qmd`).

- [ ] `01_apunts/A1.qmd` — afegir `{#sec-}` a totes les capçaleres `##`–`####` (⚠ hi ha canvis locals pendents i un `T1_.qmd` no versionat: aclarir primer quin és el fitxer bo).
- [ ] `01_apunts/A2.qmd` — ídem.
- [ ] `01_apunts/A5.qmd` — ídem.
- [ ] Excloure capçaleres dins de callouts.
- [ ] Verificació global de col·lisions d'slugs entre temes (vegeu A2).

### A2. Identificador duplicat `sec-opt-acces-sequencial`

**Config:** Sonnet 4.6 (o Fable) / Low / No

Definit dues vegades: `01_apunts/A2.qmd:2028` i `01_apunts/A4.qmd:450`. Referenciat des de `01_apunts/A2.qmd:1966`, `02_exercicis/E4.qmd:525`, `04_laboratori/L4.qmd:30,304`, `04_laboratori/L6.qmd:47`.

- [ ] Decidir quin dels dos és el canònic (probablement T4, «Optimització #1 — Accés seqüencial») i reanomenar l'altre (p. ex. `#sec-acces-sequencial-intro` a T2).
- [ ] Reapuntar les referències segons a quin dels dos conceptes es refereixen realment.

### A3. Div sense tancar a `A7.qmd`

**Config:** Sonnet 4.6 (o Fable) / Low / No

`[WARNING] Div at line 168 column 1 unclosed at line 1981` — un `:::` desaparellat prop de la línia 168 de `01_apunts/A7.qmd`.

- [ ] Localitzar el `:::` desaparellat i tancar-lo (o eliminar-lo).

### A4. Referències creuades no resoltes (reparables)

**Config:** Sonnet 4.6 (o Fable) / Medium / No

La majoria depenen d'A1 (els destins són a T2/T5/T9 sense slug) o de decisions ja documentades a `TODO.md`.

- [ ] `@sec-ecall` (T2, T3 ×2, L1) — el destí és la secció d'`ecall`; probablement quedarà resolt amb els slugs de T2 o cal crear-lo a T9 (que usa prefix `ei-`). Verificar a quin tema ha d'apuntar.
- [ ] `@sec-operands-memoria` (L2) — destí a T2; es resol amb A1.
- [ ] `@imp-ec-alineacio-pila` (L3, L4 ×2, L5 ×2) — el callout no existeix (`TODO.md` diu «si existeix»). Crear el callout `{#imp-ec-alineacio-pila}` a T3 amb la decisió presa (pila múltiple de 4 a EC) o reapuntar a `@nte-abi-alineacio-pila`.
- [ ] `@imp-exception-handler` (T3) — destí inexistent; probablement ha d'apuntar a un callout de T9. Verificar i reparar.
- [ ] `@sec-politica-reemplacement` (L6 ×2) — destí a T7; comprovar l'slug real (possible errada d'escriptura: *reemplacement* vs. *reemplaçament*).
- [ ] `13_contrib.qmd`: `@sec-nom`, `@sec-llicencia-figures-externes`, `@sec-contrib-callout-aprofundiment` — refs internes trencades del propi fitxer; reparar o eliminar.
- [ ] **No reparables sense figura** (no tocar; ja consten a `TODO.md §T7/§T8`): `@fig-cd-diagrama`, `@fig-assoc-conjunts-diagrama`, `@fig-ca-diagrama`, `@fig-texe-diagrama`, `@fig-mv-flux-traduccio`.

---

## Bloc B — Figures: fonts i colors (prioritat 2; assumpte 3.3)

### B1. Colors sense equivalent dark a `24_specs/svg.md`

**Config:** Fable / Medium / No

`gen_dark.py` reporta ~30 colors no reconeguts (llista completa a `log.log:91-274`). Cal criteri de contrast per triar cada equivalent dark.

- [x] Colors «legacy» de figures natives: afegits al bloc `#svg-dark-replacements` de `24_specs/svg.md`, marcats com a «Colors llegat» retirables quan les figures es migrin a la paleta §10.
- [x] Paleta LO Draw de les figures externes de T7: afegida al bloc de substitucions.
- [x] `#d1d1d1` i `#0099e5` eren falsos positius (metadades d'Inkscape: `deskcolor` i graella d'edició). Resolt amb lookbehind a la regex de `gen_dark.py` + entrada identitat per a `#0099e5`.
- [x] Pre-render re-executat: **0 colors no reconeguts**, substitucions verificades als fitxers dark generats.

### B2. Fonts desconegudes a les figures externes de T7

**Config:** Sonnet 4.6 / Low / No

`norm_font.py` reporta Arial/Courier/Symbol/TimesNewRoman (incrustades i CSS) a 16 fitxers `23_figs_externes/T7_*.svg`.

- [x] Afegides al `FONT_MAP` de `24_specs/svg.md`: `Arial embedded`/`Arial, sans-serif`/`Symbol`/`Symbol embedded`/`TimesNewRoman embedded`/`TimesNewRoman, serif`/`Helvetica` → SANS; `Courier`/`Courier embedded` → MONO.
- [x] Pipeline re-executat: `0 avisos` de fonts desconegudes (18 fitxers normalitzats a `23_figs_externes/`).

---

## Bloc C — Equacions en HTML per a dispositius petits (assumpte 3.1)

**Config:** Fable / Medium / No

El LaTeX de display desborda per la dreta en pantalles petites i «embruta» les taules.

- [x] Diagnòstic (Chrome headless CDP a 360 px): motor MathJax 3 CHTML; desbordaven (1) equacions display, (2) equacions inline llargues, (3) taules senceres, (4) elements off-canvas del tema Quarto (`#quarto-sidebar-glass`).
- [x] Solució aplicada a `styles.css`: `overflow-x: auto` a `mjx-container` display i inline (inline amb barra amagada per evitar barres espúries per subpíxels), taules amb scroll propi per sota de 768 px, `body{overflow-x:hidden}` per sota de 992 px per a la UI del tema.
- [x] Verificat a 360 px amb mesures CDP (0 elements desbordats sense scroll propi) i captures (equació display, inline, taula ampla); verificat desktop 1280 px sense regressions.
- [ ] (Opcional, si molesta l'scroll) Valorar partir les equacions display més llargues amb `aligned`/`split`.
- [ ] ⚠ Si es migra a MathML (`TODO.md §Tasques globals`), els selectors `mjx-container` de `styles.css` s'hauran d'adaptar (`math[display="block"]`).

---

## Bloc D — Criteri backticks / LaTeX math / cursiva (assumpte 3.2)

**Config:** Fable / High / **Sí**

Decisió de disseny transversal, ja oberta a `TODO.md §Decisions obertes` i com a TODO a `13_contrib.qmd:480-481`. Dues fases:

- [x] **Fase 1 — proposta**: auditoria feta (vegeu `D_criteri_estil.md`); el corpus ja seguia de facto un criteri semàntic coherent.
- [x] **Aprovació de l'usuari**: les 4 recomanacions (D1–D4) acceptades el 2026-07-04.
- [x] **Fase 2 — aplicació**: criteri integrat a `13_contrib.qmd` (nou §«Codi, matemàtiques i cursiva», §Equacions amb criteri de numeració, §Ressaltat amb negretes en callouts); 20 superíndexs Pandoc → math (T2, E6); apòstrof «d'10⁶» corregit; separadors de milers anglesos de T2 → espais (nova decisió oberta a `TODO.md`); 38 etiquetes `{#eq-}` revisades (totes canòniques, cap canvi); renders de verificació nets. `D_criteri_estil.md` es pot esborrar quan es vulgui.

---

## Bloc E — Ús pedagògic de les referències creuades (assumpte 3.4)

**Config:** Fable / High / **Sí**

Revisió tema a tema (un xat per tema o per parells de temes) de:

- [ ] Densitat: ni seccions òrfenes de referències ni paràgrafs saturats.
- [ ] Direccionalitat: evitar referències cap endavant a conceptes no introduïts (excepte les documentades, p. ex. `fcsr` → `@nte-zicsr`, vegeu `TODO.md §T5 P8`).
- [ ] Coherència Ax ↔ Ex ↔ Sx ↔ Lx: que problemes i laboratori remetin a la secció de teoria pertinent.
- [ ] Convencions de `13_contrib.qmd §referències creuades` (ordre tema → secció → … → equació).

Recomanació: fer-ho **després** dels blocs A i D, perquè els slugs i el criteri d'estil ja estiguin estables.

---

## Bloc F — Solucionaris pendents (de `TODO.md §Solucionaris pendents`)

**Config:** Fable / High / **Sí** (el TODO els marcava «Opus High Thinking»; Fable hi és superior)

Un xat per tema, seguint `S_criteris_seleccio.qmd`:

- [ ] T2: `exr-p3-memoria-endianness`, `exr-p3-vectors-cerca`, `exr-p3-vectors-punter-aritm`, `exr-p3-strings-copia` → `S2.qmd`.
- [ ] T3: `exr-p4-compilacio-auipc`, `exr-p4-memoria-jalr`, `exr-p4-logica-rotacio` (apartat b) → `S3.qmd`.

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
- Qüestió prèvia al bloc A: aclarir l'estat de `01_apunts/T1_.qmd` (no versionat) i dels canvis locals a `A1.qmd`/`A7.qmd` abans de tocar aquests fitxers.
