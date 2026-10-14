# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), amb sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte i fitxers que componen el llibre (`chapters:`).
2. `13_contrib.qmd` — les regles del llibre: contingut, llenguatge (terminologia), format (callouts, codi, figures, SVG), laboratori, decisions per tema i eines.
3. `TODO.md` — tasques pendents i decisions obertes.

Per a tasques que impliquin figures SVG, llegeix també `24_specs/svg.md` (paleta de colors, mapes de fonts i taula de substitució dark) i `24_specs/registres.toml` (definicions dels registres de bits, font de veritat); la skill `figures` en dona l'ordre de la feina. Abans de proposar de canviar una regla, llegeix-ne el perquè al registre de decisions.

Repartiment de responsabilitats entre fitxers:

- `13_contrib.qmd` (el capítol «Contribueix-hi») és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol regla de format, estil, terminologia o convenció, curta i sense historial.
- `24_specs/registre_de_decisions.md` recull el perquè de cada regla. Una regla nova o canviada hi porta la seva entrada, en el mateix commit. Una entrada que canvia s'edita al lloc, sense paràgrafs «Seguiment del…»: el text d'abans és a git ([D-122](24_specs/registre_de_decisions.md#d-122)).
- `.claude/skills/` recull els procediments que només fan servir les sessions de Claude Code: `escombrada`, `render`, `rars` i `figures` (`13_contrib.qmd §IA`). Cada regla d'una skill porta el cas que la va originar en una línia; el relat sencer és a git.
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació de les sessions de Claude Code. Qualsevol altre aspecte va a `13_contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO.md` només conté contingut transitori. El que ha de quedar buit al final és **el fitxer mateix**: no hi ha de restar cap entrada viva. Una entrada que canvia s'edita al lloc, sense cadenes de procedència ni xifres d'abans; una que es tanca s'esborra, i el commit que la treu en diu el motiu; el text d'abans és a git ([D-122](24_specs/registre_de_decisions.md#d-122)). Abans d'esborrar-la, les declaracions vigents de l'usuari que hi consten passen on siguin vigents (§Flux de treball).

Altres fitxers transversals: `11_riscv.qmd` (compendi de referència RISC-V, inclòs via `{{< include >}}`) i `12_sigles_simbols.qmd` (sigles, símbols, notació i termes; les sigles i els termes es generen de `24_specs/termes.toml`, la font única del lèxic, D-115 i D-118).

## Abast del projecte

L'estructura de directoris i la convenció de noms dels fitxers (`Ax.qmd`, `Px.qmd`, `Sx.qmd`, `Ly.qmd`) són a `README.md §Estructura del projecte`.

Tots els fitxers `.qmd` dels `chapters:` de `_quarto.yml` formen part del projecte, encara que estiguin comentats (es comenten per escurçar el temps de renderització en proves).

Els PDF originals (MIPS) són al directori `/PDF_originals`; consulta'ls en cas de dubte sobre els continguts.

## Estat del projecte

- **Revisió interna: tancada sencera** (declaracions de l'usuari): teoria i laboratori, el 2026-09-23; enunciats i solucions, el 2026-10-01.
- **Revisió externa: en curs.** La fan altres professors de l'assignatura. Abast (declaracions de l'usuari, 2026-10-06): A1–A8, també T3–T6; A9, Px, Sx i Ly en queden fora, de moment; les branques de revisió les crea cada equip. L'estat de les branques és a `TODO.md §Decisions obertes → Branques del remot`. Les revisions de T3 (`!5`), T4–T6 (`!7`) i T8 (`!8`, fins a §8.7 exclosa) ja són a `main`. **Els revisors hi tornen a treballar des del 2026-10-14**: l'usuari els va comunicar aquell dia que podien reprendre la revisió. Des de llavors, un canvi transversal a A1–A8 es coordina amb els equips ([D-65](24_specs/registre_de_decisions.md#d-65)), i les sessions de Claude Code treballen a la branca `operacions` (§Flux de treball, [D-123](24_specs/registre_de_decisions.md#d-123)).
- L'historial de les dues revisions i de les fases fetes del pla és a git ([D-122](24_specs/registre_de_decisions.md#d-122)): fins a la fase 9, a `§Historial de l'estat del projecte` del registre de decisions de l'etiqueta `arxiu/pre-neteja-2026-10-14`; des de la fase 10, als missatges dels commits que les fan (`git log --grep '^Fase'`).
- El fitxer en curs (WiP) l'indica l'usuari a l'inici de cada xat.

### Regles de la revisió externa

- **Abans de tocar A1–A8, `21_riscv/` o una figura que A1–A8 consumeixi**: `git fetch` i `git ls-remote --heads origin`. Si un equip ja hi té una branca que toca el fitxer, no es toca: se'n registra el pendent i s'avisa l'usuari.
- **Abans de tocar qualsevol fitxer que una branca de revisió també toqui, fes-ne una fusió de prova** (`git merge-tree --write-tree --name-only origin/main origin/<branca>`; `TODO.md §Decisions obertes → Branques del remot`) ([D-64](24_specs/registre_de_decisions.md#d-64)).
- **Harmonització abans de la revisió externa**: «preparat per a revisió externa» no vol dir tancat a canvis profunds, especialment els d'harmonització (terminologia, estil, convencions transversals). Tot el que es pugui detectar i corregir abans que la revisió externa arribi a un fitxer s'ha de fer ara, encara que impliqui tocar fitxers ja marcats com a preparats. Als fitxers on la revisió externa ja és en curs —avui, A1–A8 sencer—, un canvi transversal s'ha de coordinar amb els revisors, no aplicar-hi pel davant ([D-65](24_specs/registre_de_decisions.md#d-65)).
- Si detectes una inconsistència que afecta múltiples fitxers (per exemple, terminologia o notació aplicada de manera desigual), proposa'n la correcció sistemàtica encara que surti de l'abast estricte del xat en curs.
- Que una MR es fusioni no vol dir que el revisor doni el tema per tancat. I tancar la revisió d'un tema no tanca el que hi queda registrat: els marcadors del corpus, les figures pendents i les decisions obertes sobreviuen al tancament i es resolen des de les seves entrades del `TODO.md`, sense reobrir cap tema.

### Pla de treball

Cada fase remet a les entrades del `TODO.md`; el detall, les ordres i els ⛔ són allà. **Una sessió nova per fase o per grup de fases**, amb el model de la columna: aquesta taula és la que ho decideix, no el nom de la tasca.

| Fase | Què | Estat | Sessió | Model i effort |
| :---: | :--- | :--- | :--- | :--- |
| 8 | **Preparar el material per als equips de revisió d'A1–A8** (l'abast i les branques, a §Estat del projecte). La feina d'aquesta fase és el material, no les branques: una nota per als revisors i l'estat de cada fitxer d'A1–A8. Els equips i el calendari els decideix l'usuari; cada equip crea la seva branca, `revisio/<grup>-t<N>-t<M>` (`13_contrib.qmd §Convenció de noms de branques`). T8 ja és en revisió: `!8`, fusionada el 2026-10-06 fins a §8.7 exclosa. **Esborrany del material**: `24_specs/revisio_externa.md` (2026-10-12), punt de l'ordre del dia de la reunió del 2 de novembre (`TODO.md §Decisions obertes`). | Esborrany | — | — |

Les eines de les sessions són a `13_contrib.qmd §IA` (skills, subagents i hooks).

## Flux de treball

En començar un xat:

1. Explora el repositori. Si hi ha fitxers als quals no tens accés, demana'ls.
2. Llegeix els fitxers de referència obligatòria (vegeu §Fitxers de referència obligatòria) i la resta de fitxers necessaris per a la tasca.
3. Presenta'm la llista exhaustiva de tasques o problemes que proposes **abans de fer cap canvi**, i digues si cal que canviï el model o l'effort.
4. Espera confirmació per procedir.
5. En cas de dubte, atura't, exposa el dubte i, si pots, proposa solucions. **Una parada sense el motiu escrit és tan dolenta com no aturar-se**: qui la llegeixi ha de poder decidir sense tornar a fer la feina.

Regles operatives:

- Pots fer canvis d'ordre i crear, reanomenar o eliminar seccions, figures, taules, llistes, etc.
- Interromp l'execució només si tens un dubte que hagi de resoldre l'usuari; mostra-li les opcions disponibles.
- **Un commit per bloc d'instruccions**, i push a cada un: el bloc és la unitat que l'usuari ha confirmat i ha de ser la unitat que es pugui revisar i revertir.
- **Numeració de seccions, figures, taules, equacions i callouts: fins a l'inici de les classes (febrer del 2027) no hi ha cap referència externa als números** (declaració de l'usuari, 2026-10-02). Afegir, moure o treure elements numerats és lliure: les referències `@` s'actualitzen soles i cap material de fora del llibre no en depèn. A partir de llavors, qualsevol canvi que renumeri s'ha d'avisar abans de fer-lo. Dins del repositori, un número escrit a mà sí que caduca (la «eq. 6.8» de l'anotació #12 era `#eq-potencia`): se cita l'etiqueta, no el número.
- **Treballa per àncora de contingut, no per número de línia.** Els números que et doni l'usuari són d'una lectura seva i poden haver-se mogut; si l'àncora no hi és o no coincideix amb el que esperaves, atura't en lloc d'aplicar el canvi a on sembli que toca.
- **Abans d'esborrar o fusionar una secció, registra'n els pendents *i les declaracions vigents de l'usuari*.** Una declaració («tancat de facto», «ho dono per bo») **no es verifica: es registra**, en prosa descriptiva, on sigui vigent (aquest fitxer, `13_contrib.qmd`, el registre de decisions o el `TODO.md`). Un fet fals es corregeix; una declaració, només qui la va fer la pot retirar. El que només té valor històric no es conserva: és a git ([D-63](24_specs/registre_de_decisions.md#d-63), [D-122](24_specs/registre_de_decisions.md#d-122)).
- **Claude Code treballa a la branca `operacions`**, no a `main` ([D-123](24_specs/registre_de_decisions.md#d-123)):
    - A l'inici de cada sessió, `git fetch` i `git merge origin/main` a `operacions`.
    - Commit i `push` a `origin/operacions`, però **només de canvis que l'usuari hagi confirmat explícitament**. Fix-forward sempre: no reescriguis l'historial. L'informe de la feina en curs es publica a cada aturada, perquè la revisió es fa llegint el repositori.
    - Quan l'usuari confirma un bloc, `git merge --no-ff operacions` a `main` i `push`: el push a `main` és el de l'editor (`13_contrib.qmd §Push directe a main`).
    - Una segona sessió simultània treballa a `operacions-2` (git no admet alhora `operacions` i `operacions/<x>`), al seu *worktree*.
- **En tancar una fase del pla o una entrada del `TODO.md`**: cada punt té el commit que el fa o la línia actual que ho mostra; el que no es troba no es dona per fet, es pregunta. La fila surt de §Pla de treball, o l'entrada del `TODO.md`, i el missatge del commit en porta el que hi deia: la descripció, les decisions de l'usuari, què s'ha verificat i amb què, i què han de saber els equips de revisió. Només hi van els fitxers del tancament.
- **Al final de cada sessió**: registra els punts que hagin quedat oberts on pertoqui (`TODO.md`, aquest fitxer o el registre de decisions), escriu el missatge d'obertura de la sessió següent i digues-ne el model i l'effort.
- **Sessions en paral·lel al mateix clon: cadascuna al seu *worktree*** (`git worktree add`). Cada *worktree* té el seu `_book/` i el seu `auto_figs/`, i el hook d'abans del commit no hi veu els canvis no confirmats de l'altra sessió. Dins d'un mateix *worktree*, el `Makefile` no deixa fer dos renders alhora: el segon espera ([D-103](24_specs/registre_de_decisions.md#d-103)).
- El mirall de GitHub s'actualitza **automàticament** des de GitLab, amb un parell de minuts de retard. **No s'hi ha d'empènyer a mà** pel remot `mirror`: competiria amb la sincronització. Verificat el 2026-09-21.

## Model i effort

| Tasca | Model | Effort |
| :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet | Normal |
| Solucions (`Sx.qmd`) | Opus | High |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet | Low |
| Neteja de warnings del render | Sonnet | Low–Medium |
| Classificar diferències amb criteri (moltes decisions independents, cadascuna amb el seu veredicte) | Opus | High |
| Aplicar decisions ja preses i escrites (l'experiència de les passades A, B i C mostra que aplicar **no és mecànic**: l'especificació filtra i afloren judicis que ningú no havia previst) | Opus | High |
| Escombrades del corpus amb un discriminador (`git grep` + veredicte cas a cas, inclosos els contraexemples) | Opus | Medium–High |
| Substitucions mecàniques amb el compte ja verificat (l'abast i la xifra ja són comprovats **abans** de començar; només queda substituir) | Sonnet | Low |

- L'**effort** és la palanca del raonament estès: en aquesta versió de Claude Code **no hi ha cap interruptor de *Thinking* a part**.
- El model es tria per si el criteri ja és escrit **i verificat**, no pel nom de la tasca. I qualsevol configuració, en trobar una cosa que l'especificació no cobreix, **s'atura** en lloc de decidir-la.
- Si la tasca canvia, indica-ho explícitament.
- Si vols que et canviï la configuració, digues-m'ho.

## Enllaços

- Figures SVG: política de generació (prioritat, tipus de figures, fonts i colors) a `13_contrib.qmd §Figures i material gràfic`.
- Mirall públic del repositori: https://github.com/rbaig/migracio.ec.gitlab.upc.edu
- Renderització HTML (pot estar desactualitzada): https://rbaig.github.io/migracio.ec.gitlab.upc.edu/
