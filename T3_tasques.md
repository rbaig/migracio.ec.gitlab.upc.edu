# Context per al xat de revisió interna de `T3.qmd`

## Situació de partida

Estem migrant el curs EC (FIB-UPC) de MIPS a RISC-V (RV32I/IM/IF), i dels apunts PDF originals a un llibre Quarto en català (`github.com/rbaig/migracio.ec.gitlab.upc.edu`, branca `problemes-enunciats-separats`).

La revisió interna de `T2.qmd` (ISA, memòria, C i assemblador) ja és completa. Ara toca fer la revisió interna de `T3.qmd` (**Tema 3: Traducció de C a assemblador RISC-V**), que cobreix desplaçaments, lògica bit a bit, comparacions, salts, sentències de control (`if`/`switch`/`while`/`for`/`do-while`), estructura de memòria, subrutines i el flux de compilació-assemblatge-enllaçat-càrrega.

Els fitxers de referència del projecte per a convencions són `CLAUDE.md` i `contrib.qmd`. Les etiquetes de callout segueixen el prefix `nte-`, `imp-`, `cau-`, `tip-`, `wrn-`; les seccions `sec-`; les figures `fig-`; les taules `tbl-`.

---

## Decisions i criteris ja adoptats a T2 (que T3 ha de respectar)

Estos criteris estan consolidats i **no cal revisar-los de nou**:

- **Veu impersonal** en català: «s'utilitza», «cal fer», no «hem de fer».
- **Terminologia fixada**: `mida` (espai), `longitud` (bits), `memòria cau` (mai *cache*), `maquinari`, `programari`.
- **Convenció de bucles**: etiquetes `while:`/`fwhile:` per a la traducció naïve, `bucle:`/`fbucle:` quan s'apliquen optimitzacions.
- **Optimitzacions de bucle**: el prerequisit d'extracció d'invariants s'introdueix a T2 (`@sec-extraccio-invariants`). Les optimitzacions #1 (accés seqüencial), #2 (avaluació de la condició al final) i #3 (eliminació de la variable d'inducció) es defineixen a T4. T3 **pot anticipar i aplicar** les optimitzacions sense definir-les, amb remissions a T4.
- **Fitxers de codi**: format `.c` (minúscules), no `.C`. `filename="C"` per a C, `filename="RV32I"` per a assemblador.
- **Punt d'entrada i sortida** dels programes complets: `_start`, sortida via `li a7, 93` + `ecall` (syscall exit2 de RARS).
- **`.global` vs `.globl`**: `.globl` és la forma estàndard; `.global` és sinònim acceptat per GCC. A T3 `nte-globl` ho explica correctament. Als exemples de codi s'ha d'usar `.globl`.
- **Callouts**: categories i criteris d'ús a `contrib.qmd`. **No s'ha de deixar cap etiqueta placeholder** `{#xxx-TODO}` en el fitxer final.

---

## Punts oberts que requereixen decisió o acció

### 1. Figures — **COMPLETAT** (xat de revisió 2/2)

Totes les figures pendents han estat generades com a SVG light seguint les specs de `scripts/svg_specs.md`. Les variants dark es generen automàticament via `scripts/svg_generate_dark.py` (pre-render de Quarto).

| Etiqueta | Estat | Notes |
| :--- | :--- | :--- |
| `#fig-mapa-memoria` | ✅ Ja existia | `T3_mapa_memoria_light/dark.svg` |
| `#fig-ba-general` | ✅ Ja existia | `T3_ba_general_light/dark.svg` |
| `#fig-ba-func` | ✅ Ja existia | `T3_ba_func_light/dark.svg` |
| `#fig-func-uninivell-pila` | ✅ Generat | 3 estats: avant/durant/après crida a `funcB` |
| `#fig-pila-crides-aniuades` | ✅ Generat | 5 estats: crides aniuades `funcA`/`funcB` |
| `#fig-ba-multi` | ✅ Generat | `s0`, `s1`, `ra`; escala ×1 |
| `#fig-ba-exemple` | ✅ Generat | `q`, `v`, `w`, alineació, `s0`–`s2`, `ra`; escala ×½. Retocs manuals pendents (Roger) |
| `#fig-deps-multi` | ✅ Generat | Retocs manuals pendents (Roger) |
| `#fig-deps-exemple` | ✅ Generat | Retocs manuals pendents (Roger) |
| `#fig-compilacio-separada` | ✅ Migrat de Mermaid a SVG | `T3_compilacio_separada_light/dark.svg` |
| `#fig-flux-gcc-complet` | ✅ Migrat de Mermaid a SVG | `T3_flux_gcc_complet_light/dark.svg` |

**Infraestructura SVG generada:**
- `scripts/svg_generate_dark.py` — script pre-render que genera les dark automàticament
- `scripts/svg_specs.md` — font de veritat de paleta i convencions SVG
- `scripts/dark_exclusions.txt` — cal afegir-hi `T3_deps_multi_dark.svg` i `T3_deps_exemple_dark.svg` fins que es defineixin les seves variants dark manualment
- `_quarto.yml` — afegit `pre-render: scripts/svg_generate_dark.py`
- `T3.qmd` — blocs Mermaid substituïts pels blocs light/dark estàndard

### 2. Callouts sense etiqueta definitiva — **COMPLETAT** (xat de revisió 1/2)

- **`{#cau-TODO}` (L1079)** → renombrat a `{#cau-caller-callee}` ✅
- **`{#nte-TODO}` (L1404)** → renombrat a `{#nte-rars-fons-pila}` ✅

### 3. Decisions de contingut obertes (calen respostes dels professors)

**3a. `gp` i altres segments al mapa de memòria** (L983):
> «TODO decidir si s'hi inclou `gp` altres segments, etc.»

El `gp` (*global pointer*) és un registre que RARS usa per optimitzar l'accés a variables globals petites. Cal decidir si s'explica a T3 o s'esmenta de passada.

**3b. Pseudoinstrucció `lla`** (L1016):
> «TODO decidir si hi incloem `lla`»

`lla` (*load local address*) és la versió relativa al PC de `la`. A RARS totes dues funcionen igual perquè no hi ha ASLR; la distinció és rellevant quan s'usa GCC real. Cal decidir si es menciona.

**3c. Terminologia *leaf* / *non-leaf*** (L1049):
> «TODO Confirmar eliminació de "(*leaf*)" i "(*non-leaf*)" pq no es fa servir enlloc o restitució»

Els termes *leaf function* i *non-leaf function* apareixien als apunts originals MIPS com a sinònims d'uninivell / multinivell. S'han eliminat provisionalment. Cal confirmar si s'han de restituir com a aprofundiment (`wrn-`) o eliminar definitivament.

**3d. Restricció d'EC a 1 resultat** (L1106):
> «TODO Adrià: no veig perquè hem de restringir a 1 retorn. De fet, penso que s'ha d'explicitar que poder retornar un segon valor permet tornar el codi d'error»

`imp-ec-abi-restriccions` diu: «A EC, la quantitat màxima de paràmetres és 8 i de resultats 1.» L'ABI real permet fins a 2 resultats (`a0`/`a1`). Cal decidir si: (a) es manté la restricció d'EC a 1 resultat, (b) s'amplia a 2, o (c) s'explica l'ABI real i s'indica que a EC s'usa sempre 1.

**3e. Verificació de l'ABI sobre el bloc d'activació** (L1304):
> «TODO Verificar que ho diu l'ABI»

La frase en qüestió és: «L'ABI imposa que les subrutines reservin tot l'espai que necessitaran a l'inici de la seva execució i que l'alliberin just abans de retornar.» Cal verificar contra l'especificació RISC-V Calling Convention / psABI.

**3f. Alineació de la pila a EC** (L1322):
> «TODO Consens? Roger: a favor de 16 => eliminar `{#imp-ec-alineacio-pila}`»

`nte-abi-alineacio-pila` diu que l'ABI exigeix múltiples de 16 bytes en la crida (`sp` múltiple de 16 en el moment de qualsevol `call`/`jal`). `imp-ec-alineacio-pila` diu: «A EC, per simplicitat, s'admet múltiples de 4 bytes.» Roger és a favor d'eliminar la relaxació i exigir 16 com a l'ABI real. Cal consens dels professors.

### 4. Numeració duplicada de les Optimitzacions — **COMPLETAT** (xat de revisió 1/2)

L'Optimització #3 estava etiquetada erròniament com a #2 → corregit ✅

### 5. Callout `{#tip-traduccio-godbolt}` — **PENDENT** de decisió

> Afegir un `wrn-` d'aprofundiment amb la descripció de Compiler Explorer / Godbolt, o descartar. Decisió pendent dels professors.

---

## Correccions ja aplicades en sessió anterior (no cal re-revisar)

Aquestes incidències es van resoldre durant la revisió de T2 i van afectar T3:

- **Col·lisió d'etiqueta real** resolta: `{#cau-instruccions-no-lwu}` (L106) que parlava de `sla`/`slai` → renombrada a `{#cau-instruccions-no-sla}`.
- **Tres duplicats interns** reanomenats:
  - `{#cau-salts-condicionals-relatius-pc}` (2a ocurrència, parlava d'incondicionals) → `{#cau-salts-incondicionals-indirectes}`
  - `{#nte-pseudoinstruccions-comparacio-zero}` (2a ocurrència) → `{#nte-pseudoinstruccions-salt-condicional-zero}`
  - `{#tip-exemple-suma2}` (L1077 i L1198) → `{#tip-crida-dos-punts}` i `{#tip-pas-referencia-punters}` respectivament
- **Fusió DRY**: la taula `beqz`/`bnez`/… duplicada a la secció de comparació es va substituir per referència creuada a `@nte-pseudoinstruccions-salt-condicional-zero`.

---

## Estat global del fitxer

- **Divs de callout**: equilibrats (verificat amb parser robust).
- **Refs creuades**: totes les refs de T3 cap a T2/T4/T8 resolen correctament.
- **Refs de T2 cap a T3**: `@sec-subrutines`, `@sec-compilacio`, `@sec-multinivell-pila`, `@sec-instruccions-logiques-bit-a-bit` → totes vàlides.
- **Col·lisions d'etiquetes amb T2/T4/T8**: cap (excepte `{#imp-ec-alineacio-pila}` dins d'un comentari a T3, fals positiu).
- **Render**: 9 imatges trencades (`figures/TODO.png`). La resta del fitxer renderitza.
