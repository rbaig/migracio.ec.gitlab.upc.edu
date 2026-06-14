# Estructura de Computadors — Apunts

Material escrit de l'assignatura **Estructura de Computadors** (EC), assignatura obligatòria de 7,5 crèdits del segon quadrimestre (Q2) del [Grau en Enginyeria Informàtica](https://www.fib.upc.edu/ca/graus/grau-en-enginyeria-informatica) (GEI) de la [Facultat d'Informàtica de Barcelona](https://www.fib.upc.edu) (FIB), Universitat Politècnica de Catalunya (UPC).

Llengua: **català**. Sortida: **HTML** (web) i **PDF** (imprimible).

Elaborat amb [Quarto](https://quarto.org/) i [Claude](https://claude.ai/) (Anthropic).

## Estructura del projecte

### Teoria (T1–T9)

| Fitxer | Contingut |
| :--- | :--- |
| `Tx.qmd` | Teoria del Tema x (x = 1–9) |
| `PE_Tx.qmd` | Problemes: enunciats del Tema x |
| `PS_Tx.qmd` | Problemes: solucions d'una selecció d'exercicis del Tema x |
| `PS_criteris.qmd` | Criteris de selecció dels problemes resolts |

La correspondència entre els temes d'EC i els PDFs originals (MIPS) **no és 1:1**: la introducció de rendiment, potència i llei d'Amdahl (PDF T1) s'ha segregat al T6; els PDFs T6–T8 corresponen als temes T7–T9.

### Laboratori (L1–L5)

| Fitxer | Contingut |
| :--- | :--- |
| `Ly.qmd` | Laboratori, sessió y (y = 1–5) |

### Fitxers transversals

| Fitxer | Contingut |
| :--- | :--- |
| `_quarto.yml` | Configuració del projecte Quarto |
| `index.qmd` | Pàgina de presentació (avaluació, eines, bibliografia) |
| `riscv.qmd` | Compendi de referència RISC-V (inclòs via `include`) |
| `sigles.md` | Glossari de sigles |
| `bibliografia.bib` | Base de dades bibliogràfica (BibTeX) |
| `contrib.qmd` | Guia de contribució: convencions, estil, flux de treball |
| `CLAUDE.md` | Instruccions operatives per a Claude |
| `TODO.md` | Llista de tasques pendents |
| `_variables.yml` | Variables globals del projecte |
| `custom_dark.scss` | Estils CSS per al mode fosc (HTML) |

### Arbre de directoris

```
EC.qmd/
├── figures/              # Figures SVG (variants light i dark)
├── laboratori/           # Fitxers de suport del laboratori (RARS, startup.s, etc.)
├── referencies/          # Fragments de referència RISC-V (inclosos via `include`)
├── _quarto.yml
├── index.qmd
├── Tx.qmd                # x = 1–9 (teoria)
├── PE_Tx.qmd             # x = 1–9 (enunciats)
├── PS_Tx.qmd             # x = 2–9 (solucions seleccionades)
├── PS_criteris.qmd
├── Ly.qmd                # y = 1–6 (laboratoris)
├── riscv.qmd
├── sigles.md
├── bibliografia.bib
├── contrib.qmd
├── CLAUDE.md
├── TODO.md
├── _variables.yml
└── custom_dark.scss
```

## Renderitzar el projecte

Directori de treball:

```bash
cd ~/git/EC.qmd
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

Sense Chrome instal·lat (p. ex. servidor):

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
