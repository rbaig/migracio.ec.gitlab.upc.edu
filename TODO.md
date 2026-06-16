# TODO

## Contingut

- no `startup.s`
- retorn 2 paràmetres

### General

- Substituir cometes `"..."` per guillemets `«...»` a tot el projecte.
- Eliminar els `****` sobrants.
- Passar totes les equacions a MathML
    - definir els criteris d'inline

### `index.qmd`

- Eliminar `[Plantilles](laboratori/L0/TODO.s)` si no es fan servir.
- Decidir si `startup.s` es manté als materials (proposta: fora, forçar `li a0, 0` + (syscall `93` Linux | syscall `10`).
- Decidir si s'admeten 2 registres de retorn (`a1`).
- Consolidar noms, versions i estàndards de la taula de referències tècniques (`#imp-llenguatges-de-referencia`): versió ISO de C, versió GCC, Toolchain (entrada duplicada).
- Afegir URL de la còpia local de RARS.
- Gestió d'errades: definir protocol de gestió d'errades detectades post-commit.

### Laboratori

- Decidir si l'estudi previ es lliura com a fitxers separats o integrat al `.qmd`.
    - Plantilles Markdown: posar-ne a tots els Ly.qmd excepte L2.qmd XOR eliminar d'Le.qmd
- Decidir com mostrar el contingut de `laboratori/` per poder fer descàrrega (codi encastat per C&P vs. fitxers descarregables).

### Planificació i estat

- A `CLAUDE.md` → 

## Criteris pendents de documentar a `contrib.qmd`

- **Adreces de memòria**: `0x00000000` o `0x0000 0000` (amb espai cada 4 nibbles)?
- **Directives**: quin títol de callout? `## Directives —` o `## RARS —`?
- **`.globl` vs `.global`**: quin usar als exemples?
- **`.section`**: usar o no? si sí, amb quin criteri?
- **ISA/ABI**: on posar la informació de l'ABI de RV? `{.callout-note}` amb `## RV32I ABI —`? `{.callout-important}` amb criteri EC? callout addicional?
- **Syntax highlighting**: confirmar que `.s` és correcte per a totes les instruccions, macros i directives de RARS.
- **Negretes dins de callouts vs. cos del text**: definir criteri.
- **Noms de registres CSR al cos del text**: amb o sense backtick?
- **Numeració d'equacions**: només les referenciades? totes? les importants?
- **LaTeX math vs. backticks**: contextos on usar cada un (cos del text, títols de secció, títols de callout, cel·les de taula, captions, blocs de codi).
- **`ret` vs. `jalr x0, 0(ra)`**: criteri al retorn de funcions.
- **Codi**: definir si el codi ha d'estar sempre testejat abans de commit.
- **Criteris de codi C**: completar.

## Quarto / Infraestructura

- **Migrar diagrames Mermaid existents a SVG**.

## Referències creuades trencades

Només hi ha:
- @imp-exception-handler
- @fig-gap-processador-memoria
- @fig-cd-diagrama
- @fig-assoc-conjunts-diagrama
- @fig-ca-diagrama
- @fig-texe-diagrama
- @fig-mv-flux-traduccio