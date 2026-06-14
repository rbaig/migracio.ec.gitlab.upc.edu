# TODO

## Contingut

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

- **Error SVG en PDF (T3, T4)**:
  ```
  Package svg Error: File `svg-5d875942584dea27_svg-tex.pdf' is missing.
  ```
- **Subtítol**: el subtítol HTML (`<br>`) vs. PDF (`\linebreak`) no es pot unificar a `_quarto.yml`; cal mantenir la solució actual per `format: pdf: header-includes`.
- **Diagrames Mermaid**: migrar els existents a SVG.
- **Mides SVG recomanades**: definir per a cada context (dins callout, cos del text, columnes).
- **Visualització PDF**: definir format de pàgines (marges, capçaleres, peus de pàgina).
- **Navbar**: definir contingut i aparença de la barra superior web.
- **Sidebar**: revisar aparença (collapse-level, icones).
- **Mode fosc**: definir quins elements cal revisar manualment.
- **Numeració de callouts**: revisar criteris i aparença.
- **Migrar diagrames Mermaid existents a SVG**.
