# SVG specs — EC

Figures de referència (es generen al pre-render, §17):
- Mapa de memòria: `auto_figs/T3_mapa_memoria__mapa_light.svg`, de `24_specs/mapa.toml`
- Bloc d'activació: `auto_figs/T3_ba_general__BA_light.svg`, de `24_specs/BA.toml`

---

## 1. Convenció fonamental

**Les adreces creixen cap avall** (y creixent = adreça creixent).

La pila creix cap amunt visualment (sp decreix = nou contingut apareix a y menor).
El heap creix cap avall visualment (adreces altes = y major).

### Sistema de coordenades SVG

L'origen `(0,0)` és a la **cantonada superior esquerra**. L'eix Y creix cap **avall**. Això és el comportament estàndard SVG: no hi ha cap inversió.

La relació entre offset de memòria i coordenada y és **directa**:

```
y_element = marge_sup + offset_element × escala
```

Per exemple, amb `escala = 10 px/byte` i `marge_sup = 10`:
- Element a offset `+0`  → `y = 10`
- Element a offset `+10` → `y = 110`
- Element a offset `+12` → `y = 130`

La confusió habitual prové del vocabulari de domini: es diu que la pila "creix cap amunt", però en coordenades SVG això significa que `sp` **decreix** quan es reserva espai (el cim de pila, offset `+0`, té sempre la `y` més petita). La taula de correspondències:

| Concepte de domini | Coordenada SVG |
|:---|:---|
| Adreça baixa / cim de pila / `sp` | `y` petit (a dalt) |
| Adreça alta / fons del BA | `y` gran (a baix) |
| Offset creixent (+0, +4, +8…) | `y` creixent |
| Pila "creix cap amunt" | `y_sp` decreix en reservar espai |

**Regla per a l'edició manual:** augmentar `y` desplaça l'element cap avall (adreça més alta); reduir `y` desplaça cap amunt (adreça més baixa). Offset creixent = `y` creixent. No hi ha inversió.

### Prioritat de coordenades

Les coordenades `y` han de ser, en ordre de preferència:

1. **Múltiples de 10** (prioritat màxima)
2. **Múltiples de 5** (prioritat secundària)

Evitar decimals i valors arbitraris.

---

## 2. Canvas

Totes les figures usen `width="100%"` amb `viewBox` d'**amplada fixa**, garantint coherència visual (pes de línia, mida de text, espaiat) entre figures de la mateixa classe. `H` es calcula sempre a partir del contingut.

```
width="100%"   viewBox="0 0 {W} {H}"
```

| Classe | W | Ús típic |
|:---|:---:|:---|
| `estreta` | **340** | Figures de detall: BA, descomposicions de bits. Dues en `layout="[50,-2,50]"` ocupen un textwidth. |
| `estàndard` | **680** | Valor per defecte: mapes de memòria, diagrames de blocs, taules de caché, gràfics. |
| `ampla` | **960** | Figures panoràmiques: pipelines multi-etapa, diagrames multicore. El PDF les redueix al textwidth. |

**A l'HTML**, la mida no la decideix el `width` de l'SVG sinó el filtre `25_scripts/figures.lua`: cada imatge es mostra a l'amplada del `viewBox` per 1,4 (una figura de 680 px, a 952 px; una de 340, a 476), i la classe `img-fluid` la limita a l'amplada de la columna. Així el text d'11 px de totes les figures surt a la mateixa mida, uns 15 px, sigui quina sigui la classe; abans, una figura amb `width="100%"` s'estirava a tota la columna i una amb l'amplada en px es quedava a la mida natural (`TODO.md`, «Mida de les figures a l'HTML»). Al PDF, la figura va a la mida del `viewBox` (1 px = 0,75 pt), reduïda a l'amplada del text si no hi cap. Decisió de l'usuari (2026-10-06).

**Excepcions:**

- **Registres de bits** (`gen_regs.py`): `W = 2 + total_bits × 22 + 2` px (708 px per a 32 bits). `width="100%"` igual.
- **BA i mapes de memòria** (`gen_BA.py` i `gen_mapa.py`): classe `estreta`, amb marges `sup=inf=10 px`, columna d'etiquetes de 76 px, rectangles a `x_rect=86 px` de `w_rect=244 px` i marge dret de 10 px, igual que el superior i l'inferior. Les piles en fila (`gen_mapa.py`, tipus `piles`) són `estreta` o `estàndard` segons el nombre de columnes, amb columnes de 60 px a totes dues. Fins al 2026-10-07 (fase 7f), les figures de BA i el mapa de memòria eren de 326 px, amb `w_rect=230 px`, i les piles, de 310 i 510 px.
- **Figures estretes generades** (`gen_BA.py`, `gen_mapa.py` i `gen_memoria.py`): `width="{W}" height="{H}"` en px, i no `width="100%"`. A l'HTML, una figura de 326 o 340 px amb `width="100%"` s'estira a tota la columna (937 px, ×2,9) i el text hi surt a uns 31 px; amb l'amplada en px es mostra a la mida natural, i en un visor estret s'encongeix igualment fins a l'amplada de la columna. Al PDF no canvia res: `rsvg-convert` ja en feia servir la mida del `viewBox`. Decisió de l'usuari (2026-10-05, fase 7c, bloc 11). Des del bloc 12 (2026-10-06), la mida a l'HTML la fixa el filtre `figures.lua` per a totes les figures (vegeu més amunt), i l'amplada en px d'aquests dos generadors ja no hi influeix; es manté perquè és innòcua.

---

## 3. Escala i alçades

> **Nota:** Els valors numèrics de coordenades i dimensions de les seccions §3–§11 corresponen a la classe `estreta` (`W=340 px`, `w_rect=244 px`), la de les figures de BA i del mapa de memòria. Les primitives que les dibuixen són a `25_scripts/columna_memoria.py`, que comparteixen `gen_BA.py` i `gen_mapa.py` (§17).

**Factor d'escala de referència: 20 px/byte.**

```
1 byte  =  20 px
4 bytes =  80 px   (registre, p. ex. `ra`, `s0`...)
```

Quan el contingut és gran (vectors llargs, moltes zones), cal reduir l'escala per mantenir la figura en una mida raonable. Factors admesos, en ordre decreixent:

- ×1  = 20 px/byte (defecte; per a BAs petits o figures de referència)
- ×½  = 10 px/byte (recomanat per a la majoria de BAs amb vectors)
- ×¼  =  5 px/byte (per a BAs molt grans)

**Tria de l'escala:** usar la més gran que mantingui la figura llegible i les coordenades en múltiples de 10 (o 5 com a mínim). L'escala s'aplica uniformement a totes les zones d'una mateixa figura.

Exemple: `T3_ba_func` (`v` char×10 + `w` int×10 = 52 bytes) usa ×½ = 10 px/byte:
```
v   (10 bytes) →  100 px   (sub-rect sup 10 px + dash 80 px + sub-rect inf 10 px)
ali ( 2 bytes) →   20 px
w   (40 bytes) →  400 px   (sub-rect sup 40 px + dash 320 px + sub-rect inf 40 px)
H = 10 + 100 + 20 + 400 + 10 = 540 px   ✓
```

---

## 4. Estructura de cada zona

Cada zona es construeix amb **3 sub-rectangles apilats**:

```
┌─────────────────┐  ← sub-rect SUPERIOR (sòlid, stroke complet)
│  (ratlles)      │    h = N bytes × 20 px
├ ─ ─ ─ ─ ─ ─ ─ ┤  ← sub-rect MIG (vores verticals discontínues, sense horitzontal)
│  text centrat   │    h = M bytes × 20 px
├ ─ ─ ─ ─ ─ ─ ─ ┤
│  (ratlles)      │  ← sub-rect INFERIOR (sòlid, stroke complet)
└─────────────────┘    h = P bytes × 20 px
```

**Excepció — zona d'un sol bloc** (p. ex. `ra`, alineació):
- Un sol `<rect>` amb stroke sòlid, ratlles i text centrat.
- **L'alineació**: un sol `<rect>` amb contorn continu `#adb5bd` (el traç de la paleta, §10) i sense ratlles, perquè no conté dades. Els seus bytes són del BA —compten a la mida i al desplaçament de `sp`—, com la zona reservada del mapa, que també té contorn continu. Fins al 2026-10-07 tenia les vores verticals discontínues i cap vora horitzontal, com si fos un buit (decisió de l'usuari, 2026-10-07, a proposta de Claude Code).

### Sub-rect sòlid

```xml
<rect x="{x_rect}" y="{y}" width="{w_rect}" height="{h}"
      fill="{fill}" stroke="{stroke}" stroke-width="1"/>
```

Porta **ratlles indicadores** als costats esquerre i dret (vegeu §6). Valors de `x_rect` i `w_rect`: vegeu §5. A les figures generades, el rectangle porta només el farciment i les vores verticals: les horitzontals, les de dalt i les de baix de cada zona, es dibuixen al final, segons el color de la zona veïna (§7).

### Sub-rect mig (discontíu)

```xml
<rect x="{x_rect}" y="{y}" width="{w_rect}" height="{h}" fill="{fill}" stroke="none"/>
<line x1="{x_rect}"          y1="{y}" x2="{x_rect}"          y2="{y+h}"
      stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>
<line x1="{x_rect+w_rect}"   y1="{y}" x2="{x_rect+w_rect}"   y2="{y+h}"
      stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>
```

El text es col·loca centrat verticalment dins aquest sub-rect (vegeu §8).

**Trams continus d'un byte.** Les vores verticals del sub-rect mig són contínues durant un byte (l'escala, §3) a cada extrem, i discontínues entre mig; si el sub-rect mig fa menys de 3 bytes, són contínues de dalt a baix. Així es veu que el tram elidit continua sense tall el que té a sobre i a sota, i el contingut elidit es distingeix de l'espai lliure, que no és de ningú i és discontinu de dalt a baix. Una línia discontínua, doncs, només vol dir contingut elidit (amb els trams continus) o espai lliure. Val per al mig dels vectors (entre el primer element i el darrer) i de les zones genèriques. Ho fa `vlines_elidides()`, de `25_scripts/columna_memoria.py`. Proposta de l'usuari (2026-10-07).

---

## 5. Columna de rectangles

```
x_rect  = 86 px      (= marge_esq + 10 = 76 + 10)
w_rect  = 244 px     (marge dret de 10 px: W = 86 + 244 + 10 = 340)
```

Els sub-rectangles són adjacents (sense espai entre ells).

---

## 6. Ratlles indicadores de mida

Les ratlles van als sub-rects **sòlids** (superior i inferior), mai al mig, i només als que fan 40 px o més: en un de més petit no hi caben.
S'apliquen als **costats esquerre i dret** del rectangle, cap a l'interior.

```
x_esq_interior = 87   (= x_rect + 1)
x_dret_interior = 329  (= x_rect + w_rect - 1)
L_curta  = 6 px
L_llarga = 12 px
```

### Patró curta·llarga·curta (per a zones múltiples de 4 bytes)

3 ratlles a ¼, ½ i ¾ de l'alçada del sub-rect:

```xml
<!-- Esquerra -->
<line x1="87"  y1="{y+h*0.25}" x2="93"  y2="{y+h*0.25}" stroke="{stroke}" stroke-width="1"/>
<line x1="87"  y1="{y+h*0.50}" x2="99"  y2="{y+h*0.50}" stroke="{stroke}" stroke-width="1"/>
<line x1="87"  y1="{y+h*0.75}" x2="93"  y2="{y+h*0.75}" stroke="{stroke}" stroke-width="1"/>
<!-- Dreta -->
<line x1="329" y1="{y+h*0.25}" x2="323" y2="{y+h*0.25}" stroke="{stroke}" stroke-width="1"/>
<line x1="329" y1="{y+h*0.50}" x2="317" y2="{y+h*0.50}" stroke="{stroke}" stroke-width="1"/>
<line x1="329" y1="{y+h*0.75}" x2="323" y2="{y+h*0.75}" stroke="{stroke}" stroke-width="1"/>
```

### Patró totes curtes (per a zones no múltiples de 4, p. ex. variables locals)

3 ratlles a ¼, ½ i ¾, totes de longitud curta (6 px):

```xml
<line x1="87"  y1="{y+h*0.25}" x2="93"  y2="{y+h*0.25}" stroke="{stroke}" stroke-width="1"/>
<line x1="87"  y1="{y+h*0.50}" x2="93"  y2="{y+h*0.50}" stroke="{stroke}" stroke-width="1"/>
<line x1="87"  y1="{y+h*0.75}" x2="93"  y2="{y+h*0.75}" stroke="{stroke}" stroke-width="1"/>
<!-- Dreta igual -->
```

El patró de ratlles **totes curtes** reforça visualment que la mida de la zona
és heterogènia o no múltiple de 4.

---

## 7. Línies de separació entre zones

Una línia grisa fina a cada frontera entre zones (no entre sub-rects de la mateixa zona). La línia va **només a la columna d'etiquetes**, de `x=76` a `x=86` (10 px):

```xml
<line x1="76" y1="{y_frontera}" x2="86" y2="{y_frontera}"
      stroke="#adb5bd" stroke-width="0.5"/>
```

S'inclou la línia a `y = marge_sup` (inici) i a `y = H - marge_inf` (final).

### Vores horitzontals entre zones

Cada zona amb traç dibuixa les seves vores horitzontals **per dins de la seva àrea**, desplaçades mig gruix (0,5 px). Entre dues zones de color diferent es veuen, doncs, dues línies d'1 px, una de cada color; entre dues del mateix color, una de sola, compartida, a la frontera; i al costat d'una zona sense traç (l'espai lliure), la de la zona amb traç, sencera. L'alineació té traç, `#adb5bd` (§4). Ho fa `vores()`, de `25_scripts/columna_memoria.py`, un cop dibuixades totes les zones.

Fins al 2026-10-07, cada zona era un `<rect>` amb el traç centrat a la vora, i la que es dibuixava després tapava la meitat del traç de l'anterior amb el farciment i, si en tenia, l'altra meitat amb el seu traç: el resultat depenia de l'ordre de dibuix (mitja línia vermella sota la blava entre `.text` i `.data`; la vora inferior del heap, a mig gruix sota l'espai lliure). Decisió de l'usuari (2026-10-07, opció A), a proposta de Claude Code; la que alternava a ratlles els dos colors es va descartar perquè, en aquesta família, una línia discontínua vol dir «elidit» (§4). L'apliquen `gen_BA.py` i `gen_mapa.py`; la resta de figures, `TODO.md`.

---

## 8. Text dins les zones

### Títol (primera línia, bold)

```
font-size:    12 px
font-weight:  bold
text-anchor:  middle
x:            208  (centre de la columna = 86 + 244/2)
y:            y_mig + h_mig/2 - (n_línies-1)×16/2   (centrat vertical)
fill:         color del stroke de la zona
```

### Línies secundàries

```
font-size:    11 px
font-weight:  normal
text-anchor:  middle
x:            208
y:            y_títol + 16×i   (interlineat 16 px)
fill:         color del stroke de la zona
```

---

## 9. Etiquetes d'adreça (columna esquerra)

```
font-size:    11 px   (o 10 px per a etiquetes de rol com «adr. baixes»)
text-anchor:  end
x:            74 px
y:            y_frontera + 3   (alineada amb la vora superior del segment)
fill:         color del stroke del segment corresponent
```

### Format de les adreces

Sense espais i amb vuit dígits, com al text (`13_contrib.qmd §Criteris generals`, «Hexadecimals»), en majúscules:

```
0x00000000 · 0x00400000 · 0x10010000 · 0x10040000 · 0x7FFFEFFC
```

Fins a la fase 7c, aquesta secció deia «espai cada 4 dígits», contra el text; decisió de l'usuari 10 de la fase 7c (2026-10-03), aplicada el 2026-10-05 a les tres figures que en portaven (`T3_mapa_memoria`, `T7_mc_encert` i `T7_mc_fallada`).

### Etiquetes de rol («adr. baixes» / «adr. altes» / «sp →»)

```
«adr. baixes»  font-size=10  fill=#6c757d   y = marge_sup + 3
«sp →»         font-size=11  fill={stroke zona cim}  font-weight=bold  y = marge_sup + 12
«adr. altes»   font-size=10  fill=#6c757d   y = H - marge_inf + 3
```

A les piles en fila (`gen_mapa.py`, tipus `piles`), cada zona de la pila (els BA i la pila ocupada) porta el seu contorn, del seu color i amb les vores de §7, i la part lliure, a dalt, és com l'espai lliure del mapa: vores verticals discontínues i cap vora horitzontal. «sp →» va a l'esquerra de cada pila, a l'altura del cim, i una línia de 2 px del mateix color marca el cim: el color de la zona del cim diu quin BA és actiu (gris sobre la pila ocupada). «adr. baixes» i «adr. altes» hi van en dues línies, a l'esquerra de la primera pila.

### Desplaçaments des de `sp` (BA)

Amb `desplacaments = true` (`gen_BA.py`), cada zona porta a la vora superior el seu desplaçament des de `sp` (`+4`, `+22`…), amb la posició i el color de les etiquetes d'adreça, en monoespaiat. La primera zona no en porta: el seu desplaçament, `+0`, és el de «sp →». Amb els desplaçaments, la figura fa la feina de la taula «Desplaçament des de `sp`», que ja no cal (decisió de l'usuari, 2026-10-07).

---

## 10. Paleta de colors per zona

Paleta unificada per a **totes** les figures SVG del projecte (memòria, BA i flux).

| Zona / tipus | `fill` | `stroke` / text |
|:---|:---|:---|
| Reservada / espai lliure / processos / alineació | `#f8f9fa` | `#adb5bd` / `#6c757d` |
| `.text` / executable | `#f8d7da` | `#842029` |
| `.data` / fitxers font `.c` `.h` / variables locals (BA) | `#cfe2ff` | `#084298` |
| Heap / fitxers objecte `.o` / registres segurs (BA) | `#d1e7dd` | `#0a3622` |
| Pila / biblioteques `lib.a` / `ra` desat (BA) | `#fff3cd` | `#664d03` |
| Dependències de dades — resultat intermedi | — | `#cc0000` |
| Miss (fallada de MC) — etiqueta de resultat | — | `#dc3545` |
| Hit (encert de MC) — etiqueta de resultat   | — | `#198754` |
| Miss (zona de bloc) — fons de cel·la MC/MP  | `#f8d0d3` | `#dc3545` |
| Hit (zona de bloc) — fons de cel·la MC/MP   | `#c8ebd8` | `#198754` |
| Zona o contenidor (la CPU, el maquinari d'un flux) | `#e6f1fb` | `#084298` |
| Graella i vores secundàries | — | `#dee2e6` |
| Pila ocupada abans d'una crida (piles en fila) | `#adb5bd` | `#6c757d` |

Els dos últims colors s'hi van afegir el 2026-10-06 (decisió de l'usuari, a proposta de Claude Code), perquè ja els feien servir diverses figures amb aquest paper: `#e6f1fb`, `T1_von_neumann` i `T8_mv_flux_traduccio`; `#dee2e6`, `T4_matriu_emmagatzematge`, `T4_matriu_offset_ij` i `T7_gap_processador_memoria`. La resta de colors que quedaven fora de la paleta es van migrar el mateix dia (§14). La paleta s'ha de revisar per reduir-ne la quantitat de colors (`TODO.md`).

---

## 11. Fletxes de creixement (heap i pila)

Una línia vertical de 1,5 px i una punta triangular de 8 px (`<polygon>`), del color del traç de la zona, que surten de la zona cap a l'espai lliure; la variant fosca en canvia el color com el de qualsevol altre element (§13). Les dibuixa `fletxa()`, de `25_scripts/columna_memoria.py`.

### Heap (fletxa cap avall, a la dreta)

```
x        = x_rect + w_rect - 22 = 308
y_inici  = y_heap_fi - 15          (dins del heap)
y_fi     = y_heap_fi + 35          (la punta, a l'espai lliure)
stroke   = #0a3622   stroke-width="1.5"
```

### Pila (fletxa cap amunt, a l'esquerra)

```
x        = x_rect + 22 = 108
y_inici  = y_pila + 15             (dins de la pila)
y_fi     = y_pila - 35             (la punta, a l'espai lliure)
stroke   = #664d03   stroke-width="1.5"
```

### Text «creix» rotat

A 8 px de la fletxa, cap enfora de la columna (a la dreta de la del heap, a l'esquerra de la de la pila), centrat a la meitat de la fletxa i **desplaçat 6 px cap a la punta**: centrat a la meitat, la «c» tocava la vora entre la zona i l'espai lliure (decisió de l'usuari, 2026-10-07). Fórmula per a un text centrat al costat d'una línia vertical en `(x_L, y_centre)`:

```
rotate(+90):  <text x=" y_centre" y="-x_L"  transform="rotate(90)"  ...>
rotate(-90):  <text x="-y_centre" y=" x_L"  transform="rotate(-90)" ...>
font-size: 11 px   fill: color de la zona   text-anchor: middle
```

---

## 12. Fonts

Les fonts usades als SVG del projecte han de ser fonts de sistema disponibles sense instal·lació addicional a les plataformes habituals (Linux/Debian, macOS, Windows). Els SVG s'insereixen com a `<img>` i no hereten les fonts carregades pel CSS de Quarto.

Paquet Debian necessari: `fonts-liberation` (`sudo apt install fonts-liberation`).

### Taula de fonts

El bloc següent és la **font de veritat** de la taula de fonts i de les substitucions de migració. L'script `25_scripts/norm_font.py` el llegeix directament d'aquest fitxer en temps d'execució. Per afegir o modificar fonts, editeu només aquest bloc.

```{.python #svg-font-map}
SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'Liberation Mono', 'Courier New', Courier, monospace"

# Ús als SVG:
#   font-family="'Liberation Sans', Arial, Helvetica, sans-serif"   → cos de text, etiquetes
#   font-family="'Liberation Mono', 'Courier New', Courier, monospace" → adreces, instruccions, valors hex

# Mapa de substitució: clau = valor normalitzat (minúscules, espais col·lapsats)
# valor = nova cadena font-family
FONT_MAP = {
    # Proporcionals (llegat: Source Sans Pro, genèrics Inkscape)
    "'source sans pro', sans-serif": SANS,
    "source sans pro, sans-serif":   SANS,
    "'source sans pro'":             "'Liberation Sans'",
    "source sans pro":               "Liberation Sans",
    "'sans'":                        "Liberation Sans",
    "sans":                          "Liberation Sans",
    "sans-serif":                    SANS,
    # Monoespaciades (llegat: FreeMono, M+ 1p Fallback, Courier malformat)
    "m+ 1p fallback":                                MONO,
    "'m+ 1p fallback'":                              MONO,
    "courier new, monospace":                        MONO,
    "'courier new', monospace":                      MONO,
    "'courier new, monospace'":                      MONO,
    "courier new,monospace":                         MONO,
    "freemono":                                      "'Liberation Mono'",
    "freemono, monospace":                           MONO,
    "freemono, 'courier new', monospace":            MONO,
    "freemono,'courier new',monospace":              MONO,
    "freemono, \"courier new\", monospace":          MONO,
    # Figures externes extretes de PDF via pymupdf (text traçat, vegeu §15)
    # o exportades de LO Draw / draw.io (23_figs_externes/T7_*)
    "arial embedded":                                SANS,
    "arial, sans-serif":                              SANS,
    "courier":                                        MONO,
    "courier embedded":                               MONO,
    "symbol":                                         SANS,
    "symbol embedded":                                SANS,
    "timesnewroman embedded":                         SANS,
    "timesnewroman, serif":                            SANS,
    "helvetica":                                      SANS,
}

# Valors considerats correctes (no es reporten com a desconeguts)
KNOWN_NORMALIZED = {
    "liberation sans",
    SANS.lower(),
    "liberation mono",
    MONO.lower(),
    "arial", "helvetica", "courier new", "courier", "monospace",
    "",   # font-family="" buit (artefacte Inkscape); s'ignora silenciosament
}
```

---

## 13. Variant dark

> **Les variants dark no es creen ni editen manualment.** Es generen automàticament com a part del procés de pre-render de Quarto mitjançant l'script `25_scripts/gen_dark.py`.

L'script s'executa com a darrer pas del `pre-render` a `_quarto.yml` (vegeu `_quarto.yml` per al pipeline complet). Per a cada `auto_figs/*_light.svg`, genera el fitxer `auto_figs/*_dark.svg` corresponent aplicant la taula de substitució definida al bloc `#svg-dark-replacements` d'aquest fitxer. Per modificar la paleta dark, editeu **només** aquest bloc.

```{.python #svg-dark-replacements}
REPLACEMENTS = [
    ('#f8f9fa', '#3d3d3d'),  # reservada / neutre / processos
    ('#adb5bd', '#888888'),  # stroke neutre
    ('#6c757d', '#adb5bd'),  # text neutre
    ('#343a40', '#ffffff'),  # text fosc
    ('#cfe2ff', '#1a3a5c'),  # .data / vars locals / fitxers font (blau)
    ('#084298', '#90bfff'),
    ('#d1e7dd', '#1a3a2a'),  # heap / regs segurs / fitxers objecte (verd)
    ('#0a3622', '#90d4aa'),
    ('#fff3cd', '#3a2e00'),  # pila / ra / biblioteques (ambre)
    ('#664d03', '#ffd966'),
    ('#f8d7da', '#3a1a1e'),  # .text / executable (rosa)
    ('#842029', '#f1a8ae'),
    ('#cc0000', '#ff6b6b'),  # dependències de dades: resultats intermedis (T3_deps_*, vegeu §14)
    ('#f8d0d3', '#3d1a1e'),  # Miss zona bloc (vermell clar → fosc)
    ('#dc3545', '#f07080'),  # Miss zona bloc stroke
    ('#c8ebd8', '#1a3328'),  # Hit zona bloc (verd clar → fosc)
    ('#198754', '#70c898'),  # Hit zona bloc stroke
    ('#e6f1fb', '#173349'),  # zona o contenidor: fons blau molt clar
    ('#dee2e6', '#495057'),  # graella i vores secundàries (Bootstrap gray-300 → gray-700)
    # Figures extretes de PDF (text traçat, vegeu §15)
    ('#000000', '#adb5bd'),  # línies i text negre implícit → gris clar
    ('#ffffff', '#2d2d2d'),  # fons blanc de zones internes → gris molt fosc
    # Artefacte Inkscape: color de la graella d'edició (<inkscape:grid color=...>),
    # invisible al render. Entrada identitat perquè no es reporti com a desconegut.
    ('#0099e5', '#0099e5'),
]
```

Els colors dins els marcadors `<polygon fill="...">` també es substitueixen automàticament → les puntes adopten el color dark correcte.

---

## 14. Notes operatives sobre figures específiques

Les variants dark de totes les figures es generen automàticament (vegeu §13).

**Figures de dependències de dades** (`T3_deps_*`): el color `#cc0000` (resultats intermedis i usos posteriors a la crida) forma part de la taula de substitució dark (§13) amb l'equivalent `#ff6b6b`; la variant dark es genera automàticament.

**Colors llegat: migrats el 2026-10-06.** Fins llavors, diverses figures natives (T1, T3, T5, T6, T7) feien servir colors fora de la paleta §10, que §13 convertia per al fosc; dues, `T3_pila_uninivell` i `T3_pila_multinivell`, en feien servir un (`#e6e9ec`) que no hi era, i al fosc la memòria lliure sortia d'un gris molt clar. Es van passar a la paleta: el negre de les figures natives de T5, a `#343a40`; els blaus de T1 i de `T7_mc_fallada`, a `#084298` i `#cfe2ff`; els grisos de text de T3, a `#343a40`; els de traç de T1, a `#adb5bd`; i el de la pila, a `#f8f9fa`. Dos colors que feien servir diverses figures amb un paper propi es van afegir a §10 (`#e6f1fb` i `#dee2e6`). §13 va perdre les 32 entrades que ja no feia servir cap fitxer: les 23 de les figures externes de T7 retirades a la fase 7c i les 9 que la migració va deixar lliures. Un color nou fora de §10 s'ha d'afegir a §13 en el mateix commit, o el fosc el deixa igual (`gen_dark.py` l'avisa al render).

---

## 15. Figures extretes de PDFs existents

Algunes figures del projecte provenen de PDFs originals (material docent anterior) i es generen amb el script Python `25_scripts/extract_pdf_figure.py` (o equivalent), que fa servir `pymupdf` i `text_as_path=True`.

### Característiques tècniques

- **Text traçat**: el text es converteix a corbes de Bézier. No és editable com a text, però és totalment portable (sense dependència de fonts instal·lades al sistema). Per editar el text cal partir del PDF original i regenerar.
- **Negre implícit fet explícit**: el SVG generat afegeix `fill="#000000" stroke="none"` a l'element `<svg>` arrel. Això fa que el negre per defecte (heretat implícitament per tots els paths i formes sense color explícit) sigui substituïble per `gen_dark.py` com qualsevol altre color de la paleta.
- **Fons verd eliminat**: el color `#d9ffd9` (realçat del visor de PDFs) s'elimina durant l'extracció.

### Generació de la variant dark

Les figures extretes de PDF **es generen automàticament** per `gen_dark.py` com la resta de figures, gràcies a les dues entrades específiques de la taula `REPLACEMENTS` (§13):

| Light | Dark | Ús |
|:---|:---|:---|
| `#000000` | `#adb5bd` | Línies, contorns i text de figures de línia negra |
| `#ffffff` | `#2d2d2d` | Zones blanques internes (p. ex. àrea buida de barres) |

**El pipeline automàtic gestiona correctament totes les figures extretes de PDF**: no cal cap configuració addicional.

### Figures del projecte generades per aquest mètode

| Figura | PDF d'origen | Contingut |
|:---|:---|:---|
| `T6_amdahl` | `T6_amdahl.pdf` | Barres $t_0/t_1$, fraccions $P_x$, $s_x$ (Llei d'Amdahl) |
| `T6_tc_tc_prima` | `T6_tc_tc_prima.pdf` | Barres A/B, $t_c$ vs $t_c'$ (reducció de temps de cicle) |
| `T6_not_cmos` | `T6_not__cmos___1_0___0_1.pdf` | Porta NOT: representació funcional i CMOS |
| `T6_not_1_0` | `T6_not__cmos___1_0___0_1.pdf` | Càrrega RC, $V(t)=V_{CC}(1-e^{-t/RC})$ |
| `T6_not_0_1` | `T6_not__cmos___1_0___0_1.pdf` | Descàrrega RC, $V(t)=V_{CC}\,e^{-t/RC}$ |

Les cinc figures de T6 ja no són el resultat directe de l'extracció: el 2026-10-06 se'ls va treure el `textLength` (que `rsvg-convert` no implementa), els subíndexs es van passar a `<tspan dy>` dins d'un sol `<text>` (a `T6_amdahl`, els 38 `<text>` d'un caràcter o d'un subíndex es van refer en 15), el text es va posar en la notació d'A6 ($V_{CC}$, $V_{in}$, $V_{out}$, $s_x$, $t_{\text{no-millorat}}$, PMOS i NMOS) i els colors, a la paleta (el negre a `#343a40`, i el gris mig de les barres, `#999999` i `#b3b3b3`, a `#adb5bd`). Si mai es tornen a extreure del PDF, cal refer-ho. Un espai que obre un `<tspan>` després d'un subíndex, `rsvg-convert` se'l menja si el `<text>` no porta `xml:space="preserve"`.


---

## 16. Portes lògiques i circuits

Convenció fixada a la fase 5 (2026-10-03, decisió de l'usuari) amb les figures del sumador de T4. Hi ha una implementació de referència a `25_scripts/gen_T4_sumador.py` (funcions `and_gate`, `or_gate`, `xor_gate`, `line`, `dot`, `term`, `sig`).

- **Símbols**: forma distintiva ANSI/IEEE 91 (la de les diapositives i la d'IC), no la rectangular de l'IEC. Mides de referència: AND de 36 × 32, OR de 40 × 32 i XOR com l'OR desplaçada 6 px, amb una segona corba al darrere. Les entrades són a ±10 del centre; a l'OR i la XOR, els fils s'aturen sobre la corba del darrere (+3 px).
- **Colors**: portes i fils amb traç `#343a40` (al fosc, `#ffffff`), de 1,5 px i sense farciment. Els blocs funcionals (semisumador, sumador complet) són caixes blaves `#cfe2ff`/`#084298`, i el nom del bloc i dels ports va en blau a 11 px. El que la figura vol fer veure (p. ex. la XOR del sobreeiximent i els seus fils) es ressalta en rosa: traç `#842029`, farciment de la porta `#f8d7da`.
- **Unions i terminals**: una derivació és un punt ple de radi 2,5. Una entrada o sortida de la figura és un cercle buit de radi 2,5 (farciment `#ffffff`). Dos fils que es creuen sense punt no estan connectats.
- **Senyals**: variables en cursiva a 13 px i subíndexs a 9 px, amb `<tspan dy>` dins d'un sol `<text>` (mai `textLength`, que `rsvg-convert` no implementa). Els senyals intermedis van en gris de text neutre (`#6c757d`) a 11 px.
- **Operadors ⊕ i ∧**: Liberation Sans no en té els glifs, i cada renderitzador els pren d'una font de reserva. L'operador va en un `<tspan>` propi, separat del que el volta amb `dx="3"` a l'operador i al `<tspan>` següent, **no amb espais**: rsvg col·locava malament els espais del voltant del glif de reserva (verificat a rsvg i a Chrome).

| Figura | Generador | Contingut |
|:---|:---|:---|
| `T4_semisumador_sumador_complet` | `25_scripts/gen_T4_sumador.py` | (a) Semisumador; (b) sumador complet amb dos semisumadors i una OR |
| `T4_sumador_propagacio_rossec` | `25_scripts/gen_T4_sumador.py` | Cadena de sumadors complets i XOR del sobreeiximent |

Els SVG generats es versionen a `22_figs_originals/`: el generador no forma part del pre-render. Si es canvia, cal regenerar-los (`25_scripts/gen_T4_sumador.py`) i versionar-ne el resultat.

---

## 17. Figures generades per script

Model de generació de la fase 7c (2026-10-03, decisió de l'usuari):

- **Model (b), per a les famílies**: la definició és el font, en un TOML de `24_specs/`, i un script del pre-render (`_quarto.yml`) n'escriu les figures a `auto_figs/`, amb un sufix propi; l'SVG no es versiona. Retocar una figura és canviar-ne la definició, i una convenció nova s'aplica a tota la família d'un sol cop.
- **Model (a), per a les figures soltes**: el font és l'SVG versionat a `22_figs_originals/`, i un script el regenera. L'script té l'opció `--comprova`, que compara el que generaria amb l'SVG versionat sense escriure res, i `make comprova-figures` les passa totes: un SVG retocat a mà i no a l'script hi surt com a diferència.

Generadors del pre-render (model (b)). El sufix de cada un és a la taula de sufixos de `13_contrib.qmd §Convencions SVG`:

| Definició | Generador | Sufix | Figures |
|:---|:---|:---|:---|
| `24_specs/registres.toml` | `25_scripts/gen_regs.py` | `__registre` | Registres de bits i formats d'instrucció (T2, T3, T5, T9) |
| `24_specs/BA.toml` | `25_scripts/gen_BA.py` | `__BA` | Blocs d'activació, amb les zones de §3–§11 (T3): escalars, vectors, alineació i zones genèriques amb text lliure, i, si cal, el desplaçament de cada zona (§9) |
| `24_specs/mapa.toml` | `25_scripts/gen_mapa.py` | `__mapa` | Mapes de memòria (T3): les regions de la memòria de RARS, amb les adreces i les fletxes de creixement, i la pila en diversos moments d'una crida, una columna per moment |
| `24_specs/subrutines.toml` | `25_scripts/gen_subrutines.py` | `__subrutina` | Dependències de dades d'una subrutina: el codi, les crides en franges i una barra de vida per dada (T3) |
| `24_specs/MC.toml` | `25_scripts/gen_MC.py` | `__MC` | Memòria cau (T7): simula la MC sobre una seqüència d'accessos i en dibuixa la seqüència pas a pas, la taula de traça o l'estat en un moment donat; i els diagrames de blocs de la lectura |
| `24_specs/memoria.toml` | `25_scripts/gen_memoria.py` | `__memoria` | Memòria per bytes (T2): una fila per byte, amb l'adreça, la dada i una nota (MSB, LSB) o una fletxa de creixement |

`gen_BA.py` i `gen_mapa.py` comparteixen les primitives de la columna de memòria (zones, ratlles, etiquetes, fletxes), que són a `25_scripts/columna_memoria.py`: no és cap generador, i no té sufix.

Figures de model (a): les del sumador de T4 (taula de §16) i aquestes:

| Figura | Generador | Contingut |
|:---|:---|:---|
| `T7_texe_diagrama` | `25_scripts/gen_T7.py` | Tres instruccions etapa per etapa, amb una MC ideal i amb una fallada |
| `T7_multinivell_diagrama` | `25_scripts/gen_T7.py` | CPU–MP, CPU–MC–MP i CPU–L1–L2–MP, amb els temps de cada enllaç |
| `T7_multinivell_multicore` | `25_scripts/gen_T7.py` | Xip de quatre nuclis amb L1i, L1d i L2 privades i L3 compartida |
| `T7_tipus_fallades` | `25_scripts/gen_T7.py` | Taxa de fallades segons la mida i l'associativitat (qualitativa) |
| `T8_mv_espais` | `25_scripts/gen_T8.py` | Espais lògics de dos processos, la MMU, la memòria física i el disc |
| `T8_mv_jerarquia` | `25_scripts/gen_T8.py` | Piràmide de la jerarquia de memòria amb el disc i els temps d'accés (figura 7.2 del tema antic) |
| `T8_mv_adreca_exemple` | `25_scripts/gen_T8.py` | L'adreça 0x10010004 descomposta en VPN i desplaçament (sense peu) |
| `T8_mv_traduccio` | `25_scripts/gen_T8.py` | Traducció d'una adreça lògica de 32 bits a una de física de 14 (figura 7.4 del tema antic) |
| `T8_mv_pagines_marcs` | `25_scripts/gen_T8.py` | Pàgines de dos processos assignades a marcs, i una al disc |
| `T8_mv_taula_pagines` | `25_scripts/gen_T8.py` | Adreça lògica, registre de taula de pàgines, taula indexada pel VPN i adreça física (figura 7.5 del tema antic, amb el bit E) |
| `T8_mv_traduccio_exemple` | `25_scripts/gen_T8.py` | La traducció de 0x00001801 amb la taula del procés 2 (figura 7.6 del tema antic) |
| `T8_mv_taula_multinivell` | `25_scripts/gen_T8.py` | Taula de dos nivells de Sv32, amb VPN[1], VPN[0] i el desplaçament |
| `T8_mv_tlb_estructura` | `25_scripts/gen_T8.py` | El TLB com a còpia parcial de la taula de pàgines |
| `T8_mv_flux_traduccio` | `25_scripts/gen_T8.py` | Diagrama de flux de la traducció, amb les zones del maquinari i del SO |
| `T8_mv_comparticio` | `25_scripts/gen_T8.py` | Dues taules de pàgines que apunten al mateix marc |
| `T8_mv_pipt` | `25_scripts/gen_T8.py` | TLB i MC en sèrie, amb el cronograma de l'accés |
| `T8_mv_vipt` | `25_scripts/gen_T8.py` | TLB i MC en paral·lel i el comparador, amb el cronograma a la mateixa escala |
| `T8_mv_exemple_tlb` | `25_scripts/gen_T8.py` | Traça dels cinc accessos de `#tip-mv-tlb-exemple`, simulats, i els fotogrames `_pas<k>` de la figura dinàmica |

**Figures dinàmiques (només a l'HTML).** Amb `fotogrames = true`, `gen_MC.py` escriu també un fotograma per pas, `<nom>_pas<k>__MC_{light,dark}.svg`, tots de la mateixa mida (i `gen_T8.py`, de model (a), els de `#fig-mv-tlb-exemple`, `22_figs_originals/T8_mv_exemple_tlb_pas<k>.svg`, que el pre-render converteix com la resta d'originals), i `figures_dinamiques.html` (inclòs a l'HTML per `_quarto.yml`) converteix la figura en un navegador de passos. El PDF hi porta la figura estàtica del mateix script i de la mateixa definició, de manera que els dos formats no poden divergir. Prototip: `#fig-lru-exemple` (bloc 9 de la fase 7c, 2026-10-04); el marcatge és a `13_contrib.qmd §Figures dinàmiques`.

**Figures de memòria cau (`gen_MC.py`).** Dos estils, de la mateixa simulació: `sequencia` (la MP, cada accés amb l'explicació que en calcula l'script, i l'estat de la MC després de cada accés) i `traca` (una fila per accés, amb el bloc que conté cada línia després de l'accés; en color, el que acaba de canviar, i amb vora gruixuda, la línia accedida). Un tercer, `estat`, dibuixa només la MC després dels accessos d'`inicial`: són les taules d'organització d'A7 (`#fig-mc-organitzacio`, `#fig-assoc-conjunts-taula` i `#fig-escriptura-dirty-bit`, natives fins al 2026-10-06), amb una cel·la de dades per línia (`dades = "bloc"`) i, amb `ubica`, la MP i les vies on pot anar el bloc d'una adreça. Decisió de l'usuari (2026-10-04): al PDF, la seqüència per als exemples curts (estat inicial, polítiques d'escriptura, LRU) i la traça per als llargs (conflicte, capacitat); l'estat inicial, en totes dues, com a subfigures, perquè l'alumne faci la transició d'una a l'altra. A l'HTML hi anirà la figura dinàmica (fotogrames de l'estil `sequencia`). Els colors són un per bloc, en l'ordre en què surten a la MP, o un per vector (`color = "vector"`), i la terminologia és la de la decisió 11 de la fase 7c: «Lectura», «Escriptura», «Encert», «Fallada» i fallades «obligatòria», «de capacitat» i «de conflicte».

Una mateixa figura pot tenir alhora una versió original i una de generada, amb el mateix nom i un sufix diferent: les dependències de `multi` i d'`exemple` (A3) són a `22_figs_originals/` (amb fletxes) i a `subrutines.toml` (amb barres de vida), i A3 les mostra totes dues, com a subfigures (a) i (b). Quan el llibre consumeix només la generada, l'original es conserva a `22_figs_originals/` (`13_contrib.qmd §Convencions SVG`): els BA de `multi` i d'`exemple` des del 2026-10-04, i des del 2026-10-07, els de `func` i el general, el mapa de memòria i les dues piles en fila (A3).
