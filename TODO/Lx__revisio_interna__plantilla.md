Nom d'aquest xat: `EC L{N} Revisió interna`

Objectiu d'aquest xat: revisió profunda des de diversos punts de vista

Intensitat: Profunda

Fitxers a revisar:

- Principals: els especificats al "Nom d'aquest xat"
- Addicionalment: qualsevol que processis

**Com obtenir els fitxers:** el repositori és públic a `raw.githubusercontent.com/rbaig/migracio.ec.gitlab.upc.edu/main/...`. Ves-los a buscar tu mateix amb `bash_tool`/`curl` en el moment que et calguin (Fase A, tasques 1-3), no els demanis com a adjunt ni els llegeixis tots per endavant. Excepció: si hi ha canvis locals encara no pujats al repositori, avisa'm i te'ls passaré jo directament.

Aspectes a revisar:

- Correcció tècnica
    - Font de veritat: tots els documents de l'autor "RISC-V International" de `15_bibliografia.bib`
    - Les versions més recents d'altres documents del repositori oficial de "RISC-V International"
    - Molta atenció en la revisió dels càlculs
- Coherència entre Teoria, Problemes enunciats i Problemes solució
- Eficiència pedagògica
    - Ordre de presentació de la matèria autocontingut: presentació lineal de continguts (no emprar cap concepte que no s'hagi introduït encara, dificultat creixent, etc.)
    - Coherència estilística del llenguatge, dels recursos didàctics (ús de callouts, de referències creuades, freqüència dels exemples, ús consistent de termes, etc.)
    - Idoneïtat dels problemes proposats i dels problemes resolts
    - Detecció de llacunes o repeticions
- Català normatiu
    - Evitar anglicismes
    - Ús dels termes especificats a

Model i effortness:

- Configuració predeterminada per fase (vegeu el detall de cada fase més avall):
    - **Fase A** (exploració i comprensió): Fable 5 High amb Thinking.
    - **Fase B** (verificació numèrica dirigida): Fable 5 High amb Thinking.
    - **Fase C** (execució): Sonnet, effort High, sense Thinking.
- Al començament de cada fase, indica'm **explícitament** quina configuració esperes que tingui activa. Ara estàs en Fable 5 High amb Thinking; confirma'm si és la que toca per a la Fase A o si cal que et canviï de model, effortness o Thinking abans de continuar.
- **Regla transversal, vàlida en qualsevol punt del xat:** tan bon punt detectis que la configuració activa no és l'adequada per a la feina que has de fer a continuació (per exemple, en passar de fase, o si el contingut ho justifica), atura't, digues-me quin model/effort/thinking necessites i espera. Quan hagi fet el canvi t'ho confirmaré i et demanaré que continuïs a partir d'aquest punt.

Canvis:

- Fes els canvis a tots els fitxers que creguis oportú. Al final, ofereix-me tots els fitxers que hagis modificat.

Nota: Les revisions internes de temes pendents estan indicades més avall. Si necessites interactuar amb algun d'aquests temes, digues-m'ho i ho resolem.

---

Estat de la Revisió interna Lx

- Fetes Fable:
    - Pendents: x = {2, 3, 4, 6}
    - Fase C feta: 1, 5
    - L5: Fase A/B/C completes (2026-07-20); pendent revisió final en 3 passades (contrast ISA oficial, comparació didàctica L4/L5/L6, lingüística dedicada) en xat separat `EC L5 Revisió final (3 passades)`, Fable 5 High amb Thinking.

---

1. Estàs amb Sonnet Medium sense Thinking. Si vols canvis, digues-ho i atura't.
2. Dones la revisió pedagògica per finalitzada? O vols fer una darrera passada?
3. El mateix per la revisió tècnica.
4. El mateix per la revisió lingüística.
5. Digues si amb Opus o Sonnet 5 ho pots fer totes les revisions pendents, encara que sigui en diverses passades (p. ex. una per revisió tècnica, una per didàctica i una altra per lingüística). I si ho pots fer, digues quin model i effort necessites si vols Thinking activat.

---

## Procediment (dividit en fases per evitar exhauriment de context)

**Motiu de la divisió:** l'anàlisi de conjunt (tasques 0-4) pot consumir molt de context abans d'arribar a poder escriure el fitxer de tasques (tasca 5), especialment en temes amb alta densitat de contingut numèric/verificable (fórmules, traces d'exemples pas a pas, taules de decisió). Dividir en fases crea un punt de control intermedi que preserva el treball fet encara que el xat s'exhaureixi.

### Fase A — Exploració i comprensió

*Configuració esperada: Fable 5 High amb Thinking.*

0. Explora els fitxers que t'he passat.
1. Llegeix `CLAUDE.md`, `13_contrib.qmd` i `24_specs/svg.md`.
2. Llegeix el fitxer principal a revisar (`L{N}.qmd`) i els fitxers dels apunts les seves referències creuades (`Ax.qmd`, amb x ∈ [1, 9]).
3. `raw.githubusercontent.com/rbaig/migracio.ec.gitlab.upc.edu/main/...` al repositori els fitxers que necessitis.
4. Fes un primer mapa de l'estructura i el contingut: identifica seccions, detecta inconsistències evidents de coherència, pedagogia i llenguatge. **En aquesta fase no cal encara verificar exhaustivament cada càlcul** — l'objectiu és tenir el mapa global. Un cop extretes les convencions rellevants de `CLAUDE.md`, `13_contrib.qmd`, no cal rellegir-los sencers a la Fase B: treballa amb el resum ja fet a menys que sorgeixi un dubte concret que ho justifiqui.
5. Atura't. Presenta'm:
   - Un resum breu de l'estructura dels tres fitxers.
   - La llista de seccions que contenen càlculs crítics o traces d'exemples pas a pas que requeriran verificació numèrica profunda a la Fase B (p. ex. fórmules, exemples amb estat evolutiu, taules de rendiment).
   - Qualsevol dubte o fitxer addicional que necessitis abans de continuar.

*(Confirmaré aquest mapa abans de continuar amb la Fase B.)*

**Punt de represa:** si el xat s'exhaurís just després d'aquest punt, el mapa que m'has lliurat en aquest pas és el punt de represa vàlid per a un xat nou — no cal repetir les tasques 0-4. Si això passa, obriré un xat nou i t'hi enganxaré el mapa rebut perquè continuïs directament per la Fase B.

### Fase B — Verificació numèrica dirigida i anàlisi profund

*Configuració esperada: Fable 5 High amb Thinking.*

6. Amb el mapa validat, fes la verificació profunda **només de les seccions amb contingut numèric/verificable identificades a la Fase A** (càlculs, traces, fórmules), més la resta d'aspectes a revisar (correcció tècnica general, coherència, pedagogia, llenguatge) sobre la totalitat dels fitxers.
7. Genera la llista completa d'accions a realitzar; guarda-la al fitxer `L{N}_tasques.md` i ofereix-me-la per descarregar.

### Fase C — Execució

*Configuració esperada: Sonnet, effort High, sense Thinking.*

8. Comença a realitzar les accions que no necessiten la meva aprovació. Fes una llista de les tasques que requereixin decisió meva i, quan hagis acabat la Fase C, atura't i presenta'm la llista i les opcions de cada ítem que conté.

---

## Si el xat s'exhaureix dins la Fase B o C (sense arribar al punt d'aturada previst)

A diferència del punt de represa de la Fase A (pas 5), un exhauriment dins la Fase B (abans de completar `L{N}_tasques.md`) o dins la Fase C no deixa necessàriament un artefacte net i complet. Experiència real: en un cas, el xat es va exhaurir aparentment durant la generació del fitxer de tasques, però en realitat ja s'havia arribat a completar-la i lliurar-la — l'exhauriment va tallar el torn següent, no la tasca en si. Per tant:

1. **Abans de donar per perduda la feina**, comprova si el darrer missatge del xat exhaurit conté ja el fitxer complet ofert per descàrrega — pot ser que la tasca s'hagi acabat igualment.
2. Si no hi ha fitxer complet, **demana'm que cerqui el xat exhaurit** (`conversation_search`/`recent_chats`): encara que no pugui recuperar-ne el text literal complet, sol poder obtenir un resum estructurat del que ja s'havia analitzat o decidit, evitant repetir feina de zero.
3. Si el xat és molt recent (del mateix dia), és possible que encara no aparegui ben indexat a la cerca; en aquest cas, la via més fiable és que hi entris tu directament des de l'ordinador i copiïs manualment el contingut rescatable cap a un xat nou.
4. En qualsevol cas, un cop recuperat el que es pugui, **continua a partir d'aquell punt en un xat nou** amb la configuració de la fase corresponent — no cal repetir les fases ja completades.

---
Mirror públic del repositori: https://github.com/rbaig/migracio.ec.gitlab.upc.edu
Renderització HTML (pot estar desactualitzada): https://loi.ac.upc.edu/ec