---
name: rars
description: Verificació empírica a RARS 1.6, sense interfície, de qualsevol afirmació del llibre sobre el que fa RARS (directives, pseudoinstruccions, alineació, punt d'entrada, assemblatge de diversos fitxers) i dels programes del laboratori. Carrega-la abans d'escriure, de corregir o de retirar una afirmació sobre el comportament de RARS, i abans de donar per bo un bloc d'assemblador del laboratori.
---

# Verificació empírica a RARS

La regla és a `13_contrib.qmd §Verificació empírica a RARS`: una afirmació sobre el que fa RARS es resol executant RARS 1.6, i es comprova pel resultat, no per l'absència d'error. Aquí hi ha el procediment, i el cas que justifica cada hàbit.

## Obtenir el simulador

El `.jar` no és al repositori i no s'hi ha de posar. Es baixa de la *release* que cita `README.md §RARS`, **fora de l'arbre del projecte**, i no es versiona ni es deixa a cap carpeta del projecte. `25_scripts/verifica_laboratoris.py` ja ho fa: el busca a la variable d'entorn `RARS_JAR` o a `~/.cache/ec/rars1_6.jar` i, si no hi és, l'hi baixa i en comprova el sha256 (D-103 del registre de decisions). Per a les proves a mà, fes servir aquest mateix `.jar`; si encara no hi és:

```bash
mkdir -p ~/.cache/ec && cd ~/.cache/ec
curl -sSLO https://github.com/TheThirdOne/rars/releases/download/v1.6/rars1_6.jar
sha256sum rars1_6.jar   # 780f730eb457b1ba609e968accc2c8b77d8f92c3d9dbf30cc7fdb3cfb14e8c24
```

## Executar-lo sense interfície

S'executa **headless**, sense obrir la GUI. Les opcions que fan falta són
poques: `nc` (sense la nota de copyright, per a una sortida neta), `a`
(assembla i no simula), el nom d'un registre (`t0`, `a0`…) per veure'n el
contingut final, i `dump <segment> <format> <fitxer>` per bolcar memòria:

```bash
java -jar rars1_6.jar nc prova.s t0 t1                       # executa i mostra t0 i t1
java -jar rars1_6.jar nc a prova.s dump .text HexText /dev/stdout   # bolca el segment de text
java -jar rars1_6.jar h                                      # la llista completa d'opcions
```

## Pel resultat, no per l'absència d'error

⚠️ **Una afirmació sobre el comportament de RARS no es comprova per l'absència
d'error, sinó per les adreces del bolcat o per l'estat final dels registres.**
A l'experiment de `.section`, **tres
de les formes provades assemblaven sense queixar-se i no feien el que
semblava**: una no commutava de segment (es veu només perquè dues dades
consecutives cauen a `0x10010000` i `0x10010004`, contigües) i dues descartaven
en silenci el codi posterior a la directiva (es veu només perquè el bolcat de
`.text` té una paraula on n'hi hauria d'haver quatre). Cap de les tres no
emetia cap error. Una comprovació que s'hagués aturat a «assembla, doncs va
bé» hauria donat llum verda a la conversió.

## La interfície, per línia d'ordres

**El comportament multifitxer de la interfície es pot verificar per línia
d'ordres** (2026-09-24). Semblava que no: *Assemble all files currently open*
depèn de quina pestanya és activa, i una pestanya no té equivalent al terminal.
El té: **la pestanya activa equival al primer fitxer de la crida**, perquè
l'ordre dels arguments és l'ordre d'assemblatge.

```bash
java -jar rars1_6.jar nc a dump .text HexText t.hex s5_1_2.s s5_1_1.s   # correcte
java -jar rars1_6.jar nc a dump .text HexText t.hex s5_1_1.s s5_1_2.s   # incorrecte
```

Verificat pels dos camins alhora —a mà a la interfície i per línia d'ordres amb
el `.jar`—, amb els blocs de `L5.qmd`: els bolcats coincideixen **paraula per
paraula**, les onze de cada cas (`@nte-rars-ordre-assemblatge`). D'aquí que una
afirmació sobre la GUI **no s'hagi de donar per no verificable**: abans de dir
«això només es pot comprovar obrint RARS», busqueu quin argument de la línia
d'ordres hi correspon. Val per a l'ordre dels fitxers i per a tot el que la GUI
decideix amb un menú o una casella —`sm` n'és l'altre cas (`13_contrib.qmd
§Convencions globals del laboratori`, i el perquè a D-25 del registre de
decisions).

## Quatre hàbits

D'aquí, quatre hàbits:

- **Compareu sempre contra un control**: el mateix programa amb la forma que ja
  se sap bona. Un bolcat sol no diu si li falta res; dos, de seguida.
- **Mesureu el que afirmeu.** Si l'afirmació és sobre on van les dades,
  comproveu adreces; si és sobre si el codi s'executa, comproveu registres o
  compteu instruccions al bolcat.
- **Quan un exemple mínim falla i el codi real no, el sospitós és l'exemple.**
  D'un MWE se'n va concloure que «RARS només accepta un `.eqv` per fitxer», i el
  bloc de vuit `.eqv` d'`L4.qmd:66-73` assembla sense problema: la causa era que
  el segon símbol de l'exemple es deia `B`, que xoca amb el salt incondicional
  `b` (@nte-rars-noms-reservats). Publicar-ho hauria afirmat que L4 no
  assembla. **Abans d'escriure una limitació observada en un exemple propi,
  reproduïu-la amb un fragment real del corpus**: si el fragment real funciona,
  el que heu trobat és una propietat del vostre exemple, no del simulador.
- **Escriviu al registre el programa mínim sencer**, no la conclusió. Qui ho
  llegeixi d'aquí a un any ha de poder tornar-ho a córrer sense reconstruir-lo,
  i la versió del simulador importa: les afirmacions valen per a **RARS 1.6**.

## Els programes del laboratori

`python3 25_scripts/verifica_laboratoris.py --rars <ruta a rars1_6.jar>` extreu els blocs `.s` de `L1.qmd`–`L6.qmd`, els assembla i els executa amb RARS 1.6, i escriu l'informe a `25_scripts/out_verifica_laboratoris/informe.md` (ignorat per git): resultat, comprovacions estàtiques, i el bolcat de `.data` i dels registres finals dels que s'executen. Sense `--rars`, el busca a `RARS_JAR` o a `~/.cache/ec/`, i si no hi és l'hi baixa. Surt amb 1 si un bloc que s'ha d'assemblar o d'executar no ho fa, o si una comprovació estàtica dona un ERROR, i amb 3 si no hi ha Java: `make comprova` el passa quan es toca L1–L6. Per comprovar que un canvi no altera res, compara l'informe d'abans i el de després.
