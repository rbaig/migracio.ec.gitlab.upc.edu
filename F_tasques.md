# Bloc F — Solucionaris pendents T2 i T3: llista d'accions

## A. Solucions noves a `PS_T2.qmd`

1. **`sol-p3-memoria-endianness`** (secció «Operands en memòria», entre `lw-sw` i `lb-lh`, mirall de l'ordre de `PE_T2.qmd`):
   - a) Definició de *little-endian* (LSB a l'adreça més baixa), amb referència a @sec-endianness.
   - b) `0x12345678` a `0x10010000`: bytes `78 56 34 12`.
   - c) `lb t1, 0(t0)` → llegeix `0x78` (LSB); bit 7 = 0 → `t1 = 0x00000078`.
   - d) Big-endian: el byte a l'adreça base seria el MSB `0x12` → `t1 = 0x00000012`.
2. **`sol-p3-vectors-cerca`** (secció «Vectors», després de `vectors-bucle`): bucle amb sortida anticipada (`beq` → `trobat`), índex a `t2`, cas no trobat → `li t2, -1`. Estil coherent amb `sol-p3-vectors-bucle` (invariants extrets, etiquetes `bucle:`/`fibucle:`).
3. **`sol-p3-vectors-punter-aritm`** (secció «Vectors», després de `vectors-cerca`):
   - a) `p = v + 3` → increment de 3 × 2 bytes = **6 bytes** (`short`); `la t0, v+6` (amb la nota EC/RARS de `la label+offset`).
   - b) Bucle que dobla cada element via punter: `lh`/`sh` amb *stride* de 2 bytes.
4. **`sol-p3-strings-copia`** (secció «Strings», després de `strings-longitud`): còpia byte a byte amb `lb`/`sb`; el `'\0'` es copia abans de sortir del bucle (comprovació després de l'`sb`).

## B. Solucions noves a `PS_T3.qmd`

5. **`sol-p4-logica-rotacio`** (secció «Operacions lògiques i desplaçaments», després de `logica-64bits`):
   - a) Rotació a l'esquerra d'1 posició: `srli`+`slli`+`or` → `b30 … b0 b31`.
   - b) Seguiment del bucle (16 iteracions): `t4 = valor ≫ 16` (lògic), `t2 = valor ≪ 16` (sumes com a duplicacions); `or` final → **rotació de 16 posicions**: `b15 … b0 b31 … b16`.
   - Nota: el guió només demanava l'apartat b), però la solució cobreix a) i b) per completesa del callout (a) és breu).
6. **`sol-p4-memoria-jalr`** (secció «Subrutines: introducció», després de `subrutines-examen`, mirall de l'ordre de `PE_T3.qmd`): seguiment amb taula d'adreces; `la` s'expandeix en `auipc`+`addi`; el primer `jalr` salta a `etiq−4` (el `addi`), el segon salta a si mateix, el tercer surt del fragment. **Resposta: c) 3 vegades.** Es destaca que `jalr` llegeix `rs1` abans d'escriure `rd` (mateix registre).
7. **`sol-p4-compilacio-auipc`** (secció «Compilació, muntatge i càrrega», abans de `compilacio-relocacio`): expansió `auipc`+`addi`, per què calen dues instruccions (immediat de 12 bits insuficient per a offsets de 32 bits), i limitació: offset de 32 bits amb signe → **±2 GiB** respecte al PC. Referències a @nte-la-auipc; sense duplicar el detall de reubicació de `sol-p4-compilacio-relocacio` d).

## C. Correccions i coherència

8. **`PS_T2.qmd` — capçalera duplicada/incorrecta**: `sol-p3-memoria-lb-lh` és sota una capçalera «### Constants i immediats» errònia (línia 147); a més, l'ordre de seccions no segueix `PE_T2.qmd`. Es reordena: «Constants i immediats» (`luiaddi`) abans d'«Operands en memòria» (`lw-sw`, `endianness`, `lb-lh`), eliminant la capçalera duplicada.
9. **`PS_T3.qmd` — «±2 GB» → «±2 GiB»** a `sol-p4-compilacio-relocacio` d), per coherència amb els prefixos binaris de T3 (±4 KiB, ±1 MiB).
10. **`PS_criteris.qmd`**: afegir les 7 solucions noves a les taules de T2 i T3 (amb dificultat i temari).
11. **`TODO.md`**: marcar com a resoltes les 7 files de «Solucionaris pendents d'afegir».

## D. Decisions que et corresponen (es presentaran al final)

- **D1**: validar la dificultat assignada a les noves entrades de `PS_criteris.qmd` (proposta: endianness 1, cerca 2, punter-aritm 2, còpia 2; rotació 3, `jalr` 4, `auipc` 2).
- **D2**: confirmar la correcció «±2 GB → ±2 GiB» aplicada a la solució existent (canvi menor, ja aplicat; reversible).
