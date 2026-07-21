# Passada sistemàtica: ordre substantiu–adjectiu en català

## Context

Aquest repositori conté el material d'un curs universitari (Estructura de Computadors, UPC), escrit en català normatiu. Durant una revisió recent s'ha detectat un patró d'error lingüístic repetit: **calcs de l'ordre adjectiu+substantiu**, típics de l'anglès («single precision») o, en alguns casos, del castellà, quan el català normatiu exigeix l'ordre substantiu+adjectiu per als adjectius classificadors.

Exemple ja detectat i quantificat: **«simple precisió»** (calc) hauria de ser **«precisió simple»** (correcte). Recompte actual al repositori:
- Usen la forma correcta («precisió simple»): `13_contrib.qmd` (2, la pròpia guia d'estil), `01_apunts/A2.qmd` (3), `21_riscv/RARS_directives.qmd` (1).
- Usen la forma incorrecta («simple precisió»): `01_apunts/A5.qmd` (18), `04_laboratori/L5.qmd` (8, ja corregides), `02_exercicis/E5.qmd` (7), `03_solucions/S5.qmd` (4), `12_sigles_simbols.qmd` (3).

Però el fenomen és més general que aquest sol terme. Un altre exemple molt freqüent: **«el següent exemple»**, **«el següent codi»** (calc) haurien de ser **«l'exemple següent»**, **«el codi següent»** (correcte).

## Objectiu

Fer una passada sistemàtica per **tot el repositori** que localitzi totes les instàncies d'aquest patró general (no només «simple/doble precisió» ni només «següent») i les corregeixi amb criteri lingüístic, no amb una simple substitució de text.

## La regla lingüística

En català normatiu, els **adjectius classificadors o relacionals** (els que restringeixen o classifiquen el substantiu sense valorar-lo) es col·loquen **darrere** del substantiu. Col·locar-los davant és un calc, típicament de l'anglès (que sí que anteposa l'adjectiu per defecte) o, per a alguns mots, del castellà.

### Casos clars a corregir (adjectiu+substantiu → substantiu+adjectiu)

| Incorrecte (calc) | Correcte |
|---|---|
| simple precisió / doble precisió | precisió simple / precisió doble |
| el següent exemple / codi / apartat / pas | l'exemple / el codi / l'apartat / el pas següent |
| l'anterior exemple / secció | l'exemple anterior / la secció anterior |
| l'esmentat / citat document | el document esmentat / citat |
| l'actual versió | la versió actual |
| el propi... *(atenció: vegeu excepcions)* | — |

Aquesta taula és **il·lustrativa, no exhaustiva**. Cal generalitzar el criteri (adjectiu classificador → darrere del substantiu) a qualsevol adjectiu que hi encaixi, no limitar-se als exemples llistats.

### Casos que NO s'han de tocar (excepcions legítimes)

L'anteposició és normativa o habitual per a:

- **Ordinals**: «el primer exemple», «la segona pregunta», «el tercer pas». No tocar.
- **Quantificadors i indefinits**: «cada», «cap», «algun», «cert» (en sentit de «un cert"), «diversos», **«diferents» en sentit de «diversos/varis»** («diferents autors» = «several authors»), «molts», «pocs», «tots», «ambdós». No tocar.
- **«mateix»**: «el mateix dia» (= idèntic) és correcte anteposat; «el dia mateix» (èmfasi) també és correcte però amb un matís diferent. Deixar-ho tal com estigui si el sentit és clarament el d'identitat/igualtat.
- **«propi»**: «el meu propi cotxe», «la pròpia UPC» (sentit de pertinença/reflexiu). No tocar.
- **«altre»**: sempre anteposat en català («l'altre dia»). No tocar.
- **Adjectius valoratius o emfàtics en ús idiomàtic**: «un bon exemple», «una gran diferència», «un mal moment», «un nou enfocament» (sentit de «un altre», no «recent»). Aquests poden anar davant o darrere segons el matís semàntic; si teniu dubte raonable, no toqueu i llisteu el cas com a ambigu.
- **«simple» en sentit de «mer/només»**: «un simple error tipogràfic» (= a mere typo) és correcte anteposat. Només cal corregir «simple» quan té sentit **classificador** (simple vs. doble, simple vs. compost), no quan té sentit restrictiu/minimitzador.
- Qualsevol altre cas on l'anteposició sigui idiomàtica i estigui documentada com a acceptable a Optimot o al diccionari de l'IEC: no tocar.

**Si teniu cap dubte raonable sobre si un cas concret és un error o una excepció legítima, no el corregiu automàticament: llisteu-lo com a ambigu a l'informe (vegeu Fase 1) perquè jo el decideixi.**

## Abast

Tot el repositori, fitxers `.qmd` i `.md`, incloent-hi (no exhaustiu): `01_apunts/`, `02_exercicis/`, `03_solucions/`, `04_laboratori/`, `05_diapositives/`, `11_riscv.qmd`, `12_sigles_simbols.qmd`, `13_contrib.qmd`, `21_riscv/`, `index.qmd`, `TODO/`.

**No toqueu:**
- El contingut de blocs de codi (` ```...``` `), spans de codi inline (`` `...` ``), ni res dins de blocs YAML/metadades.
- Noms de fitxers, etiquetes (`{#...}`), referències creuades (`@...`), URLs.
- Codi C o assemblador mostrat com a exemple, encara que hi aparegui text en comentaris — reviseu els comentaris de codi (`# ...`, `// ...`) com a text normal, ja que sovint sí que contenen prosa catalana revisable, però no toqueu res que sigui sintaxi de codi.

## Metodologia (dividida en fases, per seguretat i revisió)

### Fase 1 — Reconeixement i inventari (no editeu encara res)

1. Cerqueu sistemàticament tot el repositori amb els patrons rellevants (adjectius candidats + substantiu, i substantiu + adjectiu ja correcte per contrastar-hi la proporció). Useu `grep`/`rg` amb els termes de la taula anterior com a punt de partida, però amplieu la cerca a qualsevol altre adjectiu classificador que trobeu anteposat de manera sospitosa mentre llegiu el text.
2. Per a cada instància trobada, classifiqueu-la en tres categories:
   - **[FIX]** — error clar, correcció inequívoca segons la regla.
   - **[EXCEPCIÓ]** — anteposició legítima segons la llista d'excepcions; no tocar.
   - **[AMBIGU]** — dubte raonable; requereix decisió meva.
3. Genereu un fitxer `substantiu_adjectiu__inventari.md` amb:
   - Recompte total per categoria i per fitxer.
   - Llista completa de les instàncies [FIX], amb fitxer, línia i frase completa (abans → després).
   - Llista completa de les instàncies [AMBIGU], amb fitxer, línia, frase completa i una frase explicant el dubte.
   - (Les [EXCEPCIÓ] no cal llistar-les una a una; només el recompte.)
4. **Atureu-vos aquí.** Presenteu-me l'informe. No apliqueu cap canvi encara.

### Fase 2 — Aplicació (només després de la meva confirmació de la Fase 1)

5. Apliqueu directament totes les correccions **[FIX]** confirmades.
6. Per a les **[AMBIGU]**, apliqueu només les que jo hagi resolt explícitament; la resta es queden tal com estan.
7. Verifiqueu que no heu introduït cap desequilibri de blocs Quarto (`:::`) ni trencat cap bloc de codi.
8. Genereu un resum final: nombre de correccions aplicades per fitxer, i llista dels fitxers modificats.

## Control de versions

**No feu `git add`, `git commit` ni `git push` en cap moment.** Deixeu tots els canvis com a modificacions locals sense confirmar al *working tree*; jo revisaré i pujaré els canvis manualment.

## Nota final

Aquest és un fenomen que probablement apareix desenes o centenars de vegades arreu del repositori. Prioritzeu la precisió del criteri per sobre de la velocitat: és preferible deixar un cas dubtós a la llista d'ambigus que corregir malament una excepció legítima.
