# todo

* directives
    * A on estan especificades?
    * quin tag els posem? `RV32I ABI — `? `RARS — `?
* adreces 0x00000000 o 0x0000 0000 (Roger: amb espai)
* `.globl` xor `.global` ?
* `.section` ?
* validar codi startup.s
* Afegir ISA/ABI a `{.callout-note}`? xor ABI/EC a `{.callout-important}` xor callout addicional per a ABI RV?
* Callouts, títol, substituir `,` per `—` als títols (e.g. `C,` per `C —`)
* Passar de `code` a `$funcio$`: `Mw[] = ...` ` -> $Mw[] = ...$`
* Passar de `code` a text: `rs1` -> rs1
* Aplicació de `RV32 ISA — ` a tots els callouts

## T1

* S1 dir que RISC-V és l'ISA de referència a EC

## T2

* introduir el concepte de directiva. ara està a #cau-directives
* Les directives diem que són de RISC-V, de RARS? d'assemblador en genèric? 

## Markdown

* buscar si hi ha "secció de codi per RV" per substituir l'`asm`

## Quarto

* T3 i T4 import de svg de format d'instruccions, render pdf:
```
ERROR: 
compilation failed- error
Package svg Error: File `svg-5d875942584dea27_svg-tex.pdf' is missing.
scrolling down or clicking another section. In https://quarto.org (on right) it works well.
```

* mermaids en svg (ara estan en png pq sembla que hi ha un bug que hardcoded `height=480` => espais en blanc (i potser retalls -no provat))

* confirmar que el syntax highlighting `.s` és correcte per totes les instros, macros, directives, etc.

### Mostrar el contingut de `laboratori`

* Per poder fer download

* pensar si millor fer codi encastat per poder fer C&P.


### Subtítol

HTML vs. PDF
`_quarto.ml`-> surt a totes les pàgines

subtitle: "Grau en Enginyeria Informàtica <br> Facultat d'informàtica de Barcelona <br> Universitat politècnica de Catalunya"
format:
  pdf:
    header-includes: \AtBeginDocument{\subtitle{Grau en Enginyeria Informàtica (GEI)\linebreak Facultat d'informàtica de Barcelona (FIB)\linebreak  Universitat politècnica de Catalunya (UPC)}\date{\today}}

* colors callouts dark `custom_dark.scss`

### `README.md`

* actualitzar arbre de fitxers


## ICE

### Justificació

