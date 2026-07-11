# Bloc E — Ús pedagògic de les referències creuades: llista d'accions

Anàlisi de tot el corpus (T1–T9, E1–T9, S1–T9, L1–L6, `index.qmd`, `S_criteris.qmd`).
Les accions **A** (autònomes) s'apliquen en aquest xat; les **D** (decisions) queden pendents de l'usuari.

## Diagnòstic global

- **Teoria (T1–T9)**: densitat i direccionalitat de referències molt bona. Les referències cap endavant són majoritàriament «punters» legítims (es veurà a…), moltes ja documentades (optimitzacions T2↔T4, `fcsr`→`@nte-zicsr`). Problemes puntuals: IDs duplicats, 2 referències amb destinació errònia i 5 referències a callouts `#wrn-` des del cos del text (contravé `07_contrib`).
- **Enunciats (PE)**: E4 té bones referències Nivell 2 a teoria; E1/T2 en tenen 1; E3, E5–E9 **cap**. S'apliquen referències selectives a nivell de secció (patró de E1).
- **Solucionaris (PS)**: S1–S5 amb referències integrades correctes; S6–S8 sense cap referència a teoria (s'hi afegeixen les canòniques: fórmules d'Amdahl, TAM, etc.). **Estructura de capçaleres inconsistent** (nivells `#`/`##`, slugs, YAML) — es normalitza.
- **Laboratori (L1–L6)**: les taules «Lectura prèvia» són excel·lents (model a seguir). Problemes: numeració de fitxers de lliurament desfasada amb col·lisions L1/L2 (decisió), errates tècniques (registre `t7` inexistent, etiquetes amb guionet no vàlides a RARS), slugs `sec-l5-*` a L6.

## A — Accions autònomes (aplicades)

### IDs duplicats (Quarto exigeix IDs únics)

- **A1** `A2.qmd:1030` — la figura dins `#wrn-endianness-regla-pi` duia l'ID `#fig-mc-politiques-resum` (copiat de T7) i el caption «Resum de les polítiques de memòria cau». → ID `#fig-endianness-regla-pi` i caption correcte.
- **A2** `A2.qmd:591` — `#wrn-godbolt` duplicat amb T3:1854. → T2 renomenat a `#wrn-godbolt-pseudo` (vegeu D1).
- **A3** `A2.qmd:452` — `#cau-ec-no-overflow` duplicat amb T4:27 (l'única referència, `@cau-ec-no-overflow` a T4:96, és a la còpia de T4). → T2 renomenat a `#cau-rv32i-ignora-sobreeiximent` (vegeu D1).
- (No-acció) `#nte-programa-esquelet` i `#tbl-requadres-tipus` apareixen dues vegades però dins d'un bloc comentat (T2, pendent `startup.s`) i dins de `content-visible` mutuament excloents (index), respectivament.

### Referències amb destinació errònia

- **A4** `A4.qmd:21` — autoreferència `@sec-suma-resta-i-canvi-de-signe` (la frase és dins d'aquesta mateixa secció). → `@sec-resta-ca2` (T1, on es demostra l'equivalència resta = suma del negat).
- **A5** `A5.qmd:103` (`#cau-exces-comparacio`) — «La codificació en excés (@sec-enters-en-ca2 …)» apuntava a la secció de **Ca2**. → `@sec-enters-en-exces`.
- **A6** `S_criteris.qmd` — `@exr-p3-enters-taules` trencada (l'exercici va migrar a E1 com a `exr-p1-enters-taules`). → fila traslladada a la taula del Tema 1 amb la referència nova.
- **A7** `index.qmd:153,157` — enllaços trencats `#sec-problemes-enunciats` i `#sec-problemes-solucions` (no existeixen al llibre). → apunten a `#sec-tema-introduccio-enunciats` (E1) i `#sec-tema-introduccio-solucions` (S1) (vegeu D7).

### Errates tècniques (correcció de passada)

- **A8** `A4.qmd:52` — «sumador amb propagació de **sobreeiximent** (*carry*)… el sobreeiximent d'entrada/sortida»: *carry* és **arrossegament**, no sobreeiximent. Reescrit.
- **A9** `L6.qmd` (`#sol-tiling`) — el registre `t7` **no existeix** a RV32I (temporals: `t0`–`t6`). Codi i taula de registres reescrits usant `a0`.
- **A10** `L3.qmd` — etiquetes d'assemblador amb guionet (`comp-maj:`, `es-alfa:`, `es-esp:`, `es-altre:`, `comp-esp:`, `ret-imax:`): el guionet no és vàlid en identificadors RARS. → guió baix.
- **A11** `L2.qmd` (`#sol-rars-vista-memoria`) — taula amb files desalineades/incompletes (faltaven cel·les a `cc` bytes 4–7, `dd`, `ee`, `ff`; el byte `+0` d'`ee` és `0xA7`, no `0x16`). Corregida.
- **A12** `index.qmd` (§Avaluació, variant HTML) — «NT: 0.80% de NF», «EL: 0.85% NL», etc. (haurien de ser 80%, 85%…), i `<mi>` fora de `<math>`. Corregit i decimals amb coma (0,20…) a totes dues variants, segons `07_contrib §Puntuació`.
- **A13** `A5.qmd:705` — «l'extensió Zicsr … esdevingui obligatori» → «obligatòria».
- **A14** Ortografia: «son» → «són» (L6, 7 casos) i «accesos» → «accessos» (L6, 2 casos).
- **A15** `E5`/`S5` — «desnormalitzat» → «denormal» (terme canònic de T5); capçalera «Mantissa» → «Fracció» a `#exr-p6-ieee-tipus` (a T5, la mantissa és `1,F`; el camp de 23 bits és la fracció).

### Residus editorials

- **A16** `S7.qmd:7–11` — notes de revisió en primera persona («He detallat…», «he assumit…») davant del títol. Eliminades (el contingut útil ja és dins de les solucions corresponents).
- **A17** `S1.qmd:9` — línia orfe `@exr-p1-jerarquia-python i @exr-p1-jerarquia-c` abans de les solucions. Eliminada.
- **A18** `S3.qmd:720` — `---` final sobrer. Eliminat.
- **A19** `L6.qmd:5` — TODO en text pla **abans del títol** (es renderitzava al llibre). Convertit en comentari HTML.
- **A20** `L2.qmd` — noms de fitxer copiats erròniament: plantilla `s1_1_3.md` → `s1_2_1.md` (i moguda dins del bloc `{#exr-}`), `filename="s1_1_3.c"` → `s1_2_2.c`, `filename="s1_2_1.c"` → `s1_3_1.c`; numeració garbulada a `#sol-vectors-declaracio` («1., 1. i 3.» → «1., 2.»).
- **A21** `L3.qmd:444` — accent greu sobrer després de `@exr-compta-caracter`.

### Estructura del solucionari (PS)

- **A22** Normalització de capçaleres: totes les PS ara comencen amb `# {{< var temaX >}} {#sec-tema-…-solucions}` i seccions `##`:
  - `S2` (era `##` sense slug), `S5` (era `title:` al YAML + `## Coma flotant`), `S6`–`S9` (eren `##` amb slugs `sec-solucions-*`; cap referència entrant, renomenats al patró `sec-tema-…-solucions`).
  - `S4` — afegit el YAML (`number-sections: true`) que faltava.
- **A23** `S5` — `**Enunciat:**` → `**Enunciat**:` (els dos punts mai en negreta, `07_contrib §Puntuació`).

### Referències Nivell 2 (PE/PS → teoria) — nucli del Bloc E

Format: línia «*Vegeu ….*» sota la capçalera de secció (patró de E1 §Operacions aritmètiques); referències a exercici concret només quan la solució és aplicació directa d'un element concret.

- **A24** `E1` — §Cicle de vida → `@sec-cicle-de-vida`; §Codificació → `@sec-codificacio-naturals` i `@sec-codificacio-enters`.
- **A25** `E2` — refs de secció: operands en registre/immediat/memòria, caràcters, format d'instruccions, punters, vectors i strings.
- **A26** `E3` — refs de secció: desplaçaments i lògiques, condicionals i bucles, subrutines (introducció i BA), compilació.
- **A27** `E5` — refs de secció: representació IEEE 754, operacions, no-associativitat.
- **A28** `E6` — refs de secció: rendiment (`@eq-texe2`, `@eq-cpi`), potència (`@eq-potencia-dinamica`, `@eq-potencia-estatica`), Amdahl (`@eq-guany3`, `@eq-amdahl`).
- **A29** `E7` — refs de secció + **afegida la capçalera `## Tipologia de les fallades` que faltava** (els `exr-p7-fallades-*` penjaven d'«Associativitat i multinivell»; S_criteris confirma la secció).
- **A30** `E8` — refs de secció: paginació, TLB, protecció, integració TLB–cau.
- **A31** `E9` — refs de secció: excepcions/interrupcions, crides al sistema, E/S.
- **A32** `S6` — refs a `@eq-texe2`/`@eq-cpi` (rendiment), `@eq-potencia-dinamica`/`@eq-potencia-estatica` i `@eq-guany3`/`@eq-amdahl` on les solucions reescriuen aquestes fórmules.
- **A33** `S7` — refs a `@eq-tam`, `@cau-model-temps`, `@eq-tam-multinivell` i `@sec-tipologia-fallades`.
- **A34** `S8` — refs a `@cau-mv-traduccio`, `@sec-mv-tlb` i `@sec-mv-vipt`.
- **A35** `S9` — refs a `@sec-ei-flux-hardware-accions`, `@sec-ei-rse` i `@nte-ecall-taula-rars`.
- **A36** `E2` (`#nte-p3-remissio-enters`) — remissió simplificada (duplicava enllaç i `@sec-` al mateix destí).

### Altres

- **A37** `L6.qmd` — slugs `{#sec-l5-*}` renomenats a `{#sec-l6-*}` (fitxer de la sessió 6; totes les referències són internes al fitxer).
- **A38** `A1.qmd:113` — reactivada la frase introductòria de `@tbl-impacte-canvi-interficies` (estava comentada amb un TODO); la taula queda introduïda al text.
- **A39** `A6.qmd:47` — eliminat el TODO obsolet sobre numeració d'equacions (criteri ja fixat a `07_contrib §Equacions`; les etiquetes de T6 són canòniques i/o referenciades).
- **A40** `L3`, `L4`, `L6` — afegida la frase introductòria «Cal lliurar…» a §Lliuraments (coherència amb L1/L2).
- **A41** `A3.qmd` — tres capçaleres `##` sense `{#sec-}` (Desplaçaments de bits, Operacions lògiques bit a bit, Comparacions i operacions booleanes): slugs afegits segons el criteri de `CLAUDE.md` (necessaris per referenciar-les des de E3).
- **A42** `13_contrib.qmd` — l'exemple literal «*Vegeu @sec-nom.*» generava un WARN de crossref al render; posat en codi (`` `@sec-nom` ``) i ampliat el format recomanat amb la variant «sota la capçalera de secció» (el patró aplicat a PE).

### Verificació

- Inventari programàtic de tot el corpus: **0 IDs duplicats** reals i **0 referències trencades** fora de les 5 figures pendents documentades a `TODO.md`.
- `quarto render --to html` **net**: només els 5 WARN esperats de les figures pendents.
- Els canvis concurrents de l'usuari durant el xat (harmonització KiB/GiB a T2/T3/T8/E7/E8/S8 i `#cau-prefixos-binaris`) s'han respectat i integrat.

## D — Decisions (resoltes per l'usuari el 2026-07-05; aplicades en aquest mateix xat)

Resolució i acció executada:

- **D1** ✓ Mantingudes les dues còpies del `#cau-` (recordatori legítim). Godbolt: eliminat el callout duplicat de T2 i enriquit el de T3 (`#wrn-godbolt`) amb la menció de les pseudoinstruccions.
- **D2** ✓ Permeses com a punter opcional: actualitzada la fila «Aprofundiment» de la taula de callouts de `13_contrib.qmd` (les 5 referències existents es mantenen).
- **D3** ✓ Renumerats els lliuraments al número de sessió: L2→`s2_*` … L6→`s6_*` (145 ocurrències; col·lisions L1/L2 eliminades; cada prefix apareix ara només al seu fitxer). Actualitzats els exemples de `13_contrib.qmd §Nom dels fitxers de lliurament` (ara `s3_*`, de L3). Nota afegida a `TODO.md §Laboratori` sobre el directori `laboratori/` (encara `L0`–`L5`).
- **D4** ✓ **Totes les alineacions a múltiples de 4**, també el BA: L4 (`s4_2_2.s`: BA 16→12, sense fila de padding; `s4_3_1.s`: BA 16→4) i L5 (`s5_1_2.s` i el `_start` temporal de la comprovació: BA 16→4). Els BA de 16 bytes amb 4 registres desats (L3 `codifica`, L5 `s5_3_1.s`) són exactes i es mantenen. Eliminats els dos TODO de L4 sobre aquesta decisió.
- **D5** ✓ Reformulats `exr-p9-exc-tlb-miss` (E9) i `sol-p9-exc-tlb-miss` (S9) en clau de **fallada de pàgina** (RISC-V, walker per maquinari) i de **TLB gestionat per programari** (estil MIPS) per a l'apartat c), coherents amb `@cau-tlb-miss-excepcio`. Secció de S9 i fila de `S_criteris.qmd` renomenades.
- **D6** ✓ Anotat a `TODO.md` (ítem `startup.s`): E9 `exr-p9-syscall-programa` usa `li a7, 10`; unificar amb 93 quan es decideixi.
- **D7** ✓ `S_criteris.qmd` afegit a `_quarto.yml` com a primer capítol de la part «Solucions» (títol promogut a `#`, seccions a `##`); l'enllaç «Solucions» d'`index.qmd` hi apunta (`#sec-problemes-solucions-criteris`).
- **D8** ✓ Anotat a `TODO.md §Laboratori` (secció L2 «Pseudoinstrucció `la` i `li`» amb cos TODO).
- **D9** ✓ Generat `matvec.s` (RV32IM, versió original sense *tiling*) i inserit a L6 abans de la introducció del *loop tiling*, amb la mateixa disciplina de registres que `s6_5_1.s`.
- **D10** ✓ Sense acció: RARS no defineix `abs`; no hi ha col·lisió.
- **D11** ✓ Criteri de **direccionalitat** documentat a `13_contrib.qmd §Referències creuades` (punter explícit sí, dependència conceptual no), amb la llista dels punters cap endavant acceptats (T1/T2→T3/T4, T2/T3→T9, T2→T8, T5→T9, T6→T7, T8→T9). L'extensió a tot el projecte ja queda coberta per la revisió d'aquest bloc: totes les referències cap endavant del corpus són de tipus punter.

Verificació final (2a fase): inventari programàtic net (0 duplicats reals, 0 referències trencades noves) i `quarto render --to html` net (només els 5 WARN de figures pendents), amb `S_criteris.qmd` ja integrat al llibre.

### Llista original presentada a l'usuari (es conserva com a referència)

- **D1 — Contingut duplicat**: (a) `#cau-ec-no-overflow` (T4) vs. `#cau-rv32i-ignora-sobreeiximent` (T2): text gairebé idèntic; (b) `#wrn-godbolt` (T3) vs. `#wrn-godbolt-pseudo` (T2). Mantenir totes dues còpies (recordatori legítim; ja no col·lideixen) o eliminar-ne una (DRY).
- **D2 — Referències a `#wrn-` des del cos del text** (5 casos: T5:268, T6:349, T7:58, T9:781, T9:787): `07_contrib` diu «mai referenciat al text». Opcions: permetre-les com a punter opcional (actualitzar `07_contrib`) o eliminar-les.
- **D3 — Numeració dels lliuraments de laboratori**: L2→`s1_*`, L3→`s2_*`, L4→`s3_*`, L5→`s4_*`, L6→`s5_*`, amb **col·lisions reals L1/L2** (`s1_2_1.md`, `s1_3_1.md`, `s1_4_1.*`). Renumerar L2–L6 al número de sessió (recomanat) o renumerar L1.
- **D4 — Alineació de pila al laboratori**: L4/L5 usen BA de 16 bytes («alineació ABI») tot citant `@nte-abi-alineacio-pila`, que fixa el criteri EC en múltiples de 4. TODO existent a L4 («Roger: 16»). Decidir 4 o 16 i unificar T3 + `07_contrib` + L4/L5.
- **D5 — `exr-p9-exc-tlb-miss` (PE/S9)**: la premissa «una fallada de TLB genera una excepció» contradiu T9 (`@cau-tlb-miss-excepcio`: a RISC-V la resol el *page-table walker*). Reformular l'enunciat (fallada de pàgina, o sistema amb TLB gestionat per programari) o mantenir amb advertiment.
- **D6 — Codi de sortida a E9**: `exr-p9-syscall-programa` demana «sortida amb `li a7, 10`»; la convenció de `07_contrib` és `li a7, 93`. Lligat a la decisió oberta de `startup.s`/`exit` vs `exit2`.
- **D7 — `S_criteris.qmd` fora del llibre**: no consta a `_quarto.yml`. Afegir-lo a l'inici de la part «Solucions» (recomanat; donaria destí natural a l'enllaç «Solucions» d'`index.qmd`) i completar la taula del Tema 1 (ara TODO parcial).
- **D8 — L2 §«Pseudoinstrucció `la` i `li`»**: el cos és «TODO». Redactar contingut o eliminar la secció.
- **D9 — L6 `exr-tiling`**: el text demana carregar `matvec.s` (versió original) però només existeix `matvec.c`. Afegir la traducció o reformular.
- **D10 — L5 etiqueta `abs`**: coincideix amb la pseudoinstrucció `abs` de RARS; cal verificar al simulador que s'admet com a etiqueta (si no, renomenar, p. ex. `valabs`).
- **D11 — Criteri de direccionalitat a `07_contrib`**: proposo documentar el criteri observat: les referències cap endavant només són admissibles com a *punter* explícit («s'estudia a…»), mai com a dependència conceptual; llistar les acceptades (T2→T3/T4 optimitzacions, T5→T9 `fcsr`, T6→T7, T8→T9).
