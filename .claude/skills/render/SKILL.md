---
name: render
description: Verificació del render d'EC (HTML i PDF) des d'una sessió de Claude Code. Quan cal `make render-complet`, com esperar un render en segon pla sense que el bucle quedi penjat, com buscar referències trencades al `_book/` i al PDF, com mirar l'HTML en clar i en fosc, i com llegir el registre de LaTeX. Carrega-la abans de llançar un render o de donar per verificat un canvi que en depengui.
---

# Verificació del render

Quin render demana cada canvi ho diuen `13_contrib.qmd §Comprovacions per nivells` i §Verificació de l'entorn, i què fa cada peça del render, `13_contrib.qmd §Renderitzar el projecte`. Aquí hi ha com ho comproves.

## Esperar un render en segon pla

`make render-complet` dura uns quants minuts, i per això se sol llançar en segon pla. Per saber quan acaba, escriu un marcador al registre (`make render-complet > log 2>&1; echo "exit=$?" >> log`) i espera el marcador (`until grep -q '^exit=' log; do sleep 15; done`). No esperis amb `pgrep -f "quarto render"`: el patró també és a la línia d'ordres del bucle mateix, que es troba a si mateix i no acaba mai. Un bucle així va quedar 34 hores en segon pla i bloquejava el `/exit` de Claude Code (detectat el 2026-10-06). Si de debò cal `pgrep`, el patró `"[q]uarto render"` no es troba a si mateix. Abans d'acabar la sessió, comprova que no queda cap bucle en segon pla (`ps --ppid <pid de claude>`).

Dos renders del mateix *worktree* no es fan alhora: el `Makefile` fa esperar el segon (`flock`), i ho diu a la sortida. El hook d'abans del commit renderitza segons el nivell del canvi: al nivell 2, `make render`, que esborra el PDF de `_book/` (`13_contrib.qmd §IA`); per mirar el PDF, cal un `make render-complet` posterior, o `make comprova-tot`.

## Referències trencades

Una escombrada de referències creuades trencades sobre el resultat del render
és la xarxa secundària; la primària és que el render acabi net, sense cap
WARNING, que és el que exigeix `make comprova`. `make comprova-tot` la fa (la
comprovació «Sortida» de `25_scripts/comprova.py`), i hi té en compte les
trampes d'aquí. Si la fas a mà, en té tres (xifres mesurades el 2026-10-07). **Ha de ser recursiva sobre `_book/`**: `_book/*.html` són 5
fitxers de 39 i no inclouen cap capítol de teoria, problemes, solucions ni
laboratori, que viuen en subdirectoris. **Al PDF es busca `?@`, no `??`**: els
13 `??` del PDF són els bytes de farciment indeterminat del bolcat de memòria
amb tipus mixtos d'`S2.qmd`, no referències trencades. I l'única ocurrència de
`?@` que avui apareix al `_book/` és dins d'`anchor.min.js`, JavaScript
minificat que Quarto hi copia: és una classe de caràcters d'una expressió
regular d'AnchorJS, no surt de cap `.qmd`. Fins al 2026-10-07, quan aquest
paràgraf era a `13_contrib.qmd`, en posava dues més —`_book/13_contrib.html` i
`_book/search.json`, perquè hi citava la cadena—; cap no era una referència
trencada.

La part de l'escombrada que mira el PDF demana un `make render-complet`
previ: després d'un `make render` no hi ha cap PDF a `_book/`, de manera que
una cerca sobre el PDF no és que surti neta, és que no té sobre què buscar.
Compte també amb `Estructura-de-computadors.tex`: un `make render` **no**
l'esborra, i per tant el que trobaràs a l'arrel és el de l'últim
`make render-complet`, que pot ser de fa setmanes. No el llegeixis com si fos
d'ara; per tenir-lo al dia, `make render-complet` (o `make clean` primer, si
vols que la seva absència sigui visible).

## L'HTML en clar i en fosc

- Servidor: `python3 -m http.server 8765 --directory _book` (amb `--directory`, continua servint després que un render torni a crear `_book/`). Per `file://`, Quarto no mostra res.
- `google-chrome --headless --screenshot` amb `--virtual-time-budget` o amb una àncora a l'URL dona una pàgina en blanc. Playwright, amb `chromium.launch(executable_path='/usr/bin/google-chrome')` i `new_page(color_scheme='dark'|'light')`, funciona.
- Captura d'un element: `locator(...).screenshot()`; per a un tros de pàgina, `screenshot(full_page=True, clip=...)` amb coordenades de pàgina (`top + scrollY`), no de visor.

## El registre de LaTeX

- Quarto esborra `index.log` i `index.tex` de l'arrel en acabar el render: per als «Overfull \hbox», copia'ls mentre el render corre i queda't la còpia més gran. Les taules, millor amb `python3 25_scripts/verifica_taules.py` (`13_contrib.qmd §Taules`).
- Un «Missing character» és un glif que la font del cos no té: s'hi afegeix la seva línia a `preamble.tex` (`\newunicodechar`, `13_contrib.qmd §Renderitzar el projecte`).
