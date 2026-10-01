# TODO

Reescrit el 2026-09-21 (auditoria, sessió 3) a partir d'un inventari complet:
les 58 entrades del `TODO.md` anterior, els 29 marcadors del corpus, els quatre
informes de l'auditoria i els registres de tasques del `TODO/`. Cada
entrada porta la comprovació que la sosté. Les entrades retirades són al
§Entrades retirades del final, amb el motiu i la còpia que en queda.

**42 entrades vives** (recompte del 2026-10-01: es retiren «Passades finals pendents», perquè es tanca tota la revisió interna; «Terminologia anglesa a la prosa d'E/S», que va entrar i es va executar el mateix dia; el criteri global dels quatre formats nuclears, les expressions als operands d'E/S i la grafia de «No-associativitat» i el format de les adreces; entren «Tanques de codi fora de la convenció» i «Veu dels enunciats»; «Ordre substantiu–adjectiu» passa de §Decisions obertes a §Tasques transversals, perquè ja està decidit). Una entrada = una vinyeta de primer nivell (`^- `) per
sobre de `## Entrades retirades`; les vinyetes indentades en són sub-ítems i no
compten. Ordre que ho mesura:

```bash
head -n $(($(grep -n "^## Entrades retirades" TODO.md | cut -d: -f1) - 1)) \
  TODO.md | grep -cE '^- '
```

Repartiment: `§Decisions obertes` 10 · `§Tasques transversals` 11 ·
`§Tasques per tema` 13 · `§Tasques globals` 8 (suma 42, regla 12 bis).
Ordre que el mesura, secció per secció:

```bash
awk '/^## Entrades retirades/{exit} /^## /{s=$0} /^- /{c[s]++} END{for(k in c) print c[k], k}' TODO.md
```

Tres entrades del 2026-09-23 (passades finals pendents, estat parcial de T5,
contradicció de T9) van sortir de la fusió de les dues seccions d'estat de
`CLAUDE.md`: eren pendents que només constaven a la secció eliminada o als
assumptes dels commits, i es van registrar **abans** de treure-la. Avui
**totes tres són files de §Entrades retirades → Executades**: «T5 — revisió
interna tancada», «T9 — contradicció sobre l'estat, i revisió interna tancada»
i, des del 2026-10-01, «Passades finals pendents». També hi són, com a files, les tres que van
sortir el mateix dia de l'auditoria dels 29 ítems del registre de T5 (ítems
4.8, 4.12 i 3.8).

**El directori `TODO/` ja no existeix: aquest fitxer viu a l'arrel des del
2026-09-23.** El sanejament del 2026-09-22 el va deixar com a únic habitant del
directori, i el trasllat n'ha tret el nivell sobrer. El que ha de quedar buit,
doncs, és **el fitxer**, no cap directori: el que falta per arribar-hi és
tancar o reubicar les entrades vives d'aquest `TODO.md` mateix. La comprovació
ja no és un recompte de directori sinó que el `TODO/` no hi torni a ser:

```bash
git ls-files | grep -c "^TODO/"                # 0, el directori ja no existeix
git ls-files TODO.md                           # TODO.md, a l'arrel
```

⚠️ El trasllat va invalidar el pathspec `':!TODO/'` que excloïa aquest fitxer
de les escombrades: sense `TODO/`, deixava d'excloure res i les mesures que el
fitxer publica de si mateix s'haurien inclòs a si mateixes (el compte de
«simple precisió», per exemple, passava de 52 a 56). Les 28 ordres afectades
—26 aquí i 2 a `13_contrib.qmd`— usen ara `':!TODO.md'`, i la regla d'origen és
a `13_contrib.qmd §Escombrades i verificació del corpus`, regla 1.

**Què se n'ha tret, i on és ara** (sanejament del 2026-09-22):

  - **18 registres de tasques caducs, esborrats** (`TODO/T1`–`T9_P_tasques.md`,
    `TODO/L1`–`L6_tasques.md`, `saneja_tasques.md`, `substantiu_adjectiu.md`,
    `12_sigles_simbols__revisio_interna.md`), un cop verificat un per un que la seva
    Fase C era executada o que el pendent viu ja era en aquest fitxer. Es recuperen
    tots amb `git show a211bbf:<ruta>`, que és l'últim commit on existien.
  - **9 prompts de revisió interna, moguts a `26_prompts/`** (`Ax_Ex_Px__…__plantilla.md`,
    `Lx__…__plantilla.md`, `L2`–`L6__revisio_interna*.md`). No es van comptar com a
    transitoris perquè eren plantilles reutilitzables per a la revisió interna.
    **El 2026-10-01 es van esborrar tots nou**, i el directori amb ells: amb la revisió
    interna tancada sencera no queda res on reutilitzar-los (decisió de l'usuari). Es
    recuperen amb `git show 980434b:26_prompts/<fitxer>`.
  - **7 fitxers de `TODO/laboratori/`, esborrats**, amb el seu contingut
    informatiu recollit abans en aquest fitxer: `startup.s` (l'original de RARS)
    s'ha copiat literalment a §Dades preservades, com a segon bloc i amb la taula
    que el compara amb la versió d'A2; els sis `TODO.s` (`L0`–`L5`) eren marcadors
    de **zero bytes** i les seves rutes, que eren tota la informació que
    contenien, són ara al text de l'entrada de renumeració de lliuraments.
    Es recuperen amb `git show 3a3aea6:<ruta>`.

---

## Decisions obertes

Decisions pendents de criteri. Un cop preses, han d'aterrar a `13_contrib.qmd`.

- **Syntax highlighting**: confirmar que `.s` és correcte per a instruccions, macros i directives de RARS.

- **Criteris de codi C: completar.** Dos marcadors vius al corpus ho registren (línies mesurades a `ebdf055`): `A2.qmd:728` (`<!-- TODO hi ha consens? -->`, just abans de `#imp-codi-format-criteris`) pregunta si els criteris de format de codi tenen consens entre professors, i `A2.qmd:729` (`<!-- TODO Miquel: podríem fer un checker -->`) proposa una eina de verificació de format, relacionada amb `25_scripts/verifica_laboratoris.py`, que ja existeix. Els dos marcadors segueixen al corpus fins que la decisió es prengui.

- **Figures portades d'extern: afegir-ne la font.** Dels PDF originals n'hi ha que són del Patterson (p. ex. T7 MC). Abast actual verificat: dues figures de T7 encara es consumeixen en versió `__extern_` (export de PDF, no nativa) — `A7.qmd:365,368,372` (`T7_assoc_conjunts_diagrama__extern_*`) i `A7.qmd:303,306,310` (`T7_cd_diagrama__extern_*`). Enllaça amb `§Contingut global → Figures externes (llicències)`.

- **R4-TYPE a T5** (`A5.qmd:5`, `<!-- TODO: cal introduir el R4-TYPE? (Harris) -->`): decisió d'abast de contingut. Rellevant perquè `24_specs/registres.toml` ja genera la figura `T5_instruccio_tipus_R4`, avui sense ús. El marcador és a la capçalera del fitxer, abans del `# {{< var tema5 >}}`, fora de cap secció.

  ⛔ **A4, A5 i A6 en queden fora** fins que el grup de treball hagi fusionat `temes456` (revisió externa en curs: vegeu §Decisions obertes → Branques del remot).

- **R5-TYPE (RISC-V *compressed*) com a aprofundiment** (`A5.qmd:6`): decisió d'abast que **creua dos temes** — el marcador pregunta si aniria al principi de T2. Mateixa ubicació que l'anterior.

  ⛔ **A4, A5 i A6 en queden fora** fins que el grup de treball hagi fusionat `temes456` (revisió externa en curs: vegeu §Decisions obertes → Branques del remot).

- **Figures de half-adder i full-adder (T4)** (`A4.qmd:80`, `:81`): dos marcadors consecutius dins de `#wrn-sobreeiximent-maquinari`. El primer és una **tasca** (afegir la figura d'un *half-adder* i la d'un *full-adder*); el segon és una **decisió**, pel signe d'interrogació: si cal la figura de la seqüència de *full-adders* amb la porta XOR per detectar el sobreeiximent en el darrer. Si es creen, SVG natiu segons `24_specs/svg.md`.

  ⛔ **A4, A5 i A6 en queden fora** fins que el grup de treball hagi fusionat `temes456` (revisió externa en curs: vegeu §Decisions obertes → Branques del remot).

- **Taules de memòria de T2 → figura estàndard** (`A2.qmd:964`, `:1002`, mesurat a `ebdf055`): dos marcadors amb la mateixa tasca sobre dues taules diferents — la segona és dins de `#tip-endianness` i afecta `#fig-big-endian`/`#fig-little-endian`. Pendent de figura, no de decisió, però no hi ha secció de figures de T2 en aquest fitxer: hi entra aquí fins que se'n creï una.

- **Unificar el format de les taules de pseudoinstruccions** (`A2.qmd:620`, `:645`, mesurat a `ebdf055`): dos marcadors amb text literal idèntic (`<!-- TODO Roger unificar format taules pseudoinstruccions -->`), el primer dins de `#nte-pseudoinstruccio-la` i el segon dins de `#imp-ec-la-offset`. Nota de progrés adreçada a una persona: o es fa la unificació i s'esborren, o es resolen des d'aquí. No poden quedar-se al corpus indefinidament.

- **Marcadors de codi deliberadament incorrecte sense categoria a `13_contrib.qmd`.** Els marcadors `⚠️ codi_erroni__*.c ⚠️` i `⚠️codi_erroni__*.s⚠️` no són ni llenguatge ni context: són una marca semàntica de «codi deliberadament incorrecte», i la taula de `13_contrib.qmd §Blocs de codi` no en preveu la categoria. Cal decidir si mereixen fila pròpia. Ús actual verificat (2026-09-24; línies re-mesurades a `ebdf055`): **4 blocs**, tots a `A2.qmd` — `:436` `⚠️codi_erroni__nom_reservat.s⚠️`, `:832` `codi_erroni__gcc_tipus.c`, `:1080` `⚠️codi_erroni__alineacio_incorrecte.s⚠️`, `:1806` `⚠️ codi_erroni__vectors.c ⚠️`; `grep -n "codi_erroni\|deliberadament incorrecte" 13_contrib.qmd` → cap fila. *(Detectat a la passada C; registrat aquí perquè l'informe que el contenia és transitori.)*

  ```bash
  git grep -n 'filename="[^"]*codi_erroni' -- '*.qmd' ':!TODO.md' | wc -l   # 4
  ```

  ⚠️ Les tres línies que aquesta entrada publicava abans (`:794`, `:1042`, `:1770`) **eren correctes quan es van escriure** —es comprova amb `git show 7e415a4:01_apunts/A2.qmd`— i han caducat perquè `A2.qmd` ha crescut. És la regla 11: una xifra només és certa respecte del commit on es va mesurar. Per això les d'ara van datades.

  📌 **Argument nou a favor de la fila pròpia (2026-09-24): el marcador també serveix per excloure el bloc de les escombrades del corpus.** El quart bloc és el contraexemple d'`@nte-rars-noms-reservats`, que conté a posta un `.eqv B, 16` amb un nom reservat. Sense marca, una escombrada d'identificadors el compta com a **xoc real** (17 símbols `.eqv`, amb `B` a `A2.qmd:437`, mesurat a `ebdf055`) i, per la regla d'aturada, obliga a parar-se a decidir si ho és — a l'exemple escrit precisament per ensenyar el xoc. Amb la marca al `filename`, l'exclusió es pot fer **per forma** (`codi_erroni` a la tanca) i no amb una llista de línies que caduca: el compte torna a 16 i a zero xocs. Un marcador que és alhora senyal per al lector i predicat per a les eines és un argument que no es veia amb els tres blocs anteriors, cap dels quals no conté identificadors que cap escombrada miri.

  Avui no trenca res: `25_scripts/verifica_laboratoris.py` només processa `04_laboratori/L*.qmd` (`LAB_DIR` + `L*.qmd`, `:24` i `:279`, mesurat a `ebdf055`), de manera que `A2.qmd` li queda fora d'abast. El risc apareix el dia que l'abast creixi o que algú escombri identificadors a tot el corpus.

- **Branques del remot: la revisió externa és en curs a `temes456` (T4–T6, MR `!7`) i a `contingut/t3-traduccio` (T3, MR `!5`)** (registrada 2026-09-23; T3 i les MR, 2026-10-01). Les branques es registren, **no es toquen**: cap fusió, cap esborrat, i les fusions les farà el grup de treball.

  ```bash
  git ls-remote --heads origin           # GitLab: la font de veritat
  git ls-remote --heads mirror           # GitHub: el mirall, hi ha `build` de més
  for b in contingut/t3-traduccio temes456; do
    echo "$b: $(git rev-list --count origin/$b..origin/main) darrere, \
  $(git rev-list --count origin/main..origin/$b) propis"
    git diff --stat origin/main...origin/$b | tail -1
  done
  ```

  | Branca | Remot | Darrere | Propis | Abast |
  | :--- | :--- | ---: | ---: | :--- |
  | `contingut/t3-traduccio` | tots dos | 163 | 1 | 4 fitxers, +61/−48 |
  | `temes456` | tots dos | 118 | **11** | 6 fitxers, **+243/−225** |
  | `build` | **només el mirall** | — | 1 | sortida de CI, vegeu més avall |

  **`temes456` és la revisió externa de T4, T5 i T6, i és l'etapa que segueix la interna, no una de paral·lela.** Onze commits sobre `A4.qmd`, `A5.qmd` i `A6.qmd` (+243/−225), del **21 de juliol al 7 d'agost**; la revisió interna dels tres temes es va acabar just abans, el **12–13 de juliol** (`77853ff` T6, `b81e3fa` T5, `9faab05` T4). La declaració de tancament de la interna (2026-09-23, `2f18e1a`, `4c37084`, `6846dff`) n'és la **condició prèvia**, no una contradicció.

  La signen **tres col·legues**: Rubén Tous (4 commits; hi surten com a `FIRST_NAME LAST_NAME` perquè té el `user.name` sense configurar, però el correu és el seu), Fernando Agraz (4) i Pedro J. Martinez-Ferrer (3).

  **El que la fusió haurà de resoldre.** Des del punt de separació (`0e715c2`, 2026-07-20), el que `main` ha mogut de cada fitxer:

  | Fitxer | Commits a `main` | Conseqüència |
  | :--- | ---: | :--- |
  | `A6.qmd` | **0** | **Fusió neta** |
  | `A5.qmd` | 1 | `4accc6c`, mecànic («de menor pes» → «de menys pes») |
  | `A4.qmd` | **5** | Dos amb canvis de contingut: `1f8132a` (callout de pas de matriu per referència) i `45f6cc2` (expressions als operands) |

  ```bash
  git log --oneline 0e715c2..origin/main -- 01_apunts/A4.qmd   # 5
  git log --oneline 0e715c2..origin/main -- 01_apunts/A5.qmd   # 1
  git log --oneline 0e715c2..origin/main -- 01_apunts/A6.qmd   # cap
  ```

  📌 **Fusió de prova (2026-10-01, sobre `980434b`): tres conflictes, no un.** L'ordre no toca l'arbre de treball ni l'índex:

  ```bash
  git fetch origin
  git merge-tree --write-tree --name-only origin/main origin/temes456   # .gitignore, A4.qmd, A5.qmd
  ```

  | Fitxer | Conflictes | Què xoca |
  | :--- | ---: | :--- |
  | `A4.qmd` | 1 | Previst a la taula de dalt |
  | `A5.qmd` | 2 | **No previst**: el commit de `main` que la taula qualifica de mecànic (`4accc6c`) i la branca reescriuen les mateixes dues línies, la definició d'ULP i la del mode d'arrodoniment RNE. Mecànic no vol dir que no xoqui |
  | `.gitignore` | 1 | **El va introduir `980434b` (2026-09-25)**: `!preamble.tex` cau just al costat del `.DS_Store` que hi afegeix la branca. Es resol conservant totes dues línies |

  El del `.gitignore` és una errada de procés: el commit es va fer sense comprovar contra la branca un fitxer que aquesta entrada ja deia que la branca tocava. D'aquí ve l'avís de `CLAUDE.md §Prioritats de la revisió`: abans de tocar un fitxer que una branca de revisió també toca, cal fer-ne la fusió de prova.

  ⚠️ **La branca toca dues fonts de veritat**, no només prosa: `24_specs/registres.toml` i `22_figs_originals/T5_ieee754_format_registre.svg` — els dos fitxers que l'entrada «Ordre substantiu–adjectiu» d'aquesta mateixa secció identifica com a font de la figura de T5. Conciliar-los vol dir **regenerar**, no només fusionar. També toca `.gitignore` (3 línies).

  `contingut/t3-traduccio` (un commit, `62700c0`, 2026-07-06, Pedro J. Martinez-Ferrer) porta **rutes d'abans del refactor de directoris** (`c5d9416`): `01_T/T3.qmd` i `11_riscv/…`, camins que avui no existeixen. **Qualsevol fusió és manual**, perquè git no pot resseguir el canvi de nom a través del refactor.

  ⚠️ **És la revisió externa de T3, amb MR oberta: `!5`, «T3: revisió del tema (canvis i comentaris)», oberta el 2026-07-06 i sense cap comentari a GitLab.** Fins al 2026-10-01 aquesta entrada la registrava com a branca però no com a revisió, i `CLAUDE.md` deia que, fora de T4–T6, la revisió externa «encara no ha començat». Ho va treure a la llum `glab`, no `git`: una branca no diu si té una MR al darrere. **Decisió de l'usuari (2026-10-01): el port a les rutes actuals (`01_apunts/A3.qmd`, `21_riscv/`) el fa l'autor de la MR.** Fins llavors `A3.qmd` no es toca, perquè cada canvi que hi entri és un conflicte més per al port.

  ```bash
  glab api 'projects/7916/merge_requests?state=opened' | jq -r '.[] | "!\(.iid) \(.source_branch) · \(.author.name) · \(.title)"'
  # !7 temes456 · pedro.martinez.ferrer · Revisió del temes 4,5 i 6
  # !5 contingut/t3-traduccio · pedro.martinez.ferrer · T3: revisió del tema (canvis i comentaris)
  ```

  📌 **`build` existeix només al mirall de GitHub, i no s'ha de tocar.** No és a `origin` (GitLab). El seu únic commit és `6d5d2cf` (2026-09-19), d'autor `github-actions[bot]` i assumpte «Render de 38f0ebc»: és **sortida de CI generada a GitHub**, que per això no arriba a GitLab —i el `38f0ebc` que cita no resol en aquest clon, per la mateixa raó—. El `publish.yml` actual ja no l'escriu: desplega amb `upload-pages-artifact` i `deploy-pages` (`:81`, `:94`). No és residu del `d4086cd` de juliol ni feina de ningú.

  ⚠️ **Mesureu les branques amb `git ls-remote`, i digueu de quin remot parleu** (regla 13 de `13_contrib.qmd §Escombrades i verificació del corpus`). En registrar aquesta entrada, `git branch -r` va fer declarar `build` inexistent —ho és a GitLab, no al mirall— i va fer registrar `T3-review-adria` i `to-trash` com a existents, quan eren **referències de seguiment obsoletes** d'aquest clon: ja no són a cap dels dos remots, i `git fetch mirror --prune` les ha tretes.
---

## Tasques transversals

- **Exercicis → Problemes: l'etiqueta visible.** El llibre etiqueta els enunciats com a «Exercici 11.1», «Exercici 11.10»… (el prefix per defecte de Quarto per a `#exr-`, que `_quarto.yml §language` no redefineix), mentre que la part del llibre es diu «Problemes». **Cal decidir** si l'etiqueta passa a «Problema» (`crossref-exr-prefix` i `callout`/`title` corresponents) i, si escau, la de les solucions. És la part «callout header» del títol original d'aquesta entrada.

  ✅ **La part dels identificadors és feta (2026-10-01)**, per decisió de l'usuari: `p<N>-` → `t<N>-`, amb el número del tema del fitxer. **503 substitucions** en 22 fitxers, que són totes les ocurrències del prefix antic: 498 als `.qmd` (la xifra que publicava l'entrada) i 5 a `TODO.md` i `CLAUDE.md`. No hi ha hagut cap col·lisió: les 296 definicions mapen a 296 identificadors nous diferents, i cada parella `exr`/`sol` és al mateix tema. Les 201 referències `@` resolen, i el render HTML no dona cap referència sense resoldre. La convenció és a `13_contrib.qmd §Problemari i solucionari`. El text anterior de l'entrada, amb la taula de prefixos per tema: `git show 7d78615:TODO.md`.

  ```bash
  git grep -c -E "(exr|sol)-p[0-9]+-" -- . ':!TODO.md'      # cap
  git grep -o -E "\{#(exr|sol)-t[0-9]+-" -- '*.qmd' | wc -l   # 296 definicions
  ```

  ⚠️ Els enllaços externs a les àncores publicades amb el prefix antic (`…/E2.html#exr-p3-…`) van deixar de funcionar.

- **`S_criteris_seleccio.qmd` — taula de T1 incompleta** (auditoria, sessió 2, 2026-09-21). La taula de `## {{< var tema1 >}}` té **una sola fila** (`@exr-t1-enters-taules`, `:23`) i ha de recollir la resta de problemes seleccionats de `S1.qmd`. El marcador «TODO» que ho registrava era contingut destinat a l'alumne i es va substituir per la nota neutra de `:19` («*Taula provisional: recull els problemes de `S1.qmd` seleccionats fins ara.*»); **aquesta entrada és ara l'únic registre de la tasca**. El fitxer és comentat a `_quarto.yml:95`, de manera que avui no es renderitza.

- **`L2.qmd:153-166` — alineació de `.dword` a RARS** (marcador `<!-- TODO Alineació de `long long` a RARS` a `:153`, mesurat a `ebdf055`) (registrat 2026-09-20; **no tocat** per la sessió 2, que el va declarar decisió viva). RARS alinea `.dword` a 4 bytes (no a 8, com fan GCC/MARS) i el solucionari presenta **les dues versions alhora**. Decisió pedagògica pendent: mantenir les dues, quedar-se només amb la de RARS (que és la que l'alumne observarà al laboratori), o explicitar millor per què se'n donen dues.

  ⚠️ **Del bolcat comparatiu MARS/RARS (`L2.qmd:163-164`, mesurat a `ebdf055`), només la fila MARS (`:163`) no existeix enlloc més del corpus.** La fila RARS (`:164`) coincideix paraula per paraula amb el bolcat de la solució (`:306`). Si en resoldre la decisió s'elimina el comentari, la fila MARS s'ha de preservar aquí abans, com es va fer amb el bolcat d'`A2.qmd` a la sessió 2. Ordres que ho sostenen (cadascuna discrimina una fila; l'anterior, `git grep -n "fea800fb"`, en donava 4 sense distingir-les):

  ```bash
  git grep -nE "0xfea800fb +0x00000000" -- . ':!TODO.md'      # només L2.qmd:163 (MARS)
  git grep -nE "0xfea800fb +0xfffffffd +0xffffffff +0x000000a0 +0x000016a7 +0x0000ffff +0x00000000 +0x00000000" \
    -- . ':!TODO.md'                                           # L2.qmd:164 (RARS) i :306 (solució)
  ```

- **Discrepància de noms a la figura Graphviz de T7** (detectada 2026-09-20): el fitxer font és `24_specs/T7_mc_politiques__graphviz.gv` i el SVG derivat és `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` — arrels diferents, el `_resum` només és al SVG. Documentat com a discrepància coneguda a `13_contrib.qmd §Figures Graphviz` perquè ningú no «l'arregli» pel cantó dolent. **Via de resolució**: renombrar el `.gv` a `T7_mc_politiques_resum__graphviz.gv` és **inofensiu** (cap script ni cap `.qmd` no el referencia: el `dot` s'executa a mà i el pre-render parteix del SVG ja generat). Renombrar el SVG, en canvi, **trencaria** les tres línies d'`A7.qmd` (646, 649, 653, mesurat a `ebdf055`) que consumeixen `auto_figs/T7_mc_politiques_resum__graphviz__original_{light,dark}.svg`.

- **Revisió sistemàtica del corpus per nodrir les taules de `Símbols` i `Notació` de `12_sigles_simbols.qmd`.** Abast concret verificat, que fins ara no constava: la revisió creuada de T7/T8 va deixar **sense verificar la major part de la taula actual** — tots els símbols exclusius de T1–T6 i T9 que no s'hagin creuat casualment amb T7/T8. Sospitosos prioritaris per la seva similitud notacional (font típica de confusió símbol↔concepte): $CPI$/$CPI_i$/$C_i$, $f_B$/$f_{clock}$, $K$, $m$/$m_d$/$m_i$/$m_{L1}$/$m_{L2}$, $P$/$P_d$/$P_s$/$P_x$, $s_{max}$/$s_x$, $V_{CC}$/$V_{in}$/$V_t$ — **tots de T6, tema no verificat en cap xat anterior**. Cobertura actual de la taula `## Símbols`, per tema: T1 6, T2 2, T3 3, T4 20, T5 17, T6 28, T7 39, T8 9, **T9 cap**. *(Origen: `TODO/12_sigles_simbols__revisio_interna.md:147`, fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/12_sigles_simbols__revisio_interna.md`.)*

  Hi encaixa també: **`NF`, `NC`, $T$ (mida d'element) i *stride*** apareixen en fórmules de T4 i L4 i **no tenen entrada** al glossari (`git grep -n "NF\|stride" -- 12_sigles_simbols.qmd` → cap). *(Origen: `TODO/L4_tasques.md` D4, fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/L4_tasques.md`.)*

- **Revisió sistemàtica del corpus per l'aplicació de la regla d'ús `AND`, `OR`, `XOR`, `NOT`--`barra superior`** (enters).

- **Cometes `"..."` → `«...»`: només queda `A4.qmd:122`** («s'ha "donat la volta"»), que espera la fusió de `temes456`. La resta és feta (2026-10-01): **sis línies de prosa** convertides, totes a `A2.qmd` (`:918`, `:1482`, `:1506`, `:1508`, `:1587`, `:1596`, mesurades abans del canvi). El text sencer de l'entrada anterior, amb la història de la xifra: `git show 06df489:TODO.md`.

  Ordre, amb A3–A6 exclosos (regla 12: `13_contrib.qmd` en queda fora perquè hi ha cites, no prosa del llibre):

  ```bash
  git grep -nP '(?<![-\w=])"[^"]*\p{L}[^"]*"' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' \
    ':!01_apunts/A3.qmd' ':!01_apunts/A4.qmd' ':!01_apunts/A5.qmd' ':!01_apunts/A6.qmd' \
    | grep -vP '\w+="' | wc -l      # 54 a 06df489, 49 després: tot codi, YAML o comentari HTML
  git grep -c "“" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'   # cap
  ```

  Les **49 que queden no són feina**: codi C i pseudocodi, directives (`.asciz "…"`), missatges de RARS i de GCC dins de `` ` ``, el YAML d'`index.qmd` i comentaris HTML que no es renderitzen (les especificacions de figures d'`A7` i `A8`, la nota de `L1.qmd:8`). **Els comentaris dins dels blocs de codi es deixen com són**: `13_contrib.qmd` no en diu res, i la regla de §Commits parla de prosa.

  ⚠️ **Tres correccions a l'entrada anterior**, que la mesura d'avui no reprodueix:

  - **`A2.qmd:1796-1797` no eren prosa**, sinó comentaris C dins d'un bloc `{.c}` (`/* Tipus: "vector de 100 enters" */`). Per la regla de dalt, es deixen.
  - **`A2.qmd:918` no hi era**: té `“camps”`, amb cometes tipogràfiques, i el patró només buscava `"`. És la regla 4 (cobrir totes les formes): ara `25_scripts/lint_prosa.py` també les detecta.
  - **El repartiment d'A3–A6 («1 a A4, 3 a A5 i 1 a A6») no reprodueix a cap commit**. A `bb64329`, a `ebdf055` i avui dona A3 3, A4 1, A5 1, A6 0, i d'aquestes cinc línies **només `A4.qmd:122` és prosa**: `A3.qmd:244` i `A5.qmd:6` són marcadors en comentari HTML, i `A3.qmd:1249-1250` és codi C. El total d'`A2`, que l'entrada donava com a 17, ja era **19** a `ebdf055`.

- **Ordre substantiu–adjectiu: «precisió simple/doble» al material de T5.** **Decidit i aplicat fora de T5 el 2026-10-01** (decisió de l'usuari): l'adjectiu classificador va darrere del nom, i la regla, amb les excepcions, és a `13_contrib.qmd §Criteris generals`. Fora de T5 s'han canviat 6 calcs de precisió (`A2.qmd:79`, `S_criteris_seleccio.qmd:81`, `12_sigles_simbols.qmd:135`, `:139`, `:197`, `RARS_directives.qmd:6`) i 5 de «el/la següent X» (`A1.qmd:264`, `:377`; `A2.qmd:1759`, `:1766`; `RARS_directives.qmd:1`). Línies mesurades a `bb12c2b`; el text anterior de l'entrada: `git show bb12c2b:TODO.md`.

  **Queda el material de T5, que es canvia en coordinació amb el grup de treball de `temes456`** (decisió de l'usuari): A5 és a la branca, i canviar-ne els E, els S i les figures abans faria que el tema digués una cosa a la teoria i una altra als problemes. **56 ocurrències**:

  ```bash
  25_scripts/escombrada.sh '(simple|doble) precisió' -- 01_apunts/A5.qmd 02_exercicis/E5.qmd \
    03_solucions/S5.qmd 04_laboratori/L5.qmd 22_figs_originals 24_specs
  # A5 21 · S5 10 · L5 8 · E5 8 · registres.toml 2 · SVG de T5 7 (3 en esborranys __org)
  ```

  Fora d'aquests fitxers, la mateixa forma ja no surt enlloc: `git grep -n -i -E "(simple|doble) precisió" -- . ':!TODO.md' ':!13_contrib.qmd'` amb aquests fitxers exclosos → cap.

  ⚠️ **Dues trampes que l'execució ha d'evitar, totes dues comprovades:**

  **1. L'escombrada ha de ser insensible a majúscules** (`-i`). Sis ocurrències són capitalitzades perquè encapçalen columna o paràgraf, i un patró en minúscules se les deixa totes:

  ```bash
  git grep -n "Simple precisió\|Doble precisió" -- . ':!TODO.md'
  # A5.qmd:63 (dues, capçaleres de columna) · S5.qmd:296, :309, :338, :351
  ```

  **2. L'abast no és només de prosa**: a T5, 9 ocurrències són fora dels `.qmd`, en sis fitxers. **Abans de tocar-ne cap cal saber quin és font i quin és generat**, perquè el tractament és oposat:

  | Fitxer | Naturalesa | Com s'hi canvia el text |
  | :--- | :--- | :--- |
  | `24_specs/registres.toml` (`:133`, `:136`) | **Font de veritat** (`CLAUDE.md §Fitxers de referència obligatòria`) | Editar-hi el `title` i **regenerar**: `gen_regs.py` produeix `auto_figs/T5_ieee754_format_registre__registre_{light,dark}.svg`, que és el que `A5.qmd:87,90,94` consumeix |
  | `22_figs_originals/T5_ieee754_format_registre.svg` | Font versionada, però **el corpus no en consumeix la variant `__original_`** | Comprovar si encara cal: hi ha **dues còpies del mateix text**, la del `.toml` i la d'aquest SVG |
  | `T5_recta_global.svg`, `T5_recta_zoom_zero.svg` | **Fonts natives** (`A5.qmd:268-275` i `:381-388` en consumeixen la variant `__original_`) | Editar l'SVG directament |
  | `T5_recta_global__org.svg`, `T5_recta_zoom_zero__org.svg` | **Esborranys versionats**, no referenciats per cap `.qmd`, `.yml` ni `.toml` | Decidir si es mantenen abans de perdre-hi temps |

  📌 **La lliçó, germana de la que ja teníem.** Fins ara la regla escrita deia que *un grep massa literal fabrica discrepàncies que no existeixen*. Aquesta entrada mostra l'altra cara: **també se'n deixa de reals**, i aquí ho va fer per les dues bandes alhora — un compte era sensible a majúscules i perdia sis capçaleres; l'altre mirava només els `.qmd` i perdia les nou de les figures. La forma completa de la regla: **el patró ha de cobrir totes les formes del que es mesura (majúscules incloses) i tots els tipus de fitxer on pot viure, no només els que es tenen al cap.**

  ⛔ **A5 i `24_specs/registres.toml` són a `temes456`**: no es toquen fins a la fusió (vegeu §Decisions obertes → Branques del remot).

- **Veu dels enunciats: 99 imperatius en singular a E1, E2, E3 i E9** (detectada 2026-10-01, en el bloc de terminologia d'E/S). `13_contrib.qmd §Problemari i solucionari` fixa la **2a persona del plural** per als enunciats («Traduïu», «Calculeu»), «aplicat sistemàticament a E6 i E4». Els altres temes no la segueixen:

  ```bash
  25_scripts/escombrada.sh --cas -w '(Tradueix|Escriu|Calcula|Indica|Determina|Contesta|Explica|Raona|Dibuixa|Completa|Justifica|Suposa|Considera|Codifica|Converteix|Implementa|Omple|Digues|Dona)' -- 02_exercicis
  # E3 40 · E2 37 · E9 13 · E1 9 → 99 (mesurat a 9dc02f6)
  ```

  S'ha de revisar cas a cas: la llista de verbs és la que s'ha trobat, no la completa, i a l'inici de frase «Considera» o «Indica» poden ser una 3a persona i no un imperatiu. Cal mirar també els **solucionaris**, que reprenen la veu de l'enunciat. `E3.qmd` es va donar per completat al juliol amb la veu en singular, de manera que la divergència no és d'un fitxer endarrerit, sinó d'una regla que no s'ha escombrat mai.

- **Tanques de codi fora de la convenció** (detectada 2026-10-01, en escombrar les expressions als operands). `13_contrib.qmd §Blocs de codi` fixa la tanca de cada llenguatge amb `filename`: `{.c filename="C"}`, `{.s filename="RV32I"}` (o `RV32IM`, `RV32IF`, `RV32IZicsr`, o el nom del fitxer `.s`). Mesurat a `b2530c7`, **39 tanques nues** no la segueixen:

  ```bash
  git grep -c -E '^\s*[`]{3}c\s*$' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'   # E4 28, E5 3, A7 2
  git grep -c -E '^\s*[`]{3}s\s*$' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'   # E4 6
  ```

  **No és només estètica**: una tanca nua perd l'etiqueta `filename` que veu l'alumne (`C`, `RV32I`) i fa invisible el bloc a les escombrades que filtren per `{.s` o `{.c`. Una de les d'E4 va fer que la primera escombrada d'expressions als operands comptés 32 línies en lloc de 34. Per a cada ` ```s ` cal triar el `filename` segons les instruccions del bloc: `RV32IM` si hi ha `mul` o `div`, i `RV32I` si no.

  A banda d'aquestes, n'hi ha que s'han de mirar una per una, perquè poden ser legítimes: **24 tanques sense cap llenguatge** (`L5` 8, `A1` 7, `A2` 5, `A3` 3, `E4` 1), que poden ser sortida de programa; **3 `{.default}` sense `filename`** (`A4`, `A5`, `L2`); i dues formes que la taula no recull, `{.cpp filename="C++"}` (`A1`, un exemple de C++) i `{.code filename="Abocament de memòria"}` (`A2`).

  ⛔ **A3–A6 en queden fora** (`temes456` i la MR `!5`). La resta d'aquestes tanques no són a cap branca de revisió.

- **Nova eina disponible: retalls (crops) SVG a partir d'una figura font única** (afegida 2026-07-13, revisió interna T5): `25_scripts/gen_crops.py` + `24_specs/retalls.toml`, integrat al `pre-render` de `_quarto.yml` entre `gen_regs.py` i `gen_dark.py`. Permet definir una figura «detall»/«zoom» com una finestra `(x, y, w, h)` sobre el `viewBox` d'una figura font ja existent, sense duplicar-ne el contingut. Documentat a `13_contrib.qmd §Retalls`. Aplicable només quan el detall és un subconjunt geomètric net de la font (cap connector/etiqueta tallat a mig camí).

  **Cap ús real encara**: `24_specs/retalls.toml` té 23 línies, **totes comentari**, i cap retall definit. S'ha valorat dues vegades per a les figures de T5 i descartat totes dues: (1) `T5_recta_zoom_zero` com a retall de `T5_recta_global` — `T5_recta_zoom_zero` mostra informació pròpia dels denormals (hexadecimals concrets) que la global no té espai per representar; (2) totes dues com a retalls de `T5_coma_flotant_racionals__drawio.svg` (figura orfe a `22_figs_originals/`, no referenciada per cap `.qmd`, que sembla l'esborrany original) — el drawio (7465 línies, estil amb fletxes i icones pròpies) no comparteix coordenades ni disseny amb les figures actuals en estil pla.

  **TODO futur**: investigar `gen_crops.py` sobre una figura global com la primigènia, és a dir, com a **font única des de zero** en lloc d'intentar-ho a posteriori sobre figures ja redibuixades per separat. Requeriria: (i) redibuixar aquesta figura en estil pla natiu (coherent amb `svg.md`, no drawio) com a única font de veritat amb tot el contingut (rang global + zoom de zero + denormals); (ii) definir a `retalls.toml` les finestres de cada vista actual; (iii) verificar que cada retall és net. Si viable, eliminaria la duplicació de manteniment entre les dues figures actuals. Fora de l'abast d'una revisió textual.

---

## Tasques per tema

### T2

- **Verificació tècnica de la taula de restriccions d'alineació** (`A2.qmd:1056`, mesurat a `ebdf055`; callout `#cau-memoria-restriccions-alineacio`): comprovar que la informació de la taula és correcta i coincideix amb l'**ABI `ilp32`**, i que **no hi ha col·lisió amb l'alineació a 16 del Bloc d'Activació** que fixa l'ABI de RISC-V. Afecta el rigor tècnic i no consta en cap registre anterior (detectat a l'auditoria, sessió 1). És la taula que la Fase C de L2 va corregir, de manera que la verificació ha de cobrir totes dues. El marcador segueix al corpus fins que la verificació es faci. **Sobreviu al tancament de la revisió interna de T2** (2026-09-23): es resol des d'aquí, sense reobrir el tema.

### T3

- **Criteri «quatre formats nuclears» aplicat a A3 sencer**: el criteri és a `13_contrib.qmd §Decisions per tema → T2 i T3` des del 2026-10-01, quan es va retirar l'entrada global de §Contingut global (§Entrades retirades). A3 és l'únic fitxer que en queda, i espera el port de la MR `!5`. A3 ja s'hi ha ajustat parcialment (referències creuades cap a T2 als callouts `#nte-format-b`, `#nte-format-j`, `#nte-format-u`), però cal revisar-lo sencer per aplicar el criteri de manera estricta i coherent a tot el tema. **La revisió interna de T3 es va tancar el 2026-09-23 sense aquesta passada**: es fa com a tasca d'harmonització transversal en un xat dedicat a `A3.qmd`, que no reobre la revisió del tema.

- **Decisió de contingut a `#cau-boolea-c`** (`A3.qmd:244`, pendent d'Adrià, obert des de la revisió de T3): el text diu que «unes expressions no nul·les s'interpreten com a certes» sense dir **quines**. Cal indicar com s'identifiquen les que sí i les que no. Afecta el rigor tècnic. El marcador segueix al corpus perquè la decisió és viva i no la pot prendre Claude Code.

- Retocs manuals pendents (Roger) a les figures:
  - `auto_figs/T3_ba_exemple__original_light.svg`
  - `auto_figs/T3_deps_multi__original_light.svg`
  - `auto_figs/T3_deps_exemple__original_light.svg`

### T4

- **Slug `{#sec-casos-especials}` genèric** (`A4.qmd:460`). Si mai cal desambiguar, `{#sec-casos-especials-divisio}`. ⚠️ **El registre d'origen deia que «ara no es referencia des d'enlloc; canviar-lo no trenca res», i això ja no és cert**: `S4.qmd:228` fa `@sec-casos-especials`, de manera que reanomenar-lo **obliga a tocar també aquella referència**. Prioritat baixa, però amb el cost actualitzat. Sobreviu al tancament de la revisió interna de T4 (2026-09-23): es resol des d'aquí, sense reobrir el tema.

  ```bash
  git grep -n "casos-especials" -- '*.qmd' ':!TODO.md'
  # A4.qmd:460 (definició) · S4.qmd:228 (referència)
  ```

  *(Origen: `TODO/T4_P_tasques.md:311`, tercera vinyeta del §8 «Pendents heretats que romanen oberts»; fitxer transitori esborrat, mai no va arribar a aquest fitxer fins ara. Es recupera sencer amb `git show a211bbf:TODO/T4_P_tasques.md`. El text original deia: «slug `{#sec-casos-especials}` és genèric; si mai cal desambiguar, `{#sec-casos-especials-divisio}` (ara no es referencia des d'enlloc; canviar-lo no trenca res, però tampoc no urgeix)» — l'última clàusula és la que ha caducat, com diu l'avís de dalt.)*

  ⛔ **A4, A5 i A6 en queden fora** fins que el grup de treball hagi fusionat `temes456` (revisió externa en curs: vegeu §Decisions obertes → Branques del remot).

### T5

- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present. *(No retirar sense actualitzar `13_contrib.qmd:729` —mesurat a `ebdf055`—, que hi remet explícitament: «T5 → T9: `fcsr` → `@nte-zicsr` (vegeu `TODO.md §T5 P8`)».)*

### T6

- **Etiquetes de classe d'instruccions en anglès** a les taules d'E6/S6 («Load», «Store», «Branch», «L/S»…): decidir si es mantenen com a etiquetes de columna/fila (opció actual) o es tradueixen («Lectura», «Escriptura», «Salt»), coherentment amb les substitucions obligatòries de prosa. **La decisió també afecta 7 usos en prosa**, on l'etiqueta funciona com a nom de la classe: `E6.qmd:66` («les branch 2 cicles»), `:104`; `S6.qmd:167`, `:177` (dues), `:185`, `:195` (mesurat 2026-10-01; l'entrada «Terminologia anglesa a la prosa d'E/S» els va deixar aquí). *(No retirar sense actualitzar `13_contrib.qmd:170` —mesurat a `ebdf055`—, que hi remet: «pendent una decisió transversal … (vegeu `TODO.md §T6`)».)*

### T7

- **Figures pendents de reconstrucció com a natives** (requereixen LO Draw de Roger).

  ⚠️ **Descripció corregida (auditoria, sessió 3).** La versió anterior d'aquesta taula marcava quatre figures amb «🔴 Referència trencada». **Cap ho és**: les quatre tenen el div definit i la referència resol — la verificació de la sessió 2 (`make render` sense warnings, 0 `?@` als 39 HTML) ho confirma. El que està pendent és **reconstruir-les com a natives**, perquè avui es consumeixen com a exports (`__extern_`) o amb figura provisional. L'única ocurrència de `?@` al `_book/` d'avui és dins de `site_libs/quarto-html/anchor.min.js` (JavaScript minificat de Quarto), no una referència.

  | Figura | Ancoratge | Estat verificat | Què falta |
  | :--- | :--- | :--- | :--- |
  | `fig-cd-diagrama` | `A7.qmd:300` | Consumeix `T7_cd_diagrama__extern_{light,dark}` | Reconstruir com a nativa |
  | `fig-assoc-conjunts-diagrama` | `A7.qmd:362` | Consumeix `T7_assoc_conjunts_diagrama__extern_{light,dark}` | Reconstruir com a nativa |
  | `fig-ca-diagrama` | `A7.qmd:393` | Placeholder de `7410a51`: `22_figs_originals/T7_ca_diagrama.svg` és idèntic byte a byte a `TODO.svg` | Cal crear-la |
  | `fig-texe-diagrama` | `A7.qmd:783` | Placeholder de `7410a51`: `22_figs_originals/T7_texe_diagrama.svg` és idèntic byte a byte a `TODO.svg`. Referència: PDF pàg. 24 | Cal crear-la |
  | `fig-mc-exemple-descomposicio-32bits` | — | Cap ancoratge al corpus | Export LO Draw a `23_figs_externes`; reconstruir com a natiu |
  | `fig-multinivell-diagrama` | — | Cap ancoratge | CPU→L1→L2→MP; LO Draw pendent |
  | `fig-multinivell-multicore` | — | Cap ancoratge | Xip 4 nuclis L1/L2/L3; LO Draw pendent |

  ```bash
  git grep -n "auto_figs/T7_cd_diagrama\|auto_figs/T7_assoc_conjunts_diagrama" -- '*.qmd' ':!TODO.md'
  ```

  ⚠️ **Estat corregit el 2026-09-25 (mesurat a `ebdf055`): `fig-ca-diagrama` i `fig-texe-diagrama` no eren natives, sinó placeholders.** La taula en deia «Ja `__original_` (nativa)». Els dos fitxers font —i el de T8, vegeu §T8— són **el mateix fitxer** que `TODO.svg`, creat a `7410a51` («figs que manquen -> placeholder "TODO"») i només reanomenat després:

  ```bash
  sha256sum 22_figs_originals/{TODO,T7_ca_diagrama,T7_texe_diagrama,T8_mv_flux_traduccio}.svg
  # 013175106fe402579ef6f7b202b720fca20303ea57aed15db0c37bae7ea01496 × 4
  git ls-files -z | xargs -0 sha256sum | grep -c 013175106fe4   # 4: cap altre fitxer no el comparteix
  ```

  **Per què l'error**: es va concloure «nativa» per l'**existència** del fitxer `…__original_{light,dark}.svg` que el corpus consumeix —el nom diu *original*— i no pel seu **contingut**. És la regla 2 de `13_contrib.qmd §Escombrades i verificació del corpus` (mesurar per forma, no per nom): el sufix `__original_` només diu d'on surt el derivat, no què hi ha dibuixat.

- **`fig-lru-roger` (màquina d'estats LRU)**: decidir si cal figura independent, o si n'hi ha prou amb la que ja va inclosa dins `T7_lru_exemple.svg` (`A7.qmd:460`, `#fig-lru-exemple`). ⚠️ El comentari `<!-- TODO fig-lru-roger: diagrama d'estats -->` que ho registrava al corpus **ja no hi és** (eliminat a la sessió 2 per redundant amb aquesta entrada): `git grep -n "fig-lru-roger" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'` → cap. **Aquesta entrada és ara l'única còpia.** L'exclusió del fitxer de convencions n'amaga **dues** ocurrències (mesurat a `ebdf055`; abans en deia «una sola», a `:914`): `13_contrib.qmd:1019`, la lliçó 8 de §Escombrades i verificació del corpus, que cita aquest mateix cas com a exemple de marcador que es va poder eliminar perquè el `TODO.md` ja en tenia l'entrada, i `:1083`, la llista de casos de la regla 12. Totes dues són **cites de la tasca, no ocurrències al corpus**, i sense excloure-la l'ordre diria que el marcador encara hi és (vegeu-hi la regla 12).

- **`fig-capacitat-exemple` a HTML**: dues figures separades (primera + segona passada) o figura única combinada? Existeixen totes tres variants a `auto_figs/` (`T7_capacitat_exemple__original_*`, `T7_capacitat_exemple_bucle_primera_passada__original_*`, `..._segona_passada__original_*`). Pendent de decisió.

- **Dos SVG orfes amb `____error____` al nom.** Versionats i no referenciats per cap `.qmd`:

  ```bash
  git ls-files | grep -i "error____"
  # 23_figs_externes/T7_texe_diagrama____error____.svg
  # 23_figs_externes/T7_tres_c_barres_light____error____.svg
  git grep -n "error____" -- '*.qmd' ':!TODO.md'   # cap referència
  ```

  ❓ **Pregunta oberta**: l'`__error__` al nom marca una figura **a refer**, o són **descartables**? No s'ha decidit ni tocat res. *(Els altres quatre fitxers amb el mateix patró són a `auto_figs/`, que és a `.gitignore:5`: són derivats regenerables, no entren aquí.)*

### T8 — Figures pendents de creació

**En queden 9** (mesurat a `ebdf055`): les nou especificacions `<!-- fig-mv-… -->` d'`A8.qmd`, cap de les quals no té encara SVG real.

| Especificació | Estat |
| :--- | :--- |
| `fig-mv-espais` | Sense div ni SVG |
| `fig-mv-pagines-marcs` | Sense div ni SVG |
| `fig-mv-taula-pagines` | Sense div ni SVG |
| `fig-mv-taula-multinivell` | Sense div ni SVG |
| `fig-mv-tlb-estructura` | Sense div ni SVG |
| `fig-mv-flux-traduccio` | Div `{#fig-mv-flux-traduccio}` (`A8.qmd:267`), que consumeix (`:270,273,277`) el **placeholder** de `7410a51` |
| `fig-mv-comparticio` | Sense div ni SVG |
| `fig-mv-pipt` | Sense div ni SVG |
| `fig-mv-vipt` | Sense div ni SVG |

```bash
grep -c '<!-- fig-' 01_apunts/A8.qmd                                   # 9
git grep -o "auto_figs/T8_[a-z_]*" -- 01_apunts/A8.qmd | sort -u
# només T8_mv_flux_traduccio__original_{dark,light}
sha256sum 22_figs_originals/{TODO,T8_mv_flux_traduccio}.svg           # hash idèntic
```

⚠️ **Xifra corregida dues vegades.** La primera versió deia «8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio`»; l'auditoria (sessió 3) la va baixar a **7** perquè `auto_figs/T8_mv_flux_traduccio__original_{light,dark}.svg` existien i el div els consumia. **Aquella correcció era falsa**: `22_figs_originals/T8_mv_flux_traduccio.svg` és idèntic byte a byte a `TODO.svg` (vegeu l'ordre de §T7), de manera que la prioritat **no està feta**. I el «8» original ja era curt: `A8.qmd` té nou especificacions des de `8121003`. L'error de la sessió 3 és el mateix que el de §T7 —concloure per l'**existència** del fitxer i no pel **contingut**, regla 2—; la referència, això sí, no és trencada: resol, però a un placeholder.

Rutes de destí per a les 9: `/auto_figs/T8_*__original_light.svg`.

### T9

- **F/G — Figures SVG**: diferides a una fase posterior. Estat actual: A9 consumeix 24 vegades `auto_figs/`, totes de la mateixa figura (`T9_cicle_interrupcio`).

### Laboratori

- **Renumeració de lliuraments (2026-07-05)**: els fitxers de lliurament de L2–L6 s'han renumerat al número de sessió (`s2_*`–`s6_*`; abans anaven una sessió endarrerits i col·lidien amb L1). Cal revisar-ne els noms quan es decideixi el mecanisme de descàrrega.

  El que quedava d'això al `TODO/` eren sis marcadors **de zero bytes** (comprovat amb `git cat-file -s`: 0 tots sis), les rutes dels quals eren tota la informació que contenien. S'han esborrat el 2026-09-22 i les rutes es preserven aquí, que és el que s'ha de revisar:

  ```
  TODO/laboratori/L0/TODO.s
  TODO/laboratori/L1/TODO.s
  TODO/laboratori/L2/TODO.s
  TODO/laboratori/L3/TODO.s
  TODO/laboratori/L4/TODO.s
  TODO/laboratori/L5/TODO.s
  ```

  Noteu el desfasament que la renumeració havia de resoldre, i que aquests noms encara reflecteixen: numerats `L0`–`L5` per a sessions que ara són `L1`–`L6`. Es recuperen (buits) amb `git show 3a3aea6:<ruta>`.

---

## Tasques globals

### SVG

- **Migració de canvas a amplades estàndard**: figures de BA i mapa de memòria → classe `estreta` (`W=340 px`). Decisió pendent: mantenir `w_rect=230` (marge dret 10→34) o ampliar `w_rect` a 254 (marges simètrics). Un cop decidit, aplicar a les figures afectades i actualitzar `24_specs/svg.md §2`.

  ⚠️ **Descripció corregida (auditoria, sessió 3).** La versió anterior deia «figures de BA i mapa de memòria (`W=316 px`) → …» i llistava set figures com si totes tinguessin aquell canvas. **Mesurat per forma, només una el té.** Amplades reals de les set:

  | Figura | `width` / `viewBox` |
  | :--- | :--- |
  | `T3_mapa_memoria` | **326** (`0 0 326 325`) |
  | `T3_ba_general` | **326** (`0 0 326 580`) |
  | `T3_ba_func` | **326** (`0 0 326 540`) |
  | `T3_ba_multi` | **326** (`0 0 326 260`) |
  | `T3_ba_exemple` | **316** (`0 0 316 620`) |
  | `T3_func_uninivell_pila` | **310** (`0 0 310 240`) |
  | `T3_pila_crides_aniuades` | **450** (`0 0 450 280`) |

  ```bash
  grep -l 'viewBox="0 0 316' 22_figs_originals/*.svg   # només T3_ba_exemple.svg
  ```

  📌 **Conseqüència: `24_specs/svg.md` ha quedat desfasat.** Les línies `:70` («`w_rect=230 px`; `W=316 px`») i `:76` («els valors numèrics … corresponen al canvas actual … `W=316 px`») fixen com a «canvas actual» un valor que **sis de les set figures no compleixen**. La migració ha de corregir també l'especificació, no només les figures. **No s'ha tocat**: és corpus, i l'auditoria no en modifica.

- **`22_figs_originals/T4_multiplicador_sequencial.png` (63 KB)**: decidir si s'elimina. Verificat (auditoria, sessió 2): **no el referencia ningú** — `A4.qmd:175,178,182` usen només el `.svg` via `auto_figs/`. És **l'única parella `.png`+`.svg` del directori**, de manera que eliminar-lo també elimina l'excepció al criteri d'un sol format font. No s'ha tocat: és un fitxer binari i la supressió no entrava a l'abast autoritzat.

  ⛔ **A4, A5 i A6 en queden fora** fins que el grup de treball hagi fusionat `temes456` (revisió externa en curs: vegeu §Decisions obertes → Branques del remot).

  ```bash
  git grep -n "T4_multiplicador_sequencial" -- '*.qmd' ':!TODO.md'
  # A4.qmd:175,178,182 — totes tres al .svg
  ```

### Contingut global

- **Equacions a MathML**: **decisió presa — mantenir MathJax 3**; el pendent és reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa). Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`): funciona (`underbrace`, `cases`, taules amb math correctes a Chrome) i elimina el JS de MathJax (render instantani, offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), numeració d'equacions inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. El desbordament mòbil ja està resolt via CSS.

- **PDF**: figures dins callouts no queden centrades → investigar via `preamble.tex`. A més, comportament en callouts encastats: es respecta la separació (`-1` del `layout=`), però no el repartiment si hi ha línies de text que no hi caben (falta l'exemple concret de `13_contrib.qmd`).

- **Figures externes (llicències)**: taula completa de figures extretes de PDFs (incloses fonts i llicències). Referència eliminada temporalment de `13_contrib.qmd`. Enllaça amb `§Decisions obertes → Figures portades d'extern`.

- **Gestió d'errades post-commit**: definir protocol. ⚠️ **La secció de destí és buida**: `13_contrib.qmd:779` (mesurat a `ebdf055`) té la capçalera `### Gestió d'errades` seguida directament de `## Eines` (`:781`), sense cap contingut. En resoldre-ho, o bé s'omple la secció, o bé se n'elimina la capçalera i la tasca queda només aquí.

### Eines

- **`verifica_laboratoris.py` no dedueix el «bloc no autònom».** El script **ja té** la noció de bloc que no ha d'assemblar sol, però com a **taula codificada a mà**, no com a propietat derivada del contingut (`25_scripts/verifica_laboratoris.py:79`, mesurat a `ebdf055`, `INCOMPLETE_BY_DESIGN`). Dues conseqüències:

  - **Una taula paral·lela al contingut divergeix en silenci** — el mateix motiu que va treure les plantilles `.markdown`. La raó codificada ja s'ha hagut d'actualitzar un cop (citava `@sol-update`; ara el bloc diu «vegeu la solució de `s3_4_1.s`»).
  - **`#exr-depuracio` no hi és**, i és el mateix cas per un altre camí: té tres errors a posta. Un bloc pot ser no autònom **per omissió** (falta codi) o **per incorrecció deliberada** (el codi hi és i està malament a propòsit).

  Cal una noció de **bloc no autònom** derivada del contingut. *(Origen: `TODO/decisions__informe.md`, informe transitori esborrat per `87f2853`; es recupera sencer amb `git show 87f2853^:TODO/decisions__informe.md`.)*

### `index.qmd`

- **Consolidar les versions de la taula de referències tècniques** (`#imp-llenguatges-de-referencia`). Cinc marcadors vius, `index.qmd:195-199`, que són **tres pendents distints**:

  | Marcadors | Pendent |
  | :--- | :--- |
  | `:195`, `:196` | Versió de la norma **ISO de C** (i si és tancada). La taula ja cita `[@iso9899_2024]`: el pendent és **verificar i tancar**, no decidir de zero |
  | `:197`, `:198` | Versió de **GCC** (`[@gcc16]`), i consolidar noms i versions de totes les files |
  | `:199` | **Versió numèrica o de data per a CSR** (fila de RISC-V, `[@riscv_csrs]`): decidir si la referència s'identifica per número de versió o per data. ✅ **No constava en cap registre anterior** |

  La fila duplicada de *Toolchain* ja no hi és (verificat 2026-07-13: la taula té una sola fila per ítem).

---

## Entrades retirades en la reescriptura del 2026-09-21

Cada entrada, amb el motiu i on en queda còpia. **Cap no s'ha retirat sense comprovar que el pendent o bé ja no existeix, o bé té registre en un altre lloc.**

### Executades

| Entrada | Motiu | Còpia que en queda |
| :--- | :--- | :--- |
| `startup.s` — decisió i neteja | Executada (sessió 2): eliminats els 4 blocs comentats i unificats `E9:72`/`S9:201` a `li a7, 93` | El **bolcat de dades d'`A2.qmd:744-810`** es preserva a §Dades preservades, al final |
| `_start` primera etiqueta de `.text` | **RETIRADA (2026-09-24): el criteri que la sostenia s'ha invertit.** Deia: «TANCAT (sessió 2): verificats els 25 blocs de `.text` amb `_start` de L1–L6, **0 infraccions**», amb la regla consolidada a `13_contrib.qmd:204`. El punt d'entrada ja no porta etiqueta (`b2c1a4f`), de manera que no hi ha cap ordre a verificar: la comprovació estàtica E1 de l'arnès es va retirar pel mateix motiu (`d51577d`) | **El 25 era correcte i el 26 d'avui també**: el registre comptava els blocs de **L1–L6**, i la 26a definició era `A2.qmd:1083`, fora del laboratori. Les dues xifres es reprodueixen a `d51577d` (`git grep -cE "^_start:" d51577d -- 04_laboratori/` → 25; `-- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'` → 26). La regla nova és a `13_contrib.qmd §Convencions globals del laboratori`; el que en sobreviu és l'exempció dels tres blocs (`s2_4_1.s`, `s5_1_1.s`, `s5_2_1.s`), amb el motiu que no caduca |
| Nota obsoleta a `13_contrib.qmd:204` | Retirada pel mateix tancament: la nota ja no diu «pendent d'aplicar a L3» | — |
| Plantilles Markdown (`L2.qmd` i resta) | Executada a la passada C (`733b408`). `git grep '```{.markdown' -- '*.qmd' ':!TODO.md'` → **cap** | — |
| L2 §«Pseudoinstrucció `la` i `li`» amb cos «TODO» | Omplert per la Fase C. `git grep -n "Pseudoinstrucció" -- 04_laboratori/L2.qmd` → **cap** | — |
| Referència `@imp-exception-handler` de `#tip-rars-main-multinivell` | El callout es va eliminar amb els blocs de `startup.s`; no hi ha res a verificar | — |
| Encaix T2↔T3 (caller-saved/callee-saved) | RESOLTA 2026-07-13: remissió afegida a `#nte-registres-proposit-general` d'A2 | `13_contrib.qmd` i el corpus |
| `@wrn-codificacio-enters-ca1` | RESOLTA: `A3.qmd` ja usa `@sec-enters-en-ca1` | — |
| T5 F1 — figures addicionals | RESOLTA 2026-07-13: `T5_ieee754_format` i `T5_grs_esquema` creades; la tercera ja existia | Les figures, al corpus |
| T5 — veu dels enunciats (E5) | RESOLTA 2026-07-13: E5 a 2a plural, `#tip-` d'A5 a 2a singular, S5 impersonal | — |
| (a) Harmonització `21_riscv/` `\leftarrow` | RESOLTA 2026-07-13: tots els fitxers ja usen `\leftarrow` i `offset` sencer | — |
| (b) `RV32I_registres_coma_flotant` divergent | Revisada 2026-07-13: es mantenen les dues formes, decisió presa | — |
| (c) Taules de camps de `fcsr` | Decidit 2026-07-13: es mantenen inline | — |
| (e) Criteris de numeració de callouts | RESOLTA 2026-07-13 | Documentat a `13_contrib.qmd §Callouts` |
| `void main()` vs `int main()` | **Decisió presa i executada** a la passada C, bloc 2b (`b3072a6`) | Regla a `13_contrib.qmd:492`, justificació a `:494`, blocs protegits a `:500-503` (línies mesurades a `ebdf055`). Estat del corpus a `ebdf055`: **41** línies `void main` i **5** línies `int main`, que són els **tres protegits** (`A2:835`, `E3:661`, `S3:685`), `A2:1996`, que és la nota per a l'alumne, no codi, i `A3:1896`, prosa del callout `@nte-punt-entrada-etiqueta` afegit a `b362576`. ⚠️ **El «40 `void main` i 4 `int main`» que aquesta cel·la publicava no reprodueix ni al commit citat**: a `b3072a6` les mateixes ordres donen **38** i **3** (`A2:859`, `E3:661`, `S3:685`; la nota d'`A2` encara no hi era). Ordres: `git grep -c "void main" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' \| awk -F: '{s+=$2} END{print s}'` i `git grep -n "int main" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'` (amb un commit al davant, l'`awk` llegeix `$3`) |
| `index.qmd` — enllaç a `laboratori/L0/TODO.s` | RESOLTA: ja no hi és | — |
| `index.qmd` — fila duplicada de Toolchain | RESOLTA parcialment; la resta viu a §`index.qmd` | Aquest fitxer |
| `index.qmd` — enllaç «Còpia local» de `rars1_6.jar` | **Executada (decisió de l'usuari, 2026-09-21)**: el binari es queda **fora del repositori** i l'enllaç primari és la *release* de GitHub. Eliminada l'àncora `<a href="04_laboratori/rars1_6.jar" download>` d'`index.qmd:146`, mantenint la frase i l'enllaç de GitHub. Coherent amb `fbf7c3d` (2026-07-11), que va eliminar el binari perquè ja no era al disc. L'entrada antiga d'aquesta taula («URL de la còpia local: RESOLTA, ja hi és») era la que havia introduït l'àncora | **Cap còpia pendent**: `git grep -n "download>" -- '*.qmd' ':!TODO.md'` → cap, i `git grep -n "04_laboratori/rars1_6" -- . ':!TODO.md' ':!13_contrib.qmd'` → cap. No queda cap rastre apuntant al fitxer. L'exclusió del fitxer de convencions n'amaga **dues** ocurrències (mesurat a `ebdf055`; abans en deia «una sola», a `:882`): `13_contrib.qmd:987`, que explica **per què** el binari en va sortir (era del repositori, no de qui l'executava), i `:1083`, la llista de casos de la regla 12. Totes dues són la lliçó, no rastres vius (vegeu-hi la regla 12). El `README.md:182` (mesurat a `ebdf055`) el cita com a descàrrega externa, que és correcte |
| **T1 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T1 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C executada (`f5e8223`, 2026-07-12) i revisió acabada (`9de6756`, 2026-07-13), tots dos amb «TODO segones passades» a l'assumpte; **cap passada posterior**; declaració prèvia «tancat de facto» del 2026-07-12. Les segones passades que els commits anunciaven queden cobertes pel tancament i **no** s'han de reobrir | Dues coses que només constaven a la fila: (i) la **sincronització amb el remot del 2026-07-13** —`A1.qmd`, `S1.qmd` i les tres figures SVG verificades idèntiques a la versió de Fase C—, detall a `git show a211bbf:TODO/T1_P_tasques.md`; (ii) **SVG-6**, l'etiqueta «Objecte» → «Fitxer objecte» de `T1_flux_compilacio.svg`, que la Fase C va descartar perquè el text no cabia al requadre: **l'usuari ha revisat la figura el 2026-09-23 i la dona per correcta**, de manera que l'etiqueta es queda com és (`22_figs_originals/T1_flux_compilacio.svg`, «Objecte»). No queda cap pendent de T1 |
| **T2 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T2 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`31f7571`, 2026-07-12), amb «**Falta** segones passades» a l'assumpte i **cap passada posterior**; el registre no declarava cap estat final. Les segones passades queden cobertes pel tancament i **no** s'han de reobrir | ⚠️ **El tancament del tema no tanca els set marcadors vius d'`A2.qmd`**, que és el fitxer amb més marcadors del corpus. Es van comprovar un per un abans de tancar i **tots set ja tenen entrada viva** en aquest fitxer, amb la línia exacta (línies re-mesurades a `ebdf055`): `:620` i `:645` (format de les taules de pseudoinstruccions) → `§Decisions obertes`; `:728` i `:729` (consens dels criteris de codi C i proposta de *checker*) → `§Decisions obertes`; `:964` i `:1002` (taules de memòria → figura estàndard) → `§Decisions obertes`; `:1056` (taula d'alineació contra l'ABI `ilp32`, callout `#cau-memoria-restriccions-alineacio`) → `§T2`. Són decisions i verificacions que **sobreviuen al tancament de la revisió**: es resolen des de les seves entrades, no reobrint T2 |
| **T3 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T3 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`b55e413`, 2026-07-13) —assumpte **net**, sense cap «falta» ni «TODO»— i **cap passada posterior**; el registre no declarava cap estat final. T3 és l'únic tema amb el trio A/E/S revisat: `E3.qmd` i `S3.qmd` ja constaven amb la revisió interna completada | ⚠️ **Tres entrades vives del `§T3` sobreviuen al tancament** i es resolen des d'allà, sense reobrir el tema: (i) el marcador `A3.qmd:244` (`#cau-boolea-c`, decisió d'Adrià sobre quines expressions no nul·les són certes); (ii) els **retocs manuals de tres figures** (`T3_ba_exemple`, `T3_deps_multi`, `T3_deps_exemple`), pendents de l'usuari; (iii) el criteri «quatre formats nuclears» aplicat a A3 sencer. ⚠️ **Aquesta tercera demana literalment «un xat de revisió interna dedicat a A3.qmd»**: el tancament de T3 **no** la dona per feta, i si s'executa serà com a tasca d'harmonització transversal —l'entrada canònica és a `§Contingut global`—, no com una reobertura de la revisió |
| **T4 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T4 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: revisió interna acabada (`9faab05`, 2026-07-13) amb «TODO segones passades» a l'assumpte, **cap passada posterior**, i declaració prèvia «quasi tancat» del 2026-07-12. El resum final del registre (`:329`; corregit: el `:312` d'abans no reproduïa ni al commit citat, `git show a211bbf:TODO/T4_P_tasques.md`) deia «no queda cap decisió pendent tret de l'ítem 8» | És la fila més verificada de la taula: el Bloc 4c en va auditar els tres ítems que la primera taula del registre donava per oberts i va establir que **el 3 i el 4.2 són aplicats** (`#wrn-mul-modul-2n` a `A4.qmd:323`, referenciat des de `S4.qmd:214`; punter T4→T7 a `13_contrib.qmd:730`, mesurat a `ebdf055`). **Cap pendent de T4 no depenia d'aquesta fila**: els tres que arrossega ja són entrades vives i sobreviuen al tancament — l'**ítem 8** (figures *half-adder*/*full-adder*, marcadors `A4.qmd:80,81`) a `§Decisions obertes`, el **`.png` del multiplicador seqüencial** a `§Tasques globals → SVG`, i l'**slug genèric `{#sec-casos-especials}`** a `§T4`. Vegeu també la fila **P3** d'aquesta mateixa taula, que registra el tancament de l'ítem 3 |
| **T5 · ítem 4.8 — dobles espais en prosa** | **Executada (2026-09-23).** Les tres línies de la llista de registres de `#sol-t5-ops-variancia` que alineaven la fletxa amb espais de farciment (`` - `q`   → ``, `` - `i`   → ``, `` - `m`   → ``) passen a un sol espai, com les altres dues de la mateixa llista. `S5.qmd:739-743`; prosa, no bloc de codi, de manera que hi aplica la regla de `13_contrib.qmd §Commits` | Cap pendent. Verificat: `sed -n '739,743p' 03_solucions/S5.qmd \| grep -cE "[^ ] {2,}[^ ]"` → 0 |
| **T5 · ítem 4.12 — cursives repetides de *sticky*** | **Executada (2026-09-23).** `E5.qmd:209` repetia `*sticky*` en cursiva quan la primera aparició del fitxer ja és a `:110`; s'hi treu la cursiva. La regla del projecte és cursiva només a la primera aparició per fitxer | Cap pendent. Estat final de les cinc ocurrències: `E5.qmd:110` i `A5.qmd:440` en cursiva (primeres de cada fitxer), `E5.qmd:209`, `A5.qmd:764` i `:789` sense |
| **T5 · ítem 3.8 — títol de secció «Suma i multiplicació»** | **Decisió presa i executada (usuari, 2026-09-23): «Suma i multiplicació» → «Operacions».** El registre recomanava deixar-ho com estava, i l'usuari decideix el contrari: el títol no cobria el contingut de la secció (hi ha també divisió, conversions i traducció a assemblador). **9 substitucions** en 3 fitxers: les capçaleres `E5.qmd:85` i `S5.qmd:372`, i les **7 files** de la columna de tema de `S_criteris_seleccio.qmd:82-88` | Cap pendent. Verificat abans de tocar res que les capçaleres **no porten etiqueta `{#sec-}`** i que cap `@sec-` no hi apunta (`git grep -nE "sec-suma-i-multiplicacio\|sec-suma-multiplicacio"` → cap), de manera que el canvi no trenca cap referència creuada. Després: `git grep -c "Suma i multiplicació" -- . ':!TODO.md'` → cap ocurrència. «Operacions» encaixa amb els altres valors de la columna de `S_criteris_seleccio.qmd` («Multiplicació», «Divisió», «Matrius», «Operacions lògiques i desplaçaments»…) |
| **T5 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T5 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: **l'únic tema amb la revisió declarada «parcial»** pel commit mateix (`92345e4` i `b81e3fa`, 2026-07-13) i **cap passada posterior**. ⚠️ **Què volia dir aquell «parcial» ha quedat establert**: l'auditoria del 2026-09-23 va comprovar els **29 ítems** del registre un per un contra el corpus i en va trobar 26 aplicats; els dos d'execució que restaven (4.8, 4.12) i la decisió (3.8) es van executar el mateix dia. **Els 29 ítems del registre són tancats** | Sobreviuen al tancament, i es resolen des de les seves entrades sense reobrir el tema: les decisions **R4-TYPE** i **R5-TYPE** (marcadors `A5.qmd:5,6`, a `§Decisions obertes`) i **P8** (`fcsr` amb dependència cap endavant a `@nte-zicsr` de T9, a `§T5`). Cap de les tres no surt del registre de T5 |
| **T6 — notació de la tensió d'alimentació a S6** | **Decisió presa i executada (usuari, 2026-09-23): S6 passa sencera a $V_{CC}$.** L'entrada advertia que l'harmonització «s'ha de fer sencera o no fer-se», perquè tota la derivació de `S6.qmd` usava $V$ de manera consistent i canviar-ne només la línia que cita l'equació l'hauria deixada incoherent. **5 substitucions** a `S6.qmd`: `:324` ($P_{din} = C \cdot V_{CC}^2 \cdot f$), `:326` i `:344` (aïllament de $C$), `:334` ($V_{CC,A}$, seguint el subíndex de processador de `C_A`/`f_B`) i `:346` (capçalera de columna de la taula de vuit generacions) | Cap pendent. ⚠️ **Les unitats no s'han tocat**: les cinc ocurrències de `\text{ V}` que queden a `:328`, `:330`, `:361`, `:396` i `:398` són volts, no el símbol. `S6.qmd:394` ja usava $V_{CC}$ abans del canvi, de manera que el fitxer també era incoherent amb si mateix. Notació ara uniforme a `A6.qmd:270-278`, `E6.qmd:192`, `A7.qmd:113`, `S6.qmd` i el glossari `12_sigles_simbols.qmd` |
| **T6 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T6 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`77853ff`, 2026-07-12) amb «Següent segones passades» a l'assumpte, **cap passada posterior**, i declaració prèvia «quasi tancat» del 2026-07-12. El registre declarava les tres seccions (A, B, C) aplicades, amb una verificació per script que cap resultat numèric en `\mathbf{}` de S6 no s'havia alterat (32/32 idèntics) | `A6.qmd` **no tenia cap marcador viu**, i la discrepància de notació E6/S6 —l'únic pendent tècnic del tema— s'ha resolt al mateix commit del tancament (fila anterior). Sobreviu una sola entrada, a `§T6`: les **etiquetes de classe d'instruccions en anglès** («Load», «Store», «Branch») a les taules d'E6/S6, que és una decisió transversal, no pròpia de T6; `13_contrib.qmd:170` (mesurat a `ebdf055`) hi remet |
| **T7 · C3 — seqüència d'adreces truncada a `exr-t7-assoc-multinivell`** | **Executada (2026-09-23), contrastada amb el PDF original com demanava l'entrada.** L'enunciat deia «seqüència de 28 adreces … `0, 5, 10, 12, 34, 0, 66, ...`»: amb els tres punts l'exercici **no era resoluble**, i a més el text es contradeia (28 adreces «repetides 4 vegades» són 112 accessos). Ara diu «la seqüència de 7 adreces següent, repetida 4 vegades (28 accessos en total): `0, 5, 10, 12, 34, 0, 66`» (`E7.qmd:219-221`, mesurat a `ebdf055`) | **La interpretació que l'entrada donava per probable queda confirmada per dues vies independents del `PDF_originals/`**: (i) l'enunciat original (`02_problemes.pdf`, problema 6.12 —T7 d'EC és el T6 dels originals—) diu «`0, 5, 10, 12, 34, 0, 66, ...` (que es repeteix **3 vegades més**)», és a dir 4 passades de 7 adreces; (ii) el solucionari original (`03_solucionari.pdf`) enumera la traça adreça per adreça i en dona el resultat, **$h_1 = 9/28$** i $h_2 = 7/19$, que només quadra amb 28 accessos totals. ⚠️ `S7.qmd` **no té solució per a aquest exercici**, de manera que l'enunciat n'era l'única còpia al corpus: era l'únic pendent registrat que deixava material inservible per a l'alumne |
| **T7 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T7 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: **cap passada posterior** i declaració prèvia «quasi tancat» del 2026-07-12. ⚠️ L'assumpte del commit (`2206477`, «T7-PE_T7-PS_T7 Fable raw») **no era una declaració d'estat sinó l'obertura de la revisió**: és anterior al refactor de directoris i és el commit que crea el registre. L'estat real és el del registre: **40 ítems ✅**, tres tandes de feina, i tanca dient «Pendent a `TODO.md §T7`: només C3» — que és la fila anterior, executada al mateix commit que aquest tancament | Sobreviuen quatre entrades del `§T7`, **totes de figures i totes dependents de l'usuari** (LO Draw o decisió): la taula de **7 figures pendents de reconstrucció com a natives** (⚠️ dues d'elles, `fig-ca-diagrama` i `fig-texe-diagrama`, hi constaven com a «ja natives» i són placeholders: vegeu `§T7`, corregit el 2026-09-25); **`fig-lru-roger`** (cal figura independent de la màquina d'estats LRU?), de la qual aquesta entrada **és l'única còpia** des que se'n va eliminar el marcador del corpus; **`fig-capacitat-exemple`** (dues figures o una de combinada?); i els **dos SVG orfes amb `____error____` al nom**, que ningú no ha decidit si són a refer o descartables |
| **T8 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T8 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`ccae7dd`, 2026-07-13), assumpte **net** —sense cap «falta» ni «TODO»— i **cap passada posterior**. És l'únic dels nou registres de teoria que es declarava tancat a si mateix: «**Estat: revisió interna de T8 tancada.** Blocs A, B i C íntegrament [executats]» | `A8.qmd` **no tenia cap marcador viu**. Sobreviu `§T8 — Figures pendents de creació`: **9 figures** de nova creació (mesurat a `ebdf055`), dependents de l'usuari, amb destí `/auto_figs/T8_*__original_light.svg`. ⚠️ **Aquesta fila en deia 7**, recollint la correcció de 8 a 7 de l'auditoria (sessió 3), que havia verificat que `T8_mv_flux_traduccio` existeix i que `@fig-mv-flux-traduccio` **no** és una referència trencada. **Aquella correcció era falsa**: `22_figs_originals/T8_mv_flux_traduccio.svg` és idèntic byte a byte a `TODO.svg` (el placeholder de `7410a51`), i el «8» original ja era curt, perquè `A8.qmd` té nou especificacions `<!-- fig-mv-… -->` des de `8121003`. Es va concloure per l'**existència** del fitxer, no pel **contingut** (regla 2); detall i ordres a `§T8`. Nota de comptabilitat: el `§T8` no té cap vinyeta `^- `, de manera que mai no ha comptat com a entrada viva encara que descrigui feina pendent |
| **T9 — contradicció sobre l'estat, i revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat, i la contradicció queda resolta per decisió.** L'únic commit de revisió de T9 (`87015d2`, 2026-07-11) acaba amb «**(s'ha d'acabar)**», mentre que el registre declarava «Fase C, **execució completa**». No es podien conciliar des del corpus —cap commit posterior no tanca el que `87015d2` deixava obert, i els que toquen A9/E9/S9 des de llavors són transversals (`c2a9171`, `d017ee2`, `7f243f5`, `257d37f`)—, de manera que la decisió era de l'usuari. **En tancar el tema, val el registre**: el «s'ha d'acabar» de l'assumpte descrivia l'estat d'aquell moment, no un pendent viu | `A9.qmd` **no tenia cap marcador viu**. Sobreviu una entrada al `§T9`: les **figures SVG**, diferides a una fase posterior (A9 consumeix 24 vegades `auto_figs/`, totes de `T9_cicle_interrupcio`). ⚠️ **Fora del `§T9`, T9 és el tema amb menys cobertura al glossari**: `12_sigles_simbols.qmd §Símbols` no té **cap** entrada de T9 (`grep -c "\| T9 \|"` → 0). Això no és un pendent de la revisió de T9 sinó de l'entrada transversal «nodrir les taules de Símbols i Notació», que ja ho recull i segueix viva |
| **L1 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L1.qmd` de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: «L1 revisió interna feta» (`fe53cfc`, 2026-07-13) —**l'assumpte més net dels quinze ítems**, sense cap clàusula posterior— i **cap passada posterior**. El registre confirmava les tres fases completades i que la tasca T8 es va eliminar perquè l'usuari ja l'havia resolta manualment a `L3.qmd`. La decisió de L1 es va aplicar amb l'opció 1 (blocs `{#sol-}` per als 7 exercicis, `L1.qmd:140,160,192,211,238,302,363` a `fe53cfc`; corregit: els quatre punters d'abans, `:134,142,185,187`, no reproduïen ni al commit citat) | **Cap entrada viva era específica de L1.** Dues transversals hi poden aterrar: la del **punt d'entrada de RARS**, que proposa com a destí «un `#nte-` breu a L1 (§Punts d'aturada/execució) o a A2» —i que el canvi de criteri de `_start` obliga a reformular abans d'executar-la—, i el **canvi de criteri de `_start` i `.section`** mateix, que tocarà els fragments d'assemblador de `L1.qmd` (8 ocurrències de `_start`, 4 `.globl`). Cap de les dues no reobre la revisió de L1. → **Totes dues executades** (2026-09-24): vegeu les files «Punt d'entrada de RARS» i «`_start` surt del codi» d'aquesta taula; la de `.section` al codi es va retirar per l'experiment (§Canvi de criteri `.section`) |
| **L2 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L2.qmd` de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C executada en tres commits del **2026-09-20** (`1489c84`, `254509b`, `12bac2c`) i **cap passada posterior**. ⚠️ El registre declarava només **Fase B** i la seva reconciliació del 2026-07-20 deia «tota la llista **B1–B11** continua vàlida»: era cert el juliol, i la Fase C de setembre —dos mesos després d'escriure'l— la va deixar obsoleta. **Les onze accions B1–B11 són executades** | Les B1–B11 eren les «accions d'execució directa» de la Fase C de L2 (`git show a211bbf:TODO/L2_tasques.md §B`): B1 secció «Pseudoinstruccions `la` i `li`», B2 taules, **B3 format d'adreces**, B4 cursives d'anglicisme, B5 harmonització lingüística, B6 lectura prèvia, B7 fórmules d'adreça, B8 callouts «Comprovació pràctica», B9 amplada de valors, B10 slug amb errata, B11 actualització del `TODO.md`. **B3 verificada en tancar**: el registre en deia «~64 adreces» i n'eren **99**, totes convertides per `254509b`; avui `git grep -nE "0x[0-9A-Fa-f]{4} [0-9A-Fa-f]{4}"` no en retorna cap. Sobreviuen dues transversals que hi toquen: l'**alineació de `.dword` a RARS** (`L2.qmd:153-166`, mesurat a `ebdf055`, amb l'avís que, del bolcat comparatiu MARS/RARS, **només la fila MARS (`:163`)** no existeix enlloc més: la RARS (`:164`) coincideix amb `:306`; vegeu l'entrada a §Tasques transversals) i el **canvi de criteri de `_start`/`.section`** → executat per a `_start` (fila «`_start` surt del codi») i retirat per a `.section` al codi (§Canvi de criteri `.section`) |
| **`exr-moda` (L3) — l'enunciat no deia què ha de contenir `s3_4_2.md`** | **Executada (2026-09-23).** `L3.qmd:17` llistava `s3_4_2.md` com a lliurament i `:303` obria la secció, però l'enunciat només demanava traduir `moda` i `_start`: **què havia d'anar al `.md` només es deduïa llegint el solucionari**. La frase passa a ser «Traduïu `moda` i `_start` a RV32I, **al fitxer `s3_4_2.s`**. Abans d'escriure cap instrucció, **responeu al fitxer `s3_4_2.md`**:», seguida dels dos punts que ja hi havia (registres segurs i bloc d'activació) | Cap pendent. Els dos punts numerats **ja eren a l'enunciat**: l'únic que faltava era lligar-los al fitxer de lliurament, de manera que no s'hi ha afegit cap requisit nou. Es confirma contra el solucionari, on **Pas 1** (registres segurs) i **Pas 2** (taula del BA amb els offsets) són exactament aquests dos punts. La redacció segueix el patró ja establert a `L4.qmd:319` (mesurat a `ebdf055`) («Abans d'escriure cap instrucció, responeu al fitxer `s4_3_1.md`:»), de manera que els dos fitxers de laboratori diuen ara el mateix de la mateixa manera |
| **Etiquetes de bucle heterogènies a L3** | **Decisió de l'usuari (2026-09-23): no es toca el codi; es documenta la convenció.** L'entrada les tractava com una desviació del patró dominant `for:`/`fifor:`, però **el numeratge és necessari, no estilístic**: els quatre (`for1:`/`ffor1:`/`for2:`/`ffor2:`) són **al mateix bloc de codi** (`L3.qmd:349-433`, mesurat a `ebdf055`; la solució de `s3_4_2.s`), on `moda` té dos bucles consecutius —la inicialització de l'histograma i el recorregut de la cadena—. Renombrar-los a `for:`/`fifor:` hi duplicaria etiquetes i el fragment **no assemblaria**. S'afegeix la regla a `13_contrib.qmd §T2 i T3 → Etiquetes de bucle` | ⚠️ **El patró «dominant» no tenia precedent per a aquest cas**: `L3.qmd` és **l'únic fitxer del corpus amb dos bucles al mateix bloc** (`git grep -lE "^for1:"` → només L3); els 18 `fifor:` i 13 `for:` són tots de blocs amb un sol bucle, on no hi ha res a desambiguar. De passada es fixa una segona cosa que divergia i que ningú no havia mesurat: el prefix de sortida és **`fi-`** (18 `fifor:` + 12 `fibucle:` + 2 `fiwhile:` = 32) contra 4 `fwhile:`; la regla de `13_contrib.qmd:122` ja deia `fiwhile:` i ara ho diu explícitament |
| **`fwhile:` → `fiwhile:` al laboratori** | **Decisió i execució de l'usuari (2026-09-23).** El prefix de sortida de bucle divergia amb un repartiment net —teoria `fiwhile:`, laboratori `fwhile:`— i es resol a favor de la forma majoritària, que és la que fixa `13_contrib.qmd:122`. **8 substitucions**: `L3.qmd` 6 i `L5.qmd` 2 | ⚠️ **No eren 4 sinó 8**: l'entrada comptava les **definicions** d'etiqueta (`L3.qmd:229`, `:543`, `:625`, `L5.qmd:267`) i cada una té el seu **salt** que hi apunta (`beqz t0, fwhile`, `blt t0, zero, fwhile`). Canviar només les definicions hauria deixat quatre salts a una etiqueta inexistent i els fragments no haurien assemblat. De passada es reajusta l'alineació dels comentaris de `L3.qmd:221` i `L5.qmd:263`, que `fiwhile` (dos caràcters més llarg) havia desplaçat una columna respecte de les línies veïnes. Verificat: cap `fwhile` al corpus i cap `@ref` no apuntava a aquestes etiquetes |
| **L3 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L3.qmd` de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C executada en tres commits del **2026-09-20** (`f136762`, `c52538a`, `7f0703c`) i, després, **sis correccions puntuals per exercici** (`b6c8124`, `8b9f82d`, `01fff2d`, `afdc884`, `eb3f856`, `6ee1a8a`) —l'ítem amb més activitat posterior dels quinze, tot i que cap d'aquelles no és una passada de revisió—. El registre declarava només **Fase B**, perquè es va escriure el 2026-07-19, dos mesos abans de la Fase C | **Les tres entrades que citaven `L3.qmd` s'han resolt el mateix dia del tancament**, totes tres amb fila pròpia en aquesta taula: `exr-moda` (l'enunciat no deia què contenia `s3_4_2.md`), les **etiquetes de bucle numerades** (documentades com a convenció a `13_contrib.qmd`, el codi no es toca) i **`fwhile:` → `fiwhile:`**. `L3.qmd` **no té cap marcador viu** ni cap entrada específica. Hi aterraran dues escombrades transversals pendents: el **canvi de criteri de `_start`/`.section`** (15 ocurrències de `_start`, 5 `.globl`) i les **cometes rectes → «»** (3 línies). → La primera ja és **executada** (fila «`_start` surt del codi»); la de les cometes segueix viva a §Tasques transversals |
| **L4 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat, i amb ell el cas crític de les passades finals.** ⚠️ `3cae913` (2026-07-21) és **l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu literalment «**pre passades finals**»; el registre declarava només **Fase B**. Era l'ítem que va motivar l'entrada «Passades finals pendents» i el motiu pel qual no es podia donar el laboratori per revisat sense mirar-s'hi. En tancar-lo, l'usuari **dona per cobertes aquelles passades** | **La Fase C sí que es va executar**, encara que ni l'assumpte ni el registre ho diguin: el Bloc 4c en va verificar al corpus els ítems crítics A1 i A2 (cap `.space` ni cap `li` amb expressió aritmètica, `_start` primera etiqueta dels tres blocs `.text`) i sis de la secció C (`NB`→$T$, la fórmula harmonitzada amb `@mat[0][0]`, la nota de `t4`, «offset»→«desplaçament», «*breakpoint*»→«punt d'aturada», «secció»→«segment `.data`»). `L4.qmd` **no té cap marcador viu** ni cap entrada específica. Les tres troballes transversals del seu registre (D3 punt d'entrada de RARS, D4 símbols `NF`/`NC`/$T$/*stride* al glossari, D5 etiquetes de bucle) són o segueixen sent entrades d'aquest fitxer; **D5 es va resoldre el mateix dia**. → **D3 és executada** (2026-09-24): vegeu la fila «Punt d'entrada de RARS» d'aquesta taula. La fila de L4 de la taula de «Passades finals pendents» queda marcada com a tancada |
| **L5 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L5.qmd` de `CLAUDE.md §Estat dels materials`. ⚠️ **És l'únic dels quinze ítems amb la passada final efectivament feta i declarada per les dues bandes**: l'historial mostra el cicle complet (`a83dc16` «TODO darreres passades» → `b5ca2f4` «**tres passades fetes**», 2026-07-21) i el registre ho confirma amb detall («Fase A, B i C completades» + «**Revisió final en 3 passades: completada**», feta en un xat separat). La Fase B va incloure simulació RV32I amb 100 010 casos de prova per a `descompon` | El **model del que és una passada final surt precisament de L5** (`git show 980434b:26_prompts/Lx__revisio_interna__plantilla.md`, línia 52: «contrast ISA oficial, comparació didàctica L4/L5/L6, lingüística dedicada»), i és el que l'entrada «Passades finals pendents» cita com a referència. `L5.qmd` **no té cap marcador viu** ni cap entrada específica; l'únic pendent que hi tocava, `fwhile:` → `fiwhile:` (1 ocurrència), es va executar el mateix dia. Amb aquest tancament, **els sis ítems de la taula de «Passades finals pendents» són tancats** i aquella taula passa a ser registre històric |
| **L6 · Tipografia d'UI de RARS** | **Executada (2026-09-23), just abans de tancar L6.** `L6.qmd` marcava els elements d'interfície de RARS en **negreta** mentre que L4 i L5 usen **cursiva** —harmonitzada a la revisió interna de L5 (2026-07-20)— d'acord amb `13_contrib.qmd §Codi, matemàtiques i cursiva`. **35 substitucions** en 26 línies: 19 `Data Cache Simulator`, 5 `Tools → …`, i `Set size`, `Number of blocks = N`, `Reset`, `Runtime Log`, `Connect to Program`, `Fully Associative`, `Cache` | ⚠️ **No eren 22 sinó 35**: l'entrada n'havia comptat una part. Es va inventariar **totes** les negretes del fitxer i separar-ne les d'UI de les legítimes —títols d'apartat, geometries (`32 blocs de 4 paraules`), conceptes (`cold-start`, `conflicte`, `capacitat`)—, que **no s'han tocat**. Tres casos dubtosos resolts mirant-ne el context i el precedent de L4/L5: `Cache` és el nom d'un panell (`:465`), i `Set size = 4` / `Number of blocks = 64` són camps amb el seu valor (`:767`). Verificat que les 5 seqüències `***…***` del fitxer són les d'anglicismes en negreta cursiva i segueixen intactes |
| **L6 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat, i amb ell la revisió interna de tot el laboratori.** Estat que tenia en tancar-se: el registre declarava «Fase A, B i **C: completades**» i «**Pendent: res propi de L6**», amb les troballes cross-file derivades al `TODO.md`. **Cap passada posterior.** La Fase B va incloure verificació empírica amb **RARS 1.6 headless** contra el codi font del `CacheSimulator`, més simulació Python de la cau | ⚠️ **L'assumpte del seu únic commit enganya**: `ca6c01a` es diu «L6 Fase B» i **conté la Fase C sencera** —toca els quatre fitxers que el registre llista i els seus ítems es verifiquen al corpus—. L'avís es conserva a `CLAUDE.md §Estat dels materials` perquè descriu l'historial i seguirà despistant qui el llegeixi. `L6.qmd` **no té cap marcador viu**; l'única entrada que li era específica, la tipografia d'UI, s'ha executat al mateix commit (fila anterior) |
| **P3 — matís del `mul` mòdul $2^n$** (decisió heretada de la revisió interna d'A1, 2026-07-11; ítem 3 del registre de T4) | **Executada**: el callout `#wrn-mul-modul-2n` és a `A4.qmd:323`, just després de `#tip-sobreeiximent-multiplicacio` i abans de `## Divisió entera`, amb el text exacte que proposava el registre; `S4.qmd:214` l'hi referencia amb `@wrn-mul-modul-2n` | ⚠️ **La cadena de rastre estava trencada pels dos extrems i per això es deixa aquesta fila**: l'entrada P3 d'aquest fitxer es va retirar el 2026-07-12 cedint la propietat del pendent al registre de T4, i el registre es va esborrar el 2026-09-22 (`4bfb43c`). El detall —anàlisi, opcions i text del callout— és a `git show a211bbf:TODO/T4_P_tasques.md §3` |
| **`_start` surt del codi i només es presenta a teoria** (**CANVI DE CRITERI, usuari, 2026-09-23**; entrada de §Tasques transversals, retirada el 2026-09-25) | **Executada (2026-09-24)** en quatre commits: `b2c1a4f` inverteix la regla a `13_contrib.qmd` (avui `§Convencions globals del laboratori`, `:207`: «El punt d'entrada no porta etiqueta»); `d51577d` reancora l'arnès de laboratoris a la sortida del programa i en retira la comprovació estàtica E1; `b362576` treu `_start` del corpus i afegeix el callout `@nte-punt-entrada-etiqueta` a `A3.qmd` (`A3.qmd:1890`, dins de `@sec-compilacio-separada`); `edc2a5f` corregeix el recompte posterior («en queden 3, no zero»). Les tres parts de l'entrada —(i) callout a teoria, (ii) treure les etiquetes `_start`, (iii) treure les línies `.globl _start` **conservant les sis que exporten símbols reals**— són fetes. §Dades preservades, on `_start`/`__start` és contingut històric, **no s'ha tocat**, com l'entrada demanava | **Invariant que ha de seguir valent** (mesurat a `ebdf055`, amb `X=("--" "*.qmd" ":!TODO.md" ":!13_contrib.qmd")`): `git grep -o "_start" "${X[@]}" \| wc -l` → **3** (el callout d'`A3.qmd`, prosa: `:1890` i dues a `:1892`); `git grep -cE "^_start:" "${X[@]}"` → **0**; `git grep -cE "^\s*\.globl" "${X[@]}"` → **6** línies (`suma`, `abs`, `compon`, `descompon`, `g`, `X`, que s'han de mantenir); `git grep -cE "^\s*\.globl\s+_start" "${X[@]}"` → **0** (les tres darreres, sumades amb `awk -F: '{s+=$2} END{print s+0}'`). **3 · 0 · 6 · 0**: quatre formes diferents —ocurrències, definicions, línies `.globl` de qualsevol símbol, línies `.globl _start`—, que l'entrada va confondre dues vegades. Abans del canvi, a `d51577d` (l'`awk` llegeix `$3`): 96 · 26 · 32 · 26, amb les 96 repartides `L5` 27 · `L4` 19 · `L3` 16 · `L6` 14 · `L2` 8 · `L1` 8 · `A2` 2 · `E9` 1 · `A3` 1 (suma 96). ⚠️ L'entrada deia que `.globl main` «només surt a `13_contrib.qmd:898`»: a `ebdf055` surt a `13_contrib.qmd:215`, `:220`, `:221` i `:1003`, totes en prosa o en ordres d'exemple, i al corpus no n'hi ha cap (`git grep -c "\.globl main" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'` → cap). Text sencer, amb les ordres i les correccions de xifra que va patir: `git show ebdf055:TODO.md` |
| **`.section` a teoria com a forma de GNU** (usuari, 2026-09-23; entrada de §Tasques transversals, retirada el 2026-09-25) | **Executada (2026-09-24) a `5514d08`.** El paràgraf «Forma llarga de la directiva» és al **cos visible** de `#nte-segments-memoria` (`A2.qmd:400`, `@sec-programa-segments`), no al `#wrn-segments-elf` que es proposava com a candidat: **decisió de l'usuari, ferma (2026-09-24)**, perquè aquell callout és `collapse=true` i `.section` es presenta conjuntament amb els segments de memòria, on l'alumne aprèn què és una directiva de segment. `#wrn-segments-elf` es queda amb `.rodata` i `.bss`; la fila `.section` de `21_riscv/RARS_directives.qmd` remet ara a `@sec-programa-segments` en lloc de `13_contrib.qmd`. Segueix el patró d'`A9.qmd:399-402`, exemple declarat il·lustratiu i no executable | ⚠️ **Invariant viu sense cap altra còpia** fora d'aquesta fila i del missatge de `5514d08`: **cap `.section` dins de cap bloc plegat a `01_apunts/`**. Es mesura per forma, no per línia: recorrent l'aniuament dels divs `:::` —una obertura amb atributs obre un nivell, marcat si porta `collapse`; una tanca nua en tanca un— i comprovant que cap línia amb `.section` no és dins d'un nivell marcat. A `ebdf055` en surten tres, **totes visibles**: `A2.qmd:400` (el paràgraf nou), `A9.qmd:399` i `:402` (l'exemple il·lustratiu de la RSE). **La intenció pedagògica no es va abandonar**: el que es va retirar és la conversió dels 121 fragments (§Canvi de criteri `.section`), no l'explicació. Text sencer: `git show ebdf055:TODO.md` |
| **Punt d'entrada de RARS: cap material no l'explicava a l'alumne** (entrada de §Laboratori, retirada el 2026-09-25; origen `TODO/L4_tasques.md` D3(ii), `git show a211bbf:TODO/L4_tasques.md`) | **Executada (2026-09-24) per separació, no per duplicació.** El fet general —RARS comença a la primera instrucció de `.text`, el punt d'entrada no porta etiqueta i el programa principal va abans de les subrutines— és a `A2.qmd §Segments`, al cos visible de `#nte-segments-memoria`, més una línia a `@nte-programa-esquelet` que hi remet (`5514d08`). El que és propi de L5 —l'ordre de la pestanya activa en assemblar diversos fitxers, i el diagnòstic— és a `@nte-rars-ordre-assemblatge` (`d6fb588`), amb els bolcats traslladats a la solució (`ebdf055`). Aquell callout passa de `#wrn-` (*Aprofundiment*, no avaluable, plegat) a `#nte-rars-` (avaluable, visible): **el canvi d'avaluabilitat és volgut (decisió de l'usuari, 2026-09-24)**, perquè l'ordre de la pestanya és al camí normal de l'exercici i, si és la dolenta, el programa no arrenca | Cap pendent. **La proposta original (un `#nte-` a L1) es va descartar amb motiu**: `@nte-programa-esquelet` és la lectura prèvia obligatòria de L1, de manera que la línia afegida a l'esquelet ja hi arriba; duplicar-ho hauria creat una tercera còpia del mateix fet. ⚠️ **La premissa de l'entrada era falsa des d'abans per un error de mesura** (regla 2): `L5.qmd` ja ho explicava («segment `.text` combinat») i la verificació buscava la frase literal. L'ordre per forma, `git grep -n "primera instrucció del segment" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'`, dona a `ebdf055` **cinc** ocurrències: `A2.qmd:398`, `A3.qmd:1894` i `:2054`, `E9.qmd:72`, `L5.qmd:55`. Text sencer: `git show ebdf055:TODO.md` |
| **`.gitignore`: `*.tex` s'empassaria `preamble.tex`** (entrada de §Tasques globals → Eines, retirada el 2026-09-25) | **Executada (2026-09-25) per decisió de l'usuari: excepció pel nom.** `.gitignore:15` diu `!preamble.tex`, just després del `*.tex` de `:14`. Es descarta l'alternativa de restringir `*.tex` a l'artefacte generat perquè el patró general és el que atrapa els `.tex` que Quarto genera amb un títol anterior: `Estructura-de-comput.tex`, del 2026-09-22, n'era un a l'arrel, i s'ha esborrat en la mateixa neteja. Comprovació, sense l'índex perquè `preamble.tex` és versionat: `git check-ignore --no-index -v preamble.tex` → `.gitignore:15:!preamble.tex`; `git check-ignore --no-index -v prova.tex` → `.gitignore:14:*.tex` | Cap pendent. Text sencer de l'entrada: `git show 043b985:TODO.md` |
| **Passades finals pendents: la Fase C no és el tancament de la revisió interna** (entrada de §Tasques transversals, del 2026-09-23; retirada el 2026-10-01) | **Retirada perquè es compleix la condició de retirada que ella mateixa fixava**: «es retirarà quan la revisió interna sigui tancada del tot». El 2026-09-25 no es complia perquè `CLAUDE.md` deixava 16 fitxers E/S pendents del pas combinat. El 2026-10-01 l'usuari declara: «les revisions internes es poden donar per acabades». L'historial ho sosté: els nou registres de tema (`git show a211bbf:TODO/T<x>_P_tasques.md`) ja tenien E i S com a abast, i la línia del pas combinat era del 2026-06-19 (`879f3e7`), sense actualitzar des del juliol | La taula de commits que declaraven les passades (T1 `f5e8223` i `9de6756`, T2 `31f7571`, T4 `9faab05`, T6 `77853ff`, L4 `3cae913`, L5 `a83dc16` → `b5ca2f4`), tots tancats el 2026-09-23, i el text sencer: `git show 980434b:TODO.md`. La definició de l'etapa (Fase C ≠ tancament; el tancament és una declaració) queda a `CLAUDE.md §Estat dels materials` |
| **Terminologia anglesa a la prosa d'E/S** (entrada de §Tasques transversals, registrada i retirada el 2026-10-01; era l'antiga «tasca prèvia opcional» de `CLAUDE.md`, `879f3e7`) | **Executada (2026-10-01): 27 substitucions en 9 fitxers**, segons `13_contrib.qmd §Substitucions obligatòries`: *string* → «cadena de caràcters» (o «cadena», a E2, que en parla sovint), *padding* → «**farciment** (*padding*)» la primera vegada i després «farciment», *offset* → «desplaçament», *jump table* → «taula de salts» després de la primera aparició, *overflow*/*underflow* → «sobreeiximent»/«subdesbordament» a `E5.qmd:177`, que són els termes d'A5. A `S7.qmd:64-66`, «desplaçament» segons el criteri que A7 fa servir a la prosa; les fórmules de S7 conserven $\text{offset}$, com les d'A7. ⚠️ **La classificació publicada en registrar l'entrada era incompleta**: comptava les cel·les de taula com a «codi o atributs» i acceptava qualsevol cursiva com a primera aparició. N'hi havia **11 més**: 6 en taules (`S2.qmd:310`, `S3.qmd:621`, `S5.qmd:751` i tres a `S_criteris_seleccio.qmd`) i 5 en cursiva sense el terme català al davant (`E5.qmd:177` dues, `S2.qmd:308`, `S3.qmd:246`, `:279`, `S7.qmd:432`) | De 99 ocurrències en queden 73, i cap no és feina d'aquesta entrada: 33 identificadors, 18 de codi, 4 de fórmules, 6 cursives en la forma admesa («sobreeiximent (*overflow*)», «taula de salts (*jump table*)») i **12 «branch» a E6/S6**, que són de l'entrada de §T6. Ordre: `25_scripts/escombrada.sh -w 'hardware\|software\|cache\|offset\|overflow\|underflow\|branch\|jump\|string\|padding\|aliasing\|event' -- 02_exercicis 03_solucions` (dins de la taula, cada `\|` és una barra escapada), que dona 73. Text sencer de l'entrada: `git show da35dfe:TODO.md` |
| **Criteri «quatre formats nuclears d'instrucció» (RISC-V International)** (entrada de §Tasques globals → Contingut global, adoptat a la revisió interna de T2, 2026-07; retirada el 2026-10-01) | **Executada per mesura, sense cap canvi al corpus.** L'entrada demanava ajustar els fitxers que donessin un total de formats («sis formats», «6 formats»). Avui no n'hi ha cap: només `A2.qmd:260` en dona un recompte, i és el bo. La resta són llistes de lletres (`registres.toml`, `gen_regs.py:410`, `A2.qmd:280`) que no afirmen cap total. Patró per forma, sobre tot el versionat amb A3–A6 i sense: `git grep -n -i -E "(un\|dos\|tres\|quatre\|cinc\|sis\|set\|[0-9]+) (formats\|tipus de format)"`, més les llistes `R, I, S` i `R/I/S` (a la taula, les `\|` són barres escapades). ⚠️ **El criteri no era a `13_contrib.qmd`**, només en aquesta entrada i al text d'A2: retirar-la sense moure'l n'hauria perdut l'única còpia normativa. Ara és a `13_contrib.qmd §Decisions per tema → T2 i T3` | La revisió qualitativa d'A3 (com presenta B, J i U) és a l'entrada de `§T3`, que espera el port de `!5`. Text sencer: `git show 4a33a74:TODO.md` |
| **Expressions aritmètiques als operands: escombrada pendent de `Ex`/`Sx`/`11_riscv.qmd`** (entrada de §Tasques per tema → Laboratori; retirada el 2026-10-01) | **Executada per mesura, sense cap canvi.** La regla (`13_contrib.qmd §Convencions globals del laboratori`) admet expressions a teoria, problemes i exàmens, i només exigeix el literal al laboratori. Mesurat a `b2530c7`: **34 línies** d'assemblador amb un operador aritmètic als operands a `02_exercicis`, `03_solucions`, `11_riscv.qmd` i `21_riscv/`. **27 són de `S4.qmd`**, que l'entrada mateixa excloïa («A4 i S4 [...] no es toquen»). Les 7 restants són enunciats i solucions de problemes: `E2.qmd:73`, `:411`; `E3.qmd:282`; `E4.qmd:375`, `:376`; `S2.qmd:445`, `:630`. Cap no demana executar el codi a RARS, i `E2.qmd:73`, `S2.qmd:445` i `:630` ja porten la nota que a RARS cal `la` + `addi`. `11_riscv.qmd` i `21_riscv/`: cap. ⚠️ **Una primera escombrada en va trobar 32, no 34**: filtrava els blocs per `{.s` i se saltava el d'`E4.qmd:368`, que obre amb una tanca ` ```s ` nua. D'aquí ve l'entrada «Tanques de codi fora de la convenció», de §Tasques transversals | Cap pendent. Ordre que dona 34: `git grep -n -E '^\s*([A-Za-z_]\w*:\s*)?(la\|li\|addi\|\.set\|\.space\|\.word\|\.eqv)\s+[^#]*([A-Za-z_0-9)]\s*([*/+]\|<<\|>>)\|[A-Za-z_)]\s*-)\s*[A-Za-z_0-9(]' -- 02_exercicis 03_solucions 11_riscv.qmd 21_riscv` (dins de la taula, cada `\|` és una barra escapada). Text sencer: `git show b2530c7:TODO.md` |
| **Grafia «No associativitat» vs «No-associativitat»** (entrada de §Tasques transversals, detectada 2026-09-20; retirada el 2026-10-01) | **Executada (2026-10-01). Decisió de l'usuari: amb guionet**, la forma que l'IEC fixa per a *no* davant d'un nom. El corpus ja era unànime (`A5.qmd:693`, `:719`; `E5.qmd:204`; `S5.qmd:908`, `:911`, `:989`; `S_criteris_seleccio.qmd:89`, `:90`), i l'única forma divergent era la de la convenció, `13_contrib.qmd:160`, que s'ha corregit. La regla general és ara a `13_contrib.qmd §Criteris generals` («No» davant d'un nom). No ha calgut tocar A5 | Cap pendent. `git grep -n -i -E "no (associativ\|distributiv)" -- . ':!TODO.md'` → cap (dins de la taula, cada `\|` és una barra escapada) |
| **Homogeneïtzació del format de les adreces** (entrada de §Tasques transversals, usuari, 2026-09-23; retirada el 2026-10-01) | **Executada (2026-10-01).** Dels tres aspectes, dos ja estaven resolts: separadors (regla i corpus net) i majúscules (regla permissiva, que no demana unificar). El tercer, l'**amplada**, l'ha decidit l'usuari: **8 dígits per als valors de 32 bits** (adreces, contingut de registres, codificacions), i la resta segons l'amplada del seu rol. La regla és a `13_contrib.qmd §Criteris generals`. Mesurat a `c1bac38`, fora d'A3–A6: els **61 hexadecimals de 5 a 7 dígits** són tots camps, valors o màscares, i cap no és una adreça escurçada: immediats de `lui`/`auipc` de 20 bits (A2, S2), números de bloc i etiquetes de memòria cau (A7, L6), números de pàgina de 20 bits (els 27 d'A8) i màscares de mantissa (L5). On el corpus mostra el contingut d'un registre, ja ho feia amb 8 dígits (`A2.qmd:1394-1421`, `S2.qmd:217`). **Tres canvis**: els comentaris `t1 <- 0x43` i `t2 <- 0x4142` d'`A2.qmd:1087-1088`, a la part correcta d'un bloc de codi deliberadament erroni (les errades són a L14 i L15), i l'adreça `0x100` d'`A1.qmd:267`. A A3–A6 no hi ha res a canviar: A3 només té immediats d'`auipc`, i A5 ho té tot amb 8 dígits | 📌 **Cas límit, deixat com era: les adreces abstractes dels problemes de memòria cau.** `E7.qmd` (`exr-t7-fallades-programa`) i `S7.qmd:401` diuen «a partir de l'adreça `0`», `0x400`, `0x600` i `0x000`–`0x7FF` sense fixar l'amplada de l'adreça, perquè el problema només necessita els índexs de bloc. S'han tractat com a notació pròpia del problema, igual que `0x39` a E7, que és d'una memòria de 64 bytes. Si s'hi vol aplicar la regla, són aquestes línies. Text sencer de l'entrada: `git show c1bac38:TODO.md` |

### Caduques per mesura

| Entrada | Comprovació que la retira |
| :--- | :--- |
| **A1. Slugs `{#sec-}` a T1, T2 i T5** | Mesurat **per forma**, excloent capçaleres dins de callouts (que l'entrada ja exceptuava): **cap** capçalera `##`–`####` sense etiqueta a **cap dels nou fitxers `A1`–`A9`** — més fort que l'abast de l'entrada, que només parlava de T1, T2 i T5. Coherent amb `CLAUDE.md`, que declara A1–A9 «complet». ⚠️ **Avís per a qui la refaci**: les capçaleres `##` dins d'un callout són títols, no capçaleres de document, i s'han d'excloure. Un comptador que segueixi els `:::` amb un *toggle* es descompensa amb els callouts encastats, que obren amb `::::`: cal comptar **nivells**, normalitzant la tanca amb `lstrip(':')`, no alternar un booleà. Mesura correcta, que dona **0** als nou fitxers: vegeu §Mesura dels slugs, al final |
| **A2. Identificador duplicat `sec-opt-acces-sequencial`** | `git grep -n "{#sec-opt-acces-sequencial}" -- '*.qmd' ':!TODO.md'` → **una sola definició** (`A4.qmd:681`). Les altres 6 ocurrències són referències `@` |
| **A3. Div sense tancar a `A7.qmd`** | 122 obertures `::: {` i 122 tancaments nus. `make render` de la sessió 2: **cap warning** |
| **A4. Referències creuades no resoltes** | Cap de les cinc existeix al corpus: `@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila`, `@imp-exception-handler`, `@sec-politica-reemplacement` → `git grep` sense cap ocurrència |
| **«ample de banda» → «amplada de banda»** | Única ocurrència a tot el corpus: `13_contrib.qmd:347` (mesurat a `ebdf055`; era `:324`), que **és la regla de substitució mateixa** |
| **Unitats KB/KiB** | 5 ocurrències de `KB`, **totes definitòries**: `A2.qmd:171,178` (la taula que defineix el criteri) i `13_contrib.qmd:289,368` (la convenció; mesurat a `ebdf055`, eren `:266,345`) |
| **`****` sobrants** | `git grep -n '\*\*\*\*' -- '*.qmd' ':!TODO.md'` → **cap** |

### Duplicades

| Entrada | Canònica |
| :--- | :--- |
| T3 — «quatre formats nuclears» | `§Contingut global`; la de T3 n'és el subconjunt i s'hi ha deixat com a remissió |
| T4 ítem 8 (figures half/full-adder) | `§Decisions obertes`, entrada dels marcadors `A4.qmd:80,81` |
| T3 T34 (`#cau-boolea-c`) | `§T3` |
| T7 C3, D1, D2, D3 | `§T7` |
| T6 C6 (etiquetes de classe) | `§T6` |

### Canvi de criteri `.section` — retirat per l'experiment (2026-09-23)

**Entrada retirada de `§Decisions obertes`.** La proposta (usuari, 2026-09-23)
era fer `.section` obligatòria a tots els fragments d'assemblador
(`.section .data`, `.section .text`) en lloc de les formes nues, amb un abast
mesurat de **121 directives** convertibles (126 menys les 5 d'A4–A6, exclosos
per la revisió externa). El seu punt (iii) deia: «comprovar que RARS accepta la
forma llarga en tots els casos, **abans** de convertir res». Era un tall, i ha
tallat.

**Veredicte: RARS 1.6 no admet la forma llarga. El canvi no s'adopta**, i les
121 directives nues es queden com són.

#### Formes provades i veredicte de cadascuna

| Forma | Assembla? | Què fa realment |
| :--- | :---: | :--- |
| `.section .data`, `.section .text` | ❌ | Error dur: `.section must be followed by a section name` |
| `.section .rodata`, `.section .sdata` | ✅ | **No commuta de segment, i descarta tot el que la segueix** (vegeu sota) |
| `.section .bss`, `.section data`, `.section .foo`, `.section ".data"` | ⚠️ | Avís `section name "X" is ignored`; la directiva no fa res i l'assemblador es queda on era |
| `.section .data.x`, `.section .text.trap, "ax"` | ✅ | Assembla; és la forma d'`A9.qmd:402`, declarada il·lustrativa i no executable |
| `.rodata`, `.bss`, `.sdata` (nues, sense `.section`) | ⚠️ | `RARS does not recognize the .rodata directive. Ignored.` |

#### El mecanisme

**`.section` no commuta al segment equivocat: no commuta gens**, i l'assemblador
es queda al segment on ja era. El cas que ho aïlla és `.section .bss`, que dona
dos missatges alhora:

```
.section .bss
x: .word 1
→ Warning: section name ".bss" is ignored
→ Error: ".word" directive cannot appear in text segment
```

L'error diu **text** perquè, ignorada la directiva, l'assemblador seguia al
segment per defecte; no té res a veure amb `.bss`. Es confirma posant-hi
`.data` al davant: **el mateix `.section .bss` no dona cap error** i la dada
cau a `0x10010000`.

La causa de l'error dur de `.data`/`.text` és l'analitzador lèxic: totes dues
són *tokens* de directiva i, darrere de `.section`, es consumeixen com a
directiva pròpia sense arribar-hi mai com a operand. Cap grafia no hi arriba
—tabulador, doble espai, `.SECTION`, `.DATA`, cometes—.

⚠️ **El cas greu: les formes acceptades descarten codi en silenci.** Amb un nom
que RARS reconeix (`.rodata`, `.sdata`), les instruccions posteriors a la
directiva **no s'assemblen enlloc** —ni a `.text`, ni a `.data`, ni a cap
adreça—. Quatre instruccions queden en una, sense cap error ni avís, i el
programa acaba «dropped off the bottom». **No es desen al lloc equivocat:
desapareixen.** El bolcat de `.data` del mateix programa respon «This segment
has not been written to, there is nothing to dump», cosa que descarta la
hipòtesi natural —que acabin com a dades— i tanca la recerca. La inversió és contraintuïtiva i val
la pena retenir-la: **`.section .foo`, que no es reconeix, és la forma segura**
(avisa i conserva les quatre instruccions); les reconegudes són les perilloses.

#### Com reproduir-ho

RARS **no és al repositori** i no s'hi ha de versionar (vegeu
`13_contrib.qmd §Verificació empírica a RARS`, que en descriu el procediment).

```bash
cd "$(mktemp -d)"
curl -sSLO https://github.com/TheThirdOne/rars/releases/download/v1.6/rars1_6.jar
sha256sum rars1_6.jar   # 780f730eb457b1ba609e968accc2c8b77d8f92c3d9dbf30cc7fdb3cfb14e8c24

# 1. L'error dur de la forma que el canvi proposava
printf '.section .data
x: .word 1
' > t1.s
java -jar rars1_6.jar nc t1.s            # → .section must be followed by a section name

# 2. No commuta de segment: les dues dades queden contigües
printf '.data
a: .word 0xAA
.section .rodata
b: .word 0xBB
.text
 la t0,a
 la t1,b
 li a7,10
 ecall
' > t2.s
java -jar rars1_6.jar nc t2.s t0 t1      # → t0=0x10010000, t1=0x10010004

# 3. Descarta el codi posterior: 4 instruccions → 1 paraula al bolcat
printf '.text
 li t0,0x77
.section .rodata
 li t1,0x88
 li a7,10
 ecall
' > t3.s
java -jar rars1_6.jar nc a t3.s dump .text HexText /dev/stdout   # → només 07700293
java -jar rars1_6.jar nc a t3.s dump .data HexText /dev/stdout   # → "has not been written to":
                                                                #   no són a cap segment, desapareixen

# 4. L'assemblador es queda on era (el mateix .bss, amb i sense .data al davant)
printf '.section .bss
x: .word 1
' > t4.s          # → avís + error "text segment"
printf '.data
.section .bss
x: .word 1
' > t5.s   # → només l'avís, cap error
```

Xifres de l'abast, que es conserven per si el criteri es reobre mai amb un
altre simulador: **126** directives nues totals · **121** excloent A4–A6 ·
repartiment `A2` 34 · `E2` 13 · `L6` 12 · `L2` 11 · `L3` 9 · `A3` 9 · `L5` 8 ·
`L1` 8 · `L4` 6 · `S5` 4 · `S9` 2 · `S3` 2 · `E3` 2 · `S2` 1 (suma **121**,
regla 12 bis).

```bash
git grep -oE "^\s*\.(data|text|bss|rodata)\b" -- '*.qmd' ':!TODO.md' | wc -l   # 126
git grep -oE "^\s*\.(data|text|bss|rodata)\b" -- '*.qmd' ':!TODO.md' \
  ':!01_apunts/A4.qmd' ':!01_apunts/A5.qmd' ':!01_apunts/A6.qmd' | wc -l          # 121
```

#### Què en sobreviu

- **El motiu, a les dues regles**: `13_contrib.qmd:132` i `:230` (mesurat a `ebdf055`; era `:208`) deien
  «`.section`: no s'utilitza» sense dir per què. Ara en porten el motiu tècnic,
  datat i verificat, perquè una regla sense motiu convida a reobrir-la.
- **El mètode**, a `13_contrib.qmd §Verificació empírica a RARS`: és la segona
  vegada que una afirmació sobre RARS s'ha hagut de resoldre executant-lo.
- **La intenció pedagògica**, que **no** es retira: presentar `.section` a
  teoria com a forma de GNU. → **Executada a `5514d08`** (2026-09-24): vegeu la
  fila «`.section` a teoria com a forma de GNU» de §Executades.
- `A9.qmd:402` **no es toca**: assembla, i el text ja el declara il·lustratiu.

---

## Dades preservades del bloc eliminat `A2.qmd:744-810`

Aquestes dades **no existien en cap altre lloc del corpus** (`git grep -c "00c000ef" -- . ':!TODO.md' ':!13_contrib.qmd'` → cap) i es van copiar aquí **abans** de la supressió, a la sessió 2. L'exclusió del fitxer de convencions n'amaga **quatre ocurrències en tres línies** (mesurat a `ebdf055`; abans en deia «una sola», a `:918`): `13_contrib.qmd:1023`, que és **l'ordre mateixa escrita dins de la lliçó 8**, `:1080`, la mateixa ordre repetida a la regla 12, i `:1084`, la llista de casos d'aquella regla. És el cas pur de la regla 12, perquè la comprovació es comptava a si mateixa. El «només A2» que aquesta línia publicava abans descrivia l'estat **anterior** a la supressió del bloc `A2.qmd:744-810`; avui, suprimit el bloc, el corpus no en té cap ocurrència. Documenten el mecanisme **exclòs** per la decisió del 2026-07-19 (assignatura, tots els professors): només tenen valor si algú reobre mai aquella decisió.

Bolcat de RARS en carregar un programa amb `startup.s` — les tres primeres instruccions de `.text`:

| Adreça | Codi | Bàsic | Línia font |
| :--- | :--- | :--- | :--- |
| `0x00400000` | `0x00c000ef` | `jal x1, 0x0000000c` | `jal main` |
| `0x00400004` | `0x00a00893` | `addi x17, x0, 10` | `li a7, 10` |
| `0x00400008` | `0x00000073` | `ecall` | `ecall` |

Flux complet documentat: `_start` → `main` → `exit` → `_exit`. RARS emulava `__start` i la syscall `exit` (número 10), però no la funció `exit` de la libc ni `_exit`.

**Són dues versions diferents, i la diferència és el contingut informatiu.** El primer bloc és el `startup.s` **tal com el presentava A2**; el segon és **l'original de RARS**, que fins al 2026-09-22 vivia a `TODO/laboratori/startup.s` i que s'ha copiat aquí en esborrar-lo (es recupera amb `git show 3a3aea6:TODO/laboratori/startup.s`). Difereixen en tres punts, i cap no és accessori:

| | Versió d'A2 | Original de RARS |
| :--- | :--- | :--- |
| Etiqueta | `_start` (`.globl _start`) | **`__start`** (`.globl __start`), amb dos guions baixos |
| Servei d'`ecall` | `li a7, 93` (sortida amb codi de sortida) | **`li a7, 10`** (sortida simple) |
| Codi de retorn | `li a0, 0` explícit | **cap**: no en posa |

L'original és el que documenta **què emulava RARS**: l'etiqueta `__start` i el servei 10. La fila `li a7, 10` de la taula de bolcat de dalt correspon a aquest segon bloc, no al primer.

Versió tal com la presentava `A2.qmd`:

```
.text
.globl _start
_start:
        jal     main

        li      a0, 0       # Valor de retorn de main a a0 (exit code)
        li      a7, 93      # Número de servei a a7; 93 (sortida amb codi de sortida);
                            #   a0 (codi de sortida)
        ecall
```

Original de RARS (contingut literal de `TODO/laboratori/startup.s`, amb tabulacions):

```
###################################
# Standard startup code.  Invokes the routine "main"
# and calls exit() on return from main
.text
.globl __start
__start:
	jal	main

	li	a7, 10		# Service number in register a7; 10 (exit)
	ecall
```

---

## Mesura dels slugs `{#sec-}` a les capçaleres

L'ordre que sosté l'entrada retirada «A1. Slugs `{#sec-}`». Compta **nivells**
de callout en lloc d'alternar un booleà, perquè els callouts encastats obren
amb `::::` i descompensen un *toggle*. Resultat actual: **0 als nou fitxers**.

```bash
python3 - <<'PY'
import re, pathlib, glob
for f in sorted(glob.glob('01_apunts/A*.qmd')):
    niv, mal = 0, []
    for i, l in enumerate(pathlib.Path(f).read_text().split('\n'), 1):
        s = l.strip()
        if s.startswith(':::'):
            cos = s.lstrip(':').strip()
            if cos.startswith('{'): niv += 1
            elif cos == '': niv = max(0, niv - 1)
            continue
        m = re.match(r'^(#{2,4})\s+(.*)$', l)
        if m and niv == 0 and not re.search(r'\{#', m.group(2)):
            mal.append((i, m.group(2)[:60]))
    print(f, len(mal), mal)
PY
```
