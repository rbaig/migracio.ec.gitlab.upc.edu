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

Directori `02_exercicis/`:

| Fitxer | Contingut |
| :--- | :--- |
| `E1.qmd`–`E9.qmd` | Problemes: enunciats del Tema x (x = 1–9) |

Directori `03_solucions/`:

| Fitxer | Contingut |
| :--- | :--- |
| `S1.qmd`–`S9.qmd` | Problemes: solucions d'una selecció d'exercicis del Tema x (x = 1–9) |
| `S_criteris_seleccio.qmd` | Criteris de selecció dels problemes resolts |

La correspondència entre els temes d'EC i els PDFs originals (MIPS) **no és 1:1**: la introducció de rendiment, potència i llei d'Amdahl (PDF T1) s'ha segregat al T6; els PDFs T6–T8 corresponen als temes T7–T9.

### Laboratori (L1–L6)

Directori `04_laboratori/`:

| Fitxer | Contingut |
| :--- | :--- |
| `L1.qmd`–`L6.qmd` | Laboratori, sessió y (y = 1–6) |

### Fitxers transversals

| Fitxer | Contingut |
| :--- | :--- |
| `_quarto.yml` | Configuració del projecte Quarto |
| `Makefile` | `make render` (genera les taules fusionades i renderitza) i `make clean` |
| `_variables.yml` | Variables globals del projecte (títols de tema, URLs, etc.) |
| `15_bibliografia.bib` | Base de dades bibliogràfica (BibTeX) |
| `CLAUDE.md` | Instruccions operatives per a Claude |
| `13_contrib.qmd` | Guia de contribució: convencions, estil, flux de treball |
| `custom_dark.scss` | Estils CSS addicionals per al mode fosc (HTML) |
| `custom_light.scss` | Estils CSS addicionals per al mode clar (HTML) |
| `custom.scss` | Estils CSS comuns a tots dos modes (HTML) |
| `ieee.csl` | Estil de citació IEEE (CSL) |
| `index.qmd` | Pàgina de presentació (avaluació, eines, bibliografia) |
| `preamble.tex` | Preàmbul LaTeX addicional (PDF) |
| `11_riscv.qmd` | Compendi de referència RISC-V (inclòs via `include`) |
| `12_sigles.qmd` | Glossari de sigles |
| `styles.css` | Estils CSS addicionals (HTML) |
| `24_specs/svg.md` | Especificacions d'estil per a les figures SVG |
| `TODO.md` | Llista de tasques pendents (contingut transitori) |

### Arbre de directoris

```
.
├── .vscode/                    # Diccionari
├── 01_apunts/                  # Apunts        (`Ax.qmd`, x ∈ [1, 9])
├── 02_exercicis/                # Problemes     (`Ex.qmd`, x ∈ [1, 9])
├── 03_solucions/               # Solucions     (`Sx.qmd`, x ∈ [1, 9])
├── 04_laboratori/              # Laboratori    (`Ly.1md`, y ∈ [1, 6])
│   ├── Ly/                     # Plantilles sessió y
│   └── rars1_6.jar             # Simulador RARS (versió de referència)
├── 21_riscv/                   # Contingut de taules de `.callout-note`
├── 22_figs_originals/
├── 23_figs_externes/
├── 24_specs/
├── 25_scripts/
├── _book                       # Quarto: Directori de sortida
├── auto_figs/                  # Figures generades per script (s'elimina a cada render)
├── auto_riscv/                 # Taules generades per script (s'elimina a cada render)
├── index_files/                # Quarto
├── TODO/                       # Fitxers de suport a l'edició
├── 11_riscv.qmd
├── 12_sigles.qmd
├── 13_contrib.qmd
├── 14_LICENSE.qmd
├── 15_bibliografia.bib
├── CLAUDE.md
├── custom_dark.scss
├── custom_light.scss
├── custom.scss
├── dark_exclusions.txt
├── Estructura-de-computadors.tex
├── ieee.csl
├── index.qmd
├── LICENSE.md
├── Makefile
├── preamble.tex
├── _quarto.yml
├── README.md
├── styles.css
└── _variables.yml
```

## Renderitzar el projecte

Directori de treball:

```bash
cd ~/git/EC
```

| Comanda | Efecte |
| :--- | :--- |
| `make render` | Genera les taules fusionades (`auto_riscv/`) i tot seguit renderitza les dues sortides |
| `make clean` | Elimina els artefactes de render (`_book`, `*_files`, `*.html`, `*.log`, `Estructura-de-computadors.tex`) |
| `quarto render --to html` | Renderitza HTML (ràpid; recomanat durant el desenvolupament) |
| `quarto render --to pdf` | Renderitza PDF (lent; requereix LaTeX) |
| `quarto render` | Renderitza les dues sortides |

> **Nota**: `quarto render --to html` neteja la carpeta `_book` abans de renderitzar. Si cal conservar el PDF generat, feu `quarto render` complet (o `make render`) o guardeu el PDF abans.

> **Taules fusionades de `11_riscv.qmd`**: `make render` ja genera `auto_riscv/` abans de renderitzar. Si en comptes d'això useu `quarto render` directament i obteniu un error del tipus `could not find file .../auto_riscv/NOM.qmd`, executeu primer:
>
> ```bash
> python3 25_scripts/gen_taules_auto.py 24_specs/taules_fusio.toml 21_riscv --output-dir="auto_riscv/"
> ```
>
> Cal repetir-ho el primer cop després de clonar el repositori, i sempre que editeu un fitxer de `21_riscv/` que aparegui a `24_specs/taules_fusio.toml`: si no, `auto_riscv/` queda desactualitzat en silenci (el render no fallarà, però la taula no reflectirà el canvi). Detalls tècnics a `13_contrib.qmd` §Fitxer de referència tècnica.

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

Vegeu el fitxer [`13_contrib.qmd`](13_contrib.qmd), que conté:

- El flux de treball amb Git (branques, commits, Merge Requests).
- Les convencions d'estil (veu, puntuació, negretes, anglicismes, sigles).
- El sistema de callouts i prefixos d'etiquetes.
- Les convencions de figures SVG i blocs de codi.
- Les decisions terminològiques i de format per tema.

## Llicència

Aquest material es publica sota la llicència [Creative Commons Reconeixement-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca).

Podeu copiar-lo, distribuir-lo i adaptar-lo sempre que en reconegueu l'autoria, no en feu un ús comercial i distribuïu les obres derivades sota la mateixa llicència.
