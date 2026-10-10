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
| `L1.qmd`–`L6.qmd` | Laboratori y, Ly (y = 1–6) |

### Fitxers i directoris

Un fitxer o directori de l'arrel per línia. `make comprova` comprova que la llista coincideix amb els fitxers versionats (`13_contrib.qmd §Comprovacions per nivells`).

```
.
├── .claude/                    # Claude Code: hooks, skills i subagents (`13_contrib.qmd §IA`)
├── .github/                    # Workflow de publicació a GitHub Pages
├── .githooks/                  # Hooks de git opcionals: `make instal·la-hooks`
├── .vscode/                    # VS Code: corrector ortogràfic i extensions recomanades
├── 01_apunts/                  # Apunts        (`Ax.qmd`, x ∈ [1, 9])
├── 02_problemes/               # Problemes     (`Px.qmd`, x ∈ [1, 9])
├── 03_solucions/               # Solucions     (`Sx.qmd`, x ∈ [1, 9])
├── 04_laboratori/              # Laboratori    (`Ly.qmd`, y ∈ [1, 6]) i calendari
├── 05_diapositives/            # Reservat (encara sense contingut)
├── 21_riscv/                   # Fragments de taula del compendi RISC-V i dels callouts
├── 22_figs_originals/          # Figures natives (SVG); `conservats/`, les que el llibre ja no consumeix
├── 23_figs_externes/           # Figures d'una font externa
├── 24_specs/                   # Especificacions: figures (`svg.md` i els `.toml`), registre de decisions, arxiu del TODO, glossari, diccionari
├── 25_scripts/                 # Generadors del pre-render, filtres Lua i eines de comprovació
├── _book/                      # Generat · Quarto: directori de sortida
├── auto_figs/                  # Generat · Figures per script (el pre-render l'esborra i el refà)
├── auto_riscv/                 # Generat · Taules fusionades de `11_riscv.qmd` (`make taules`; `make render` ja el crida)
├── .gitignore
├── 10_continguts.qmd           # Pàgina «📑 Continguts»: l'índex dels apunts, només a l'HTML; l'escriu `25_scripts/continguts.lua`
├── 11_riscv.qmd                # Compendi de referència RISC-V
├── 12_sigles_simbols.qmd       # Glossari de sigles, símbols i termes
├── 13_contrib.qmd              # Guia de contribució (capítol «Contribueix-hi»): les regles del llibre i el flux de treball
├── 14_LICENSE.qmd              # Capítol de la llicència i els reconeixements
├── 15_bibliografia.bib         # Base de dades bibliogràfica (BibTeX)
├── CLAUDE.md                   # Instruccions operatives per a les sessions de Claude Code
├── custom_dark.scss            # Estils addicionals del mode fosc (HTML)
├── custom_light.scss           # Estils addicionals del mode clar (HTML)
├── custom.scss                 # Estils comuns als dos modes (HTML)
├── Estructura-de-computadors.tex   # Generat · Font LaTeX del PDF (no versionada)
├── figures_dinamiques.html     # Navegador de passos de les figures dinàmiques (HTML)
├── formules_en_linia.html      # Desplaçament horitzontal de les fórmules en línia que no caben (HTML)
├── ieee.csl                    # Estil de citació IEEE (CSL)
├── index.qmd                   # Pàgina de presentació (avaluació, eines, bibliografia)
├── LICENSE.md                  # Text de la llicència (l'inclou `14_LICENSE.qmd`)
├── Makefile                    # Les ordres del projecte: `make help`
├── preamble.tex                # Preàmbul LaTeX addicional (PDF)
├── _quarto.yml                 # Configuració del projecte Quarto
├── README.md
├── styles.css                  # Estils addicionals (HTML)
├── TODO.md                     # Tasques pendents (contingut transitori)
└── _variables.yml              # Variables globals del projecte (títols de tema, URL, etc.)
```

**Temes.** Un tema `Tx` (T1–T9) és el conjunt dels seus apunts, problemes i solucions, `Ax.qmd`, `Px.qmd` i `Sx.qmd`; és el sentit de «T3» a la guia, al `TODO.md` i al registre de decisions (`13_contrib.qmd §T2 i T3`, per exemple). El laboratori (`Ly.qmd`) es numera per sessions, no per temes.

## Renderitzar el projecte

Directori de treball:

```bash
cd ~/git/EC
```

| Ordre | Efecte |
| :--- | :--- |
| `make render` | Genera les taules fusionades (`auto_riscv/`) i renderitza **només l'HTML** (1–3 min): el bucle diari |
| `make comprova` | Les comprovacions del nivell dels canvis, abans de cada commit (de segons a 8 min) |
| `make comprova-tot` | Totes les comprovacions, amb l'HTML, el PDF i RARS (5–10 min): abans d'obrir una MR o de publicar |
| `make help` | Totes les ordres de `make`, amb el que fa cadascuna |

Els nivells i les comprovacions, a `13_contrib.qmd §Comprovacions per nivells`; quan cal el PDF i com es generen les taules fusionades de `11_riscv.qmd`, a §Verificació de l'entorn, §Renderitzar el projecte i §Fitxer de referència tècnica. `quarto render` també funciona, però sense les taules fusionades i sense el bloqueig que impedeix dos renders alhora al mateix directori.

Neteja:

```bash
make clean
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

### Python (≥ 3.11) i les comprovacions

Les comprovacions de `25_scripts/` fan servir Python 3.11 o posterior i, la de les taules, el paquet fontTools. L'ortografia, opcional, fa servir hunspell amb els diccionaris català i anglès:

```bash
pip install fonttools
sudo apt install hunspell hunspell-ca hunspell-en-us   # Debian i Ubuntu
```

Hooks de git opcionals, que passen les comprovacions abans del commit i del push (`13_contrib.qmd §Comprovacions per nivells`):

```bash
make instal·la-hooks
```

### RARS (simulador RISC-V)

Descarregueu [`rars1_6.jar`](https://github.com/TheThirdOne/rars/releases/download/v1.6/rars1_6.jar) i assegureu-vos de tenir el [Java Runtime Environment (JRE)](https://www.java.com/en/download/help/download_options.html) versió 8.0 o superior. Per a les comprovacions no cal baixar-lo: `25_scripts/verifica_laboratoris.py` el baixa a `~/.cache/ec/` la primera vegada (o fa servir el de la variable d'entorn `RARS_JAR`).

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
