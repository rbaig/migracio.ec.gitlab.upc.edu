# Estructura de Computadors — Apunts

Material escrit de l'assignatura **Estructura de Computadors** (EC), assignatura obligatòria de 7,5 crèdits del segon quadrimestre (Q2) del [Grau en Enginyeria Informàtica](https://www.fib.upc.edu/ca/graus/grau-en-enginyeria-informatica) (GEI) de la [Facultat d'Informàtica de Barcelona](https://www.fib.upc.edu) (FIB), Universitat Politècnica de Catalunya (UPC).

Llengua: **català**. Sortida: **HTML** (web) i **PDF** (imprimible).

Elaborat amb [Quarto](https://quarto.org/) i [Claude](https://claude.ai/) (Anthropic).

## Estructura del projecte

### Teoria (T1–T9)

Directori `01_apunts/`:

| Fitxer | Contingut |
| :--- | :--- |
| `A1.qmd`–`A9.qmd` | Teoria del Tema x (x = 1–9) |

Directori `02_problemes/`:

| Fitxer | Contingut |
| :--- | :--- |
| `P1.qmd`–`P9.qmd` | Problemes: enunciats del Tema x (x = 1–9) |

Directori `03_solucions/`:

| Fitxer | Contingut |
| :--- | :--- |
| `S1.qmd`–`S9.qmd` | Solucions d'una selecció dels problemes del Tema x (x = 1–9) |

La correspondència entre els temes d'EC i els PDF originals (MIPS) **no és 1:1**: la introducció de rendiment, potència i llei d'Amdahl (PDF T1) s'ha segregat al T6; els PDF T6–T8 corresponen als temes T7–T9.

### Laboratori (L1–L6)

Directori `04_laboratori/`:

| Fitxer | Contingut |
| :--- | :--- |
| `L1.qmd`–`L6.qmd` | Laboratori, sessió y (y = 1–6) |

### Fitxers transversals

| Fitxer | Contingut |
| :--- | :--- |
| `_quarto.yml` | Configuració del projecte Quarto |
| `Makefile` | `make render` / `make render-complet` (HTML, o HTML + PDF) i `make clean` |
| `_variables.yml` | Variables globals del projecte (títols de tema, URL, etc.) |
| `15_bibliografia.bib` | Base de dades bibliogràfica (BibTeX) |
| `CLAUDE.md` | Instruccions operatives per a les sessions de Claude Code |
| `13_contrib.qmd` | Guia de contribució (capítol «Contribueix-hi»): les regles del llibre i el flux de treball |
| `24_specs/registre_de_decisions.md` | Registre de decisions: el perquè i l'historial de les regles de `13_contrib.qmd` |
| `custom_dark.scss` | Estils CSS addicionals per al mode fosc (HTML) |
| `custom_light.scss` | Estils CSS addicionals per al mode clar (HTML) |
| `custom.scss` | Estils CSS comuns a tots dos modes (HTML) |
| `ieee.csl` | Estil de citació IEEE (CSL) |
| `index.qmd` | Pàgina de presentació (avaluació, eines, bibliografia) |
| `preamble.tex` | Preàmbul LaTeX addicional (PDF) |
| `11_riscv.qmd` | Compendi de referència RISC-V (inclòs via `include`) |
| `12_sigles_simbols.qmd` | Glossari de sigles i símbols |
| `styles.css` | Estils CSS addicionals (HTML) |
| `24_specs/svg.md` | Especificacions d'estil per a les figures SVG |
| `TODO.md` | Llista de tasques pendents (contingut transitori) |

### Arbre de directoris

```
.
├── .claude/                    # Claude Code: hooks, skills i subagents (vegeu `13_contrib.qmd §IA`)
├── .github/                    # Workflow de publicació a GitHub Pages
├── .vscode/                    # Diccionari
├── 01_apunts/                  # Apunts        (`Ax.qmd`, x ∈ [1, 9])
├── 02_problemes/               # Problemes     (`Px.qmd`, x ∈ [1, 9])
├── 03_solucions/               # Solucions     (`Sx.qmd`, x ∈ [1, 9])
├── 04_laboratori/              # Laboratori    (`Ly.qmd`, y ∈ [1, 6])
├── 05_diapositives/            # Reservat (encara sense contingut)
├── 21_riscv/                   # Contingut de taules de `.callout-note`
├── 22_figs_originals/
├── 23_figs_externes/
├── 24_specs/
├── 25_scripts/
├── _book/                      # Generat · Quarto: directori de sortida
├── auto_figs/                  # Generat · Figures per script (s'elimina a cada render)
├── auto_riscv/                 # Generat · Taules per script (s'elimina a cada render)
├── .gitignore
├── 11_riscv.qmd
├── 12_sigles_simbols.qmd
├── 13_contrib.qmd
├── 14_LICENSE.qmd
├── 15_bibliografia.bib
├── CLAUDE.md
├── custom_dark.scss
├── custom_light.scss
├── custom.scss
├── dark_exclusions.txt
├── Estructura-de-computadors.tex   # Generat · Font LaTeX del PDF (no versionada)
├── ieee.csl
├── index.qmd
├── LICENSE.md
├── Makefile
├── preamble.tex
├── _quarto.yml
├── README.md
├── styles.css
├── TODO.md
└── _variables.yml
```

**Temes.** Un tema `Tx` (T1–T9) és el conjunt dels seus apunts, problemes i solucions, `Ax.qmd`, `Px.qmd` i `Sx.qmd`; és el sentit de «T3» a la guia, al `TODO.md` i al registre de decisions (`13_contrib.qmd §T2 i T3`, per exemple). El laboratori (`Ly.qmd`) es numera per sessions, no per temes.

## Renderitzar el projecte

Directori de treball:

```bash
cd ~/git/EC
```

| Comanda | Efecte |
| :--- | :--- |
| `make render` | Genera les taules fusionades (`auto_riscv/`) i renderitza **només l'HTML** (bucle diari, segons) |
| `make render-complet` | Genera les taules fusionades i renderitza **HTML + PDF** (~7 min; requereix LaTeX) |
| `make taules` | Genera només les taules fusionades (`auto_riscv/`), sense renderitzar; `render` i `render-complet` ja en depenen |
| `make clean` | Elimina els artefactes de render (`_book`, `*_files`, `*.html`, `*.log`, `Estructura-de-computadors.tex`) |
| `quarto render --to html` | Renderitza HTML sense generar les taules fusionades |
| `quarto render --to pdf` | Renderitza PDF (lent; requereix LaTeX) |
| `quarto render` | Renderitza les dues sortides |

Què neteja cada ordre, quan cal `make render-complet` i com es generen les taules fusionades de `11_riscv.qmd` (`auto_riscv/`), a `13_contrib.qmd §Verificació de l'entorn`, §Renderitzar el projecte i §Fitxer de referència tècnica.

Neteja:

```bash
make clean
```

O manualment (aneu amb compte: `*.tex` també coincidiria amb `preamble.tex`, que és font versionada — no l'esborreu):

```bash
rm -f *.html *.log Estructura-de-computadors.tex
rm -rf *_files _book
```

## Instal·lació

### Quarto (≥ 1.5)

```bash
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.36/quarto-1.9.36-linux-amd64.deb
sudo dpkg -i quarto-1.9.36-linux-amd64.deb
quarto --version
```

Sense Chrome instal·lat (p. ex. en un servidor):

```bash
quarto install chrome-headless-shell
```

### TinyTeX (per a PDF)

```bash
quarto install tinytex
```

### Verificació de l'entorn

```bash
quarto check
```

### RARS (simulador RISC-V)

Descarregueu [`rars1_6.jar`](https://github.com/TheThirdOne/rars/releases/download/v1.6/rars1_6.jar) i assegureu-vos de tenir el [Java Runtime Environment (JRE)](https://www.java.com/en/download/help/download_options.html) versió 8.0 o superior.

## Contribució

Vegeu el fitxer [`13_contrib.qmd`](13_contrib.qmd) (el capítol «Contribueix-hi» del llibre), que conté les regles; el perquè i l'historial de cada una són a [`24_specs/registre_de_decisions.md`](24_specs/registre_de_decisions.md). La guia conté:

- El flux de treball amb Git (branques, commits, Merge Requests).
- Les convencions d'estil (veu, puntuació, negretes, anglicismes, sigles).
- El sistema de callouts i prefixos d'etiquetes.
- Les convencions de figures SVG i blocs de codi.
- Les decisions terminològiques i de format per tema.

## Llicència

Aquest material es publica sota la llicència [Creative Commons Reconeixement-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca).

Podeu copiar-lo, distribuir-lo i adaptar-lo sempre que en reconegueu l'autoria, no en feu un ús comercial i distribuïu les obres derivades sota la mateixa llicència.
