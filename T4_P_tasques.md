# T4, PE_T4, PS_T4 — Llista d'accions de revisió interna

## LLEGENDA
- ✅ Fet
- ⏳ En curs / pendent de confirmació
- ❓ Requereix decisió de l'usuari
- 🔴 Error crític (aritmètic o tècnic)
- 🟡 Error menor o lingüístic
- 🔵 Millora pedagògica o de coherència

---

## 1. ERRORS ARITMÈTICS (🔴)

### 1.1 PS_T4 — `sol-p5-mul-passos`, apartat a) — TAULA COMPLETAMENT ERRÒNIA
✅ **CORREGIT** (Opus High Thinking)

La taula era incorrecta des de la iteració 2. Error sistemàtic: el PS havia llegit el bit 0 del MR post-shift de la iteració actual en lloc del MR pre-shift. Errors en P (iters 2–6), MR[0] (iters 2, 4, 5) i Acció (iters 2, 4, 5). El binari del resultat final (`001100 111000₂`) valia 824, no 760.

**Canvis aplicats:**
- Taula reescrita completament amb convenció explicitada (MR[0] i Acció referits a l'operació executada en arribar a aquell estat; fila inicial amb «—»).
- Nota de convenció afegida al callout.
- Resultat corregit: `001011 111000₂ = 760₁₀`.

---

### 1.2 PS_T4 — `sol-p5-mul-passos`, apartat b) — columnes MR[0]/Acció desfasades
✅ **CORREGIT** (Opus High Thinking)

Les columnes MR[0] i Acció estaven desfasades 1 iteració (iters 2 i 3 intercanviades). El P i el resultat final (216) eren correctes.

**Canvis aplicats:** Columnes corregides; convenció unificada amb l'apartat a).

---

### 1.3 PS_T4 — `sol-p5-div-passos`, apartat a) — valors intermedis de R−D incorrectes
✅ **CORREGIT** (Opus High Thinking)

A les iteracions 1, 2 i 3 el valor de la resta R−D era incorrecte (bit de signe correcte → decisions correctes → resultat final correcte, però els bits intermedis estaven malcalculats).

**Canvis aplicats:**
- Taula reformatada amb nou format net: columna R mostra estat final (ja restaurat), columna R−D mostra el valor intermedi de la resta.
- Els tres valors de R−D corregits: iter 1 `110111 001000`, iter 2 `111011 111000`, iter 3 `111110 010000`.
- Apartat b) reformatat igualment (valors ja eren correctes; s'afegeix el detall complet de cada iteració en lloc del resum «1–6 sempre negatiu»).
- Nota de convenció afegida.

---

## 2. ERRORS TÈCNICS

### 2.1 T4.qmd — Callout `#cau-ec-no-overflow` mancat
✅ **CORREGIT** (Fase A)

Referència `@cau-ec-no-overflow` (T4.qmd, línia 92) apuntava a un callout inexistent.

**Canvi aplicat:** Callout creat a T4.qmd just abans de `### Condicions de sobreeiximent`:
```markdown
::: {#cau-ec-no-overflow .callout-caution}
A **RV32I**, les operacions de suma i resta **ignoren** el sobreeiximent: el resultat és
simplement els 32 bits de menys pes de l'operació, independentment de si és correcte en
el rang dels enters representables.
:::
```

---

### 2.2–2.9 T4.qmd — Altres referències creuades
⏳ **Pendent de verificació al repositori** (no disponibles en aquest xat)

Les referències `@sec-multiplicacio-potencies-2`, `@sec-extensio-m-t2`, `@cau-sra-divisio`, `@imp-ec-sll-acces-vector`, `@sec-riscv`, `@eq-rang-ca2`, `@sec-enters-en-ca2`, `@eq-acces-aleatori-vector`, `@sec-extraccio-invariants` no s'han pogut verificar sense accés als fitxers T1, T2, T3, T5 i 05_riscv.qmd. Tasca per a Claude Code.

---

## 3. ERRORS TIPOGRÀFICS / LINGÜÍSTICS

### 3.1 T4.qmd — Paraula duplicada «la resta la resta»
✅ **CORREGIT** (Fase A)

### 3.2 T4.qmd — «sobreeiximent enters» amb minúscula inicial
✅ **CORREGIT** (Fase A) → «Sobreeiximent en enters»

### 3.3 PE_T4.qmd — «desbordament (*carry*)» → «arrossegament (*carry*)»
✅ **CORREGIT** (Fase A, D2) — 2 ocurrències

### 3.4 PE_T4.qmd — «desbordament (*overflow*)» → «sobreeiximent (*overflow*)»
✅ **CORREGIT** (Fase A, D2) — 2 ocurrències + 3 frases addicionals

### 3.5 T4.qmd — 23 `{#sec-}` dins de callouts eliminats
✅ **CORREGIT** (Fase A, tasca 5.1)

Capçaleres `##` dins de callouts `tip-`, `wrn-`, `cau-`, `imp-`, `nte-` que no es referencien des de fora del callout no han de portar `{#sec-}`.

---

## 4. COHERÈNCIA PEDAGÒGICA

### 4.1 PE_T4.qmd — 12 refs creuades selectives afegides als exercicis
✅ **FET** (Fase A, tasca 4.4)

Format `*Vegeu @sec-nom.*` al final dels blocs `{#exr-}` que tenen conceptes de teoria referenciables.

### 4.2 PE_T4.qmd — Reordenació de seccions (D3)
✅ **FET** (Fase A)

Ordre anterior: Suma/resta → Mul → **Divisió** → Matrius → Acc. seq.
Ordre nou (coherent amb T4.qmd): Suma/resta → Mul → Matrius → Acc. seq. → **Divisió**

### 4.3 PS_T4 — Solucions noves a generar
⏳ **PENDENT** — Proposta de selecció presentada a l'usuari, pendent de confirmació.

Proposta (9 exercicis de 23 pendents):

| # | Exercici | Dificultat | Secció |
|:---:|:---|:---:|:---|
| 1 | `exr-p5-sr-conversio` | 1 | Suma i resta |
| 2 | `exr-p5-sr-overflow-deteccio-natural` | 3 | Suma i resta |
| 3 | `exr-p5-mul-instruccions` | 3 | Multiplicació |
| 4 | `exr-p5-matrius-diagonal` | 3 | Matrius |
| 5 | `exr-p5-seq-bucles` (c–d) | 4 | Accés seqüencial |
| 6 | `exr-p5-seq-mixed` | 3 | Accés seqüencial |
| 7 | `exr-p5-seq-short` | 3 | Accés seqüencial |
| 8 | `exr-p5-div-algorisme` | 1 | Divisió |
| 9 | `exr-p5-div-programa` | 4 | Divisió |

---

## 5. FORMAT / ESTIL

### 5.1 PS_T4 — «sobreeiximent» vs. «desbordament» als títols de callout
✅ **VERIFICAT** — PS_T4 ja usa «sobreeiximent» de manera consistent.

### 5.2 PS_T4 — Convenció de les taules de seguiment
✅ **UNIFICADA** — Multiplicador i divisor ara fan servir la mateixa convenció: cada fila mostra l'estat *final* de la iteració; MR[0]/R[11] i Acció indiquen el que s'ha executat *en aquella iteració*; fila inicial amb «—».

---

## 6. COHERÈNCIA T4 ↔ T3 (punt d'encaix)

### 6.1 `lui` — mode immediat
✅ **VERIFICAT** — T4 no fa referència explícita a `lui` en el context dels modes d'adreçament; consistent amb la classificació de T3.

### 6.2 Numeració de les optimitzacions de bucle
✅ **VERIFICAT** — T4.qmd implementa exactament la numeració establerta a `07_contrib.qmd §T4` (#1 acc. seqüencial, #2 condició al final, #3 elim. variable d'inducció).

---

## FITXERS MODIFICATS

| Fitxer | Estat | Disponible per descarregar |
|:---|:---|:---:|
| `T4.qmd` | ✅ Modificat | ✓ |
| `PE_T4.qmd` | ✅ Modificat | ✓ |
| `PS_T4.qmd` | ⏳ Parcialment modificat (taules corregides; solucions noves pendents) | — |

---

## PENDENTS GLOBALS (fora d'abast d'aquest xat)

- Verificació de refs creuades a T1/T2/T3/T5 (tasca Claude Code).
- `sol-p5-seq-bucles` apartats c i d: inclosos a la proposta de solucions noves (#5).
- Cometes `"..."` → `«...»`: substitució global (tasca global, no específica de T4).
