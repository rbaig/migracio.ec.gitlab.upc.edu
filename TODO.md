# TODO

Reescrit el 2026-09-21 (auditoria, sessió 3) a partir d'un inventari complet:
les 58 entrades del `TODO.md` anterior, els 29 marcadors del corpus, els quatre
informes de l'auditoria i els registres de tasques del `TODO/`. Cada
entrada porta la comprovació que la sosté. Les entrades retirades són al
§Entrades retirades del final, amb el motiu i la còpia que en queda.

**39 entrades vives** (recompte del 2026-10-03, després de la fase 7b: se'n retiren cinc, executades —de §Tasques per tema → T2, «Verificació tècnica de la taula de restriccions d'alineació» i «La taula de l'exemple `#tip-codificacio-instruccions` surt del callout al PDF»; de §Decisions obertes, «Unificar el format de les taules de pseudoinstruccions»; i de §Tasques transversals, «Guany, no *speedup*…» i «`L2.qmd:153-166` — alineació de `.dword` a RARS»—, i n'entren quatre: a §Decisions obertes, «Pseudoinstruccions: un sol esquema de columnes i un sol prefix de títol» i «Figures i taules amb etiqueta dins dels callouts `#nte-`»; a §Tasques transversals, «Revisar la distribució de les columnes de totes les taules»; i a §Tasques per tema → T3, «`auipc` no és al compendi ni té taula ISA». Recompte anterior del 2026-10-03, després de la fase 7: es retira de §Decisions obertes «Sigles: VPN i PPN», decidida; abans, es retira de §Tasques per tema → T6 «Etiquetes de classe d'instruccions en anglès», executada. Recompte anterior del 2026-10-03, fase 7: es retira de §Tasques transversals «Revisió sistemàtica del corpus per nodrir les taules de `Símbols` i `Notació`», executada; entren a §Tasques transversals «Guany, no *speedup*, a E6, S6 i `S_criteris_seleccio.qmd`» i a §Decisions obertes «Sigles: VPN i PPN són a la taula, i el criteri d'inclusió les exclou». Recompte anterior del 2026-10-03, després de la fase 5: entra a §Tasques globals → Eines «Font monoespaiada del PDF». Recompte del 2026-10-03, fase 5: es retira de §Decisions obertes «Figures de half-adder i full-adder (T4)», executada; entren a §Tasques transversals «Confirmar al Termcat “semisumador” i “sumador complet”» i «Revisió general de les figures i generació per script». Recompte anterior del 2026-10-03: entren a §T2 «La taula de l'exemple `#tip-codificacio-instruccions` surt del callout al PDF» i a §Tasques globals → SVG «Text de figura en gris de traç», totes dues detectades a la fase 4. Recompte del 2026-10-02: es retira de §Decisions obertes «Anotacions de la revisió externa de T3», amb els vuit comentaris resolts; es retira de §T2 «La figura de `#nte-instruccions-tipus` mostra els set formats», executada a la fase 4; entren a §Tasques globals → Eines «Identificador del commit a la data de publicació» i «Valorar si les taules de `21_riscv/` haurien de passar a `.json`», per al futur; es retira «R5-TYPE (RISC-V *compressed*) com a aprofundiment», decidida «no» a la fase 6, i «R4-TYPE a T5», decidida «sí, com a aprofundiment» i executada; entra a §T2 «La figura de `#nte-instruccions-tipus` mostra els set formats». Recompte del 2026-10-01: entren «Anotacions de la revisió externa de T3», en portar la MR `!5`, i «Tres SVG orfes de T5», i es retiren la regla d'ús d'`AND`/`OR`, les cometes i l'ordre substantiu–adjectiu de T5 i els quatre formats a A3, executades; es retiren «Passades finals pendents», perquè es tanca tota la revisió interna; «Terminologia anglesa a la prosa d'E/S», que va entrar i es va executar el mateix dia; el criteri global dels quatre formats nuclears, les expressions als operands d'E/S i la grafia de «No-associativitat» i el format de les adreces; entren i s'executen «Tanques de codi fora de la convenció» i «Veu dels enunciats»; es retira «Exercicis → Problemes»; entra l'inventari del grup de treball de T4–T6; «Ordre substantiu–adjectiu» passa de §Decisions obertes a §Tasques transversals, perquè ja està decidit). Una entrada = una vinyeta de primer nivell (`^- `) per
sobre de `## Entrades retirades`; les vinyetes indentades en són sub-ítems i no
compten. Ordre que ho mesura:

```bash
head -n $(($(grep -n "^## Entrades retirades" TODO.md | cut -d: -f1) - 1)) \
  TODO.md | grep -cE '^- '
```

Repartiment: `§Decisions obertes` 9 · `§Tasques transversals` 6 ·
`§Tasques per tema` 12 · `§Tasques globals` 12 (suma 39, regla 12 bis).
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

  📌 **Estat a 2026-10-03.** El marcador del *checker* (`A2.qmd:729`) s'ha esborrat: l'eina és `25_scripts/verifica_format_codi.py` (decisió de l'usuari). Decidit i aplicat el mateix dia: «tabulat» → «8 espais» al callout, i les 101 línies d'instrucció o dada sense els 8 espais (E2 73, S2 19, E4 5, A1 2, A5 2), indentades. **Queden dues decisions**: (1) el marcador «hi ha consens?», i (2) si s'afegeix al callout l'alineació dels operands en columna, que l'usuari va acceptar sobre una xifra que Claude Code havia mesurat malament: va donar 1 179 línies alineades contra 605 amb un sol espai, i la regla F5 del *checker*, que compta totes les formes (també les directives i les línies amb etiqueta), en troba **849 fora de columna** de 2 768 línies de codi, un cop indentades les 101 de dalt; el 61% són als laboratoris (L3 169, L6 161, L2 71, L4 60, L5 57). Aplicar-la vol dir reformatar aquestes 849 línies. **Totes dues van a la reunió del grup de treball del 2026-10-05** (decisió de l'usuari), a l'apartat «Per decidir a la reunió: format del codi» de la nota «EC — Canvis a A3–A6 després de la revisió externa», que hi afegeix una tercera pregunta: si el format s'avalua. Context per a la reunió: els materials MIPS originals no tenien cap criteri de format (`PDF_originals/`; només el quadern de la sessió 0 diu que els comentaris comencen per `#`), i el marcador hi és des del primer esborrany (`1d57f8d`, 2026-04-27).

  ```bash
  python3 25_scripts/verifica_format_codi.py            # F3 0 i F5 849 a l'arbre de treball sobre 8e19383
  ```

- **Figures portades d'extern: afegir-ne la font.** Dels PDF originals n'hi ha que són del Patterson (p. ex. T7 MC). Abast actual verificat: dues figures de T7 encara es consumeixen en versió `__extern_` (export de PDF, no nativa) — `A7.qmd:365,368,372` (`T7_assoc_conjunts_diagrama__extern_*`) i `A7.qmd:303,306,310` (`T7_cd_diagrama__extern_*`). Enllaça amb `§Contingut global → Figures externes (llicències)`.

- **Taules de memòria de T2 → figura estàndard** (`A2.qmd:964`, `:1002`, mesurat a `ebdf055`): dos marcadors amb la mateixa tasca sobre dues taules diferents — la segona és dins de `#tip-endianness` i afecta `#fig-big-endian`/`#fig-little-endian`. Pendent de figura, no de decisió, però no hi ha secció de figures de T2 en aquest fitxer: hi entra aquí fins que se'n creï una.

- **Pseudoinstruccions: un sol esquema de columnes i un sol prefix de títol** (registrada el 2026-10-03, fase 7b). És l'opció B de l'entrada «Unificar el format de les taules de pseudoinstruccions» (avui a §Entrades retirades → Executades): l'usuari va triar l'A, que unifica A2 i afegeix `la` al compendi, perquè la B toca fitxers en revisió externa. A `a7876b9` hi ha 16 taules (A2 4, A3 5, A4 1, `11_riscv.qmd` 6): 15 de pseudoinstruccions, amb cinc esquemes de columnes, i la de la notació EC de `#imp-ec-la-offset`. Els esquemes: «Pseudoinstrucció, Operació, Expansió» (6), «Pseudoinstrucció, Expansió, Ús» (3), «Pseudoinstrucció, Condició, Expansió» (2, `li`), «Pseudoinstrucció, Expansió, Condició» (2) i «Pseudoinstrucció, Expansió» (2). «Condició» hi vol dir dues coses: a `li`, quan s'aplica cada expansió; als salts amb zero, la condició del salt, escrita amb la sintaxi de C («salta si `rs == 0`») i no amb la de les taules ISA. Els títols dels callouts fan servir dos prefixos, «Pseudoinstrucció —» (A2; A3, `not`; A4) i «RV32I ABI —» (A3, els salts, i el compendi; A5, «RV32F ABI —»), i les pseudoinstruccions no són ABI: les defineix el manual de l'assemblador. `13_contrib.qmd §Callouts` dona `## Pseudoinstruccions — `. Proposta: «Pseudoinstrucció, Operació, Expansió» a totes, amb l'operació en la notació de les taules ISA ($rs = 0 \,?\, PC \leftarrow \ldots$), `li` amb una columna més per a la condició, i un sol prefix. Toca A3, A4 i A5 (revisió externa de T3–T6) i set fragments de `21_riscv/`: s'ha de coordinar amb el grup de revisió, per exemple a la reunió del 2026-10-05.

  ```bash
  git grep -h -E '^\| (Pseudoinstrucció|Notació EC) \|' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' | sort | uniq -c   # 6 capçaleres, 16 taules a a7876b9
  git grep -n -E '^## .*[Pp]seudoinstrucci' -- '*.qmd' ':!13_contrib.qmd'                                          # els títols
  ```

- **Figures i taules amb etiqueta dins dels callouts `#nte-`** (registrada el 2026-10-03, fase 7b). `13_contrib.qmd §Callouts` diu que les figures i taules internes dels `#nte-` van «sense etiqueta ni caption», i a `a7876b9` n'hi ha 17 amb etiqueta: 15 figures i 2 taules (A2 6, A3 2, A5 1, A9 8), entre elles `#tbl-tipus-alineacio` (A2) i `#tbl-syscalls-rars` (A9). **Cap de les 17 no té cap referència** (comprovat una per una amb `git grep -o "@<etiqueta>\b"`). O es treuen les etiquetes, i amb elles el número de figura o de taula que generen, o es canvia la convenció. Ordre que les compta (un `div` sense `#` al davant, com `::: {tbl-colwidths=…}`, no és una etiqueta):

  ```bash
  python3 - <<'EOF'   # 17 a a7876b9
  import re,subprocess
  n=0
  for f in subprocess.run(['git','ls-files','*.qmd',':!TODO.md',':!13_contrib.qmd'],capture_output=True,text=True).stdout.split():
      st=[];code=False
      for l in open(f,encoding='utf-8'):
          if re.match(r'(```|~~~)',l): code=not code; continue
          if code: continue
          m=re.match(r':{3,}\s*\{(?:#([\w-]+))?',l)
          dins=any(s.startswith('nte-') for s in st)
          if m: n+=dins and (m.group(1) or '').startswith(('fig-','tbl-')); st.append(m.group(1) or ''); continue
          if re.match(r':{3,}\s*$',l): st and st.pop(); continue
          n+=dins*len(re.findall(r'\{#(?:fig|tbl)-',l))
  print(n)
  EOF
  ```

- **Marcadors de codi deliberadament incorrecte sense categoria a `13_contrib.qmd`.** Els marcadors `⚠️ codi_erroni__*.c ⚠️` i `⚠️codi_erroni__*.s⚠️` no són ni llenguatge ni context: són una marca semàntica de «codi deliberadament incorrecte», i la taula de `13_contrib.qmd §Blocs de codi` no en preveu la categoria. Cal decidir si mereixen fila pròpia. Ús actual verificat (2026-09-24; línies re-mesurades a `ebdf055`): **4 blocs**, tots a `A2.qmd` — `:436` `⚠️codi_erroni__nom_reservat.s⚠️`, `:832` `codi_erroni__gcc_tipus.c`, `:1080` `⚠️codi_erroni__alineacio_incorrecte.s⚠️`, `:1806` `⚠️ codi_erroni__vectors.c ⚠️`; `grep -n "codi_erroni\|deliberadament incorrecte" 13_contrib.qmd` → cap fila. *(Detectat a la passada C; registrat aquí perquè l'informe que el contenia és transitori.)*

  ```bash
  git grep -n 'filename="[^"]*codi_erroni' -- '*.qmd' ':!TODO.md' | wc -l   # 4
  ```

  ⚠️ Les tres línies que aquesta entrada publicava abans (`:794`, `:1042`, `:1770`) **eren correctes quan es van escriure** —es comprova amb `git show 7e415a4:01_apunts/A2.qmd`— i han caducat perquè `A2.qmd` ha crescut. És la regla 11: una xifra només és certa respecte del commit on es va mesurar. Per això les d'ara van datades.

  📌 **Argument nou a favor de la fila pròpia (2026-09-24): el marcador també serveix per excloure el bloc de les escombrades del corpus.** El quart bloc és el contraexemple d'`@nte-rars-noms-reservats`, que conté a posta un `.eqv B, 16` amb un nom reservat. Sense marca, una escombrada d'identificadors el compta com a **xoc real** (17 símbols `.eqv`, amb `B` a `A2.qmd:437`, mesurat a `ebdf055`) i, per la regla d'aturada, obliga a parar-se a decidir si ho és — a l'exemple escrit precisament per ensenyar el xoc. Amb la marca al `filename`, l'exclusió es pot fer **per forma** (`codi_erroni` a la tanca) i no amb una llista de línies que caduca: el compte torna a 16 i a zero xocs. Un marcador que és alhora senyal per al lector i predicat per a les eines és un argument que no es veia amb els tres blocs anteriors, cap dels quals no conté identificadors que cap escombrada miri.

  Avui no trenca res: `25_scripts/verifica_laboratoris.py` només processa `04_laboratori/L*.qmd` (`LAB_DIR` + `L*.qmd`, `:24` i `:279`, mesurat a `ebdf055`), de manera que `A2.qmd` li queda fora d'abast. El risc apareix el dia que l'abast creixi o que algú escombri identificadors a tot el corpus.

- **Branques del remot: les MR de la revisió externa de T4–T6 (`!7`, `temes456`) i de T3 (`!5`, `contingut/t3-traduccio`) es van tancar sense fusionar el 2026-10-01; `temes456` es va fusionar a `main` el mateix dia (`451c3ef`), i `!5` s'hi va portar també el mateix dia (`ab48732`)** (registrada 2026-09-23; T3, les MR i el tancament, 2026-10-01; la fusió, 2026-10-01).

  ✅ **`temes456` fusionada a `main` el 2026-10-01: `451c3ef`**, commit de fusió sense *rebase* (pares `e3a7cc3` i `661733b`), que conserva l'autoria dels 11 commits. Tres conflictes, resolts amb l'aprovació de l'usuari: `.gitignore` (totes dues línies), `A4.qmd` (`#imp-eqv-dimensions`: la frase del revisor i el paràgraf de `main`) i `A5.qmd` (ULP i RNE: la línia de `main`, amb la marca dels termes anglesos i «de menys pes»). Després, dos commits sobre el que la branca portava sense conflicte: `40396e8` (set errades: `\text{CPI}{i}` sense subíndex, «pot emprat», «ext.ensió»…) i `454a82e` (restaura la marca dels termes anglesos, de les sigles i d'«A **EC**», que el revisor treia contra `13_contrib.qmd`). La resolució sencera: `git show --cc 451c3ef`. Les branques remotes **no s'han esborrat**: és decisió del grup, amb l'etiqueta d'arxiu de `13_contrib.qmd §Convenció de noms de branques`.

  ```bash
  git merge-base --is-ancestor origin/temes456 origin/main && echo dins || echo fora   # dins, des de 451c3ef
  ```

  ✅ **`!5` (`62700c0`) portada a `main` el 2026-10-01: `ab48732`**, amb `Co-authored-by` de Pedro J. Martinez-Ferrer. Fusió a tres bandes per fitxer (base `62700c0^`, la branca i `main`), sobre les rutes actuals (`01_apunts/A3.qmd`, `21_riscv/`). De 46 hunks: 1 ja aplicat (`RV32I_instruccions_comparacio.qmd`), 1 equivalent ja aplicat (A3, «als quals s'escriu»), 6 conflictes resolts conservant tots dos costats, i 2 refusats per l'usuari: «*double-word*» com a variant de `lw`/`sw` (RV32I no en té) i una línia en blanc dins d'un bloc de codi. Ajustos aprovats: la sigla LIFO segueix §Sigles, i els comentaris del revisor porten `TODO: ` (entrada «Anotacions de la revisió externa de T3»). Detall al missatge del commit. `contingut/t3-traduccio` no se n'ha fet ancestre —el port és un commit nou, no una fusió—, de manera que `git merge-base --is-ancestor` hi continuarà dient «fora»: el que ho certifica és `ab48732`.

  📌 **Estat a 2026-10-01, 16:21: totes dues MR tancades sense fusionar**, per `pedro.martinez.ferrer` (`!5` a les 16:20 i `!7` a les 16:21). `!7` tenia `merge_status: cannot_be_merged`, coherent amb els tres conflictes de la fusió de prova de més avall. Les branques continuen al remot, sense cap commit nou: `temes456` a `661733b`, amb 11 commits fora de `main`, i `origin/main` sense cap fusió. **Decisió de l'usuari: s'espera el grup de treball**, que la refarà o la reobrirà, i `A3.qmd`–`A6.qmd` no es toquen. ⚠️ **Substituïda el mateix dia**, després de rebre l'inventari del grup (entrada següent): **la fusió de `temes456` i el port de `!5` els fa una sessió de Claude Code** (decisió de l'usuari), amb la resolució de cada conflicte i els casos dubtosos del port presentats a l'usuari abans del push. La fusió es fa amb un commit de fusió, per conservar l'autoria dels 11 commits; el port porta `Co-authored-by` de l'autor. Es va saber per `glab`, en preparar dues tasques que l'usuari donava per desbloquejades perquè creia que `!7` s'havia fusionat: «tancada» no és «fusionada», i això només ho diu GitLab, no el clon.

  ```bash
  glab api 'projects/7916/merge_requests/7' | jq -r '"\(.state) · fusionada: \(.merged_at // "no") · tancada: \(.closed_at // "no")"'
  git merge-base --is-ancestor origin/temes456 origin/main && echo dins || echo fora   # fora (fins a 451c3ef)
  ```

  Les branques es registren, **no es toquen**: cap fusió, cap esborrat, i les fusions les farà el grup de treball. ⚠️ **Superat el 2026-10-01** per la decisió de l'usuari del paràgraf anterior: les fusions les fa una sessió de Claude Code; l'esborrat continua sent del grup.

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

  ⚠️ **La branca toca dues fonts de veritat**, no només prosa: `24_specs/registres.toml` i `22_figs_originals/T5_ieee754_format_registre.svg` — els dos fitxers que l'entrada «Ordre substantiu–adjectiu» (avui a §Entrades retirades → Executades) identificava com a font de la figura de T5. Conciliar-los vol dir **regenerar**, no només fusionar. També toca `.gitignore` (3 línies).

  `contingut/t3-traduccio` (un commit, `62700c0`, 2026-07-06, Pedro J. Martinez-Ferrer) porta **rutes d'abans del refactor de directoris** (`c5d9416`): `01_T/T3.qmd` i `11_riscv/…`, camins que avui no existeixen. **Qualsevol fusió és manual**, perquè git no pot resseguir el canvi de nom a través del refactor.

  ⚠️ **És la revisió externa de T3, amb MR oberta: `!5`, «T3: revisió del tema (canvis i comentaris)», oberta el 2026-07-06 i sense cap comentari a GitLab.** Fins al 2026-10-01 aquesta entrada la registrava com a branca però no com a revisió, i `CLAUDE.md` deia que, fora de T4–T6, la revisió externa «encara no ha començat». Ho va treure a la llum `glab`, no `git`: una branca no diu si té una MR al darrere. **Decisió de l'usuari (2026-10-01): el port a les rutes actuals (`01_apunts/A3.qmd`, `21_riscv/`) el fa l'autor de la MR.** Fins llavors `A3.qmd` no es toca, perquè cada canvi que hi entri és un conflicte més per al port. ⚠️ **Substituïda el mateix dia** (el port el fa una sessió de Claude Code), i **executada: `ab48732`**. `A3.qmd` ja es pot tocar.

  ```bash
  glab api 'projects/7916/merge_requests?state=opened' | jq -r '.[] | "!\(.iid) \(.source_branch) · \(.author.name) · \(.title)"'
  # !7 temes456 · pedro.martinez.ferrer · Revisió del temes 4,5 i 6
  # !5 contingut/t3-traduccio · pedro.martinez.ferrer · T3: revisió del tema (canvis i comentaris)
  ```

  📌 **`build` existeix només al mirall de GitHub, i no s'ha de tocar.** No és a `origin` (GitLab). El seu únic commit és `6d5d2cf` (2026-09-19), d'autor `github-actions[bot]` i assumpte «Render de 38f0ebc»: és **sortida de CI generada a GitHub**, que per això no arriba a GitLab —i el `38f0ebc` que cita no resol en aquest clon, per la mateixa raó—. El `publish.yml` actual ja no l'escriu: desplega amb `upload-pages-artifact` i `deploy-pages` (`:81`, `:94`). No és residu del `d4086cd` de juliol ni feina de ningú.

  ⚠️ **Mesureu les branques amb `git ls-remote`, i digueu de quin remot parleu** (regla 13 de `13_contrib.qmd §Escombrades i verificació del corpus`). En registrar aquesta entrada, `git branch -r` va fer declarar `build` inexistent —ho és a GitLab, no al mirall— i va fer registrar `T3-review-adria` i `to-trash` com a existents, quan eren **referències de seguiment obsoletes** d'aquest clon: ja no són a cap dels dos remots, i `git fetch mirror --prune` les ha tretes.

- **Anotacions de la revisió externa de T4–T6: inventari i pla del grup de treball** (document lliurat a l'usuari el 2026-10-01, generat pel grup amb Claude Code; aquesta entrada n'és l'única còpia al repositori). Verificat contra el repositori el mateix dia: `5a737f2` (2026-07-21) és la fusió de `!6`, i ja és a `main`; queden 11 commits de `temes456` fora de `main` (`fc14bea`…`661733b`), entre ells `7dc4746`; hi ha 4 marcadors a `main` (A4 2, A5 2) i 14 a la branca; les cinc àncores de les anotacions [br] existeixen tant a `main` com a la branca. **[main]** vol dir que el marcador ja és a `main`, i **[br]** que només és a la branca, tot i que el problema que descriu també és a `main`.

  | # | Tema | Anotació | Valoració del grup |
  | ---: | :--- | :--- | :--- |
  | 1 | T4 | [main] Figures del *half-adder* i del *full-adder* (`#wrn-sobreeiximent-maquinari`); en SVG natiu, juntament amb la #2 | Factible. ✅ **Resolta (2026-10-03, fase 5)**: `#fig-semisumador-sumador-complet` (`22_figs_originals/T4_semisumador_sumador_complet.svg`, generat per `25_scripts/gen_T4_sumador.py`), amb (a) el semisumador i (b) el sumador complet fet amb dos semisumadors i una OR, i les etiquetes dels senyals intermedis de l'equació de $c_{i+1}$. El text anomena ara el semisumador. Convenció de les portes: `24_specs/svg.md §16`. Termes «semisumador» i «sumador complet», pendents de confirmar al Termcat (§Tasques transversals). Marcador esborrat. |
  | 2 | T4 | [main] Figura de la cadena de *full-adders* amb una XOR per al sobreeiximent: sí que cal, perquè il·lustra l'equació del maquinari | Factible . ✅ **Resolta (2026-10-03, fase 5)**: `#fig-sumador-propagacio-rossec` (`22_figs_originals/T4_sumador_propagacio_rossec.svg`, del mateix generador que la #1), amb la cadena de sumadors complets del bit $n-1$ al $0$, el ròssec de dreta a esquerra i la XOR de $c_{n-1}$ i $c_n$ que dona $v$, ressaltada en rosa (`24_specs/svg.md §16`). Marcador esborrat. |
  | 3 | T4 | [br] Moure `#cau-sobreeiximent-extensio-m` a §Sobreeiximent en la multiplicació | Important. ✅ **Resolta (2026-10-01, fase 3)**: el callout, literal, és ara a §Sobreeiximent en la multiplicació, després del paràgraf que presenta el truncament de `mul`. No tenia cap remissió entrant, i les dues que conté apunten enrere. Marcador esborrat. |
  | 4 | T4 | [br] Algorismes en cursiva i blocs titulats només «Pseudocodi» (multiplicació i divisió): cal fixar-ne una convenció a `13_contrib.qmd` | Factible. **Convenció escrita (2026-10-01, `13_contrib.qmd §Blocs de codi`) i títols aplicats** als quatre blocs (`A4.qmd:186`, `:386`, `:749`; `S4.qmd:804`). **Queda la cursiva**, que és del PDF: `\theoremstyle{plain}` per a `theorem` al `.tex` generat; va a la passada de render (fase 4). El marcador `A4.qmd:181` es manté fins llavors. ✅ **Cursiva resolta (2026-10-02, fase 4)**: `preamble.tex` redefineix `\th@plain` a `\AtBeginDocument` (amsthm resol l'estil pel nom a cada ús, i Quarto el declara després del preàmbul); el cos dels blocs Algorisme surt en rodona al PDF (verificat a «Algorisme 4.1»). Marcador esborrat. |
  | 5 | T5 | [main] Introduir el R4-TYPE? La figura existeix i no s'usa; només té sentit si el tema tracta les instruccions FMA | Decisió. ✅ **Decidida: sí, com a aprofundiment** (usuari, 2026-10-02, fase 6): `#wrn-instruccions-fusionades` a A5 §Instruccions, amb la figura R4 (`#fig-format-r4`) i l'arrodoniment únic de les FMA. Marcador `A5.qmd:5` esborrat; entrada retirada a §Entrades retirades → Executades. |
  | 6 | T5 | [main] R5-TYPE (*compressed*) com a aprofundiment: fora de l'abast de T5; en tot cas, a T2 | No val la pena. ✅ **Decidida: no** (usuari, 2026-10-02, fase 6). Marcador `A5.qmd:6` esborrat; entrada retirada a §Entrades retirades → Executades. |
  | 7 | T5 | [br] «denormals» no es llegeix bé a `#fig-recta-global` | Render. ✅ **Resolta (2026-10-02, fase 4)**: a `22_figs_originals/T5_recta_global.svg`, el «denormals» de la recta positiva començava fora del `viewBox` (`x=42`, ancorat a la dreta) i sortia tallat («enormals»), i tots dos eren en gris de traç (`#adb5bd`), poc llegible a la mida del PDF. Ara són en gris de text neutre (`#6c757d`, `24_specs/svg.md`; al fosc, `#adb5bd`), i el de la recta positiva acaba a `x=60`, amb la fletxa grisa escurçada fins a `x=72`. Marcador esborrat. |
  | 8 | T5 | [br] Fórmules de `#tip-suma-ieee754`: les mantisses llargues poden sortir del marge al PDF | Render. ✅ **Verificada sense canvi (2026-10-02, fase 4)**: al PDF de `c14f448` (pàgines 184–185 del fitxer), dins del callout la prosa justificada acaba a x ≈ 524 pt i cap fórmula no hi arriba (`pdftotext -bbox`). No sortien del marge. Marcador esborrat. |
  | 9 | T6 | [br] Els exemples de §Definicions barregen temps d'execució i rendiment: cal enunciar abans la relació | Important. ✅ **Resolta (2026-10-01, fase 3)**: `#eq-rendiment` («A EC, el rendiment es mesura amb el temps d'execució») i el bloc «Quina diferència hi ha entre temps d'execució i rendiment?» passen davant dels dos exemples, i la resposta dels exemples diu que A té més rendiment. Les subseccions es diuen ara «Temps d'execució, rendiment i productivitat» i «Guany de rendiment» (cap dels dos slugs antics no tenia remissions). A més, decisió de l'usuari: la definició de rendiment com a «quant de treball per unitat de temps», que era la de productivitat, passa a «quantes vegades es pot executar la tasca per unitat de temps, l'una darrere l'altra». Marcador esborrat. |
  | 10 | T6 | [br] La llegenda de $t_c$ a `#fig-tc-tc-prima` no es renderitza | Render. ✅ **Resolta (2026-10-02, fase 4)**: no era el peu de figura, sinó l'SVG. Cada etiqueta amb subíndex («t<sub>c</sub>», «2t<sub>c</sub>'», «disseny inicial amb temps t<sub>c</sub>», «disseny amb temps t<sub>c</sub>' menor») eren `<text>` separats amb `textLength`, que `rsvg-convert` (el que fa servir Quarto per al PDF) no implementa: al PDF els textos eren més amples que l'espai reservat i trepitjaven el subíndex, i els dos rètols sortien del `viewBox`. Ara cada etiqueta és un sol `<text>` amb `<tspan dy>` per al subíndex, sense `textLength`, i els rètols passen de 10,07 a 9 px perquè hi càpiguen. Marcador esborrat. |
  | 11 | T6 | [br] Equació massa llarga a `#tip-comparacio-cpua-cpub`: cal partir-la | Factible. ✅ **Resolta (2026-10-02, fase 4)**: al PDF de `c14f448` (pàgina 199 del fitxer) arribava a x = 543,75 pt, uns 20 pt més enllà de la vora interior del callout. Partida en dues línies amb `aligned`, alineades a `=`; de pas, `1,33` → `1{,}33` (`13_contrib.qmd §Nombres decimals`). Marcador esborrat. |
  | 12 | T6 | [br] Reordenar §Potència (tres anotacions): definició i equació primer, Moore i Dennard al final de §Potència estàtica. Ampliació possible: miniaturització i reducció del consum (`7dc4746`) | Important (ordre); Decisió (ampliació). ✅ **Ordre resolt (2026-10-01, fase 3)**: §Potència comença per la definició i `#eq-potencia`; el paràgraf de Moore, el de miniaturització i `#wrn-dennard` són ara a una subsecció nova, `### Miniaturització i límit tèrmic` (`#sec-miniaturitzacio-i-limit-termic`), darrere de §Potència estàtica (decisió de l'usuari: capçalera pròpia, perquè no és potència estàtica). La frase que tancava §Potència estàtica amb Dennard es fusiona amb la que tanca el paràgraf de miniaturització; `#wrn-dennard` remet ara als corrents de fuita (`#eq-potencia-estatica`), no als «corrents paràsits» de `#eq-potencia`, i hi diu «augmentar la productivitat» en lloc de «rendiment total (productivitat)», coherent amb la definició de la #9. `A7.qmd:58` i `E6.qmd:159` no canvien de destí. Tres marcadors esborrats. ✅ **Ampliació decidida i executada** (usuari, 2026-10-02, fase 6): les conseqüències de la miniaturització ja les cobrien §Miniaturització i límit tèrmic i `#wrn-dennard`; s'hi afegeix l'aprofundiment `#wrn-reduccio-consum` (DVFS, inhibició del rellotge i desconnexió de l'alimentació, cadascuna lligada al terme de l'equació on actua, i l'estalvi d'energia del DVFS, que ve de la tensió i no de la freqüència). Termes catalans proposats per Claude Code i acceptats per l'usuari, amb l'anglès en cursiva a la primera aparició. |

  El pla del grup: (1) acabar la fusió de `temes456`; (2) #12, #9 i #3; (3) una sola passada de render per a #7, #8, #10 i #11; (4) #4 i #1–#2; (5) decisions #5, #6 i l'ampliació de #12; (6) en resoldre cada anotació, esborrar-ne el marcador i actualitzar-ne l'entrada; les de la branca es registren aquí en fusionar-la. És la base de `CLAUDE.md §Pla de treball` des del 2026-10-01. Les #1–#2, #5 i #6 coincideixen amb entrades que ja hi eren (figures de *half-adder* i *full-adder*, R4-TYPE, R5-TYPE), i hi consta la valoració del grup.

  📌 **Marcadors de la branca, a `main` des de la fusió** (`451c3ef`, 2026-10-01; línies mesurades a `454a82e`). Els 10 [br] d'aquesta taula, amb el text literal de cada un abreujat:

  | # | Marcador | Text |
  | ---: | :--- | :--- |
  | 3 | ~~`A4.qmd:110`~~ | «Aquest "caution" hauria d'estar més endavant, quan es parla de l'extensió M…» — esborrat, resolta |
  | 4 | ~~`A4.qmd:181`~~ | «La descripció de l'algorisme no hauria de ser tota en cursives. Els titols del codis no haurien de ser simplemement "pseudocodi".» — esborrat, resolta |
  | 7 | ~~`A5.qmd:269`~~ | «PM: la paraula denormals de la figura a baix no s'aprecia del tot bé» — esborrat, resolta |
  | 8 | ~~`A5.qmd:531`~~ | «PM: Check that this formula is well displayed under LaTeX» — esborrat, verificada |
  | 9 | ~~`A6.qmd:13`~~ | «PM: els exemples són confusos perquè es barreja "temps d'execució" amb "rendiment"…» — esborrat, resolta |
  | 10 | ~~`A6.qmd:148`~~ | «PM: la legenda de la figura (temps t_c) no s'ha compilat correctament» — esborrat, resolta |
  | 11 | ~~`A6.qmd:178`~~ | «PM: equació más llarga (cal separar-la en més d'una línia)» — esborrat, resolta |
  | 12 | ~~`A6.qmd:260`~~ | «PM: l'aprofundiment no hauria de començar abans de la eq. 6.8» — esborrat, resolta |
  | 12 | ~~`A6.qmd:272`~~ | «PM: aquí s'introdueix la potència després de tota la parrafada anterior…» — esborrat, resolta |
  | 12 | ~~`A6.qmd:373`~~ | «Aquí és el lloc idoniï per deixar els aprofundiments» — esborrat, resolta |

  ```bash
  git grep -c '<!-- TODO' -- 01_apunts/A4.qmd 01_apunts/A5.qmd 01_apunts/A6.qmd   # a 454a82e: A4 4 · A5 4 · A6 6 = 14 (4 [main] + 10 [br])
  git grep -o -I -F -e '<!-- TODO' -- 01_apunts/A4.qmd 01_apunts/A5.qmd 01_apunts/A6.qmd ':!TODO.md' ':!13_contrib.qmd' | wc -l   # després de la fase 3 (2026-10-01): A4 3 · A5 4 · A6 2 = 9 (4 [main] + 5 [br])
  # després de la fase 4 (2026-10-02; la fase 6 n'havia esborrat els dos [main] d'A5): A4 2 · A5 0 · A6 0 = 2 (2 [main], les figures #1 i #2 de la fase 5; cap [br])
  # després de la fase 5 (2026-10-03): A4 0 · A5 0 · A6 0 = 0 (cap marcador de l'inventari al corpus)
  ```

  ⚠️ «eq. 6.8» (`A6.qmd:260`) és un número d'equació escrit a mà: es refereix a la numeració del render que va veure el revisor, i caduca amb qualsevol equació nova anterior. En resoldre l'anotació #12, cal localitzar l'equació pel contingut, no pel número. *(Fet, 2026-10-01: és `#eq-potencia`, la vuitena equació etiquetada d'A6, comptada sobre `6915e05`.)*

  📌 **Freqüència de sostre: A6 i A7 no diuen el mateix** (detectat a la fase 3, 2026-10-01, en revisar la remissió entrant de `#wrn-dennard`). `#wrn-dennard` diu que la freqüència «va tocar sostre als 3–4 GHz» i que un portàtil i un servidor tenen «freqüències de rellotge similars (3–4 GHz)»; `A7.qmd:58` (`#sec-fi-escalat-dennard`) diu que «s'ha estancat entre els 3 i els 5 GHz, amb pics puntuals de fins a 6 GHz en mode *turbo*». No es contradiuen del tot, però el lector veu dues xifres per al mateix fet. Cal triar-ne una i escriure-la als dos llocs; A7 no era de l'abast de la fase 3, i per això només es registra.

  📌 **Tres coses de la fusió que no són anotacions del grup, però que el grup ha de conèixer** (detectades en revisar-la, 2026-10-01):

  - **El canvi a `22_figs_originals/T5_ieee754_format_registre.svg` (la «S» sense girar, `9bc5f46`) no arriba al llibre.** `A5.qmd:87-94` consumeix `auto_figs/T5_ieee754_format_registre__registre_*.svg`, que genera `25_scripts/gen_regs.py` des de `24_specs/registres.toml`; i `gen_regs.py:270` gira sempre els camps d'1 bit (`use_vertical = (nbits == 1) or …`). Perquè la «S» surti horitzontal cal una opció per camp a `gen_regs.py` i al `.toml`. El canvi del `.toml` de la mateixa branca («Reserved» → «Reservat» a `T5_fcsr`), en canvi, sí que s'hi veu: verificat a `auto_figs/T5_fcsr__registre_light.svg` després del render.
  - **Contingut que la revisió treu**, sense errada però perquè el grup ho confirmi: A5 treu «A **EC** s'estudia el format de **simple precisió** (32 bits), que correspon al tipus `float` de C» (la correspondència amb `float` es manté a la taula d'`A5.qmd:64`, «Tipus C», i la restricció a la precisió simple a `#imp-ec-simple-precisio`: la frase era redundant) i l'enunciat «Expressa els nombres següents en notació científica normalitzada:» d'un exemple, que queda amb la taula sola; A6 treu la pregunta «Quin té més productivitat?» de dos exemples, però en manté la resposta («B té major productivitat»).
  - **Notació de CPI**: A6 passa de `$CPI$` a `$\text{CPI}$`. El corpus ja barrejava les dues formes; es resol a l'entrada «Revisió sistemàtica del corpus per nodrir les taules de `Símbols` i `Notació`» (§Tasques transversals). ✅ **Resolta (2026-10-03, fase 7, `a5340f3`)**: cap CPI dins de fórmules sense `\text{}`; l'entrada és ara a §Entrades retirades → Executades.

---

## Tasques transversals

- **Revisió general de les figures i generació per script** (registrada 2026-10-03, fase 5; proposta de l'usuari, ampliada amb la valoració de Claude Code el mateix dia). Les figures són avui la part més heterogènia del corpus, i n'hi ha que encara s'han de fer (§T7, §T8 — Figures pendents de creació, §T9, les taules de memòria de T2 de §Decisions obertes). Cal revisar-les totes, amb la integració, i decidir com es generen d'ara endavant. Sessió pròpia, **Opus, effort High**: és classificació amb criteri i decisions de model, no execució.

  **Símptomes mesurats** (2026-10-03, sobre `8e4702f`; mesura preliminar per dimensionar la feina, que el pas 1 ha de refer i completar):

  ```bash
  git ls-files 22_figs_originals | wc -l          # 69 (67 SVG, 2 PNG)
  git ls-files 23_figs_externes | wc -l           # 23 (19 SVG, 4 PNG/JPG)
  comm -12 <(git ls-files 22_figs_originals | xargs -n1 basename | sort) \
           <(git ls-files 23_figs_externes  | xargs -n1 basename | sort) | wc -l   # 10, totes de T7
  for f in $(git ls-files 22_figs_originals 23_figs_externes | grep '\.svg$'); do
    git grep -q -F "$(basename $f .svg)" -- '*.qmd' 24_specs/retalls.toml || echo "$f"; done | wc -l   # 15 sense cap .qmd que les citi
  for f in $(git ls-files 22_figs_originals | grep '\.svg$'); do grep -q '<desc' $f || echo $f; done | wc -l   # 28 de 67 sense <desc>
  ```

  - **Deu figures de T7 són alhora a `22_figs_originals/` i a `23_figs_externes/`** amb el mateix nom (`T7_escriptura_*`, `T7_lru_exemple`, `T7_cd_diagrama`…): cal saber quina es consumeix i retirar l'altra.
  - **Sufixos de nom que fan de marcador d'estat**: `____error____`, `____no_inclosa_pero_interessant____`, `__net__`, `__org`, `__drawio`, `___drawio`, i un `T7_escriptura_dirty_bit__.svg` al costat de `T7_escriptura_dirty_bit.svg`. Un estat no ha de viure al nom del fitxer: o va al `TODO.md` o la figura es retira.
  - **Orígens barrejats**: SVG natius fets a mà, generats per script (`gen_regs.py`, `gen_T4_sumador.py`), Graphviz, drawio, extrets de PDF amb text traçat, i PNG/JPG.
  - **Colors fora de paleta**: el bloc «Colors llegat» de `24_specs/svg.md §13` (T1, T3, T6, T7) i les entrades drawio de T7.
  - **Accessibilitat**: el `<title>`/`<desc>` de l'SVG no arriba al lector de pantalla quan la figura s'insereix com a `<img>`; el que compta és el text alternatiu de la imatge (`fig-alt` a Quarto), que avui no es fa servir. Cal decidir la font de veritat de la descripció i, si és l'SVG, com es copia a `fig-alt`.

  **Pla proposat:**

  1. **Inventari** (una taula, al `TODO.md` o a `24_specs/`): per a cada figura, fitxer font, origen (natiu, script, Graphviz, drawio, extret, ràster), qui la consumeix (`#fig-` i fitxer), si té remissió `@fig-` des del text, peu, `<title>`/`<desc>`, colors fora de paleta, fonts, i variant fosca verificada. D'aquí surten les orfes, els duplicats i les que s'han de refer.
  2. **Integració**: tota figura amb `{#fig-}` té peu acabat en punt i almenys una remissió des del text; plantilla de `13_contrib.qmd §Integració al .qmd`; mides coherents dins de cada tema.
  3. **Model de generació** (decisió de l'usuari). Dues opcions, compatibles:
     - **(a) L'SVG versionat és el font i l'script només el regenera** (el que fa `gen_T4_sumador.py`). Adequat per a figures soltes.
     - **(b) La definició és el font i l'SVG es genera al pre-render** (el que fa `gen_regs.py` amb `registres.toml`). Adequat per a famílies: una sola convenció, i retocar és canviar un paràmetre.
     Proposta de Claude Code: (b) per a les famílies grans, (a) per a la resta. Arguments de la fase 5: la convenció viu en un sol lloc i no es pot aplicar de manera desigual; els defectes que la fase 4 va trobar d'un en un (`textLength`, gris de traç, subíndexs en `<text>` separats) desapareixen per construcció; i les funcions de portes de `gen_T4_sumador.py` (`and_gate`, `or_gate`, `xor_gate`, `sig`…) es poden convertir en una biblioteca compartida.
  4. **Pilot: T7 (memòria cau)**. És la família més gran i més regular: MC, MP i descomposició de l'adreça són la mateixa estructura amb paràmetres diferents (correspondència directa, associativa, per conjunts; cada pas d'un exemple d'escriptura o de reemplaçament). Un generador amb un fitxer de definició (com `registres.toml`) en faria les variants sense dibuixar-les una per una, i resoldria alhora els duplicats i els drawio de T7. Les portes lògiques (T4, T6) són la segona família.
  5. **Figures dinàmiques** (exploració): a T7 tenen molt valor pedagògic (accés rere accés, amb encert o fallada, i l'estat de la MC). Només poden existir a l'HTML. Regla proposada: **tota figura dinàmica té una seqüència estàtica equivalent per al PDF, generada pel mateix script i a partir de la mateixa definició**; si no, els dos formats divergeixen. Cal decidir la tecnologia (SVG amb JavaScript propi dins d'un bloc `.content-visible when-format="html"`, Observable JS, que Quarto ja suporta, o un altre) i comprovar que conviu amb el canvi clar/fosc.

  Precedents a la mà: `25_scripts/gen_T4_sumador.py` i `24_specs/svg.md §16` (fase 5), `25_scripts/gen_regs.py` i `24_specs/registres.toml`, `25_scripts/gen_crops.py` (entrada «Nova eina disponible: retalls», més avall, que té el mateix objectiu de font única per a T5).

  📌 **Fase 7c (2026-10-03): pas 1 fet, i decisions de l'usuari per als passos 2–5.** L'inventari és `24_specs/figures.md`, generat per `25_scripts/inventari_figures.py` (`make inventari`), que mesura pel contingut: l'origen (marques de l'editor i taules de `svg.md §15` i `§16`), qui consumeix cada fitxer, els duplicats per hash, el placeholder, `<title>` i `<desc>`, els colors fora de paleta, `textLength`, el text en gris de traç, els peus i les remissions. Sobre `722c522`: 78 `#fig-` (75 amb imatge i 3 taules d'A2) i 9 imatges sense etiqueta; 92 fitxers a `22_figs_originals/` i `23_figs_externes/`, dels quals 59 consumits i 33 orfes; i 18 figures de `gen_regs.py`. La variant fosca es va verificar a ull sobre el render de `rsvg-convert` (el del PDF) de totes les variants: totes bé, tret de `fig-assoc-conjunts-diagrama`, que és un ràster incrustat i surt blanc també en fosc. La mesura preliminar de més amunt dona 15 SVG «sense cap .qmd que les citi», i són 29 (33 fitxers amb els quatre ràsters): cercava el nom base, i el nom base d'una exportació orfe de `23_figs_externes/` és el mateix que el de la nativa consumida (l'ordre encara dona 15 a `722c522`).

  ```bash
  make inventari   # 78 etiquetes, 92 fitxers (33 orfes), sobre 722c522
  ```

  Mesurat pel contingut i no pel nom (regla 2), l'inventari troba:

  - `fig-assoc-conjunts-diagrama` és la figura del Patterson & Hennessy, en ràster i en anglès, amb la signatura de l'autor retallada al peu: és un problema de llicència, no només d'estil.
  - `22_figs_originals/T7_cd_diagrama.svg` no és natiu: és, byte a byte, l'exportació de LO Draw de `23_figs_externes/`.
  - Noms que no diuen el contingut: `23_figs_externes/T7_mc_exemple_descomposicio_32bits.svg` és una taula de MC (la de `fig-mc-organitzacio`, en LO Draw); `23_figs_externes/T7_multinivell_diagrama.svg` és una jerarquia amb capacitats, no el diagrama (a)–(c) que especifica A7; i els dos `____error____` són retalls equivocats (una pàgina de text i una taula de definicions).
  - `22_figs_originals/T7_mc_descomposicio_bits.svg`, orfe, il·lustra exactament `#tip-mc-numbloc` (§T7, fila `fig-mc-exemple-descomposicio-32bits`).
  - `22_figs_originals/T5_ieee754_format_registre.svg`, orfe: la figura surt de `registres.toml`, i el canvi del revisor «S sense girar» (`9bc5f46`) només és en aquest fitxer (§Decisions obertes → Anotacions de la revisió externa de T4–T6).
  - `T7_lru_exemple.svg` porta el `<title>` i el `<desc>` d'`estat_inicial`; els placeholders, els de «Raspberry Pi Pico 2…»; i 20 títols diuen «(mode clar)», també a la variant fosca.
  - Al render de `rsvg-convert`: el requadre «Exponent en IEEE 754» de `T5_exponent` surt tallat per la dreta; a `T9_cicle_interrupcio`, la línia discontínua trepitja «(detecció)» i la fletxa vermella trepitja «Execució normal»; a `T3_deps_*`, les fletxes travessen el codi; i a `T4_multiplicador_arbre`, «Z · producte (2n bits)» toca les vores de la caixa, i hi ha «desplacats» i «nomes».
  - Les figures de T7 porten «Load/Store», «Hit/Miss» i «Cold/Capacity/Conflict Miss» (també dos peus), contra `13_contrib.qmd §Substitucions obligatòries`.
  - `24_specs/svg.md §9` escriu les adreces amb espais («0x1001 0000»), contra `13_contrib.qmd §T2 i T3` («sense espais»).
  - L'especificació de `fig-texe-diagrama` (comentari d'A7) diu `addu`, que és de MIPS.

  **Decisions de l'usuari (2026-10-03, a proposta de Claude Code):**

  1. Model de generació: (b) per a les famílies i (a) per a les figures soltes, amb una comprovació que l'SVG versionat coincideix amb el que genera l'script.
  2. Pilot de T7: la família «estat de la MC» (taules i seqüències d'accessos, que el generador simula), la descomposició de l'adreça, els diagrames de blocs de la lectura (correspondència directa, associativa per conjunts i completament associativa, amb les portes de `svg.md §16` en una biblioteca compartida) i les figures soltes (`texe`, multinivell i multicore). Hi entren les set de §T7.
  3. Les set figures de §T7, que aquest fitxer assignava a LO Draw (Roger), i els retocs de T3 (§T3) els fa Claude Code, en SVG natiu.
  4. Figures dinàmiques: fotogrames i un navegador de passos amb JS propi sobre els `<img>` clar i fosc de sempre; el PDF porta la seqüència estàtica, generada pel mateix script. Prototip: `#fig-lru-exemple`. L'usuari tem que les seqüències del PDF surtin massa llargues: cal estudiar-ho sobre el resultat.
  5. Es retiren els orfes i els duplicats (llista a l'inventari), i `gen_regs.py` rep una opció d'orientació per camp, per a la «S» de T5.
  6. Text alternatiu: el `<desc>` de l'SVG n'és la font de veritat, i un filtre Lua el copia a l'`alt` en renderitzar; si no és viable, `fig-alt` al `.qmd`. El peu (*caption*) es queda al `.qmd` i no es desa a l'SVG: les escombrades, `lint_prosa.py` i `revisor-linguistic` llegeixen els `.qmd`, el peu és Markdown, una mateixa imatge pot anar amb peus diferents (les de registres, amb peu a T2 o T9 i sense al compendi), i l'`alt` no ha de repetir el peu. L'inventari avisa quan un `<desc>` falta o és idèntic al peu.
  7. Etiquetes dins dels `#nte-`: es treuen les 17 (§Decisions obertes).
  8. Remissió obligatòria per a les figures del cos del text, que al PDF poden flotar (24 sense cap `@`), però no per a les dels callouts. Cal canviar `13_contrib.qmd §Referències creuades`, que avui diu que no cal.
  9. Text de figura en gris de text (`#6c757d`), també els rètols de nivell de T4 (§Tasques globals → SVG).
  10. Adreces sense espais també a les figures (`svg.md §9`).
  11. Terminologia catalana a les figures de T7: «Lectura», «Escriptura», «Encert», «Fallada» i fallades «obligatòries», «de capacitat» i «de conflicte».
  12. L'inventari, a `24_specs/figures.md`, generat.
  13. La migració del canvas dels BA queda per a una família de memòria futura (§Tasques globals → SVG); les taules de memòria de T2 entren ara, amb un generador mínim de «memòria per bytes».

  ✅ **Decisió 5, primera part: 29 fitxers retirats** (2026-10-03). Cap no el consumia cap `.qmd`, i cadascun es recupera amb `git show 1f5f006:<ruta>`. De T7: les deu exportacions de LO Draw de `23_figs_externes/` que tenen la nativa consumida a `22_figs_originals/` (`assoc_conjunts_taula`, `capacitat_exemple`, `conflicte_exemple`, `escriptura_dirty_bit`, `escriptura_estat_inicial`, `escriptura_immediata_amb_assignacio`, `escriptura_immediata_assignacio`, que n'era un duplicat byte a byte, `escriptura_immediata_sense_assignacio`, `escriptura_retardada` i `lru_exemple`); la còpia de `T7_cd_diagrama.svg` de `22_figs_originals/`; els dos `____error____` i `____no_inclosa_pero_interessant____` (el percentatge de fallades segons l'associativitat i la mida, la figura 6.27 del PDF original); el drawio de LRU (§T7, `fig-lru-roger`); `T7_capacitat_exemple.svg` (la combinada), `T7_escriptura_dirty_bit__.svg` (una taula buida) i `T7_tecnologies_memoria.svg` (duplicava la taula Markdown d'`A7.qmd` §Tecnologies de memòria); les dues de nom equivocat (`T7_mc_exemple_descomposicio_32bits` i `T7_multinivell_diagrama`); i els dos PNG del Patterson & Hennessy. De T5, els quatre esborranys (§T5); de T6, `T6_amdahl_mod.svg`; i els PNG de T3 (`T3_func_multinivell_pila.png`) i de T4 (§Tasques globals → SVG). En queden quatre d'orfes, a propòsit: `TODO.svg`, fins que cap figura no faci servir el placeholder; `T5_ieee754_format_registre.svg`, fins que `gen_regs.py` porti la «S» horitzontal; `T7_mc_descomposicio_bits.svg`, que s'integrarà a `#tip-mc-numbloc`; i `23_figs_externes/T7_multinivell_multicore.svg`, que és la referència per refer-la en natiu.

  ```bash
  make inventari   # 63 fitxers (4 orfes), després de la retirada
  ```

- **Confirmar al Termcat «semisumador» (*half-adder*) i «sumador complet» (*full-adder*)** (registrada 2026-10-03, fase 5). Són els termes que fan servir A4 (`#wrn-sobreeiximent-maquinari`) i les figures del sumador, i ja són a la taula de `13_contrib.qmd §Substitucions obligatòries`, marcats «pendent de confirmar». L'usuari no els ha pogut trobar a la interfície nova del Termcat; només hi consta *adder* → «sumador». Si el Termcat en dona uns altres, cal canviar la taula, el text d'A4 i els rètols dels SVG (`git grep -n -i 'semisumador\|sumador complet'`).

- **`S_criteris_seleccio.qmd` — taula de T1 incompleta** (auditoria, sessió 2, 2026-09-21). La taula de `## {{< var tema1 >}}` té **una sola fila** (`@exr-t1-enters-taules`, `:23`) i ha de recollir la resta de problemes seleccionats de `S1.qmd`. El marcador «TODO» que ho registrava era contingut destinat a l'alumne i es va substituir per la nota neutra de `:19` («*Taula provisional: recull els problemes de `S1.qmd` seleccionats fins ara.*»); **aquesta entrada és ara l'únic registre de la tasca**. El fitxer és comentat a `_quarto.yml:95`, de manera que avui no es renderitza.

- **Discrepància de noms a la figura Graphviz de T7** (detectada 2026-09-20): el fitxer font és `24_specs/T7_mc_politiques__graphviz.gv` i el SVG derivat és `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` — arrels diferents, el `_resum` només és al SVG. Documentat com a discrepància coneguda a `13_contrib.qmd §Figures Graphviz` perquè ningú no «l'arregli» pel cantó dolent. **Via de resolució**: renombrar el `.gv` a `T7_mc_politiques_resum__graphviz.gv` és **inofensiu** (cap script ni cap `.qmd` no el referencia: el `dot` s'executa a mà i el pre-render parteix del SVG ja generat). Renombrar el SVG, en canvi, **trencaria** les tres línies d'`A7.qmd` (646, 649, 653, mesurat a `ebdf055`) que consumeixen `auto_figs/T7_mc_politiques_resum__graphviz__original_{light,dark}.svg`.

- **Revisar la distribució de les columnes de totes les taules** (petició de l'usuari, 2026-10-03, fase 7b). A la fase 7b, dues taules d'A2 sortien malament al PDF, i cap de les dues coses no es veia a l'HTML: la de `#tip-codificacio-instruccions` desbordava el callout, perquè la darrera columna tenia el 12% i en necessitava el 20%, i la de `la`, amb les tres columnes iguals, partia en dues línies cada instrucció de l'expansió. A `a7876b9` hi ha 300 taules *pipe* (línies separadores) i 102 `tbl-colwidths` (també als `div` que embolcallen una taula), de manera que almenys 198 taules no declaren amplades i deixen que Pandoc les reparteixi. Cal revisar-les totes al PDF de `make render-complet`: (1) que cap cel·la no surti del text del callout ni de la pàgina (`pdftotext -bbox`; la prosa acaba a x ≈ 538,6 pt i el text dels callouts, a x ≈ 524 pt); (2) que cap cel·la curta no es parteixi (`pdftotext -layout`); i (3) que cada `tbl-colwidths` sumi 100 (`13_contrib.qmd §Taules`). Per dimensionar-les: en una taula de nou columnes dins d'un callout, 1% de `tbl-colwidths` són uns 3,6 pt de text (mesurat a `#tip-codificacio-instruccions`). Primera mesura, només contra el marge de la pàgina: al PDF de `a7876b9`, l'única paraula que passa de x = 545 pt no és de cap taula, sinó codi en línia de la prosa d'A2, `char[<quantitat_caracters>]` (§Cadenes de caràcters, pàgina 94 del fitxer, x = 573,5 pt), que no es pot partir. Les altres quatre per sobre de 541 pt són números de pàgina de l'índex (tres) i una cometa.

  ```bash
  git grep -o -I -E -i -e '^ *\| *:?-{3,}:? *\|' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' | wc -l   # 300 a a7876b9
  git grep -o -I -F -i -e tbl-colwidths -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' | wc -l           # 102 a a7876b9
  pdftotext -bbox _book/Estructura-de-computadors.pdf - | awk '/<page /{p++} /<word /{match($0,/xMax="[0-9.]+"/); x=substr($0,RSTART+6,RLENGTH-7)+0; if (x>545) print p, x}'   # 94 573.535
  ```

- **Nova eina disponible: retalls (crops) SVG a partir d'una figura font única** (afegida 2026-07-13, revisió interna T5): `25_scripts/gen_crops.py` + `24_specs/retalls.toml`, integrat al `pre-render` de `_quarto.yml` entre `gen_regs.py` i `gen_dark.py`. Permet definir una figura «detall»/«zoom» com una finestra `(x, y, w, h)` sobre el `viewBox` d'una figura font ja existent, sense duplicar-ne el contingut. Documentat a `13_contrib.qmd §Retalls`. Aplicable només quan el detall és un subconjunt geomètric net de la font (cap connector/etiqueta tallat a mig camí).

  **Cap ús real encara**: `24_specs/retalls.toml` té 23 línies, **totes comentari**, i cap retall definit. S'ha valorat dues vegades per a les figures de T5 i descartat totes dues: (1) `T5_recta_zoom_zero` com a retall de `T5_recta_global` — `T5_recta_zoom_zero` mostra informació pròpia dels denormals (hexadecimals concrets) que la global no té espai per representar; (2) totes dues com a retalls de `T5_coma_flotant_racionals__drawio.svg` (figura orfe a `22_figs_originals/`, no referenciada per cap `.qmd`, que sembla l'esborrany original; retirada a la fase 7c, el 2026-10-03, i es recupera amb `git show 1f5f006:<ruta>`, l'últim commit on hi era) — el drawio (7465 línies, estil amb fletxes i icones pròpies) no comparteix coordenades ni disseny amb les figures actuals en estil pla.

  **TODO futur**: investigar `gen_crops.py` sobre una figura global com la primigènia, és a dir, com a **font única des de zero** en lloc d'intentar-ho a posteriori sobre figures ja redibuixades per separat. Requeriria: (i) redibuixar aquesta figura en estil pla natiu (coherent amb `svg.md`, no drawio) com a única font de veritat amb tot el contingut (rang global + zoom de zero + denormals); (ii) definir a `retalls.toml` les finestres de cada vista actual; (iii) verificar que cada retall és net. Si viable, eliminaria la duplicació de manteniment entre les dues figures actuals. Fora de l'abast d'una revisió textual.

---

## Tasques per tema

### T2

Cap entrada viva des del 2026-10-03 (les dues últimes, la verificació de la taula d'alineació i la taula de `#tip-codificacio-instruccions`, són a §Entrades retirades → Executades, fase 7b).

### T3

- **Decisió de contingut a `#cau-boolea-c`** (`A3.qmd:249`, mesurat a `ab48732`, pendent d'Adrià, obert des de la revisió de T3): el text diu que «unes expressions no nul·les s'interpreten com a certes» sense dir **quines**. Cal indicar com s'identifiquen les que sí i les que no. Afecta el rigor tècnic. El marcador segueix al corpus perquè la decisió és viva i no la pot prendre Claude Code.

- **`auipc` no és al compendi ni té taula ISA** (detectat el 2026-10-03, fase 7b). `auipc` és una instrucció de RV32I base, de format U com `lui`, i només la presenta `#nte-la-auipc` (A3), un callout de RARS sobre l'expansió de `la`; A2 la nomena, sense descriure-la, a la llista de categories d'instruccions (§Càrrega d'immediats). No té fragment a `21_riscv/` ni taula a `11_riscv.qmd`, i des de la fase 7b el compendi la cita a l'expansió de `la` (`#nte-rv-pseudo-la`). Cal un fragment (p. ex. al costat de `RV32I_instruccions_lui.qmd`), afegir-lo al compendi i decidir on es presenta a la teoria: amb `lui` i el format U a T2 (`#nte-format-u`) o amb `la` a T3. A3 és en revisió externa.

  ```bash
  git grep -n -w auipc -- 21_riscv/ 11_riscv.qmd   # només 21_riscv/RV32I_pseudo_la.qmd, l'expansió de la (a a7876b9)
  ```

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

  ✅ **Desbloquejat el 2026-10-01**: `temes456` es va fusionar a `main` (`451c3ef`), i A4, A5 i A6 ja es poden tocar (vegeu §Decisions obertes → Branques del remot).

### T5

- **Tres SVG orfes de T5** (registrats 2026-10-01, a petició de l'usuari, que segurament els eliminarà). Versionats a `22_figs_originals/` i sense cap referència en cap `.qmd`, `.yml` ni `.toml`:

  ```bash
  for f in T5_recta_global__org T5_recta_zoom_zero__org T5_coma_flotant_racionals__drawio; do
    echo "$f: $(git grep -l "$f" -- . ':!TODO.md' | wc -l) referències"; done   # 0 · 0 · 0
  ```

  - `T5_recta_global__org.svg` (32 línies) i `T5_recta_zoom_zero__org.svg` (34): esborranys de les rectes de T5, actualitzats igualment a «precisió simple» el 2026-10-01 (`2693ec3`, decisió de l'usuari).
  - `T5_coma_flotant_racionals__drawio.svg` (7 465 línies): l'esborrany original de totes dues rectes, en estil drawio. L'entrada «Nova eina disponible: retalls (crops)…» de §Tasques transversals el va valorar i descartar com a font de retalls.

  ⚠️ Si s'eliminen, cal actualitzar aquella entrada de retalls, que en parla.

  ✅ **Retirats a la fase 7c (2026-10-03, decisió de l'usuari 5)**, tots tres i un quart que l'inventari va trobar orfe i que aquesta entrada no comptava: `22_figs_originals/T5_coma_flotant_exponent__drawio.svg` (l'esborrany de `T5_exponent.svg`). L'entrada de retalls ja ho diu. Cada fitxer es recupera amb `git show 1f5f006:<ruta>`, l'últim commit on hi era. Es retira en tancar la fase.

- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present. *(No retirar sense actualitzar `13_contrib.qmd:729` —mesurat a `ebdf055`—, que hi remet explícitament: «T5 → T9: `fcsr` → `@nte-zicsr` (vegeu `TODO.md §T5 P8`)».)*

### T6

Cap entrada viva des del 2026-10-03 (l'última, les etiquetes de classe d'instruccions, és a §Entrades retirades → Executades).

### T7

- **Figures pendents de reconstrucció com a natives** (requereixen LO Draw de Roger). ⚠️ **Decisió de l'usuari (2026-10-03, fase 7c): les fa Claude Code, en SVG natiu**, dins del pilot de T7 (§Tasques transversals → «Revisió general de les figures i generació per script»).

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

  ⚠️ **Tres files corregides pel contingut (2026-10-03, fase 7c; `24_specs/figures.md`).** `fig-assoc-conjunts-diagrama` no és cap exportació pròpia: és la figura del Patterson & Hennessy, en ràster incrustat a l'SVG, en anglès i amb la signatura de l'autor retallada al peu; i en fosc surt blanca. `fig-mc-exemple-descomposicio-32bits` ja existeix en natiu, orfe: `22_figs_originals/T7_mc_descomposicio_bits.svg` descompon l'adreça `0x100100F8` en número de bloc i desplaçament, que és l'exemple de `#tip-mc-numbloc`; el fitxer de `23_figs_externes/` amb aquest nom és en realitat una taula de MC (la de `fig-mc-organitzacio`, en LO Draw). I `23_figs_externes/T7_multinivell_diagrama.svg` no és el diagrama (a)–(c) de l'especificació (`A7.qmd`, comentari `fig-multinivell-diagrama`), sinó una jerarquia CPU–MC–MP–disc amb capacitats; la de `T7_multinivell_multicore.svg` sí que correspon a la seva especificació. Totes dues especificacions són al corpus com a comentari, no com a `div`: d'aquí el «Cap ancoratge».

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

  ✅ **Decidida a la fase 7c (2026-10-03, decisió de l'usuari 5): no cal figura independent.** `#fig-lru-exemple` ja mostra l'LRU de 2 vies, que és el que el text desenvolupa (per a 4 vies o més, A7 diu que s'usen aproximacions). L'esborrany era `23_figs_externes/T7_lru_roger___drawio.svg`, una pila LRU de tres posicions amb les transicions d'encert i de fallada, orfe i en draw.io; s'ha retirat, i es recupera amb `git show 1f5f006:<ruta>`, l'últim commit on hi era. Es retira en tancar la fase; les dues cites de `13_contrib.qmd` es queden, perquè són lliçons.

- **`fig-capacitat-exemple` a HTML**: dues figures separades (primera + segona passada) o figura única combinada? Existeixen totes tres variants a `auto_figs/` (`T7_capacitat_exemple__original_*`, `T7_capacitat_exemple_bucle_primera_passada__original_*`, `..._segona_passada__original_*`). Pendent de decisió.

  ✅ **Decidida a la fase 7c (2026-10-03, decisió de l'usuari 4).** A l'HTML, una sola figura dinàmica, amb un navegador de passos; al PDF, la seqüència estàtica, que avui són les dues figures. Totes dues sortiran del generador de la família «estat de la MC». La figura combinada (`22_figs_originals/T7_capacitat_exemple.svg`) era orfe i s'ha retirat, igual que la seva exportació de LO Draw; es recupera amb `git show 1f5f006:<ruta>`, l'últim commit on hi era. L'usuari tem que les seqüències del PDF surtin massa llargues: es mirarà sobre el resultat.

- **Dos SVG orfes amb `____error____` al nom.** Versionats i no referenciats per cap `.qmd`:

  ```bash
  git ls-files | grep -i "error____"
  # 23_figs_externes/T7_texe_diagrama____error____.svg
  # 23_figs_externes/T7_tres_c_barres_light____error____.svg
  git grep -n "error____" -- '*.qmd' ':!TODO.md'   # cap referència
  ```

  ❓ **Pregunta oberta**: l'`__error__` al nom marca una figura **a refer**, o són **descartables**? No s'ha decidit ni tocat res. ✅ **Descartables, i retirats (fase 7c, 2026-10-03, decisió de l'usuari 5)**: mirats pel contingut, no són figures sinó retalls equivocats del PDF original, una pàgina de text («8. Tipologia de les fallades de cache») i una taula de definicions ($n_{ins}$, $n_{cicles}$…). La figura de `fig-texe-diagrama` es farà des de l'especificació d'A7. Cada fitxer es recupera amb `git show 1f5f006:<ruta>`, l'últim commit on hi era. *(Els altres quatre fitxers amb el mateix patró són a `auto_figs/`, que és a `.gitignore:5`: són derivats regenerables, no entren aquí.)*

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

- **F/G — Figures SVG**: diferides a una fase posterior. Estat actual: A9 consumeix 24 vegades `auto_figs/`, totes de la mateixa figura (`T9_cicle_interrupcio`). ✅ **Executada, i la xifra era equivocada** (comprovat el 2026-10-03, fase 7c). F/G era «Registres → diagrames de camps» (`git show aab3b22^:T9_tasques.md`, §7), i les set figures de registres de T9 ja les genera `gen_regs.py` des de `registres.toml` (`T9_mcause`, `T9_mepc`, `T9_mstatus`, `T9_mtvec`, `T9_mip`, `T9_mie`, `T9_satp`). Les 24 rutes `auto_figs/` d'A9 no són d'una sola figura: són 8 figures per 3 rutes cadascuna (clara, fosca i PDF), la del cicle d'interrupció i les set de registres (`24_specs/figures.md`). Es retira en tancar la fase 7c.

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

- **`22_figs_originals/T4_multiplicador_sequencial.png` (63 KB)**: decidir si s'elimina. Verificat (auditoria, sessió 2): **no el referencia ningú** — `A4.qmd:175,178,182` usen només el `.svg` via `auto_figs/`. És **l'única parella `.png`+`.svg` del directori**, de manera que eliminar-lo també elimina l'excepció al criteri d'un sol format font. No s'ha tocat: és un fitxer binari i la supressió no entrava a l'abast autoritzat. ✅ **Retirat a la fase 7c (2026-10-03, decisió de l'usuari 5)**; es recupera amb `git show 1f5f006:<ruta>`, l'últim commit on hi era. Es retira en tancar la fase.

  ✅ **Desbloquejat el 2026-10-01**: `temes456` es va fusionar a `main` (`451c3ef`), i A4, A5 i A6 ja es poden tocar (vegeu §Decisions obertes → Branques del remot).

  ```bash
  git grep -n "T4_multiplicador_sequencial" -- '*.qmd' ':!TODO.md'
  # A4.qmd:175,178,182 — totes tres al .svg
  ```

- **Text de figura en gris de traç (`#adb5bd`) en lloc del gris de text neutre (`#6c757d`)** (detectat 2026-10-02, en resoldre l'anotació #7 de T4–T6; mesurat a `62b4d27`). A la paleta de `24_specs/svg.md`, `#adb5bd` és el gris de traç neutre i `#6c757d` el de text neutre; al fosc, `gen_dark.py` els converteix en `#888888` i `#adb5bd`. El «denormals» de `#fig-recta-global` era en `#adb5bd`, i el revisor el va trobar poc llegible: l'anotació #7 es va resoldre passant-lo a `#6c757d` (`70865b6`). Queden 5 textos amb el mateix gris: «normalitzats», dues vegades, a `T5_recta_zoom_zero.svg` (`#fig-recta-zoom-zero`, A5), i «nivell 1», «nivell 2» i «nivell 3» a `T4_multiplicador_arbre.svg` (`#fig-multiplicador-arbre`, A4). Al zoom de T5 és el mateix cas que #7: l'etiqueta fa el paper de «denormals» a la figura germana. A T4 pot ser una tria de disseny (etiquetes de nivell atenuades al marge), i cal decidir-ho. Ordre que ho mesura (5 a `62b4d27`); mira el `fill` i l'`style` de cada `<text>` o `<tspan>`, no el color heretat d'un `<g>`:

  ```bash
  python3 -c "import subprocess,xml.etree.ElementTree as E;print(sum(1 for p in subprocess.run(['git','ls-files','22_figs_originals/*.svg','23_figs_externes/*.svg'],capture_output=True,text=True).stdout.split() for e in E.parse(p).iter() if e.tag.split('}')[-1] in('text','tspan') and '#adb5bd' in ((e.get('fill') or '')+(e.get('style') or '')).lower() and ''.join(e.itertext()).strip()))"
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

- **Identificador del commit a la data de publicació** (petició de l'usuari, 2026-10-02, per al futur): afegir el hash curt del commit renderitzat, entre parèntesis, després de la data de «Publicat» de l'HTML i a la portada del PDF, si no és massa complicat tècnicament. Avui la data surt de `book.date: last-modified` (`_quarto.yml`), i el render es fa des del `Makefile` (local) i des de `.github/workflows/publish.yml` (CI del mirall, que té el mateix hash que GitLab). Punts que cal resoldre en valorar-ho, no verificats encara: (i) si Quarto accepta un text lliure al camp `date` o si cal un camp a part (el `date` es formata com a data); (ii) d'on surt el hash —`-M` a `quarto render` des del `Makefile` i del CI, o una variable a `_variables.yml` escrita abans del render; el `pre-render` no serveix per al que Quarto llegeix en l'escaneig de configuració, que s'executa abans (vegeu-ne el cas a `25_scripts/gen_taules_auto.py`)—, i (iii) què s'hi escriu si l'arbre té canvis no confirmats (p. ex. `-dirty`).

- **Valorar si les taules de `21_riscv/` haurien de passar a `.json`** (petició de l'usuari, 2026-10-02, per al futur). Avui són 44 fragments `.qmd` (`git ls-files 21_riscv | grep -c "\.qmd$"`, a `4658e90`) amb files de taula *pipe*, inclosos amb `{{< include >}}` als callouts dels temes i a `11_riscv.qmd`; les taules que combinen fragments es fusionen amb `25_scripts/gen_taules_auto.py` i `24_specs/taules_fusio.toml`, que s'han d'executar a mà abans del render. Una font estructurada permetria generar les taules (i les fusions) per script i validar-ne el contingut; el cost és un generador nou i una dependència més del render. Cal valorar-ho abans de decidir res.

- **Font monoespaiada del PDF** (registrada 2026-10-03, fase 5; proposta de Claude Code, que l'usuari vol tenir en compte). Al PDF, els blocs de codi surten en Latin Modern Mono: el `.tex` generat carrega `lmodern` (`Estructura-de-computadors.tex`, amb `keep-tex: true`) i `_quarto.yml` no fixa cap `monofont`. Té poca cobertura Unicode, i ja n'hi ha un símptoma registrat: «—» surt com a `---` en un `filename` (`13_contrib.qmd §Blocs de codi`, títol dels blocs de pseudocodi). Hi ha blocs de codi amb `─` i `✓` (p. ex. `#tip-suma-ca2-mono` d'A1).
  1. **Primer pas: verificar quins glifs falten avui.** Fer `make render-complet` i buscar «Missing character» al registre de LaTeX; comparar visualment els blocs amb caràcters fora de l'ASCII (`git grep -n -P '[^\x00-\x7F]'` dins dels blocs de codi).
  2. **Proposta: `monofont: "DejaVu Sans Mono"`** a `format: pdf` (amb `monofontoptions: Scale=MatchLowercase` o similar), que té la cobertura més àmplia i ja és instal·lada al sistema i al CI (comprovar-ho al CI). Alternativa: Source Code Pro, que faria joc amb Source Sans de l'HTML (`styles.css`), però que s'hauria d'instal·lar.
  3. Toca tot el PDF: comprovar que cap bloc de codi no canvia d'amplada fins a sortir del marge (`pdftotext -bbox`), sobretot a les taules de `21_riscv/` i als bolcats del laboratori. Decisió de l'usuari.

  **No canvia**: la font monoespaiada dels SVG (Liberation Mono, `24_specs/svg.md §12`). Els SVG s'insereixen com a `<img>`, no poden carregar fonts web i es dibuixen amb la font que el lector tingui; Liberation Mono té les mateixes mides que Courier New (Windows, macOS), i per això les figures fan la mateixa amplada a tot arreu. Una altra font només val la pena incrustada a l'SVG. Tampoc l'HTML, que fa servir la pila monoespaiada de Bootstrap; com a molt, Source Code Pro via Google Fonts, si es vol harmonia amb Source Sans.

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
| **Homogeneïtzació del format de les adreces** (entrada de §Tasques transversals, usuari, 2026-09-23; retirada el 2026-10-01) | **Executada (2026-10-01).** Dels tres aspectes, dos ja estaven resolts: separadors (regla i corpus net) i majúscules (regla permissiva, que no demana unificar). El tercer, l'**amplada**, l'ha decidit l'usuari: **8 dígits per als valors de 32 bits** (adreces, contingut de registres, codificacions), i la resta segons l'amplada del seu rol. La regla és a `13_contrib.qmd §Criteris generals`. Mesurat a `c1bac38`, fora d'A3–A6: els **61 hexadecimals de 5 a 7 dígits** són tots camps, valors o màscares, i cap no és una adreça escurçada: immediats de `lui`/`auipc` de 20 bits (A2, S2), números de bloc i etiquetes de memòria cau (A7, L6), números de pàgina de 20 bits (els 27 d'A8) i màscares de mantissa (L5). On el corpus mostra el contingut d'un registre, ja ho feia amb 8 dígits (`A2.qmd:1394-1421`, `S2.qmd:217`). **Tres canvis**: els comentaris `t1 <- 0x43` i `t2 <- 0x4142` d'`A2.qmd:1087-1088`, a la part correcta d'un bloc de codi deliberadament erroni (les errades són a L14 i L15), i l'adreça `0x100` d'`A1.qmd:267`. A A3–A6 no hi ha res a canviar: A3 només té immediats d'`auipc`, i A5 ho té tot amb 8 dígits | 📌 **Cas límit, resolt el 2026-10-01: el format reduït és correcte, i s'explicita.** Decisió de l'usuari: on un problema escriu adreces de 32 bits sense els zeros de l'esquerra perquè només en calen els bits de menys pes, el format hi és correcte, i es diu amb una «**Nota**:» a l'enunciat. En porten `exr-t7-fallades-programa` (on «l'adreça `0`» passa a `0x000`, com a S7) i `exr-t8-mv-proteccio`, que són els dos únics problemes amb hexadecimals curts sense amplada definida. No en porten els que defineixen la mida de la màquina (`exr-t7-cache-adreces`, 64 bytes; `exr-t8-mv-matriu-lru`, 64 KiB), on l'amplada surt de l'enunciat, ni els que escriuen adreces en decimal («a partir de l'adreça 0»: `exr-t7-cache-matriu`, `exr-t7-assoc-versions`, `exr-t8-mv-cache-tlb`). La regla, amb l'excepció, és a `13_contrib.qmd §Criteris generals`. Text sencer de l'entrada: `git show c1bac38:TODO.md` |
| **Tanques de codi fora de la convenció** (entrada de §Tasques transversals, detectada i retirada el 2026-10-01; confirmada per l'usuari) | **Executada: 40 tanques** passen a la forma de `13_contrib.qmd §Blocs de codi`. Les 33 ` ```c ` (E4 28, E5 3, A7 2) passen a `{.c filename="C"}`; les 6 ` ```s ` d'E4, a `{.s filename="RV32I"}`, tret de la d'`E4.qmd:218`, que conté `mul` i passa a `RV32IM`; i el fragment de C amb buits d'`E4.qmd:437`, que no tenia cap llenguatge, a `{.c filename="C"}`. Obertures i tancaments quadren a tots tres fitxers, i el render és net. ⚠️ **La xifra de tanques sense llenguatge que publicava l'entrada era falsa: 24, quan en són 19.** Les 5 d'`A2.qmd` eren **tancaments** de blocs que obren dins d'un element de llista (`- ```{.c …}`), que l'escàner no reconeixia com a obertura. És la regla 4 (cobrir totes les formes), aplicada a l'eina de mesura mateixa | Les 19 sense llenguatge es deixen: són sortida de RARS (`L5` 8), disposicions aritmètiques en binari (`A1` 7) i 3 a `A3`, que espera el port de `!5`. També es deixen els 3 `{.default}` sense `filename` (`L2.qmd:304`, un bolcat de RARS, i un a A4 i un altre a A5, a `temes456`). Ordre: `git grep -h -E '^\s*[`]{3}[cs]\s*$' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' \| wc -l` → 0 (dins de la taula, `\|` és una barra escapada) |
| **Veu dels enunciats: 99 imperatius en singular a E1, E2, E3 i E9** (entrada de §Tasques transversals, detectada i retirada el 2026-10-01; confirmada per l'usuari) | **Executada: 151 formes passen al plural**, de les quals 131 són imperatius a l'inici de frase o d'apartat i 20 dins de la frase. La xifra registrada (99) es quedava curta per tres motius: la llista de verbs era incompleta (faltaven «Efectua», «Respon», «Assumeix», «Desassembla», «Il·lustra-ho» i l'indicatiu «Pots»), l'escombrada només mirava majúscules, i **E4, E6 i E8 també en tenien**, dins de la frase (`E4.qmd:530` barrejava «Apliqueu», «usa» i «Escriviu» en una sola línia). Les terceres persones («el bucle que calcula», «que converteix», «s'executa») i els noms («**Nota**», «Crida al sistema») es deixen. **Les solucions no hi entren**: són a `.callout-tip`, que segons `13_contrib.qmd §Criteris generals` fa servir la 2a persona del singular | Cap pendent. La nota de `13_contrib.qmd §Problemari i solucionari`, que deia «aplicat sistemàticament a E6 i E4», diu ara que s'aplica a E1–E9. Escombrada amb la llista ampliada de verbs (`25_scripts/escombrada.sh --cas -w '(Tradueix\|Escriu\|…\|Pots\|Programa)' -- 02_exercicis`; dins de la taula, `\|` és una barra escapada) → 0 |
| **Exercicis → Problemes** (entrada de §Tasques transversals; identificadors fets a `9dc02f6` i `1c9aae5`, etiqueta feta i entrada retirada el 2026-10-01) | **Executada.** «Problema» a Problemes i Solucions i «Exercici» al laboratori, en tots dos formats (decisions de l'usuari: només en aquestes parts, i macro LaTeX per al PDF). HTML: `language:` a la capçalera dels 19 E/S. PDF: «⁂» com a títol i prefix (`_quarto.yml`), expandit a `\exercisename` (`preamble.tex`), amb un `\renewcommand` a l'inici d'E1 i de L1. Verificat amb `make render-complet`: al PDF, 299 «Problema» i 91 «Exercici», que sumen els 390 d'abans; les referències de les solucions diuen «Problema»; cap `⁂` ni `\exercisename` literal; els prefixos dels callouts es mantenen. A l'HTML, «Problema 11.x» a E2 i S2 i «Exercici 30.x» a L3 | Cap pendent. El mecanisme, i les dues formes que es van provar i no funcionen (bloc `crossref:` al fitxer; `\exercisename` directament al prefix), són a `13_contrib.qmd §Problemari i solucionari`. Història de l'entrada: `git show 171cf18:TODO.md` |
| **Regla d'ús `AND`, `OR`, `XOR`, `NOT`–barra superior (enters)** (entrada de §Tasques transversals, d'una sola línia, de `9faab05`, 2026-07-13; retirada el 2026-10-01) | **Executada.** La regla no era escrita enlloc. Mesurat a `41ce419` (`git grep -o -P`, sense `TODO.md` ni `13_contrib.qmd`), el corpus ja la seguia gairebé sencer: a les fórmules, `\land` 5, `\lor` 3, `\oplus` 17 i `\overline` 21 (més 1 de període decimal); a la prosa, AND/OR/XOR/NOT en majúscules i sense format; a les instruccions, minúscula i `` ` ``. Decisió de l'usuari: s'escriu tal com és, amb les taules ISA dins de la regla (opció A), a `13_contrib.qmd §Codi, matemàtiques i cursiva`. S'hi alineen les 15 línies que se'n desviaven: 12 files de taula ISA a `21_riscv/` amb `\text{ and }`/`or`/`xor`/`and not` (lògiques 6, Zicsr 6), `A2.qmd:1269` (`ori`) i els dos $\sim$ (`RV32I_pseudo_not.qmd:1`, `S5.qmd:37`). També, a petició de l'usuari, parèntesis a la fórmula del *carry-out* d'`A4.qmd:75`, que barrejava $\land$ i $\lor$ sense. Ordre que ho comprova (15 abans, a `41ce419`; cap després): `git grep -n -I -F -e '\text{ and' -e '\text{ or' -e '\text{ xor' -e '\sim' -e '\neg' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'` → cap. Fora d'abast i viu: el marcador del revisor `A3.qmd:184` (no fer servir «NOT»), a §Decisions obertes → Anotacions de la revisió externa de T3. | `git show 41ce419:TODO.md` |
| **Cometes `"..."` → `«...»`** (entrada de §Tasques transversals, retirada el 2026-10-01) | **Executada.** Les sis línies de prosa d'A2 es van fer a `da35dfe`; l'última, `A4.qmd:119` («s'ha «donat la volta»»), en repassar A3–A6 després de la fusió de `temes456` (fase 2). A A3–A6, la resta de casos de l'ordre són comentaris HTML (marcadors) i codi C. Ordre, ara sense exclusions: `git grep -nP '(?<![-\w=])"[^"]*\p{L}[^"]*"' -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd'` i treure'n les línies amb atributs `x="…"` (`grep -vP '\w+="'`); `lint_prosa.py` ja no en troba cap. | `git show c4c247a:TODO.md` |
| **Ordre substantiu–adjectiu: «precisió simple/doble» al material de T5** (entrada de §Tasques transversals; decidida i aplicada fora de T5 a `681556a`; retirada el 2026-10-01) | **Executada.** Després de fusionar `temes456`, l'usuari decideix canviar-ho ara (opció a), tot el tema alhora perquè la teoria i els problemes diguin el mateix. **55 ocurrències** (56 a l'entrada: la revisió externa va treure una frase d'A5): A5 20, S5 10, L5 8, E5 8, `24_specs/registres.toml` 2 (font de la figura `T5_ieee754_format_registre__registre_*`, regenerada) i SVG 7: `T5_recta_global.svg` 1 i `T5_recta_zoom_zero.svg` 2 (fonts natives), `T5_ieee754_format_registre.svg` 1 (no consumit) i els tres esborranys sense cap referència, que l'usuari també vol actualitzats: `T5_recta_global__org.svg` 2 i `T5_recta_zoom_zero__org.svg` 1. Formes: «simple i doble precisió» → «precisió simple i doble», i les capitalitzades («Simple precisió» → «Precisió simple»). Els identificadors (`#imp-ec-simple-precisio`, `#exr-t5-ieee-doble-precisio`…) no canvien. Ordre, insensible a majúscules i sobre tots els tipus de fitxer: `git grep -n -i -E "(simple|doble) precisió" -- . ':!TODO.md'` → només la regla de `13_contrib.qmd`. | `git show d50b0ba:TODO.md` (amb la taula de fonts i generats i la lliçó de les dues trampes) |
| **Criteri «quatre formats nuclears» aplicat a A3 sencer** (entrada de §Tasques per tema → T3; retirada el 2026-10-01) | **Executada.** Cap text d'A3 no donava un recompte de formats. El problema era d'ordre: `A2.qmd:260` ajornava el format U a T3, i a A3 el J (`:516`) es presentava com a «variant del format Tipus-U, presentat més avall en aquest mateix tema», abans del U (`:1083`). Decisió de l'usuari (opció b): el callout `#nte-format-u` passa a T2, a §Operands en mode immediat, al costat de `lui`, i la figura passa de `T3_instruccio_tipus_U` a `T2_instruccio_tipus_U` a `24_specs/registres.toml`; el J i l'expansió de `la` d'A3 hi remeten. L'identificador no canvia (`11_riscv.qmd:50` hi remet). Mesura de l'abast a A3 (sobre `41ce419`): `git grep -n -i "format\w* \*\*Tipus\|Tipus-[BJUSIR]\b\|formats\? d'instrucci\|sis formats\|quatre formats" -- 01_apunts/A3.qmd` → 7 línies, totes llegides. La regla, amb on es presenta cada format, a `13_contrib.qmd §Decisions per tema → T2 i T3`. | `git show f066a8e:TODO.md` |
| **R5-TYPE (RISC-V *compressed*) com a aprofundiment** (`A5.qmd:6`; anotació #6 de la revisió externa de T4–T6) | **Decidida: no** (usuari, 2026-10-02, fase 6, a proposta de Claude Code i amb la valoració «No val la pena» del grup). Motius: no existeix cap format «R5» —l'extensió C té nou formats de 16 bits (CR, CI, CSS, CIW, CL, CS, CA, CB i CJ)—; A2 ja presenta l'extensió C (`A2.qmd:84`) i diu que les instruccions poden ser de 16 bits (nota al peu de `#sec-format-instruccions`); i RARS 1.6 no admet l'extensió C, de manera que al laboratori no es podria veure mai. Marcador esborrat | El text del marcador era: «com a "aprofundiment" R5-TYPE (RISC-V compressed) per a la codificació de les instruccions? Al principi de T2?». Es recupera amb `git show 48f0f06:01_apunts/A5.qmd` |
| **R4-TYPE a T5** (`A5.qmd:5`; anotació #5 de la revisió externa de T4–T6) | **Decidida i executada** (usuari, 2026-10-02, fase 6, a proposta de Claude Code; el grup l'havia valorada «Decisió»): aprofundiment `#wrn-instruccions-fusionades` a A5 §Instruccions (`#sec-instruccions-rvf`), darrere de `#nte-instruccions-aritmetiques-f`, amb les quatre instruccions fusionades, el format R4 (`#fig-format-r4`, figura `T5_instruccio_tipus_R4` de `24_specs/registres.toml`) i el motiu de fons: `fmadd.s` arrodoneix una sola vegada, i la seqüència `fmul.s` + `fadd.s`, dues (remet a §Arrodoniment i §No-associativitat). Marcador esborrat | ⚠️ **L'entrada deia que la figura era «sense ús», i només ho era a mitges**: la figura individual no la usava ningú, però l'entrada R4 del `.toml` alimenta `compendi_registres` (`#nte-rv-instruccions-formats-detall` a `11_riscv.qmd`), de manera que mai no es podia esborrar. En analitzar-ho es va trobar l'errada de la figura de `#nte-instruccions-tipus` d'A2 (§T2). El text del marcador era «cal introduir el R4-TYPE? (Harris)»; es recupera amb `git show 48f0f06:01_apunts/A5.qmd` |
| **La figura de `#nte-instruccions-tipus` mostra els set formats, no R, I i S** (entrada de §Tasques per tema → T2, detectada el 2026-10-02; retirada el mateix dia) | **Executada (fase 4, a proposta de Claude Code; usuari, 2026-10-02).** El retall de `compendi_registres` no era net: la capçalera de números de bit hi porta `27` i `26`, que són només del `funct2` de R4 i haurien quedat penjats, i la fila inferior d'amplades és la de R4. Es fa amb una variant a `25_scripts/gen_regs.py`: la taula `COMPENDIS` hi genera ara dos compendis, `compendi_registres` (els set formats; sortida idèntica byte a byte a l'anterior, verificat) i `compendi_registres_RIS` (R, I i S, amb les amplades de R a la fila inferior). `A2.qmd §Format de les instruccions RV32I` inclou el segon; `11_riscv.qmd` continua amb el primer. Documentat a `13_contrib.qmd §Política de generació SVG` («Figures de registres de bits»). Ordre que ho comprova (després de `make render`): `grep -o "<text[^>]*>[^<]*</text>" auto_figs/compendi_registres_RIS__registre_light.svg | grep -c "Type"` → 3 (i 7 per a `compendi_registres__registre_light.svg`). | `git show 0d7bd5c:TODO.md` (l'entrada sencera, a §Tasques per tema → T2) |
| **Anotacions de la revisió externa de T3 (MR `!5`)** (entrada de §Decisions obertes, registrada el 2026-10-01 en portar la MR, `ab48732`; retirada el 2026-10-02) | **Executada.** Els vuit comentaris de Pedro J. Martinez-Ferrer, valorats i resolts: set a la fase 3b de `CLAUDE.md §Pla de treball` (de `fec6d95` a `4a5cad5`, decisions de l'usuari a proposta de Claude Code) i la «↔» a la fase 4 (`0d7bd5c`, «inverteix el LSb»). L'entrada en tenia el text, la valoració i el resultat de cadascun; l'original dels comentaris és a `62700c0`. Ordre que ho comprova: `git grep -n '<!-- TODO: PM:\|<!-- TODO: El caràcter' -- 01_apunts/A3.qmd | wc -l` → 0 (8 a `ab48732`). No hi quedava cap pendent: `#cau-boolea-c`, que no era d'aquesta revisió, té entrada pròpia a §Tasques per tema → T3. Que els comentaris siguin resolts no vol dir que el revisor doni T3 per tancat. | `git show 8dc3887:TODO.md` (l'entrada sencera, amb la taula dels vuit comentaris) |
| **Figures de half-adder i full-adder (T4)** (entrada de §Decisions obertes, `A4.qmd:79`, `:80`; anotacions #1 i #2 de la revisió externa de T4–T6; retirada el 2026-10-03) | **Executada (fase 5, 2026-10-03; esbossos aprovats per l'usuari).** La tasca (#1) i la decisió (#2, «sí que cal», valoració del grup) són ara `#fig-semisumador-sumador-complet` i `#fig-sumador-propagacio-rossec`, dins de `#wrn-sobreeiximent-maquinari`: SVG natiu a `22_figs_originals/`, generats per `25_scripts/gen_T4_sumador.py`. Convenció nova de portes lògiques a `24_specs/svg.md §16`. Decisions de terminologia de la mateixa sessió: *carry* → «ròssec» (escombrada del corpus, `e49c014`), *half-adder* → «semisumador» i *full-adder* → «sumador complet», aquestes dues pendents de confirmar al Termcat (§Tasques transversals). Els dos marcadors, esborrats. | Files #1 i #2 de l'inventari «Anotacions de la revisió externa de T4–T6» (§Decisions obertes); `git show 65f225a:TODO.md` per al text de l'entrada |
| **Revisió sistemàtica del corpus per nodrir les taules de `Símbols` i `Notació` de `12_sigles_simbols.qmd`** (entrada de §Tasques transversals, amb el 📌 «Notació de CPI, barrejada» i la nota de `NF`, `NC`, $T$ i *stride*; retirada el 2026-10-03) | **Executada (fase 7 de `CLAUDE.md §Pla de treball`, 2026-10-03; decisions de l'usuari a proposta de Claude Code), en cinc commits.** (1) `a5340f3`: la regla de `\text{…}` per a les sigles dins de fórmules. Mesurada **per forma** —dins de `$…$` i `$$…$$`, fora dels blocs de codi—, el CPI sense `\text{}` era 29 (S6 19, `12_sigles_simbols.qmd` 10), no els 13 que dona el patró `$CPI` de l'entrada, que només veu el CPI que obre la fórmula; ara 0, i `\text{CPI}` passa de 45 a 74. La resta de sigles que l'escombrada va trobar: `\text{CI}` (S3, sigla no definida) → $n_{ins}$; els registres $MD$ i $MR$ d'E4, a text pla. (2) `ca98373`, T6: S6 i E6 amb la notació d'A6 ($s$, $s_{max}$, $P_x$, $s_x$, $f_A$, $P_d$…), amb la col·lisió greu de S6, on $f$ era la fracció d'Amdahl i alhora la freqüència. (3) `e0ff377`, T4 i T5: una sola notació per a la divisió ($x = y \cdot q + r$; n'hi havia tres a A4), el producte combinacional, i $b_{-(p-1)}$ a A5, que donava $p$ bits a la fracció contra el $p-1$ del mateix tema. (4) `477b9ca`, el glossari: Símbols 100 → 109 files i Notació 17 → 27, amb les files que no deien el que hi ha al corpus corregides ($f_B$ «de bus», $n_c$ «nombre de cicles», $V$ «tensió a T7», $K$, $E$…), les remissions de TAM i ULP, que apuntaven a files inexistents, i la notació de les taules ISA. (5) `d61a848`: `\mathtt` → `\texttt` (44), `←` → `\leftarrow` i rangs `[a:b]` a les taules ISA, i el superíndex de Pandoc d'A3. Decisions de criteri escrites a `13_contrib.qmd` (§T4, §T5, §T6, §Sigles, símbols i notació i §Dins de les fórmules): subíndexs en cursiva també quan són sigles ($V_{CC}$, $t_{MP}$), i l'excepció de les taules ISA ($PC$, $MPIE$). ⚠️ **Dues afirmacions de l'entrada eren falses**: que $T$ (mida d'element) no tenia entrada —hi era des de `f041476` (2026-07-13), set dies abans que s'escrivís la nota D4 que ho deia (`5dc16d0`)—, i que les quatre (`NF`, `NC`, $T$, *stride*) eren «símbols de fórmules»: `NF` i `NC` són constants del codi, i ja eren `\texttt` a les fórmules. Cobertura de Símbols per tema, a `477b9ca`: T1 8, T2 1, T3 3, T4 20, T5 22, T6 33, T7 41, T8 9, T9 cap (l'entrada donava T1 6, T2 2, T3 3, T4 20, T5 17, T6 28, T7 39, T8 9, que reprodueix a `8e4702f`). T9 no té cap símbol: A9 i E9 no tenen fórmules, i S9 només hi té literals en `\texttt`. En surten dues entrades noves: «Guany, no *speedup*» (§Tasques transversals) i «Sigles: VPN i PPN» (§Decisions obertes) | `git show 8e4702f:TODO.md`. Les ordres de la mesura són als missatges dels commits: la del CPI, a `a5340f3`; la de la cobertura per tema, al del commit que retira aquesta entrada |
| **Etiquetes de classe d'instruccions en anglès a E6 i S6** (entrada de §Tasques per tema → T6; retirada el 2026-10-03) | **Executada.** Decisió de l'usuari (2026-10-03, a proposta de Claude Code): es tradueixen, com mana la taula de substitucions obligatòries. «Load» → «Lectura», «Store» → «Escriptura», «Load/Store» → «Lectura/escriptura», «L/S» → «L/E» (també $P_{L/E}$, $s_{L/E}$) i «Branch» → «Salt», a les taules i als 7 usos en prosa que l'entrada comptava. L'escombrada de la forma, amb la regla 6, en va trobar tres més fora de T6, que s'hi inclouen: `E3.qmd` («sense fer cap load»), `E9.qmd` («(load)») i `S_criteris_seleccio.qmd` (2). Total, 22 línies a `c186ca1`: E6 7, S6 11, E3 1, E9 1, `S_criteris_seleccio.qmd` 2. Queden fora els noms de les instruccions de les taules ISA, els identificadors i la glossa de les lletres (A2, A3). `13_contrib.qmd §T6` diu ara la regla | `git show c186ca1:TODO.md` |
| **Sigles: VPN i PPN són a la taula, i el criteri d'inclusió les exclou** (entrada de §Decisions obertes, registrada i retirada el 2026-10-03) | **Decidida: es queden a la taula de sigles** (usuari, 2026-10-03, a proposta de Claude Code). S'ajusta el criteri de `13_contrib.qmd §Sigles, símbols i notació`, que les posava d'exemple de nom de camp exclòs: a T8 són conceptes (encapçalen §Traducció d'adreces), no només noms de camp. `12_sigles_simbols.qmd` no canvia | — |
| **Verificació tècnica de la taula de restriccions d'alineació** (entrada de §Tasques per tema → T2, callout `#cau-memoria-restriccions-alineacio`; retirada el 2026-10-03) | **Executada (fase 7b, `5684c8a`; decisions de l'usuari 1a i 1b, a proposta de Claude Code).** La taula de `#nte-restriccions-alineacio` és correcta: les quatre files coincideixen amb `sizeof` i `_Alignof` de clang 19 per a `-mabi=ilp32`. La «correcció de la Fase C de L2» que l'entrada esmentava era només l'identificador (`1489c84`), i el registre de L2 ja havia verificat el contingut el 2026-07-19. Col·lisió amb l'alineació a 16 del BA: cap de real, perquè cap BA del corpus no conté un tipus de 8 bytes, però latent, perquè EC relaxa `sp` a múltiple de 4 i el fons de pila de RARS, `0x7FFFEFFC`, ja només ho és de 4; `#nte-abi-alineacio-pila` (A3) ho diu ara. A més, `#nte-punters-32-bits` diu que els punters s'alineen a 4, que és el que L2 demana a `#exr-punters-valors`. En va sortir un error d'A2: a RARS, `.dword` només s'alinea a 4 (fila «`L2.qmd:153-166`», a sota). Marcador esborrat | El text del marcador era «Verificar que la informació de la taula és correcta i coincideix amb l'ABI `ilp32` i que no hi ha col·lisió amb l'ABI RV de Bloc d'Activació alineació a 16». L'entrada sencera, a `git show a7876b9:TODO.md`; les ordres, al missatge de `5684c8a` |
| **`L2.qmd:153-166` — alineació de `.dword` a RARS** (entrada de §Tasques transversals; retirada el 2026-10-03) | **Decidida i executada (fase 7b, `1da9c2e`; opció D, decisió de l'usuari a proposta de Claude Code)**, que retira la declaració de l'usuari del 2026-07-19 de mantenir-ne el marcador per a la revisió externa (`git show a211bbf:TODO/L2_tasques.md`, l. 31). Una sola solució, la de l'ABI: la solució de `s2_1_1.s` porta `.align 3` davant de `cc`, i amb això RARS 1.6 dona exactament la fila «MARS» del comentari (verificat), que és ara el bolcat de `#exr-rars-vista-memoria`. Fora la «solució alternativa» de RARS, que presentava un error d'alineació com a resposta, i la menció de MARS, que és un simulador de MIPS. Error d'A2 que en surt, corregit al mateix commit: `#sec-directives-alineacio-memoria` deia que totes les directives de dades alineen soles, i a RARS `.dword` només s'alinea a 4; l'exemple `#tip-traduccio-declaracions-globals` deixava el `long long` a `0x1001000C`, i ara porta `.align 3` | El comentari esborrat, literal, amb la fila MARS i la RARS: §Dades preservades del comentari eliminat de `L2.qmd`, al final d'aquest fitxer. L'entrada, a `git show a7876b9:TODO.md` |
| **Unificar el format de les taules de pseudoinstruccions** (entrada de §Decisions obertes, dos marcadors, a `#nte-pseudoinstruccio-la` i `#imp-ec-la-offset`; retirada el 2026-10-03) | **Executada, opció A (fase 7b, `d9543e4`, `46bc860` i `8c780c3`; decisió de l'usuari a proposta de Claude Code).** `la` té taula amb el format de `mv`, `not` i `neg` (fragment nou, `21_riscv/RV32I_pseudo_la.qmd`), `#imp-ec-la-offset` també, `mv` diu «Expansió» sense «(ISA)», i el compendi té `#nte-rv-pseudo-la`. De pas, `<br/>` no arribava al PDF: l'expansió de `li` hi sortia enganxada i una capçalera d'A2 deia «Significaten anglès»; ara és `<br/>` per a l'HTML i `\newline` per al LaTeX (les quatre ocurrències del corpus). L'opció B, un sol esquema per a totes les taules, toca fitxers en revisió externa i té entrada pròpia a §Decisions obertes. Marcadors esborrats | El text dels dos marcadors era «TODO Roger unificar format taules pseudoinstruccions». L'entrada, a `git show a7876b9:TODO.md` |
| **La taula de l'exemple `#tip-codificacio-instruccions` surt del callout al PDF** (entrada de §Tasques per tema → T2; retirada el 2026-10-03) | **Executada (fase 7b, `6e885e8`; decisions de l'usuari 3A i 3b, a proposta de Claude Code).** `tbl-colwidths` passa de `[9,26,9,9,9,9,9,8,12]` a `[10,26,8,10,5,10,5,6,20]`: `offset[11:0]` acaba ara a x = 520,5 pt, dins del text del callout (524,0), i no a 549,4. A més, els rangs de l'immediat són complets (`sw`, `offset[11:0]`; `jal`, `offset[20:1]`), i una nota sota la taula diu quins bits ocupa a cada format: la columna `rd` de `sw` deia «-» quan els bits 11–7 porten `offset[4:0]`. En surt l'entrada «Revisar la distribució de les columnes de totes les taules» (§Tasques transversals), a petició de l'usuari | L'entrada, a `git show a7876b9:TODO.md`; l'ordre de la mesura, al missatge de `6e885e8` |
| **«Guany», no *speedup*, a E6, S6 i `S_criteris_seleccio.qmd`** (entrada de §Tasques transversals; retirada el 2026-10-03) | **Executada (fase 7b, `964eab6`; decisions de l'usuari 4 i 4b).** De 32 ocurrències en queden 5, una per fitxer, amb la cursiva de la primera aparició: A6:58, E6:71, S6:27, `S_criteris_seleccio.qmd`:99 i el glossari; A6:64 perd la segona cursiva. De pas (4b), la taula de T6 de `S_criteris_seleccio.qmd`, que el render no veu perquè el fitxer és comentat a `_quarto.yml`, segueix ara la resta de regles de `13_contrib.qmd §T6`: «Potència», «capacitat equivalent», $P$, «corrents de fuita», «unitat de coma flotant» i «maquinari» | L'entrada, a `git show a7876b9:TODO.md`; l'ordre, al missatge de `964eab6` |

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

## Dades preservades del comentari eliminat de `L2.qmd` (`#sol-mapa-memoria`)

Copiat aquí el 2026-10-03, al mateix commit que l'esborra (fase 7b, decisió D de l'usuari: una sola solució, la de l'ABI, amb `.align 3` a la solució de `s2_1_1.s`). L'entrada «`L2.qmd:153-166` — alineació de `.dword` a RARS» demanava preservar-ne la fila MARS, l'única que no existia enlloc més del corpus. **Des d'aquest commit sí que hi existeix**: amb `.align 3` davant de `cc:`, RARS 1.6 dona exactament aquell bolcat, i és el que mostra ara `#exr-rars-vista-memoria`. La fila RARS, que era el bolcat antic de `s2_1_3`, és la que ja no hi és. Text literal del comentari:

```
<!-- TODO Alineació de `long long` a RARS

⚠️ Problema: RARS alinea `.dword` a 4 bytes en lloc de 8, a diferència de GCC real i MARS.
Això fa que la solució del mapa de memòria sigui diferent segons el simulador:
- Solució correcta (GCC/MARS): cc s'alinea a 0x10010008 (4 bytes de padding entre bb i cc).
- Solució RARS: cc s'alinea a 0x10010004 (0 bytes de padding entre bb i cc).
Cal decidir quina versió presentar als alumnes i si s'ha d'afegir
una nota sobre aquest comportament. De moment es presenten les dues versions. 

                                                                  xxxx xxxxxxxxxx
MARS 0xfea800fb 0x00000000 0xfffffffd 0xffffffff 0x000000a0 0x000016a7 0x0000ffff 0x00000000
RARS 0xfea800fb 0xfffffffd 0xffffffff 0x000000a0 0x000016a7 0x0000ffff 0x00000000 0x00000000

-->
```

```bash
git grep -nE "0xfea800fb +0x00000000 +0xfffffffd" -- . ':!TODO.md'   # L2.qmd, el bolcat de #exr-rars-vista-memoria
git grep -nE "0xfea800fb +0xfffffffd" -- . ':!TODO.md'               # cap: la fila RARS només és aquí
```

⚠️ «A diferència de GCC real» no és exacte: l'assemblador GNU no alinea cap directiva de dades per si sol (verificat amb clang 19: `.byte` seguit de `.word` deixa la paraula a l'adreça 1), i és el compilador el que emet `.p2align 3` davant d'un `long long`. La nota d'A2 ho evita parlant només de RARS i de l'ABI.

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
