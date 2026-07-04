# TODO

## Decisions obertes

Decisions pendents de criteri. Un cop preses, han d'aterrar a `07_contrib.qmd`.

- **`startup.s`**: mantenir o eliminar? Proposta: eliminar; forçar `li a7, 93` + `ecall`. Afecta T2: `#nte-programa-esquelet` i blocs comentats `__start`/`a7,10` (ln 742-772).
- ~~**Retorn de 2 paràmetres**: restricció EC a 1 resultat (`a0`) o ampliar a 2 (`a0`/`a1`)? Posició d'Adrià: ampliar, el segon com a codi d'error. Afecta T3 (L1106).~~ → ✓ Decisió: `a0` i `a1` (fins a dos resultats escalars). Ja implementat a `{#nte-abi-pas-parametres}` (T3, L1140).
- ~~**Alineació de la pila**: múltiples de 16 (ABI real) o mantenir relaxació a múltiples de 4?~~ → ✓ Decisió: múltiples de **4** a EC (relaxació pedagògica). L'ABI estàndard (×16) es menciona a `{#nte-abi-alineacio-pila}`. Afecta T3 (L1322) i `{#imp-ec-alineacio-pila}` (si existeix).
- ~~**`.globl` vs `.global`**: quin usar als exemples?~~ → ✓ Decisió: `.globl`. Documentat a `07_contrib.qmd §T2 i T3`.
- **`ret` vs `jalr x0, 0(ra)`**: criteri al retorn de funcions. Pendent de consens del professorat. Criteri provisional: `ret` als exemples (pseudoinstrucció estàndard, més llegible).
- **Adreces de memòria**: format `0x00000000` o `0x0000 0000` (espai cada 4 nibbles)? Pendent de decisió global. Criteri provisional: sense espais (`0x10010000`), coherent amb l'ús actual a T2–T9.
- **`.section`**: usar o no? si sí, amb quin criteri?
- ~~**Directives**: títol de callout `## Directives —` o `## RARS —`?~~ → ✓ Decisió: `## Directives —` (genèric) per a callouts amb directives estàndard GNU AS; `## RARS —` per a comportament exclusiu de RARS. Aplicat a T2 i T3.
- **ISA/ABI**: on posar la informació de l'ABI de RV? `{.callout-note}` `## RV32I ABI —` o `{.callout-important}`?
- **Syntax highlighting**: confirmar que `.s` és correcte per a instruccions, macros i directives de RARS.
- **Negretes dins de callouts vs. cos del text**: definir criteri.
- **Noms de registres CSR al cos del text**: amb o sense backtick?
- **Numeració d'equacions**: només les referenciades? totes? les importants?
- **LaTeX math vs. backticks**: definir contextos (cos del text, títols de secció, títols de callout, cel·les de taula, captions, blocs de codi).
- **Coherència de títols en `.callout-caution`**: `07_contrib.qmd` indica sense títol; a T5 alguns en porten. Excepció o unificar?
- **Criteris de codi C**: completar.
- **Estudi previ de laboratori** (`L1.qmd`–`L6.qmd`): lliurar com a fitxers separats o integrat al `.qmd`?
- **Plantilles Markdown** (`L2.qmd` i resta): posar-ne a tots excepte `L2.qmd`, o eliminar de `L2.qmd`?
- **Descàrrega de `laboratori/`**: codi encastat per C&P o fitxers descarregables?
- **Figures portades d'extern**: afegir font (dels PDF n'hi ha que són del Patterson -e.g. T7 MC)

---

## Tasques per tema

### T2

- ~~Verificar a RARS: `.byte 0101` (octal, ln 2082)~~ → ✓ `0101₈ = 65`. Corregit el comentari.
- ~~`.byte`/`.half`/... sense operands (ln 1112)~~ → ✓ Nota corregida; eliminar la instrucció sense operands.
- ~~`li` amb `lo₁₂==0` (ln 524)~~ → ✓ TODO eliminat; nota aclarida.
- ~~`#tbl-tipus-alineacio` sense caption~~ → ✓ Caption afegit.
- ~~Nota `07_contrib.qmd` §T2/T4 imprecisa~~ → ✓ Verificat que el text actual de `07_contrib.qmd` ja és precís.
- ~~Redundància «modularitat» (ln 57/69/86)~~ → ✓ L. 86 reformulada.

### T3

- ~~Corregir etiqueta `#cau-instruccions-no-sla` (ln 106): parla de `sla`/`slai`, no de `lwu`. Reanomenar a la revisió de T3.~~ → ✓ El slug és correcte: el callout parla de `sla`/`slai`. El TODO era imprecís.
- ~~Revisió del fragment AND/OR/XOR (`git show a288aaf`): `#cau-cas-extensio-zero`, `#cau-immediats-logics-extensio-signe`, títol `#nte-pseudoinstruccio-not`, composició `nor`.~~ → ✓ Resolt en la revisió interna: callout redundant eliminat, `#cau-immediats-logics-extensio-signe` reescrit amb exemple numèric, títol `not` corregit, `nor` eliminat.
- ~~TODO Adrià: validar integració del patch AND/OR/XOR (`git show a288aaf`).~~ → ✓ Fragment integrat i revisat. Pendent validació d'Adrià sobre la terminologia «unes expressions» (L. 253, vegeu ítem pendent a continuació).
- ~~**Referència trencada `@nte-pseudoinstruccions-salt-condicional-zero`** (T3): verificar on ha d'apuntar (probablement T2 o compendi `05_riscv.qmd`) i reparar.~~ → ✓ El callout és `#nte-pseudoinstruccions-salt-zero` (T3 §4). Referència corregida a T3.qmd L. 255.
- **Encaix T2↔T3 — caller-saved/callee-saved**: verificar que T2.qmd introdueix els conceptes de registres temporals/segurs de manera consistent amb la terminologia i les referències creuades establertes a T3 en la revisió interna (títol `## RV32I ABI —`, connexió «temporals = *caller-saved*», «segurs = *callee-saved*», refs `@nte-caller-saved-vs-callee-saved`). Fer en un xat nou amb T2.qmd i T3.qmd.
- Retocs manuals pendents (Roger) a les figures:
  - `figs_auto/T3_ba_exemple__original_light.svg`
  - `figs_auto/T3_deps_multi__original_light.svg`
  - `figs_auto/T3_deps_exemple__original_light.svg`

### T5

- ~~**F2** — Taula de registres FP: `11_riscv/RV32I_registres_coma_flotant.qmd` existeix amb contingut **divergent** del de T5 (alineació, noms, cursives). Decidir versió canònica abans de connectar; ara la taula es manté inline.~~ → ✓ Unificat el format amb `RV32I_registres_proposit_general.qmd` (negretes, cursives, rangs amb guió). T5 ara usa `{{< include >}}`. `05_riscv.qmd` també.
- ~~**Taules de camps de `fcsr`** (`frm`, `fflags`): decidir si van a includes de `11_riscv/` o es mantenen inline.~~ → ✓ Mantingudes inline a T5 i a `05_riscv.qmd` (la figura SVG fa inviable l'externalització per include).
- **F1 — figures** addicionals: (1) disposició S\|E\|F (32 bits), (2) recta numèrica rang/precisió amb denormals, (3) esquema d'arrodoniment GRS.
- **Harmonització notacional RV32I ↔ RV32F**: taules RV32F usen `\leftarrow` i `off`; RV32I usen `=` i `offset`. Unificar.
- **P7** — Alinear l'ordre de la taula de codificacions especials amb el de les subseccions.
- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present.
- **`#cau-underflow`**: opcionalment reanomenar a `#cau-subdesbordament` (cosmètic; no referenciat).
- Explicar perquè quantitat de denormals 2·(2^(23)-1) v.s. qualsevol rang normalitzat 2·2^(23) Nota: `2·` és per les dues opcions del bit de signe. L'explicació està a draw.io
- Assegurar que es diu que en denormals bit ocult és o

### T6

- SVGs `T6_not_cmos`, `T6_not_1_0`, `T6_not_0_1`: alçades diferents; textos solapats al PDF. Provar les versions `___tracable____original_light.svg`.

### T7 — Figures pendents de creació

~~`fig-escriptura-estat-inicial`, `fig-escriptura-immediata-amb-assignacio`, `fig-escriptura-immediata-sense-assignacio`, `fig-escriptura-retardada`, `fig-lru-exemple`, `fig-assoc-conjunts-taula`, `fig-conflicte-exemple`, `fig-capacitat-exemple-bucle-primera-passada`, `fig-capacitat-exemple-bucle-segona-passada`, `fig-gap-processador-memoria`~~ → ✓ Generades i integrades a `T7.qmd`.

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
- ~~`fig-tres-c-barres`~~ → ✓ Descartada (gràfic de dades sense valors numèrics disponibles).

Colors nous afegits a `21_specs/svg.md` en aquest xat:
- Miss zona bloc: `#f8d0d3` / `#dc3545` (light/stroke) · `#3d1a1e` / `#f07080` (dark)
- Hit zona bloc: `#c8ebd8` / `#198754` (light/stroke) · `#1a3328` / `#70c898` (dark)

### T8 — Figures pendents de creació

8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol `@fig-mv-flux-traduccio` 🔴). Rutes: `/figs_auto/T8_*__original_light.svg`.

### T9

- **E3 — Slugs sense prefix**: `sec-introduccio`, `sec-flux-hardware`, `sec-rse`, `sec-ecall`, `sec-interrupcions`, `sec-tlb`… Risc de col·lisió global. Vegeu pas 1 de la seqüència a `CLAUDE.md`.
- **F/G — Figures SVG**: diferides a una fase posterior.

---

## Tasques globals

### SVG

- **Migració de canvas a amplades estàndard**: figures de BA i mapa de memòria (`W=316 px`) → classe `estreta` (`W=340 px`). Decisió pendent: mantenir `w_rect=230` (marge dret 10→34) o ampliar `w_rect` a 254 (marges simètrics). Un cop decidit, aplicar a les 7 figures afectades i actualitzar `21_specs/svg.md §2`. Figures: `T3_mapa_memoria`, `T3_ba_general`, `T3_ba_func`, `T3_ba_multi`, `T3_ba_exemple`, `T3_func_uninivell_pila`, `T3_pila_crides_aniuades`.
- **Migrar diagrames Mermaid existents a SVG**.
- **`T3_deps_*` dark**: afegir `#cc0000` a `REPLACEMENTS` de `21_specs/svg.md` o crear dark manualment.
- ~~**Formats d'instrucció B, U, J, R4**: figures individuals i compendi `compendi_registres` generats i integrats a `22_scripts/gen_regs.py` + `21_specs/registres.toml`.~~ → ✓ Completat.

### Contingut global

- ~~**Exercicis Ca1/Ca2/excés a PE_T2**: la secció «Representació de naturals i enters» de PE_T2 s'ha traslladat a PE_T1 (IDs `exr-p1-enters-*`); PE_T2 conté una nota de remissió. La solució `sol-p1-enters-taules` s'ha traslladat a PS_T1.~~ → ✓ Completat.
- ~~**Ordre de seccions PE_T2**: «Constants i immediats» és ara la 2a secció (entre «Operands en registre» i «Operands en memòria»), consistent amb l'ordre de T2.qmd.~~ → ✓ Completat.

- **Cometes** `"..."` → `«...»`: substitució global.
- **`****` sobrants**: eliminar.
- **Equacions a MathML**: passar totes les equacions; definir criteris d'inline.
- **PDF**: figures dins callouts no queden centrades → investigar via `preamble.tex`.
- **Gestió d'errades post-commit**: definir protocol (vegeu `07_contrib.qmd §Gestió d'errades`).

### Solucionaris pendents d'afegir

| Tema | Cobertura | Estat |
| :--- | :--- | :--- |
| T1 | Conversió a Ca1/Ca2/SM/Excés per a 4 valors de 8 bits (`exr-p1-enters-conversio8`) | ✓ Resolt a `PS_T1.qmd` |
| T1 | Ca2 en mínim format (8 o 16 bits) per a 9 valors (`exr-p1-enters-codificacio`) | ✓ Resolt a `PS_T1.qmd` |
| T1 | Ca2 16 bits → decimal per a 2 valors (`exr-p1-enters-ca2-16bits`) | ✓ Resolt a `PS_T1.qmd` |
| T1 | Natural vs. Ca2 per a 4 patrons de bits (`exr-p1-enters-implicit`) | ✓ Resolt a `PS_T1.qmd` |
| T1 | Mínim Ca2 en 13 bits (`exr-p1-enters-minim13`) | ✓ Resolt a `PS_T1.qmd` |
| T1 | Màxim Ca2 en 13 bits (`exr-p1-enters-maxim13`) | ✓ Resolt a `PS_T1.qmd` |
| T1 | Divisió en Ca2: quocient, residu i sobreeiximent (`exr-p1-aritm-divisio`) | ✓ Afegit i resolt a `PE_T1.qmd`/`PS_T1.qmd` |
| T2 | *Little-endian*, ordre de bytes (`exr-p3-memoria-endianness`) | Pendent (Opus High Thinking) |
| T2 | Cerca en vector, retorn −1 (`exr-p3-vectors-cerca`) | Pendent (Opus High Thinking) |
| T2 | Aritmètica de punters sobre `short` (`exr-p3-vectors-punter-aritm`) | Pendent (Opus High Thinking) |
| T2 | Còpia de string (`exr-p3-strings-copia`) | Pendent (Opus High Thinking) |
| T3 | `switch` amb salts encadenats i *jump table* (`exr-p4-bucles-switch`) | ✓ Resolt a `PS_T3.qmd` |
| T3 | `exr-p4-compilacio-auipc`: expansió de `la`, rang ±2 GiB | Pendent (Opus High Thinking) |
| T3 | `exr-p4-memoria-jalr`: tracing de `jalr` (resposta: 3 vegades) | Pendent (Opus High Thinking) |
| T3 | `exr-p4-logica-rotacio` apartat b): rotació de 16 posicions | Pendent (Opus High Thinking) |

### `index.qmd`

- Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir.
- Consolidar taula de referències tècniques (`#imp-llenguatges-de-referencia`): versió ISO de C, versió GCC, toolchain (entrada duplicada).
- Afegir URL de la còpia local de RARS.
