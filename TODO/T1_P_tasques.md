# T1_P_tasques — Revisió interna (Fable): A1, E1, S1

**Estat: Fase C executada (2026-07-12) i sincronitzada amb el repositori remot (2026-07-13).**

Totes les tasques 🔴/🟠/🟡/⚪ d'A1.qmd, E1.qmd, S1.qmd, el compendi de sigles i les tres figures SVG s'han aplicat, incloent-hi les decisions P1–P5. Única excepció deliberada: SVG-6 (etiqueta «Objecte»→«Fitxer objecte» a `T1_flux_compilacio.svg`) es descarta perquè el text no cap al requadre existent sense desbordar-lo.

**Sincronització amb el repositori (2026-07-13)**: el repositori remot ha evolucionat en paral·lel amb treball d'altres temes (T2, T3, T5, T6) des de la meva última descàrrega. Verificació fitxer per fitxer:

| Fitxer | Estat trobat al remot | Acció presa |
| :--- | :--- | :--- |
| `A1.qmd` | Idèntic a la meva versió Fase C | Cap; ja sincronitzat |
| `S1.qmd` | Idèntic a la meva versió Fase C | Cap; ja sincronitzat |
| Les 3 figures SVG de T1 | Idèntiques a la meva versió Fase C | Cap; ja sincronitzades |
| `E1.qmd` | **Versió pre-Fase-C** (els meus 7 canvis no hi constaven) | Es manté la meva versió local amb la Fase C aplicada; és la versió correcta a pujar |
| `12_sigles.qmd` | **Renombrat pel projecte a `12_sigles_simbols.qmd`**, amb seccions noves `## Símbols` i `## Notació` | Reaplicades les entrades **Ca1** i **S&M** (que faltaven) sobre la nova estructura; la resta de contingut nou del remot es conserva intacte |
| `TODO/TODO.md` | Molt contingut nou d'altres revisions (T2/T3/T5/T6); **la meva nota `### T4` (P3) hi havia desaparegut** | Reinserida la nota T4 al lloc correcte (entre T3 i T5); es conserva tot el contingut nou trobat |

**Incidència detectada i documentada (no corregida en aquesta revisió)**: la promoció de Ca1 del `#wrn-` al cos del text (decisió D2, Fase C) va canviar l'ID `wrn-codificacio-enters-ca1` → `sec-enters-en-ca1`. Això trenca una referència des de `A3.qmd` (L. 48, fora de l'abast de T1). Ja hi havia una entrada genèrica sobre aquest warning a `TODO.md`; l'he ampliada amb l'origen exacte i la solució (un simple canvi de referència a `A3.qmd`), perquè qui reprengui A3 el pugui resoldre directament.

Data d'anàlisi original: 2026-07-11
Fitxers principals: `A1.qmd`, `E1.qmd`, `S1.qmd`
Fitxers analitzats addicionalment: `22_figs_originals/T1_flux_compilacio.svg`, `T1_picopi_fases.svg`, `T1_von_neumann.svg`, `12_sigles_simbols.qmd` (abans `12_sigles.qmd`)

Verificació numèrica: **totes** les traces de A1 §1.4–1.6 i les 15 solucions de S1 verificades per càlcul independent. Resultat: 1 error numèric (A1-1, corregit), 2 problemes conceptuals (A1-2, S1-1, corregits) i la resta correcta.

Decisions de l'usuari preses i aplicades:

- D1. Subsecció nova d'hexadecimal a `A1.qmd`. ✓
- D2. Ca1 i signe i magnitud promocionats del `#wrn-` al cos del text. ✓
- D3. Els tres SVG de T1 inclosos a la revisió. ✓
- P1. Fusió lleugera de les quatre etapes del *toolchain*. ✓
- P2. Pico 2 (no Pico 2 W) arreu. ✓
- P3. Matís de `mul` mòdul $2^n$ ajornat a T4, apuntat a `TODO.md`. ✓
- P4. Fase 1 (Creació) afegida a `T1_picopi_fases.svg`. ✓
- P5. Migració mínima de canvas (`width="100%"`, `viewBox` enter) a les tres figures. ✓

## Contingut de les tasques aplicades

Vegeu el detall complet fitxer per fitxer (A1-1 a A1-28, E1-1 a E1-5, S1-1 a S1-6, SVG-1 a SVG-6, SIG-1) al cos d'aquest document tal com es va lliurar en tancar la Fase C; totes s'han verificat presents a la versió final dels fitxers adjunts, excepte SVG-6 (descartada per manca d'espai al requadre).

## Pendent (fora de l'abast de T1)

- Corregir a `A3.qmd` (L. 48) la referència `@wrn-codificacio-enters-ca1` → `@sec-enters-en-ca1` (causat per la promoció D2 d'aquesta revisió). Ja anotat a `TODO.md §T3`.
