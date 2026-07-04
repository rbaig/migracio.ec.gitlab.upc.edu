Nom d'aquest xat: `EC Bloc E — Ús pedagògic de les referències creuades`

Objectiu d'aquest xat: revisió profunda des de diversos punts de vista
Intensitat: Profunda
Fitxers a revisar:

- Principals: `01_T/T1.qmd`–`01_T/T9.qmd`, `02_PE/PE_T1.qmd`–`PE_T9.qmd`, `03_PS/PS_T1.qmd`–`PS_T9.qmd`, `04_L/L1.qmd`–`L6.qmd`
- Addicionalment: qualsevol que processis

Aspectes a revisar:

- Ús pedagògic de les referències creuades (`@sec-`, `@fig-`, `@tbl-`, `@eq-`, `@nte-`, `@tip-`, `@cau-`, `@imp-`):
    - **Densitat**: ni seccions òrfenes de referències ni paràgrafs saturats.
    - **Direccionalitat**: evitar referències cap endavant a conceptes no introduïts encara, excepte les ja documentades i acceptades (p. ex. `fcsr` → `@nte-zicsr` a T5, vegeu `TODO.md §T5 P8`).
    - **Coherència Tx ↔ PE_Tx ↔ PS_Tx ↔ Lx**: que problemes i laboratori remetin a la secció de teoria pertinent quan calgui.
    - Convencions de `07_contrib.qmd §Referències creuades` (ordre de precisió tema → secció → subsecció → callout → figura → taula → equació; article determinat segons el tipus de referència).
- Correcció tècnica de qualsevol contingut que es toqui de passada (però l'abast principal d'aquest xat és les referències creuades, no una revisió tècnica exhaustiva — aquesta ja s'ha fet tema a tema en xats anteriors).

Context previ rellevant (ja resolt, no cal repassar-ho):

- Slugs `{#sec-}` complets a tots els temes (T1–T9).
- Bloc D (criteri backticks/math/cursiva/numeració d'equacions) ja aplicat a `07_contrib.qmd`.
- Totes les referències creuades trencades detectades pel render (`log.log`) ja reparades; només resten pendents les que depenen de figures encara no creades (`@fig-cd-diagrama`, `@fig-assoc-conjunts-diagrama`, `@fig-ca-diagrama`, `@fig-texe-diagrama`, `@fig-mv-flux-traduccio` — no tocar, consten a `TODO.md`).

Model i effortness:

- Ara estàs en Fable 5 High amb Thinking. Confirma'm **explícitament** si t'està bé aquesta configuració o si vols que et canviï de model, effortness o Thinking, digues-m'ho i para perquè pugui fer el canvi de configuració. Quan l'hagi fet te n'informaré i et demanaré que continuïs a partir d'aquest punt.
- Has d'interrompre l'execució sempre que vulguis que et canviï la configuració.

Canvis:

- Fes els canvis a tots els fitxers que creguis oportú. Al final, ofereix-me tots els fitxers que hagis modificat.

Comença:
0. Explora el repositori.
1. Llegeix `CLAUDE.md`, `07_contrib.qmd` i `TODO.md`.
2. Llegeix els fitxers principals a revisar (per tema: teoria → enunciats → solucions → laboratori, si escau).
3. Demana'm o busca al repositori els fitxers que necessitis.
4. Fes un anàlisi profund de l'ús de referències creuades tema a tema.
5. Genera la llista d'accions a realitzar; guarda-la a fitxer `E_tasques.md` i ofereix-me-la per descarregar.
6. Comença a realitzar les accions que no necessitin la meva aprovació. Fes una llista de les tasques que requereixin decisió meva i, quan hagis acabat la tasca anterior (6.), atura't i presenta'm la llista i les opcions de cada ítem que conté.
