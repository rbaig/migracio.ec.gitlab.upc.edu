# Revisió externa d'A1–A8: nota per als equips

> **Esborrany del 2026-10-12** (fase 8 de `CLAUDE.md §Pla de treball`), pendent que l'editor el revisi abans d'enviar-lo. Els equips i el calendari els decideix l'editor.

## Abans de començar

- **Partiu de `main` d'avui.** Des del 2026-10-06, quan es va declarar l'abast de la revisió (A1–A8), tots els fitxers han canviat (taula de sota). Una còpia d'abans no serveix de base.
- **Una branca per equip**: `revisio/<grup>-t<N>-t<M>`, creada des de `main` i actualitzada amb `main` periòdicament (`13_contrib.qmd §Convenció de noms de branques`). Al final, una *Merge Request* a `main`. El push directe a `main` és només per a l'editor (`§Push directe a `main``).
- **Les regles són a `13_contrib.qmd`** (el capítol «Contribueix-hi» del llibre), curtes i sense historial. El perquè de cadascuna, i qui la va decidir, és a `24_specs/registre_de_decisions.md`: abans de proposar de canviar una regla, llegiu-ne l'entrada.
- **Abans de cada commit, `make comprova`** (`§Comprovacions per nivells`): mira el que heu canviat i, si cal, renderitza. Els hooks de git opcionals ho fan sols (`make instal·la-hooks`). Cada push d'una branca passa `make comprova-branca` al mirall de GitHub (`§Les branques, al mirall de GitHub`).
- **No editeu a mà el que es genera**: `auto_figs/`, `auto_riscv/`, `auto_termes/` (el glossari de termes, que es genera de `24_specs/termes.toml`), `_book/`, les variants `_dark.svg` de les figures i els SVG dels generadors de model (a) (`make registres`).
- **Una errada del material publicat**: una *issue* amb l'etiqueta `errada` (`§Errades del material publicat`, D-96).

## Convencions noves des del 2026-10-06

Totes són a `13_contrib.qmd`; aquí només hi ha la llista, perquè sapigueu què ha canviat. Entre parèntesis, l'entrada del registre.

- **Llenguatge**: les sigles, sense plural (D-79), amb l'article segons com es llegeixen (D-80), expandides només a la primera aparició del llibre (D-89) i en un format únic, «unitat d'estat sòlid (*solid-state drive*, SSD)», a partir de `[sigles]` de `24_specs/termes.toml`, que `make comprova` atura si no s'hi segueix (D-118); un espai que no es parteix entre el nombre i la unitat o el % (D-87); el lèxic anglès–català, el de `24_specs/termes.toml`, que n'és l'única font: un terme nou s'hi afegeix, amb les seves fonts, i es presenta al text en el mateix commit, i `make comprova` atura una presentació que no coincideixi amb el fitxer (D-88, D-108, D-115); el terme català o l'anglès, segons les fonts lèxiques per ordre de precedència (DIEC, Termcat, Optimot, Softcatalà, Viquipèdia); després de la presentació, sempre el terme català, i l'anglès, sempre en cursiva, també a les taules i a les figures, que `make comprova` també atura a la prosa (D-116); formes que no s'han de fer servir, que `make comprova` atura (D-105, D-106); noms de persona (D-107); adjectius darrere del nom (D-72); «on», en minúscula després d'una fórmula (D-112); «imbricat», «lectura/escriptura», «ròssec», «coma flotant», «farciment», «multinucli» (D-34 a D-38).
- **Codi**: els comentaris del C, amb `//` i línia per línia (D-83); l'operand de memòria, sempre `desplaçament(base)` (D-84); cap etiqueta ni constant `b` o `B` (D-111); les taules de pseudoinstruccions, amb un sol esquema (D-66); els formats d'instrucció, on es presenta cadascun (D-5); Zifencei, fora d'EC (D-77); les convencions d'EC no penalitzen a l'avaluació (D-85).
- **Format**: cap callout dins d'un altre (D-110); el prefix «C — » als títols, només quan el contingut és només de C (D-114); una taula amb `#tbl-` porta peu (D-102); els punters cap endavant permesos (D-70, D-78).
- **Figures**: el nom, pel fitxer que la consumeix (`A<N>_`, D-76); el `<desc>` és el text alternatiu (D-51); les vores entre zones, per dins (D-99); els originals substituïts es conserven a `22_figs_originals/conservats/` (D-68); la paleta, de 17 colors (D-113).

## Estat de cada fitxer

Revisió interna: tancada per a tot A1–A8 el 2026-09-23 (l'editor). Canvis des del 2026-10-06, mesurats el 2026-10-13 sobre `main` (`cb833ad`):

```bash
for n in 1 2 3 4 5 6 7 8; do echo "A$n $(git log --since=2026-10-06 --oneline -- 01_apunts/A$n.qmd | wc -l) $(git diff --shortstat 7ac2fc9 HEAD -- 01_apunts/A$n.qmd)"; done
```

| Fitxer | Revisió externa anterior | Canvis des del 2026-10-06 | Punts oberts que el toquen (`TODO.md`) |
| :--- | :--- | :--- | :--- |
| A1 | — | 19 commits; +151 −133 | Exemples plegables a l'HTML: A1 n'és el pilot (D-90) |
| A2 | — | 42 commits; +478 −459 | Remissions `@lst-` (3) |
| A3 | `!5` (T3), a `main` el 2026-10-01 | 23 commits; +273 −310 | Remissions `@lst-` (3) |
| A4 | `!7` (T4–T6), a `main` el 2026-10-01 | 14 commits; +68 −68 | — |
| A5 | `!7` | 22 commits; +102 −97 | — |
| A6 | `!7` | 18 commits; +60 −60 | La pregunta de productivitat de dos exemples (reunió del 2 de novembre) |
| A7 | — | 21 commits; +234 −238 | — |
| A8 | `!8` (T8), a `main` el 2026-10-06, fins a §8.7 exclosa | 9 commits; +113 −109 | Per al revisor de T8: la condició VIPT de `#sec-mv-vipt`; la branca `tema8` es conserva perquè hi pugui continuar, i li convé incorporar-hi `main` abans |

Afecta tots els fitxers: la revisió completa de la norma de lèxic anglès/català, feta el 2026-10-13 (D-116), ha canviat formes a tot el corpus (entre d'altres, «desbordament» per *overflow*, «taula de salts», «tipus de dades», «enllaçament», «punt de ruptura», «subnormal» i «la memòria cau», sense la forma curta).
