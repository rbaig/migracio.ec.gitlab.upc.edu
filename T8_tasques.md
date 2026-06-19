# T8 — Revisió interna: estat final

Llegenda: ✅ **FET** · ⏳ **PENDENT (xat de T9)**

---

## Decisions de coherència entre capítols

### ✅ CC1 — Bit de presència de la PTE: `V` (ISA/H&H)
`V` adoptat arreu a T8 (PTE, TLB, exemple, comentaris de figures).
Callout `@wrn-mv-notacio-v` (Aprofundiment) avisa de la divergència amb P&H.
Justificació a `contrib.qmd` § Decisions T8.
⏳ Al xat de T9: afegir referència enrere a `@wrn-mv-notacio-v` a `@sec-tlb-bit-v`.

### ✅ CC2 — Model de fallada de TLB: Opció C (abstracte + aprofundiment)
Cos del text abstracte i correcte; `@wrn-mv-tlb-hw-walker` (Aprofundiment) explica
hardware walker (RISC-V) vs. programari (MIPS) i remet a T9 per a la fallada de pàgina.
⏳ Al xat de T9: reescriure `@sec-tlb` i `@sec-tlb-mecanisme`; reenllençar la RSE com a
il·lustració de fallada de pàgina; invertir `@wrn-tlb-page-table-walker`.

### ⏳ CC3 — Bit D: model hardware (T8) vs. via excepció (T9)
Pendent del xat de T9. T8 no canvia; T9 ha d'alinear-se.

### ✅ CC4 — Modes privilegiats
T8 usa «mode sistema/usuari» (genèric, correcte per al nivell de T8).
Ja remet a `@sec-csr-privilegis` (T9) per als modes M/S/U de RISC-V.

---

## Tasques de revisió — totes tancades

### Tècnica (B)
- ✅ B1 — Ordre LRU corregit a l'exemple (el més recent és VPN=1).
- ✅ B2 — Columna `E` afegida a la taula de pàgines de l'exemple (E=1 per a totes
  les pàgines de dades, coherent amb el TLB de l'exemple que ja tenia E=1).
- ✅ B5 — «escriptura diferida» → «retardada» + `@sec-escriptura-combinacions`.
- B3/B4 — Lligats a CC2; cos del text ja és abstracte. ✅ resolt per CC2.

### Pedagògica (C)
- ✅ C1 — `@sec-mv-multinivell`: paràgraf introductori afegit + placeholder de figura
  `fig-mv-taula-multinivell`.
- ✅ C2 — Referència DRY `@sec-jerarquia` (T7) afegida.

### Lingüística (D)
- ✅ D1 — `cache` → `memòria cau`/`cau` a tota la secció d'integració (títols,
  cos, callouts, comentaris de figures). Slugs `#sec-mv-cache-*` conservats.
- ✅ D2 — Xifres alineades a T7: cau `0,5–5 ns`, SSD `0,05–0,1 ms`.
  Referència creuada `@tbl-tecnologies-memoria` afegida al caption (DRY).
- ✅ D3 — «Emmagatzematge secundari» → «Memòria secundària».
- ✅ B5 (D) — «escriptura diferida» → «retardada».
- D5 (global) — «de sols lectura»: decisió global del projecte, pendent.

### Format Quarto (E)
- ⏳ E1 — `@fig-mv-flux-traduccio`: referència trencada. Resoldre a la fase de figures.
- E2 (menor) — Taules sense `tbl-colwidths` (estructura TLB). Opcional.

---

## Coherència amb altres temes — notes per al xat de T9

| Punt | Acció a T9 |
|:---|:---|
| CC1: `V` a la PTE | Verificar i conservar `@sec-tlb-bit-v`; afegir ref. a `@wrn-mv-notacio-v` |
| CC2: model fallada TLB | Reescriure intro `@sec-tlb`; RSE → fallada de pàgina; invertir `@wrn-tlb-page-table-walker` |
| CC3: bit D | Alinear model de T9 al d'T8 (hardware sense excepció) o documentar divergència |
| D1: terminologia | Verificar que T9 usa «memòria cau» (no `cache`) |
| Co6 (T9_tasques): «modificada» vs «modificació» | Unificar «bit de modificació» (T7) arreu |

---

## Sigles (`sigles.qmd`)
- ✅ VPN, PPN afegides.

---

## Fitxers modificats en aquest xat

| Fitxer | Canvis principals |
|:---|:---|
| `T8.qmd` | CC1, CC2, B1, B2, B5, C1, C2, D1, D2, D3 |
| `sigles.qmd` | VPN, PPN |
| `contrib.qmd` | Decisió CC1 documentada a § Decisions T8 |
| `T7.qmd` | Etiquetes `{#sec-}` duplicades eliminades (línies 41, 50) |

---

## Figures (F/G) — fase posterior

8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol E1).
Rutes des de `01_T/`: `../figures/T8_*_light.svg`.
