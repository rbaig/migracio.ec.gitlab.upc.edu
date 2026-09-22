# TODO

Reescrit el 2026-09-21 (auditoria, sessió 3) a partir d'un inventari complet:
les 58 entrades del `TODO.md` anterior, els 29 marcadors del corpus, els quatre
informes de l'auditoria i els registres de tasques del `TODO/`. Cada
entrada porta la comprovació que la sosté. Les entrades retirades són al
§Entrades retirades del final, amb el motiu i la còpia que en queda.

**49 entrades vives.** Una entrada = una vinyeta de primer nivell (`^- `) per
sobre de `## Entrades retirades`; les vinyetes indentades en són sub-ítems i no
compten. Ordre que ho mesura:

```bash
head -n $(($(grep -n "^## Entrades retirades" TODO/TODO.md | cut -d: -f1) - 1)) \
  TODO/TODO.md | grep -cE '^- '
```

Repartiment: `§Decisions obertes` 10 · `§Tasques transversals` 10 ·
`§Tasques per tema` 19 · `§Tasques globals` 10.

**El `TODO/` té un subdirectori, i el compte és de 17 fitxers versionats, no
de 10.** `CLAUDE.md` diu que al final el `TODO/` ha de quedar buit; qui
n'inventariï el contingut ha de comptar-lo recursivament, perquè un `ls` de
l'arrel en deixa set fora:

```bash
git ls-files TODO/ | wc -l                     # 17, el total
git ls-files TODO/ | grep -c '^TODO/[^/]*$'    # 10, només l'arrel
git ls-files TODO/laboratori/ | wc -l          # 7, el subdirectori
```

Els 10 de l'arrel són aquest `TODO.md` i **9 prompts** de revisió interna
(`Ax_Ex_Px__…__plantilla.md`, `Lx__…__plantilla.md`, `L2`–`L6__revisio_interna*.md`).

**Els 18 registres de tasques caducs es van esborrar el 2026-09-22** (`TODO/T1`–`T9_P_tasques.md`,
`TODO/L1`–`L6_tasques.md`, `saneja_tasques.md`, `substantiu_adjectiu.md`,
`12_sigles_simbols__revisio_interna.md`), un cop verificat un per un que la seva
Fase C era executada o que el pendent viu ja era en aquest fitxer. Es recuperen
tots amb `git show a211bbf:<ruta>`, que és l'últim commit on existien.

Els set de `TODO/laboratori/` no són residu: `startup.s` és l'original de RARS
que referencia §Dades preservades, i els sis `TODO.s` (`L0`–`L5`) són l'objecte
de l'entrada de renumeració de lliuraments. Cap dels dos grups no es pot
esborrar mentre l'entrada que el referencia sigui viva.

---

## Decisions obertes

Decisions pendents de criteri. Un cop preses, han d'aterrar a `13_contrib.qmd`.

- **Syntax highlighting**: confirmar que `.s` és correcte per a instruccions, macros i directives de RARS.

- **Criteris de codi C: completar.** Dos marcadors vius al corpus ho registren: `A2.qmd:692` (`<!-- TODO hi ha consens? -->`, just abans de `#imp-codi-format-criteris`) pregunta si els criteris de format de codi tenen consens entre professors, i `A2.qmd:693` (`<!-- TODO Miquel: podríem fer un checker -->`) proposa una eina de verificació de format, relacionada amb `25_scripts/verifica_laboratoris.py`, que ja existeix. Els dos marcadors segueixen al corpus fins que la decisió es prengui.

- **Figures portades d'extern: afegir-ne la font.** Dels PDF originals n'hi ha que són del Patterson (p. ex. T7 MC). Abast actual verificat: dues figures de T7 encara es consumeixen en versió `__extern_` (export de PDF, no nativa) — `A7.qmd:365,368,372` (`T7_assoc_conjunts_diagrama__extern_*`) i `A7.qmd:303,306,310` (`T7_cd_diagrama__extern_*`). Enllaça amb `§Contingut global → Figures externes (llicències)`.

- **R4-TYPE a T5** (`A5.qmd:5`, `<!-- TODO: cal introduir el R4-TYPE? (Harris) -->`): decisió d'abast de contingut. Rellevant perquè `24_specs/registres.toml` ja genera la figura `T5_instruccio_tipus_R4`, avui sense ús. El marcador és a la capçalera del fitxer, abans del `# {{< var tema5 >}}`, fora de cap secció.

- **R5-TYPE (RISC-V *compressed*) com a aprofundiment** (`A5.qmd:6`): decisió d'abast que **creua dos temes** — el marcador pregunta si aniria al principi de T2. Mateixa ubicació que l'anterior.

- **Figures de half-adder i full-adder (T4)** (`A4.qmd:80`, `:81`): dos marcadors consecutius dins de `#wrn-sobreeiximent-maquinari`. El primer és una **tasca** (afegir la figura d'un *half-adder* i la d'un *full-adder*); el segon és una **decisió**, pel signe d'interrogació: si cal la figura de la seqüència de *full-adders* amb la porta XOR per detectar el sobreeiximent en el darrer. Si es creen, SVG natiu segons `24_specs/svg.md`.

- **Taules de memòria de T2 → figura estàndard** (`A2.qmd:926`, `:964`): dos marcadors amb la mateixa tasca sobre dues taules diferents — la segona és dins de `#tip-endianness` i afecta `#fig-big-endian`/`#fig-little-endian`. Pendent de figura, no de decisió, però no hi ha secció de figures de T2 en aquest fitxer: hi entra aquí fins que se'n creï una.

- **Unificar el format de les taules de pseudoinstruccions** (`A2.qmd:584`, `:609`): dos marcadors amb text literal idèntic (`<!-- TODO Roger unificar format taules pseudoinstruccions -->`), el primer dins de `#nte-pseudoinstruccio-la` i el segon dins de `#imp-ec-la-offset`. Nota de progrés adreçada a una persona: o es fa la unificació i s'esborren, o es resolen des d'aquí. No poden quedar-se al corpus indefinidament.

- **Marcadors de codi deliberadament incorrecte sense categoria a `13_contrib.qmd`.** Els marcadors `⚠️ codi_erroni__*.c ⚠️` i `⚠️codi_erroni__alineacio_incorrecte.s⚠️` no són ni llenguatge ni context: són una marca semàntica de «codi deliberadament incorrecte», i la taula de `13_contrib.qmd §Blocs de codi` no en preveu la categoria. Cal decidir si mereixen fila pròpia. Ús actual verificat: 3 blocs, tots a `A2.qmd` (`:794` `codi_erroni__gcc_tipus.c`, `:1042` `⚠️codi_erroni__alineacio_incorrecte.s⚠️`, `:1770` `⚠️ codi_erroni__vectors.c ⚠️`); `grep -n "codi_erroni\|deliberadament incorrecte" 13_contrib.qmd` → cap fila. *(Detectat a la passada C; registrat aquí perquè l'informe que el contenia és transitori.)*

- **Ordre substantiu–adjectiu: «simple precisió» vs «precisió simple».** Són **dues tasques i en aquest ordre**; si s'executa la segona sense la primera, qui la faci donarà per fixat un criteri que ningú no ha fixat.

  **(i) Decidir la forma canònica i registrar-la a `13_contrib.qmd`.** Avui **no hi ha cap regla d'ordre substantiu–adjectiu** al fitxer de convencions: `grep -niP "substantiu|adjectiu|anteposa" 13_contrib.qmd` → cap resultat. (`13_contrib.qmd:143` parla d'«esbiaixat»/«biaix» i només fa servir l'ordre bo dins del títol d'una font citada; no fixa cap criteri.) La regla lingüística de fons: en català normatiu els adjectius **classificadors** van darrere del substantiu, i anteposar-los és un calc de l'anglès. Amb excepcions que la decisió ha de recollir: ordinals, quantificadors i indefinits, «mateix», «propi», «altre», adjectius valoratius idiomàtics, i **«simple» en sentit de «mer»** («un simple error tipogràfic»), que sí que va anteposat.

  **(ii) L'escombrada.** Asimetria mesurada sobre tot el versionat, exclòs `TODO/`, **insensible a majúscules**:

  | Forma | Ocurrències | Repartiment |
  | :--- | ---: | :--- |
  | «simple precisió» (calc) | **52** | 43 als `.qmd` + 9 fora |
  | «precisió simple» | **6** | tots als `.qmd` |
  | «doble precisió» (calc) | **10** | tots als `.qmd` |
  | «precisió doble» | **0** | — |

  ```bash
  git grep -oi "simple precisió" -- . ':!TODO/' | wc -l    # 52
  git grep -oi "precisió simple" -- . ':!TODO/' | wc -l    #  6
  git grep -oi "doble precisió"  -- . ':!TODO/' | wc -l    # 10
  git grep -oi "precisió doble"  -- . ':!TODO/' | wc -l    #  0
  ```

  ⚠️ **Dues trampes que l'execució ha d'evitar, totes dues comprovades:**

  **1. L'escombrada ha de ser insensible a majúscules** (`-i`). Sis ocurrències són capitalitzades perquè encapçalen columna o paràgraf, i un patró en minúscules se les deixa totes:

  ```bash
  git grep -n "Simple precisió\|Doble precisió" -- . ':!TODO/'
  # A5.qmd:63 (dues, capçaleres de columna) · S5.qmd:296, :309, :338, :351
  ```

  **2. L'abast no és només de prosa**: 9 ocurrències són fora dels `.qmd`, en sis fitxers. **Abans de tocar-ne cap cal saber quin és font i quin és generat**, perquè el tractament és oposat:

  | Fitxer | Naturalesa | Com s'hi canvia el text |
  | :--- | :--- | :--- |
  | `24_specs/registres.toml` (`:133`, `:136`) | **Font de veritat** (`CLAUDE.md §Fitxers de referència obligatòria`) | Editar-hi el `title` i **regenerar**: `gen_regs.py` produeix `auto_figs/T5_ieee754_format_registre__registre_{light,dark}.svg`, que és el que `A5.qmd:87,90,94` consumeix |
  | `22_figs_originals/T5_ieee754_format_registre.svg` | Font versionada, però **el corpus no en consumeix la variant `__original_`** | Comprovar si encara cal: hi ha **dues còpies del mateix text**, la del `.toml` i la d'aquest SVG |
  | `T5_recta_global.svg`, `T5_recta_zoom_zero.svg` | **Fonts natives** (`A5.qmd:268-275` i `:381-388` en consumeixen la variant `__original_`) | Editar l'SVG directament |
  | `T5_recta_global__org.svg`, `T5_recta_zoom_zero__org.svg` | **Esborranys versionats**, no referenciats per cap `.qmd`, `.yml` ni `.toml` | Decidir si es mantenen abans de perdre-hi temps |

  📌 **La lliçó, germana de la que ja teníem.** Fins ara la regla escrita deia que *un grep massa literal fabrica discrepàncies que no existeixen*. Aquesta entrada mostra l'altra cara: **també se'n deixa de reals**, i aquí ho va fer per les dues bandes alhora — un compte era sensible a majúscules i perdia sis capçaleres; l'altre mirava només els `.qmd` i perdia les nou de les figures. La forma completa de la regla: **el patró ha de cobrir totes les formes del que es mesura (majúscules incloses) i tots els tipus de fitxer on pot viure, no només els que es tenen al cap.**

  L'altre patró que el registre d'origen citava («el següent exemple» → «l'exemple següent») és **residual**: 6 ocurrències del calc contra 244 de la forma bona. *(Origen: `TODO/substantiu_adjectiu.md`, fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/substantiu_adjectiu.md`.)*

---

## Tasques transversals

- **Exercicis → Problemes** (slugs, callout header, refs, etc.). Els IDs d'`Ex.qmd`/`Sx.qmd` usen el prefix `p<N>-` (`#exr-p3-...`, `#sol-p3-...`), numeració llegada de les col·leccions MIPS on `p` feia referència a «problema». Amb la migració a RISC-V l'estructura és 1 tema = 1 fitxer `Ax.qmd`/`Ex.qmd`/`Sx.qmd`, per tant té més sentit `t<N>-` (de «tema»), coherent amb la numeració de la resta del llibre. Cal: (i) substituir `p<N>-` per `t<N>-` a tots els IDs `#exr-p<N>-*` i `#sol-p<N>-*`; (ii) actualitzar totes les referències creuades (`@exr-p<N>-*`, `@sol-p<N>-*`) a tot el repositori (`Ax.qmd` també en pot contenir); (iii) verificar que no queda cap referència trencada. **Nota**: E1/E3 tenen prefixos `p1-`/`p4-` respectivament, que no es corresponen amb el seu número de tema real (haurien de ser `t1-`/`t3-`) — cal aclarir aquest desajust abans de renumerar.

  Volum verificat: **498 ocurrències**, repartides per prefix p1–p9 (46, 56, 74, 74, 77, 67, 40, 32, 32).

  ```bash
  git grep -o "exr-p[0-9]*-\|sol-p[0-9]*-" -- '*.qmd' ':!TODO/' | wc -l   # 498
  ```

  Mecànic i de volum considerable: candidat clar per a Claude Code.

- **Grafia «No associativitat» vs «No-associativitat»** (detectada 2026-09-20, sessió B de la recuperació de diffs). Cal decidir quina és la canònica i harmonitzar-la. Afecta també «No distributivitat»/«No-distributivitat». Estat mesurat: el **corpus és unànime amb guionet** (5 ocurrències) i el fitxer de convencions és l'únic divergent:

  | Forma | On |
  | :--- | :--- |
  | «No-associativitat» | `A5.qmd:693` (títol de secció), `E5.qmd:204`, `S5.qmd:908`, `S_criteris_seleccio.qmd:89`, `:90` |
  | «No associativitat» | `13_contrib.qmd:155` (la convenció) |

  El commit `92345e4` («A5-E5-S5 revisió interna parcial») va introduir la forma amb guionet al solucionari, de manera que la del fitxer de convencions és l'anterior.

- **`S_criteris_seleccio.qmd` — taula de T1 incompleta** (auditoria, sessió 2, 2026-09-21). La taula de `## {{< var tema1 >}}` té **una sola fila** (`@exr-p1-enters-taules`, `:23`) i ha de recollir la resta de problemes seleccionats de `S1.qmd`. El marcador «TODO» que ho registrava era contingut destinat a l'alumne i es va substituir per la nota neutra de `:19` («*Taula provisional: recull els problemes de `S1.qmd` seleccionats fins ara.*»); **aquesta entrada és ara l'únic registre de la tasca**. El fitxer és comentat a `_quarto.yml:95`, de manera que avui no es renderitza.

- **`exr-moda` (L3): l'enunciat no diu què ha de contenir el lliurament `s3_4_2.md`** (detectada 2026-09-20). `L3.qmd:17` el llista com a lliurament i `L3.qmd:303` obre la secció `## \`s3_4_2.md\` i \`s3_4_2.s\``, però l'enunciat (llegit sencer, `:303-335`) només demana traduir `moda` i `_start` a RV32I i comprovar el resultat: enlloc no s'especifica què ha d'anar al fitxer `.md`. Només es dedueix llegint el solucionari. És el **mateix tipus de forat que ja es va detectar a P2**. Cal redactar a l'enunciat què s'espera del fitxer de lliurament.

- **`L2.qmd:156-166` — alineació de `.dword` a RARS** (registrat 2026-09-20; **no tocat** per la sessió 2, que el va declarar decisió viva). RARS alinea `.dword` a 4 bytes (no a 8, com fan GCC/MARS) i el solucionari presenta **les dues versions alhora**. Decisió pedagògica pendent: mantenir les dues, quedar-se només amb la de RARS (que és la que l'alumne observarà al laboratori), o explicitar millor per què se'n donen dues.

  ⚠️ **El bolcat comparatiu MARS/RARS de `L2.qmd:164-166` no existeix enlloc més del corpus.** Si en resoldre la decisió s'elimina el comentari, aquelles línies s'han de preservar aquí abans, com es va fer amb el bolcat d'`A2.qmd` a la sessió 2. Ordre que ho sosté: `git grep -n "fea800fb" -- . ':!TODO/'`.

- **Discrepància de noms a la figura Graphviz de T7** (detectada 2026-09-20): el fitxer font és `24_specs/T7_mc_politiques__graphviz.gv` i el SVG derivat és `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` — arrels diferents, el `_resum` només és al SVG. Documentat com a discrepància coneguda a `13_contrib.qmd §Figures Graphviz` perquè ningú no «l'arregli» pel cantó dolent. **Via de resolució**: renombrar el `.gv` a `T7_mc_politiques_resum__graphviz.gv` és **inofensiu** (cap script ni cap `.qmd` no el referencia: el `dot` s'executa a mà i el pre-render parteix del SVG ja generat). Renombrar el SVG, en canvi, **trencaria** les tres línies d'`A7.qmd` (648, 651, 655) que consumeixen `auto_figs/T7_mc_politiques_resum__graphviz__original_{light,dark}.svg`.

- **Revisió sistemàtica del corpus per nodrir les taules de `Símbols` i `Notació` de `12_sigles_simbols.qmd`.** Abast concret verificat, que fins ara no constava: la revisió creuada de T7/T8 va deixar **sense verificar la major part de la taula actual** — tots els símbols exclusius de T1–T6 i T9 que no s'hagin creuat casualment amb T7/T8. Sospitosos prioritaris per la seva similitud notacional (font típica de confusió símbol↔concepte): $CPI$/$CPI_i$/$C_i$, $f_B$/$f_{clock}$, $K$, $m$/$m_d$/$m_i$/$m_{L1}$/$m_{L2}$, $P$/$P_d$/$P_s$/$P_x$, $s_{max}$/$s_x$, $V_{CC}$/$V_{in}$/$V_t$ — **tots de T6, tema no verificat en cap xat anterior**. Cobertura actual de la taula `## Símbols`, per tema: T1 6, T2 2, T3 3, T4 20, T5 17, T6 28, T7 39, T8 9, **T9 cap**. *(Origen: `TODO/12_sigles_simbols__revisio_interna.md:147`, fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/12_sigles_simbols__revisio_interna.md`.)*

  Hi encaixa també: **`NF`, `NC`, $T$ (mida d'element) i *stride*** apareixen en fórmules de T4 i L4 i **no tenen entrada** al glossari (`git grep -n "NF\|stride" -- 12_sigles_simbols.qmd` → cap). *(Origen: `TODO/L4_tasques.md` D4, fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/L4_tasques.md`.)*

- **Revisió sistemàtica del corpus per l'aplicació de la regla d'ús `AND`, `OR`, `XOR`, `NOT`--`barra superior`** (enters).

- **Cometes `"..."` → `«...»`**: substitució global. Abast mesurat per forma (cometes rectes que envolten text amb lletres, descartats els atributs `clau="valor"`): **65 línies candidates en 14 fitxers** — `A1` 3, `A2` 12, `A3` 1, `A4` 1, `A5` 1, `A7` 9, `A8` 9, `A9` 1, `S4` 1, `L1` 2, `L3` 3, `13_contrib` 18, `RARS_directives` 3, `index` 1.

  ```bash
  git grep -nP '(?<![-\w=])"[^"]*\p{L}[^"]*"' -- '*.qmd' ':!TODO/' | grep -vP '\w+="'
  ```

  **Bona part són codi C i directives legítimes** (`printf("%d", x)`, `.asciz "cadena"`), que no s'han de tocar: el discriminador ha de ser cas a cas. Casos reals de prosa ja identificats: `A2.qmd:1446` («punter a», «multiplicació», «desreferència/indirecció»), `:1470` («adreça de»), `:1472` («ampersand»), `:1560` («variable de tipus punter al \<tipus\>»), `:1760-1761` («vector de 100 enters»).

- **Nova eina disponible: retalls (crops) SVG a partir d'una figura font única** (afegida 2026-07-13, revisió interna T5): `25_scripts/gen_crops.py` + `24_specs/retalls.toml`, integrat al `pre-render` de `_quarto.yml` entre `gen_regs.py` i `gen_dark.py`. Permet definir una figura «detall»/«zoom» com una finestra `(x, y, w, h)` sobre el `viewBox` d'una figura font ja existent, sense duplicar-ne el contingut. Documentat a `13_contrib.qmd §Retalls`. Aplicable només quan el detall és un subconjunt geomètric net de la font (cap connector/etiqueta tallat a mig camí).

  **Cap ús real encara**: `24_specs/retalls.toml` té 23 línies, **totes comentari**, i cap retall definit. S'ha valorat dues vegades per a les figures de T5 i descartat totes dues: (1) `T5_recta_zoom_zero` com a retall de `T5_recta_global` — `T5_recta_zoom_zero` mostra informació pròpia dels denormals (hexadecimals concrets) que la global no té espai per representar; (2) totes dues com a retalls de `T5_coma_flotant_racionals__drawio.svg` (figura orfe a `22_figs_originals/`, no referenciada per cap `.qmd`, que sembla l'esborrany original) — el drawio (7465 línies, estil amb fletxes i icones pròpies) no comparteix coordenades ni disseny amb les figures actuals en estil pla.

  **TODO futur**: investigar `gen_crops.py` sobre una figura global com la primigènia, és a dir, com a **font única des de zero** en lloc d'intentar-ho a posteriori sobre figures ja redibuixades per separat. Requeriria: (i) redibuixar aquesta figura en estil pla natiu (coherent amb `svg.md`, no drawio) com a única font de veritat amb tot el contingut (rang global + zoom de zero + denormals); (ii) definir a `retalls.toml` les finestres de cada vista actual; (iii) verificar que cada retall és net. Si viable, eliminaria la duplicació de manteniment entre les dues figures actuals. Fora de l'abast d'una revisió textual.

---

## Tasques per tema

### T2

- **Verificació tècnica de la taula de restriccions d'alineació** (`A2.qmd:1018`, callout `#cau-memoria-restriccions-alineacio`): comprovar que la informació de la taula és correcta i coincideix amb l'**ABI `ilp32`**, i que **no hi ha col·lisió amb l'alineació a 16 del Bloc d'Activació** que fixa l'ABI de RISC-V. Afecta el rigor tècnic i no consta en cap registre anterior (detectat a l'auditoria, sessió 1). És la taula que la Fase C de L2 va corregir, de manera que la verificació ha de cobrir totes dues. El marcador segueix al corpus fins que la verificació es faci.

### T3

- **Criteri «quatre formats nuclears» aplicat a A3 sencer**: vegeu `§Contingut global → Criteri «quatre formats nuclears d'instrucció»`, que n'és l'entrada canònica. A3 ja s'hi ha ajustat parcialment (referències creuades cap a T2 als callouts `#nte-format-b`, `#nte-format-j`, `#nte-format-u`), però cal revisar-lo sencer per aplicar el criteri de manera estricta i coherent a tot el tema. Fer en un xat de revisió interna dedicat a A3.qmd.

- **Decisió de contingut a `#cau-boolea-c`** (`A3.qmd:244`, pendent d'Adrià, obert des de la revisió de T3): el text diu que «unes expressions no nul·les s'interpreten com a certes» sense dir **quines**. Cal indicar com s'identifiquen les que sí i les que no. Afecta el rigor tècnic. El marcador segueix al corpus perquè la decisió és viva i no la pot prendre Claude Code.

- Retocs manuals pendents (Roger) a les figures:
  - `auto_figs/T3_ba_exemple__original_light.svg`
  - `auto_figs/T3_deps_multi__original_light.svg`
  - `auto_figs/T3_deps_exemple__original_light.svg`

### T4

- **Slug `{#sec-casos-especials}` genèric** (`A4.qmd:460`). Si mai cal desambiguar, `{#sec-casos-especials-divisio}`. ⚠️ **El registre d'origen deia que «ara no es referencia des d'enlloc; canviar-lo no trenca res», i això ja no és cert**: `S4.qmd:228` fa `@sec-casos-especials`, de manera que reanomenar-lo **obliga a tocar també aquella referència**. Prioritat baixa, però amb el cost actualitzat.

  ```bash
  git grep -n "casos-especials" -- '*.qmd' ':!TODO/'
  # A4.qmd:460 (definició) · S4.qmd:228 (referència)
  ```

  *(Origen: `TODO/T4_P_tasques.md:311`, tercera vinyeta del §8 «Pendents heretats que romanen oberts»; fitxer transitori esborrat, mai no va arribar a aquest fitxer fins ara. Es recupera sencer amb `git show a211bbf:TODO/T4_P_tasques.md`. El text original deia: «slug `{#sec-casos-especials}` és genèric; si mai cal desambiguar, `{#sec-casos-especials-divisio}` (ara no es referencia des d'enlloc; canviar-lo no trenca res, però tampoc no urgeix)» — l'última clàusula és la que ha caducat, com diu l'avís de dalt.)*

### T5

- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present. *(No retirar sense actualitzar `13_contrib.qmd:706`, que hi remet explícitament: «T5 → T9: `fcsr` → `@nte-zicsr` (vegeu `TODO.md §T5 P8`)».)*

### T6

- **Etiquetes de classe d'instruccions en anglès** a les taules d'E6/S6 («Load», «Store», «Branch», «L/S»…): decidir si es mantenen com a etiquetes de columna/fila (opció actual) o es tradueixen («Lectura», «Escriptura», «Salt»), coherentment amb les substitucions obligatòries de prosa. *(No retirar sense actualitzar `13_contrib.qmd:166`, que hi remet: «pendent una decisió transversal … (vegeu `TODO.md §T6`)».)*

- **Notació de la tensió d'alimentació a la fórmula de potència dinàmica** (auditoria, sessió 2, 2026-09-21). `A6.qmd:278` defineix `@eq-potencia-dinamica` amb $V_{CC}^{2}$, i `E6.qmd:192` també usa $V_{CC}$. `A7.qmd:113` deia $V^2$ i **ja s'ha harmonitzat** a $V_{CC}^{2}$ (citava la secció; ara cita l'equació, com fa `A6.qmd:354`). **Queda `S6.qmd:324`**, que usa $V$ de manera consistent dins de tota la seva derivació (`$C = P_{din}/(V^2 \cdot f)$`, `$V_A^2$`, `$C_A$`/`$C_B$`): canviar-hi només la línia que cita l'equació el deixaria incoherent amb el seu propi desenvolupament, de manera que l'harmonització de S6 **s'ha de fer sencera o no fer-se**. Decisió pendent; afecta la parella E6/S6, que ara no concorda.

### T7

- **`exr-p7-assoc-multinivell`: seqüència d'adreces truncada**. L'enunciat diu «seqüència de 28 adreces … : `0, 5, 10, 12, 34, 0, 66, ...`» i amb els tres punts l'exercici no és resoluble. Interpretació probable: 7 adreces repetides 4 vegades (28 accessos). **Contrastar amb el PDF original** i reescriure: «la seqüència de 7 adreces següent, repetida 4 vegades (28 accessos en total): `0, 5, 10, 12, 34, 0, 66`».

- **Figures pendents de reconstrucció com a natives** (requereixen LO Draw de Roger).

  ⚠️ **Descripció corregida (auditoria, sessió 3).** La versió anterior d'aquesta taula marcava quatre figures amb «🔴 Referència trencada». **Cap ho és**: les quatre tenen el div definit i la referència resol — la verificació de la sessió 2 (`make render` sense warnings, 0 `?@` als 39 HTML) ho confirma. El que està pendent és **reconstruir-les com a natives**, perquè avui es consumeixen com a exports (`__extern_`) o amb figura provisional. L'única ocurrència de `?@` al `_book/` d'avui és dins de `site_libs/quarto-html/anchor.min.js` (JavaScript minificat de Quarto), no una referència.

  | Figura | Ancoratge | Estat verificat | Què falta |
  | :--- | :--- | :--- | :--- |
  | `fig-cd-diagrama` | `A7.qmd:300` | Consumeix `T7_cd_diagrama__extern_{light,dark}` | Reconstruir com a nativa |
  | `fig-assoc-conjunts-diagrama` | `A7.qmd:362` | Consumeix `T7_assoc_conjunts_diagrama__extern_{light,dark}` | Reconstruir com a nativa |
  | `fig-ca-diagrama` | `A7.qmd:393` | Ja `__original_` (nativa) | Revisar si compleix `svg.md` |
  | `fig-texe-diagrama` | `A7.qmd:783` | Ja `__original_` (nativa). Referència: PDF pàg. 24 | Revisar |
  | `fig-mc-exemple-descomposicio-32bits` | — | Cap ancoratge al corpus | Export LO Draw a `23_figs_externes`; reconstruir com a natiu |
  | `fig-multinivell-diagrama` | — | Cap ancoratge | CPU→L1→L2→MP; LO Draw pendent |
  | `fig-multinivell-multicore` | — | Cap ancoratge | Xip 4 nuclis L1/L2/L3; LO Draw pendent |

  ```bash
  git grep -n "auto_figs/T7_cd_diagrama\|auto_figs/T7_assoc_conjunts_diagrama" -- '*.qmd' ':!TODO/'
  ```

- **`fig-lru-roger` (màquina d'estats LRU)**: decidir si cal figura independent, o si n'hi ha prou amb la que ja va inclosa dins `T7_lru_exemple.svg` (`A7.qmd:460`, `#fig-lru-exemple`). ⚠️ El comentari `<!-- TODO fig-lru-roger: diagrama d'estats -->` que ho registrava al corpus **ja no hi és** (eliminat a la sessió 2 per redundant amb aquesta entrada): `git grep -n "fig-lru-roger" -- '*.qmd' ':!TODO/'` → cap. **Aquesta entrada és ara l'única còpia.**

- **`fig-capacitat-exemple` a HTML**: dues figures separades (primera + segona passada) o figura única combinada? Existeixen totes tres variants a `auto_figs/` (`T7_capacitat_exemple__original_*`, `T7_capacitat_exemple_bucle_primera_passada__original_*`, `..._segona_passada__original_*`). Pendent de decisió.

- **Dos SVG orfes amb `____error____` al nom.** Versionats i no referenciats per cap `.qmd`:

  ```bash
  git ls-files | grep -i "error____"
  # 23_figs_externes/T7_texe_diagrama____error____.svg
  # 23_figs_externes/T7_tres_c_barres_light____error____.svg
  git grep -n "error____" -- '*.qmd' ':!TODO/'   # cap referència
  ```

  ❓ **Pregunta oberta**: l'`__error__` al nom marca una figura **a refer**, o són **descartables**? No s'ha decidit ni tocat res. *(Els altres quatre fitxers amb el mateix patró són a `auto_figs/`, que és a `.gitignore:5`: són derivats regenerables, no entren aquí.)*

### T8 — Figures pendents de creació

⚠️ **Xifra corregida (auditoria, sessió 3): en queden 7, no 8.** La versió anterior deia «8 figures de nova creació. Prioritat: `T8_mv_flux_traduccio` (resol `@fig-mv-flux-traduccio` 🔴)». **Aquella prioritat ja està feta**: `auto_figs/T8_mv_flux_traduccio__original_{light,dark}.svg` existeixen i `A8.qmd:270,273,277` els consumeixen des del div `{#fig-mv-flux-traduccio}` (`A8.qmd:267`), de manera que la referència tampoc no és trencada.

```bash
git grep -o "auto_figs/T8_[a-z_]*" -- 01_apunts/A8.qmd | sort -u
# només T8_mv_flux_traduccio__original_{dark,light}
```

Rutes de destí per a les 7 restants: `/auto_figs/T8_*__original_light.svg`.

### T9

- **F/G — Figures SVG**: diferides a una fase posterior. Estat actual: A9 consumeix 24 vegades `auto_figs/`, totes de la mateixa figura (`T9_cicle_interrupcio`).

### Laboratori

- **Renumeració de lliuraments (2026-07-05)**: els fitxers de lliurament de L2–L6 s'han renumerat al número de sessió (`s2_*`–`s6_*`; abans anaven una sessió endarrerits i col·lidien amb L1). El directori `TODO/laboratori/` conserva els subdirectoris `L0`–`L5` amb `TODO.s` (6 fitxers, verificat amb `find`): revisar-ne els noms quan es decideixi el mecanisme de descàrrega.

- **L6 — Tipografia d'UI de RARS**: L6 marca sistemàticament els elements d'interfície de RARS en negreta (**Tools → Data Cache Simulator**, **Set size**, **Reset**…), mentre que L4 i L5 (harmonitzat a la revisió interna de L5, 2026-07-20) usen cursiva, coherent amb l'exemple de `13_contrib.qmd §Codi, matemàtiques i cursiva` («A RARS: "F3", "Execute", "*Settings*"»). Abast mesurat: **22 negretes d'UI** a `L6.qmd`. Harmonitzar a cursiva en la seva pròpia revisió interna.

- **Cap material explica a l'alumne el punt d'entrada de RARS.** La regla existeix com a **convenció interna** a `13_contrib.qmd:204` («`_start` ha de ser la primera etiqueta de `.text`»), però cap `.qmd` no explica a l'estudiant que RARS comença a executar a la primera instrucció de `.text` i que `_start` no és una etiqueta reconeguda pel simulador. Proposta d'origen: un `#nte-` breu a L1 (§Punts d'aturada/execució) o a A2. Verificació: `git grep -n "primera instrucció del segment de text" -- '*.qmd' ':!TODO/'` → només `13_contrib.qmd:204`. *(Origen: `TODO/L4_tasques.md` D3(ii), fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/L4_tasques.md`.)*

- **Etiquetes de bucle heterogènies a L3.** El patró dominant al corpus és `for:`/`fifor:`; `L3.qmd:396,403,410,433` usa `for1:`/`ffor1:`/`for2:`/`ffor2:` en un mateix exercici. Harmonització menor, candidata per al xat de revisió interna de L3. *(Origen: `TODO/L4_tasques.md` D5, fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/L4_tasques.md`.)*

- **Expressions aritmètiques als operands: escombrada pendent de `Ex`/`Sx`/`11_riscv.qmd`.** La regla ja és consolidada a `13_contrib.qmd §Convencions globals del laboratori`, amb **exempció explícita** per a teoria, problemes i exàmens (decisió de la sessió 2: l'aritmètica als operands s'hi admet perquè fa visible l'estructura del càlcul; al laboratori cal el literal ja calculat). A4 i S4 van rebre la remissió a `@nte-rars-operands-literals` i **no es toquen**. Queda revisar la resta d'`Ex.qmd`/`Sx.qmd` i `11_riscv.qmd` per detectar casos que siguin realment de laboratori.

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

  ```bash
  git grep -n "T4_multiplicador_sequencial" -- '*.qmd' ':!TODO/'
  # A4.qmd:175,178,182 — totes tres al .svg
  ```

### Contingut global

- **Criteri «quatre formats nuclears d'instrucció» (RISC-V International)**: adoptat a la revisió interna de T2 (2026-07). Font de veritat: `@riscv_rv32i` (docs.riscv.org, «four core instruction formats (R/I/S/U)»; B i J són variants de S i U). Revisar tots els fitxers del repositori (`Ax.qmd`, `Ex.qmd`, `Sx.qmd`, `11_riscv.qmd`, laboratoris) que esmentin el nombre total de formats d'instrucció de RV32I («sis formats», «6 formats», etc.) i ajustar-los, amb el mateix matís sobre B/J com a variants de S/U. Punt de partida fet: A2.qmd (T2) i referències creuades puntuals a A3.qmd (vegeu `§T3`).

- **Equacions a MathML**: **decisió presa — mantenir MathJax 3**; el pendent és reavaluar quan Quarto adopti MathJax 4 (partició de línies nativa). Avaluació preliminar (2026-07-04, prova real amb T5 + `-M html-math-method:mathml`): funciona (`underbrace`, `cases`, taules amb math correctes a Chrome) i elimina el JS de MathJax (render instantani, offline sense CDN). En contra: tipografia inferior a Chrome (MathML Core), numeració d'equacions inline (`\qquad(5.1)`) en lloc d'alineada a la dreta, i caldria adaptar els selectors `mjx-container` de `styles.css` a `math[display="block"]`. El desbordament mòbil ja està resolt via CSS.

- **PDF**: figures dins callouts no queden centrades → investigar via `preamble.tex`. A més, comportament en callouts encastats: es respecta la separació (`-1` del `layout=`), però no el repartiment si hi ha línies de text que no hi caben (falta l'exemple concret de `13_contrib.qmd`).

- **Figures externes (llicències)**: taula completa de figures extretes de PDFs (incloses fonts i llicències). Referència eliminada temporalment de `13_contrib.qmd`. Enllaça amb `§Decisions obertes → Figures portades d'extern`.

- **Gestió d'errades post-commit**: definir protocol. ⚠️ **La secció de destí és buida**: `13_contrib.qmd:756` té la capçalera `### Gestió d'errades` seguida directament de `## Eines`, sense cap contingut. En resoldre-ho, o bé s'omple la secció, o bé se n'elimina la capçalera i la tasca queda només aquí.

### Eines

- **`verifica_laboratoris.py` no dedueix el «bloc no autònom».** El script **ja té** la noció de bloc que no ha d'assemblar sol, però com a **taula codificada a mà**, no com a propietat derivada del contingut (`25_scripts/verifica_laboratoris.py:76`, `INCOMPLETE_BY_DESIGN`). Dues conseqüències:

  - **Una taula paral·lela al contingut divergeix en silenci** — el mateix motiu que va treure les plantilles `.markdown`. La raó codificada ja s'ha hagut d'actualitzar un cop (citava `@sol-update`; ara el bloc diu «vegeu la solució de `s3_4_1.s`»).
  - **`#exr-depuracio` no hi és**, i és el mateix cas per un altre camí: té tres errors a posta. Un bloc pot ser no autònom **per omissió** (falta codi) o **per incorrecció deliberada** (el codi hi és i està malament a propòsit).

  Cal una noció de **bloc no autònom** derivada del contingut. *(Origen: `TODO/decisions__informe.md`, informe transitori esborrat per `87f2853`; es recupera sencer amb `git show 87f2853^:TODO/decisions__informe.md`.)*

- **El `.gitignore` té `*.tex` i `preamble.tex` és versionat.** Avui funciona, perquè el `.gitignore` no desversiona el que ja ho està. La fragilitat és el cas futur: si mai se suprimeix `preamble.tex` i es torna a afegir, `*.tex` (`.gitignore:14`) se l'empassarà **en silenci**, i `git add preamble.tex` no dirà res tret que s'hi posi `-f`.

  ```bash
  git ls-files | grep "\.tex$"     # preamble.tex
  sed -n '10p;14p' .gitignore      # Estructura-de-computadors.tex  /  *.tex
  ```

  Verificat que el risc és real: un `.tex` nou a l'arrel queda ignorat per `.gitignore:14` i invisible a `git status`. Pesa més des que `make render` és HTML-only (2026-09-22): `preamble.tex` és el preàmbul LaTeX del PDF —el fitxer que algú editaria justament quan el PDF es trenqui— i els renders de PDF passen a ser rars, de manera que una pèrdua trigaria a fer-se visible. La línia 10 ja excepciona `Estructura-de-computadors.tex` pel seu nom; la correcció natural és afegir `!preamble.tex` després del `*.tex`, però **no s'ha tocat**: cal decidir si es vol l'excepció pel nom o restringir `*.tex` a l'artefacte generat.

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
| `_start` primera etiqueta de `.text` | **TANCAT** (sessió 2): verificats els 25 blocs de `.text` amb `_start` de L1–L6, **0 infraccions** | Regla consolidada a `13_contrib.qmd:204` |
| Nota obsoleta a `13_contrib.qmd:204` | Retirada pel mateix tancament: la nota ja no diu «pendent d'aplicar a L3» | — |
| Plantilles Markdown (`L2.qmd` i resta) | Executada a la passada C (`733b408`). `git grep '```{.markdown' -- '*.qmd' ':!TODO/'` → **cap** | — |
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
| `void main()` vs `int main()` | **Decisió presa i executada** a la passada C, bloc 2b (`b3072a6`) | Regla a `13_contrib.qmd:469`, justificació a `:471`, blocs protegits a `:479`. Estat del corpus: 40 `void main` i 4 `int main`, que són els **tres protegits** (`A2:797`, `E3:661`, `S3:685`) més `A2:1960`, que és la nota per a l'alumne, no codi |
| `index.qmd` — enllaç a `laboratori/L0/TODO.s` | RESOLTA: ja no hi és | — |
| `index.qmd` — fila duplicada de Toolchain | RESOLTA parcialment; la resta viu a §`index.qmd` | Aquest fitxer |
| `index.qmd` — enllaç «Còpia local» de `rars1_6.jar` | **Executada (decisió de l'usuari, 2026-09-21)**: el binari es queda **fora del repositori** i l'enllaç primari és la *release* de GitHub. Eliminada l'àncora `<a href="04_laboratori/rars1_6.jar" download>` d'`index.qmd:146`, mantenint la frase i l'enllaç de GitHub. Coherent amb `fbf7c3d` (2026-07-11), que va eliminar el binari perquè ja no era al disc. L'entrada antiga d'aquesta taula («URL de la còpia local: RESOLTA, ja hi és») era la que havia introduït l'àncora | **Cap còpia pendent**: `git grep -n "download>" -- '*.qmd' ':!TODO/'` → cap, i `git grep -n "04_laboratori/rars1_6"` → cap. No queda cap rastre apuntant al fitxer. El `README.md:174` el cita com a descàrrega externa, que és correcte |

### Caduques per mesura

| Entrada | Comprovació que la retira |
| :--- | :--- |
| **A1. Slugs `{#sec-}` a T1, T2 i T5** | Mesurat **per forma**, excloent capçaleres dins de callouts (que l'entrada ja exceptuava): **cap** capçalera `##`–`####` sense etiqueta a **cap dels nou fitxers `A1`–`A9`** — més fort que l'abast de l'entrada, que només parlava de T1, T2 i T5. Coherent amb `CLAUDE.md`, que declara A1–A9 «complet». ⚠️ **Avís per a qui la refaci**: les capçaleres `##` dins d'un callout són títols, no capçaleres de document, i s'han d'excloure. Un comptador que segueixi els `:::` amb un *toggle* es descompensa amb els callouts encastats, que obren amb `::::`: cal comptar **nivells**, normalitzant la tanca amb `lstrip(':')`, no alternar un booleà. Mesura correcta, que dona **0** als nou fitxers: vegeu §Mesura dels slugs, al final |
| **A2. Identificador duplicat `sec-opt-acces-sequencial`** | `git grep -n "{#sec-opt-acces-sequencial}" -- '*.qmd' ':!TODO/'` → **una sola definició** (`A4.qmd:681`). Les altres 6 ocurrències són referències `@` |
| **A3. Div sense tancar a `A7.qmd`** | 122 obertures `::: {` i 122 tancaments nus. `make render` de la sessió 2: **cap warning** |
| **A4. Referències creuades no resoltes** | Cap de les cinc existeix al corpus: `@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila`, `@imp-exception-handler`, `@sec-politica-reemplacement` → `git grep` sense cap ocurrència |
| **«ample de banda» → «amplada de banda»** | Única ocurrència a tot el corpus: `13_contrib.qmd:324`, que **és la regla de substitució mateixa** |
| **Unitats KB/KiB** | 5 ocurrències de `KB`, **totes definitòries**: `A2.qmd:171,178` (la taula que defineix el criteri) i `13_contrib.qmd:266,345` (la convenció) |
| **`****` sobrants** | `git grep -n '\*\*\*\*' -- '*.qmd' ':!TODO/'` → **cap** |

### Duplicades

| Entrada | Canònica |
| :--- | :--- |
| T3 — «quatre formats nuclears» | `§Contingut global`; la de T3 n'és el subconjunt i s'hi ha deixat com a remissió |
| T4 ítem 8 (figures half/full-adder) | `§Decisions obertes`, entrada dels marcadors `A4.qmd:80,81` |
| T3 T34 (`#cau-boolea-c`) | `§T3` |
| T7 C3, D1, D2, D3 | `§T7` |
| T6 C6 (etiquetes de classe) | `§T6` |

---

## Dades preservades del bloc eliminat `A2.qmd:744-810`

Aquestes dades **no existien en cap altre lloc del corpus** (`git grep -c "00c000ef" -- . ':!TODO/'` → només A2) i es van copiar aquí **abans** de la supressió, a la sessió 2. Documenten el mecanisme **exclòs** per la decisió del 2026-07-19 (assignatura, tots els professors): només tenen valor si algú reobre mai aquella decisió.

Bolcat de RARS en carregar un programa amb `startup.s` — les tres primeres instruccions de `.text`:

| Adreça | Codi | Bàsic | Línia font |
| :--- | :--- | :--- | :--- |
| `0x00400000` | `0x00c000ef` | `jal x1, 0x0000000c` | `jal main` |
| `0x00400004` | `0x00a00893` | `addi x17, x0, 10` | `li a7, 10` |
| `0x00400008` | `0x00000073` | `ecall` | `ecall` |

Flux complet documentat: `_start` → `main` → `exit` → `_exit`. RARS emulava `__start` i la syscall `exit` (número 10), però no la funció `exit` de la libc ni `_exit`. Contingut del fitxer `startup.s` tal com el presentava A2 (l'original de RARS, amb `__start` i `li a7, 10`, és a `TODO/laboratori/startup.s` fins que es buidi `TODO/`):

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
