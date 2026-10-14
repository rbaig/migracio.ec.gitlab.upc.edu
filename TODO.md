# TODO

Tasques pendents i decisions obertes. Ha de quedar buit: cap entrada viva. Cada entrada porta la comprovació que la sosté. Una entrada que es tanca en surt, i l'historial de les parts ja fetes d'una entrada viva, també: tots dos van **literals** a l'arxiu, [`24_specs/arxiu_todo.md`](24_specs/arxiu_todo.md), amb el motiu i on en queda còpia ([D-91](24_specs/registre_de_decisions.md#d-91)). L'arxiu no es llegeix en començar una sessió.

**16 entrades vives** (recompte del 2026-10-14, en afegir a §Decisions obertes «Nota per als revisors externs» i a §Tasques globals → Eines «Neteja profunda dels fitxers operatius»; abans, 14, en retirar de §Tasques transversals «Remissions `@lst-` en lloc de «el codi següent»», executada; abans, 15, en afegir a §Tasques globals → Eines «Workflows de GitHub: validar-ne el YAML a `comprova.py`»; abans, 14, en afegir a §Tasques transversals «Autoproves de les comprovacions que fan servir eines externes»; abans, 11, en retirar de §Tasques transversals «Revisió completa de la norma de lèxic anglès/català», executada; l'historial dels recomptes és a `git log -p TODO.md`, i l'última versió que el portava, a `git show c29b58d:TODO.md`). Una entrada = una vinyeta de primer nivell (`^- `); les vinyetes indentades en són sub-ítems i no compten. Ordre que ho mesura:

```bash
grep -cE '^- ' TODO.md
```

Repartiment: `§Decisions obertes` 5 · `§Tasques transversals` 3 · `§Tasques per tema` 1 · `§Tasques globals` 6 · `§Llarg termini` 1 (suma 16, regla 12 bis). Ordre que el mesura, secció per secció:

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

  Cap de les tres no s'ha esborrat: és decisió del grup, amb l'etiqueta d'arxiu de `13_contrib.qmd §Convenció de noms de branques`. `build` només és al mirall de GitHub (`6d5d2cf`, sortida de CI) i no s'ha de tocar. L'abast de la revisió externa i les branques per equip (declaracions literals de l'usuari, 2026-10-06) són a `CLAUDE.md §Estat del projecte`, i la regla de coordinació, a [D-65](24_specs/registre_de_decisions.md#d-65). Les branques es mesuren amb `git ls-remote`, dient de quin remot (regla 13 de la skill `escombrada`). Mesura del 2026-10-09, a la tarda: cap branca d'equip, i `tema8` i `temes456` sense cap commit fora de `main`. 🗓️ **Opcions per a la reunió del 2 de novembre** (l'usuari, 2026-10-12, literal: «Només anota aquestes opcions a `TODO.md`. Vull consensuar les decisions a la reunió.»): (a) conservar-les totes; (b) arxivar `temes456` i `contingut/t3-traduccio` amb l'etiqueta d'arxiu i esborrar-les, i mantenir `tema8` fins que el revisor de T8 acabi (recomanació de Claude Code); (c) arxivar-les i esborrar-les totes tres. Executar-ho, quan es decideixi, és feina de Claude Code.

  ```bash
  git fetch --prune origin && git ls-remote --heads origin               # contingut/t3-traduccio, main, tema8, temes456 (2026-10-09)
  git rev-list --count origin/main..origin/tema8                         # 0 (2026-10-09)
  git merge-tree --write-tree --name-only origin/main origin/<branca>    # fusió de prova abans de tocar un fitxer que la branca també toca (D-64)
  ```

- **Contingut que la revisió externa de T4–T6 va treure: A6, per a la reunió de coordinació del 2 de novembre** (registrada el 2026-10-06; les altres dues retirades de la fusió, a A5 —la frase de la correspondència amb `float` i l'enunciat d'un exemple de notació científica—, les va confirmar l'usuari el 2026-10-07, a recomanació de Claude Code: la informació hi és en un altre lloc). La fusió de `temes456` (`451c3ef`) va treure de dos exemples d'A6, `#tip-rendiment-avio` i `#tip-rendiment-cpu` (`b7aab9c`, Fernando Agraz, 2026-07-22), la pregunta «Quin té més productivitat?». Hi ha quedat una incoherència: la pregunta és només «Quin té més rendiment?», i la resposta parla també de la productivitat de B. 🗓️ **Per a la reunió de coordinació del 2 de novembre del 2026** (decisió de l'usuari, 2026-10-07; la data, corregida per l'usuari el 2026-10-09: deia «la reunió del grup de treball del 7 de novembre», i és la del dia 2, la mateixa que la de l'entrada «Problemes i solucions…»: «És el dia 2. Confirmat.»). Proposta de Claude Code: tornar a posar la pregunta, per exemple «Quin té més rendiment? I més productivitat?», perquè els exemples són per contrastar les dues coses (els títols diuen «Rendiment i productivitat…»). Alternativa: treure la frase de la productivitat de les respostes. **Opcions** (l'usuari, 2026-10-12, literal: «Només anota aquestes opcions a `TODO.md`. Vull consensuar les decisions a la reunió.»): (a) tornar a posar la pregunta de la productivitat (recomanació de Claude Code); (b) treure de les respostes la frase de la productivitat.

  ```bash
  git grep -n "productivitat major" -- 01_apunts/A6.qmd   # :39 i :48 (2026-10-09; fins a 5e55cc8, «major productivitat»)
  ```

- **Exemples i solucions plegables a l'HTML** (petició de l'usuari, 2026-10-08, fase 7g: «Fer els exemples dinàmics? És a dir, que per veure la solució calgui prémer un botó. […] I segurament també les solucions dels problemes. A l'HTML es podrien encastar dins mateix dels enunciats»; la valoració inicial de Claude Code, amb les opcions i la recomanació, és a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). ✅ **Pilot de T1 fet** (2026-10-09; decisió de l'usuari: «Fes T1 com a pilot»; [D-90](24_specs/registre_de_decisions.md#d-90)): el filtre `25_scripts/plegables.lua` plega a l'HTML el div `.resposta` dels cinc exemples d'A1 amb el format **Pregunta** → **Solució** → **Resposta**, i afegeix a cadascun dels 15 enunciats de P1 la remissió a la seva solució («Solució 19.1»), a l'HTML i al PDF. **Queda, per decidir en valorar el pilot**: (b) a la resta de temes, que és afegir-los a la taula `PILOT` del filtre, sense tocar cap `.qmd` (P2–P9 i S2–S9 són fora de la revisió externa); (a) a la resta d'exemples amb el format **Pregunta** (A3 2, A6 5 i A7 4; A9 no en té cap), que demana marcar el div a mà, i A2–A8 són als fitxers que revisen els equips (D-65); i l'encastat de la solució dins de l'enunciat, que amb `{{< include >}}` duplicaria els identificadors `#sol-`: caldria un filtre que en copiés el contingut sense l'identificador, o carregar-la des de la pàgina de solucions amb JS. ⚠️ **Trobat en verificar el pilot** (2026-10-09): el títol de les 108 solucions diu «Exemple 19.1: Solució: …» a l'HTML i «Exemple 1: Solució: …» al PDF, perquè són `.callout-tip` i Quarto hi posa el prefix dels exemples; la remissió diu «Solució 19.1» (HTML) o «Solució 1» (PDF), de manera que l'enllaç porta a un bloc que es diu «Exemple». Ja passava abans del pilot amb les remissions `@sol-` entre solucions, però el pilot el fa visible a cada enunciat. Proposta de Claude Code, per decidir amb l'extensió: que el títol digui «Solució 19.1: …» (un filtre o una clau de `language:`, per investigar) i treure el «Solució:» que repeteix cada `## Solució: …`. **La part de les solucions** (estendre la remissió, encastar-les i el títol) es decideix a la reunió de coordinació del 2 de novembre: entrada següent. 🗓️ **Opcions per a la reunió del 2 de novembre** (l'usuari, 2026-10-12, literal: «Només anota aquestes opcions a `TODO.md`. Vull consensuar les decisions a la reunió.»): (b) estendre el pilot a P2–P9 i S2–S9, afegint-los a la taula `PILOT` del filtre, sense tocar cap `.qmd` (recomanació de Claude Code, si el pilot es dona per bo); (a) marcar a mà el div `.resposta` dels exemples amb **Pregunta** d'A3 (2), A6 (5) i A7 (4), que són d'A1–A8 (recomanació: després de la revisió externa); i l'encastat de la solució sota l'enunciat, que depèn del punt 1 de l'entrada «Problemes i solucions…».

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
  4. **Quan es publiquen les solucions: un interruptor del render** (recomanació de Claude Code; l'usuari, 2026-10-09: «Apunta-ho a `TODO.md`»). Publicar les solucions de cada sessió del laboratori un cop avaluada, i, si la reunió en reserva algun (punt 2), les dels problemes reservats quan toqui. Proposta d'implementació, per acabar de decidir en fer-ho: un paràmetre del render amb el que ja es pot publicar (l'última sessió avaluada, i els problemes reservats ja alliberats), llegit pel `Makefile` i pel CI de publicació, i un filtre Lua que tregui de l'HTML i del PDF els blocs `#sol-` que encara no toquen. Les remissions que hi apunten han de sortir alhora, o Quarto avisa d'una referència no resolta: les que el pilot afegeix als enunciats (D-90) i les 5 `@sol-` del laboratori (L3 1, L4 1, L6 3). Ha de funcionar abans que la versió dels estudiants es publiqui: avui la versió publicada a `rbaig.github.io` ja mostra totes les solucions. Si la reunió ho aprova, és una sessió curta (Opus, effort mitjà). ✅ **Recomanació de Claude Code acceptada per l'usuari** (2026-10-12, «Les teves recomanacions»): fer-lo ara, en una sessió nova, perquè la versió publicada ja mostra totes les solucions del laboratori, amb una configuració per defecte que publica el mateix que avui; la reunió decideix què s'amaga i quan.

  ```bash
  git grep -o -I -E -e '^:{3,} *\{#exr-' -- 02_problemes | wc -l    # 188 (2026-10-09, 6647801): P1 15, P2 31, P3 37, P4 32, P5 22, P6 14, P7 16, P8 10, P9 11
  git grep -o -I -E -e '^:{3,} *\{#sol-' -- 03_solucions | wc -l    # 108: S1 15, S2 14, S3 12, S4 17, S5 14, S6 14, S7 8, S8 7, S9 7
  git grep -o -I -E -e '^:{3,} *\{#sol-' -- 04_laboratori | wc -l   # 43: L1 7, L2 8, L3 6, L4 4, L5 4, L6 14 (i 43 #exr-)
  git grep -o -I -E -e '@sol-' -- 04_laboratori | wc -l               # 5 (2026-10-09): L3 1, L4 1, L6 3, totes a solucions del laboratori
  ```

- **Nota per als revisors externs, `24_specs/revisio_externa.md`: punt de l'ordre del dia de la reunió del 2 de novembre** (decisió de l'usuari, 2026-10-14, en la neteja dels fitxers operatius: el fitxer no s'esborra). És l'esborrany de la fase 8 (2026-10-12), amb les convencions noves des del 2026-10-06 i l'estat de cada fitxer d'A1–A8. A la reunió cal decidir si es distribueix, i com es manté: les xifres de la taula d'estat són d'una mesura (`281606d`), i la llista de convencions creix amb cada D-n nova.

  ```bash
  git log --oneline -1 -- 24_specs/revisio_externa.md   # l'última versió
  ```

---

## Tasques transversals

- **Registres que es mantenen a mà: quins es poden generar d'una sola font** (petició de l'usuari, 2026-10-13, literal: «Endavant», a la proposta de Claude Code d'anotar-ho; la pregunta que la va originar: «El treball que facis en aquesta sessió es podrà reaprofitar per a la resta de taules de "12_sigles_simbols.qmd". I per altres inventaris o registres?»). El patró de [D-115](24_specs/registre_de_decisions.md#d-115) (un fitxer de dades, una taula generada en renderitzar amb `25_scripts/taula_md.py`, i una comprovació contra el que descriu) es pot aplicar als registres del punt 3 de `13_contrib.qmd §Registres`, que es mantenen a mà i que `comprova.py` només vigila: l'arbre del `README.md`, el recompte d'aquesta capçalera, i les taules de la guia de les peces del render, del directori `.claude/` i dels sufixos d'origen. També hi ha llistes que repeteixen dades d'un altre fitxer, com la taula dels generadors del pre-render de `24_specs/svg.md §17`, que repeteix el `pre-render` de `_quarto.yml`; no s'han inventariat. Les taules de `21_riscv/` ja es van valorar el 2026-10-12 (recomanació de Claude Code, acceptada per l'usuari): no passen a `.json` ni a `.toml`, perquè una font estructurada demana un generador nou i una dependència més del render, i no hi ha cap problema concret que ho justifiqui; es pot tornar a plantejar si mai cal validar-ne el contingut (que cada instrucció tingui el format i l'operació coherents). Les taules Símbols i Notació de `12_sigles_simbols.qmd` no hi entren: tenen una sola font, i passar-les a un fitxer de dades només en canviaria el format. Primer, l'inventari, amb la proposta per a cadascun (generar-lo, comprovar-lo o deixar-lo com és); sense tocar A1–A8.

  ```bash
  sed -n '/^#### Registres/,/^### Verificació de l/p' 13_contrib.qmd    # els tres punts
  grep -n 'gen_' _quarto.yml 24_specs/svg.md                              # el pre-render i la taula de svg.md §17
  ```

- **Remissions per posició a exemples i taules** (observació de Claude Code, 2026-10-13, en mesurar les remissions `@lst-`; l'usuari, sobre apuntar-la: «Confirmat»). `13_contrib.qmd §Callouts` demana referenciar els callouts amb `@prefix-etiqueta`, i el corpus hi remet per posició 7 vegades: «l'exemple anterior» (A2, a `#tip-load-half-byte-unsigned`; A3, a §Resultat de l'enllaçament dels mòduls A i B; A8, abans de `@fig-mv-traduccio`), «els exemples següents» (A7, A9 dues vegades) i «les taules següents» (A2, les mides dels tipus de C). Escombrada amb veredicte cas a cas, com la de les `@lst-`, que ho decideixi: un exemple sense etiqueta, o una sèrie d'exemples presentada per un paràgraf, potser no en necessita. A2, A3, A7 i A8 són a l'abast de la revisió externa: abans d'avisar-ne els equips, o coordinat amb ells.

  ```bash
  git grep -o -I -E -i -e '\b(exemples?|figures?|taules?|callouts?) (següents?|anteriors?)\b' -- '*.qmd' ':!TODO.md' ':!24_specs/arxiu_todo.md' ':!24_specs/registre_de_decisions.md' ':!24_specs/revisio_externa.md' ':!24_specs/lexic/' ':!.claude/' ':!13_contrib.qmd' | wc -l   # 7 (0e5431d): A2 2, A3 1, A7 1, A8 1, A9 2
  ```

- **Autoproves de les comprovacions que fan servir eines externes** (petició de l'usuari, 2026-10-14, literal: «M'interessa que hi hagi un sistema bastant complet de testos automàtics, per exemple, pels revisors externs.»; [D-120](24_specs/registre_de_decisions.md#d-120)). `25_scripts/autoproves.py` prova les comprovacions de Python pur: les sigles, el lèxic, la prosa, el format del codi, els callouts, el calendari, les decisions citades amb els enunciats i les solucions, i la classificació (`13_contrib.qmd §Autoproves de les comprovacions`). Queden les que depenen d'una eina externa o de les figures: l'ortografia (`ortografia.py`, hunspell), la gramàtica (`gramatica.py`, LanguageTool i Java), les taules del PDF (`verifica_taules.py`, fontTools i les fonts del PDF), els programes del laboratori (`verifica_laboratoris.py`, RARS i Java), les figures (`inventari_figures.py`, `comprova_vores.py`), els fitxers orfes (`orfes.py`) i `escombrada.sh`. Proposta de Claude Code: una bateria per eina, que surti com a «omesa» si l'eina externa no hi és, com fan les comprovacions mateixes; la CI del mirall, que les té, les passaria sempre.

  ```bash
  python3 25_scripts/autoproves.py --llista | grep -c '^[a-z]'   # 8 bateries (2026-10-14)
  ```

---

## Tasques per tema

### T8

- **Per al revisor de T8** (decisió de l'usuari 10; fins al 2026-10-13, l'últim punt obert de l'entrada «Fase 8a: el que queda de la revisió d'A1–A8», de §Tasques transversals, que en sortir-ne va deixar aquest a §Tasques per tema: el text d'abans, a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives): A8 `#sec-mv-vipt`, «És una condició suficient per evitar l'aliàsing en una memòria cau VIPT, no una equivalència amb la PIPT en tots els aspectes» (`9db74b7`). Amb $N_C \cdot B \le T$, una VIPT tria el mateix conjunt i compara la mateixa etiqueta física que una PIPT de la mateixa geometria: fan els mateixos encerts i les mateixes fallades. Si es volia dir «suficient, però no necessària», ho ha de decidir el revisor. És també al missatge d'obertura de la fase 8.

---

## Tasques globals

### Contingut global

- **PDF: la numeració de les taules i de les figures als capítols sense número** (petició de l'usuari, 2026-10-10: «Sí, apunta-ho a `TODO.md`. Una observació: a `# Presentació` Surt "Taula 1. ", "Taula 2. ", etc.»; retallada el 2026-10-12, en treure el punt sobrer darrere dels números, `numbers=noendperiod` a `_quarto.yml`, D-109: el text d'abans, a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). Mesurat al PDF de `ccedc54`: als capítols sense número, la numeració no és la del capítol: la Presentació diu «Taula 1», «Taula 2»… (4 taules), sense prefix; i el glossari (`12_sigles_simbols.qmd`), «Taula 6.4» a «6.8», com si fossin taules d'un capítol 6 (probablement el comptador del capítol numerat anterior, el laboratori 6, per comprovar). A l'HTML, «Taula 1», «Taula 2»…, sense prefix. Cal decidir com han de sortir: sense número, amb un prefix propi o numerades a part (recomanació de Claude Code, 2026-10-12: sense número a la Presentació, i amb un prefix propi al glossari, «Taula G.1»). No toca A1–A8: és de `_quarto.yml` o de `preamble.tex`.

  ```bash
  pdftotext -layout _book/Estructura-de-computadors.pdf - | grep -o -E "(Taula|Figura) [0-9]+(\.[0-9]+)?\.?:" | sed -E 's/[0-9]+/N/g' | sort | uniq -c
  ```

- **Número de capítol dels problemes, les solucions i el laboratori: un a l'HTML i un altre al PDF** (observació de Claude Code, 2026-10-13, en investigar les remissions `@lst-`; l'usuari, sobre apuntar-la: «Confirmat»). `preamble.tex` fa `\counterwithin{chapter}{part}`, i el PDF reinicia el número de capítol a cada part; l'HTML els numera seguits, del 1 (A1) al 33 (L6). Totes les remissions numerades de P, S i L surten diferents als dos formats: el primer problema de P2 és «Problema 11.1» a l'HTML i «Problema 2.1» al PDF, i el primer exercici de L2, «Exercici 29.1» i «Exercici 2.1» (mesurat a `0e5431d`). A A1–A9 coincideixen. Fins a l'inici de les classes (febrer del 2027) cap material de fora del llibre no depèn dels números (`CLAUDE.md §Flux de treball`): cal decidir abans quina numeració es vol, o deixar-ho com a no coincidència acceptada i documentar-ho. No toca A1–A8: és de `preamble.tex` o de l'HTML.

  ```bash
  grep -n 'counterwithin{chapter}{part}' preamble.tex
  grep -o -m1 -E 'theorem-title"><strong>Problema [0-9]+\.1\b' _book/02_problemes/P2.html   # …Problema 11.1 (0e5431d)
  pdftotext _book/Estructura-de-computadors.pdf - | grep -c -E '^Problema 2\.1\b'           # 1: el de P2 (després de make render-complet)
  ```

- **PDF: capçaleres i títols sols al peu de la pàgina** (observació de Claude Code, 2026-10-13, en revisar el render de les remissions `@lst-`; l'usuari, 2026-10-14: «Sí, apunta-ho, i fes-ho extensiu a test general», que Claude Code llegeix com a «text general»). La capçalera d'un bloc de codi (el nom del fitxer, o «Codi 2.3: …» als llistats `#lst-`) es queda sola al final d'una pàgina i el codi comença a la següent: **40 pàgines** del PDF de `9e53096` amb el bloc 2a de les remissions (la llista, l'ordre de sota). Passa des de D-69: `preamble.tex` hi posa `\nopagebreak`, que LaTeX no garanteix, i dins dels callouts (`tcolorbox` partible) encara menys. Proposta per al codi: un `\needspace` (paquet `needspace`) a l'inici de `ec@codelisting`, que demani la capçalera i unes quantes línies de codi a la mateixa pàgina; dins dels callouts cal provar-ho a part. **Extensiu al text en general**: el mateix per a tot el que presenta el que el segueix i no se n'hauria de separar (títols de secció i de callout, peus de taula a dalt, i paràgrafs que acaben amb dos punts davant d'un bloc, una fórmula o una llista): primer mesurar-ho al PDF, com aquí, i després triar el mecanisme. Un cop resolt, la mesura pot passar a ser una comprovació de `make comprova-tot` ([D-121](24_specs/registre_de_decisions.md#d-121)). No toca A1–A8: és de `preamble.tex`.

  ```bash
  python3 - <<'EOF'   # pàgines del PDF que acaben amb la capçalera d'un bloc de codi: 40 (2026-10-14), després de make render-complet
  import re,subprocess
  t=open('Estructura-de-computadors.tex').read()
  n={x.replace('\\_','_') for x in re.findall(r'\\(?:caption\{(?:\\label\{[^}]*\})?|ecfitxer\{)\\texttt\{([^}]*)\}',t)}
  for i,p in enumerate(subprocess.run(['pdftotext','-layout','_book/Estructura-de-computadors.pdf','-'],capture_output=True,text=True).stdout.split('\f'),1):
      l=[x.strip() for x in p.splitlines() if x.strip()]
      if len(l)>1 and (l[-2] if l[-1].isdigit() else l[-1]) in n: print(i)
  EOF
  ```

- **Equacions a MathML**: **decisió presa — mantenir MathJax 3**; el pendent és reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa). Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`): funciona (`underbrace`, `cases`, taules amb math correctes a Chrome) i elimina el JS de MathJax (render instantani, offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), numeració d'equacions inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. El desbordament mòbil ja està resolt via CSS.

### Eines

- **Neteja profunda dels fitxers operatius** (petició de l'usuari, 2026-10-14; política a [D-122](24_specs/registre_de_decisions.md#d-122); fases 10a–10d de `CLAUDE.md §Pla de treball`, una sessió per fase). S0, feta el 2026-10-14: la branca `operacions` (D-123), l'etiqueta `arxiu/pre-neteja-2026-10-14` i `CLAUDE.md` al dia. 10a, feta el 2026-10-14: el registre de decisions, de 217 a 74 kB, sense l'§Historial de l'estat del projecte (el subpunt, a l'arxiu). Decisions de l'usuari sobre la proposta de Claude Code, totes amb la recomanació:
    - **10b, l'arxiu del `TODO.md`** (250 kB): primer, triar-ne el que encara és viu (les declaracions de l'usuari vigents, l'experiment de `.section` que cita D-8, les dades preservades d'A2 i de L2) i moure-ho on toqui; després, esborrar-lo, retirar D-91 i treure'n les remissions (`git grep -l arxiu_todo`) i la fila de `comprova.py`. `24_specs/lexic/` es conserva sencer: cal documentar com es fan servir els scripts d'ara endavant i quins són els criteris del lèxic.
    - **10c, `TODO.md` i les eines de Claude**: es treuen el recompte de la capçalera i la comprovació que el vigila (`comprova.py`, «Registres»; la regla 12 bis de l'escombrada); les entrades, sense cadenes de procedència; la skill `tancar-fase`, sense l'arxiu; els casos d'`escombrada/regles.md`, en una línia; l'arbre del `README.md`; i les regles perquè els fitxers no tornin a créixer (una entrada del registre s'edita al lloc, sense «Seguiment del…»; una entrada del `TODO.md` que es tanca s'esborra, i el commit en diu el motiu). **Per decidir a la 10c, si la skill `tancar-fase` es retira** (pregunta de l'usuari a la 10a, 2026-10-14: si encara té valor). Valoració de Claude Code: sense l'arxiu (10b), el recompte (10c) i l'§Historial del registre (10a), en queda una llista de cinc punts que ja són regles d'altres fitxers (la feina feta, les declaracions de D-63, la fila del pla, la D-n d'una regla nova, les xifres amb `escombrada`); recomanació, retirar-la i deixar aquests punts en un paràgraf de `CLAUDE.md §Flux de treball`. A la 10a se n'ha tret només el pas de l'§Historial.
    - **10d, `13_contrib.qmd`, `svg.md` i `README.md`**: la taula de les autoproves, reduïda a una fila per bateria (els casos, a `autoproves.py --llista`); els paràgrafs que descriuen les eines; el text transitori («Encara no tenen autoproves…»); la instal·lació i el render, al `README.md`, i la guia hi remet; a `svg.md`, la referència a `extract_pdf_figure.py`, que no ha existit mai, i les taules que repeteixen `_quarto.yml`.

  ```bash
  wc -c 24_specs/registre_de_decisions.md 24_specs/arxiu_todo.md TODO.md 13_contrib.qmd 24_specs/svg.md CLAUDE.md   # 213 kB, 250 kB, 28 kB, 149 kB, 37 kB, 13 kB (ae6c355)
  git grep -l arxiu_todo                                                                                            # els fitxers que hi remeten
  ```

- **Workflows de GitHub: validar-ne el YAML a `comprova.py`** (petició de l'usuari, 2026-10-14, en corregir la línia 51 de `.github/workflows/publish.yml`, literal: «Valora si cal fer extensiu el canvi a totes les entrades -name. Si no vols fer-ho en aquesta sessió, apunta-ho a TODO.md»). La línia, `- name: Genera les taules del lèxic (auto_termes/: glossari, sigles i formes)`, trencava el YAML des de `54f9c4b` (el «: » d'un valor sense cometes en fa una clau) i aturava la publicació; ara va entre cometes. **Valoració de Claude Code**: no cal posar cometes als 20 `name:` (13 de `publish.yml` i 7 de `comprova.yml`), perquè només aquest portava «: », i el risc no és dels `name:` sinó de qualsevol valor sense cometes amb «: » o « #» (també un `run:`). La protecció és una comprovació: avui `.github/` és de nivell 0 i res no en mira la sintaxi, i per això no ho va aturar res. **Proposta**: que la comprovació «Eines» de `comprova.py` validi el YAML dels `.github/workflows/*.yml` canviats (`yaml.safe_load`; «omesa» si no hi ha PyYAML, com les altres eines externes), amb la seva bateria d'autoproves (un workflow vàlid, i un amb un «: » en un valor sense cometes). Sessió curta (Sonnet, effort baix o mitjà).

  ```bash
  python3 -c "import glob, yaml; [yaml.safe_load(open(f)) for f in glob.glob('.github/workflows/*.yml')]; print('vàlid')"   # vàlid (2026-10-14, després de la correcció)
  ```

---

## Llarg termini

Tasques sense data ni urgència (secció creada el 2026-10-14, a petició de l'usuari).

- **Les formes catalanes de les expansions de sigles que avui només són en anglès** (petició de l'usuari, 2026-10-14, literal: «Apunta-ho a `TODO.md` en una secció nova de "Llarg termini"», sobre un punt obert del tancament de les sigles, [D-118](24_specs/registre_de_decisions.md#d-118)). El format únic de l'expansió admet «forma catalana (*expansió anglesa*, SIGLA)», però les sigles noves de `[sigles]` de `24_specs/termes.toml` només van rebre la forma catalana que el text ja feia servir (i la de LED). N'hi ha 28 amb només l'expansió anglesa: 13 són noms propis (ARM, ASCII, ELF, GCC, HTML, IEC, IEEE, ISO, JRE, MARS, MIPS, POSIX i RARS), que es queden en anglès, i les altres 15 en poden tenir una de catalana segons les fonts lèxiques de [D-116](24_specs/registre_de_decisions.md#d-116): ABI, AMAT (l'equivalent anglès de TAM: potser es queda així), AMO, API, CISC, CMOS, FIFO, LRU, MRU, NaN, RAM, RISC, ROM, TLB i ULP. Per a cadascuna: la consulta de les fonts, el camp `ca` a `termes.toml` i, si n'hi ha forma, l'expansió del text, on la comprovació de les sigles (`25_scripts/sigles.py`) la demanarà. Afecta A1–A8: amb la revisió externa en curs, s'ha de coordinar amb els equips (D-65).

  ```bash
  python3 -c "import tomllib; d=tomllib.load(open('24_specs/termes.toml','rb'))['sigles']; l=sorted(s for s,e in d.items() if e.get('en') and not e.get('ca')); print(len(l), *l)"   # 28 (2026-10-14)
  ```
