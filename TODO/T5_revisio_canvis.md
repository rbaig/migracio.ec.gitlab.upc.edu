# A5.qmd — Canvis aplicats (revisió interna)

## Bloc 1 — correccions de contingut i format

| # | Tipus | Descripció | Estat |
| :--- | :--- | :--- | :---: |
| B1 | 🔴 Tècnic | Multiplicació IEEE-754: resultat `0xBEB60004` → **`0xBEB60002`**. Refets els passos 2 (producte sense `10` espuri), 4 (mantissa normalitzada), 5 (guarda `11`, arrodoniment `…001→010`) i 6 (codificació). | ✔ |
| B2 | 🟡 Tècnic | Codificació: binari de l'error reposicionat (1 a la posició 25 → `×2¹⁰ = 1,111₂×2⁻¹⁵`). | ✔ |
| B3 | 🟡 Tècnic | Suma: binari de l'error reposicionat (1 a la posició 25 → `×2¹ = 2⁻²⁴`). | ✔ |
| C1 | 🟠 Pedag. | Codificació: eliminada la línia duplicada amb notació malmesa `…/2 × 10⁵`. | ✔ |
| C2 | 🟠 Pedag. | Descodificació: eliminat el terme espuri `+ 2²` (`2¹² + 2⁵ + 2³ = 4136`). | ✔ |
| D1 | 🟡 Lingü. | «cal comprovar» → «Cal comprovar» (majúscula després de punt). | ✔ |
| E1 | 🟡 Format | `{.C filename="C"}` → `{.c filename="C"}` (2 blocs). | ✔ |

## D2 — terminologia *underflow* → *subdesbordament*

- Glossa única a la primera aparició en prosa (callout `#cau-underflow`):
  «genera una excepció de **subdesbordament** (*underflow*)».
- Títol de secció, títol de callout, taula `fcsr` i passos d'operacions: «subdesbordament» en pla.
- Es manté l'identificador intern `#cau-underflow` (no es referencia enlloc; canviar-lo és opcional).
- ⚠️ A revisar: «gradual underflow» (§ denormals) s'ha traduït com **subdesbordament gradual** sense
  glossa, per coherència amb la regla d'una sola glossa. Si vols mantenir el terme anglès com a
  referència, es pot afegir «(*gradual underflow*)».

## F3 — extracció de taules RV32F a includes (`21_riscv/`)

6 fitxers nous (només files de dades; capçalera, separador i `tbl-colwidths` queden al tema):

| Include | Callout d'origen |
| :--- | :--- |
| `RV32F_instruccions_carrega_emmagatzemament.qmd` | `#nte-instruccions-flw-fsw` |
| `RV32F_instruccions_aritmetiques.qmd` | `#nte-instruccions-aritmetiques-f` |
| `RV32F_instruccions_moviment.qmd` | `#nte-instruccions-moviment-f` |
| `RV32F_instruccions_comparacio.qmd` | `#nte-instruccions-comparacio-f` |
| `RV32F_instruccions_conversio.qmd` | `#nte-instruccions-conversio-f` (taula de conversions) |
| `RV32F_instruccions_moviment_bits.qmd` | `#nte-instruccions-conversio-f` (taula de moviments de bits) |

Camí d'include: `../21_riscv/…` (coherent amb T2/T3). El compendi `11_riscv.qmd` (encara *stub*)
podrà reutilitzar aquests includes quan es desenvolupi.

## Pendent (no aplicat)

- **F2** — Taula de registres FP: l'include `21_riscv/RV32I_registres_coma_flotant.qmd` JA existeix
  però amb contingut **divergent** del de T5 (alineació, negretes, verbositat). Cal decidir versió
  canònica abans de connectar T5. La taula es manté **inline** a T5 de moment.
- **Taules de camps de `fcsr`** (frm, fflags): són taules de camps de registre (no d'instruccions).
  Decisió oberta: també a includes per al compendi, o es mantenen inline?
- **Inconsistència notacional**: les taules RV32F usen `\leftarrow` i `off`; les RV32I existents usen
  `=` i `offset`. Harmonització pendent (futur).

## Revisió pedagògica (estructura) — segona passada

| # | Canvi | Detall |
| :--- | :--- | :--- |
| P1 | **G/R/S promogut a contingut principal** | Nova subsecció `#### Bits de guarda {#sec-bits-de-guarda}` dins `### Arrodoniment` amb la definició de G/R/S i la taula de decisió RNE. Abans només vivien dins l'aprofundiment plegable `#wrn-bits-guarda` (no avaluable), tot i que els exemples de suma i multiplicació en depenen. |
| P2 | **Notació unificada** | L'exemple `#tip-arrodoniment-rne` passa de «1r bit descartat / resta» a columna `G R S`, coherent amb el cos i amb els exemples d'operacions. |
| P1 | **Aprofundiment aprimat** | `#wrn-bits-guarda` queda reduït a la justificació («per què 3 bits basten») + l'exemple $p=6$; se'n treu la definició i la taula duplicades. |
| P3 | **Redundància de la fita d'error** | Al cos de `### Error de representació` es deixa el resultat $\eta_{\max} < 2^{-23} = 1\text{ ULP}$ amb remissió a `@wrn-error-relatiu-formal`; la derivació completa queda només a l'aprofundiment. |
| P5 | **Cinquè mode d'arrodoniment** | `### Arrodoniment` reconeix que IEEE-754 (2008) en defineix cinc i esmenta RMM amb remissió a `@nte-fcsr` (abans deia «quatre», en desacord amb la taula de `fcsr`). |
| P6 | **«dígits» en context decimal** | Als exemples en base 10 (suma i multiplicació), «bits descartats» → «dígits descartats». |
| P4 | **Exemple de divisió afegit** | Nou `#tip-divisio-ieee754`: $8{,}0 / 3{,}0$ (`0x41000000 / 0x40400000`) → `0x402AAAAB` $\approx 2{,}6667$. Il·lustra el cas propi de la divisió: quocient de mantisses periòdic ($1{,}0_2/1{,}1_2 = 0{,}101010\ldots$) que obliga a arrodonir (G=1, R=0, S=1). Verificat amb `struct`. |

### Pendent (suggeriments pedagògics no aplicats)

- **P7** — Ordre de la taula de codificacions especials (Zero/Denormal/Normalitzat/Infinit/NaN) vs.
  ordre de les subseccions (Zero/Infinit/NaN/Denormals): alinear o afegir una frase pont. Molt menor.
- **P8** — Dependència cap endavant: `fcsr` remet a `@nte-zicsr` (definit a T9, posterior). Funciona,
  però convé tenir-ho present en la seqüència del curs.
