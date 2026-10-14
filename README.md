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

## Instal·lació

### Accés i editor

- **Git** i accés com a **Developer** al repositori de GitLab, [gitlab.upc.edu/ec/migracio](https://gitlab.upc.edu/ec/migracio) ([cal ser membre del grup `ec`](https://gitlab.upc.edu/groups/ec/)).
- **VS Code**: [code.visualstudio.com](https://code.visualstudio.com/). En obrir el repositori, proposa les extensions recomanades (`.vscode/extensions.json`): [Quarto](https://marketplace.visualstudio.com/items?itemName=quarto.quarto), [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) i [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker), amb el diccionari [català](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-catalan). El corrector llegeix els mots del projecte de `24_specs/diccionari.txt` i `24_specs/diccionari_termes.txt` (`13_contrib.qmd §Referència normativa`).

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

### Comprovació de la instal·lació

```bash
quarto check
```

### Python (≥ 3.11) i les comprovacions

Les comprovacions de `25_scripts/` fan servir Python 3.11 o posterior. La de les taules del PDF fa servir, a més, el paquet fontTools i les fonts del PDF (Latin Modern i DejaVu Sans Mono), i l'ortografia, hunspell amb els diccionaris català i anglès. Totes dues són opcionals: sense, la comprovació surt com a omesa.

```bash
pip install fonttools
sudo apt install hunspell hunspell-ca hunspell-en-us fonts-lmodern fonts-dejavu-core   # Debian i Ubuntu
```

Hooks de git opcionals, que passen les comprovacions abans del commit i del push (`13_contrib.qmd §Hooks de git`):

```bash
make instal·la-hooks
```

### Java, RARS i LanguageTool

RARS demana Java 8 o posterior, i LanguageTool, Java 17 o posterior; sense Java, les comprovacions que els fan servir surten com a omeses. Ni RARS ni LanguageTool no s'instal·len a mà per a les comprovacions: els scripts fan servir el de la variable d'entorn (`RARS_JAR`, `LANGUAGETOOL_DIR`), si n'hi ha cap al sistema, i si no, el baixen la primera vegada al directori `.cache/` del clon, que git ignora i que comparteixen tots els *worktrees*, i en comproven el sha256.

### RARS (simulador RISC-V)

Per treballar el laboratori, descarregueu [`rars1_6.jar`](https://github.com/TheThirdOne/rars/releases/download/v1.6/rars1_6.jar) i assegureu-vos de tenir el [Java Runtime Environment (JRE)](https://www.java.com/en/download/help/download_options.html) versió 8.0 o superior. `25_scripts/verifica_laboratoris.py`, que assembla i executa els blocs `.s` de L1–L6, el baixa sol a `.cache/rars1_6.jar`.

### LanguageTool (gramàtica, opcional)

`make gramatica` passa [LanguageTool](https://languagetool.org/) 6.6 sobre la prosa dels `.qmd`. `25_scripts/gramatica.py` el baixa la primera vegada (uns 250 MB; uns 400 un cop descomprimit). El que al llibre hi és soroll és a `24_specs/gramatica.toml` (`13_contrib.qmd §Comprovacions per nivells`).

```bash
make gramatica                                     # el corpus sencer
python3 25_scripts/gramatica.py 01_apunts/A7.qmd   # un fitxer
python3 25_scripts/gramatica.py --tot --resum      # el compte per regla
```

## Renderitzar el projecte

Des de l'arrel del clon (o d'un *worktree*):

| Ordre | Efecte |
| :--- | :--- |
| `make render` | Genera les taules fusionades (`auto_riscv/`) i les taules del lèxic (`auto_termes/`: el glossari de termes i les sigles), i renderitza **només l'HTML** (1–3 min): el bucle diari |
| `make render-complet` | HTML i PDF (4–8 min) |
| `make comprova` | Les comprovacions del nivell dels canvis, abans de cada commit (de segons a 8 min) |
| `make comprova-tot` | Totes les comprovacions, amb l'HTML, el PDF i RARS (5–10 min): abans d'obrir una MR o de publicar |
| `make autoproves` | Les autoproves de les comprovacions: cada eina, sobre llibres mínims amb errors coneguts, només amb Python i git (uns segons) |
| `make gramatica` | LanguageTool sobre la prosa del corpus; també és a `make comprova-tot` |
| `make clean` | Elimina els artefactes del render (`_book`, `*_files`, els `*.html` de l'arrel que no són versionats, `*.log`, `Estructura-de-computadors.tex`), sense tocar cap fitxer font |
| `make help` | Totes les ordres de `make`, amb el que fa cadascuna |

**`make render` neteja `_book/` i no hi deixa cap PDF**: el que hi hagués d'un render anterior desapareix. És el que volem al bucle diari, que és prosa i referències. Quan cal el PDF —la verificació final abans d'obrir una MR, material per a alumnes, o qualsevol canvi que el toqui—, `make comprova-tot` o `make render-complet`. Un PDF que s'hagi de conservar es guarda fora de `_book/` abans.

`quarto render` (`--to html`, `--to pdf` o les dues sortides) també funciona, però sense les taules fusionades i sense el bloqueig que impedeix dos renders alhora al mateix directori (`13_contrib.qmd §Renderitzar el projecte`). Els nivells i les comprovacions són a `13_contrib.qmd §Comprovacions per nivells`, i quan cal el PDF, a §Verificació de l'entorn.

## Contribució

Vegeu el fitxer [`13_contrib.qmd`](13_contrib.qmd) (el capítol «Contribueix-hi» del llibre), que conté les regles; el perquè de cada una és a [`24_specs/registre_de_decisions.md`](24_specs/registre_de_decisions.md). La guia conté:

- El flux de treball amb Git (branques, commits, Merge Requests).
- Les convencions d'estil (veu, puntuació, negretes, anglicismes, sigles).
- El sistema de callouts i prefixos d'etiquetes.
- Les convencions de figures SVG i blocs de codi.
- Les decisions terminològiques i de format per tema.

## Llicència

Aquest material es publica sota la llicència [Creative Commons Reconeixement-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca).

Podeu copiar-lo, distribuir-lo i adaptar-lo sempre que en reconegueu l'autoria, no en feu un ús comercial i distribuïu les obres derivades sota la mateixa llicència.
