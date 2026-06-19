# T9 — Revisió interna: llista d'accions (revisada amb T7/T8 correctes)

**Fitxer objectiu:** `01_T/T9.qmd` (Excepcions i interrupcions)
**Fonts creuades:** `T7.qmd`, `T8.qmd`, `T7_tasques.md`, `T8_tasques.md`, `contrib.qmd`, `svg_specs.md`
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ resolt · ⏳ pendent · ⚪ neteja

> **Nota:** aquesta versió substitueix la inicial, que es basava en una còpia antiga de T8.
> Amb el T8 correcte, el «conflicte P vs V» desapareix (T8 ja usa `V` a la PTE) i el model
> de fallada de TLB ja està decidit (Opció C al xat de T8).

---

## 0. Coherència inter-capítol (estat real amb T7/T8 correctes)

| # | Punt | T7 | T8 (correcte) | T9 (actual) | Acció a T9 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| CC1 | Bit presència PTE | — | ✅ `V` + `@wrn-mv-notacio-v` | `V` ✅ | Ja alineat. Afegir ref. enrere a `@wrn-mv-notacio-v`; DRY amb `@sec-mv-tlb-bitv` |
| CC2 | Fallada de TLB | — | ✅ Opció C (cos abstracte + `@wrn-mv-tlb-hw-walker`) | 🔴 «per programari» com a model RISC-V | **Reescriure** `@sec-tlb` (vegeu §1) |
| CC3 | Bit D | bit modificació (write-back) | maquinari, sense excepció (escr. immediata TLB↔PTE) | via excepció | 🔵 **D-CC3**: alinear o documentar divergència |
| CC4 | Modes | — | «mode sistema/usuari» → remet a `@sec-csr-privilegis` | M/S/U ✅ | Cap canvi |
| Co5 | Terme write-back | «escriptura retardada» | ✅ ja corregit a «retardada» | «retardada» ✅ | Cap canvi |
| Co6 | Nom bit D | «bit de modificació» | «modificada» | «modificada» (l. 918) | ⚪ unificar a «bit de modificació» |

---

## 1. CC2 — Reescriptura de la secció TLB (tasca principal) 🔴

Estat actual de T9 (incorrecte per a RISC-V estàndard):

- L. 797: «les fallades de TLB en RISC-V es gestionen per **programari**» → fals: a RISC-V
  el reompliment del TLB és transparent (*hardware page-table walker*); només la **fallada de
  pàgina** és una excepció gestionada pel SO.
- L. 805: «`mcause` no distingeix entre fallada de TLB i fallada de pàgina (codis 12/13/15)»
  → fals: 12/13/15 són **fallades de pàgina**; no hi ha codi estàndard de «TLB miss».
- `@sec-tlb-modes-rutina`: mostra un `tlb_miss_handler` per programari com si fos la norma.
- `@wrn-tlb-page-table-walker`: presenta el walker per maquinari com a excepcional.

Accions (alineades amb la decisió Opció C de T8, `@wrn-mv-tlb-hw-walker`):

1. Reescriure `@sec-tlb` / `@sec-tlb-recordatori` / `@sec-tlb-mecanisme`: la fallada de TLB
   es resol de manera **transparent** (walker); el que el SO gestiona com a excepció és la
   **fallada de pàgina** (codis 12/13/15).
2. Reconvertir `tlb_miss_handler` en un **`page_fault_handler`** (gestió de fallada de pàgina
   en mode S): és el que T8 anuncia («el Tema 9 il·lustra el mecanisme de gestió de fallades
   de pàgina amb codi RISC-V»).
3. **Invertir** `@wrn-tlb-page-table-walker`: el walker per maquinari és la norma RISC-V; el
   TLB gestionat per programari és el model **MIPS** (aprofundiment).
4. Ajustar la taula `@tbl-tipologia` (l. 34): la fila «Fallada de TLB» (excepció reexecutada)
   no correspon a RISC-V estàndard; deixar només «Fallada de pàgina», o etiquetar TLB com a
   transparent.
5. Afegir referència enrere a `@wrn-mv-tlb-hw-walker` i `@sec-mv-tlb` (T8).

---

## 2. Decisions obertes 🔵

### D-CC3 — Bit D (dirty): alinear a T8 o documentar divergència
- **T8 (fix):** la MMU posa D=1 a TLB i PTE per **escriptura immediata**, sense excepció.
- **T9 (actual):** D s'actualitza **via excepció** (`@sec-tlb-bit-d`, l. 916-925).
- **Recomanació:** alinear el cos de T9 al model maquinari de T8 i deixar la variant per
  excepció a `@wrn-tlb-bit-ad` (que ja existeix i cobreix exactament el cas sense Svadu).

### D-Zicsr/Zifencei — `sfence.vma` mal atribuïda 🔴 + decisió
- L. 859: «`sfence.vma` pertany a Zifencei» i títol «Zicsr ISA — `sfence.vma`» → **incorrecte**.
  `sfence.vma` és de l'arquitectura **Supervisor** (privilegiada). Zifencei = `fence.i`.
- **Decisió:** a `contrib.qmd` (taula d'extensions, l. 758-759) Zifencei surt per a T9. Si no
  s'usa `fence.i` enlloc, (i) corregir l'atribució i (ii) **treure Zifencei** de la taula
  d'extensions d'EC.

### D-RARS — Compatibilitat de la RSE
- `@sec-rse-exemple` usa `.section .text.trap` i `mret`; TODO «port a RARS?». Decidir si és
  **il·lustratiu** (pissarra) o **executable a RARS**, i etiquetar/ajustar.

---

## 3. Revisió tècnica (Tasca B)

| # | Element | Estat |
| :-- | :-- | :-- |
| B1 | `sfence.vma` / Zifencei | 🔴 (= D-Zicsr/Zifencei) |
| B2 | Codis `mcause` (128-147) | ✅ verificat correcte |
| B3 | Bits `mip`/`mie` (250-258) | ✅ correcte (opcional: reordenar 1,3,5,7,9,11,13) |
| B4 | Codis RARS i Linux/asm-generic | ✅ verificat correcte (PrintInt=1…Exit2=93) |
| B5 | `tlb_miss_handler` → `page_fault_handler` (= CC2) | 🔴/🟡 reescriure; indentació `lw t3` (l. 890) |
| B6 | `@sec-tlb-bit-v` dins comentari de codi (l. 901) | 🟡 no es renderitza; treure del bloc |

---

## 4. Revisió pedagògica (Tasca C)

- C1 — DRY: tres condicions d'interrupció repetides a `@cau-mip-mie-combinat` (265-269) i
  `@cau-permisos-interrupcions` (764-772). Consolidar amb referència creuada.
- C2 — DRY: `mtval` explicat a `@sec-csr-mtval` (224-230) i de nou a
  `@sec-flux-hardware-diferencies` (318). Referenciar.
- C3 — Estructura de la llista de la tipologia (44-52): paral·lelisme trencat.
- C4 — Mode M/S: `@sec-tlb-modes-rutina` mostra handler en mode S al cos; després de CC2 cal
  decidir-ne l'encaix (cos vs aprofundiment).

---

## 5. Revisió lingüística (Tasca D)

- D-L1 — «per al caller» (538) → «per al procés que l'ha cridat».
- D-L2 — Llista tipologia (47-51): comes davant de parèntesis, «Són irrecuperables» en
  majúscula, puntuació.
- D-L3 — «bit de modificada» (918) → «bit de modificació» (= Co6).
- D-L4 — Passada completa de majúscules/minúscules després de dos punts i punts finals.

---

## 6. Format Quarto (Tasca E)

- E1 — 🔴 **Figures sense `content-visible when-format`** (mcause 121, mepc 163, mstatus 179,
  mtvec 199, mip/mie 241, satp 836, `@fig-cicle-interrupcio` 746) → es **dupliquen al PDF**.
  Aplicar el patró canònic de T7 (Convenció A).
- E2 — `@fig-cicle-interrupcio` (747, 750) porta `style="text-align: center;"` → treure'l.
- E3 — Slugs genèrics sense prefix de tema (`sec-introduccio`, `sec-flux-hardware`, `sec-rse`,
  `sec-ecall`, `sec-interrupcions`, `sec-tlb`…) → risc de col·lisió global. Prefixar
  (verificar contra T1-T6). Tasca sistemàtica ja prevista a `CLAUDE.md`.
- E4 — Resoldre/documentar TODOs (389-404, 410, 847, 850).

---

## 7. Figures (F/G) — fase posterior

Diferides. Registres → diagrames de camps (referències a `docs.riscv.org` als comentaris).
Només es toca el patró d'integració (E1/E2) en aquesta passada.

---

## 8. Fitxers que es preveu modificar

| Fitxer | Motiu |
| :-- | :-- |
| `T9.qmd` | totes les tasques anteriors |
| `contrib.qmd` | decisió Zifencei (taula d'extensions) i, si escau, `@wrn-mv-notacio-v` |
| `T8.qmd` | només si D-CC3 es resol documentant divergència (afegir nota) |
| `sigles.qmd` | si apareixen sigles noves de T9 no recollides |
