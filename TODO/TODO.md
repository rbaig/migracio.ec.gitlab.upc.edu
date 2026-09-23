# TODO

Reescrit el 2026-09-21 (auditoria, sessió 3) a partir d'un inventari complet:
les 58 entrades del `TODO.md` anterior, els 29 marcadors del corpus, els quatre
informes de l'auditoria i els registres de tasques del `TODO/`. Cada
entrada porta la comprovació que la sosté. Les entrades retirades són al
§Entrades retirades del final, amb el motiu i la còpia que en queda.

**48 entrades vives.** Una entrada = una vinyeta de primer nivell (`^- `) per
sobre de `## Entrades retirades`; les vinyetes indentades en són sub-ítems i no
compten. Ordre que ho mesura:

```bash
head -n $(($(grep -n "^## Entrades retirades" TODO/TODO.md | cut -d: -f1) - 1)) \
  TODO/TODO.md | grep -cE '^- '
```

Repartiment: `§Decisions obertes` 10 · `§Tasques transversals` 13 ·
`§Tasques per tema` 15 · `§Tasques globals` 10.

Les tres entrades del 2026-09-23 (passades finals pendents, estat parcial de
T5, contradicció de T9) surten de la fusió de les dues seccions d'estat de
`CLAUDE.md`: eren pendents que només constaven a la secció eliminada o als
assumptes dels commits, i s'han registrat **abans** de treure-la. Les tres
següents (§T5, ítems 4.8, 4.12 i 3.8) surten de l'auditoria dels 29 ítems del
registre de T5, feta el mateix dia contra el corpus.

**El `TODO/` ja només conté aquest fitxer.** `CLAUDE.md` diu que al final ha de
quedar buit: el que falta per arribar-hi és buidar aquest `TODO.md` mateix, és a
dir, tancar o reubicar les entrades vives. Ja no hi ha cap subdirectori ni cap
altre fitxer, de manera que el compte recursiu i el de l'arrel coincideixen:

```bash
git ls-files TODO/ | wc -l                     # 1, només aquest fitxer
```

**Què se n'ha tret, i on és ara** (sanejament del 2026-09-22):

  - **18 registres de tasques caducs, esborrats** (`TODO/T1`–`T9_P_tasques.md`,
    `TODO/L1`–`L6_tasques.md`, `saneja_tasques.md`, `substantiu_adjectiu.md`,
    `12_sigles_simbols__revisio_interna.md`), un cop verificat un per un que la seva
    Fase C era executada o que el pendent viu ja era en aquest fitxer. Es recuperen
    tots amb `git show a211bbf:<ruta>`, que és l'últim commit on existien.
  - **9 prompts de revisió interna, moguts a `26_prompts/`** (`Ax_Ex_Px__…__plantilla.md`,
    `Lx__…__plantilla.md`, `L2`–`L6__revisio_interna*.md`). **No són transitoris**: són
    plantilles reutilitzables, i per això no entren al compte del que s'ha de buidar.
    Les rutes que citen (`CLAUDE.md`, `13_contrib.qmd`, `24_specs/svg.md`,
    `TODO/TODO.md`) són des de l'arrel del repositori i segueixen sent vàlides.
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

- 🔴 **CANVI DE CRITERI (usuari, 2026-09-23): `_start` surt de tot el codi del llibre i només es presenta a teoria.** Fins ara la convenció era l'oposada —`13_contrib.qmd:203-204` **exigeix** `_start` com a punt d'entrada i com a primera etiqueta de `.text`—, de manera que això **inverteix una regla consolidada** i s'ha d'executar de dalt a baix, no fitxer a fitxer. Tres parts:

  **(i) Afegir el callout a teoria.** A `A3.qmd §Compilació separada` (`{#sec-compilacio-separada}`, `A3.qmd:1857`), un `#nte-` amb el contingut: «A EC es programa directament sobre el xip (@sec-entorn-autonom-bare-metal); quan es programa en Linux, el SO exigeix que el punt d'entrada al programa estigui marcat amb l'etiqueta `_start`». Les dues àncores existeixen i resolen (`sec-entorn-autonom-bare-metal` és a `A1.qmd:87`).

  **(ii) Eliminar les etiquetes `_start` dels fragments d'assemblador.** Abast mesurat: **104 ocurrències de `_start`** a 10 fitxers, de les quals **26 són definicions d'etiqueta** (`^_start:`). Repartiment: `L5` 24 · `L4` 16 · `L3` 15 · `L6` 14 · `L2` 8 · `L1` 8 · `13_contrib` 2 · `A2` 2 · `E9` 1 · `A3` 1.

  **(iii) Eliminar les línies `.globl _start`.** ⚠️ **No totes les `.globl` se'n van**: de les **45** del corpus, **27 són `.globl _start`** i les altres **18 exporten símbols reals** (`suma`, `abs`, `descompon`, `compon`, `main`, `X`, `g`) i **s'han de mantenir**. Un esborrat per `.globl` sense discriminar el símbol trencaria la compilació separada de T3.

  ```bash
  git grep -o "_start" -- '*.qmd' ':!TODO/' | wc -l          # 104
  git grep -oE "^_start:" -- '*.qmd' ':!TODO/' | wc -l       #  26
  git grep -oE "\.globl\s+_start" -- '*.qmd' ':!TODO/' | wc -l  # 27 de 45
  ```

  ⚠️ **Cal reescriure la regla de `13_contrib.qmd:203-204` abans o al mateix temps**, perquè diu el contrari. Afecta també tres entrades d'aquest fitxer: la de **«Cap material explica el punt d'entrada de RARS»** (`§Laboratori`), que proposava documentar precisament la regla que ara desapareix i que **s'ha de reformular o retirar**; la fila **«`_start` primera etiqueta de `.text`»** de §Entrades retirades, que registra un tancament que aquest canvi deixa obsolet; i **§Dades preservades**, on `_start`/`__start` és el contingut històric i **no s'ha de tocar**.

- 🔴 **CANVI DE CRITERI (usuari, 2026-09-23): la directiva `.section` és obligatòria a tots els fragments d'assemblador.** Decisió pedagògica: `.section` s'ha de presentar a teoria i fer-se servir sistemàticament (`.section .data`, `.section .text`, etc.) en lloc de les formes nues. Abast mesurat: **126 directives de segment nues** (`.data`, `.text`, `.bss`, `.rodata` a principi de línia) contra només **5 `.section`** a tot el corpus. Cal: (i) decidir on es presenta la directiva a teoria (candidat natural: A2, on es presenten els segments) i registrar-ho a `13_contrib.qmd`; (ii) convertir les 126; (iii) comprovar que RARS accepta la forma llarga en tots els casos, **abans** de convertir res.

  ```bash
  git grep -oE "^\s*\.(data|text|bss|rodata)\b" -- '*.qmd' ':!TODO/' | wc -l   # 126
  git grep -o "\.section" -- '*.qmd' ':!TODO/' | wc -l                          #   5
  ```

  Es va detectar arran del canvi de criteri de `_start`: totes dues tasques toquen les mateixes capçaleres de fragment, de manera que **convé executar-les en la mateixa passada**.

- **Homogeneïtzació del format de les adreces** (usuari, 2026-09-23). Revisió transversal del format amb què s'escriuen les adreces i els valors hexadecimals a tot el corpus. `13_contrib.qmd` en fixa avui **dos** aspectes i en deixa la resta sense criteri:

  | Aspecte | Estat | Mesura |
  | :--- | :--- | :--- |
  | Espais de separació | ✅ **Regla fixada** (`13_contrib.qmd:130`: «sense espais», no separador cada 4 nibbles) i **corpus net** | `git grep -nE "0x[0-9A-Fa-f]{4} [0-9A-Fa-f]{4}" -- '*.qmd' ':!TODO/'` → cap. Les 99 de `L2.qmd` les va convertir la Fase C (`254509b`) |
  | Majúscules/minúscules | ⚠️ **Regla permissiva** (`13_contrib.qmd:267`: preferència per majúscules, «s'admeten minúscules perquè és el criteri de RARS», i diu explícitament que **no cal unificar-ho**) | **534 en majúscules · 36 en minúscules** (`A2` 5, `A3` 5, `L1` 1, `L2` 9 i la resta). La majoria de minúscules són **bolcats reals de RARS**, on la grafia és fidelitat a l'eina |
  | **Amplada / farciment de zeros** | 🔴 **Sense cap regla** | Conviuen amplades diferents dins d'un mateix fitxer: `A2` 64 de 8 dígits i 4 de 5; `A8` 6 de 8 i 27 de 5; `L2` 175 de 8 i 2 de 7 |

  **El que cal decidir és sobretot el tercer**: si les adreces de memòria s'escriuen sempre amb 8 dígits (`0x00400000`) o si s'admet escurçar-les quan no hi ha ambigüitat, i si el criteri val igual per a adreces, per a contingut de registres i per a codificacions d'instrucció. Un cop decidit, ha d'aterrar a `13_contrib.qmd` al costat de les altres dues regles.

  ⚠️ **Abans d'escombrar, dues cauteles.** (i) La regla de majúscules **exempta explícitament** els bolcats de RARS: una substitució global a majúscules els falsejaria. (ii) Els hexadecimals no són tots adreces —n'hi ha de valors, de màscares i de codificacions d'instrucció—, i el criteri d'amplada no té per què ser el mateix: mesureu **per forma i per rol**, no pel prefix `0x`.

- **Passades finals pendents: la Fase C no és el tancament de la revisió interna.** Entre «Fase C executada» i «revisió interna acabada» hi ha una etapa sencera —les *segones passades* o *passades finals*—, i el tancament és una **declaració de l'usuari**, no una cosa deduïble del corpus: `26_prompts/Lx__revisio_interna__plantilla.md` tanca preguntant si es donen per finalitzades la revisió pedagògica, la tècnica i la lingüística (tres preguntes separades). El model del que és una passada final el dona `26_prompts/Lx__revisio_interna__plantilla.md:52` per a L5: «contrast ISA oficial, comparació didàctica L4/L5/L6, lingüística dedicada», en xat separat.

  **Aquesta entrada és l'única còpia viva d'aquest pendent.** Fins ara només constava als assumptes dels commits, que el diuen a la segona meitat de la línia —el lloc on és més fàcil de perdre— i a la secció `CLAUDE.md §Seqüència de revisió pendent`, eliminada el 2026-09-23 per duplicada (`git show 397c2da:CLAUDE.md`). Els commits que el declaren:

  | Ítem | Commit | El que diu l'assumpte | Estat |
  | :--- | :--- | :--- | :--- |
  | T1 | `f5e8223`, `9de6756` | «Fase C completa. **TODO segones passades**» | ✅ tancat 2026-09-23 |
  | T2 | `31f7571` | «Fase C acabada. **Falta segones passades**» | ✅ tancat 2026-09-23 |
  | T4 | `9faab05` | «revisió interna acabada. **TODO segones passades**» | ✅ tancat 2026-09-23 |
  | T6 | `77853ff` | «Fase C acabada. **Següent segones passades**» | ✅ tancat 2026-09-23 |
  | **L4** | `3cae913` | «L4 revisió interna **pre passades finals**» | ✅ tancat 2026-09-23 |
  | L5 | `a83dc16` → `b5ca2f4` | «TODO darreres passades» → «**tres passades fetes**» (l'únic ítem amb la passada posterior feta) | ✅ tancat 2026-09-23 |

  ⚠️ **L4 era el cas crític**: `3cae913` és **l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu literalment que és *previ* a les passades finals. En tancar L4 (2026-09-23), l'usuari **dona per cobertes aquelles passades**: el que l'assumpte anunciava no s'ha de reobrir.

  📌 **Per què l'entrada segueix viva amb tots els ítems tancats.** **No és una llista de feina sinó la definició d'una etapa**: documenta que entre «Fase C executada» i «revisió interna acabada» hi ha les passades finals, i que el tancament és una **declaració de l'usuari** que no es dedueix del corpus. La taula de dalt ha passat a ser el **registre històric** de com es va tancar cada ítem que en tenia constància. La distinció segueix valent per a `L6.qmd` —l'únic ítem que resta obert a `CLAUDE.md §Estat dels materials`— i per a la revisió externa, on la mateixa confusió pot tornar a aparèixer. Es retirarà quan la revisió interna sigui tancada del tot.

- **Nova eina disponible: retalls (crops) SVG a partir d'una figura font única** (afegida 2026-07-13, revisió interna T5): `25_scripts/gen_crops.py` + `24_specs/retalls.toml`, integrat al `pre-render` de `_quarto.yml` entre `gen_regs.py` i `gen_dark.py`. Permet definir una figura «detall»/«zoom» com una finestra `(x, y, w, h)` sobre el `viewBox` d'una figura font ja existent, sense duplicar-ne el contingut. Documentat a `13_contrib.qmd §Retalls`. Aplicable només quan el detall és un subconjunt geomètric net de la font (cap connector/etiqueta tallat a mig camí).

  **Cap ús real encara**: `24_specs/retalls.toml` té 23 línies, **totes comentari**, i cap retall definit. S'ha valorat dues vegades per a les figures de T5 i descartat totes dues: (1) `T5_recta_zoom_zero` com a retall de `T5_recta_global` — `T5_recta_zoom_zero` mostra informació pròpia dels denormals (hexadecimals concrets) que la global no té espai per representar; (2) totes dues com a retalls de `T5_coma_flotant_racionals__drawio.svg` (figura orfe a `22_figs_originals/`, no referenciada per cap `.qmd`, que sembla l'esborrany original) — el drawio (7465 línies, estil amb fletxes i icones pròpies) no comparteix coordenades ni disseny amb les figures actuals en estil pla.

  **TODO futur**: investigar `gen_crops.py` sobre una figura global com la primigènia, és a dir, com a **font única des de zero** en lloc d'intentar-ho a posteriori sobre figures ja redibuixades per separat. Requeriria: (i) redibuixar aquesta figura en estil pla natiu (coherent amb `svg.md`, no drawio) com a única font de veritat amb tot el contingut (rang global + zoom de zero + denormals); (ii) definir a `retalls.toml` les finestres de cada vista actual; (iii) verificar que cada retall és net. Si viable, eliminaria la duplicació de manteniment entre les dues figures actuals. Fora de l'abast d'una revisió textual.

---

## Tasques per tema

### T2

- **Verificació tècnica de la taula de restriccions d'alineació** (`A2.qmd:1018`, callout `#cau-memoria-restriccions-alineacio`): comprovar que la informació de la taula és correcta i coincideix amb l'**ABI `ilp32`**, i que **no hi ha col·lisió amb l'alineació a 16 del Bloc d'Activació** que fixa l'ABI de RISC-V. Afecta el rigor tècnic i no consta en cap registre anterior (detectat a l'auditoria, sessió 1). És la taula que la Fase C de L2 va corregir, de manera que la verificació ha de cobrir totes dues. El marcador segueix al corpus fins que la verificació es faci. **Sobreviu al tancament de la revisió interna de T2** (2026-09-23): es resol des d'aquí, sense reobrir el tema.

### T3

- **Criteri «quatre formats nuclears» aplicat a A3 sencer**: vegeu `§Contingut global → Criteri «quatre formats nuclears d'instrucció»`, que n'és l'entrada canònica. A3 ja s'hi ha ajustat parcialment (referències creuades cap a T2 als callouts `#nte-format-b`, `#nte-format-j`, `#nte-format-u`), però cal revisar-lo sencer per aplicar el criteri de manera estricta i coherent a tot el tema. **La revisió interna de T3 es va tancar el 2026-09-23 sense aquesta passada**: es fa com a tasca d'harmonització transversal en un xat dedicat a `A3.qmd`, que no reobre la revisió del tema.

- **Decisió de contingut a `#cau-boolea-c`** (`A3.qmd:244`, pendent d'Adrià, obert des de la revisió de T3): el text diu que «unes expressions no nul·les s'interpreten com a certes» sense dir **quines**. Cal indicar com s'identifiquen les que sí i les que no. Afecta el rigor tècnic. El marcador segueix al corpus perquè la decisió és viva i no la pot prendre Claude Code.

- Retocs manuals pendents (Roger) a les figures:
  - `auto_figs/T3_ba_exemple__original_light.svg`
  - `auto_figs/T3_deps_multi__original_light.svg`
  - `auto_figs/T3_deps_exemple__original_light.svg`

### T4

- **Slug `{#sec-casos-especials}` genèric** (`A4.qmd:460`). Si mai cal desambiguar, `{#sec-casos-especials-divisio}`. ⚠️ **El registre d'origen deia que «ara no es referencia des d'enlloc; canviar-lo no trenca res», i això ja no és cert**: `S4.qmd:228` fa `@sec-casos-especials`, de manera que reanomenar-lo **obliga a tocar també aquella referència**. Prioritat baixa, però amb el cost actualitzat. Sobreviu al tancament de la revisió interna de T4 (2026-09-23): es resol des d'aquí, sense reobrir el tema.

  ```bash
  git grep -n "casos-especials" -- '*.qmd' ':!TODO/'
  # A4.qmd:460 (definició) · S4.qmd:228 (referència)
  ```

  *(Origen: `TODO/T4_P_tasques.md:311`, tercera vinyeta del §8 «Pendents heretats que romanen oberts»; fitxer transitori esborrat, mai no va arribar a aquest fitxer fins ara. Es recupera sencer amb `git show a211bbf:TODO/T4_P_tasques.md`. El text original deia: «slug `{#sec-casos-especials}` és genèric; si mai cal desambiguar, `{#sec-casos-especials-divisio}` (ara no es referencia des d'enlloc; canviar-lo no trenca res, però tampoc no urgeix)» — l'última clàusula és la que ha caducat, com diu l'avís de dalt.)*

### T5

- **P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9). Tenir-ho present. *(No retirar sense actualitzar `13_contrib.qmd:706`, que hi remet explícitament: «T5 → T9: `fcsr` → `@nte-zicsr` (vegeu `TODO.md §T5 P8`)».)*

### T6

- **Etiquetes de classe d'instruccions en anglès** a les taules d'E6/S6 («Load», «Store», «Branch», «L/S»…): decidir si es mantenen com a etiquetes de columna/fila (opció actual) o es tradueixen («Lectura», «Escriptura», «Salt»), coherentment amb les substitucions obligatòries de prosa. *(No retirar sense actualitzar `13_contrib.qmd:166`, que hi remet: «pendent una decisió transversal … (vegeu `TODO.md §T6`)».)*

### T7

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

- **Cap material explica a l'alumne el punt d'entrada de RARS.** La regla existeix com a **convenció interna** a `13_contrib.qmd:204` («`_start` ha de ser la primera etiqueta de `.text`»), però cap `.qmd` no explica a l'estudiant que RARS comença a executar a la primera instrucció de `.text` i que `_start` no és una etiqueta reconeguda pel simulador. Proposta d'origen: un `#nte-` breu a L1 (§Punts d'aturada/execució) o a A2. Verificació: `git grep -n "primera instrucció del segment de text" -- '*.qmd' ':!TODO/'` → només `13_contrib.qmd:204`. *(Origen: `TODO/L4_tasques.md` D3(ii), fitxer transitori esborrat; es recupera sencer amb `git show a211bbf:TODO/L4_tasques.md`.)*

  🔴 **Afectada pel canvi de criteri del 2026-09-23** (vegeu `§Tasques transversals`): si `_start` surt de tot el codi, aquesta entrada **no es pot executar tal com està escrita**, perquè proposava explicar a l'alumne una convenció que deixa d'existir. S'ha de reformular —el que caldrà explicar és que RARS comença per la primera instrucció de `.text`, sense parlar de `_start`— o retirar-se. **No s'executi abans que el canvi de criteri.**

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
| **T1 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T1 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C executada (`f5e8223`, 2026-07-12) i revisió acabada (`9de6756`, 2026-07-13), tots dos amb «TODO segones passades» a l'assumpte; **cap passada posterior**; declaració prèvia «tancat de facto» del 2026-07-12. Les segones passades que els commits anunciaven queden cobertes pel tancament i **no** s'han de reobrir | Dues coses que només constaven a la fila: (i) la **sincronització amb el remot del 2026-07-13** —`A1.qmd`, `S1.qmd` i les tres figures SVG verificades idèntiques a la versió de Fase C—, detall a `git show a211bbf:TODO/T1_P_tasques.md`; (ii) **SVG-6**, l'etiqueta «Objecte» → «Fitxer objecte» de `T1_flux_compilacio.svg`, que la Fase C va descartar perquè el text no cabia al requadre: **l'usuari ha revisat la figura el 2026-09-23 i la dona per correcta**, de manera que l'etiqueta es queda com és (`22_figs_originals/T1_flux_compilacio.svg`, «Objecte»). No queda cap pendent de T1 |
| **T2 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T2 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`31f7571`, 2026-07-12), amb «**Falta** segones passades» a l'assumpte i **cap passada posterior**; el registre no declarava cap estat final. Les segones passades queden cobertes pel tancament i **no** s'han de reobrir | ⚠️ **El tancament del tema no tanca els set marcadors vius d'`A2.qmd`**, que és el fitxer amb més marcadors del corpus. Es van comprovar un per un abans de tancar i **tots set ja tenen entrada viva** en aquest fitxer, amb la línia exacta: `:584` i `:609` (format de les taules de pseudoinstruccions) → `§Decisions obertes`; `:692` i `:693` (consens dels criteris de codi C i proposta de *checker*) → `§Decisions obertes`; `:926` i `:964` (taules de memòria → figura estàndard) → `§Decisions obertes`; `:1018` (taula d'alineació contra l'ABI `ilp32`, callout `#cau-memoria-restriccions-alineacio`) → `§T2`. Són decisions i verificacions que **sobreviuen al tancament de la revisió**: es resolen des de les seves entrades, no reobrint T2 |
| **T3 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T3 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`b55e413`, 2026-07-13) —assumpte **net**, sense cap «falta» ni «TODO»— i **cap passada posterior**; el registre no declarava cap estat final. T3 és l'únic tema amb el trio A/E/S revisat: `E3.qmd` i `S3.qmd` ja constaven amb la revisió interna completada | ⚠️ **Tres entrades vives del `§T3` sobreviuen al tancament** i es resolen des d'allà, sense reobrir el tema: (i) el marcador `A3.qmd:244` (`#cau-boolea-c`, decisió d'Adrià sobre quines expressions no nul·les són certes); (ii) els **retocs manuals de tres figures** (`T3_ba_exemple`, `T3_deps_multi`, `T3_deps_exemple`), pendents de l'usuari; (iii) el criteri «quatre formats nuclears» aplicat a A3 sencer. ⚠️ **Aquesta tercera demana literalment «un xat de revisió interna dedicat a A3.qmd»**: el tancament de T3 **no** la dona per feta, i si s'executa serà com a tasca d'harmonització transversal —l'entrada canònica és a `§Contingut global`—, no com una reobertura de la revisió |
| **T4 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T4 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: revisió interna acabada (`9faab05`, 2026-07-13) amb «TODO segones passades» a l'assumpte, **cap passada posterior**, i declaració prèvia «quasi tancat» del 2026-07-12. El resum final del registre (`:312`) deia «no queda cap decisió pendent tret de l'ítem 8» | És la fila més verificada de la taula: el Bloc 4c en va auditar els tres ítems que la primera taula del registre donava per oberts i va establir que **el 3 i el 4.2 són aplicats** (`#wrn-mul-modul-2n` a `A4.qmd:323`, referenciat des de `S4.qmd:214`; punter T4→T7 a `13_contrib.qmd:706`). **Cap pendent de T4 no depenia d'aquesta fila**: els tres que arrossega ja són entrades vives i sobreviuen al tancament — l'**ítem 8** (figures *half-adder*/*full-adder*, marcadors `A4.qmd:80,81`) a `§Decisions obertes`, el **`.png` del multiplicador seqüencial** a `§Tasques globals → SVG`, i l'**slug genèric `{#sec-casos-especials}`** a `§T4`. Vegeu també la fila **P3** d'aquesta mateixa taula, que registra el tancament de l'ítem 3 |
| **T5 · ítem 4.8 — dobles espais en prosa** | **Executada (2026-09-23).** Les tres línies de la llista de registres de `#sol-p6-ops-variancia` que alineaven la fletxa amb espais de farciment (`` - `q`   → ``, `` - `i`   → ``, `` - `m`   → ``) passen a un sol espai, com les altres dues de la mateixa llista. `S5.qmd:739-743`; prosa, no bloc de codi, de manera que hi aplica la regla de `13_contrib.qmd §Commits` | Cap pendent. Verificat: `sed -n '739,743p' 03_solucions/S5.qmd \| grep -cE "[^ ] {2,}[^ ]"` → 0 |
| **T5 · ítem 4.12 — cursives repetides de *sticky*** | **Executada (2026-09-23).** `E5.qmd:209` repetia `*sticky*` en cursiva quan la primera aparició del fitxer ja és a `:110`; s'hi treu la cursiva. La regla del projecte és cursiva només a la primera aparició per fitxer | Cap pendent. Estat final de les cinc ocurrències: `E5.qmd:110` i `A5.qmd:440` en cursiva (primeres de cada fitxer), `E5.qmd:209`, `A5.qmd:764` i `:789` sense |
| **T5 · ítem 3.8 — títol de secció «Suma i multiplicació»** | **Decisió presa i executada (usuari, 2026-09-23): «Suma i multiplicació» → «Operacions».** El registre recomanava deixar-ho com estava, i l'usuari decideix el contrari: el títol no cobria el contingut de la secció (hi ha també divisió, conversions i traducció a assemblador). **9 substitucions** en 3 fitxers: les capçaleres `E5.qmd:85` i `S5.qmd:372`, i les **7 files** de la columna de tema de `S_criteris_seleccio.qmd:82-88` | Cap pendent. Verificat abans de tocar res que les capçaleres **no porten etiqueta `{#sec-}`** i que cap `@sec-` no hi apunta (`git grep -nE "sec-suma-i-multiplicacio\|sec-suma-multiplicacio"` → cap), de manera que el canvi no trenca cap referència creuada. Després: `git grep -c "Suma i multiplicació" -- . ':!TODO/'` → cap ocurrència. «Operacions» encaixa amb els altres valors de la columna de `S_criteris_seleccio.qmd` («Multiplicació», «Divisió», «Matrius», «Operacions lògiques i desplaçaments»…) |
| **T5 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T5 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: **l'únic tema amb la revisió declarada «parcial»** pel commit mateix (`92345e4` i `b81e3fa`, 2026-07-13) i **cap passada posterior**. ⚠️ **Què volia dir aquell «parcial» ha quedat establert**: l'auditoria del 2026-09-23 va comprovar els **29 ítems** del registre un per un contra el corpus i en va trobar 26 aplicats; els dos d'execució que restaven (4.8, 4.12) i la decisió (3.8) es van executar el mateix dia. **Els 29 ítems del registre són tancats** | Sobreviuen al tancament, i es resolen des de les seves entrades sense reobrir el tema: les decisions **R4-TYPE** i **R5-TYPE** (marcadors `A5.qmd:5,6`, a `§Decisions obertes`) i **P8** (`fcsr` amb dependència cap endavant a `@nte-zicsr` de T9, a `§T5`). Cap de les tres no surt del registre de T5 |
| **T6 — notació de la tensió d'alimentació a S6** | **Decisió presa i executada (usuari, 2026-09-23): S6 passa sencera a $V_{CC}$.** L'entrada advertia que l'harmonització «s'ha de fer sencera o no fer-se», perquè tota la derivació de `S6.qmd` usava $V$ de manera consistent i canviar-ne només la línia que cita l'equació l'hauria deixada incoherent. **5 substitucions** a `S6.qmd`: `:324` ($P_{din} = C \cdot V_{CC}^2 \cdot f$), `:326` i `:344` (aïllament de $C$), `:334` ($V_{CC,A}$, seguint el subíndex de processador de `C_A`/`f_B`) i `:346` (capçalera de columna de la taula de vuit generacions) | Cap pendent. ⚠️ **Les unitats no s'han tocat**: les cinc ocurrències de `\text{ V}` que queden a `:328`, `:330`, `:361`, `:396` i `:398` són volts, no el símbol. `S6.qmd:394` ja usava $V_{CC}$ abans del canvi, de manera que el fitxer també era incoherent amb si mateix. Notació ara uniforme a `A6.qmd:270-278`, `E6.qmd:192`, `A7.qmd:113`, `S6.qmd` i el glossari `12_sigles_simbols.qmd` |
| **T6 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T6 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`77853ff`, 2026-07-12) amb «Següent segones passades» a l'assumpte, **cap passada posterior**, i declaració prèvia «quasi tancat» del 2026-07-12. El registre declarava les tres seccions (A, B, C) aplicades, amb una verificació per script que cap resultat numèric en `\mathbf{}` de S6 no s'havia alterat (32/32 idèntics) | `A6.qmd` **no tenia cap marcador viu**, i la discrepància de notació E6/S6 —l'únic pendent tècnic del tema— s'ha resolt al mateix commit del tancament (fila anterior). Sobreviu una sola entrada, a `§T6`: les **etiquetes de classe d'instruccions en anglès** («Load», «Store», «Branch») a les taules d'E6/S6, que és una decisió transversal, no pròpia de T6; `13_contrib.qmd:166` hi remet |
| **T7 · C3 — seqüència d'adreces truncada a `exr-p7-assoc-multinivell`** | **Executada (2026-09-23), contrastada amb el PDF original com demanava l'entrada.** L'enunciat deia «seqüència de 28 adreces … `0, 5, 10, 12, 34, 0, 66, ...`»: amb els tres punts l'exercici **no era resoluble**, i a més el text es contradeia (28 adreces «repetides 4 vegades» són 112 accessos). Ara diu «la seqüència de 7 adreces següent, repetida 4 vegades (28 accessos en total): `0, 5, 10, 12, 34, 0, 66`» (`E7.qmd:220-222`) | **La interpretació que l'entrada donava per probable queda confirmada per dues vies independents del `PDF_originals/`**: (i) l'enunciat original (`02_problemes.pdf`, problema 6.12 —T7 d'EC és el T6 dels originals—) diu «`0, 5, 10, 12, 34, 0, 66, ...` (que es repeteix **3 vegades més**)», és a dir 4 passades de 7 adreces; (ii) el solucionari original (`03_solucionari.pdf`) enumera la traça adreça per adreça i en dona el resultat, **$h_1 = 9/28$** i $h_2 = 7/19$, que només quadra amb 28 accessos totals. ⚠️ `S7.qmd` **no té solució per a aquest exercici**, de manera que l'enunciat n'era l'única còpia al corpus: era l'únic pendent registrat que deixava material inservible per a l'alumne |
| **T7 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T7 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: **cap passada posterior** i declaració prèvia «quasi tancat» del 2026-07-12. ⚠️ L'assumpte del commit (`2206477`, «T7-PE_T7-PS_T7 Fable raw») **no era una declaració d'estat sinó l'obertura de la revisió**: és anterior al refactor de directoris i és el commit que crea el registre. L'estat real és el del registre: **40 ítems ✅**, tres tandes de feina, i tanca dient «Pendent a `TODO.md §T7`: només C3» — que és la fila anterior, executada al mateix commit que aquest tancament | Sobreviuen quatre entrades del `§T7`, **totes de figures i totes dependents de l'usuari** (LO Draw o decisió): la taula de **7 figures pendents de reconstrucció com a natives**; **`fig-lru-roger`** (cal figura independent de la màquina d'estats LRU?), de la qual aquesta entrada **és l'única còpia** des que se'n va eliminar el marcador del corpus; **`fig-capacitat-exemple`** (dues figures o una de combinada?); i els **dos SVG orfes amb `____error____` al nom**, que ningú no ha decidit si són a refer o descartables |
| **T8 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de T8 de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C acabada (`ccae7dd`, 2026-07-13), assumpte **net** —sense cap «falta» ni «TODO»— i **cap passada posterior**. És l'únic dels nou registres de teoria que es declarava tancat a si mateix: «**Estat: revisió interna de T8 tancada.** Blocs A, B i C íntegrament [executats]» | `A8.qmd` **no tenia cap marcador viu**. Sobreviu `§T8 — Figures pendents de creació`: **7 figures** de nova creació, dependents de l'usuari, amb destí `/auto_figs/T8_*__original_light.svg`. ⚠️ La xifra ja era corregida de 8 a 7 per l'auditoria (sessió 3), en verificar que `T8_mv_flux_traduccio` existeix i que `@fig-mv-flux-traduccio` **no** és una referència trencada. Nota de comptabilitat: el `§T8` no té cap vinyeta `^- `, de manera que mai no ha comptat com a entrada viva encara que descrigui feina pendent |
| **T9 — contradicció sobre l'estat, i revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat, i la contradicció queda resolta per decisió.** L'únic commit de revisió de T9 (`87015d2`, 2026-07-11) acaba amb «**(s'ha d'acabar)**», mentre que el registre declarava «Fase C, **execució completa**». No es podien conciliar des del corpus —cap commit posterior no tanca el que `87015d2` deixava obert, i els que toquen A9/E9/S9 des de llavors són transversals (`c2a9171`, `d017ee2`, `7f243f5`, `257d37f`)—, de manera que la decisió era de l'usuari. **En tancar el tema, val el registre**: el «s'ha d'acabar» de l'assumpte descrivia l'estat d'aquell moment, no un pendent viu | `A9.qmd` **no tenia cap marcador viu**. Sobreviu una entrada al `§T9`: les **figures SVG**, diferides a una fase posterior (A9 consumeix 24 vegades `auto_figs/`, totes de `T9_cicle_interrupcio`). ⚠️ **Fora del `§T9`, T9 és el tema amb menys cobertura al glossari**: `12_sigles_simbols.qmd §Símbols` no té **cap** entrada de T9 (`grep -c "\| T9 \|"` → 0). Això no és un pendent de la revisió de T9 sinó de l'entrada transversal «nodrir les taules de Símbols i Notació», que ja ho recull i segueix viva |
| **L1 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L1.qmd` de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: «L1 revisió interna feta» (`fe53cfc`, 2026-07-13) —**l'assumpte més net dels quinze ítems**, sense cap clàusula posterior— i **cap passada posterior**. El registre confirmava les tres fases completades i que la tasca T8 es va eliminar perquè l'usuari ja l'havia resolta manualment a `L3.qmd`. La decisió de L1 es va aplicar amb l'opció 1 (blocs `{#sol-}` per als 7 exercicis, `L1.qmd:134,142,185,187`) | **Cap entrada viva era específica de L1.** Dues transversals hi poden aterrar: la del **punt d'entrada de RARS**, que proposa com a destí «un `#nte-` breu a L1 (§Punts d'aturada/execució) o a A2» —i que el canvi de criteri de `_start` obliga a reformular abans d'executar-la—, i el **canvi de criteri de `_start` i `.section`** mateix, que tocarà els fragments d'assemblador de `L1.qmd` (8 ocurrències de `_start`, 4 `.globl`). Cap de les dues no reobre la revisió de L1 |
| **L2 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L2.qmd` de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C executada en tres commits del **2026-09-20** (`1489c84`, `254509b`, `12bac2c`) i **cap passada posterior**. ⚠️ El registre declarava només **Fase B** i la seva reconciliació del 2026-07-20 deia «tota la llista **B1–B11** continua vàlida»: era cert el juliol, i la Fase C de setembre —dos mesos després d'escriure'l— la va deixar obsoleta. **Les onze accions B1–B11 són executades** | Les B1–B11 eren les «accions d'execució directa» de la Fase C de L2 (`git show a211bbf:TODO/L2_tasques.md §B`): B1 secció «Pseudoinstruccions `la` i `li`», B2 taules, **B3 format d'adreces**, B4 cursives d'anglicisme, B5 harmonització lingüística, B6 lectura prèvia, B7 fórmules d'adreça, B8 callouts «Comprovació pràctica», B9 amplada de valors, B10 slug amb errata, B11 actualització del `TODO.md`. **B3 verificada en tancar**: el registre en deia «~64 adreces» i n'eren **99**, totes convertides per `254509b`; avui `git grep -nE "0x[0-9A-Fa-f]{4} [0-9A-Fa-f]{4}"` no en retorna cap. Sobreviuen dues transversals que hi toquen: l'**alineació de `.dword` a RARS** (`L2.qmd:156-166`, amb l'avís que el bolcat comparatiu MARS/RARS de `:164-166` no existeix enlloc més) i el **canvi de criteri de `_start`/`.section`** |
| **`exr-moda` (L3) — l'enunciat no deia què ha de contenir `s3_4_2.md`** | **Executada (2026-09-23).** `L3.qmd:17` llistava `s3_4_2.md` com a lliurament i `:303` obria la secció, però l'enunciat només demanava traduir `moda` i `_start`: **què havia d'anar al `.md` només es deduïa llegint el solucionari**. La frase passa a ser «Traduïu `moda` i `_start` a RV32I, **al fitxer `s3_4_2.s`**. Abans d'escriure cap instrucció, **responeu al fitxer `s3_4_2.md`**:», seguida dels dos punts que ja hi havia (registres segurs i bloc d'activació) | Cap pendent. Els dos punts numerats **ja eren a l'enunciat**: l'únic que faltava era lligar-los al fitxer de lliurament, de manera que no s'hi ha afegit cap requisit nou. Es confirma contra el solucionari, on **Pas 1** (registres segurs) i **Pas 2** (taula del BA amb els offsets) són exactament aquests dos punts. La redacció segueix el patró ja establert a `L4.qmd:323` («Abans d'escriure cap instrucció, responeu al fitxer `s4_3_1.md`:»), de manera que els dos fitxers de laboratori diuen ara el mateix de la mateixa manera |
| **Etiquetes de bucle heterogènies a L3** | **Decisió de l'usuari (2026-09-23): no es toca el codi; es documenta la convenció.** L'entrada les tractava com una desviació del patró dominant `for:`/`fifor:`, però **el numeratge és necessari, no estilístic**: els quatre (`for1:`/`ffor1:`/`for2:`/`ffor2:`) són **al mateix bloc de codi** (`L3.qmd:358-445`, la solució de `s3_4_2.s`), on `moda` té dos bucles consecutius —la inicialització de l'histograma i el recorregut de la cadena—. Renombrar-los a `for:`/`fifor:` hi duplicaria etiquetes i el fragment **no assemblaria**. S'afegeix la regla a `13_contrib.qmd §T2 i T3 → Etiquetes de bucle` | ⚠️ **El patró «dominant» no tenia precedent per a aquest cas**: `L3.qmd` és **l'únic fitxer del corpus amb dos bucles al mateix bloc** (`git grep -lE "^for1:"` → només L3); els 18 `fifor:` i 13 `for:` són tots de blocs amb un sol bucle, on no hi ha res a desambiguar. De passada es fixa una segona cosa que divergia i que ningú no havia mesurat: el prefix de sortida és **`fi-`** (18 `fifor:` + 12 `fibucle:` + 2 `fiwhile:` = 32) contra 4 `fwhile:`; la regla de `13_contrib.qmd:122` ja deia `fiwhile:` i ara ho diu explícitament |
| **`fwhile:` → `fiwhile:` al laboratori** | **Decisió i execució de l'usuari (2026-09-23).** El prefix de sortida de bucle divergia amb un repartiment net —teoria `fiwhile:`, laboratori `fwhile:`— i es resol a favor de la forma majoritària, que és la que fixa `13_contrib.qmd:122`. **8 substitucions**: `L3.qmd` 6 i `L5.qmd` 2 | ⚠️ **No eren 4 sinó 8**: l'entrada comptava les **definicions** d'etiqueta (`L3.qmd:229`, `:543`, `:625`, `L5.qmd:267`) i cada una té el seu **salt** que hi apunta (`beqz t0, fwhile`, `blt t0, zero, fwhile`). Canviar només les definicions hauria deixat quatre salts a una etiqueta inexistent i els fragments no haurien assemblat. De passada es reajusta l'alineació dels comentaris de `L3.qmd:221` i `L5.qmd:263`, que `fiwhile` (dos caràcters més llarg) havia desplaçat una columna respecte de les línies veïnes. Verificat: cap `fwhile` al corpus i cap `@ref` no apuntava a aquestes etiquetes |
| **L3 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L3.qmd` de `CLAUDE.md §Estat dels materials`. Estat que tenia en tancar-se: Fase C executada en tres commits del **2026-09-20** (`f136762`, `c52538a`, `7f0703c`) i, després, **sis correccions puntuals per exercici** (`b6c8124`, `8b9f82d`, `01fff2d`, `afdc884`, `eb3f856`, `6ee1a8a`) —l'ítem amb més activitat posterior dels quinze, tot i que cap d'aquelles no és una passada de revisió—. El registre declarava només **Fase B**, perquè es va escriure el 2026-07-19, dos mesos abans de la Fase C | **Les tres entrades que citaven `L3.qmd` s'han resolt el mateix dia del tancament**, totes tres amb fila pròpia en aquesta taula: `exr-moda` (l'enunciat no deia què contenia `s3_4_2.md`), les **etiquetes de bucle numerades** (documentades com a convenció a `13_contrib.qmd`, el codi no es toca) i **`fwhile:` → `fiwhile:`**. `L3.qmd` **no té cap marcador viu** ni cap entrada específica. Hi aterraran dues escombrades transversals pendents: el **canvi de criteri de `_start`/`.section`** (15 ocurrències de `_start`, 5 `.globl`) i les **cometes rectes → «»** (3 línies) |
| **L4 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat, i amb ell el cas crític de les passades finals.** ⚠️ `3cae913` (2026-07-21) és **l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu literalment «**pre passades finals**»; el registre declarava només **Fase B**. Era l'ítem que va motivar l'entrada «Passades finals pendents» i el motiu pel qual no es podia donar el laboratori per revisat sense mirar-s'hi. En tancar-lo, l'usuari **dona per cobertes aquelles passades** | **La Fase C sí que es va executar**, encara que ni l'assumpte ni el registre ho diguin: el Bloc 4c en va verificar al corpus els ítems crítics A1 i A2 (cap `.space` ni cap `li` amb expressió aritmètica, `_start` primera etiqueta dels tres blocs `.text`) i sis de la secció C (`NB`→$T$, la fórmula harmonitzada amb `@mat[0][0]`, la nota de `t4`, «offset»→«desplaçament», «*breakpoint*»→«punt d'aturada», «secció»→«segment `.data`»). `L4.qmd` **no té cap marcador viu** ni cap entrada específica. Les tres troballes transversals del seu registre (D3 punt d'entrada de RARS, D4 símbols `NF`/`NC`/$T$/*stride* al glossari, D5 etiquetes de bucle) són o segueixen sent entrades d'aquest fitxer; **D5 es va resoldre el mateix dia**. La fila de L4 de la taula de «Passades finals pendents» queda marcada com a tancada |
| **L5 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat.** L'usuari elimina la fila de `L5.qmd` de `CLAUDE.md §Estat dels materials`. ⚠️ **És l'únic dels quinze ítems amb la passada final efectivament feta i declarada per les dues bandes**: l'historial mostra el cicle complet (`a83dc16` «TODO darreres passades» → `b5ca2f4` «**tres passades fetes**», 2026-07-21) i el registre ho confirma amb detall («Fase A, B i C completades» + «**Revisió final en 3 passades: completada**», feta en un xat separat). La Fase B va incloure simulació RV32I amb 100 010 casos de prova per a `descompon` | El **model del que és una passada final surt precisament de L5** (`26_prompts/Lx__revisio_interna__plantilla.md:52`: «contrast ISA oficial, comparació didàctica L4/L5/L6, lingüística dedicada»), i és el que l'entrada «Passades finals pendents» cita com a referència. `L5.qmd` **no té cap marcador viu** ni cap entrada específica; l'únic pendent que hi tocava, `fwhile:` → `fiwhile:` (1 ocurrència), es va executar el mateix dia. Amb aquest tancament, **els sis ítems de la taula de «Passades finals pendents» són tancats** i aquella taula passa a ser registre històric |
| **L6 · Tipografia d'UI de RARS** | **Executada (2026-09-23), just abans de tancar L6.** `L6.qmd` marcava els elements d'interfície de RARS en **negreta** mentre que L4 i L5 usen **cursiva** —harmonitzada a la revisió interna de L5 (2026-07-20)— d'acord amb `13_contrib.qmd §Codi, matemàtiques i cursiva`. **35 substitucions** en 26 línies: 19 `Data Cache Simulator`, 5 `Tools → …`, i `Set size`, `Number of blocks = N`, `Reset`, `Runtime Log`, `Connect to Program`, `Fully Associative`, `Cache` | ⚠️ **No eren 22 sinó 35**: l'entrada n'havia comptat una part. Es va inventariar **totes** les negretes del fitxer i separar-ne les d'UI de les legítimes —títols d'apartat, geometries (`32 blocs de 4 paraules`), conceptes (`cold-start`, `conflicte`, `capacitat`)—, que **no s'han tocat**. Tres casos dubtosos resolts mirant-ne el context i el precedent de L4/L5: `Cache` és el nom d'un panell (`:465`), i `Set size = 4` / `Number of blocks = 64` són camps amb el seu valor (`:767`). Verificat que les 5 seqüències `***…***` del fitxer són les d'anglicismes en negreta cursiva i segueixen intactes |
| **L6 — revisió interna tancada** (decisió de l'usuari, 2026-09-23) | **Tancat, i amb ell la revisió interna de tot el laboratori.** Estat que tenia en tancar-se: el registre declarava «Fase A, B i **C: completades**» i «**Pendent: res propi de L6**», amb les troballes cross-file derivades al `TODO.md`. **Cap passada posterior.** La Fase B va incloure verificació empírica amb **RARS 1.6 headless** contra el codi font del `CacheSimulator`, més simulació Python de la cau | ⚠️ **L'assumpte del seu únic commit enganya**: `ca6c01a` es diu «L6 Fase B» i **conté la Fase C sencera** —toca els quatre fitxers que el registre llista i els seus ítems es verifiquen al corpus—. L'avís es conserva a `CLAUDE.md §Estat dels materials` perquè descriu l'historial i seguirà despistant qui el llegeixi. `L6.qmd` **no té cap marcador viu**; l'única entrada que li era específica, la tipografia d'UI, s'ha executat al mateix commit (fila anterior) |
| **P3 — matís del `mul` mòdul $2^n$** (decisió heretada de la revisió interna d'A1, 2026-07-11; ítem 3 del registre de T4) | **Executada**: el callout `#wrn-mul-modul-2n` és a `A4.qmd:323`, just després de `#tip-sobreeiximent-multiplicacio` i abans de `## Divisió entera`, amb el text exacte que proposava el registre; `S4.qmd:214` l'hi referencia amb `@wrn-mul-modul-2n` | ⚠️ **La cadena de rastre estava trencada pels dos extrems i per això es deixa aquesta fila**: l'entrada P3 d'aquest fitxer es va retirar el 2026-07-12 cedint la propietat del pendent al registre de T4, i el registre es va esborrar el 2026-09-22 (`4bfb43c`). El detall —anàlisi, opcions i text del callout— és a `git show a211bbf:TODO/T4_P_tasques.md §3` |

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
