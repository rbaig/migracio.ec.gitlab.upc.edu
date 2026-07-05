# TODO

## Decisions obertes

Decisions pendents de criteri. Un cop preses, han d'aterrar a `07_contrib.qmd`.

- **`startup.s`**: mantenir o eliminar? Decisió ajornada a la fase de revisió externa. Hipòtesi de treball durant la revisió interna: **no hi ha `startup.s`** (sense SO); tot el material nou es genera sense considerar-lo, i el material existent relatiu a l'opció «amb `startup.s`» es manté comentat (no s'elimina). Blocs comentats amb les instruccions de reactivació: T2.qmd (`#imp-programa-esquelet`/`#imp-exception-handler`, ln 719-784), T3.qmd (`#tip-rars-main-multinivell`, ln 1543-1550), `index.qmd` (descàrrega i configuració de l'*Exception Handler*, ln 181-198). Afecta també PE_T9: `exr-p9-syscall-programa` demana la sortida amb `li a7, 10`; unificar amb `li a7, 93` quan es prengui la decisió.
- **Syntax highlighting**: confirmar que `.s` és correcte per a instruccions, macros i directives de RARS.
- **Coherència de títols en `.callout-caution`**: `07_contrib.qmd` indica sense títol. No és una excepció puntual de T5: és una deriva d'estil real entre temes. Recompte: T2/T3/T4/T9 mai en porten (0 casos); T7 (5/5) i T8 (6/6) sempre en porten; T5 és mixt (4/7 amb títol). Decisió pendent (2026-07-05, deixada oberta expressament): unificar sense títol (coherent amb el criteri actual, 15 callouts a retocar a T5/T7/T8), unificar amb títol (canviar el criteri, 22 callouts a retocar a T2/T3/T4/T9), o valorar cas per cas si el títol aporta valor real.
- **Criteris de codi C**: completar.
- **Plantilles Markdown** (`L2.qmd` i resta): posar-ne a tots excepte `L2.qmd`, o eliminar de `L2.qmd`?
- **Figures portades d'extern**: afegir font (dels PDF n'hi ha que són del Patterson -e.g. T7 MC).

---

## Tasques per tema

### T3

- **Encaix T2↔T3 — caller-saved/callee-saved**: verificar que T2.qmd introdueix els conceptes de registres temporals/segurs de manera consistent amb la terminologia i les referències creuades establertes a T3 en la revisió interna (títol `## RV32I ABI —`, connexió «temporals = *caller-saved*», «segurs = *callee-saved*», refs `@nte-caller-saved-vs-callee-saved`). Fer en un xat nou amb T2.qmd i T3.qmd.
- **Revisar referència `@imp-exception-handler` reparada** (T3.qmd, ~L. 1546, callout `#tip-rars-main-multinivell`): l'etiqueta original no tenia destí; s'ha reescrit apuntant a `@sec-ei-rse` (T9) i retocat la frase perquè tingués sentit gramatical. És una interpretació de Claude Code, no una simple correcció mecànica d'slug — verificar que el destí i la redacció són correctes.
- Retocs manuals pendents (Roger) a les figures:
  - `figs_auto/T3_ba_exemple__original_light.svg`
  - `figs_auto/T3_deps_multi__original_light.svg`
  - `figs_auto/T3_deps_exemple__original_light.svg`

### T5

- **F1 — figures** addicionals: (1) disposició S\|E\|F (32 bits), (2) recta numèrica rang/precisió amb denormals, (3) esquema d'arrodoniment GRS.
- **P7** — Alinear l'ordre de la taula de codificacions especials amb el de les subseccions.
- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present.
- **`#cau-underflow`**: opcionalment reanomenar a `#cau-subdesbordament` (cosmètic; no referenciat).
- Explicar perquè quantitat de denormals 2·(2^(23)-1) v.s. qualsevol rang normalitzat 2·2^(23). Nota: `2·` és per les dues opcions del bit de signe. L'explicació està a draw.io.
- Assegurar que es diu que en denormals bit ocult és 0.

### T6

- SVGs `T6_not_cmos`, `T6_not_1_0`, `T6_not_0_1`: alçades diferents; textos solapats al PDF. Provar les versions `___tracable____original_light.svg`.

### T7 — Figures pendents de creació

Figures pendents (totes requereixen LO Draw de Roger):

| Figura | Descripció | Notes |
| :--- | :--- | :--- |
| `fig-mc-exemple-descomposicio-32bits` | Descomposició 32 bits adreça `0x100100F8` | Export LO Draw existent a `13_figs_externes`; reconstruir com a natiu |
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

8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol `@fig-mv-flux-traduccio` 🔴). Rutes: `/figs_auto/T8_*__original_light.svg`.

### T9

- **E3 — Slugs sense prefix**: `sec-introduccio`, `sec-flux-hardware`, `sec-rse`, `sec-ecall`, `sec-interrupcions`, `sec-tlb`… Risc de col·lisió global. Vegeu pas 1 de la seqüència a `CLAUDE.md`.
- **F/G — Figures SVG**: diferides a una fase posterior.

### Laboratori

- **L2 §«Pseudoinstrucció `la` i `li`»**: el cos de la secció és només «TODO»; redactar-ne el contingut o eliminar la secció.
- **Renumeració de lliuraments (2026-07-05)**: els fitxers de lliurament de L2–L6 s'han renumerat al número de sessió (`s2_*`–`s6_*`; abans anaven una sessió endarrerits i col·lidien amb L1). El directori `laboratori/` conserva els subdirectoris `L0`–`L5` amb `TODO.s`: revisar-ne els noms quan es decideixi el mecanisme de descàrrega.

---

## Tasques globals

### SVG

- **Migració de canvas a amplades estàndard**: figures de BA i mapa de memòria (`W=316 px`) → classe `estreta` (`W=340 px`). Decisió pendent: mantenir `w_rect=230` (marge dret 10→34) o ampliar `w_rect` a 254 (marges simètrics). Un cop decidit, aplicar a les 7 figures afectades i actualitzar `21_specs/svg.md §2`. Figures: `T3_mapa_memoria`, `T3_ba_general`, `T3_ba_func`, `T3_ba_multi`, `T3_ba_exemple`, `T3_func_uninivell_pila`, `T3_pila_crides_aniuades`.
- **Migrar diagrames Mermaid existents a SVG**.

### Contingut global

- **Cometes** `"..."` → `«...»`: substitució global.
- **`****` sobrants**: eliminar.
- **Equacions a MathML**: passar totes les equacions; definir criteris d'inline. **Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`)**: funciona (`underbrace`, `cases`, taules amb math correctes a Chrome), i elimina el JS de MathJax (render instantani, funciona offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), la numeració d'equacions queda inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. Recomanació: mantenir MathJax 3 (el desbordament mòbil ja està resolt via CSS); reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa).
- **PDF**: figures dins callouts no queden centrades → investigar via `preamble.tex`.
- **Gestió d'errades post-commit**: definir protocol (vegeu `07_contrib.qmd §Gestió d'errades`).

### `index.qmd`

- Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir.
- Consolidar taula de referències tècniques (`#imp-llenguatges-de-referencia`): versió ISO de C, versió GCC, toolchain (entrada duplicada).
- Afegir URL de la còpia local de RARS.
