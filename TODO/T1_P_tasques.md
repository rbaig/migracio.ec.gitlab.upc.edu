# T1_P_tasques — Revisió interna (Fable): A1, E1, S1

**Estat: Fase C executada (2026-07-12, Sonnet High, sense Thinking).** Totes les tasques 🔴/🟠/🟡/⚪ d'A1.qmd, E1.qmd, S1.qmd, `12_sigles.qmd` i les tres figures SVG s'han aplicat, incloent-hi les decisions P1–P5. Única excepció deliberada: SVG-6 (etiqueta «Objecte»→«Fitxer objecte» a `T1_flux_compilacio.svg`) es descarta perquè el text no cap al requadre existent sense desbordar-lo.

Data: 2026-07-11
Fitxers principals: `A1.qmd`, `E1.qmd`, `S1.qmd`
Fitxers analitzats addicionalment: `22_figs_originals/T1_flux_compilacio.svg`, `T1_picopi_fases.svg`, `T1_von_neumann.svg`, `12_sigles.qmd`
Fitxers de referència llegits: `CLAUDE.md`, `13_contrib.qmd`, `24_specs/svg.md`, `_quarto.yml`, `_variables.yml`, `15_bibliografia.bib`, `TODO/TODO.md`, `TODO/T1_P_tasques.md` (pre-Fable, 2026-06-25), `A2.qmd`, `A3.qmd`, `A4.qmd`, `E3.qmd` (contrast de convencions)

Verificació numèrica: **totes** les traces de A1 §1.4–1.6 i les 15 solucions de S1 verificades per càlcul independent (Python + comprovació manual). Resultat: **1 error numèric** (A1-1), 2 problemes conceptuals (A1-2, S1-1) i la resta correcta. Codificació `add a0, a0, a1` = `0x00B50533` verificada contra el format R de RV32I ✓. Convenció de signes de `div`/`rem` (truncació cap a zero, residu amb signe del dividend) conforme a l'espec RV32M i C ✓.

Decisions de l'usuari ja preses (Fase A):

- D1. Crear subsecció nova d'hexadecimal a `A1.qmd`. ✓
- D2. Promocionar Ca1 i signe i magnitud del `#wrn-` al cos del text. ✓
- D3. Incloure els tres SVG de T1 a la revisió. ✓

Llegenda de prioritat: 🔴 error tècnic · 🟠 coherència/pedagogia · 🟡 llenguatge/format · ⚪ micro/lint
«Dec.» = requereix decisió de l'usuari (vegeu §Decisions pendents).

---

## `A1.qmd`

| # | Pri | Tipus | Acció |
| :--- | :---: | :--- | :--- |
| A1-1 | 🔴 | Error numèric | `#tip-resta-ca2-mono`, 2n exemple $(-100)-(+45)$: la fila de préstec «`0 0 0 0 0 0 1 0`» és incorrecta. La fila correcta (préstec entrant a cada bit, b7…b0) és «`1 1 0 1 1 1 1 0`». (El 1r exemple, $45-30$, és correcte.) |
| A1-2 | 🔴 | Imprecisió conceptual | `#tip-resta-ca2-mono`, 2n exemple: la conclusió «Dos operands negatius i resultat positiu: sobreeiximent» no lliga amb el que es mostra (una **resta** amb minuend −100 i subtrahend **+45**). Reformular: explicitar que en la suma equivalent $(-100)+(-45)$ tots dos operands són negatius, o donar la regla directa de la resta (sobreeiximent si els signes dels operands difereixen i el resultat té el signe del subtrahend). |
| A1-3 | 🔴 | Referència errònia | §Representació: enter → bits: «el procediment és idèntic al dels naturals (@sec-extensio-zeros)» → la referència correcta és `@sec-representacio-naturals` (divisions successives), no l'extensió de zeros. |
| A1-4 | 🔴 | Terminologia tècnica | §Interfícies en la «Visió del Programador»: «tradueix la suma a l'**opcode** `0x00B50533`» → `0x00B50533` és la **codificació completa de la instrucció** (el camp `opcode` només en són els 7 bits baixos). Substituir per «al codi màquina `0x00B50533`». |
| A1-5 | 🟠 | Contingut nou (D1) | Subsecció nova `### Notació hexadecimal {#sec-notacio-hexadecimal}` al final de §Codificació de nombres naturals (després de §Extensió de zeros): base 16, dígits 0–9/A–F, prefix `0x`, correspondència 1 dígit hex ↔ 1 **quartet** (terme del projecte), conversió binari↔hex per quartets, exemple amb `#tip-`. Afegir-hi referència des dels punts de A1 que usen hex (`0xE2`, `0x00B50533`) si escau. |
| A1-6 | 🟠 | Reestructuració (D2) | Promocionar `#wrn-signe-magnitud` i `#wrn-codificacio-enters-ca1` a subseccions del cos (`### Enters en signe i magnitud {#sec-enters-signe-magnitud}` i `### Enters en complement a 1 (Ca1) {#sec-enters-en-ca1}`) dins §Codificació d'enters, mantenint rang, doble zero i inconvenients; eliminar el contenidor §Altres codificacions si queda buit (regla d'un sol ítem per nivell). Harmonitzar el terme a «signe i magnitud» (no «signe-magnitud»). |
| A1-7 | 🟠 | Contingut nou | Afegir a §Enters en Ca2 la relació Ca2 ↔ natural que S1 usa sistemàticament com a drecera: si $X_{n-1}=1$, $x_s = x_u - 2^n$ (interpretació) i $\text{Ca2}(x) = x + 2^n$ (representació de negatius). Proposta: `#cau-` essencial breu, referenciat des de S1. |
| A1-8 | 🟠 | Generalització | §Enters en excés: presentar primer el concepte general amb excés $K$ arbitrari (coherent amb `13_contrib.qmd §T1 i T5`) i, tot seguit, fixar $K = 2^{n-1}-1$ com l'elecció habitual (la dels exercicis i la de l'exponent IEEE 754, T5). |
| A1-9 | 🟠 | DRY | Les quatre etapes del *toolchain* es descriuen **dues vegades** (§El flux de generació i §Les quatre etapes del GCC) amb solapament substancial. **Dec. P1** (vegeu opcions). |
| A1-10 | 🟠 | Sigles/DRY | CPU expandida tres cops (§Nivells d'abstracció, `#wrn-picopi`, §Components de Von Neumann). Mantenir la definició de §Nivells d'abstracció; a `#wrn-picopi` «la Unitat Central de Processament (CPU)» → «la CPU»; a §Components mantenir el nom català sense reexpansió anglesa. |
| A1-11 | 🟠 | Terminologia | §Components de Von Neumann: «Sistema d'entrada/sortida (**I/O**)» → «(**E/S**)» (sigla del projecte, ja usada al caption de la figura). |
| A1-12 | 🟡 | Format de sigla | §Cicle d'instrucció: «**Program Counter** o **PC**» → «***Program Counter*** (**PC**)» (anglicisme en cursiva + sigla entre parèntesis). |
| A1-13 | 🟡 | Apostrofació | §La dependència de l'entorn: «no **la estableix** el llenguatge» → «no l'estableix». |
| A1-14 | 🟡 | Apostrofació | §Llenguatges interpretats: «es **interpreten**» → «s'**interpreten**». |
| A1-15 | 🟡 | Lèxic | «corre» per a programes (×3: §Interfícies en execució, §Per què és important…, §Llenguatges interpretats) → «s'executa» / «està en execució». |
| A1-16 | 🟡 | Redacció | §Interfícies: reescriure la frase «En un **entorn allotjat (*hosted*)** amb **SO**, el cas *full-stack*, que és el més habitual, per exemple, el de Programació I (PRO1), n'hi ha tres:». Proposta: «En un **entorn allotjat** (***hosted***) amb **SO** —el cas més habitual, per exemple el de Programació I (PRO1)—, n'hi ha tres:», valorant si *full-stack* aporta res o s'elimina. |
| A1-17 | 🟡 | Redacció | §Capes i interfícies (1a frase): gerundi «dissenyar qualsevol sistema operatiu (SO) o programa modern **interactuant** directament» → «…que interactuï directament» (o «si s'interactua directament»). |
| A1-18 | 🟡 | Redacció | §Host vs. target: «un PC de la facultat o **d'**un portàtil» → «o un portàtil». |
| A1-19 | 🟡 | Precisió | §Per què C i no C++: «el polimorfisme o **el manteniment d'objectes**» → terme poc clar; proposta: «la gestió automàtica d'objectes (constructors i destructors)». |
| A1-20 | 🟡 | Majúscules | Minúscula inicial en sintagmes catalans a mig text: «Codi Objecte» → «codi objecte»; «L'Enllaçador» → «l'enllaçador»; «L'**Executable final**» → «l'**executable final**»; «**Memòria Principal**» (§programa emmagatzemat) → «memòria principal»; «El **Sistema Operatiu** carrega» → «sistema operatiu»; «la Unitat de Control» (×2, §ISA en execució i §Cicle d'instrucció) → «la unitat de control»; «El paper del Simulador» → «del simulador»; «perifèrics d'Entrada/Sortida» (`#wrn-picopi`) → «d'entrada/sortida»; títol `#wrn-coll`: «El «Coll d'ampolla»» → «El «coll d'ampolla»». |
| A1-21 | 🟡 | Harmonització | *Host*/*Target* amb majúscula i cursiva irregulars (conviuen *Host*, *host*, host, *Target*, target). Harmonitzar: cursiva a la primera aparició, després rodona i sempre en minúscula. |
| A1-22 | 🟡 | Harmonització | Notació de l'arquitectura amfitriona: conviuen «x86_64», «x86-64» i «x86». Unificar a «x86-64» quan es refereix a l'arquitectura del host (E1/S1 ja l'usen); mantenir «x86» només com a nom de família d'ISA (ex. «Intel i AMD amb x86»). |
| A1-23 | 🟡 | Harmonització | Tips de §1.4–1.5: dos comencen amb infinitiu nu («Interpretar $X$…», «Representar $x_s$…») mentre els seus bessons usen «**Pregunta**: …». Unificar el format dins del fitxer (afegir **Pregunta**/**Solució**/**Resposta** on falti o treure les etiquetes pertot; proposta: afegir-les, com els tips de naturals). |
| A1-24 | ⚪ | Lint | Llistes numerades amb doble espai després del marcador («`1.  `», 23 casos) → un sol espai, com a A2/A3 ja revisats. |
| A1-25 | ⚪ | Lint | `#wrn-inversio-limit`: `collapse="true"` → `collapse=true` (com els altres cinc `#wrn-` del fitxer). |
| A1-26 | ⚪ | Coherència menor | Taula `@tbl-impacte-canvi-interficies`: «Modificar codi + Recompilar» → «Modificar el codi i recompilar» (estil de prosa en cel·la). |
| A1-27 | 🟠 | Coherència producte | Títol de `#wrn-picopi`: «Raspberry Pi **Pico 2 W**» però el cos i la figura diuen «Pico 2» (×5) i l'enllaç apunta a la pàgina del Pico 2. **Dec. P2**: quin és el maquinari real previst (2 o 2 W)? Harmonitzar-ho tot al que es decideixi. |
| A1-28 | 🟠 | Matís tècnic (opcional) | §Multiplicació en Ca2: «**no** pot aplicar directament l'algorisme dels naturals» és la simplificació pedagògica estàndard, però estrictament el producte mòdul $2^n$ (part baixa) sí que és correcte independentment del signe (per això `mul` de RV32M no distingeix signes; els que difereixen són `mulh`/`mulhu`, T4). **Dec. P3**: afegir un matís breu (nota o `#wrn-`) o deixar-ho com està fins a T4. |

## `E1.qmd`

| # | Pri | Tipus | Acció |
| :--- | :---: | :--- | :--- |
| E1-1 | 🟠 | Coherència (D1) | Afegir la referència a la nova subsecció d'hexadecimal a la nota de secció: «*Vegeu @sec-codificacio-naturals, @sec-notacio-hexadecimal i @sec-codificacio-enters.*» (els exercicis 4–11 demanen o donen valors en hex). |
| E1-2 | 🟠 | Rigor d'enunciat | `#exr-p1-enters-minim13` (i per simetria `maxim13`): «Expressat en hexadecimal (en complement a 2)» amb 13 bits (no múltiple de 4) és ambigu. Reformular: «Escriu el patró de 13 bits i expressa'l en hexadecimal completant el **patró** amb zeros a l'esquerra fins a 16 bits» (vegeu S1-1 per a la solució). |
| E1-3 | 🟡 | Veu | «**Volem** executar un programa…» (×2, `jerarquia-python` i `jerarquia-c`) → «Es vol executar…» (veu impersonal de la guia). |
| E1-4 | 🟡 | Pronominalització | «calcula **el seu** valor decimal» (×2, `naturals` i `enters-implicit`) → «calcula'n el valor decimal». |
| E1-5 | ⚪ | Redacció | `#exr-p1-naturals` b): «Si el valor no és representable **amb aquells bits**, indica NC» → «amb el nombre de bits indicat, indica-ho amb NC (no codificable)» (primera expansió de NC; després ja es pot usar sol). |

## `S1.qmd`

| # | Pri | Tipus | Acció |
| :--- | :---: | :--- | :--- |
| S1-1 | 🔴 | Imprecisió conceptual | `#sol-p1-enters-minim13` a): «(s'omple amb zeros fins a 16 bits): `0x1000`» és perillós: llegit com a Ca2 de **16 bits**, `0x1000` val $+4096$; l'extensió a 16 bits en Ca2 seria de **signe** (`0xF000`). Reformular: deixar clar que `0x1000` és el **patró de 13 bits** escrit en hex (amb zeros afegits al patró, no al valor) i afegir la remarca que la representació Ca2 de $-4096$ en 16 bits és `0xF000` (extensió de signe, `@sec-extensio-de-signe`). |
| S1-2 | 🟠 | Sigles | `#sol-p1-naturals`: «(de LSB a MSB)» es refereix a **bits** → «de LSb a MSb» segons `12_sigles.qmd` (LSB/MSB són *bytes*). |
| S1-3 | 🟠 | Coherència (A1-7) | Un cop afegit el `#cau-` de la drecera $x_s = x_u - 2^n$ a A1, referenciar-lo a les solucions que la usen (`implicit`, `conversio8`, `ca2-16bits`, comprovacions d'`extensio-signe`). |
| S1-4 | 🟡 | Convenció PE/PS | Eliminar la línia «*Vegeu @sec-operacions-ca2.*» sota §Operacions aritmètiques (les altres dues seccions de S1 no en porten i la convenció del solucionari és integrar les referències al text de cada solució, cosa que ja es fa). |
| S1-5 | ⚪ | Sigles | Si es manté «S&M» (títol i taula de `conversio8`), afegir l'entrada a `12_sigles.qmd` (vegeu SIG-1); altrament, desplegar «signe i magnitud». |
| S1-6 | ⚪ | Lint | Línia en blanc duplicada després de la capçalera de §El cicle de vida (l. 8–9). |

## Figures SVG (`22_figs_originals/`)

| # | Pri | Tipus | Acció |
| :--- | :---: | :--- | :--- |
| SVG-1 | 🔴 | Errada de text | `T1_von_neumann.svg`: etiqueta «Bus **de d'**adreces» → «Bus d'adreces». |
| SVG-2 | 🟡 | Majúscules | `T1_von_neumann.svg`: «Memòria **P**rincipal» → «Memòria principal» (criteri de majúscules del projecte). |
| SVG-3 | 🟠 | Coherència fig.↔text | `T1_picopi_fases.svg`: la figura mostra «Configuració física», «Fase 2: Càrrega» i «Fase 3: Execució/Depuració», però **no hi apareix la «Fase 1: Creació»** que el text sí que llista. **Dec. P4**: afegir un panell/nota per a la Fase 1 (només intervé el host) o mantenir-ho i alinear el text/caption. |
| SVG-4 | 🟡 | Canvas (spec §2) | Cap de les tres figures usa `width="100%"`: `flux_compilacio` té `width="900.5"` (i `viewBox` amb decimals `900.5 × 90.607422`), `von_neumann` té `width="700"` + `height`, `picopi_fases` té `width="680"`. Mínim autònom: `width="100%"`, eliminar `height`, arrodonir el `viewBox` a enters. **Dec. P5**: migració completa a amplades de classe (`flux` → 960 ampla; `von_neumann` → 680 estàndard) ara o diferida amb la resta de migracions de canvas (`TODO.md §SVG`). |
| SVG-5 | ⚪ | Nota (cap acció) | Fonts llegat (`Source Sans Pro` a `picopi`/`von_neumann`) i colors llegat (`#1a5276`, `#4a90b8`, `#e8f4f8`, `#185fa5`, `#e6f1fb`, `#888780`): **coberts pel pipeline** (`norm_font.py` + `gen_dark.py`, entrades ja documentades a `svg.md §13–14`). Si s'executa la migració de P5, aprofitar per normalitzar fonts i paleta al fitxer font i retirar les entrades llegat corresponents de §13. |
| SVG-6 | ⚪ | Harmonització | `T1_flux_compilacio.svg`: etiqueta «Objecte» vs. text «fitxer objecte»/«codi objecte» (A1-20 en fixa la forma); valorar «Objecte (.o)» → «Fitxer objecte (.o)» si hi cap. |

## `12_sigles.qmd`

| # | Pri | Tipus | Acció |
| :--- | :---: | :--- | :--- |
| SIG-1 | 🟠 | Entrades noves (D2) | En promocionar Ca1 i signe i magnitud al cos del text: afegir «**Ca1** Complement a u» (o «a 1», coherent amb «Ca2 Complement a dos») i, si es manté l'abreviatura de S1, «**S&M** Signe i magnitud». |

---

## Decisions pendents de l'usuari

- **P1 (A1-9) — Duplicació del *toolchain***: (a) fusionar §Les quatre etapes del GCC dins §El flux de generació (una sola presentació, amb els noms de les eines `cpp`/`cc1`/`as`/`ld` integrats); (b) mantenir les dues seccions però buidar la segona de repeticions (deixar-hi només noms d'eines i remissió a la primera); (c) deixar-ho com està (dues «visions» deliberades: interfícies vs. eines). *Recomanació: (b), mínimament invasiva i conforme al DRY.*
- **P2 (A1-27) — Pico 2 vs. Pico 2 W**: quin maquinari es farà servir realment? S'harmonitza títol, cos, enllaços i figura al que diguis.
- **P3 (A1-28) — Matís `mul` mòdul $2^n$**: afegir nota/aprofundiment a A1 o deixar-ho per a T4. *Recomanació: deixar-ho per a T4 (A4 ja ho tracta amb `mulh`); com a molt, un punter «es matisa a @sec-… (T4)».*
- **P4 (SVG-3) — Fase 1 a `T1_picopi_fases.svg`**: afegir panell per a la Fase 1 (Creació) o alinear text/caption amb els tres panells actuals. *Recomanació: afegir una franja mínima «Fase 1: Creació» només amb el host, per simetria amb el text.*
- **P5 (SVG-4) — Migració de canvas de les figures T1**: només el mínim (`width="100%"` + `viewBox` enter) ara, o migració completa a amplades de classe (960/680) amb normalització de fonts i paleta. *Recomanació: mínim ara; migració completa quan s'executi el pla de `TODO.md §SVG`.*

## Pla d'execució (Fase C)

1. Autònomes sobre `A1.qmd`: A1-1…A1-5, A1-7, A1-8, A1-10…A1-26 (i A1-6 segons D2 ja decidit).
2. Autònomes sobre `E1.qmd`: E1-1…E1-5.
3. Autònomes sobre `S1.qmd`: S1-1…S1-4, S1-6 (S1-5 depèn de SIG-1).
4. Autònomes sobre SVG: SVG-1, SVG-2, SVG-6 (+ part mínima de SVG-4 si P5 = mínim).
5. `12_sigles.qmd`: SIG-1.
6. Pendents de P1–P5: A1-9, A1-27, A1-28, SVG-3, resta de SVG-4/5.
