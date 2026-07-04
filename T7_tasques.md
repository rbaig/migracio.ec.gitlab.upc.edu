# T7 — Revisió interna profunda: llista d'accions

**Fitxer objectiu:** `01_T/T7.qmd`
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent · ⚪ neteja

---

## Tasques A–E ✅ TANCADES

Totes les tasques d'exploració, revisió tècnica (B1–B6), pedagògica (C1–C2),
lingüística (D1–D8) i de format Quarto (E1–E7) estan aplicades a `T7.qmd`.

Canvis destacats: reescriptura exemple conflicte (B1), correccions latència/cicles (B3),
$\alpha$→$P_x$ al bloc Amdahl (B6), `offset`→`desplaçament` a la prosa (D1),
`multicore`→`multinucli` (D3), 4 `{#sec-}` afegits (E3), slug `reemplacament` (E5).

---

## Tasca F/G — Figures SVG

### Política

**Canvas estàndard: 800px** per a les figures de la sèrie MC (escriptura, LRU, conflicte,
capacitat). Classe `ampla` (960px) reservada per a pipelines i diagrames multicore.
Tots els SVG generats per Claude van a `12_figs_originals/`; el pre-render els processa
com a `__original_light/dark`. Les figures externes (extrets de PDF o LO Draw sense
reconstrucció) van a `13_figs_externes/` com a `__extern_light/dark`.

Decisions de disseny establertes en aquest xat:
- Colors Miss/Hit: `#dc3545`/`#198754` (afegits a `svg.md §10` com a colors d'etiqueta)
- Colors de zona bloc MP/MC: 4 colors de paleta + 2 nous (`#f8d0d3`/`#dc3545` i `#c8ebd8`/`#198754`, afegits a `svg.md §10` i `REPLACEMENTS`)
- Cold Miss: ambre `#664d03` · Conflict Miss: vermell `#dc3545` · Capacity Miss: verd `#198754`
- Fonts: `'Liberation Sans'` / `'Liberation Mono'` (per `svg.md §12`)
- `width="100%"` al SVG (sense percentatge al `.qmd`)

### Figures integrades a `T7.qmd` ✅

| ID Quarto | Fitxer font | Directori | Estat |
|:---|:---|:---|:---|
| `fig-jerarquia-piramide` | `T7_jerarquia_piramide` | `12_figs_originals` | ✅ |
| `fig-mc-organitzacio` | `T7_mc_organitzacio` | `12_figs_originals` | ✅ |
| `fig-mc-encert` | `T7_mc_encert` | `12_figs_originals` | ✅ |
| `fig-mc-fallada` | `T7_mc_fallada` | `12_figs_originals` | ✅ |
| `fig-cd-descomposicio-bits` | `T7_cd_descomposicio_bits` | `12_figs_originals` | ✅ |
| `fig-gap-processador-memoria` | `T7_gap_processador_memoria` | `13_figs_externes` | ✅ integrat aquest xat |
| `fig-i9-13900k-die` | *(fotografia)* | — | ✅ |
| `fig-escriptura-dirty-bit` | `T7_escriptura_dirty_bit` | `12_figs_originals` | ✅ fet manualment per Roger |
| `fig-escriptura-estat-inicial` | `T7_escriptura_estat_inicial` | `12_figs_originals` | ✅ generat+integrat |
| `fig-escriptura-immediata-amb-assignacio` | `T7_escriptura_immediata_amb_assignacio` | `12_figs_originals` | ✅ generat+integrat |
| `fig-escriptura-immediata-sense-assignacio` | `T7_escriptura_immediata_sense_assignacio` | `12_figs_originals` | ✅ generat+integrat |
| `fig-escriptura-retardada` | `T7_escriptura_retardada` | `12_figs_originals` | ✅ generat+integrat |
| `fig-lru-exemple` | `T7_lru_exemple` | `12_figs_originals` | ✅ fet manualment per Roger+integrat |
| `fig-assoc-conjunts-taula` | `T7_assoc_conjunts_taula` | `12_figs_originals` | ✅ generat+integrat |
| `fig-conflicte-exemple` | `T7_conflicte_exemple` | `12_figs_originals` | ✅ generat+integrat |
| `fig-capacitat-exemple-bucle-primera-passada` | `T7_capacitat_exemple_bucle_primera_passada` | `12_figs_originals` | ✅ generat+integrat |
| `fig-capacitat-exemple-bucle-segona-passada` | `T7_capacitat_exemple_bucle_segona_passada` | `12_figs_originals` | ✅ generat+integrat |

### Figures pendents de generar ⏳

Totes requereixen LO Draw de Roger o referència externa.

| ID Quarto | Descripció | Bloqueig |
|:---|:---|:---|
| `fig-mc-exemple-descomposicio-32bits` | Descomposició 32 bits adreça `0x100100F8` | LO Draw disponible a `13_figs_externes` (export antic) — reconstruir com a natiu |
| `fig-cd-diagrama` | Diagrama blocs MC correspondència directa | LO Draw pendent |
| `fig-assoc-conjunts-diagrama` | Diagrama blocs MC associativa per conjunts | LO Draw pendent |
| `fig-ca-diagrama` | Diagrama blocs MC completament associativa | LO Draw pendent |
| `fig-texe-diagrama` | Diagrama temporal lw/addu/lw ideal vs. real | Referència: pàg. 24 PDF original |
| `fig-lru-roger` | Màquina d'estats LRU | Inclosa a `T7_lru_exemple.svg` (Roger); potser suficient |
| `fig-multinivell-diagrama` | CPU→L1→L2→MP | LO Draw pendent |
| `fig-multinivell-multicore` | Xip 4 nuclis L1/L2/L3 | LO Draw pendent |

### Figures descartades definitivament ⚪

`fig-tres-c-barres` (gràfic de dades sense valors numèrics disponibles).

### Warnings de referència trencada pendents

```
WARN T7.html: @fig-cd-diagrama           → pendent LO Draw
WARN T7.html: @fig-assoc-conjunts-diagrama → pendent LO Draw
WARN T7.html: @fig-ca-diagrama           → pendent LO Draw
WARN T7.html: @fig-texe-diagrama         → pendent PDF pàg. 24
```

*(Resolts en aquest xat: `@fig-gap-processador-memoria` ✅)*

---

## Fitxers modificats en aquest xat

| Fitxer | Canvis |
|:---|:---|
| `01_T/T7.qmd` | Integració de 11 figures noves + `fig-gap-processador-memoria` |
| `21_specs/svg.md` | Colors Miss/Hit zona bloc afegits a §10 i `REPLACEMENTS` |
| `12_figs_originals/` | 10 SVG nous generats (sèrie escriptura, assoc_conjunts_taula, conflicte, capacitat×2) |
| `13_figs_externes/` | `T7_gap_processador_memoria` (ja existent, integrat) |

---

## Decisions obertes

- 🔵 `fig-capacitat-exemple`: HTML mostra dues figures separades (primera+segona passada); PDF igual. Alternativa: figura única combinada per a HTML. Pendent de decisió.
- 🔵 `fig-lru-roger` (màquina d'estats LRU): determinar si cal com a figura independent o és suficient la inclusió dins `T7_lru_exemple.svg`.
