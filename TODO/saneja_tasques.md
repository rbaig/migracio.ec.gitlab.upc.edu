# Sanejament dels fitxers operacionals — llista d'accions

**Abast:** `CLAUDE.md`, `13_contrib.qmd`, `TODO/` (excepte `TODO/laboratori`).
**Generat:** 2026-07-12, Fase B (Fable 5 High + Thinking), amb verificacions contra el repositori (`raw.githubusercontent.com`, branca `main`).
**Fase C completada:** 2026-07-12 (Sonnet High, sense Thinking).
**Llegenda:** [C] correcció executable · [D] decisió de l'usuari · [V] verificació pendent.
**Criteri acordat:** els registres `T*_P_tasques.md` **no** es tanquen ni s'esborren en aquest sanejament (ho declara l'usuari); només s'hi resolen duplicitats.

**RESUM FASE C:**
- ✅ Tots els ítems [C] (seccions 1-4) executats
- ✅ Decisions [D] (1.4–1.7, 2.9, 4.5, §5) aplicades segons les ordres de l'usuari
- ✅ 7 fitxers esborrats, `pla_tasques.md` migrat a `TODO.md` i esborrat
- ✅ Fitxers modificats: `CLAUDE.md`, `13_contrib.qmd`, `TODO.md`, `T2_P_tasques.md`
- ⏳ Verificacions [V] pendents: 2.8 (render), 4.4 (log.log recent)

---

## 1. `CLAUDE.md`

- [C] **1.1** L30: `sigles.md` → `12_sigles_simbols.qmd` (nom real verificat; el fitxer va ser renomenat des de `12_sigles.qmd` el 2026-07-12).
- [C] **1.2** §Estat dels materials, E3/S3: eliminar «Pendent: afegir solucions a `S3.qmd` … (vegeu `TODO/TODO.md §Solucionaris pendents`)» — **obsolet**: les 7 solucions (Bloc F) són al repositori (verificat: `sol-p3-memoria-endianness`, `sol-p3-vectors-cerca`, `sol-p3-vectors-punter-aritm`, `sol-p3-strings-copia` a `S2.qmd`; `sol-p4-logica-rotacio`, `sol-p4-memoria-jalr`, `sol-p4-compilacio-auipc` a `S3.qmd`). La secció `TODO.md §Solucionaris pendents` ja no existeix.
- [C] **1.3** Mateixa subsecció: la segona referència a `TODO/TODO.md §Solucionaris pendents` (a «pas combinat») també apunta a secció inexistent; eliminar o reapuntar.
- [D] **1.4** §Model i effortness: la taula és **pre-Fable** i és la tercera font de configuracions recomanades, divergent de `pla_tasques.md §Ordre d'execució` i de la plantilla `Ax_Ex_Sx`. Proposta: fer de `CLAUDE.md §Model i effortness` **l'única font canònica**, actualitzada amb Fable (revisió profunda: Fable High + Thinking; execució/Fase C: Sonnet High sense Thinking; tasques mecàniques: Sonnet Low), i que plantilla i altres fitxers hi remetin en lloc de repetir valors.
- [D] **1.5** §Seqüència de revisió pendent: el punt 2 diu «(T3 completat.)» però ara T1 està tancat (Fase C executada), T2/T3/T8 tenen Fase C pendent i T4/T6/T7 estan quasi tancats. Actualitzar l'estat o substituir la llista per una remissió a `TODO.md` (evita una segona font d'estat que caduca).
- [D] **1.6** §Figures SVG: política de generació — **solapament** amb `13_contrib.qmd §Figures i material gràfic` (generació dark descrita a tots dos; tots dos remeten a `svg.md`). Segons el repartiment declarat al mateix `CLAUDE.md` («qualsevol decisió de format/convenció va a `13_contrib.qmd`»), la política de generació és convenció → moure-la a `13_contrib.qmd` i deixar a `CLAUDE.md` només un punter. Alternativa conservadora: mantenir-la però eliminar-ne els paràgrafs duplicats (generació dark, flux pre-render).
- [D] **1.7** §Etiquetes `{#sec-}`: els *criteris de generació d'slug* són convenció de format → mateix cas que 1.6: candidats a moure a `13_contrib.qmd` (l'*estat* «complet» sí que és operacional i pot quedar-se o purgar-se un cop consolidat).

## 2. `13_contrib.qmd`

- [C] **2.1** L324 i L327: `sigles.md` → `12_sigles_simbols.qmd` (×2).
- [C] **2.2** L562 (§Bibliografia): «al fitxer `bibliografia.qmd`» → `15_bibliografia.bib` (verificat: `bibliografia.qmd` no existeix; `15_bibliografia.bib` HTTP 200). Revisar també l'exemple de L388 («Noms de fitxers `A1.qmd`, `bibliografia.qmd`») — com a exemple genèric pot quedar-se, però val més usar un nom real.
- [C] **2.3** §Figures Graphviz, taula «Figures Graphviz existents»: **contradiu la seva pròpia convenció** (declarada dues línies abans: font `.gv` a `22_figs_originals/`, sortida a `auto_figs/`). La taula diu font=`24_specs/T7_mc_politiques_resum__graphviz.svg` i sortida=`22_figs_originals/…__graphviz.svg.svg` (extensió duplicada). Verificar les rutes reals al repositori i corregir la taula.
- [C] **2.4** §Integració al `.qmd`: bloc de codi amb tancament penjat (un ``` ``` `` sobrant després de la línia «l'esclat es fa amb `width="40%"`»); a més, «l'esclat» sembla errata per «l'escalat», i la vinyeta comença en minúscula.
- [C] **2.5** §Verificació de l'entorn: la vinyeta final («Només es permeten referències sense resoldre cap a seccions… etiquetes provisionals…») no té relació amb la verificació de l'entorn — és una convenció de referències creuades. Moure-la a §Referències creuades.
- [C] **2.6** **TODOs en comentaris HTML** — duplicitats amb `TODO.md` (el lloc canònic de tasques segons la pròpia guia):
    - (a) §Integració al `.qmd`: TODO «figures dins callouts… PDF… preamble.tex» — **duplicat exacte** de `TODO.md §Contingut global (PDF)`. Eliminar el comentari; deixar `TODO.md` com a única entrada.
    - (b) §Gestió d'errades: TODO «Definir protocol…» — **referència circular**: `TODO.md` diu «vegeu `13_contrib.qmd §Gestió d'errades`» i aquella secció només conté aquest TODO. Deixar la tasca només a `TODO.md` (sense la remissió circular) i eliminar la secció buida de `13_contrib.qmd` (o deixar-hi una línia «pendent de definir, vegeu TODO»).
    - (c) §Callouts: TODO «Revisar criteris de numeració de callouts i aparença» — no consta a `TODO.md`: migrar-lo a `TODO.md §Contingut global` i treure el comentari.
    - (d) §Figures externes (llicències) i §HTML callouts encastats: TODOs que documenten les dues refs eliminades temporalment (`#sec-llicencia-figures-externes`, `#sec-contrib-callout-aprofundiment`) — coherents amb `pla_tasques.md §A4`; migrar a `TODO.md` si `pla_tasques.md` es buida (vegeu §4).
- [C] **2.7** §IAs: la llista «Cal passar-los sempre els fitxers següents…» **duplica amb divergències** `CLAUDE.md §Fitxers de referència obligatòria` (allà hi ha `index.qmd`; aquí no; aquí s'hi afegeix `CLAUDE.md` mateix). Deixar una sola llista canònica a `CLAUDE.md` i reduir §IAs a una remissió («vegeu `CLAUDE.md`») + la frase de revisió obligatòria del contingut generat.
- [V] **2.8** `@sec-nom` (L193-194): és un **placeholder d'exemple** dins backticks, no una ref trencada real; si el render l'avisa (segons `pla_tasques.md §A4`), reformular perquè Quarto no l'interpreti (p. ex. `@sec-〈nom〉`).
- [D] **2.9** §Convencions globals del laboratori: «No es fa servir `startup.s`» s'afirma com a fet tancat, però `TODO.md §Decisions obertes` la manté com a **decisió ajornada** (hipòtesi de treball). Afegir-hi el matís («hipòtesi de treball durant la revisió interna, vegeu `TODO.md`») o deixar-ho com està si es considera que per al laboratori és definitiu.

## 3. `TODO/TODO.md`

- [C] **3.1** Purgar les dues entrades resoltes ratllades: «Coherència de títols en `.callout-caution`» (§Decisions obertes) i «SVGs `T6_not_*`» (§T6) — les notes de resolució ja consten al registre T2 i a `13_contrib.qmd §T6` respectivament.
- [C] **3.2** §Tasques transversals: «"Sigles i símbols" → Afegir secció "Símbols"» — **resolta** (verificat: `12_sigles_simbols.qmd` té `## Símbols` a L102, i el fitxer ja duu el nom nou). Eliminar.
- [C] **3.3** **Afegir-hi les tasques vives que ara només viuen en fitxers esborrables** (vegeu §5):
    - (a) *Harmonització notacional `21_riscv/` RV32I/RV32M*: estendre `=` → `\leftarrow` (i revisar `off`/`offset`) als fitxers RV32I/RV32M llistats a `prompt_claude_code_harmonitzacio_rv32f.md §Fora d'abast`; coordinar amb les revisions de T2/T3/T4/T9 que els inclouen. [de `prompt_…rv32f.md` + `T5_revisio_canvis.md`]
    - (b) *`RV32I_registres_coma_flotant.qmd` divergent de la taula inline de T5*: decidir versió canònica i connectar T5 via include. [de `T5_revisio_canvis.md §F2`]
    - (c) *Taules de camps de `fcsr` (frm, fflags)*: també a includes per al compendi, o inline? [de `T5_revisio_canvis.md`]
    - (d) *T5 P7*: alinear l'ordre de la taula de codificacions especials amb el de les subseccions, o frase pont. [de `T5_revisio_canvis.md`]
    - (e) *Criteris de numeració/aparença de callouts*. [de `13_contrib.qmd §Callouts`, vegeu 2.6c]

## 4. `TODO/pla_tasques.md`

- [C] **4.1** Blocs B, C i D: completats (tots els ítems [x] llevat de dos opcionals del C) — purgar-los segons la pròpia norma del fitxer («cada tasca s'esborra quan es completa»), migrant abans a `TODO.md` els dos residus del Bloc C: (i) opcional `aligned/split` per a equacions llargues; (ii) avís d'adaptació de selectors CSS si mai es migra a MathML (ja parcialment cobert a `TODO.md §Equacions a MathML` — fusionar).
- [C] **4.2** Bloc E: contradicció amb `E_tasques.md`, que declara l'anàlisi de tot el corpus **feta i aplicada** (2026-07-05, decisions resoltes). Marcar el Bloc E com a completat i purgar-lo (la feina viva que en queda ja està repartida als registres T* i a `TODO.md`).
- [C] **4.3** Bloc F: completat (verificat al repo, vegeu 1.2). Purgar.
- [V] **4.4** Bloc A (warnings del render): estat **no verificable des d'aquí** sense un `log.log` recent. Demanar a l'usuari un render actual o marcar-ho per verificar en el proper `make render`. Nota: la taula «Ordre d'execució recomanat» quedarà obsoleta si s'adopta 1.4 (font única de configuracions a `CLAUDE.md`).
- [D] **4.5** Si després de 4.1–4.4 només queda el Bloc A viu: valorar fusionar-lo dins `TODO.md §Tasques globals` i **esborrar `pla_tasques.md`** (un fitxer de planificació menys a mantenir).

## 5. Fitxers candidats a esborrar [D — decisió de l'usuari, cap ja aplicat conté informació única no migrada un cop fets 3.3 i 4.x]

| Fitxer | Motiu | Condició prèvia |
|:---|:---|:---|
| `D_criteri_estil.md` | Integrat a `13_contrib.qmd`; `pla_tasques.md §D` ja deia «es pot esborrar» | Cap |
| `E_tasques.md` | Aplicat íntegrament (2026-07-05); conté refs al nom antic `07_contrib` | 4.2 |
| `F_tasques.md` | Aplicat (verificat al repo) | 4.3 |
| `prompt_claude_code_harmonitzacio_rv32f.md` | Aplicat (verificat: 7 `\leftarrow`, `offset` corregit) | 3.3a |
| `T5_figures_integracio.md` | Aplicat (verificat: `fig-exponent-ieee754`, `fig-recta-global` a `A5.qmd`) | [V] confirmar la 3a figura (recta zoom al zero) |
| `T5_revisio_canvis.md` | Registre històric; pendents migrats | 3.3b-d |
| `T7_tasques.md` | **Duplicat pur**: `TODO.md §T7` en conté un superconjunt més recent (mateixa taula de 8 figures + mateixes 2 decisions + l'ítem de la seqüència truncada) | Cap |

## 6. Registres `T*_P_tasques.md` (només duplicitats; no es tanquen)

- **Es mantenen tots** (`T1`–`T8`): T1 tancat de facto però la declaració de tancament és de l'usuari; T3/T8 amb Fase C pendent; T4/T6/T7 amb ítems ⏳/🔵; T2 vegeu 6.2.
- **6.1 Verificació dirigida feta (2026-07-12)**: totes les afirmacions «aplicat a `13_contrib.qmd`» / «anotat a `TODO.md`» dels 7 registres s'han contrastat contra els fitxers reals i són **certes** (subseccions §T6/§T7 de contrib, veu plural dels enunciats, «amplada de banda», entrades TODO §T5/§T6/§T7, retirada de P3, `12_sigles_simbols` a §T6). Cap forat silenciós. Cap incompatibilitat de criteris entre registres (singular `#tip-` vs plural `#exr-`, unitats, numeració d'optimitzacions: tot coherent i ben distingit a contrib).
- [C] **6.2 ⚠ Estat estantís a `T2_P_tasques.md`**: la cua diu «*Fase C pendent*», però al repositori la secció A està (totalment o parcial) **executada**: includes `RV32I_pseudo_mv/li` a `A2.qmd` L527/L543 (A.6), referència A2→A7 corregida a contrib L258 (A.22), adreça `0x00400014` aplicada (B.12). Corregir la nota d'estat del registre (o verificar ítem a ítem la secció A abans de declarar-lo) per evitar una reexecució o confusió.
- [D] **6.3** Criteri **LSb/MSb (bits) vs LSB/MSB (bytes)** (aplicat a T1 segons el seu registre): només consta a `12_sigles_simbols.qmd` i al registre T1 — no està registrat a `13_contrib.qmd`. Si és convenció de tot el llibre, registrar-la (p. ex. a §Sigles o a una subsecció §T1).
- [V] **6.4** (Fora d'abast del sanejament, per a les properes sessions de revisió): confirmar l'estat real dels 🔵 de T6 (14) i T7 (15) — molts semblen resolts dins dels xats respectius però el recompte de marques no ho distingeix.

## 7. Ordre d'execució proposat per a la Fase C

1. Correccions de text puntuals [C]: 1.1–1.3, 2.1–2.5, 3.1–3.2.
2. Migracions a `TODO.md` [C]: 3.3, 2.6, 4.1–4.3.
3. Decisions [D] a presentar a l'usuari: 1.4–1.7, 2.9, 4.5, i la llista d'esborraments del §5.
4. Verificacions [V]: 2.8 i 4.4 (amb render), §5 T5-figures (3a figura).

**Configuració recomanada per a la Fase C:** Claude Code (Sonnet, effort High, sense Thinking), perquè és edició directa multi-fitxer sobre el repositori (correccions, migracions de blocs, esborraments); alternativament, claude.ai amb Sonnet High sense Thinking oferint els fitxers modificats per descarregar.
