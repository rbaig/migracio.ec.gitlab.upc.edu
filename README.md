# Estructura de Computadors — Apunts

Material escrit de l'assignatura **Estructura de Computadors** (EC), assignatura obligatòria de 7,5 crèdits del segon quadrimestre (Q2) del [Grau en Enginyeria Informàtica](https://www.fib.upc.edu/ca/graus/grau-en-enginyeria-informatica) (GEI) de la [Facultat d'Informàtica de Barcelona](https://www.fib.upc.edu) (FIB), Universitat Politècnica de Catalunya (UPC).

Llengua: **català**. Sortida: **HTML** (web) i **PDF** (imprimible).

Elaborat amb [Quarto](https://quarto.org/) i [Claude](https://claude.ai/) (Anthropic).

## Estructura del projecte

### Teoria (T1–T9)

Directori `01_T/`:

| Fitxer | Contingut |
| :--- | :--- |
| `T1.qmd`–`T9.qmd` | Teoria del Tema x (x = 1–9) |

Directori `02_PE/`:

| Fitxer | Contingut |
| :--- | :--- |
| `PE_T1.qmd`–`PE_T9.qmd` | Problemes: enunciats del Tema x (x = 1–9) |

Directori `03_PS/`:

| Fitxer | Contingut |
| :--- | :--- |
| `PS_T1.qmd`–`PS_T9.qmd` | Problemes: solucions d'una selecció d'exercicis del Tema x (x = 1–9) |
| `PS_criteris.qmd` | Criteris de selecció dels problemes resolts |

La correspondència entre els temes d'EC i els PDFs originals (MIPS) **no és 1:1**: la introducció de rendiment, potència i llei d'Amdahl (PDF T1) s'ha segregat al T6; els PDFs T6–T8 corresponen als temes T7–T9.

### Laboratori (L1–L6)

Directori `04_L/`:

| Fitxer | Contingut |
| :--- | :--- |
| `L1.qmd`–`L6.qmd` | Laboratori, sessió y (y = 1–6) |

### Fitxers transversals

| Fitxer | Contingut |
| :--- | :--- |
| `_quarto.yml` | Configuració del projecte Quarto |
| `_variables.yml` | Variables globals del projecte (títols de tema, URLs, etc.) |
| `bibliografia.bib` | Base de dades bibliogràfica (BibTeX) |
| `CLAUDE.md` | Instruccions operatives per a Claude |
| `contrib.qmd` | Guia de contribució: convencions, estil, flux de treball |
| `custom_dark.scss` | Estils CSS addicionals per al mode fosc (HTML) |
| `custom_light.scss` | Estils CSS addicionals per al mode clar (HTML) |
| `custom.scss` | Estils CSS comuns a tots dos modes (HTML) |
| `ieee.csl` | Estil de citació IEEE (CSL) |
| `index.qmd` | Pàgina de presentació (avaluació, eines, bibliografia) |
| `preamble.tex` | Preàmbul LaTeX addicional (PDF) |
| `riscv.qmd` | Compendi de referència RISC-V (inclòs via `include`) |
| `sigles.qmd` | Glossari de sigles |
| `styles.css` | Estils CSS addicionals (HTML) |
| `svg_specs.md` | Especificacions d'estil per a les figures SVG |
| `TODO.md` | Llista de tasques pendents (contingut transitori) |

### Arbre de directoris

```
EC/
├── 01_T/                       # Teoria
│   └── Tx.qmd                  # x = 1–9
├── 02_PE/                      # Enunciats de problemes
│   └── PE_Tx.qmd               # x = 1–9
├── 03_PS/                      # Solucions seleccionades
│   ├── PS_Tx.qmd               # x = 1–9
│   └── PS_criteris.qmd
├── 04_L/                       # Laboratori
│   └── Ly.qmd                  # y = 1–6
├── figures/                    # Figures SVG (variants light i dark)
│   └── T<N>_nom_figura_{light,dark}.svg
├── laboratori/                 # Fitxers de suport del laboratori
│   ├── L0/–L5/                 # Plantilles i fitxers per sessió
│   ├── rars1_6.jar             # Simulador RARS (versió de referència)
│   └── startup.s               # Fitxer d'inicialització RARS
├── riscv/                      # Fragments de referència RISC-V (inclosos via `include`)
│   ├── RV32I_instruccions_*.qmd
│   ├── RV32I_registres_*.qmd
│   ├── RV32I_format_instruccions.qmd
│   └── RARS_*.qmd
├── extern/                     # Figures i recursos externs (no SVG propi)
├── scripts/                    # Scripts auxiliars (p. ex. generació de SVGs)
├── _quarto.yml
├── _variables.yml
├── bibliografia.bib
├── CLAUDE.md
├── contrib.qmd
├── custom_dark.scss
├── custom_light.scss
├── custom.scss
├── ieee.csl
├── index.qmd
├── preamble.tex
├── riscv.qmd
├── sigles.qmd
├── styles.css
├── svg_specs.md
└── TODO.md
```

## Renderitzar el projecte

Directori de treball:

```bash
cd ~/git/EC
```

| Comanda | Efecte |
| :--- | :--- |
| `quarto render --to html` | Renderitza HTML (ràpid; recomanat durant el desenvolupament) |
| `quarto render --to pdf` | Renderitza PDF (lent; requereix LaTeX) |
| `quarto render` | Renderitza les dues sortides |
| `quarto preview` | Previsualització en viu (VS Code) |

> **Nota**: `quarto render --to html` neteja la carpeta `_book` abans de renderitzar. Si cal conservar el PDF generat, feu `quarto render` complet o guardeu el PDF abans.

Neteja:

```bash
rm *.html *.log *.tex
rm -rf *_files
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

Vegeu el fitxer [`contrib.qmd`](contrib.qmd), que conté:

- El flux de treball amb Git (branques, commits, Merge Requests).
- Les convencions d'estil (veu, puntuació, negretes, anglicismes, sigles).
- El sistema de callouts i prefixos d'etiquetes.
- Les convencions de figures SVG i blocs de codi.
- Les decisions terminològiques i de format per tema.

## Llicència

Aquest material es publica sota la llicència [Creative Commons Reconeixement-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca).

Podeu copiar-lo, distribuir-lo i adaptar-lo sempre que en reconegueu l'autoria, no en feu un ús comercial i distribuïu les obres derivades sota la mateixa llicència.
