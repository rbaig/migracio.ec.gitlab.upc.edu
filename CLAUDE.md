# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), amb sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte i fitxers que componen el llibre (`chapters:`).
2. `13_contrib.qmd` — les regles del llibre: contingut, llenguatge (terminologia), format (callouts, codi, figures, SVG), laboratori, decisions per tema i eines.
3. `TODO.md` — tasques pendents i decisions obertes. El seu arxiu, `24_specs/arxiu_todo.md` (les entrades retirades i l'historial), no: s'hi va quan una entrada o el registre hi remeten.

Per a tasques que impliquin figures SVG, llegeix també `24_specs/svg.md` (paleta de colors, mapes de fonts i taula de substitució dark) i `24_specs/registres.toml` (definicions dels registres de bits, font de veritat); la skill `figures` en dona l'ordre de la feina. Abans de proposar de canviar una regla, llegeix-ne el perquè al registre de decisions.

Repartiment de responsabilitats entre fitxers:

- `13_contrib.qmd` (el capítol «Contribueix-hi») és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol regla de format, estil, terminologia o convenció, curta i sense historial.
- `24_specs/registre_de_decisions.md` recull el perquè i l'historial de cada regla, i l'historial de l'estat del projecte. Una regla nova o canviada hi porta la seva entrada, en el mateix commit.
- `.claude/skills/` recull els procediments que només fan servir les sessions de Claude Code: `escombrada`, `render`, `rars` i `figures` (`13_contrib.qmd §IA`).
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació de les sessions de Claude Code. Qualsevol altre aspecte va a `13_contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO.md` només conté contingut transitori. El que ha de quedar buit al final és **el fitxer mateix**: no hi ha de restar cap entrada viva. El que en surt —una entrada que es tanca, o l'historial de les parts ja fetes d'una entrada viva— va **literal** a `24_specs/arxiu_todo.md` ([D-91](24_specs/registre_de_decisions.md#d-91)).

Altres fitxers transversals: `11_riscv.qmd` (compendi de referència RISC-V, inclòs via `{{< include >}}`) i `12_sigles_simbols.qmd` (glossari de sigles i símbols).

## Abast del projecte

L'estructura de directoris i la convenció de noms dels fitxers (`Ax.qmd`, `Px.qmd`, `Sx.qmd`, `Ly.qmd`) són a `README.md §Estructura del projecte`.

Tots els fitxers `.qmd` dels `chapters:` de `_quarto.yml` formen part del projecte, encara que estiguin comentats (es comenten per escurçar el temps de renderització en proves).

Els PDF originals (MIPS) són al directori `/PDF_originals`; consulta'ls en cas de dubte sobre els continguts.

## Estat del projecte

- **Revisió interna: tancada sencera** (declaracions de l'usuari): teoria i laboratori, el 2026-09-23; enunciats i solucions, el 2026-10-01.
- **Revisió externa: en curs.** La fan altres professors de l'assignatura. Abast (declaracions de l'usuari, 2026-10-06): A1–A8, també T3–T6; A9, Px, Sx i Ly en queden fora, de moment; les branques de revisió les crea cada equip. El text literal és al registre de decisions, `§Historial de l'estat del projecte → Revisió externa`, i l'estat de les branques, a `TODO.md §Decisions obertes → Branques del remot`. Les revisions de T3 (`!5`), T4–T6 (`!7`) i T8 (`!8`, fins a §8.7 exclosa) ja són a `main`.
- L'historial de les dues revisions i de les fases fetes del pla és al registre de decisions, `§Historial de l'estat del projecte`.
- El fitxer en curs (WiP) l'indica l'usuari a l'inici de cada xat.

### Regles de la revisió externa

- **Abans de tocar A1–A8, `21_riscv/` o una figura que A1–A8 consumeixi**: `git fetch` i `git ls-remote --heads origin`. Si un equip ja hi té una branca que toca el fitxer, no es toca: se'n registra el pendent i s'avisa l'usuari.
- **Abans de tocar qualsevol fitxer que una branca de revisió també toqui, fes-ne una fusió de prova** (`git merge-tree --write-tree --name-only origin/main origin/<branca>`; `TODO.md §Decisions obertes → Branques del remot`) ([D-64](24_specs/registre_de_decisions.md#d-64)).
- **Finestra de canvis fins al diumenge 2026-10-11** (declaracions de l'usuari: el 2026-10-08, literal, «fins demà a la tarda pots fer canvis a tots els fitxers. Els revisors externs ja s'adaptaran a aquests canvis.»; i el 2026-10-09, literal, «La finestra s'allarga fins a diumenge 11 d'octubre»): fins llavors es pot tocar qualsevol fitxer, A1–A8 inclosos, sense coordinar-ho abans amb els equips ([D-65](24_specs/registre_de_decisions.md#d-65)). La comprovació de les branques dels dos punts anteriors continua.
- **Harmonització abans de la revisió externa**: «preparat per a revisió externa» no vol dir tancat a canvis profunds, especialment els d'harmonització (terminologia, estil, convencions transversals). Tot el que es pugui detectar i corregir abans que la revisió externa arribi a un fitxer s'ha de fer ara, encara que impliqui tocar fitxers ja marcats com a preparats. Als fitxers on la revisió externa ja és en curs —avui, A1–A8 sencer—, un canvi transversal s'ha de coordinar amb els revisors, no aplicar-hi pel davant ([D-65](24_specs/registre_de_decisions.md#d-65)).
- Si detectes una inconsistència que afecta múltiples fitxers (per exemple, terminologia o notació aplicada de manera desigual), proposa'n la correcció sistemàtica encara que surti de l'abast estricte del xat en curs.
- Que una MR es fusioni no vol dir que el revisor doni el tema per tancat. I tancar la revisió d'un tema no tanca el que hi queda registrat: els marcadors del corpus, les figures pendents i les decisions obertes sobreviuen al tancament i es resolen des de les seves entrades del `TODO.md`, sense reobrir cap tema.

### Pla de treball

Cada fase remet a les entrades del `TODO.md`; el detall, les ordres i els ⛔ són allà. **Una sessió nova per fase o per grup de fases**, amb el model de la columna: aquesta taula és la que ho decideix, no el nom de la tasca. Les fases fetes (de la 1 a la 7h, i la 8a; del 2026-10-01 al 2026-10-09), amb la descripció, les decisions i els commits de cadascuna, són al registre de decisions (`§Historial de l'estat del projecte → Fases del pla de treball`); la taula que les llistava amb la sessió i el model de cadascuna, a `git show c29b58d:CLAUDE.md`.

| Fase | Què | Estat | Sessió | Model i effort |
| :---: | :--- | :--- | :--- | :--- |
| 7i | **Suggeriments de la 7g** (`TODO.md §Tasques transversals`): els 86 suggeriments sense proposta d'A9, Px, Sx, Ly i `index.qmd` (els tres desajustos de la guia i del glossari, fets el 2026-10-09). Acceptada per l'usuari el 2026-10-08, a proposta de Claude Code. Fora de la revisió externa. | Pendent | — | Opus, High |
| 8 | **Preparar el material per als equips de revisió d'A1–A8** (l'abast i les branques, a §Estat del projecte). La feina d'aquesta fase és el material, no les branques: una nota per als revisors i l'estat de cada fitxer d'A1–A8. Els equips i el calendari els decideix l'usuari; cada equip crea la seva branca, `revisio/<grup>-t<N>-t<M>` (`13_contrib.qmd §Convenció de noms de branques`). T8 ja és en revisió: `!8`, fusionada el 2026-10-06 fins a §8.7 exclosa. | Pendent | — | — |

Sense fase pròpia, quan hi hagi ocasió i sense bloquejar res: `#cau-boolea-c` (pendent d'un col·lega) i la taula de referències d'`index.qmd` (`TODO.md`). Les eines de les sessions són a `13_contrib.qmd §IA` (skills, subagents i hooks).

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
- **Abans d'esborrar o fusionar una secció, registra'n els pendents *i les declaracions de l'usuari*.** Una declaració («tancat de facto», «quasi tancat», «ho dono per bo») **no es verifica: es registra**. No té commit que la sostingui per construcció —demanar-l'hi és com demanar el commit que demostra una decisió—, de manera que descartar-la per «no verificable» n'esborra l'única còpia. Un fet fals es corregeix; una declaració, només qui la va fer la pot retirar ([D-63](24_specs/registre_de_decisions.md#d-63)).
- Claude Code: pots fer commit i `push` a `origin`, però **només de canvis que l'usuari hagi confirmat explícitament**. Fix-forward sempre: no reescriguis l'historial. L'informe de la feina en curs es publica a cada aturada, perquè la revisió es fa llegint el repositori. El push directe a `main` és el de l'editor (`13_contrib.qmd §Push directe a main`).
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
