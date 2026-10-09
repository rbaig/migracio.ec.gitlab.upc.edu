# TODO

Tasques pendents i decisions obertes. Ha de quedar buit: cap entrada viva. Cada entrada porta la comprovació que la sosté. Una entrada que es tanca en surt, i l'historial de les parts ja fetes d'una entrada viva, també: tots dos van **literals** a l'arxiu, [`24_specs/arxiu_todo.md`](24_specs/arxiu_todo.md), amb el motiu i on en queda còpia ([D-91](24_specs/registre_de_decisions.md#d-91)). L'arxiu no es llegeix en començar una sessió.

**27 entrades vives** (recompte del 2026-10-09, en afegir a §Tasques globals → Eines «Protocols d'execució dels generadors i de les comprovacions, per nivells»; l'historial dels recomptes és a `git log -p TODO.md`, i l'última versió que el portava, a `git show c29b58d:TODO.md`). Una entrada = una vinyeta de primer nivell (`^- `); les vinyetes indentades en són sub-ítems i no compten. Ordre que ho mesura:

```bash
grep -cE '^- ' TODO.md
```

Repartiment: `§Decisions obertes` 5 · `§Tasques transversals` 8 · `§Tasques per tema` 5 · `§Tasques globals` 9 (suma 27, regla 12 bis). Ordre que el mesura, secció per secció:

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

- **Fitxers orfes: un directori per als que es conserven, i un detector per a la resta** (petició de l'usuari, 2026-10-08, fase 7g: «Valora si té sentit crear un directori a on posar els fitxers orfes que es volen guardar; d'aquesta manera, es pot crear un agent (o el mecanisme que pertoqui) per buscar orfes fora d'aquest directori i presentar-los demanant si cal moure'ls al directori de fitxers orfes o esborrar»). **Llista del 2026-10-08** (`6a17af1`; les figures, per l'inventari, que mira si algun `.qmd` les consumeix, i la resta, per si algun fitxer les cita): els 15 originals de `22_figs_originals/` amb una versió generada al llibre, que es conserven per a les diapositives (D-68) i que `make inventari` ja llista a part (`24_specs/figures.md`, «Originals amb una versió generada al llibre»): set de T3 (`A3_ba_exemple`, `A3_ba_func`, `A3_ba_general`, `A3_ba_multi`, `A3_mapa_memoria`, `A3_pila_uninivell`, `A3_pila_multinivell`) i vuit de T7 (`A7_capacitat_exemple_bucle_primera_passada`, `…_segona_passada`, `A7_conflicte_exemple`, `A7_escriptura_estat_inicial`, `A7_escriptura_immediata_amb_assignacio`, `…_sense_assignacio`, `A7_escriptura_retardada`, `A7_lru_exemple`); i `05_diapositives/placeholder.txt`, que reserva el directori (`README.md`), afegit a mà: «placeholder» surt en altres contextos i la comprovació no el marca. Cap `.qmd`, script ni `.toml` orfe: `A7_mc_politiques_resum__graphviz.gv` és la font de `#fig-mc-politiques-resum` (A7). **Proposta de Claude Code**: (1) moure els 15 a `22_figs_originals/conservats/`, amb la regla a D-68, i que l'inventari prengui el directori com a criteri en lloc de deduir-ho; (2) un `25_scripts/orfes.py` (la comprovació de dalt, que deixa fora la configuració de les eines, `.github/`, `.vscode/` i `.claude/`, i els PDF de referència, `PDF_*/`) a `make inventari`; i (3) un avís al hook d'abans del commit quan un commit deixa un orfe nou fora de `conservats/`, amb la pregunta de moure'l o esborrar-lo. Un agent no cal: és una comprovació mecànica. §T3 d'aquest fitxer en cita quatre dels set de T3 pel nom (`A3_ba_exemple`, `A3_ba_func` i les dues piles; recompte del 2026-10-09, en retallar-la), i s'hauria d'actualitzar alhora. Decisió de l'usuari.

  ```bash
  git ls-files | grep -v -E '^(\.github|\.vscode|\.claude/|PDF_)' | while read f; do b=$(basename "$f"); s=${b%.*}
    git grep -q -F -e "$b" -e "$s" -- ":(exclude)$f" ':!TODO.md' ':!24_specs/arxiu_todo.md' ':!24_specs/registre_de_decisions.md' ':!24_specs/figures.md' || echo "$f"
  done   # 8 (6a17af1): A7_capacitat_exemple_bucle_* (2) i els fotogrames A8_mv_exemple_tlb_pas* (6, el nom el compon gen_T8.py)
  # Els altres 13 conservats no hi surten perquè la versió generada en comparteix l'arrel (A3_ba_exemple__BA): per a les figures, el criteri és l'inventari, que mira el consum.
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
  2. **Solucions a tots els problemes**, no a una selecció (avui, D-73: «aproximadament un de cada dos o tres»). N'hi ha 108 per a 188 problemes, i en falten 80: T2 17, T3 25, T4 15, T5 8, T7 8, T8 3 i T9 4 (T1 i T6 ja les tenen totes). L'usuari: «Jo soc partidari de fer-ho pq penso que el valor pedagògic d'un problema sense solució és limitat i pq amb Claude ara es solucionen tots.» **Valoració de Claude Code**: a favor. El segon argument també demana una solució oficial i verificada: la que l'estudiant obté d'un assistent pot fallar justament en el que EC ensenya (les convencions de RARS i d'EC, el sobreeiximent en Ca2, les traces de memòria cau). Per a la reunió: si algun problema es reserva per fer-lo a classe o per a l'avaluació (llavors, la solució es pot publicar més tard, amb l'interruptor del punt 3), i qui revisa les solucions noves. Cost: és feina de solucions, Opus amb effort alt (`CLAUDE.md §Model i effortness`), amb RARS per al codi; unes quantes sessions, per tema. Si es fa, D-73 canvia.
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

- **Glossari: presentacions dubtoses, per decidir** (registrada el 2026-10-06, en generar la secció «Termes» de `12_sigles_simbols.qmd` amb `25_scripts/gen_glossari.py`; l'usuari en vol la llista, no cap correcció; les resoltes —les traduccions divergents, el 2026-10-07, i les presentacions dubtoses d'A1–A8, el 2026-10-09— són a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). El glossari mostra la forma de la primera presentació i surt del text, de manera que cada decisió es corregeix al corpus i el glossari es regenera. Queden les **presentacions dubtoses** de fora d'A1–A8 i les que no són termes (el patró és correcte, però la presentació no és la d'un terme): *biased exponent* → «esbiaixada» (A5:110, la negreta només cobreix l'adjectiu); *flush* → «anul·len» (A9:317, un verb conjugat); *harts* → «entre múltiples nuclis o fils d'execució» (A2:946); *Segfault* → «Segmentation Fault» (A2:1722, tots dos en anglès); *dirty* → «bit D» (A8:158); *offset*, la primera presentació en negreta és a L6:53, tot i que el terme surt abans; dues expansions de sigla, *Not a Number* (A5:405) i *American Standard Code for Information Interchange* (A2:2127), que ja són a §Sigles; i *good design demands good compromises* (A2:256), un principi i no un terme. Línies mesurades a `35be646`.

- **Confirmar al Termcat «semisumador» (*half-adder*) i «sumador complet» (*full-adder*)** (registrada 2026-10-03, fase 5). Són els termes que fan servir A4 (`#wrn-sobreeiximent-maquinari`) i les figures del sumador, i ja són a la taula de `13_contrib.qmd §Substitucions obligatòries`, marcats «pendent de confirmar». L'usuari no els ha pogut trobar a la interfície nova del Termcat; només hi consta *adder* → «sumador». Si el Termcat en dona uns altres, cal canviar la taula, el text d'A4 i els rètols dels SVG (`git grep -n -i 'semisumador\|sumador complet'`).

- **Guia i glossari: tres desajustos trobats a la fase 7g** (registrats el 2026-10-08; decisió de l'usuari: «registra qualsevol possible error»). Fase 7i de `CLAUDE.md §Pla de treball`. `13_contrib.qmd` i `12_sigles_simbols.qmd` eren fora de l'abast de la fase. Línies mesurades a `6a17af1`.

  - **`13_contrib.qmd:156`** (§Decisions per tema → T5): l'estructura de cada solució comença per `**Enunciat:** @exr-...`, i el corpus fa `**Enunciat**:` 108 vegades de 108. És la guia la que s'ha de corregir.
  - **`13_contrib.html` fa 1 681 px a l'escriptori**: la taula de §Figures Graphviz porta noms de fitxer llargs en codi, que no es parteixen. Mesurat amb Playwright el 2026-10-08, en verificar el bloc 2 de la fase 7g.
  - **`12_sigles_simbols.qmd:202`**: $t_{pd}$ i $t_{pi}$ hi són «Temps de processament de dades / d'instruccions», i A7:789 en diu «temps de penalització de $\text{MC}_i$ i $\text{MC}_d$». És el glossari el que s'ha de corregir.

- **Suggeriments de la fase 7g sense proposta concreta, per decidir** (registrats el 2026-10-08; criteri de l'usuari per al bloc 3c: «E i H; S amb proposta», i la resta al `TODO.md`). Són de la passada de control de qualitat d'A9, els problemes, les solucions i el laboratori sobre `7a1640e` (34 informes dels subagents `auditor-xifres` i `revisor-linguistic`). Un subagent els ha contrastat un per un amb `git diff 7a1640e 6a17af1` i amb el text d'avui: **100 aplicats i 88 oberts** (3 de parcials), comptant una entrada per fitxer; des del 2026-10-08, 86, amb l'ordre de la sortida d'A9 i S9 fet. **Fase 7i de `CLAUDE.md §Pla de treball`** (acceptada per l'usuari el 2026-10-08), amb l'entrada següent. Cap no és una errada: són millores de redacció, de didàctica o de notació, i alguns demanen un criteri. Són fora de la revisió externa, tret dels que lliguen amb A1–A8, que ho diuen. Línies a `6a17af1`.

  - **De criteri, a diversos fitxers**: «word» de la interfície de RARS a la prosa, en lloc de «paraula» (L1:122, :207; L2:216, :218, :239, :308, :551, :602); futurs de 2a persona del plural a les introduccions del laboratori («combinareu», L3:44; «practicareu», L3:451; «desenvolupareu», L5:400; «analitzareu», L5:536); dos punts dins de la negreta (S3:224, :247; L4:172, :176); blocs `.s` que comencen amb una línia buida (L4:64, :195, :364; L6:137, :351, :559, :665, :835, :967); sigles sense expandir a la primera aparició del fitxer (P6:17 ISA; S3:707 ABI i ISA, :325 CPI; L3:237 i L4:192 BA; A9:44 PC, :76 ISA, :337 ABI, :776 PTE i MMU); «només quan V = 0», i també hi ha fallades de pàgina per permisos i pels bits A/D (A9:776, P9:129, S9:375); l'ordre dels operands de `csrw` a RARS 1.6, invertit, si mai s'hi fa servir (A9:440, S9:86, :166, `21_riscv/Zicsr_pseudo.qmd:2`). ✅ L'ordre de la sortida (A9 i S9, amb l'esquelet d'A2), fet el 2026-10-08 (`03e3d7c`): `li a7, 93` abans de `li a0, 0`, com el laboratori (decisió de l'usuari).
  - **Problemes**: P1:136 «emprant» (la resta del fitxer diu «usant»); P2:95 i :167, `.dword` sense dir la regla d'alineació (RARS alinea a 4, l'ABI a 8), i la resposta canvia; P2:80, la nota dona la resposta de b); P2:261, les dades no posen a prova `.align 0`; P2:84 i :158 «a nivell de paraula/byte» → «per paraules», «byte a byte»; P3:43 «la suma amb si mateix» → «el doble»; P3:52 «emmagatzemat» → «guardat»; P4:260–261, :407 i :438, tres verbs per al mateix («utilitzant», «fent servir», «usant»); P4:18, «complement a 2 (Ca2)» a la primera aparició; P5:93 i :101, «Suposant…:» sense verb principal; P5:113 i :212 *sticky* sense terme català (com A5); P5:72–219 *half* en cursiva a cada aparició; P6:149–150 «inst»; P7:180 «L word = lectura de 2 bytes» (a EC, la paraula és de 32 bits: cal mirar-ho a l'original); P7:261–262, sagnat de 3 espais; P8:269, l'enunciat no diu que la MC és VIPT, i S8 ho suposa.
  - **Solucions**: S1:35–39, el pas 2 («Interpretar el compilador de C») és artificial; S1:297–301, els negatius de 8 bits sense el càlcul $256 + x$; S1:333 i :341, les negacions no es mostren (o remetre a `@sec-inversio-signe`); S1:19–22 i :34–37, majúscula després dels dos punts; S1:399 «$30 \in$ rang»; S1:261 `0xFFCD` igualat al valor amb signe; S1:141 S&M al títol abans de definir-la; S2:570–572, `t1` sobreescrit sense dir-ho; S2:583–584, `.space 40` sense `.align 2`; S2:309–318, la regla d'alineació de `.dword`; S4:629–648, a) no diu el nombre d'instruccions; S4:635, `la` compta 1 cicle (S3 ara en compta 2: cal escriure el conveni); S4:728, :750 i :784, instruccions i cicles barrejats, amb un model de costos que l'enunciat no dona; S4:66, falta la negació del subtrahend (també c i d); S5:881, :901 i :907 *cast* sense terme català; S5:749, dir que no cal preservar cap registre «abans de cada crida»; S5:970, la fletxa de *Guard* assenyala −12; S5:919, `#sol-t5-assoc-suma` només resol a); S5:1183, el NaN (silenciós o canònic, segons A5); S5:453 *half* sense presentar; S5:1118, «els valors exactes» són els de l'última operació amb els intermedis arrodonits (el valor exacte d'A×(B+C) és 15,2183…); S6:27, $\text{CPI}_1 \cdot f_2$ contra $\text{CPI}_{P2}$ de :50; S6:31–34, c) no respon «no» explícitament, i «el mateix compilador» és una hipòtesi; S6:202 «Tampoc és possible» (opcional: «Tampoc no»); S7:119, :122 i :125, la columna D; S7:162–211, la barra de $\bar{t}_{p_1}$ i $\bar{t}_{pd}$, que A7 no fa servir; S7:113, :134, :146, :172 i :217, *write-back* per a l'acció (A7 en fa la política); S7:158, `@cau-model-temps` és un punter imprecís (`#sec-tam-mc-unificada`, `@cau-tam-retardada`); S7:404 i :415, 1 KiB; S8:141 i :161, falten els totals de fallades i l'ordre LRU final; S8:195, «E» de la fila c.
  - **Laboratori**: L1:207 *endianness* sense cursiva; L4:357, la solució aplica l'optimització #3, que l'enunciat no demana; L4:266, una tasca dins de la solució; L4:18, espais al final d'una línia; L5:169, a RARS 1.6 és «Dump Memory…» i escriu un fitxer (el llistat publicat és de la *Text Segment window*); L6:287 i :319, A7 no defineix $t_{MP}$ (`@sec-texe-mc`) (✅ des de la fase 8a, `19b9913`, A7 el defineix a `@sec-gap-memoria` i és al glossari: queda per decidir si L6 hi remet); L6:48 i :265, `@sec-opt-acces-sequencial` no parla de memòria cau.
  - **A9**: :380, `ebreak` i el +4 (en un punt de parada de programari no n'hi ha); :226, `mtval` «pot contenir» la instrucció (l'especificació hi permet 0); :519, el 214 (`brk`) no és a RARS (Sbrk, 9); :714, l'ordre de «executa el tractament… i crida l'*exception handler*»; :64, :286 i :486 «Firmware» → «microprogramari (*firmware*)»; :319 i :321 *pipeline*, que A1–A8 no fan servir; :389 *dispatcher* → «distribuïdor (*dispatcher*)»; :294, :298, :300 i :337, «Guardar», «Desar» i «Salvar» per al mateix; i, trobat en tancar la fase, :539, el títol «Exemples de crides al sistema a RARS» d'un `#tip-`, que surt «Exemple 9.N: Exemples…».
  - **`index.qmd`**: :57 «l'estudianta» contra :58 «l'alumne» (genèric; tria de l'usuari); :139 MWE sense el format de sigla; :103 i :113 «Exemple | **Sí**» contra «Marg.» de `13_contrib.qmd §Callouts`; :105 i :115, els peus de la taula no coincideixen entre el PDF i l'HTML; :46, «S1» vol dir sessió de laboratori al menú i tema de solucions, i «L1–L3» no surt enlloc.

- **Remissions `@lst-` en lloc de «el codi següent»** (decisió de l'usuari, 2026-10-09: «Decisió, remissions»; abans, decisió oberta: «“El codi següent”: remissions `@lst-`?», petició de l'usuari del 2026-10-08). **Delegada a una sessió nova** (Opus, effort alt), perquè demana investigar el render: al PDF, els blocs amb `filename` ja surten com a flotants numerats («Codi 4.7», pel `codelisting` de LaTeX i `preamble.tex`, D-69), i a l'HTML no, de manera que afegir `#lst-` i `lst-cap` pot donar una numeració diferent als dos formats. Abast, a `6a17af1`: 23 remissions per posició a un bloc de codi (19 «següent(s)» i 4 «anterior»): A2 3, A3 3, A9 1, P2 6, P3 2, P4 1, P7 1, P8 1, L1 1, L2 1, L3 1 i L6 2; cap `#lst-` al corpus. A2 i A3 són a l'abast de la revisió externa: si es fa després de la finestra de canvis, cal avisar-ne els equips. La regla, a `13_contrib.qmd §Referències creuades` amb la seva entrada al registre.

  ```bash
  git grep -c -i -E "(codi|programa|fragment|bloc) (de codi )?(següent|anterior)|(codis|programes|fragments|blocs) (següents|anteriors)" -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'   # 23 (6a17af1)
  git grep -c -E '\{#lst-|@lst-' -- '*.qmd'                                                                                                                           # cap
  ```

- **Revisió completa de la norma de lèxic anglès/català** (petició de l'usuari, 2026-10-09: «apunta que cal fer una revisió completa d'aquesta norma»). D-88 (`13_contrib.qmd §Anglicismes i terminologia obligatòria`): si un terme no és a l'Optimot ni al diccionari anglès-català de Softcatalà, es fa servir l'anglès; s'admet l'anglès quan el català és molt poc usat, documentat a la taula de la guia. Cal passar tots els anglicismes del corpus per la regla: els de la taula de §Substitucions obligatòries, els del glossari de termes (`12_sigles_simbols.qmd §Termes`, 105 termes) i els que el corpus fa servir sense traduir (*toolchain*, *stride*, *fetch*, *buffer*, *gap*, *working set*…). Sessió pròpia, amb una llista per terme (Optimot, Softcatalà, ús al corpus, proposta). Afecta A1–A9 i la resta: si es fa després de la finestra de canvis, coordinar-ho amb els equips.

- **Taula de traduccions anglès–castellà–català** (petició de l'usuari, 2026-10-09: «Valora si tindria sentit incorporar en un apèndix o similar la taula de traduccions Anglès-castellà-català»). **Valoració de Claude Code**: sí, però no com un apèndix nou, sinó com una tercera columna del glossari de termes que ja existeix (`12_sigles_simbols.qmd §Termes`, generat per `gen_glossari.py`), perquè no hi hagi dues taules del mateix contingut. Ajudaria qui fa servir bibliografia en castellà (la traducció de Patterson & Hennessy, per exemple). El castellà no surt del corpus: caldria una font, un `24_specs/termes_es.toml` per terme anglès, amb el Termcat com a referència (dona els equivalents castellans). Cost: el fitxer, una columna més al generador i el manteniment. Decisió de l'usuari; fora de la revisió externa.

- **Fase 8a: el que queda de la revisió d'A1–A8** (registrada el 2026-10-09, en tancar la fase 8a de `CLAUDE.md §Pla de treball`; l'entrada de les troballes i el que s'hi ha resolt després —la revisió del 2026-10-09 al matí, el %, l'article davant del codi i els dubtes tècnics de les lectures— són a l'arxiu, `24_specs/arxiu_todo.md`, §Entrades retirades → Executades i §Historial retallat de les entrades vives). Hi queda el que demana una decisió de l'usuari o el revisor de T8. Línies del tancament d'aquesta revisió.

  - **Per al revisor de T8** (decisió de l'usuari 10): A8 `#sec-mv-vipt`, «És una condició suficient per evitar l'aliàsing en una memòria cau VIPT, no una equivalència amb la PIPT en tots els aspectes» (`9db74b7`). Amb $N_C \cdot B \le T$, una VIPT tria el mateix conjunt i compara la mateixa etiqueta física que una PIPT de la mateixa geometria: fan els mateixos encerts i les mateixes fallades. Si es volia dir «suficient, però no necessària», ho ha de decidir el revisor. És també al missatge d'obertura de la fase 8.
  - **Majúscula després de dos punts a les definicions** (lectura lingüística d'A7 i A8): «**LRU** (…): Reemplaça…», «**Escriptura immediata** (…): S'escriu…». La guia demana minúscula en explicacions breus i majúscula en frases independents; aquestes són frases completes, i s'han deixat. S'han passat a minúscula els casos clarament breus («**Cas d'encert**: el bloc…», «**Accés 1**: escriptura…»).
  - **No aplicat, de les lectures, per ser preferència o canvi de matís**: A3 «El seu valor ha estat generat per **última vegada ABANS** d'una crida» (`#sec-determinacio-registres-segurs`); A6 «On $t_{exe}$ és…» després d'una fórmula (també A6 «On:», que caldria decidir sistemàticament); A8 «A petició del procés P1» (redundant amb la frase anterior) i «el camp PPN no té validesa».

---

## Tasques per tema

### T3

- **Decisió de contingut a `#cau-boolea-c`** (`A3.qmd:249`, mesurat a `ab48732`, pendent d'Adrià, obert des de la revisió de T3): el text diu que «unes expressions no nul·les s'interpreten com a certes» sense dir **quines**. Cal indicar com s'identifiquen les que sí i les que no. Afecta el rigor tècnic. El marcador segueix al corpus perquè la decisió és viva i no la pot prendre Claude Code.

- **Retocs manuals pendents (Roger) a cinc originals de T3** (des del 2026-10-04; retallada el 2026-10-09: els estats del 2026-10-04 i del 2026-10-07, amb les decisions de l'usuari que hi van portar, són a l'arxiu, `24_specs/arxiu_todo.md` §Historial retallat de les entrades vives). Els esmena l'usuari, a `22_figs_originals/`, perquè també els fa servir per a les diapositives. Quatre es conserven sense que el llibre els consumeixi, perquè A3 en fa servir la versió generada, que ja no té l'error ([D-68](24_specs/registre_de_decisions.md#d-68)); el cinquè, `A3_deps_exemple.svg`, és la subfigura (a) de `#fig-deps-exemple`, i l'error surt al llibre fins que s'esmeni.

  - `A3_deps_exemple.svg`: posa fletxes a `a` i `b`, que no travessen cap crida, i hi diu `e = res_g + res_f`, quan el text diu `res_f + res_g`.
  - `A3_ba_exemple.svg`: dibuixa `w` com a `int` de 80 bytes, quan el codi diu `char w[20]` (20 bytes), i rotula `v[0]` la subfranja de `v[17]`.
  - `A3_ba_func.svg`: pinta `w` (`int w[10]`, una variable local) del verd dels registres segurs desats (`#d1e7dd`, 3 ocurrències), i no del blau de les variables locals (`24_specs/svg.md §10`).
  - `A3_pila_uninivell.svg` i `A3_pila_multinivell.svg`: marquen `sp` amb `#cc0000` (6 i 10 ocurrències), el vermell que la paleta reserva a les dependències de dades. Les generades el marquen del color de la zona del cim (`svg.md §9`).

  ```bash
  grep -o -i "d1e7dd" 22_figs_originals/A3_ba_func.svg | wc -l                                            # 3 (2026-10-07)
  for f in uninivell multinivell; do grep -o "cc0000" 22_figs_originals/A3_pila_$f.svg | wc -l; done    # 6 i 10 (2026-10-07)
  ```

### T5

- **Figura font única per a les rectes de T5, amb retalls** (registrada el 2026-10-06; era el «TODO futur» de l'entrada «Nova eina disponible: retalls», avui a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades → Executades). `#fig-recta-global` (`A5_recta_global.svg`) i `#fig-recta-zoom-zero` (`A5_recta_zoom_zero.svg`) són dues figures dibuixades per separat, i `24_specs/retalls.toml` no té cap retall definit. Es podria redibuixar una sola figura en estil pla (`24_specs/svg.md`), amb el rang global, el zoom de zero i els denormals, i definir-ne les dues vistes com a retalls (`13_contrib.qmd §Retalls`), si cada retall surt net. Fer-ho sobre les figures actuals ja s'ha descartat dues vegades (motius a l'entrada retirada, `git show 7ac2fc9:TODO.md`). Prioritat baixa, i A5 és a l'abast de la revisió externa.

  ```bash
  grep -c "^\[crops" 24_specs/retalls.toml   # 0 a 7ac2fc9
  ```

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

- **Calendari del laboratori: el 07/05/2026 i el quadrimestre, per confirmar** (registrada el 2026-10-08, fase 7g, en la primera passada de `25_scripts/verifica_calendari.py`). (1) La fila dels divendres (subgrups 31, 32 i 33) diu 07/05 a la sessió 5, i el 07/05/2026 és dijous. La setmana té l'1 de maig, divendres i festiu: si la universitat va fer el dijous 7 amb horari de divendres, és correcte; si no, és una errada. (2) El quadrimestre, «primavera 2025-26», ja és passat: el calendari s'ha de refer per a la primavera 2026-27, quan la FIB en publiqui les dates. Des de la fase 7g la taula només surt a l'HTML (el PDF hi remet), i el hook d'abans del commit hi passa l'script quan un commit toca `04_laboratori/Lcalendari.qmd`, amb l'avís de passar l'agent `verificador-calendari` (D-74). Confirmació de l'usuari.

  ```bash
  python3 25_scripts/verifica_calendari.py   # ✗ fila «31, 32, 33»: 07/05/2026 és dijous, no divendres (2026-10-08)
  ```

---

## Tasques globals

### SVG

- **Vores compartides amb el traç centrat: la resta de figures** (registrada el 2026-10-07, fase 7f; decisió de l'usuari G2). **Fase 7h de `CLAUDE.md §Pla de treball`** (acceptada per l'usuari el 2026-10-08). Els noms de les figures són els de després de D-76 (`A4_…`, 2026-10-08). `24_specs/svg.md §7` diu, des del 2026-10-07, que cada zona amb traç dibuixa les seves vores per dins de la seva àrea, perquè la frontera entre dues zones de color diferent no depengui de l'ordre de dibuix. Ho apliquen `gen_BA.py` i `gen_mapa.py`. A la resta, dos `<rect>` amb traç de color diferent comparteixen una vora (el segon tapa el primer), o un farciment sense traç en tapa mitja. Hi ha 54 figures amb almenys una vora així: 44 de consumides —17 de `gen_regs.py` (`__registre`), 7 de `gen_MC.py` (`__MC`) i 20 originals: `A4_matriu_emmagatzematge`, `A4_matriu_offset_ij`, `A4_matriu_recorreguts_strides`, `A5_grs_esquema`, `A7_cd_descomposicio_bits`, `A7_mc_descomposicio_bits`, `A7_mc_encert`, `A7_mc_fallada`, `A7_texe_diagrama` (`gen_T7.py`), deu de T8 (`gen_T8.py`) i `A9_cicle_interrupcio`— i 10 originals conservats que el llibre no consumeix (els cinc de T3 de la família de memòria i cinc de T7, D-68). Els generadors es corregeixen al generador; els SVG natius, a mà. Toca figures d'A2–A5 i A7–A9 i del compendi. Mesurat el 2026-10-07 sobre `auto_figs/` (cal un render previ), sense els fotogrames `_pas`.

  ```bash
  python3 - <<'PY'   # 54 {'registre': 17, 'original': 30, 'MC': 7}
  import re, glob, collections
  r = collections.Counter()
  for f in sorted(glob.glob('auto_figs/*_light.svg')):
      if '_pas' in f: continue
      R = [(float(a['x']), float(a['y']), float(a['width']), float(a['height']), a.get('stroke', 'none').lower(), a.get('fill', '').lower())
           for a in (dict(re.findall(r'([\w-]+)="([^"]*)"', m)) for m in re.findall(r'<rect\b([^>]*)>', open(f).read()))
           if 'transform' not in a and all(k in a for k in ('x', 'y', 'width', 'height'))]
      def xoc(p, q):
          (x1, y1, w1, h1, s1, f1), (x2, y2, w2, h2, s2, f2) = p, q
          toca = ((abs(y1 + h1 - y2) < .01 or abs(y2 + h2 - y1) < .01) and min(x1 + w1, x2 + w2) - max(x1, x2) > 1) or \
                 ((abs(x1 + w1 - x2) < .01 or abs(x2 + w2 - x1) < .01) and min(y1 + h1, y2 + h2) - max(y1, y2) > 1)
          if not toca: return False
          if 'none' not in (s1, s2): return s1 != s2                        # dos traços de color diferent
          return (s1 == 'none') != (s2 == 'none') and (f1 if s1 == 'none' else f2) not in ('none', '')   # un farciment tapa mitja vora
      if any(xoc(p, q) for i, p in enumerate(R) for q in R[i + 1:]):
          r[f.split('__')[-1].replace('_light.svg', '')] += 1
  print(sum(r.values()), dict(r))
  PY
  ```

- **Revisió de la paleta de colors per reduir-ne la quantitat** (petició de l'usuari, 2026-10-06, en migrar els colors llegats a la paleta). Després de la migració, la paleta de `24_specs/svg.md §10` i `§16` té 20 colors, i alguns papers es repeteixen amb tons gairebé iguals: dos vermells de traç (`#cc0000`, dependències de dades; `#dc3545`, fallada), dos fons rosats (`#f8d7da`, `.text`; `#f8d0d3`, fallada), dos fons verds (`#d1e7dd`, heap; `#c8ebd8`, encert), dos fons blaus (`#cfe2ff`, `.data`; `#e6f1fb`, zona o contenidor) i cinc grisos (`#f8f9fa`, `#dee2e6`, `#adb5bd`, `#6c757d` i `#343a40`). Cal decidir quins es fusionen i amb quin paper; cada fusió vol dir regenerar o editar les figures que el fan servir (`25_scripts/inventari_figures.py` les llista per color) i retirar-ne l'entrada de §13.

  ```bash
  python3 -c "import re; md=open('24_specs/svg.md').read(); s=md.split('## 10.')[1].split('## 11.')[0]+md.split('## 16.')[1].split('## 17.')[0]; print(len({c.lower() for c in re.findall(r'#[0-9a-fA-F]{6}', s)}))"   # 20, 2026-10-06
  ```

### Contingut global

- **Equacions a MathML**: **decisió presa — mantenir MathJax 3**; el pendent és reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa). Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`): funciona (`underbrace`, `cases`, taules amb math correctes a Chrome) i elimina el JS de MathJax (render instantani, offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), numeració d'equacions inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. El desbordament mòbil ja està resolt via CSS.

- **PDF: comportament de `layout=` en callouts encastats**: es respecta la separació (`-1` del `layout=`), però no el repartiment si hi ha línies de text que no hi caben (falta l'exemple concret). ⚠️ **No se sap de quin format és**: fins al 2026-10-07, `13_contrib.qmd §Imbricacions` en tenia la mateixa observació amb el títol «HTML: comportament en callouts encastats», i aquesta entrada diu PDF; cap de les dues no porta cap exemple. Aquella subsecció s'ha tret de la guia en partir-la (fase 7e), perquè era una observació sense verificar i no una regla, i aquesta entrada n'és ara l'única còpia (`git show a125e3f:13_contrib.qmd`, línies 843–845). *(Fins al 2026-10-06 aquesta entrada començava amb «figures dins callouts no queden centrades → investigar via `preamble.tex`», que és a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades → Executades.)*

- **Gestió d'errades post-commit**: definir protocol. La capçalera buida `### Gestió d'errades` de `13_contrib.qmd` (a `ebdf055`, `:779`, seguida directament de `## Eines`) se'n va treure el 2026-10-07, en partir la guia (fase 7e): la tasca queda només aquí. Quan es defineixi el protocol, tindrà secció pròpia a `13_contrib.qmd §Eines`.

- **HTML: un índex de continguts de tot el llibre, com el del PDF** (petició de l'usuari, 2026-10-09: «Té sentit a la versió HTML afegir un índex de continguts per poder tenir una visió general? (com en el PDF)»). Avui l'HTML en té dos de parcials: la barra lateral, amb els capítols (les parts, plegades: `sidebar: collapse-level: 1`), i la «Taula de continguts» de cada pàgina (`toc: true`, a l'esquerra), amb les seccions del capítol obert i prou. Cap vista no mostra les seccions de tot el llibre alhora, que és el que dona l'índex del PDF. **Valoració de Claude Code**: té sentit, per a la visió general (també per als revisors), i és barat. Un script de `pre-render`, com el de les taules de `auto_riscv/`, llegeix les capçaleres `#` i `##` dels `chapters:` de `_quarto.yml`, en l'ordre del llibre, i en genera una llista d'enllaços (`[1.4 Codificació…](01_apunts/A1.qmd#sec-…)`) que es mostra només a l'HTML (`::: {.content-visible when-format="html"}`), plegada per parts. Els títols i els enllaços surten del text: no s'han de mantenir a mà. No toca A1–A8. ✅ **Decidit per l'usuari** (2026-10-09): profunditat fins a `###`; i una pàgina pròpia entre «👋 Presentació» i «Apunts», no dins de la Presentació, perquè «és massa llarga per formar part de 👋 Presentació». El punt delicat és el PDF: la pàgina ha de ser un capítol per sortir al menú de l'HTML, però no ha de deixar res al PDF. Sessió nova: Opus, effort alt; un commit, amb `make render-complet` per comprovar que el PDF no canvia.

### Eines

- **Valorar si les taules de `21_riscv/` haurien de passar a `.json` o `.toml`** (petició de l'usuari, 2026-10-02, per al futur). Avui són 44 fragments `.qmd` (`git ls-files 21_riscv | grep -c "\.qmd$"`, a `4658e90`) amb files de taula *pipe*, inclosos amb `{{< include >}}` als callouts dels temes i a `11_riscv.qmd`; les taules que combinen fragments es fusionen amb `25_scripts/gen_taules_auto.py` i `24_specs/taules_fusio.toml`, que s'han d'executar a mà abans del render. Una font estructurada permetria generar les taules (i les fusions) per script i validar-ne el contingut; el cost és un generador nou i una dependència més del render. Cal valorar-ho abans de decidir res.

- **Protocols d'execució dels generadors i de les comprovacions, per nivells** (petició de l'usuari, 2026-10-09, literal: «En algun moment caldrà explicitar els protocols d'execució dels scripts generadors i de testeig. Penso que cal definir nivells (per exemple "commit menor", "commit major", "revisió estètica", "revisió de continguts", "refer llista de continguts") perquè tal com està ara em sembla que hi ha testos innecessaris (per exemple, no cal renderitzar quan només hi ha canvis a `TODO.md`)»). ✅ Ja fet, el 2026-10-09: el hook d'abans del commit se salta el `make render` quan el render no llegeix cap fitxer canviat ([D-61](24_specs/registre_de_decisions.md#d-61)). Queda la resta: l'inventari de les comprovacions (el hook, el `Makefile`, els verificadors i els `--comprova` de `25_scripts/`, les skills, els subagents), què les dispara, quant triguen i què detecten, i una taula de nivells (quina mena de canvi demana quines comprovacions) que el hook pugui deduir dels fitxers canviats. Sessió nova: Opus, effort alt; la proposta, abans de canviar res.

### `index.qmd`

- **Consolidar les versions de la taula de referències tècniques** (`#imp-llenguatges-de-referencia`). Cinc marcadors vius, `index.qmd:195-199`, que són **tres pendents distints**:

  | Marcadors | Pendent |
  | :--- | :--- |
  | `:195`, `:196` | Versió de la norma **ISO de C** (i si és tancada). La taula ja cita `[@iso9899_2024]`: el pendent és **verificar i tancar**, no decidir de zero |
  | `:197`, `:198` | Versió de **GCC** (`[@gcc16]`), i consolidar noms i versions de totes les files |
  | `:199` | **Versió numèrica o de data per a CSR** (fila de RISC-V, `[@riscv_csrs]`): decidir si la referència s'identifica per número de versió o per data. ✅ **No constava en cap registre anterior** |

  La fila duplicada de *Toolchain* ja no hi és (verificat 2026-07-13: la taula té una sola fila per ítem).

