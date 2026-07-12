# T6-E6-S6 — Revisió interna profunda: llista d'accions

**Fitxers objectiu:** `01_apunts/A6.qmd`, `02_exercicis/E6.qmd`, `03_solucions/S6.qmd` (+ `13_contrib.qmd`, `TODO/TODO.md`, `12_sigles.qmd` segons decisions)
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent

Nota de context: pas combinat E6+S6 (adaptació + revisió pròpia) i revisió
profunda de T6. Tots els càlculs de S6 i dels `#tip-` d'A6 s'han verificat
pas a pas amb Python (aritmètica exacta amb fraccions on escau). El
repositori estava al dia (cap canvi local pendent, confirmat per Roger).

---

## A — Errors tècnics i de normativa (execució directa) ⏳

### A6.qmd

- 🔴⏳ **A1 — §Potència: definició incorrecta de potència.** «La potència ($P$)
  és l'energia dissipada per la circulació de corrents elèctrics» → «és
  l'energia dissipada **per unitat de temps** per la circulació de corrents
  elèctrics» (la potència és una taxa, no una energia; coherent amb
  `@eq-energia`, $E = P \cdot t$).
- 🔴⏳ **A2 — `#tip-comparacio-versions-programa`: typos i veu.** «**Solució
  1**: Càlcul el núm d'instruccions» → «Calculeu el nombre d'instruccions»;
  «**Solució 2**: Calculem dels CPI» → «Calculeu els CPI» (2a persona del
  plural als `#tip-`, convenció del projecte).
- 🔴⏳ **A3 — Article que falta:** «o, fins i tot, a conjunt de programes» →
  «a un conjunt de programes» (§Reducció del nombre de cicles).
- 🔴⏳ **A4 — «Al + infinitiu» causal:** «Al conduir» ×2 → «En conduir»
  (`#wrn-RC`, paràgrafs de càrrega i descàrrega).
- 🔴⏳ **A5 — Cometes rectes → guillemets** (regla de linting): «"rendiment"»
  (l. 15), «"quant de temps"» i «"quant de treball"» (l. 55).
- 🔴⏳ **A6 — Unitats:** «1200 Km/h» i «1000 Km/h» → «km/h»
  (`#tip-rendiment-avio`); «en Joules» → «en joules» (§Potència dinàmica; els
  noms d'unitat van en minúscula, com ja fan «watts» i «farads»).
- 🔴⏳ **A7 — `@eq-guany3`: subíndex inconsistent.** $P_{X}$ ×2 → $P_{x}$
  (la resta de la derivació usa $P_{x}$).
- 🔴⏳ **A8 — «tc» en text pla** al final de `#tip-augment-freq` («La reducció
  de tc només suposarà…») → $t_{clock}$ (o el símbol que resulti de C2).
- 🔴⏳ **A9 — Apòstrofs tipogràfics (’) → rectes (')**: 5 línies (nota al peu
  `[^CPIins]`, `#tip-augment-freq` l. 150, `#wrn-RC` l. 296/298/315); la
  resta del fitxer usa l'apòstrof recte.
- 🔴⏳ **A10 — `#wrn-RC`:** «puja per sobre de cert llindar» → «per sobre
  d'un cert llindar» (simetria amb «baixa d'un cert llindar»).

### E6.qmd

- 🔴⏳ **A11 — «la única millora»** → «l'única millora»
  (`exr-p2-amdahl-limit`).
- 🔴⏳ **A12 — «ràtio» és femení (DIEC2):** «Calcula els ràtios» → «les
  ràtios»; «dels ràtios» → «de les ràtios» (`exr-p2-potencia-evolucio` a i c).
- 🔴⏳ **A13 — Cometes rectes:** «"10 vegades més ràpid"» → «10 vegades més
  ràpid» amb guillemets (`exr-p2-amdahl-limit`).
- 🔴⏳ **A14 — Terminologia obligatòria:** «afegir un multiplicador hardware»
  → «un multiplicador per maquinari» (`exr-p2-rendiment-speedup-mul`).
- 🔴⏳ **A15 — Veu: 2a persona del plural** (convenció fixada al xat T7,
  `T7_P_tasques.md` A8): «Contesta» ×3 → «Contesteu»; «Considera» ×2 →
  «Considereu»; «Calcula» ×4 → «Calculeu»; «Troba» ×2 → «Trobeu»; «Raona» →
  «Raoneu»; «quina tries? Per què?» → «quina trieu? Per què?».

### S6.qmd

- 🔴⏳ **A16 — `#sol-p2-rendiment-coma-flotant`: dada inventada i
  contradictòria.** «Amb FPU, cada subrutina de **200 instruccions** CF es
  substitueix per 1 instrucció CF HW: el nombre d'instruccions CF es redueix
  10 vegades» — les 200 instruccions no són a l'enunciat (pertanyen a
  `exr-p2-rendiment-speedup-mul`) i «200 → 1» equivaldria a una reducció
  ×200, no ×10. Reescriptura: «Amb la unitat de coma flotant, el nombre
  d'instruccions CF executades es redueix 10 vegades (enunciat). Les
  instruccions no-CF no canvien:». Els càlculs posteriors (×10) són
  correctes i no es toquen.
- 🔴⏳ **A17 — `#sol-p2-amdahl-multicomponent`: generalització incompleta.**
  $S = 1/\sum_i (f_i/k_i)$ només és vàlida si $\sum f_i = 1$. →
  $S = 1/\big((1 - \sum_i f_i) + \sum_i f_i/k_i\big)$, amb la nota que en
  aquest exercici les fraccions cobreixen el 100 % del temps i el primer
  terme s'anul·la. El resultat numèric (24/11) no canvia.
- 🔴⏳ **A18 — `#sol-p2-amdahl-limit` c): conclusió errònia.** «Ni amb
  instruccions CF infinitament ràpides **no s'arribaria** a 1,54×» — 1,54×
  és precisament el límit asimptòtic. → «Amb instruccions CF infinitament
  ràpides el guany tendiria a 1,54× sense poder superar-lo.» I substituir la
  frase final («optimitzar la part dominant és sempre més efectiu…», que no
  lliga amb un apartat on la CF és només el 35 %) per la lectura correcta:
  «el guany màxim queda sempre limitat per la fracció de temps no
  millorada».
- 🔴⏳ **A19 — `#sol-p2-rendiment-classes`: «pipeline» no introduït.**
  L'observació final («una implementació simple (sense pipeline optimitzat
  per tipus)…») usa un concepte aliè al temari en aquest punt. Reescriure
  sense el terme (p. ex. «un disseny amb CPI uniforme pot ser competitiu si
  la freqüència de rellotge és prou alta») o eliminar l'observació.
- 🔴⏳ **A20 — `tbl-colwidths` que no suma 100** a la taula de
  `#sol-p2-potencia-evolucio`: `[5,22,12,7,8,8,8,10]` suma 80 (trenca el
  render PDF). → escalar, p. ex. `[6,27,15,9,10,10,10,13]`.
- 🔴⏳ **A21 — Separador de milers:** «**1.350**» → «**1 350**» (taula de
  `#sol-p2-rendiment-distribucio`; criteri: espai, mai punt ni coma).
- 🔴⏳ **A22 — «ràtio» femení:** «El ràtio màxim de freqüència… El ràtio
  màxim de potència» → «La ràtio màxima…» ×2; «dels ràtios» → «de les
  ràtios» (`#sol-p2-potencia-evolucio` b i c).
- 🔴⏳ **A23 — hardware/HW → maquinari:** títols «## Solució: unitat de coma
  flotant hardware» i «## Solució: multiplicador hardware» → «…per
  maquinari»; «multiplicador HW» → «multiplicador per maquinari»;
  «1 instrucció CF HW» → «1 instrucció CF en maquinari»; «el nou
  multiplicador» resta igual.
- 🔴⏳ **A24 — `#sol-p2-rendiment-coma-flotant` a): precisió del «13 % més
  lent».** $S = 0{,}87$ vol dir un 13 % menys de *rendiment*, però un
  14,8 % més de *temps* ($3{,}444/3 = 1{,}148$). → «té un rendiment un 13 %
  inferior (triga un 14,8 % més): no val la pena».

## B — Millores i harmonitzacions menors (execució directa) ⏳

- 🟡⏳ **B1 (T6)** Línia en blanc que falta després de la capçalera
  «#### Reducció del nombre de cicles»; doble espai fora de fórmula a
  `$$…$$␣␣{#eq-n-cicles}`.
- 🟡⏳ **B2 (T6)** Paraules catalanes en math itàlica → `\text{…}` (criteri
  `13_contrib.qmd §Codi, matemàtiques i cursiva`): $Rendiment$ i $Guany$ a
  `@eq-rendiment`/`@eq-guany1` ($\text{Rendiment}_{\text{nou}}$, amb
  «referència» accentuada), $t_{millorat}$ i $t_{no\text{-}millorat}$ a
  `@eq-guany2` i les línies següents.
- 🟡⏳ **B3 (T6)** Unitats dins math: «10 $\mu s$» / «20 $\mu s$» →
  «$10\ \mu\text{s}$» (harmonitza amb S6); «$2\text{GHz}$», «$10\text{s}$»,
  «$6\text{s}$» del `#tip-comparacio-cpua-cpua-millorat` → amb espai
  ($2\ \text{GHz}$…).
- 🟡⏳ **B4 (T6)** Definició d'$\alpha$: «la mitjana de portes que commuten
  globalment» → «la fracció mitjana de portes que commuten en cada cicle».
- 🟡⏳ **B5 (T6)** «material i grandària dels transistors i connectors
  connectats» → «material i mida dels transistors i de les interconnexions
  connectats» («mida», terme del projecte; evita «connectors connectats»).
- 🟡⏳ **B6 (T6)** «(**fan-out**)» → «(*fan-out*)» (anglicisme en cursiva, no
  negreta).
- 🟡⏳ **B7 (T6)** «el disseny **multicore**» (`#wrn-dennard`) → «el disseny
  **multinucli** (*multicore*)» — primera aparició al llibre; A7 ja usa
  «processadors multinucli (*multicore*)».
- 🟡⏳ **B8 (T6)** `#wrn-RC`: expandir NMOS simètricament amb PMOS
  («*n-channel metal–oxide–semiconductor* (NMOS)») i unificar «*pmos*» /
  «*nmos*» → PMOS/NMOS; «(circuit-obert)» → «(circuit obert)».
- 🟡⏳ **B9 (T6)** «encara que sigui a costa d'augmentar el nombre de les més
  ràpides, si la suma és inferior» → «…si la suma total de cicles resultant
  és inferior» (claredat).
- 🟡⏳ **B10 (T6)** «no és segur que hi hagi guanyat» → «no és segur que s'hi
  guanyi» (`#sec-augment-de-la-frequencia…`).
- 🟡⏳ **B11 (T6)** Nota al peu `[^CPIins]`: «els *loads* i *stores*» → «les
  instruccions de lectura (*load*) i d'escriptura (*store*)»; «No obstant,»
  → «No obstant això,»; «referint-nos llavors a la mitjana» → veu
  impersonal («cas en què es parla de la mitjana…»).
- 🟡⏳ **B12 (T6)** Taula de `#tip-comparacio-versions-programa`:
  `style="width: 70%;"` → `style="width: 70%; margin: auto;"` (centrat dins
  el callout, criteri de `13_contrib.qmd §Taules`).
- 🟡⏳ **B13 (PE+PS)** Notació de la teoria per a la potència estàtica:
  fórmula d'`exr-p2-potencia-estatica`
  $P_{\text{estàtica}} = V \times I_{\text{leak}}$ →
  $P_{s} = V_{CC} \cdot I_{fuita}$ (`@eq-potencia-estatica`); «la fuita de
  corrent produeix» → «els corrents de fuita produeixen»; a S6, $I_{leak}$
  ×3 → $I_{fuita}$ (la teoria preval, precedent T8).
- 🟡⏳ **B14 (PE)** `exr-p2-rendiment-coma-flotant`: «El nombre mitjà
  d'instruccions executades per les subrutines de coma flotant és ara 10
  vegades menor» → «El nombre d'instruccions de coma flotant executades és
  ara 10 vegades menor» (amb la nova unitat ja no hi ha subrutines).
- 🟡⏳ **B15 (PE)** Nota de §Potència i consum: retirar `@eq-energia` de la
  llista (cap exercici usa $E = P \cdot t$); queden
  `@eq-potencia-dinamica` i `@eq-potencia-estatica`.
- 🟡⏳ **B16 (PS)** «l'era de l'escalada de freqüència» → «l'era del
  creixement de la freqüència» (harmonitza amb A6 §Potència;
  `#sol-p2-potencia-evolucio`).
- 🟡⏳ **B17 (T6)** Caption de `@fig-amdahl`: reformular la subordinada
  («…comparat amb el programa millorat que mostra un temps reduït…») →
  «…i el programa millorat, amb temps $t_{1}$, on el temps de la part
  optimitzada queda dividit pel guany $s_{x}$.»

## C — Decisions de Roger ⏳

- 🔵⏳ **C1 — Ordre i noms de secció E6/S6 vs. A6.** La teoria fa
  Rendiment → **Amdahl** → Potència; E6 i S6 fan Rendiment → **Potència i
  consum** → Amdahl, i el nom «Potència i consum» no coincideix amb el
  «Potència» d'A6. Opcions: (a) **recomanada** — reordenar E6/S6 al mirall
  de la teoria i renombrar la secció a «Potència» (`exr-p2-rendiment-temps`
  pot restar a §Rendiment: es resol per temps directes, sense la fórmula
  d'Amdahl); (b) reordenar A6 (Potència abans d'Amdahl); (c) deixar-ho.
- 🔵⏳ **C2 — Notació del tema:** les equacions d'A6 usen
  $t_{clock}$/$f_{clock}$/$n_{ins}$, però els tips d'A6 i tot S6 usen
  $t_c$/$f$/$N$ (S6 fins i tot cita `@eq-texe2` amb els símbols canviats).
  Opcions: (a) **recomanada** — mantenir $t_{clock}$/$f_{clock}$/$n_{ins}$
  a les definicions i introduir-hi explícitament les abreviatures
  ($t_c$, $f$, $N$) que després s'usen lliurement; (b) unificar-ho tot a
  $t_c$/$f$/$N$; (c) unificar-ho tot a les formes llargues. En qualsevol
  cas, registrar-ho en una nova subsecció `#### T6` de `13_contrib.qmd`.
- 🔵⏳ **C3 — «càrrega capacitiva» (E6/S6, calc de *capacitive load*) vs.
  «capacitat equivalent» / «capacitància» (A6).** `exr-p2-potencia-basica`
  barreja les dues dins el mateix enunciat («càrrega capacitiva» a l'apartat
  a, «capacitància» al b). Opcions: (a) «capacitància $C$» pertot;
  (b) «capacitat equivalent $C$» pertot. Registrar a `13_contrib.qmd`.
- 🔵⏳ **C4 — Sigles CMOS / FPU / CF.** CMOS s'usa al cos d'E6 i S6 però
  només es defineix dins un `#wrn-` d'A6 i no és a `12_sigles.qmd` (el
  criteri exclou les sigles dels wrn, però l'ús al cos d'E6/S6 la fa
  incloïble); FPU (S6) i CF (E6/S6, força usada) no s'expandeixen mai ni hi
  tenen entrada. Opcions: (a) **recomanada** — expandir a primera aparició
  del cos (E6: «circuits CMOS (*complementary metal–oxide–semiconductor*)»;
  E6 `exr-p2-amdahl-basic`: «instruccions de coma flotant (CF)») + entrades
  CMOS i CF a `12_sigles.qmd`, i substituir «FPU» de S6 per «unitat de coma
  flotant» / «unitat CF»; (b) evitar les sigles del tot a PE/PS.
- 🔵⏳ **C5 — *speedup* vs. «guany».** A6 defineix «guany de rendiment o
  guany (***speedup***)», però E6 (×10) i S6 (×14) usen «*speedup*» en
  cursiva a totes les aparicions (la convenció diu cursiva només a la
  primera). Opcions: (a) **recomanada** — usar «guany» sistemàticament a
  PE/PS, amb «(*speedup*)» només a la primera aparició de cada fitxer;
  (b) mantenir «speedup» però sense cursiva a partir de la segona aparició.
- 🔵⏳ **C6 — Etiquetes de classe d'instruccions en anglès** a les taules
  d'E6/S6 («Store», «Load», «Branch», «Load/Store», «L/S», «Coma flotant»).
  Opcions: (a) mantenir-les com a noms de classe (etiquetes, no prosa),
  potser en cursiva; (b) traduir («Lectura», «Escriptura», «Salt»). Nota:
  les substitucions obligatòries (load/store → lectura/escriptura,
  branch → salt) semblen pensades per a la prosa.
- 🔵⏳ **C7 — Majúscules de lleis i principis (transversal).** «Llei
  d'Amdahl», «Llei de Moore» i «Escalat de Dennard» amb majúscula a
  A6 (parcialment: també hi ha «l'escalat de Dennard» en minúscula al cos),
  S6 (×7) i `13_contrib.qmd`, però A7 escriu sistemàticament «la llei
  d'Amdahl» en minúscula (×3). La normativa IEC prefereix la minúscula
  («llei d'Amdahl»). Opcions: (a) **recomanada** — minúscula al cos del
  text a tot el llibre (A6, S6, 13_contrib; les capçaleres mantenen la
  majúscula inicial de títol); (b) majúscula pertot (retocar A7). Registrar.
- 🔵⏳ **C8 — Títols dels `#tip-` d'A6.** Cap dels 8 tips d'A6 porta títol
  `##`; A5 en porta 12/12 i A7 4/8; la taula de `13_contrib.qmd` indica
  «Títol: Sí» per als Exemples (la regla general permet ometre'l en
  callouts curts). Opcions: (a) afegir títol als 8 (coherència amb A5);
  (b) només als 5 amb càlcul substancial; (c) deixar-ho i tractar-ho amb la
  decisió anàloga oberta dels `#cau-` (`TODO.md §Decisions obertes`).
- 🔵⏳ **C9 — Etiquetes d'equació no referenciades.** `@eq-rendiment`,
  `@eq-guany1`, `@eq-guany2`, `@eq-texe1`, `@eq-texe3` i `@eq-n-cicles` no
  es referencien des d'enlloc del llibre (comprovat als 84 `.qmd`). Criteri:
  etiquetar només les referenciades o canòniques. Opcions: (a) desetiquetar
  els passos intermedis (`eq-guany1`, `eq-guany2`, `eq-n-cicles`) i mantenir
  les canòniques (`eq-rendiment`, `eq-texe1`, `eq-texe3`); (b) mantenir-les
  totes com a fórmules canòniques del tema.
- 🔵⏳ **C10 — Canvas de les figures T6 (i entrada obsoleta de `TODO.md`).**
  Les 5 figures del tema (extretes de PDF, `svg.md §15`) porten `width` fix
  en píxels en lloc de `width="100%"`, amb mides heterogènies:
  `T6_not_cmos` 360×101, `T6_not_1_0` 386×138, `T6_not_0_1` 386×123,
  `T6_amdahl` 220×95, `T6_tc_tc_prima` 284×120 — cap coincideix amb les
  classes 340/680/960 de `svg.md §2`. Això explica versemblantment les
  «alçades diferents; textos solapats al PDF» que apuntava `TODO.md §T6`
  (les versions «`___tracable____`» que s'hi esmenten no existeixen:
  informació obsoleta, confirmat 2026-07-12). Opcions: (a) normalitzar
  `width="100%"` i homogeneïtzar el trio `T6_not_*` (mateixa amplada de
  viewBox); (b) regenerar les cinc com a figures natives de classe
  `estreta`/`estàndard`; (c) només retirar l'entrada obsoleta de `TODO.md`
  i ajornar. En tots els casos, reescriure l'entrada de `TODO.md §T6`.
- 🔵⏳ **C11 — Amplades de figura al `.qmd` inconsistents:** `fig-amdahl` i
  `fig-tc-tc-prima` usen `width="40%"` a HTML i `width="50%"` a PDF; les
  tres `fig-not-*` usen `width="50%"` a HTML i **cap** width a PDF (100 %
  del textwidth). Definir un criteri (probablement lligat a C10) i
  aplicar-lo.
- 🔵⏳ **C12 — `exr-p2-rendiment-speedup-mul`: CPI del disseny original
  implícit.** L'enunciat només dona el CPI del disseny nou; la solució
  assumeix (raonablement, i ho declara) que al disseny original totes les
  instruccions tenen CPI = 3. Opcions: (a) **recomanada** — fer-ho explícit
  a l'enunciat («al disseny original, totes les instruccions tenen un CPI
  mitjà de 3»), pel criteri de bona definició (precedent T8);
  (b) mantenir-ho com a hipòtesi declarada de la solució.

## D — Fora d'abast d'aquest xat (anotar) ⏳

- 🔵⏳ **D1 — E5 també usa la veu singular** («Contesta les preguntes…»):
  mateixa harmonització que A15, per a la propera passada d'E5 (revisió
  pre-Fable) o per a una escombrada global amb Claude Code. Anotar a
  `TODO.md`.
- 🟡⏳ **D2 — A7 escriu la potència dinàmica com $P_d = \alpha \cdot C \cdot
  V^2 \cdot f_{clock}$** (l. 113) mentre A6 usa $V_{CC}^2$:
  micro-harmonització transversal opcional.

## E — Verificacions completades sense incidència ✅

Càlculs verificats pas a pas i correctes (aritmètica exacta):
`sol-p2-rendiment-compiladors` (1,5/0,8/0,25 ms; ×6; ×3,2),
`sol-p2-rendiment-dos-processadors` (312,5/250 µs; 1,25; 1,25·10⁶),
`sol-p2-rendiment-coma-flotant` (0,82N; S = 0,871 i 1,116 — només cal el
retoc de redacció A16/A24), `sol-p2-rendiment-distribucio` (1 350 cicles;
CPI 1,93; S 1,23; CPI 1,69), `sol-p2-rendiment-classes` (2,8/2,0; 28/15),
`sol-p2-rendiment-speedup-mul` (1,995N; 1197/637 ≈ 1,88; 1274/1197 ≈ 1,064
GHz), `sol-p2-rendiment-temps` (193 s/1,036; 39,2 %; 1,18 < 1,25; 200 s/1,05;
43,75 %; 1,17), `sol-p2-potencia-basica` (8 nF; 33,3 nF; 600 W),
`sol-p2-potencia-evolucio` (les 8 càrregues capacitives 10,56/10,25/7,84/
6,12/13,36/12,29/18,31/29,44 nF; els 7 parells de ràtios; màxims r_f = 10 i
r_P = 2,88; mitjanes geomètriques 2,15 i 1,62; 213× i 28,8×),
`sol-p2-potencia-estatica` (98 %/2 %; 62,5 %/37,5 %; 0,303 A; 40,9 A; ×135),
`sol-p2-amdahl-basic` (25/13; 2,5; −1/15 → impossible),
`sol-p2-amdahl-multicomponent` (24/11; 1,33/1,29/1,07),
`sol-p2-amdahl-limit` (18/19 ≈ 94,7 %; 1,50; 1,538),
`sol-p2-amdahl-cpi` (1800/1125 cicles; CPI 3,0/2,5; F_A/F_B = 1,6; S = 2).
Exemples d'A6 verificats: `tip-comparacio-versions-programa` (10/9 cicles;
CPI 2/1,5), `tip-comparacio-cpua-cpub` (1,33), `tip-comparacio-cpua-cpua-millorat`
(4 GHz), `tip-amdahl` (5) i la derivació de $P_d = \alpha C V_{CC}^2 f$
(coherent internament: energia $CV^2$ per cicle complet de càrrega i
descàrrega; el mateix conveni que apliquen E6/S6 amb $\alpha = 1$ declarat).

Coherència estructural: aparellament `#exr-`↔`#sol-` complet (14/14); IDs de
T6 únics a tot el llibre; totes les referències d'E6/S6 cap a A6
(`@sec-rendiment`, `@sec-potencia`, `@sec-amdahl`, `@eq-texe2`, `@eq-cpi`,
`@eq-guany3`, `@eq-amdahl`, `@eq-potencia*`, `@eq-energia`) existeixen; les
referències externes cap a T6 (A7 → `@sec-amdahl`, `@wrn-dennard`,
`@sec-potencia-dinamica`; `index.qmd` → `#sec-tema-rendiment-potencia`)
queden intactes amb totes les accions proposades (cap canvi d'slug ni
d'etiqueta). Els punters cap endavant T6 → T7 (`#sec-tema-mc`,
`@fig-i9-13900k-die`) són els registrats a `13_contrib.qmd §Direccionalitat`.
Cobertura del solucionari: 14/14 (excepcional; la resta de temes en
seleccionen un subconjunt — cap acció, però es fa constar).

---

## Fitxers a modificar (previsió Fase C)

| Fitxer | Accions |
|:---|:---|
| `01_apunts/A6.qmd` | A1–A10, B1–B12, B17 + C1/C2/C5/C7/C8/C9/C11 segons decisió |
| `02_exercicis/E6.qmd` | A11–A15, B13–B15 + C1/C3/C4/C5/C6/C12 segons decisió |
| `03_solucions/S6.qmd` | A16–A24, B13, B16 + C1/C2/C3/C4/C5/C6/C7 segons decisió |
| `13_contrib.qmd` | nova subsecció `#### T6` (C2, C3, C7…) segons decisió |
| `TODO/TODO.md` | reescriure §T6 (C10) + anotar D1 |
| `12_sigles.qmd` | entrades CMOS/CF si C4(a) |
| `22_figs_originals/T6_not_*.svg` | només si C10(a)/(b) |
