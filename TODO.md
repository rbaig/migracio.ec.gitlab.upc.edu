# TODO

Tasques pendents i decisions obertes. Ha de quedar buit: cap entrada viva. Cada entrada porta la comprovació que la sosté. Una entrada que es tanca en surt, i l'historial de les parts ja fetes d'una entrada viva, també: tots dos van **literals** a l'arxiu, [`24_specs/arxiu_todo.md`](24_specs/arxiu_todo.md), amb el motiu i on en queda còpia ([D-91](24_specs/registre_de_decisions.md#d-91)). L'arxiu no es llegeix en començar una sessió.

**15 entrades vives** (recompte del 2026-10-12, en retirar de §Tasques globals → SVG «Vores compartides als originals conservats (Roger)», feta; l'historial dels recomptes és a `git log -p TODO.md`, i l'última versió que el portava, a `git show c29b58d:TODO.md`). Una entrada = una vinyeta de primer nivell (`^- `); les vinyetes indentades en són sub-ítems i no compten. Ordre que ho mesura:

```bash
grep -cE '^- ' TODO.md
```

Repartiment: `§Decisions obertes` 4 · `§Tasques transversals` 3 · `§Tasques per tema` 4 · `§Tasques globals` 4 (suma 15, regla 12 bis). Ordre que el mesura, secció per secció:

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

- **Remissions `@lst-` en lloc de «el codi següent»** (decisió de l'usuari, 2026-10-09: «Decisió, remissions»; abans, decisió oberta: «“El codi següent”: remissions `@lst-`?», petició de l'usuari del 2026-10-08). **Delegada a una sessió nova** (Opus, effort alt), perquè demana investigar el render: al PDF, els blocs amb `filename` ja surten com a flotants numerats («Codi 4.7», pel `codelisting` de LaTeX i `preamble.tex`, D-69), i a l'HTML no, de manera que afegir `#lst-` i `lst-cap` pot donar una numeració diferent als dos formats. Abast, a `6a17af1`: 23 remissions per posició a un bloc de codi (19 «següent(s)» i 4 «anterior»): A2 3, A3 3, A9 1, P2 6, P3 2, P4 1, P7 1, P8 1, L1 1, L2 1, L3 1 i L6 2; cap `#lst-` al corpus. A2 i A3 són a l'abast de la revisió externa: si es fa després de la finestra de canvis, cal avisar-ne els equips. La regla, a `13_contrib.qmd §Referències creuades` amb la seva entrada al registre.

  ```bash
  git grep -c -i -E "(codi|programa|fragment|bloc) (de codi )?(següent|anterior)|(codis|programes|fragments|blocs) (següents|anteriors)" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'   # 23 (6a17af1)
  git grep -c -E '\{#lst-|@lst-' -- '*.qmd'                                                                                                                           # cap
  ```

- **Revisió completa de la norma de lèxic anglès/català** (petició de l'usuari, 2026-10-09: «apunta que cal fer una revisió completa d'aquesta norma»). D-88 (`13_contrib.qmd §Anglicismes i terminologia obligatòria`): si un terme no és a l'Optimot ni al diccionari anglès-català de Softcatalà, es fa servir l'anglès; s'admet l'anglès quan el català és molt poc usat, documentat a la taula de la guia. Cal passar tots els anglicismes del corpus per la regla: els del glossari de termes, que des del 2026-10-09 és l'única font del lèxic ([D-100](24_specs/registre_de_decisions.md#d-100); `12_sigles_simbols.qmd §Termes`, 117 termes i la taula dels que es mantenen en anglès) i els que el corpus fa servir sense traduir (*toolchain*, *stride*, *fetch*, *buffer*, *gap*, *working set*…). Sessió pròpia, amb una llista per terme (Optimot, Softcatalà, ús al corpus, proposta). Afecta A1–A9 i la resta: si es fa després de la finestra de canvis, coordinar-ho amb els equips. ✅ **Anàlisi feta el 2026-10-12** (subagent, Opus; l'usuari: «Endavant»), sense tocar cap fitxer del llibre: `24_specs/lexic/revisio_2026-10-12.md`, amb els scripts a `24_specs/lexic/scripts/`. 193 entrades (els 114 termes del glossari, les 6 de la taula dels mantinguts en anglès i 73 anglicismes del corpus que no hi són), consultades al Cercaterm, a l'Optimot i a Softcatalà: se'n mantenen 152, hi ha 29 propostes de canvi (A1, A2, A3, A6, A7, A9, P3, P9, S3, S7, S9, L1, L2, L3, L6 i `glossari.toml`) i 15 dubtes. **Decisions per a l'usuari** (el detall i la recomanació de cadascuna, al fitxer): (1) com es llegeix D-88 amb els sintagmes transparents: literalment, 47 termes del glossari passarien a l'anglès (*page fault*, *write-through*…), i el fitxer proposa una redacció que admeti el sintagma català fet amb mots que hi són; (2) si tots els termes que es mantenen en anglès van a la segona taula del glossari (7 candidats: *stride*, *working set*, *tiling*, *TLB shootdown*, *fall-through*, *round-robin*, *half*); (3) les formes del llibre que no són les del Termcat (*overflow* «sobreeiximent» / «desbordament», 110 ocurrències; *pseudoinstruction*, *branch*, *breakpoint*, *throughput*, *speedup*, *lazy*, *fetch*, *escape sequence*); (4) *little-endian* i *big-endian*, en anglès com a excepció documentada (recomanació); (5) *toolchain*: tres glosses diferents al text; (6) menors (*dirty hack*, «enllaçat», *ampersand*). **Altres troballes**: `gen_glossari.py` no recull les presentacions amb més d'una cosa dins del parèntesi ni llegeix `21_riscv/`, i se n'escapen *conflict*, *coherence*, *write-back*, *valid bit*, *stack frame*, *data type*, *return address*, *stack pointer*…; i, segons la consulta, el Termcat no té *half-adder* ni *full-adder* ni *multicore*, que el glossari anota «Termcat.» (l'usuari els havia confirmat el 2026-10-09, literal: «Confirmat»; cal que ho miri). Les xifres de la segona passada són aproximades: les que es publiquin, amb `escombrada.sh`.

- **Fase 8a: el que queda de la revisió d'A1–A8** (registrada el 2026-10-09, en tancar la fase 8a de `CLAUDE.md §Pla de treball`; l'entrada de les troballes i el que s'hi ha resolt després —la revisió del 2026-10-09 al matí, el %, l'article davant del codi i els dubtes tècnics de les lectures— són a l'arxiu, `24_specs/arxiu_todo.md`, §Entrades retirades → Executades i §Historial retallat de les entrades vives). Hi queda el que demana una decisió de l'usuari o el revisor de T8. Línies del tancament d'aquesta revisió.

  - **Per al revisor de T8** (decisió de l'usuari 10): A8 `#sec-mv-vipt`, «És una condició suficient per evitar l'aliàsing en una memòria cau VIPT, no una equivalència amb la PIPT en tots els aspectes» (`9db74b7`). Amb $N_C \cdot B \le T$, una VIPT tria el mateix conjunt i compara la mateixa etiqueta física que una PIPT de la mateixa geometria: fan els mateixos encerts i les mateixes fallades. Si es volia dir «suficient, però no necessària», ho ha de decidir el revisor. És també al missatge d'obertura de la fase 8.
  - **Majúscula després de dos punts a les definicions** (lectura lingüística d'A7 i A8): «**LRU** (…): Reemplaça…», «**Escriptura immediata** (…): S'escriu…». La guia demana minúscula en explicacions breus i majúscula en frases independents; aquestes són frases completes, i s'han deixat. S'han passat a minúscula els casos clarament breus («**Cas d'encert**: el bloc…», «**Accés 1**: escriptura…»).
  - **No aplicat, de les lectures, per ser preferència o canvi de matís**: A3 «El seu valor ha estat generat per **última vegada ABANS** d'una crida» (`#sec-determinacio-registres-segurs`); A6 «On $t_{exe}$ és…» després d'una fórmula (també A6 «On:», que caldria decidir sistemàticament); A8 «A petició del procés P1» (redundant amb la frase anterior) i «el camp PPN no té validesa».

---

## Tasques per tema

### T2

- **A2, `#sec-punters` i `#sec-vectors`: el que la revisió del 2026-10-12 no va aplicar, per decidir** (registrada el 2026-10-12; retallada el mateix dia, en aplicar-ne, per recomanació de Claude Code acceptada per l'usuari, les remissions cap endavant i la regla que s'havia perdut: el text d'abans, a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). L'usuari va reescriure les dues seccions a mà (`5aa5bc9`) i en va demanar la revisió tècnica i la lingüística; dos subagents la van fer (el tècnic, amb RARS 1.6), i les errades i les harmonitzacions que diu la guia es van aplicar (`2da1542`, `132edbf`). Queda el que demana una decisió de l'editor, perquè toca l'estructura o l'estil d'un text seu, i A2 ja és dels revisors externs (`CLAUDE.md §Estat del projecte`). Treballeu per àncora:
  - **Ordre**: el paràgraf que presenta el **declarador** (el que comença «En una declaració») va després del que ja en parla (sota `#tip-punters-c-declaracio`), i les definicions no lliguen («el declarador `*`» o el `*` com a part del declarador `*<nom>`); `#cau-void-main` diu «A partir d'aquí», però el primer `void main()` d'A2 és abans, a `#tip-inicialitzacio-punters-1`; `#wrn-index-aritmetica-punters` fa servir `3[vec]` ≡ `*(3 + vec)` abans que el text defineixi `vec[i]` ≡ `*(vec + i)`; i `#wrn-punters-funcions` és dins de §Absència de control en l'accés a memòria, amb què no té relació.
  - **Títols**: el criteri que es dedueix de `5aa5bc9` («C — » quan la secció no té part en RV32I) donaria «C — » a §Relació entre punters i vectors; el títol de §C — Tipus `<tipus> nom_vector[…]` no lliga amb el cos (`<tipus_elements>`, `<quantitat_elements>`); `#tip-desreferencia-punters-c` es diu «C — …» i conté RV32I; i `#tip-optimitzacio-acces-sequencial` i el seu germà d'accés aleatori no tenen el mateix patró de títol.
  - **Estil**: una sola forma de «punter a tipus enter» (hi ha també «punter de tipus enter» i «punter al tipus»); «**punter nul** (*null pointer*)», en negreta, perquè el glossari l'agafi; l'abast de `&` («davant del nom d'una variable», però més avall `&vec[0]`); el cas `int *p4, p5;`, dues vegades; la nota `[^decau]`, que remet a la seva pròpia secció; el títol de `#tip-c-tipus-vector-matriu-decaiment`, gairebé igual que el de §Relació entre punters i vectors; i la mateixa `n` per a `.space` i `.align` a `#nte-directives-align-space`.

  ```bash
  git grep -n -E "A partir d'aquí|punter de tipus enter|punter nul \(" -- 01_apunts/A2.qmd
  ```

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

- **Revisió de la paleta de colors per reduir-ne la quantitat** (petició de l'usuari, 2026-10-06, en migrar els colors llegats a la paleta). Després de la migració, la paleta de `24_specs/svg.md §10` i `§16` té 20 colors, i alguns papers es repeteixen amb tons gairebé iguals: dos vermells de traç (`#cc0000`, dependències de dades; `#dc3545`, fallada), dos fons rosats (`#f8d7da`, `.text`; `#f8d0d3`, fallada), dos fons verds (`#d1e7dd`, heap; `#c8ebd8`, encert), dos fons blaus (`#cfe2ff`, `.data`; `#e6f1fb`, zona o contenidor) i cinc grisos (`#f8f9fa`, `#dee2e6`, `#adb5bd`, `#6c757d` i `#343a40`). Cal decidir quins es fusionen i amb quin paper; cada fusió vol dir regenerar o editar les figures que el fan servir (`25_scripts/inventari_figures.py` les llista per color) i retirar-ne l'entrada de §13.

  ```bash
  python3 -c "import re; md=open('24_specs/svg.md').read(); s=md.split('## 10.')[1].split('## 11.')[0]+md.split('## 16.')[1].split('## 17.')[0]; print(len({c.lower() for c in re.findall(r'#[0-9a-fA-F]{6}', s)}))"   # 20, 2026-10-06
  ```

### Contingut global

- **PDF: la numeració de les taules i de les figures als capítols sense número** (petició de l'usuari, 2026-10-10: «Sí, apunta-ho a `TODO.md`. Una observació: a `# Presentació` Surt "Taula 1. ", "Taula 2. ", etc.»; retallada el 2026-10-12, en treure el punt sobrer darrere dels números, `numbers=noendperiod` a `_quarto.yml`, D-109: el text d'abans, a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). Mesurat al PDF de `ccedc54`: als capítols sense número, la numeració no és la del capítol: la Presentació diu «Taula 1», «Taula 2»… (4 taules), sense prefix; i el glossari (`12_sigles_simbols.qmd`), «Taula 6.4» a «6.8», com si fossin taules d'un capítol 6 (probablement el comptador del capítol numerat anterior, el laboratori 6, per comprovar). A l'HTML, «Taula 1», «Taula 2»…, sense prefix. Cal decidir com han de sortir: sense número, amb un prefix propi o numerades a part (recomanació de Claude Code, 2026-10-12: sense número a la Presentació, i amb un prefix propi al glossari, «Taula G.1»). No toca A1–A8: és de `_quarto.yml` o de `preamble.tex`.

  ```bash
  pdftotext -layout _book/Estructura-de-computadors.pdf - | grep -o -E "(Taula|Figura) [0-9]+(\.[0-9]+)?\.?:" | sed -E 's/[0-9]+/N/g' | sort | uniq -c
  ```

- **Equacions a MathML**: **decisió presa — mantenir MathJax 3**; el pendent és reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa). Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`): funciona (`underbrace`, `cases`, taules amb math correctes a Chrome) i elimina el JS de MathJax (render instantani, offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), numeració d'equacions inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. El desbordament mòbil ja està resolt via CSS.

### Eines

- **Valorar si les taules de `21_riscv/` haurien de passar a `.json` o `.toml`** (petició de l'usuari, 2026-10-02, per al futur). Avui són 44 fragments `.qmd` (`git ls-files 21_riscv | grep -c "\.qmd$"`, a `4658e90`) amb files de taula *pipe*, inclosos amb `{{< include >}}` als callouts dels temes i a `11_riscv.qmd`; les taules que combinen fragments es fusionen amb `25_scripts/gen_taules_auto.py` i `24_specs/taules_fusio.toml`, que s'han d'executar a mà abans del render. Una font estructurada permetria generar les taules (i les fusions) per script i validar-ne el contingut; el cost és un generador nou i una dependència més del render. Cal valorar-ho abans de decidir res.
