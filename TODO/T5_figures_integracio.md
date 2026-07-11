# Integració de les figures de coma flotant a T5

Tres fitxers font (light) a `22_figs_originals/`. El pre-render (`norm_font.py` + `gen_dark.py`)
en genera automàticament `auto_figs/T5_<nom>__original_{light,dark}.svg`. **No cal crear la variant
dark manualment**: tots els traços/textos són `#000000`, que la taula de substitució converteix a
`#adb5bd` en mode fosc.

| Font (`22_figs_originals/`) | On va a T5 |
| :--- | :--- |
| `T5_exponent.svg` | `### L'estàndard IEEE-754` (prop de `#cau-exces-comparacio` / `#### Exponent`) |
| `T5_recta_global.svg` | `### Rang i precisió` |
| `T5_recta_zoom_zero.svg` | `### Codificacions especials` (prop de `#### Denormals`) |

---

## 1. Figura de l'exponent → `### L'estàndard IEEE-754`

```markdown
::: {#fig-exponent-ieee754}
::: {.content-visible when-format="html"}
::: {.light-content}
![](/auto_figs/T5_exponent__original_light.svg)
:::
::: {.dark-content}
![](/auto_figs/T5_exponent__original_dark.svg)
:::
:::
::: {.content-visible when-format="pdf"}
![](/auto_figs/T5_exponent__original_light.svg)
:::
Correspondència entre l'exponent emmagatzemat ($E$, 0–255) i l'exponent real ($e = E - 127$): els denormals ocupen $E=0$ i $\pm\infty$/NaN ocupen $E=255$.
:::
```

Referència al text amb `@fig-exponent-ieee754`.

## 2. Recta global → `### Rang i precisió`

```markdown
::: {#fig-recta-global}
::: {.content-visible when-format="html"}
::: {.light-content}
![](/auto_figs/T5_recta_global__original_light.svg)
:::
::: {.dark-content}
![](/auto_figs/T5_recta_global__original_dark.svg)
:::
:::
::: {.content-visible when-format="pdf"}
![](/auto_figs/T5_recta_global__original_light.svg)
:::
Recta de la coma flotant IEEE-754 (simple precisió): $\pm\infty$ i NaN als extrems ($E=255$) i les potències de 2 equiespaiades, perquè l'exponent és lineal.
:::
```

## 3. Recta — zoom al zero → `### Codificacions especials`

```markdown
::: {#fig-recta-zoom-zero}
::: {.content-visible when-format="html"}
::: {.light-content}
![](/auto_figs/T5_recta_zoom_zero__original_light.svg)
:::
::: {.dark-content}
![](/auto_figs/T5_recta_zoom_zero__original_dark.svg)
:::
:::
::: {.content-visible when-format="pdf"}
![](/auto_figs/T5_recta_zoom_zero__original_light.svg)
:::
Zoom al voltant del zero: $\pm 0$ i els denormals ($E=0$) omplen el buit entre el zero i el normal més petit ($2^{-126}$).
:::
```

---

## Notes

- **Amplada (PDF)**: `T5_recta_global.svg` (1820 px) i `T5_recta_zoom_zero.svg` (1360 px) són figures
  amples. En HTML s'ajusten bé; en PDF, escalades a l'amplada de text queden petites. Si cal, posar-les
  en una pàgina apaïsada (`pdflscape`: `\begin{landscape} … \end{landscape}`) o reduir el nombre de
  columnes. La divisió en dues (global + zoom) ja redueix molt la densitat respecte de l'original.
- **Realçat vermell perdut**: a `T5_exponent`, les etiquetes «−127»/«+127» del biaix tenien color
  vermell només en mode fosc (via `light-dark()`). S'ha unificat a negre per conformitat amb el
  pipeline. Si es vol recuperar l'èmfasi, es pot posar en negreta o afegir el fitxer a
  `dark_exclusions.txt` amb una dark retocada.
- **Correccions aplicades respecte dels SVG originals**: línia de puntets enganyosa eliminada
  (exponent); hex malformats, NaN duplicat com a ∞, i 0x3E000000 etiquetat com a 0,25 (és 0,125)
  corregits (recta); fonts → Liberation Sans; decimals amb coma; `light-dark()` → colors plans.
