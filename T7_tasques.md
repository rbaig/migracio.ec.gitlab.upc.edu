# T7 — Revisió interna profunda: llista d'accions

**Fitxer objectiu:** `01_T/T7.qmd` (800 línies)
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent · ⚪ neteja

---

## Tasques A–E ✅ TANCADES

Totes les tasques d'exploració, revisió tècnica (B1–B6), pedagògica (C1–C2),
lingüística (D1–D8) i de format Quarto (E1–E7) estan aplicades a `T7.qmd`.

Canvis destacats: reescriptura exemple conflicte (B1), correccions latència/cicles (B3),
$\alpha$→$P_x$ al bloc Amdahl (B6), `offset`→`desplaçament` a la prosa (D1),
`multicore`→`multinucli` (D3), 4 `{#sec-}` afegits (E3), slug `reemplacament` (E5).

---

## Tasca F/G — Figures SVG ⏳ PENDENT

### Política

**SVG natiu per defecte** (elements `<rect>`, `<line>`, `<text>`, etc., paleta del projecte).
L'extracció de PDF es reserva per a figures de complexitat excepcional, decidida conjuntament.
Les figures de LO Draw es passen com a SVG exportat (esbós de referència); Claude les reconstrueix com a SVG natiu net.

### Figures integrades al `.qmd` amb SVG existent ✅

| ID | SVG al repositori |
|:---|:---|
| `@fig-jerarquia-piramide` | `T7_jerarquia_piramide` |
| `@fig-mc-organitzacio` | `T7_mc_organitzacio` |
| `@fig-mc-encert` | `T7_mc_encert` |
| `@fig-mc-fallada` | `T7_mc_fallada` |
| `@fig-cd-descomposicio-bits` | `T7_cd_descomposicio_bits` |
| `@fig-gap-processador-memoria` | `T7_gap_processador_memoria` |
| `@fig-i9-13900k-die` | *(fotografia, ja integrada)* |

### Figures pendents ⏳

| ID | Descripció | Notes |
|:---|:---|:---|
| `fig-mc-exemple-descomposicio-32bits` | Taula MC (V, Etiqueta, Bloc de dades) — contingut igual a `mc_organitzacio` però per a l'exemple de `0x100100F8` dins `@tip-mc-numbloc` | Referència: `T7_mc_organitzacio__original_light.svg` existent |
| `fig-cd-diagrama` | Diagrama blocs maquinari MC correspondència directa (decodificador, comparador, mux) | Referència: `T7_cd_diagrama__original_light.svg` (LO Draw, passat per Roger) |
| `fig-assoc-conjunts-diagrama` | Diagrama blocs MC associativa per conjunts (N comparadors en paral·lel, OR, mux N:1) | Anàleg a fig-cd-diagrama però associativa |
| `fig-ca-diagrama` | Diagrama blocs MC completament associativa (tots comparadors sobre totes les línies, sense decodificador) | 🔴 referència trencada al `.qmd` |
| `fig-texe-diagrama` | Diagrama temporal lw/addu/lw (etapes F/D/R/A/M/W, ideal vs. real amb penalització) | Referència: pàg. 24 PDF original |
| `fig-lru-exemple` | Evolució estat MC (conjunt 1, 2 vies) als 4 accessos LRU (4, 38, 6, 52) | Possiblement amb `fig-lru-roger` com a mosca |
| `fig-lru-roger` | Màquina d'estats de l'algorisme LRU | SVG natiu; pot anar com a mosca dins `fig-lru-exemple` |

### Figures placeholder descartades / a decidir

| ID | Estat |
|:---|:---|
| `fig-assoc-conjunts-taula` | ⏳ Taula 4 conjunts × 3 vies — pendent |
| `fig-escriptura-estat-inicial` | ⏳ Estat MC 5 lectures inicials — pendent |
| `fig-escriptura-immediata-assignacio` | ⏳ pendent |
| `fig-escriptura-immediata-sense-assignacio` | ⏳ pendent |
| `fig-escriptura-retardada` | ⏳ pendent (inclou columna D) |
| `fig-tres-c-barres` | ⏳ Gràfic % fallades vs. associativitat — pendent |
| `fig-conflicte-exemple` | ⏳ Taula estat MC exemple conflicte — pendent |
| `fig-capacitat-exemple` | ⏳ Taula estat MC exemple capacitat — pendent |
| `fig-multinivell-diagrama` | ⏳ CPU→L1→L2→MP — pendent |
| `fig-multinivell-multicore` | ⏳ Xip 4 nuclis L1/L2/L3 — pendent |

### Figures de referència disponibles (al repositori)

Per mantenir coherència visual, usar sempre com a referència:
- `T7_mc_organitzacio__original_light.svg` — estil de taules (blau, neutre, capçalera)
- `T7_cd_descomposicio_bits__original_light.svg` — estil de descomposició de bits (claudàtors, colors camps)
- `T7_mc_encert__original_light.svg` — estil de diagrames CPU/MC/MP amb fletxes

---

## Pendent d'actualitzar (ja fet en aquest xat)

- `07_contrib.qmd`: criteri linting ✅, criteri E6 ✅, convenció A d'integració ✅
- `CLAUDE.md`: política figures SVG ✅
