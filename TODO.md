# TODO

Tasques pendents i decisions obertes. Ha de quedar buit: cap entrada viva. Cada entrada porta la comprovació que la sosté. Una entrada que es tanca en surt, i l'historial de les parts ja fetes d'una entrada viva, també: tots dos van **literals** a l'arxiu, [`24_specs/arxiu_todo.md`](24_specs/arxiu_todo.md), amb el motiu i on en queda còpia ([D-91](24_specs/registre_de_decisions.md#d-91)). L'arxiu no es llegeix en començar una sessió.

**17 entrades vives** (recompte del 2026-10-10, en retirar de §Tasques globals → Eines «Protocols d'execució dels generadors i de les comprovacions, per nivells», feta; l'historial dels recomptes és a `git log -p TODO.md`, i l'última versió que el portava, a `git show c29b58d:TODO.md`). Una entrada = una vinyeta de primer nivell (`^- `); les vinyetes indentades en són sub-ítems i no compten. Ordre que ho mesura:

```bash
grep -cE '^- ' TODO.md
```

Repartiment: `§Decisions obertes` 4 · `§Tasques transversals` 4 · `§Tasques per tema` 3 · `§Tasques globals` 6 (suma 17, regla 12 bis). Ordre que el mesura, secció per secció:

```bash
awk '/^## /{s=$0} /^- /{c[s]++} END{for(k in c) print c[k], k}' TODO.md
```

---

## Decisions obertes

Decisions pendents de criteri. Un cop preses, han d'aterrar a `13_contrib.qmd`.

- **Branques del remot: les tres revisions externes ja són a `main`, i esborrar les branques és decisió del grup** (registrada el 2026-09-23; retallada el 2026-10-09: el text sencer, amb la fusió de `temes456`, el port de `!5`, les fusions de prova i les mesures de cada moment, és a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). Les branques de revisió d'`origin`:

  | Branca | MR | A `main` | Estat |
  | :--- | :--- | :--- | :--- |
  | `temes456` | `!7`, T4–T6 | `451c3ef`, commit de fusió (2026-10-01) | És ancestre de `main` |
  | `contingut/t3-traduccio` | `!5`, T3 | `ab48732`, port hunk a hunk (2026-10-01) | No n'és ancestre, perquè el port és un commit nou: `git merge-base --is-ancestor` hi dirà «fora» |
  | `tema8` | `!8`, T8 | `80f8946`, commit de fusió de l'usuari (2026-10-06) | **Revisió parcial**, fins a §8.7 exclosa. Es conserva perquè el revisor hi pugui continuar; abans, li convé incorporar-hi `main`. El nom no segueix `revisio/<grup>-t<N>-t<M>` |

  Cap de les tres no s'ha esborrat: és decisió del grup, amb l'etiqueta d'arxiu de `13_contrib.qmd §Convenció de noms de branques`. `build` només és al mirall de GitHub (`6d5d2cf`, sortida de CI) i no s'ha de tocar. L'abast de la revisió externa i les branques per equip (declaracions literals de l'usuari, 2026-10-06) són al registre de decisions, §Historial de l'estat del projecte → Revisió externa, i la finestra de canvis, a [D-65](24_specs/registre_de_decisions.md#d-65). Les branques es mesuren amb `git ls-remote`, dient de quin remot (regla 13 de la skill `escombrada`). Mesura del 2026-10-09, a la tarda: cap branca d'equip, i `tema8` i `temes456` sense cap commit fora de `main`.

  ```bash
  git fetch --prune origin && git ls-remote --heads origin               # contingut/t3-traduccio, main, tema8, temes456 (2026-10-09)
  git rev-list --count origin/main..origin/tema8                         # 0 (2026-10-09)
  git merge-tree --write-tree --name-only origin/main origin/<branca>    # fusió de prova abans de tocar un fitxer que la branca també toca (D-64)
  ```

- **Contingut que la revisió externa de T4–T6 va treure: A6, per a la reunió de coordinació del 2 de novembre** (registrada el 2026-10-06; les dues retirades d'A5, confirmades per l'usuari el 2026-10-07, i la informació recollida per decidir són a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). La fusió de `temes456` (`451c3ef`) va treure de dos exemples d'A6, `#tip-rendiment-avio` i `#tip-rendiment-cpu` (`b7aab9c`, Fernando Agraz, 2026-07-22), la pregunta «Quin té més productivitat?». Hi ha quedat una incoherència: la pregunta és només «Quin té més rendiment?», i la resposta parla també de la productivitat de B. 🗓️ **Per a la reunió de coordinació del 2 de novembre del 2026** (decisió de l'usuari, 2026-10-07; la data, corregida per l'usuari el 2026-10-09: deia «la reunió del grup de treball del 7 de novembre», i és la del dia 2, la mateixa que la de l'entrada «Problemes i solucions…»: «És el dia 2. Confirmat.»). Proposta de Claude Code: tornar a posar la pregunta, per exemple «Quin té més rendiment? I més productivitat?», perquè els exemples són per contrastar les dues coses (els títols diuen «Rendiment i productivitat…»). Alternativa: treure la frase de la productivitat de les respostes.

  ```bash
  git grep -n "productivitat major" -- 01_apunts/A6.qmd   # :39 i :48 (2026-10-09; fins a 5e55cc8, «major productivitat»)
  ```

- **Exemples i solucions plegables a l'HTML** (petició de l'usuari, 2026-10-08, fase 7g: «Fer els exemples dinàmics? És a dir, que per veure la solució calgui prémer un botó. […] I segurament també les solucions dels problemes. A l'HTML es podrien encastar dins mateix dels enunciats»; la valoració inicial de Claude Code, amb les opcions i la recomanació, és a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). ✅ **Pilot de T1 fet** (2026-10-09; decisió de l'usuari: «Fes T1 com a pilot»; [D-90](24_specs/registre_de_decisions.md#d-90)): el filtre `25_scripts/plegables.lua` plega a l'HTML el div `.resposta` dels cinc exemples d'A1 amb el format **Pregunta** → **Solució** → **Resposta**, i afegeix a cadascun dels 15 enunciats de P1 la remissió a la seva solució («Solució 19.1»), a l'HTML i al PDF. **Queda, per decidir en valorar el pilot**: (b) a la resta de temes, que és afegir-los a la taula `PILOT` del filtre, sense tocar cap `.qmd` (P2–P9 i S2–S9 són fora de la revisió externa); (a) a la resta d'exemples amb el format **Pregunta** (A3 2, A6 5 i A7 4; A9 no en té cap), que demana marcar el div a mà, i A2–A8 són als fitxers que revisen els equips (D-65); i l'encastat de la solució dins de l'enunciat, que amb `{{< include >}}` duplicaria els identificadors `#sol-`: caldria un filtre que en copiés el contingut sense l'identificador, o carregar-la des de la pàgina de solucions amb JS. ⚠️ **Trobat en verificar el pilot** (2026-10-09): el títol de les 108 solucions diu «Exemple 19.1: Solució: …» a l'HTML i «Exemple 1: Solució: …» al PDF, perquè són `.callout-tip` i Quarto hi posa el prefix dels exemples; la remissió diu «Solució 19.1» (HTML) o «Solució 1» (PDF), de manera que l'enllaç porta a un bloc que es diu «Exemple». Ja passava abans del pilot amb les remissions `@sol-` entre solucions, però el pilot el fa visible a cada enunciat. Proposta de Claude Code, per decidir amb l'extensió: que el títol digui «Solució 19.1: …» (un filtre o una clau de `language:`, per investigar) i treure el «Solució:» que repeteix cada `## Solució: …`. **La part de les solucions** (estendre la remissió, encastar-les i el títol) es decideix a la reunió de coordinació del 2 de novembre: entrada següent.

  ```bash
  git grep -h -c -E '^:{3,} *\{#tip-' -- 01_apunts | awk '{s+=$1} END{print s}'      # 138 (139 el 2026-10-08; la fase 8a en va suprimir un d'A2)
  git grep -c '@sol-' -- 02_problemes | wc -l                                         # 0 fitxers (les remissions del pilot les genera el filtre)
  git grep -c '{\.resposta}' -- 01_apunts                                            # A1:5
  git grep -c '\*\*Pregunta\*\*' -- 01_apunts                                          # A1 5, A3 2, A6 5, A7 4
  git grep -h -c -E '^:{3,} *\{#sol-' -- 03_solucions | awk '{s+=$1} END{print s}'   # 108
  ```

- **Problemes i solucions: decisions per a la reunió de coordinació del 2 de novembre del 2026** (decisió de l'usuari, 2026-10-09: «Apunta-ho com a decisió que cal prendre a la reunió del 2 de novembre, la propera reunió de coordinació»; són decisions per consensuar amb els col·legues, i l'usuari porta una posició a cada una).

  1. **Solucions encastades sota l'enunciat, a l'HTML** (a partir del pilot de T1, D-90). L'usuari: «La separació entre Apunts i Problemes-Solucions em sembla justificada perquè es pot donar el cas de voler tenir tots dos recursos oberts al mateix temps, però "Problemes" i "Solucions" oberts a l'hora no em sembla un cas d'ús realista. Em sembla que és una decisió que hauré de consensuar amb els meus col·legues.» De les dues opcions de Claude Code, tria l'**(A)**, «Les fonts no canvien»: els fitxers P i S continuen separats, i un filtre encasta cada solució, plegada, sota el seu enunciat a l'HTML; el PDF conserva la part «Solucions» separada, perquè en paper no es pot plegar i imprimir només els enunciats és un ús real. La (B), ajuntar les fonts (un fitxer per tema, i un filtre que mogui les solucions al final del PDF), queda descartada. Per investigar en fer-ho: com treure la part «Solucions» de l'HTML sense duplicar els identificadors `#sol-` (per exemple, amb perfils de Quarto, una llista de capítols per format). Amb l'encastat desapareix el títol «Exemple 19.1: Solució: …» de l'entrada anterior; al laboratori, on el `#sol-` no és un callout, Quarto ja el titula «Solució 29.1».
  2. **Solucions a tots els problemes**, no a una selecció (avui, D-73: «aproximadament un de cada dos o tres»). N'hi ha 108 per a 188 problemes, i en falten 80: T2 17, T3 25, T4 15, T5 8, T7 8, T8 3 i T9 4 (T1 i T6 ja les tenen totes). L'usuari: «Jo soc partidari de fer-ho pq penso que el valor pedagògic d'un problema sense solució és limitat i pq amb Claude ara es solucionen tots.» **Valoració de Claude Code**: a favor. El segon argument també demana una solució oficial i verificada: la que l'estudiant obté d'un assistent pot fallar justament en el que EC ensenya (les convencions de RARS i d'EC, el sobreeiximent en Ca2, les traces de memòria cau). Per a la reunió: si algun problema es reserva per fer-lo a classe o per a l'avaluació (llavors, la solució es pot publicar més tard, amb l'interruptor del punt 3), i qui revisa les solucions noves. Cost: és feina de solucions, Opus amb effort alt (`CLAUDE.md §Model i effort`), amb RARS per al codi; unes quantes sessions, per tema. Si es fa, D-73 canvia.
  3. **Solucions del laboratori**. L'usuari: «Jo soc partidari de fer-ho.» **Fet**: els 43 exercicis del laboratori ja porten la solució al font, just sota l'enunciat (`13_contrib.qmd §Laboratori`, «enunciat en `{#exr-...}` + solució en `{#sol-...}`»), i la versió publicada les mostra sense plegar («Solució 29.1» a L2, comprovat el 2026-10-09 a `rbaig.github.io`). La decisió és, doncs, si la versió dels estudiants les manté i **quan**. Les sessions s'avaluen: el treball previ es lliura abans de la sessió, i la nota es posa durant la pràctica, amb la verificació de les respostes i les preguntes del professor (`index.qmd §Qualificació`); l'avaluació continuada és el 15 % de NL, i NL, el 20 % de NF: el 3 % de la nota final. Amb la solució visible abans de la sessió, el treball previ es pot copiar. **Valoració de Claude Code**: a favor, publicant les de cada sessió quan s'ha avaluat. És un interruptor del render (un filtre que amagui els `#sol-` del laboratori fins a la sessió que es vulgui), i el mateix serviria per als problemes del punt 2. Si es publiquen des del principi, la nota de la sessió descansa en la verificació a la pràctica.
  4. **Quan es publiquen les solucions: un interruptor del render** (recomanació de Claude Code; l'usuari, 2026-10-09: «Apunta-ho a `TODO.md`»). Publicar les solucions de cada sessió del laboratori un cop avaluada, i, si la reunió en reserva algun (punt 2), les dels problemes reservats quan toqui. Proposta d'implementació, per acabar de decidir en fer-ho: un paràmetre del render amb el que ja es pot publicar (l'última sessió avaluada, i els problemes reservats ja alliberats), llegit pel `Makefile` i pel CI de publicació, i un filtre Lua que tregui de l'HTML i del PDF els blocs `#sol-` que encara no toquen. Les remissions que hi apunten han de sortir alhora, o Quarto avisa d'una referència no resolta: les que el pilot afegeix als enunciats (D-90) i les 5 `@sol-` del laboratori (L3 1, L4 1, L6 3). Ha de funcionar abans que la versió dels estudiants es publiqui: avui la versió publicada a `rbaig.github.io` ja mostra totes les solucions. Si la reunió ho aprova, és una sessió curta (Opus, effort mitjà).

  ```bash
  git grep -o -I -E -e '^:{3,} *\{#exr-' -- 02_problemes | wc -l    # 188 (2026-10-09, 6647801): P1 15, P2 31, P3 37, P4 32, P5 22, P6 14, P7 16, P8 10, P9 11
  git grep -o -I -E -e '^:{3,} *\{#sol-' -- 03_solucions | wc -l    # 108: S1 15, S2 14, S3 12, S4 17, S5 14, S6 14, S7 8, S8 7, S9 7
  git grep -o -I -E -e '^:{3,} *\{#sol-' -- 04_laboratori | wc -l   # 43: L1 7, L2 8, L3 6, L4 4, L5 4, L6 14 (i 43 #exr-)
  git grep -o -I -E -e '@sol-' -- 04_laboratori | wc -l               # 5 (2026-10-09): L3 1, L4 1, L6 3, totes a solucions del laboratori
  ```

---

## Tasques transversals

- **Suggeriments de la fase 7g (fase 7i): el que queda** (registrats el 2026-10-08; fets el 2026-10-10 i el 2026-10-11 a la fase 12, `94468b4` i `ada62c7`, amb les decisions de l'usuari sobre la llista de 33 punts amb opcions i recomanació de Claude Code: «Totes les recomanacions acceptades». L'entrada d'abans, sencera, és a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). Hi queda l'únic punt sense recomanació:

  - **Exemples (`#tip-`) avaluables: «Sí» o «Marg.»**. La taula de requadres d'`index.qmd` (`#tbl-requadres-tipus`, a l'HTML i al PDF) diu que els exemples són matèria avaluable («**Sí**»), i la taula de callouts de `13_contrib.qmd §Callouts`, «Marg.» (marginalment). Cal decidir quin és el criteri de l'assignatura i fer que les dues taules diguin el mateix.

  ```bash
  git grep -n -E 'Exemple +\| \*\*Sí\*\*|Groc \| Marg\.' -- index.qmd 13_contrib.qmd
  ```

- **Remissions `@lst-` en lloc de «el codi següent»** (decisió de l'usuari, 2026-10-09: «Decisió, remissions»; abans, decisió oberta: «“El codi següent”: remissions `@lst-`?», petició de l'usuari del 2026-10-08). **Delegada a una sessió nova** (Opus, effort alt), perquè demana investigar el render: al PDF, els blocs amb `filename` ja surten com a flotants numerats («Codi 4.7», pel `codelisting` de LaTeX i `preamble.tex`, D-69), i a l'HTML no, de manera que afegir `#lst-` i `lst-cap` pot donar una numeració diferent als dos formats. Abast, a `6a17af1`: 23 remissions per posició a un bloc de codi (19 «següent(s)» i 4 «anterior»): A2 3, A3 3, A9 1, P2 6, P3 2, P4 1, P7 1, P8 1, L1 1, L2 1, L3 1 i L6 2; cap `#lst-` al corpus. A2 i A3 són a l'abast de la revisió externa: si es fa després de la finestra de canvis, cal avisar-ne els equips. La regla, a `13_contrib.qmd §Referències creuades` amb la seva entrada al registre.

  ```bash
  git grep -c -i -E "(codi|programa|fragment|bloc) (de codi )?(següent|anterior)|(codis|programes|fragments|blocs) (següents|anteriors)" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'   # 23 (6a17af1)
  git grep -c -E '\{#lst-|@lst-' -- '*.qmd'                                                                                                                           # cap
  ```

- **Revisió completa de la norma de lèxic anglès/català** (petició de l'usuari, 2026-10-09: «apunta que cal fer una revisió completa d'aquesta norma»). D-88 (`13_contrib.qmd §Anglicismes i terminologia obligatòria`): si un terme no és a l'Optimot ni al diccionari anglès-català de Softcatalà, es fa servir l'anglès; s'admet l'anglès quan el català és molt poc usat, documentat a la taula de la guia. Cal passar tots els anglicismes del corpus per la regla: els del glossari de termes, que des del 2026-10-09 és l'única font del lèxic ([D-100](24_specs/registre_de_decisions.md#d-100); `12_sigles_simbols.qmd §Termes`, 117 termes i la taula dels que es mantenen en anglès) i els que el corpus fa servir sense traduir (*toolchain*, *stride*, *fetch*, *buffer*, *gap*, *working set*…). Sessió pròpia, amb una llista per terme (Optimot, Softcatalà, ús al corpus, proposta). Afecta A1–A9 i la resta: si es fa després de la finestra de canvis, coordinar-ho amb els equips.

- **Fase 8a: el que queda de la revisió d'A1–A8** (registrada el 2026-10-09, en tancar la fase 8a de `CLAUDE.md §Pla de treball`; l'entrada de les troballes i el que s'hi ha resolt després —la revisió del 2026-10-09 al matí, el %, l'article davant del codi i els dubtes tècnics de les lectures— són a l'arxiu, `24_specs/arxiu_todo.md`, §Entrades retirades → Executades i §Historial retallat de les entrades vives). Hi queda el que demana una decisió de l'usuari o el revisor de T8. Línies del tancament d'aquesta revisió.

  - **Per al revisor de T8** (decisió de l'usuari 10): A8 `#sec-mv-vipt`, «És una condició suficient per evitar l'aliàsing en una memòria cau VIPT, no una equivalència amb la PIPT en tots els aspectes» (`9db74b7`). Amb $N_C \cdot B \le T$, una VIPT tria el mateix conjunt i compara la mateixa etiqueta física que una PIPT de la mateixa geometria: fan els mateixos encerts i les mateixes fallades. Si es volia dir «suficient, però no necessària», ho ha de decidir el revisor. És també al missatge d'obertura de la fase 8.
  - **Majúscula després de dos punts a les definicions** (lectura lingüística d'A7 i A8): «**LRU** (…): Reemplaça…», «**Escriptura immediata** (…): S'escriu…». La guia demana minúscula en explicacions breus i majúscula en frases independents; aquestes són frases completes, i s'han deixat. S'han passat a minúscula els casos clarament breus («**Cas d'encert**: el bloc…», «**Accés 1**: escriptura…»).
  - **No aplicat, de les lectures, per ser preferència o canvi de matís**: A3 «El seu valor ha estat generat per **última vegada ABANS** d'una crida» (`#sec-determinacio-registres-segurs`); A6 «On $t_{exe}$ és…» després d'una fórmula (també A6 «On:», que caldria decidir sistemàticament); A8 «A petició del procés P1» (redundant amb la frase anterior) i «el camp PPN no té validesa».

---

## Tasques per tema

### T3

- **Decisió de contingut a `#cau-boolea-c`** (`A3.qmd:249`, mesurat a `ab48732`, pendent d'Adrià, obert des de la revisió de T3): el text diu que «unes expressions no nul·les s'interpreten com a certes» sense dir **quines**. Cal indicar com s'identifiquen les que sí i les que no. Afecta el rigor tècnic. El marcador segueix al corpus perquè la decisió és viva i no la pot prendre Claude Code.

- **Retocs manuals pendents (Roger) a cinc originals de T3** (des del 2026-10-04; retallada el 2026-10-09: els estats del 2026-10-04 i del 2026-10-07, amb les decisions de l'usuari que hi van portar, són a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). Els esmena l'usuari, perquè també els fa servir per a les diapositives. Quatre es conserven a `22_figs_originals/conservats/` sense que el llibre els consumeixi, perquè A3 en fa servir la versió generada, que ja no té l'error ([D-68](24_specs/registre_de_decisions.md#d-68)); el cinquè, `22_figs_originals/A3_deps_exemple.svg`, és la subfigura (a) de `#fig-deps-exemple`, i l'error surt al llibre fins que s'esmeni.

  - `A3_deps_exemple.svg`: posa fletxes a `a` i `b`, que no travessen cap crida, i hi diu `e = res_g + res_f`, quan el text diu `res_f + res_g`.
  - `A3_ba_exemple.svg`: dibuixa `w` com a `int` de 80 bytes, quan el codi diu `char w[20]` (20 bytes), i rotula `v[0]` la subfranja de `v[17]`.
  - `A3_ba_func.svg`: pinta `w` (`int w[10]`, una variable local) del verd dels registres segurs desats (`#d1e7dd`, 3 ocurrències), i no del blau de les variables locals (`24_specs/svg.md §10`).
  - `A3_pila_uninivell.svg` i `A3_pila_multinivell.svg`: marquen `sp` amb `#cc0000` (6 i 10 ocurrències), el vermell que la paleta reserva a les dependències de dades. Les generades el marquen del color de la zona del cim (`svg.md §9`).

  ```bash
  grep -o -i "d1e7dd" 22_figs_originals/conservats/A3_ba_func.svg | wc -l                                            # 3 (2026-10-07)
  for f in uninivell multinivell; do grep -o "cc0000" 22_figs_originals/conservats/A3_pila_$f.svg | wc -l; done    # 6 i 10 (2026-10-07)
  ```

### T5

- **Figura font única per a les rectes de T5, amb retalls** (registrada el 2026-10-06; era el «TODO futur» de l'entrada «Nova eina disponible: retalls», avui a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades → Executades). `#fig-recta-global` (`A5_recta_global.svg`) i `#fig-recta-zoom-zero` (`A5_recta_zoom_zero.svg`) són dues figures dibuixades per separat, i `24_specs/retalls.toml` no té cap retall definit. Es podria redibuixar una sola figura en estil pla (`24_specs/svg.md`), amb el rang global, el zoom de zero i els denormals, i definir-ne les dues vistes com a retalls (`13_contrib.qmd §Retalls`), si cada retall surt net. Fer-ho sobre les figures actuals ja s'ha descartat dues vegades (motius a l'entrada retirada, `git show 7ac2fc9:TODO.md`). Prioritat baixa, i A5 és a l'abast de la revisió externa.

  ```bash
  grep -c "^\[crops" 24_specs/retalls.toml   # 0 a 7ac2fc9
  ```

---

## Tasques globals

### SVG

- **Vores compartides als originals conservats (Roger)** (registrada el 2026-10-09, en tancar la fase 7h de `CLAUDE.md §Pla de treball`; l'entrada de la fase és a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades → Executades). Les figures que el llibre consumeix ja segueixen `24_specs/svg.md §7` ([D-99](24_specs/registre_de_decisions.md#d-99)); els originals de `22_figs_originals/conservats/`, no, per decisió de l'usuari (2026-10-09, opció (a)): les esmenes que necessitin les fa l'usuari, perquè els fa servir per a les diapositives ([D-68](24_specs/registre_de_decisions.md#d-68)). En són 7, amb almenys una vora compartida per dos `<rect>` amb traç de color diferent, o mig tapada per un farciment: set de T7 (`A7_capacitat_exemple_bucle_primera_passada`, `A7_capacitat_exemple_bucle_segona_passada`, `A7_conflicte_exemple`, `A7_escriptura_estat_inicial`, `A7_escriptura_immediata_amb_assignacio`, `A7_escriptura_immediata_sense_assignacio` i `A7_escriptura_retardada`). Si l'usuari els vol corregir amb la mateixa funció que els natius del llibre, `vores_compartides()` de `25_scripts/figlib.py` ho fa en un pas.

  ```bash
  python3 - <<'PY'   # 12 (2026-10-09)
  import re, glob
  n = 0
  for f in sorted(glob.glob('22_figs_originals/conservats/*.svg')):
      R = [(float(a['x']), float(a['y']), float(a['width']), float(a['height']), a.get('stroke', 'none').lower(), a.get('fill', '').lower())
           for a in (dict(re.findall(r'([\w-]+)="([^"]*)"', m)) for m in re.findall(r'<rect\b([^>]*)>', open(f).read()))
           if 'transform' not in a and all(k in a for k in ('x', 'y', 'width', 'height'))]
      def xoc(p, q):
          (x1, y1, w1, h1, s1, f1), (x2, y2, w2, h2, s2, f2) = p, q
          toca = ((abs(y1 + h1 - y2) < .01 or abs(y2 + h2 - y1) < .01) and min(x1 + w1, x2 + w2) - max(x1, x2) > 1) or \
                 ((abs(x1 + w1 - x2) < .01 or abs(x2 + w2 - x1) < .01) and min(y1 + h1, y2 + h2) - max(y1, y2) > 1)
          if not toca: return False
          if 'none' not in (s1, s2): return s1 != s2
          return (s1 == 'none') != (s2 == 'none') and (f1 if s1 == 'none' else f2) not in ('none', '')
      n += any(xoc(p, q) for i, p in enumerate(R) for q in R[i + 1:])
  print(n)
  PY
  ```

- **Revisió de la paleta de colors per reduir-ne la quantitat** (petició de l'usuari, 2026-10-06, en migrar els colors llegats a la paleta). Després de la migració, la paleta de `24_specs/svg.md §10` i `§16` té 20 colors, i alguns papers es repeteixen amb tons gairebé iguals: dos vermells de traç (`#cc0000`, dependències de dades; `#dc3545`, fallada), dos fons rosats (`#f8d7da`, `.text`; `#f8d0d3`, fallada), dos fons verds (`#d1e7dd`, heap; `#c8ebd8`, encert), dos fons blaus (`#cfe2ff`, `.data`; `#e6f1fb`, zona o contenidor) i cinc grisos (`#f8f9fa`, `#dee2e6`, `#adb5bd`, `#6c757d` i `#343a40`). Cal decidir quins es fusionen i amb quin paper; cada fusió vol dir regenerar o editar les figures que el fan servir (`25_scripts/inventari_figures.py` les llista per color) i retirar-ne l'entrada de §13.

  ```bash
  python3 -c "import re; md=open('24_specs/svg.md').read(); s=md.split('## 10.')[1].split('## 11.')[0]+md.split('## 16.')[1].split('## 17.')[0]; print(len({c.lower() for c in re.findall(r'#[0-9a-fA-F]{6}', s)}))"   # 20, 2026-10-06
  ```

### Contingut global

- **PDF: la numeració de les taules i de les figures als capítols sense número, i el punt després del número** (petició de l'usuari, 2026-10-10: «Sí, apunta-ho a `TODO.md`. Una observació: a `# Presentació` Surt "Taula 1. ", "Taula 2. ", etc.»). Mesurat al PDF de `ccedc54` (574 pàgines, `pdftotext`): (1) Als capítols sense número, la numeració no és la del capítol: la Presentació diu «Taula 1.», «Taula 2.»… (4 taules), sense prefix; i el glossari (`12_sigles_simbols.qmd`), «Taula 6.4.» a «6.8.», com si fossin taules d'un capítol 6 (probablement el comptador del capítol numerat anterior, el laboratori 6, per comprovar). A l'HTML, «Taula 1», «Taula 2»…, sense prefix. (2) A tot el PDF, el número de taula i de figura acaba amb un punt abans dels dos punts: «Taula 2.1.: Prefixos», «Figura 2.2.: Big-endian.» (a la sortida de l'ordre de sota, «Figura N.N.:» 81 vegades, «Taula N.N.:» 21 i «Taula N.:» 4, i només 2 «Figura N.N:» sense el punt; a l'HTML, «Taula 2.1:»). Probablement és l'opció de numeració de KOMA-Script (`scrbook`, `numbers=autoendperiod`: hi posa el punt quan algun número porta lletres, com els d'un apèndix), per comprovar. Cal decidir com han de sortir les taules i les figures dels capítols sense número (sense número, amb un prefix propi, o numerades a part) i treure el punt sobrer. No toca A1–A8: és de `_quarto.yml` o de `preamble.tex`. Sessió: Opus, effort mitjà; `make render-complet` i el PDF mirat.

  ```bash
  pdftotext -layout _book/Estructura-de-computadors.pdf - | grep -o -E "(Taula|Figura) [0-9]+(\.[0-9]+)?\.?:" | sed -E 's/[0-9]+/N/g' | sort | uniq -c   # 81 Figura N.N.:, 2 Figura N.N:, 4 Taula N.:, 21 Taula N.N.: (ccedc54)
  ```

- **Equacions a MathML**: **decisió presa — mantenir MathJax 3**; el pendent és reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa). Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`): funciona (`underbrace`, `cases`, taules amb math correctes a Chrome) i elimina el JS de MathJax (render instantani, offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), numeració d'equacions inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. El desbordament mòbil ja està resolt via CSS.

### Eines

- **Valorar si les taules de `21_riscv/` haurien de passar a `.json` o `.toml`** (petició de l'usuari, 2026-10-02, per al futur). Avui són 44 fragments `.qmd` (`git ls-files 21_riscv | grep -c "\.qmd$"`, a `4658e90`) amb files de taula *pipe*, inclosos amb `{{< include >}}` als callouts dels temes i a `11_riscv.qmd`; les taules que combinen fragments es fusionen amb `25_scripts/gen_taules_auto.py` i `24_specs/taules_fusio.toml`, que s'han d'executar a mà abans del render. Una font estructurada permetria generar les taules (i les fusions) per script i validar-ne el contingut; el cost és un generador nou i una dependència més del render. Cal valorar-ho abans de decidir res.

### `index.qmd`

- **Consolidar les versions de la taula de referències tècniques** (`#imp-llenguatges-de-referencia`). Cinc marcadors vius, `index.qmd:195-199`, que són **tres pendents distints**:

  | Marcadors | Pendent |
  | :--- | :--- |
  | `:195`, `:196` | Versió de la norma **ISO de C** (i si és tancada). La taula ja cita `[@iso9899_2024]`: el pendent és **verificar i tancar**, no decidir de zero |
  | `:197`, `:198` | Versió de **GCC** (`[@gcc16]`), i consolidar noms i versions de totes les files |
  | `:199` | **Versió numèrica o de data per a CSR** (fila de RISC-V, `[@riscv_csrs]`): decidir si la referència s'identifica per número de versió o per data. ✅ **No constava en cap registre anterior** |

