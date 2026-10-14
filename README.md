# Estructura de Computadors — Apunts

Material escrit de l'assignatura **Estructura de Computadors** (EC), assignatura obligatòria de 7,5 crèdits del segon quadrimestre (Q2) del [Grau en Enginyeria Informàtica](https://www.fib.upc.edu/ca/graus/grau-en-enginyeria-informatica) (GEI) de la [Facultat d'Informàtica de Barcelona](https://www.fib.upc.edu) (FIB), Universitat Politècnica de Catalunya (UPC).

Llengua: **català**. Sortida: **HTML** (web) i **PDF** (imprimible).

Elaborat amb [Quarto](https://quarto.org/) i [Claude](https://claude.ai/) (Anthropic).

## Estructura del projecte

Un fitxer o directori de l'arrel per línia; `make comprova` comprova que la llista coincideix amb els fitxers versionats (`13_contrib.qmd §Registres`).

```
.
├── .cache/                     # Generat · RARS i LanguageTool, baixats pels scripts (no versionat)
├── .claude/                    # Claude Code: hooks, skills i subagents (`13_contrib.qmd §IA`)
├── .github/                    # Workflows de GitHub: publicació i comprovacions de les branques
├── .githooks/                  # Hooks de git opcionals (`make instal·la-hooks`)
├── .vscode/                    # VS Code: corrector ortogràfic i extensions recomanades
├── 01_apunts/                  # Teoria: `Ax.qmd`, tema x (x = 1–9)
├── 02_problemes/               # Enunciats dels problemes: `Px.qmd`
├── 03_solucions/               # Solucions d'una selecció dels problemes: `Sx.qmd`
├── 04_laboratori/              # Laboratori: `Ly.qmd`, sessió y (y = 1–6), i el calendari
├── 05_diapositives/            # Reservat (encara sense contingut)
├── 21_riscv/                   # Fragments de taula del compendi RISC-V i dels callouts
├── 22_figs_originals/          # Figures natives (SVG)
├── 23_figs_externes/           # Figures d'una font externa
├── 24_specs/                   # Especificacions: figures, lèxic, registre de decisions
├── 25_scripts/                 # Generadors del pre-render, filtres Lua i comprovacions
├── _book/                      # Generat · Sortida de Quarto
├── auto_figs/                  # Generat · Figures per script (pre-render)
├── auto_riscv/                 # Generat · Taules fusionades de `11_riscv.qmd`
├── auto_termes/                # Generat · Glossari, sigles i formes, de `24_specs/termes.toml`
├── .gitignore
├── 10_continguts.qmd           # Índex dels apunts (només HTML)
├── 11_riscv.qmd                # Compendi de referència RISC-V
├── 12_sigles_simbols.qmd       # Sigles, símbols, notació i termes
├── 13_contrib.qmd              # Guia de contribució: les regles del llibre
├── 14_LICENSE.qmd              # Llicència i reconeixements
├── 15_bibliografia.bib         # Bibliografia (BibTeX)
├── CLAUDE.md                   # Instruccions de les sessions de Claude Code
├── custom_dark.scss            # Estils del mode fosc (HTML)
├── custom_light.scss           # Estils del mode clar (HTML)
├── custom.scss                 # Estils comuns als dos modes (HTML)
├── Estructura-de-computadors.tex   # Generat · Font LaTeX del PDF
├── figures_dinamiques.html     # Navegador de passos de les figures dinàmiques (HTML)
├── formules_en_linia.html      # Desplaçament de les fórmules en línia que no caben (HTML)
├── ieee.csl                    # Estil de citació IEEE
├── index.qmd                   # Presentació (avaluació, eines, bibliografia)
├── LICENSE.md                  # Text de la llicència
├── Makefile                    # Ordres del projecte (`make help`)
├── preamble.tex                # Preàmbul LaTeX (PDF)
├── _quarto.yml                 # Configuració del projecte Quarto
├── README.md
├── styles.css                  # Estils addicionals (HTML)
├── TODO.md                     # Tasques pendents
└── _variables.yml              # Variables globals (títols de tema, URL…)
```

**Temes.** Un tema `Tx` (T1–T9) és el conjunt dels seus apunts, problemes i solucions, `Ax.qmd`, `Px.qmd` i `Sx.qmd`; és el sentit de «T3» a la guia, al `TODO.md` i al registre de decisions. El laboratori (`Ly.qmd`) es numera per sessions, no per temes. La correspondència entre els temes d'EC i els PDF originals (MIPS) **no és 1:1**: la introducció de rendiment, potència i llei d'Amdahl (PDF T1) s'ha segregat al T6, i els PDF T6–T8 corresponen als temes T7–T9.

## Renderitzar el projecte

Directori de treball:

```bash
cd ~/git/EC
```

| Ordre | Efecte |
| :--- | :--- |
| `make render` | Genera les taules fusionades (`auto_riscv/`) i les taules del lèxic (`auto_termes/`: el glossari de termes i les sigles), i renderitza **només l'HTML** (1–3 min): el bucle diari |
| `make comprova` | Les comprovacions del nivell dels canvis, abans de cada commit (de segons a 8 min) |
| `make comprova-tot` | Totes les comprovacions, amb l'HTML, el PDF i RARS (5–10 min): abans d'obrir una MR o de publicar |
| `make autoproves` | Les autoproves de les comprovacions: cada eina, sobre llibres mínims amb errors coneguts, només amb Python i git (uns segons) |
| `make gramatica` | LanguageTool sobre la prosa del corpus, sense el que al llibre és soroll (`24_specs/gramatica.toml`); també és a `make comprova-tot` |
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

Les comprovacions de `25_scripts/` fan servir Python 3.11 o posterior i, la de les taules, el paquet fontTools i les fonts del PDF (Latin Modern i DejaVu Sans Mono). L'ortografia, opcional, fa servir hunspell amb els diccionaris català i anglès:

```bash
pip install fonttools
sudo apt install hunspell hunspell-ca hunspell-en-us fonts-lmodern fonts-dejavu-core   # Debian i Ubuntu
```

Hooks de git opcionals, que passen les comprovacions abans del commit i del push (`13_contrib.qmd §Comprovacions per nivells`):

```bash
make instal·la-hooks
```

### LanguageTool (gramàtica, opcional)

`make gramatica` passa [LanguageTool](https://languagetool.org/) 6.6 sobre la prosa dels `.qmd`. No cal instal·lar-lo: `25_scripts/gramatica.py` fa servir el de la variable d'entorn `LANGUAGETOOL_DIR`, si n'hi ha cap al sistema, i si no, el baixa la primera vegada al directori `.cache/` del clon (uns 250 MB; uns 400 un cop descomprimit), que git ignora i que comparteixen tots els *worktrees*, i en comprova el sha256. Demana Java 17 o posterior; sense Java, la comprovació surt com a omesa. El que al llibre hi és soroll és a `24_specs/gramatica.toml`, que es manté a mà: una regla que només en fa s'hi desactiva amb el seu perquè, i una forma correcta que marca una regla activa hi va com a excepció.

```bash
make gramatica                                     # el corpus sencer
python3 25_scripts/gramatica.py 01_apunts/A7.qmd   # un fitxer
python3 25_scripts/gramatica.py --tot --resum      # el compte per regla
```

### RARS (simulador RISC-V)

Descarregueu [`rars1_6.jar`](https://github.com/TheThirdOne/rars/releases/download/v1.6/rars1_6.jar) i assegureu-vos de tenir el [Java Runtime Environment (JRE)](https://www.java.com/en/download/help/download_options.html) versió 8.0 o superior. Per a les comprovacions no cal baixar-lo: `25_scripts/verifica_laboratoris.py` fa servir el de la variable d'entorn `RARS_JAR`, si n'hi ha cap, i si no, el baixa la primera vegada a `.cache/`, com LanguageTool.

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
