# T8 — Revisió interna: llista d'accions (estat actualitzat)

Llegenda: ✅ **FET** · 🟡 **DECISIÓ** (cal que triïs) · ⏳ **POSTERIOR** · 🔵 **PENDENT APLICAR**

---

## Decisions de notació / coherència entre capítols — TANCADES

### ✅ CC1 — Bit de presència de la PTE: `V` (ISA/H&H) adoptat

**Decisió presa:** la PTE usa `V` (*Valid*), coherent amb la ISA Sv32 i H&H.
**Justificació documentada a:** `contrib.qmd` → «Decisions per tema → T8».
**Canvis aplicats a T8:**
- Cos del text: «bit P» → «bit V» a PTE (definició, fallada de pàgina, TLB).
- Callout `@cau-mv-pte`: fila P → V, «Quan P=0» → «Quan V=0».
- Callout `@wrn-mv-notacio-v` (abans `@cau-mv-notacio-v`): convertit a `{.callout-warning collapse="true"}` amb títol — avisa de la divergència amb P&H com a aprofundiment, no com a Essencial.
- Secció `@sec-mv-tlb-bitv`: reescrita per explicar el doble paper del V del TLB per *context d'ús*.
- Comentari `fig-mv-taula-pagines`: actualitzat (P→V).
- Exemple del TLB: capçalera TP «P» → «V»; «P=0/P=1» → «V=0/V=1».

**Pendent (quan es tingui T9):** afegir referència enrere a `@wrn-mv-notacio-v` a `@sec-tlb-bit-v` de T9.

### ✅ CC2 — Model de fallada de TLB: Opció C adoptada

**Decisió presa:** T8 descriu el mecanisme de manera abstracta i correcta; un `{.callout-warning}` nou (`@wrn-mv-tlb-hw-walker`) explica la distinció hardware (RISC-V) vs. programari (MIPS) com a aprofundiment.
**Canvis aplicats a T8:**
- Callout `@wrn-mv-tlb-hw-walker` afegit just després de `@cau-mv-tlb-fallada`: explica que a RISC-V el reompliment del TLB el fa el *hardware walker* de manera transparent; el model per programari era MIPS; la fallada de pàgina (V=0) és l'excepció que sí arriba al SO (remissió a T9).

**Pendent (quan es tingui T9):** reescriure la introducció de `@sec-tlb` i `@sec-tlb-mecanisme`; reenllençar el codi de la RSE com a il·lustració de fallada de *pàgina*; invertir `@wrn-tlb-page-table-walker`.

---

## Tasca B — Revisió tècnica

- ✅ **B1** — Ordre LRU corregit a l'exemple (el més recent és VPN=1, no VPN=2).
- 🟡 **B2** — La taula de pàgines de l'exemple no té columna `E` (el TLB sí). *Opcions:* (a) afegir columna `E`; (b) frase fixant E=1. *Recomanació: (a).*
- 🟡 **B3/B4** — L'exemple (Accés 2) no segueix el model de dos passos (còpia al TLB amb V=0 → reintent → fallada de pàgina), i barreja reemplaçament de marc i d'entrada del TLB. Pendent de decisió CC2 (model hardware/software de fallada de TLB).
- ✅ **B5** — «escriptura diferida» → «retardada» + `@sec-escriptura-combinacions`.

---

## Tasca C — Revisió pedagògica

- ✅ **C2** — Referència DRY `@sec-jerarquia` (T7) afegida.
- 🟡 **C1** — `@sec-mv-multinivell` sense cos de text (només dos callout-warning). Decidir si s'hi afegeix una frase introductòria.

---

## Tasca D — Revisió lingüística

- 🔵 **D1** — `cache` → `memòria cau`/`cau` (36 ocurrències a la secció d'integració + títols). Pendent de confirmació.
- 🟡 **D2** — Taula de jerarquia: cau `0,5–40 ns` (T7: `0,5–5`); SSD `0,02–0,1 ms` (T7: `0,05–0,1`). Alinear a T7?
- 🟡 **D3** — «Emmagatzematge secundari» (T8) → «Memòria secundària» (T7).
- 🟡 **D5** (global) — «de sols lectura»: poc normatiu. Decisió global del projecte.

---

## Tasca E — Revisió format Quarto

- 🔵 **E1** (crític) — `@fig-mv-flux-traduccio` (línia ~246) referència trencada. La figura és un comentari HTML → Quarto renderitza `??`. Resoldre a la fase de figures (F5).
- 🟡 **E2** (menor) — Taules sense `tbl-colwidths` (TLB i exemple).

---

## Coherència entre capítols — decisions pendents

### 🟡 CC2 — Fallada de TLB: model hardware (T8) vs. software/RSE (T9)

T8 descriu el reompliment del TLB de manera abstracta/automàtica. T9 (i T9_tasques D2) diu que a RISC-V les fallades de TLB es gestionen **per programari** via RSE — però T9_tasques nota que això és en realitat el model MIPS, i que RISC-V estàndard usa un *page-table walker* per hardware. Cal decidir el model del curs. Afecta B3/B4.

### 🟡 CC3 — Bit D: escriptura immediata TLB↔PTE (T8) vs. via excepció (T9)

Lligat a CC2.

### 🟡 CC4 — Terminologia modes: «mode sistema/usuari» (T8) vs. «mode M/S/U» (T9)

T8 ja remet a `@sec-csr-privilegis` (T9). Suficient per ara?

---

## Sigles

- ✅ **VPN** i **PPN** afegides a `sigles.qmd`.

---

## Tasques F (figures) i G (integració) — POSTERIORS

8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol E1).

---

## Fitxers modificats en aquest xat

| Fitxer | Canvis |
|:---|:---|
| `T8.qmd` | CC1 complet (P→V PTE); B1, B5, C2, DRY T9 |
| `sigles.qmd` | VPN, PPN afegides |
| `contrib.qmd` | Decisió notació V(PTE)/V(TLB) documentada a §T8 |
| `T7.qmd` | Etiquetes {#sec-} duplicades eliminades (línies 41, 50) |
