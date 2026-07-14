# TODO

## Decisions obertes

Decisions pendents de criteri. Un cop preses, han d'aterrar a `13_contrib.qmd`.

- **`startup.s`**: mantenir o eliminar? Decisió ajornada a la fase de revisió externa. Hipòtesi de treball durant la revisió interna: **no hi ha `startup.s`** (sense SO); tot el material nou es genera sense considerar-lo, i el material existent relatiu a l'opció «amb `startup.s`» es manté comentat (no s'elimina). Blocs comentats amb les instruccions de reactivació: A2.qmd (`#imp-programa-esquelet`/`#imp-exception-handler`, ln 719-784), A3.qmd (`#tip-rars-main-multinivell`, ln 1543-1550), `index.qmd` (descàrrega i configuració de l'*Exception Handler*, ln 181-198). Afecta també E9: `exr-p9-syscall-programa` demana la sortida amb `li a7, 10`; unificar amb `li a7, 93` quan es prengui la decisió.
- **Syntax highlighting**: confirmar que `.s` és correcte per a instruccions, macros i directives de RARS.
- **Criteris de codi C**: completar.
- **Plantilles Markdown** (`L2.qmd` i resta): posar-ne a tots excepte `L2.qmd`, o eliminar de `L2.qmd`?
- **Figures portades d'extern**: afegir font (dels PDF n'hi ha que són del Patterson -e.g. T7 MC).

---

## Tasques transversals

- **Exercicis** -> Problemes (slugs, callout header, refs, etc.). Detall complet de l'abast (afegit a la revisió interna de T2, xat A2-E2-S2): els IDs d'`Ex.qmd`/`Sx.qmd` usen actualment el prefix `p<N>-` (`#exr-p3-...`, `#sol-p3-...`), numeració llegada de les col·leccions MIPS on `p` feia referència a «problema». Amb la migració a RISC-V, l'estructura és 1 tema = 1 fitxer `Ax.qmd`/`Ex.qmd`/`Sx.qmd`, per tant té més sentit `t<N>-` (de «tema»), coherent amb la numeració de la resta del llibre. Cal: (i) substituir `p<N>-` per `t<N>-` a tots els IDs `#exr-p<N>-*` i `#sol-p<N>-*` de tots els `Ex.qmd`/`Sx.qmd`; (ii) actualitzar totes les referències creuades (`@exr-p<N>-*`, `@sol-p<N>-*`) a tot el repositori (`Ax.qmd` també en pot contenir cap a `Ex.qmd`/`Sx.qmd`); (iii) verificar que no queda cap referència trencada després del canvi. Nota: E1/E3 tenen prefixos `p1-`/`p4-` respectivament, que no es corresponen amb el seu número de tema real (haurien de ser `t1-`/`t3-`) — cal aclarir aquest desajust abans de renumerar. Volum de canvi considerable i mecànic: candidat clar per a Claude Code.

- **Revisió sistemàtica del corpus** per nodrir les taules de `Símbols` i `Notació` de `12_sigles_simbols.qmd`

- **Revisió sistemàtica del corpus** per l'aplicació de la regla d'ús `AND`, `OR`, `XOR`, `NOT`--`barra superior` (enters)

- **Nova eina disponible: retalls (crops) SVG a partir d'una figura font única** (afegida 2026-07-13, revisió interna T5, xat A5-E5-S5): `25_scripts/gen_crops.py` + `24_specs/retalls.toml` (encara buit), integrat al `pre-render` de `_quarto.yml` entre `gen_regs.py` i `gen_dark.py`. Permet definir una figura "detall"/"zoom" com una simple finestra `(x, y, w, h)` sobre el `viewBox` d'una figura font ja existent, sense duplicar-ne el contingut. Documentat a `13_contrib.qmd §Retalls`. Aplicable només quan el detall és un subconjunt geomètric net de la font (cap connector/etiqueta tallat a mig camí); si el detall necessita contingut addicional, continua calent un SVG independent. **Cap ús real encara**, tot i haver-se valorat dues vegades per a les figures de T5: (1) `T5_recta_zoom_zero` com a retall de `T5_recta_global` — descartat perquè `T5_recta_zoom_zero` mostra informació pròpia dels denormals (hexadecimals concrets) que `T5_recta_global` no té espai per representar; (2) `T5_recta_global`/`T5_recta_zoom_zero` com a retalls de `T5_coma_flotant_racionals__drawio.svg` (figura orfe a `22_figs_originals/`, no referenciada per cap `.qmd`, que sembla l'esborrany original del qual es van redibuixar les altres dues) — descartat en l'estat **actual** perquè el drawio (7465 línies, estil amb fletxes/icones pròpies) no comparteix coordenades ni disseny amb les figures actuals en estil pla; són una reconstrucció completa, no un retall.

    **TODO futur**: investigar l'ús de `gen_crops.py` directament sobre una figura global com la primigènia (`T5_coma_flotant_racionals__drawio.svg` o equivalent), és a dir, com a **font única des de zero** en lloc d'intentar-lo a posteriori sobre figures ja redibuixades per separat. Requeriria: (i) redibuixar aquesta figura en estil pla natiu (coherent amb `svg.md`, no drawio) com a única font de veritat amb tot el contingut (rang global + zoom de zero + denormals); (ii) definir a `retalls.toml` les finestres `(x, y, w, h)` corresponents a cada vista actual (`T5_recta_global`, `T5_recta_zoom_zero`) com a retalls d'aquesta font; (iii) verificar que cada retall és net (cap element tallat a mig camí). Si viable, eliminaria la duplicació de manteniment entre les dues figures actuals. No s'ha fet en aquesta revisió perquè implica redibuixar una figura complexa des de zero, fora de l'abast d'una revisió textual.

#### Tasques vives migrades de fitxers esborrables

- ~~**(a) Harmonització notacional `21_riscv/` RV32I/RV32M**: estendre `=` → `\leftarrow` (i revisar `off`/`offset`)…~~ **RESOLTA (2026-07-13, verificat en revisió interna T5, xat A5-E5-S5):** comprovat que tots els fitxers de `21_riscv/` (RV32I, RV32M i RV32F) ja usen `\leftarrow` per a assignació i `offset` sencer arreu; cap ocurrència residual de `=` d'assignació ni d'`off` abreujat a tot el directori. No calia cap canvi.

- **(b) `RV32I_registres_coma_flotant.qmd` divergent de la taula inline de T5**: decidir versió canònica i connectar T5 via include. [de `T5_revisio_canvis.md §F2`] *(Revisat 2026-07-13: es manté sense canvis; la taula inline d'A5 és un resum de 3 categories i l'include reflecteix el desglossament ABI complet de 6 trams — es considera acceptable mantenir totes dues.)*

- **(c) Taules de camps de `fcsr` (frm, fflags)**: també a includes per al compendi, o inline? [de `T5_revisio_canvis.md`] *(Decidit 2026-07-13: es mantenen inline. Sense canvis.)*

- ~~**(e) Criteris de numeració/aparença de callouts**.~~ **RESOLTA (2026-07-13, revisió interna T5, xat A5-E5-S5):** documentat a `13_contrib.qmd §Callouts` que tot callout etiquetat (`#nte-`/`#imp-`/`#cau-`/`#tip-`/`#wrn-`) ja queda numerat automàticament per Quarto via els prefixos `crossref-*-prefix` de `_quarto.yml` (mecanisme natiu, ja actiu; no calia cap canvi). Icones: `custom.scss` personalitza `note`/`warning`/`caution`; `tip`/`important` es deixen deliberadament amb la icona per defecte de Quarto (bombeta i cercle d'exclamació) — decidit, sense homogeneïtzar.

---

## Tasques per tema

### T3

- ~~`WARN: 01_apunts/A3.html: Unable to resolve crossref @wrn-codificacio-enters-ca1`~~ **RESOLTA (verificat 2026-07-13):** `A3.qmd` L. 48 ja usa `@sec-enters-en-ca1` (no `@wrn-codificacio-enters-ca1`). Sense acció.

- **Criteri «quatre formats nuclears» (RISC-V International)**: la revisió interna de T2 (A2.qmd) ha adoptat el criteri de la font de veritat `@riscv_rv32i` (docs.riscv.org, citada a `15_bibliografia.bib`): RV32I té «quatre formats nuclears d'instrucció» (R/I/S/U), amb B i J com a variants de S i U respectivament. A3.qmd ja s'hi ha ajustat parcialment (referències creuades afegides cap a T2 als callouts `#nte-format-b`, `#nte-format-j`, `#nte-format-u`), però cal revisar-lo sencer per aplicar aquest mateix criteri de manera estricta i coherent a tot el tema (redactat, introducció dels formats, qualsevol menció al nombre total de formats). Fer en un xat de revisió interna dedicat a A3.qmd.
- ~~**Encaix T2↔T3 — caller-saved/callee-saved**: verificar que A2.qmd introdueix els conceptes de registres temporals/segurs...~~ **RESOLTA (2026-07-13, xat A2-E2-S2):** l'encaix ja era correcte per construcció (A2 presenta la taula amb la columna «Qui el guarda (*Saver*)» sense anticipar la terminologia anglesa; A3 ja hi remet formalment via `@nte-registres-proposit-general`). S'hi ha afegit, dins el mateix callout `#nte-registres-proposit-general` d'A2.qmd, una remissió puntual («Aquesta distinció es formalitza al Tema 3 amb la terminologia *caller-saved*/*callee-saved*, @nte-caller-saved-vs-callee-saved»), coherent amb el patró ja aplicat a T2 per a altres avançaments terminològics (salts/desplaçaments de bits als bucles, `slt`).
- **Revisar referència `@imp-exception-handler` reparada** (A3.qmd, ~L. 1546, callout `#tip-rars-main-multinivell`): l'etiqueta original no tenia destí; s'ha reescrit apuntant a `@sec-ei-rse` (T9) i retocat la frase perquè tingués sentit gramatical. És una interpretació de Claude Code, no una simple correcció mecànica d'slug — verificar que el destí i la redacció són correctes.
- Retocs manuals pendents (Roger) a les figures:
  - `auto_figs/T3_ba_exemple__original_light.svg`
  - `auto_figs/T3_deps_multi__original_light.svg`
  - `auto_figs/T3_deps_exemple__original_light.svg`

### T5

- ~~**F1 — figures** addicionals: (1) disposició S\|E\|F (32 bits), (2) recta numèrica rang/precisió amb denormals, (3) esquema d'arrodoniment GRS.~~ **RESOLTA (2026-07-13, revisió interna T5, xat A5-E5-S5):** (1) creada — `T5_ieee754_format` afegit a `24_specs/registres.toml` (generada per `gen_regs.py`, mateix pipeline que `T5_fcsr`/`T5_instruccio_tipus_R4`), inserida a A5.qmd després de la fórmula S·E·F (`#fig-ieee754-format`). (3) creada — `22_figs_originals/T5_grs_esquema.svg` (SVG natiu, estil pla coherent amb `T5_recta_global.svg`), inserida després de la llista G/R/S (`#fig-grs-esquema`). (2) **ja existia**: coberta conjuntament per `T5_recta_global.svg` (rang complet, ja inserida a §Rang i precisió) i `T5_recta_zoom_zero.svg` (detall de denormals al voltant de zero, ja inserida a §Denormals) — l'entrada del TODO estava desactualitzada.
- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present.
- ~~**Veu dels enunciats (E5)**: E5 usa la 2a persona del singular…~~ **RESOLTA (2026-07-13, revisió interna T5, xat A5-E5-S5):** E5 harmonitzat a 2a plural; `#tip-` d'A5 harmonitzats a 2a singular (criteri revisat 2026-07); S5 harmonitzat a veu impersonal (referència: S3). Fase C executada: vegeu `T5_P_tasques.md` per al detall complet (correcció crítica del mode d'arrodoniment de `fcvt.w.s`/`fcvt.wu.s`, reordenació de S5 segons E5, grafia «IEEE 754», etc.).

### T6

- **Etiquetes de classe d'instruccions en anglès** a les taules d'E6/S6 («Load», «Store», «Branch», «L/S»…): decidir si es mantenen com a etiquetes de columna/fila (opció actual) o es tradueixen («Lectura», «Escriptura», «Salt»), coherentment amb les substitucions obligatòries de prosa. Revisió pendent 2026-07-12 (`13_contrib.qmd §T6`).

### T7 — Figures pendents de creació

**Pendents del xat de revisió E7/S7 (2026-07):**

- **`exr-p7-assoc-multinivell`: seqüència d'adreces truncada**. L'enunciat diu «seqüència de 28 adreces … : `0, 5, 10, 12, 34, 0, 66, ...`» i amb els tres punts l'exercici no és resoluble. Interpretació probable: 7 adreces repetides 4 vegades (28 accessos). **Contrastar amb el PDF original** i reescriure: «la seqüència de 7 adreces següent, repetida 4 vegades (28 accessos en total): `0, 5, 10, 12, 34, 0, 66`».

Figures pendents (totes requereixen LO Draw de Roger):

| Figura | Descripció | Notes |
| :--- | :--- | :--- |
| `fig-mc-exemple-descomposicio-32bits` | Descomposició 32 bits adreça `0x100100F8` | Export LO Draw existent a `23_figs_externes`; reconstruir com a natiu |
| `fig-cd-diagrama` | Diagrama blocs MC correspondència directa | 🔴 Referència trencada · LO Draw pendent |
| `fig-assoc-conjunts-diagrama` | Diagrama blocs MC associativa per conjunts | 🔴 Referència trencada · LO Draw pendent |
| `fig-ca-diagrama` | Diagrama blocs MC completament associativa | 🔴 Referència trencada · LO Draw pendent |
| `fig-texe-diagrama` | Diagrama temporal lw/addu/lw (etapes F/D/R/A/M/W) | 🔴 Referència trencada · Referència: PDF pàg. 24 |
| `fig-lru-roger` | Màquina d'estats LRU | Ja inclosa dins `T7_lru_exemple.svg`; decidir si cal figura independent |
| `fig-multinivell-diagrama` | CPU→L1→L2→MP | LO Draw pendent |
| `fig-multinivell-multicore` | Xip 4 nuclis L1/L2/L3 | LO Draw pendent |

Decisions obertes de T7:
- 🔵 **`fig-capacitat-exemple` a HTML**: dues figures separades (primera+segona passada) o figura única combinada? Pendent de decisió.

### T8 — Figures pendents de creació

8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol `@fig-mv-flux-traduccio` 🔴). Rutes: `/auto_figs/T8_*__original_light.svg`.

### T9

- **F/G — Figures SVG**: diferides a una fase posterior.

### Laboratori

- **L2 §«Pseudoinstrucció `la` i `li`»**: el cos de la secció és només «TODO»; redactar-ne el contingut o eliminar la secció.
- **Renumeració de lliuraments (2026-07-05)**: els fitxers de lliurament de L2–L6 s'han renumerat al número de sessió (`s2_*`–`s6_*`; abans anaven una sessió endarrerits i col·lidien amb L1). El directori `laboratori/` conserva els subdirectoris `L0`–`L5` amb `TODO.s`: revisar-ne els noms quan es decideixi el mecanisme de descàrrega.

---

## Tasques globals

### SVG

- **Migració de canvas a amplades estàndard**: figures de BA i mapa de memòria (`W=316 px`) → classe `estreta` (`W=340 px`). Decisió pendent: mantenir `w_rect=230` (marge dret 10→34) o ampliar `w_rect` a 254 (marges simètrics). Un cop decidit, aplicar a les 7 figures afectades i actualitzar `24_specs/svg.md §2`. Figures: `T3_mapa_memoria`, `T3_ba_general`, `T3_ba_func`, `T3_ba_multi`, `T3_ba_exemple`, `T3_func_uninivell_pila`, `T3_pila_crides_aniuades`.

### Neteja de warnings del render

- **A1. Slugs `{#sec-}` a T1, T2 i T5**: afegir identificadors a totes les capçaleres `##`–`####` segons criteris de `13_contrib.qmd` (referència: `A4.qmd`). Excloure capçaleres dins callouts. Verificació global de col·lisions entre temes.
- **A2. Identificador duplicat `sec-opt-acces-sequencial`**: definit dues vegades (T2 i T4). *(Verificat 2026-07-13 amb A2.qmd i A4.qmd disponibles: a `A2.qmd` L. 1982 només hi ha una **referència** `@sec-opt-acces-sequencial`, no una segona definició `{#sec-opt-acces-sequencial}`; la definició real és a `A4.qmd` L. 463. Confirmat de nou 2026-07-13 amb A2.qmd sencer disponible: **cap definició `{#sec-opt-acces-sequencial}` a tot A2.qmd**, només la referència `@`. No s'ha trobat la col·lisió amb aquests dos fitxers — la segona definició deu ser a un tercer fitxer no revisat (laboratori, o algun `Ex.qmd`/`Sx.qmd`). Cal aportar més fitxers per localitzar-la.)*
- **A3. Div sense tancar a `A7.qmd`**: localitzar `:::` desaparellat (warning L168–1981) i reparar.
- **A4. Referències creuades no resoltes (reparables)**: `@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila`, `@imp-exception-handler`. *(Verificat 2026-07-13: `@sec-politica-reemplacement` **ja no aplica** — l'slug real `sec-politica-reemplacament` ja s'usa consistentment a `A7.qmd` L. 321, 433, 643; probablement error tipogràfic en aquesta mateixa entrada del TODO. Amb A1–A9 disponibles, `@sec-ecall`, `@sec-operands-memoria` i `@imp-ec-alineacio-pila` no apareixen citats enlloc — la citació trencada deu ser a E9/S9/laboratoris o a `13_contrib.qmd`, no revisats. `A9.qmd` L. 499 defineix `{#sec-ei-ecall}` — probablement l'slug correcte al qual hauria d'apuntar `@sec-ecall`. Verificat també 2026-07-13, xat A2-E2-S2: cap de les tres cites `@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila` apareix a A2.qmd, E2.qmd ni S2.qmd — descartat T2 com a origen, la cerca es pot acotar a E9/S9/laboratoris/`13_contrib.qmd`.)* i refs internes trencades de `13_contrib.qmd`.

### Contingut global

- **Criteri «quatre formats nuclears d'instrucció» (RISC-V International)**: adoptat a la revisió interna de T2 (2026-07, xat A2-E2-S2). Font de veritat: `@riscv_rv32i` (docs.riscv.org, «four core instruction formats (R/I/S/U)»; B i J són variants de S i U). Revisar tots els fitxers del repositori (`Ax.qmd`, `Ex.qmd`, `Sx.qmd`, `11_riscv.qmd`, laboratoris) que esmentin el nombre total de formats d'instrucció de RV32I («sis formats», «6 formats», etc.) i ajustar-los a aquest criteri, amb el mateix matís sobre B/J com a variants de S/U. Punt de partida ja fet: A2.qmd (T2) i referències creuades puntuals a A3.qmd (T3, vegeu `§T3` més amunt).
- **«ample de banda» → «amplada de banda»**: substitució global (afegida a les substitucions obligatòries de `13_contrib.qmd`; T7 ja fet. *Verificat 2026-07-13: cap ocurrència de «ample de banda» a A1–A6, A8, A9 — nets. Verificat també 2026-07-13, xat A2-E2-S2: cap ocurrència a E2.qmd ni S2.qmd — nets. No revisats: E/S de T1, T3–T6, T8, T9, laboratoris.*).
- **Unitats KB/KiB**: revisar la resta de temes segons el criteri de `13_contrib.qmd §T7` (binàries per a registres/MC/MP; decimals per a emmagatzematge secundari, costos i amplades de banda; T7 ja fet. *Verificat 2026-07-13: única ocurrència de KB a A1–A9 és A2.qmd L. 178, dins la taula que **defineix** el criteri KiB vs. KB — correcta, no cal cap canvi. Verificat també 2026-07-13, xat A2-E2-S2: cap ocurrència de KB a E2.qmd ni S2.qmd — nets. No revisats: E/S de T1, T3–T6, T8, T9, laboratoris.*).
- **Cometes** `"..."` → `«...»`: substitució global. *(Verificat 2026-07-13 a A7/E7/S7: totes les cometes trobades són atributs YAML de Quarto (`tbl-colwidths="..."`, `collapse="true"`), no prosa — cap cas real en aquests tres fitxers. Verificat també 2026-07-13, xat A2-E2-S2: mateix resultat a E2.qmd/S2.qmd (69 ocurrències, totes `filename="..."` de blocs de codi) — cap cas real. No revisats: la resta.)*
- **`****` sobrants**: eliminar. *(Verificat 2026-07-13: cap ocurrència a A1–A9, E7, S7, `13_contrib.qmd`. Verificat també 2026-07-13, xat A2-E2-S2: cap ocurrència a E2.qmd ni S2.qmd.)*
- **Equacions a MathML**: passar totes les equacions; definir criteris d'inline. **Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`)**: funciona (`underbrace`, `cases`, taules amb math correctes a Chrome), i elimina el JS de MathJax (render instantani, funciona offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), la numeració d'equacions queda inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. Recomanació: mantenir MathJax 3 (el desbordament mòbil ja està resolt via CSS); reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa).
- **PDF**: figures dins callouts no queden centrades → investigar via `preamble.tex`. A més, comportament en callouts encastats: es respecta la separació (`-1` del `layout=`), però no el repartiment si hi ha línies de text que no hi caben (falta l'exemple concret de `13_contrib.qmd`).
- **Figures externes (llicències)**: taula completa de figures extretes de PDFs (inclús fonts, llicències). Referència eliminada temporalment de `13_contrib.qmd`.
- **Gestió d'errades post-commit**: definir protocol (vegeu `13_contrib.qmd §Gestió d'errades`).

### `index.qmd`

- ~~Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir.~~ **RESOLTA (verificat 2026-07-13):** ja no hi ha cap enllaç a `laboratori/L0/TODO.s` a `index.qmd`.
- ~~Consolidar taula de referències tècniques (`#imp-llenguatges-de-referencia`): versió ISO de C, versió GCC, toolchain (entrada duplicada).~~ **RESOLTA parcialment (verificat 2026-07-13):** la fila duplicada de Toolchain ja no hi és; la taula (L. 247-254) té una sola fila per ítem. Pendent encara: versió ISO de C i versió GCC (marcades amb `<!-- TODO -->` a les línies anteriors a la taula), fora de l'abast d'aquest xat (calen decisions de contingut, no una neteja mecànica).
- ~~Afegir URL de la còpia local de RARS.~~ **RESOLTA (verificat 2026-07-13):** ja hi és, L. 179 (`<a href="04_laboratori/rars1_6.jar" download>Còpia local</a>`).
