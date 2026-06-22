# TODO

## Decisions de criteri

Decisions obertes que, un cop preses, han d'aterrar a `07_contrib.qmd`.

### Convencions d'assemblador

- **`startup.s`**: mantenir als materials o eliminar? Proposta: eliminar; forçar `li a7, 93` + `ecall` (syscall `exit` Linux).
  - Afecta T2: `#nte-programa-esquelet` (duplicat al bloc comentat de `startup.s`) i `__start`/`a7,10` (blocs comentats, ln 742-772).
- **Retorn de 2 paràmetres**: mantenir restricció EC a 1 resultat (`a0`) o ampliar a 2 (`a0`/`a1`)? Posició d'Adrià: ampliar a 2 i explicitar que el segon pot ser un codi d'error. Afecta T3 (L1106).
- **Alineació de la pila**: exigir múltiples de 16 (ABI real) o mantenir relaxació a múltiples de 4 (EC actual)? Posició de Roger: a favor d'eliminar la relaxació. Afecta T3 (L1322) i `{#imp-ec-alineacio-pila}`.
- **`.globl` vs `.global`**: quin usar als exemples?
- **`.section`**: usar o no? si sí, amb quin criteri?
- **`ret` vs `jalr x0, 0(ra)`**: criteri al retorn de funcions.
- **Codi testejat**: definir si el codi ha d'estar sempre testejat abans de commit.

### Convencions de contingut

- **`gp` al mapa de memòria** (T3, L983): incloure el *global pointer* al mapa o esmentar-lo de passada.
- **Pseudoinstrucció `lla`** (T3, L1016): incloure `lla` (*load local address*) o no.
- **Terminologia *leaf*/*non-leaf*** (T3, L1049): eliminar definitivament o restituir com a `wrn-` d'aprofundiment.
- **Verificació ABI sobre el BA** (T3, L1304): confirmar contra RISC-V Calling Convention / psABI que «les subrutines reserven tot l'espai a l'inici i l'alliberen just abans de retornar».
- **«De sols lectura»** (T8, global): decisió global sobre l'expressió.
- **TLB validity bit**: unificació del criteri d'adopció `V` vs `E` a tot el projecte.
- ~~**`underflow`** (T5): unificar amb terme català **subdesbordament**~~ → **RESOLT**: s'adopta **subdesbordament**, amb glossa `**subdesbordament** (*underflow*)` a la primera aparició (i `(*gradual underflow*)` per al subdesbordament gradual). *Cal recollir-ho a `07_contrib.qmd` (substitucions de terminologia).*

### Convencions de format Quarto

- **Adreces de memòria**: `0x00000000` o `0x0000 0000` (amb espai cada 4 nibbles)?
- **Directives**: quin títol de callout? `## Directives —` o `## RARS —`?
- **ISA/ABI**: on posar la informació de l'ABI de RV? `{.callout-note}` amb `## RV32I ABI —`? `{.callout-important}`?
- **Syntax highlighting**: confirmar que `.s` és correcte per a totes les instruccions, macros i directives de RARS.
- **Negretes dins de callouts vs. cos del text**: definir criteri.
- **Noms de registres CSR al cos del text**: amb o sense backtick?
- **Numeració d'equacions**: només les referenciades? totes? les importants?
- **LaTeX math vs. backticks**: contextos on usar cada un (cos del text, títols de secció, títols de callout, cel·les de taula, captions, blocs de codi).
- **Coherència de títols en `.callout-caution`**: `07_contrib.qmd` indica que `.callout-caution` (Essencial) no porta títol; a T5 alguns en porten. Acceptar com a excepció o unificar.
- **Criteris de codi C**: completar.

---

## Tasques tècniques per tema

### T2

- Verificar a RARS: `.byte 0101` (octal, ln 2082), `.byte`/`.half`/... sense operands (ln 1112), `li` amb `lo₁₂==0` (ln 524).
- `#tbl-tipus-alineacio` (i possibles altres `#tbl-`) sense caption → afegir.
- Nota `07_contrib.qmd` §T2/T4: «es defineixen totes a T4» és imprecisa (`sec-extraccio-invariants` es defineix a T2, l.1916) → actualitzar contrib.
- Redundància «modularitat» (ln 57/69/86): revisió editorial.

### T3

- Corregir etiqueta `#cau-instruccions-no-sla` (ln 106): actualment mal etiquetada (parla de `sla`/`slai`, no de `lwu`). Reanomenar a la revisió de T3.
- Retocs manuals pendents (Roger) a les figures:
  - `figs_auto/T3_ba_exemple__original_light.svg`
  - `figs_auto/T3_deps_multi__original_light.svg`
  - `figs_auto/T3_deps_exemple__original_light.svg`

### T5 *(revisió interna feta — sessió actual)*

**Fet** (lliurat: `T5.qmd` corregit + 6 includes a `11_riscv/`):

- **B1** — Multiplicació IEEE-754: corregit `0xBEB60004` → **`0xBEB60002`** (refets passos 2, 4, 5, 6).
- **B2** / **B3** — Binaris d'error reposicionats (codificació i suma; 1 a la posició 25).
- **C1** — Línia duplicada amb notació malmesa eliminada. **C2** — Terme espuri `+ 2²` eliminat.
- **D1** — Majúscula «Cal comprovar». **E1** — `{.C}` → `{.c}` (2 blocs).
- **D2** — Terminologia *underflow* → **subdesbordament** (glossa única a la primera aparició;
  glossa pròpia per a *gradual underflow*).
- **F3** — Taules d'instruccions RV32F extretes a `11_riscv/` (6 includes: càrrega/emmagatzemament,
  aritmètiques, moviment, comparació, conversió, moviment de bits) i reconnectades amb `{{< include >}}`.

**Pendent:**

- **F2** — Taula de registres FP: l'include `11_riscv/RV32I_registres_coma_flotant.qmd` JA existeix
  amb contingut **divergent** del de T5 (alineació `:---` vs `:---:`, «**Temporals** coma flotant»
  vs «Temporals», cursives a *Caller*/*Callee*). **Decidir versió canònica** abans de connectar T5;
  ara mateix la taula es manté inline a T5.
- **Taules de camps de `fcsr`** (`frm`, `fflags`, camps): decidir si també van a includes de `11_riscv/`
  per al compendi, o es mantenen inline (són taules de camps de registre, no d'instruccions).
- **F1 — figures** addicionals (decisió oberta). Ja fet: `#fig-fcsr`. Candidates pendents:
  (1) disposició de camps S\|E\|F (32 bits), (2) recta numèrica rang/precisió amb denormals,
  (3) esquema d'arrodoniment GRS.
- **Harmonització notacional RV32I ↔ RV32F**: les taules RV32F usen `\leftarrow` i `off`; les RV32I
  existents usen `=` i `offset`. Unificar criteri (afecta includes de tots dos jocs).
- **Identificador `#cau-underflow`**: opcionalment renombrar a `#cau-subdesbordament` (ara no es
  referencia enlloc; és cosmètic).

**Pedagògic** (segona passada — fet: G/R/S al cos, notació unificada, aprofundiments aprimats,
5è mode d'arrodoniment, «dígits» en context decimal, **exemple de divisió** `#tip-divisio-ieee754`
afegit). Pendent:

- **P7** — Alinear l'ordre de la taula de codificacions especials amb el de les subseccions
  (o afegir frase pont). Molt menor.
- **P8** — `fcsr` té una dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present.

### T6

- SVGs `T6_not_cmos`, `T6_not_1_0`, `T6_not_0_1`: alçades diferents; textos solapats al PDF. Provar les versions `___tracable____original_light.svg` (desagrupant i tornant a agrupar s'hi poden fer modificacions petites).

### T7 — Figures pendents de creació

Usar com a referència d'estil: `T7_mc_organitzacio__original_light.svg` (taules), `T7_cd_descomposicio_bits__original_light.svg` (descomposició de bits), `T7_mc_encert__original_light.svg` (diagrames CPU/MC/MP).

| Figura | Descripció | Notes |
| :--- | :--- | :--- |
| `fig-mc-exemple-descomposicio-32bits` | Taula MC (V, Etiqueta, Bloc de dades) per a l'exemple `0x100100F8` dins `@tip-mc-numbloc` | Basar-se en `T7_mc_organitzacio` |
| `fig-cd-diagrama` | Diagrama blocs maquinari MC correspondència directa | Referència: LO Draw disponible |
| `fig-assoc-conjunts-diagrama` | Diagrama blocs MC associativa per conjunts (N comparadors en paral·lel, OR, mux N:1) | Anàleg a `fig-cd-diagrama` |
| `fig-ca-diagrama` | Diagrama blocs MC completament associativa | 🔴 Referència trencada al `.qmd` |
| `fig-texe-diagrama` | Diagrama temporal lw/addu/lw (etapes F/D/R/A/M/W, ideal vs. real) | Referència: pàg. 24 PDF original |
| `fig-lru-exemple` | Evolució estat MC (conjunt 1, 2 vies) als 4 accessos LRU (4, 38, 6, 52) | Possible mosca `fig-lru-roger` |
| `fig-lru-roger` | Màquina d'estats de l'algorisme LRU | SVG natiu; pot anar com a mosca dins `fig-lru-exemple` |
| `fig-assoc-conjunts-taula` | Taula 4 conjunts × 3 vies | |
| `fig-escriptura-estat-inicial` | Estat MC 5 lectures inicials | |
| `fig-escriptura-immediata-assignacio` | | |
| `fig-escriptura-immediata-sense-assignacio` | | |
| `fig-escriptura-retardada` | Inclou columna D (dirty bit) | |
| `fig-tres-c-barres` | Gràfic % fallades vs. associativitat | |
| `fig-conflicte-exemple` | Taula estat MC exemple conflicte | |
| `fig-capacitat-exemple` | Taula estat MC exemple capacitat | |
| `fig-multinivell-diagrama` | CPU→L1→L2→MP | |
| `fig-multinivell-multicore` | Xip 4 nuclis L1/L2/L3 | |

### T8 — Figures pendents de creació

8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol la referència trencada `@fig-mv-flux-traduccio`). Rutes des de `01_T/`: `/figs_auto/T8_*__original_light.svg`.

### T9

- **E3 — Slugs sense prefix de tema**: `sec-introduccio`, `sec-flux-hardware`, `sec-rse`, `sec-ecall`, `sec-interrupcions`, `sec-tlb`… Risc de col·lisió global. Resoldre a la tasca sistemàtica de prefixat (pas 2 de la seqüència de revisió de `CLAUDE.md`).
- **F/G — Figures SVG**: diferides a una fase posterior.

---

## Infraestructura i global

### Scripts i tooling

- Substituir el JavaScript al browser de canvi de numeració de problemes per script de Python o Lua durant la generació?
- **Migrar diagrames Mermaid existents a SVG** (pipeline automàtic ja cobreix els SVG).

### Contingut global

- **Cometes** `"..."` → `«...»`: substitució global a tot el projecte.
- **`****` sobrants**: eliminar.
- **Equacions a MathML**: passar totes les equacions; definir els criteris d'inline.
- **PDF**: figures dins de callouts no queden centrades (investigar via `preamble.tex`, p. ex. `\centering` a l'entorn de callout).

### Solucionaris pendents d'afegir

| Tema | Exercici | Cobertura |
| :--- | :--- | :--- |
| T2 | — | *Little-endian*, ordre de bytes |
| T2 | — | Cerca en vector, retorn −1 |
| T2 | — | Aritmètica de punters sobre `short` |
| T2 | — | Còpia de string |
| T3 | — | `switch` amb salts encadenats i *jump table* |

### `index.qmd`

- Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir.
- Decidir si `startup.s` es manté (vegeu §Decisions de criteri).
- Consolidar noms, versions i estàndards de la taula de referències tècniques (`#imp-llenguatges-de-referencia`): versió ISO de C, versió GCC, toolchain (entrada duplicada).
- Afegir URL de la còpia local de RARS.
- Gestió d'errades post-commit: definir protocol.

### Laboratori

- Decidir si l'estudi previ es lliura com a fitxers separats o integrat al `.qmd`.
- Plantilles Markdown: posar-ne a tots els `Ly.qmd` excepte `L2.qmd`, o eliminar de `L2.qmd`.
- Decidir com mostrar el contingut de `laboratori/` per a descàrrega (codi encastat C&P vs. fitxers descarregables).

### Referències creuades trencades

| Referència | Tema | Estat |
| :--- | :--- | :--- |
| `@fig-mv-flux-traduccio` | T8 | Pendent de creació de la figura |
| `@fig-cd-diagrama` | T7 | Pendent de creació de la figura |
| `@fig-assoc-conjunts-diagrama` | T7 | Pendent de creació de la figura |
| `@fig-ca-diagrama` | T7 | Pendent de creació de la figura |
| `@fig-texe-diagrama` | T7 | Pendent de creació de la figura |
