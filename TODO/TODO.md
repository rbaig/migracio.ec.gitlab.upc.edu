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

#### Tasques vives migrades de fitxers esborrables

- **(a) Harmonització notacional `21_riscv/` RV32I/RV32M**: estendre `=` → `\leftarrow` (i revisar `off`/`offset`) als fitxers RV32I/RV32M llistats a `prompt_claude_code_harmonitzacio_rv32f.md §Fora d'abast`; coordinar amb les revisions de T2/T3/T4/T9 que els inclouen. [de `prompt_…rv32f.md` + `T5_revisio_canvis.md`]

- **(b) `RV32I_registres_coma_flotant.qmd` divergent de la taula inline de T5**: decidir versió canònica i connectar T5 via include. [de `T5_revisio_canvis.md §F2`]

- **(c) Taules de camps de `fcsr` (frm, fflags)**: també a includes per al compendi, o inline? [de `T5_revisio_canvis.md`]

- **(d) T5 P7**: alinear l'ordre de la taula de codificacions especials amb el de les subseccions, o frase pont. [de `T5_revisio_canvis.md`]

- **(e) Criteris de numeració/aparença de callouts**. [de `13_contrib.qmd §Callouts`]

---

## Tasques per tema

### T3

- `WARN: 01_apunts/A3.html: Unable to resolve crossref @wrn-codificacio-enters-ca1`

- **Criteri «quatre formats nuclears» (RISC-V International)**: la revisió interna de T2 (A2.qmd) ha adoptat el criteri de la font de veritat `@riscv_rv32i` (docs.riscv.org, citada a `15_bibliografia.bib`): RV32I té «quatre formats nuclears d'instrucció» (R/I/S/U), amb B i J com a variants de S i U respectivament. A3.qmd ja s'hi ha ajustat parcialment (referències creuades afegides cap a T2 als callouts `#nte-format-b`, `#nte-format-j`, `#nte-format-u`), però cal revisar-lo sencer per aplicar aquest mateix criteri de manera estricta i coherent a tot el tema (redactat, introducció dels formats, qualsevol menció al nombre total de formats). Fer en un xat de revisió interna dedicat a A3.qmd.
- **Encaix T2↔T3 — caller-saved/callee-saved**: verificar que A2.qmd introdueix els conceptes de registres temporals/segurs de manera consistent amb la terminologia i les referències creuades establertes a T3 en la revisió interna (títol `## RV32I ABI —`, connexió «temporals = *caller-saved*», «segurs = *callee-saved*», refs `@nte-caller-saved-vs-callee-saved`). Fer en un xat nou amb A2.qmd i A3.qmd.
- **Revisar referència `@imp-exception-handler` reparada** (A3.qmd, ~L. 1546, callout `#tip-rars-main-multinivell`): l'etiqueta original no tenia destí; s'ha reescrit apuntant a `@sec-ei-rse` (T9) i retocat la frase perquè tingués sentit gramatical. És una interpretació de Claude Code, no una simple correcció mecànica d'slug — verificar que el destí i la redacció són correctes.
- Retocs manuals pendents (Roger) a les figures:
  - `auto_figs/T3_ba_exemple__original_light.svg`
  - `auto_figs/T3_deps_multi__original_light.svg`
  - `auto_figs/T3_deps_exemple__original_light.svg`

### T5

- **F1 — figures** addicionals: (1) disposició S\|E\|F (32 bits), (2) recta numèrica rang/precisió amb denormals, (3) esquema d'arrodoniment GRS.
- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present.
- **Veu dels enunciats (E5)**: E5 usa la 2a persona del singular («Contesta les preguntes…») en lloc de la 2a del plural («Contesteu»), convenció establerta a partir de la revisió de T7/T6. Harmonitzar en una propera passada d'E5.

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
- **Migrar diagrames Mermaid existents a SVG**.

### Neteja de warnings del render

- **A1. Slugs `{#sec-}` a T1, T2 i T5**: afegir identificadors a totes les capçaleres `##`–`####` segons criteris de `13_contrib.qmd` (referència: `A4.qmd`). Excloure capçaleres dins callouts. Verificació global de col·lisions entre temes.
- **A2. Identificador duplicat `sec-opt-acces-sequencial`**: definit dues vegades (T2 i T4). Decidir quin és canònic i reanomenar l'altre.
- **A3. Div sense tancar a `A7.qmd`**: localitzar `:::` desaparellat (warning L168–1981) i reparar.
- **A4. Referències creuades no resoltes (reparables)**: `@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila`, `@imp-exception-handler`, `@sec-politica-reemplacement`, i refs internes trencades de `13_contrib.qmd`.

### Contingut global

- **Criteri «quatre formats nuclears d'instrucció» (RISC-V International)**: adoptat a la revisió interna de T2 (2026-07, xat A2-E2-S2). Font de veritat: `@riscv_rv32i` (docs.riscv.org, «four core instruction formats (R/I/S/U)»; B i J són variants de S i U). Revisar tots els fitxers del repositori (`Ax.qmd`, `Ex.qmd`, `Sx.qmd`, `11_riscv.qmd`, laboratoris) que esmentin el nombre total de formats d'instrucció de RV32I («sis formats», «6 formats», etc.) i ajustar-los a aquest criteri, amb el mateix matís sobre B/J com a variants de S/U. Punt de partida ja fet: A2.qmd (T2) i referències creuades puntuals a A3.qmd (T3, vegeu `§T3` més amunt).
- **«ample de banda» → «amplada de banda»**: substitució global (afegida a les substitucions obligatòries de `13_contrib.qmd`; T7 ja fet, revisar la resta de temes, p. ex. amb Claude Code).
- **Unitats KB/KiB**: revisar la resta de temes segons el criteri de `13_contrib.qmd §T7` (binàries per a registres/MC/MP; decimals per a emmagatzematge secundari, costos i amplades de banda; T7 ja fet).
- **Cometes** `"..."` → `«...»`: substitució global.
- **`****` sobrants**: eliminar.
- **Equacions a MathML**: passar totes les equacions; definir criteris d'inline. **Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`)**: funciona (`underbrace`, `cases`, taules amb math correctes a Chrome), i elimina el JS de MathJax (render instantani, funciona offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), la numeració d'equacions queda inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. Recomanació: mantenir MathJax 3 (el desbordament mòbil ja està resolt via CSS); reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa).
- **PDF**: figures dins callouts no queden centrades → investigar via `preamble.tex`. A més, comportament en callouts encastats: es respecta la separació (`-1` del `layout=`), però no el repartiment si hi ha línies de text que no hi caben (falta l'exemple concret de `13_contrib.qmd`).
- **Figures externes (llicències)**: taula completa de figures extretes de PDFs (inclús fonts, llicències). Referència eliminada temporalment de `13_contrib.qmd`.
- **Gestió d'errades post-commit**: definir protocol (vegeu `13_contrib.qmd §Gestió d'errades`).

### `index.qmd`

- Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir.
- Consolidar taula de referències tècniques (`#imp-llenguatges-de-referencia`): versió ISO de C, versió GCC, toolchain (entrada duplicada).
- Afegir URL de la còpia local de RARS.
