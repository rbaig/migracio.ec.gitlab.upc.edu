# T3.qmd — Tasques pendents

## Decisions de contingut (calen respostes dels professors)

**`gp` i altres segments al mapa de memòria** (L983): decidir si s'inclou `gp` (*global pointer*) al mapa de memòria o s'esmenta de passada.

**Pseudoinstrucció `lla`** (L1016): decidir si s'inclou `lla` (*load local address*, versió relativa al PC de `la`).

**Terminologia *leaf* / *non-leaf*** (L1049): confirmar si s'eliminen definitivament o es restitueixen com a `wrn-` d'aprofundiment.

**Restricció d'EC a 1 resultat** (L1106): decidir entre (a) mantenir restricció a 1 resultat, (b) ampliar a 2 (`a0`/`a1` com a l'ABI real), o (c) explicar l'ABI real i indicar que a EC s'usa sempre 1. (Posició d'Adrià: ampliar a 2 i explicitar que el segon valor pot ser un codi d'error.)

**Verificació ABI sobre el BA** (L1304): verificar contra la RISC-V Calling Convention / psABI que «les subrutines reserven tot l'espai a l'inici i l'alliberen just abans de retornar».

**Alineació de la pila a EC** (L1322): consens sobre si eliminar `{#imp-ec-alineacio-pila}` (relaxació a múltiples de 4) i exigir múltiples de 16 com a l'ABI real. (Posició de Roger: a favor d'eliminar la relaxació.)

**Callout Godbolt** (L1678): decidir si s'afegeix un `wrn-` d'aprofundiment sobre Compiler Explorer / Godbolt, o es descarta.

## Figures amb retocs manuals pendents (Roger)

- `figures/T3_ba_exemple_light.svg`
- `figures/T3_deps_multi_light.svg`
- `figures/T3_deps_exemple_light.svg`

Un cop retocades, afegir `T3_deps_multi_dark.svg` i `T3_deps_exemple_dark.svg` a `scripts/dark_exclusions.txt` i generar les dark manualment.
