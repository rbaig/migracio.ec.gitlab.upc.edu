---
name: figures
description: Llista de comprovacions per crear, modificar o retirar una figura d'EC (SVG natiu, generador del pre-render o de model (a), registres de bits, Graphviz, retalls, figures dinàmiques). Carrega-la abans de tocar `22_figs_originals/`, `23_figs_externes/`, els `.toml` de figures de `24_specs/` o un generador de `25_scripts/`.
---

# Figures

Les regles són a `13_contrib.qmd §Figures i material gràfic` i a `24_specs/svg.md`, que en són l'única font. Aquí només hi ha l'ordre de la feina i les comprovacions; no en copiïs cap regla.

1. **Llegeix `24_specs/svg.md`** sencer abans de la primera figura de la sessió, i `24_specs/registres.toml` si és un registre de bits.
2. **Tria com es fa** (`svg.md §17`): una família, amb el seu TOML i un generador del pre-render (model (b), amb el sufix de la taula de `13_contrib.qmd §Convencions SVG`); una figura solta, amb l'SVG versionat i un script que el regenera (model (a), amb `--comprova`); un SVG natiu a `22_figs_originals/`; o, només si l'editor hi està d'acord, una extracció de PDF a `23_figs_externes/`.
3. **`<title>` i `<desc>`** a l'arrel de l'SVG. El `<desc>` és el text alternatiu i descriu el que es veu, sense repetir el peu.
4. **Colors** només de la paleta (`svg.md §10` i `§16`). La variant fosca la fa `gen_dark.py`: no s'edita a mà.
5. **Al `.qmd`**, el marcatge de `13_contrib.qmd §Integració al .qmd` (o de §Figures dinàmiques), i una remissió `@fig-…` des del text si és al cos del text.
6. **Els avisos de l'inventari** te'ls dona `make comprova` (i el hook) a cada commit. La taula sencera, `make inventari` (`25_scripts/out_inventari_figures/figures.md`, no versionat).
7. **`make registres`**, si has tocat un generador de model (a): en regenera els SVG, i `make comprova` comprova que coincideixen amb el que generen.
8. **Mira-la renderitzada**, en clar i en fosc a l'HTML i al PDF (skill `render`).
