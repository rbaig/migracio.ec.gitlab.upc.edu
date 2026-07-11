# T7 — Revisió interna profunda: llista d'accions

**Fitxer objectiu:** `01_apunts/A7.qmd`
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent · ⚪ neteja

### Figures pendents de generar ⏳

Totes requereixen LO Draw de Roger o referència externa.

| ID Quarto | Descripció | Bloqueig |
|:---|:---|:---|
| `fig-mc-exemple-descomposicio-32bits` | Descomposició 32 bits adreça `0x100100F8` | LO Draw disponible a `23_figs_externes` (export antic) — reconstruir com a natiu |
| `fig-cd-diagrama` | Diagrama blocs MC correspondència directa | LO Draw pendent |
| `fig-assoc-conjunts-diagrama` | Diagrama blocs MC associativa per conjunts | LO Draw pendent |
| `fig-ca-diagrama` | Diagrama blocs MC completament associativa | LO Draw pendent |
| `fig-texe-diagrama` | Diagrama temporal lw/addu/lw ideal vs. real | Referència: pàg. 24 PDF original |
| `fig-lru-roger` | Màquina d'estats LRU | Inclosa a `T7_lru_exemple.svg` (Roger); potser suficient |
| `fig-multinivell-diagrama` | CPU→L1→L2→MP | LO Draw pendent |
| `fig-multinivell-multicore` | Xip 4 nuclis L1/L2/L3 | LO Draw pendent |

### Warnings de referència trencada pendents

```
WARN T7.html: @fig-cd-diagrama           → pendent LO Draw
WARN T7.html: @fig-assoc-conjunts-diagrama → pendent LO Draw
WARN T7.html: @fig-ca-diagrama           → pendent LO Draw
WARN T7.html: @fig-texe-diagrama         → pendent PDF pàg. 24
```

*(Resolts en aquest xat: `@fig-gap-processador-memoria` ✅)*


## Decisions obertes

- 🔵 `fig-capacitat-exemple`: HTML mostra dues figures separades (primera+segona passada); PDF igual. Alternativa: figura única combinada per a HTML. Pendent de decisió.
- 🔵 `fig-lru-roger` (màquina d'estats LRU): determinar si cal com a figura independent o és suficient la inclusió dins `T7_lru_exemple.svg`.
