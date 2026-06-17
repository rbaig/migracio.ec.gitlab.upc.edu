# SVG specs — EC

Figures de referència:
- Mapa de memòria: `figures/T3_mapa_memoria_light.svg`
- Bloc d'activació: `figures/T3_ba_general_light.svg`

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

## 2. Canvas i marges

El canvas **es calcula** a partir dels marges fixos i l'extensió dels objectes; no té mida fixa.

```
marge_superior  = 10 px
marge_inferior  = 10 px
marge_esquerre  = 76 px   (reservat per a etiquetes d'adreça + eix visual)
marge_dret      = 10 px
```

Fórmules:

```
W = 76 + w_rect + 10  =  76 + 230 + 10  =  316 + 10  =  326 px
H = 10 + h_total_segments + 10
```

On `w_rect = 230 px` i `h_total_segments` és la suma de les alçades de totes les zones.

---

## 3. Escala i alçades

**Factor d'escala de referència: 20 px/byte.**

```
1 byte  =  20 px
4 bytes =  80 px   (registre, p. ex. `ra`, `s0`...)
```

Quan el contingut és gran (vectors llargs, moltes zones), cal reduir l'escala per mantenir la figura en una mida razonable. Factors admesos, en ordre decreixent:

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

**Excepció — zona d'un sol bloc** (p. ex. `ra`, alineació simple):
- Un sol `<rect>` amb stroke sòlid, ratlles i text centrat.
- O un sol `<rect>` amb vores verticals discontínues si la mida no és múltiple de 4.

### Sub-rect sòlid

```xml
<rect x="86" y="{y}" width="230" height="{h}"
      fill="{fill}" stroke="{stroke}" stroke-width="1"/>
```

Porta **ratlles indicadores** als costats esquerre i dret (vegeu §6).

### Sub-rect mig (discontíu)

```xml
<rect x="86" y="{y}" width="230" height="{h}" fill="{fill}" stroke="none"/>
<line x1="86"  y1="{y}" x2="86"  y2="{y+h}"
      stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>
<line x1="316" y1="{y}" x2="316" y2="{y+h}"
      stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>
```

El text es col·loca centrat verticalment dins aquest sub-rect (vegeu §8).

---

## 5. Columna de rectangles

```
x_rect  = 86 px      (= marge_esq + 10 = 76 + 10)
w_rect  = 230 px
```

Els sub-rectangles són adjacents (sense espai entre ells).

---

## 6. Ratlles indicadores de mida

Les ratlles van als sub-rects **sòlids** (superior i inferior), mai al mig.
S'apliquen als **costats esquerre i dret** del rectangle, cap a l'interior.

```
x_esq_interior = 87   (= x_rect + 1)
x_dret_interior = 315  (= x_rect + w_rect - 1)
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
<line x1="315" y1="{y+h*0.25}" x2="309" y2="{y+h*0.25}" stroke="{stroke}" stroke-width="1"/>
<line x1="315" y1="{y+h*0.50}" x2="303" y2="{y+h*0.50}" stroke="{stroke}" stroke-width="1"/>
<line x1="315" y1="{y+h*0.75}" x2="309" y2="{y+h*0.75}" stroke="{stroke}" stroke-width="1"/>
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

> **Nota:** La documentació anterior indicava `x2="316"` (amplada total). Els SVGs de referència usen `x2="86"` (10 px). La mida correcta és **10 px**.

---

## 8. Text dins les zones

### Títol (primera línia, bold)

```
font-size:    12 px
font-weight:  bold
text-anchor:  middle
x:            201  (centre de la columna = 86 + 230/2)
y:            y_mig + h_mig/2 - (n_línies-1)×16/2   (centrat vertical)
fill:         color del stroke de la zona
```

### Línies secundàries

```
font-size:    11 px
font-weight:  normal
text-anchor:  middle
x:            201
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

Espai cada 4 dígits hexadecimaux:

```
0x0000 0000 · 0x0040 0000 · 0x1001 0000 · 0x1004 0000 · 0x7fff effc
```

### Etiquetes de rol («adr. baixes» / «adr. altes» / «sp →»)

```
«adr. baixes»  font-size=10  fill=#6c757d   y = marge_sup + 3
«sp →»         font-size=11  fill={stroke zona cim}  font-weight=bold  y = marge_sup + 12
«adr. altes»   font-size=10  fill=#6c757d   y = H - marge_inf + 3
```

---

## 10. Paleta de colors per zona

Paleta unificada per a **totes** les figures SVG del projecte (memòria, BA i flux).

| Zona / tipus | `fill` | `stroke` / text |
|:---|:---|:---|
| Reservada / espai lliure / processos | `#f8f9fa` | `#adb5bd` / `#6c757d` |
| Alineació | `#f8f9fa` | `#adb5bd` / `#6c757d` |
| `.text` / executable | `#f8d7da` | `#842029` |
| `.data` / fitxers font `.c` `.h` / variables locals (BA) | `#cfe2ff` | `#084298` |
| Heap / fitxers objecte `.o` / registres segurs (BA) | `#d1e7dd` | `#0a3622` |
| Pila / biblioteques `lib.a` / `ra` desat (BA) | `#fff3cd` | `#664d03` |
| Dependències de dades — resultat intermedi | — | `#cc0000` |

---

## 11. Fletxes de creixement (heap i pila)

### Marcadors (`<defs>`)

```xml
<!-- Punta cap amunt (pila) -->
<marker id="arr-up" markerWidth="8" markerHeight="8"
        refX="4" refY="0" orient="auto">
  <polygon points="0,8 4,0 8,8" fill="#664d03"/>
</marker>
<!-- Punta cap avall (heap) -->
<marker id="arr-dn" markerWidth="8" markerHeight="8"
        refX="4" refY="8" orient="auto">
  <polygon points="0,0 4,8 8,0" fill="#0a3622"/>
</marker>
```

El color del `fill` del marcador coincideix amb el `stroke` de la zona.

### Heap (fletxa cap avall, a la dreta del rectangle)

```
x_fletxa = x_rect + 208 = 294   (dins del canvas, a la dreta de w_rect)
y_inici  = y_heap + 47
y_fi     = y_heap_fi + 33
stroke   = #0a3622   stroke-width="1.5"   marker-end="url(#arr-dn)"
```

### Pila (fletxa cap amunt, a l'esquerra del rectangle)

```
x_fletxa = x_rect + 22 = 108
y_inici  = y_pila + 8
y_fi     = y_pila - 33
stroke   = #664d03   stroke-width="1.5"   marker-end="url(#arr-up)"
```

### Text «creix» rotat

Fórmula per a un text centrat al costat d'una línia vertical en `(x_L, y_centre)`:

```
rotate(+90):  <text x=" y_centre" y="-x_L"  transform="rotate(90)"  ...>
rotate(-90):  <text x="-y_centre" y=" x_L"  transform="rotate(-90)" ...>
font-size: 11 px   fill: color de la zona   text-anchor: middle
```

---

## 12. Variant dark

> **Les variants dark no es creen ni editen manualment.** Es generen automàticament com a part del procés de render de Quarto mitjançant l'script `scripts/svg_generate_dark.py`.

### Generació automàtica

L'script s'executa com a `pre-render` a `_quarto.yml`:

```yaml
project:
  pre-render: scripts/svg_generate_dark.py
```

Per a cada `figures/*_light.svg`, l'script genera (o actualitza) el fitxer `figures/*_dark.svg` corresponent aplicant la taula de substitució de colors. La generació es **salta** si:

- El fitxer dark és **més nou** que el light (ja és vigent).
- El nom del fitxer dark és a `scripts/dark_exclusions.txt` (dark gestionada manualment).

Per protegir una dark retocada manualment a Inkscape, afegiu el seu nom a `scripts/dark_exclusions.txt`:

```
# scripts/dark_exclusions.txt
T3_ba_general_dark.svg
```

### Taula de substitució light → dark

El bloc següent és la **font de veritat** de la taula. L'script `scripts/svg_generate_dark.py` el llegeix directament d'aquest fitxer en temps d'execució (vegeu §12 «Generació automàtica»). Per modificar la paleta dark, editeu només aquest bloc.

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
    # Figures extretes de PDF (text traçat, vegeu §14)
    ('#000000', '#adb5bd'),  # línies i text negre implícit → gris clar
    ('#ffffff', '#2d2d2d'),  # fons blanc de zones internes → gris molt fosc
    ('#b3b3b3', '#666666'),  # gris mig (p. ex. barres de tc/tc') → gris fosc llegible
]
```

Els colors dins els marcadors `<polygon fill="...">` també es substitueixen automàticament → les puntes adopten el color dark correcte.

---

## 13. Figures afectades per aquests patrons

Les variants dark de totes les figures es generen automàticament (vegeu §12). La columna «Notes» indica el contingut o les convencions específiques.

| Figura | Tipus | Notes |
|:---|:---|:---|
| `T3_mapa_memoria` | Mapa de memòria | Figura de referència del conveni de colors |
| `T3_ba_general` | BA genèric | Figura de referència del model de BA |
| `T3_ba_func` | BA | `v` (char×10), alineació, `w` (int×10); escala ×½ |
| `T3_ba_multi` | BA | `s0`, `s1`, `ra`; escala ×1 |
| `T3_ba_exemple` | BA | `q`, `v`, `w`, alineació, `s0`–`s2`, `ra`; escala ×½ |
| `T3_func_uninivell_pila` | Pila dinàmica | 3 estats: avant/durant/après crida a `funcB` |
| `T3_pila_crides_aniuades` | Pila dinàmica | 5 estats: crides aniuades `funcA`/`funcB` |
| `T3_compilacio_separada` | Graf de flux | Graf LR: `p1.c`/`p9.c` → `gcc` → `.o` → `ld` → executable |
| `T3_flux_gcc_complet` | Graf de flux | Graf TD: flux complet GCC amb subgraphs |
| `T3_deps_multi` | Dependències de dades | `c`, `d` (blau `#084298`) travessen la frontera; `c`, `d`, `e` al return (vermell `#cc0000`) |
| `T3_deps_exemple` | Dependències de dades | `a`, `b`, `c`, `d` (blau); `res_f`, `res_g` com a òvals (vermell `#cc0000`); dues fronteres |

> **Nota sobre les figures de dependències:** el color `#cc0000` s'usa per a cercles/òvals de resultats intermedis i per als usos posteriors a la crida. Aquest color **no forma part de la taula de substitució dark** (§12) i, per tant, les figures `T3_deps_*` s'han d'afegir a `scripts/dark_exclusions.txt` fins que es defineixi la seva variant dark manualment.

---

## 14. Figures extretes de PDFs existents

Algunes figures del projecte provenen de PDFs originals (material docent anterior) i es generen amb el script Python `scripts/extract_pdf_figure.py` (o equivalent), que fa servir `pymupdf` i `text_as_path=True`.

### Característiques tècniques

- **Text traçat**: el text es converteix a corbes de Bézier. No és editable com a text, però és totalment portable (sense dependència de fonts instal·lades al sistema). Per editar el text cal partir del PDF original i regenerar.
- **Negre implícit fet explícit**: el SVG generat afegeix `fill="#000000" stroke="none"` a l'element `<svg>` arrel. Això fa que el negre per defecte (heretat implícitament per tots els paths i formes sense color explícit) sigui substituïble per `svg_generate_dark.py` com qualsevol altre color de la paleta.
- **Fons verd eliminat**: el color `#d9ffd9` (realçat del visor de PDFs) s'elimina durant l'extracció.

### Generació de la variant dark

Les figures extretes de PDF **es generen automàticament** per `svg_generate_dark.py` com la resta de figures, gràcies a les tres entrades específiques de la taula `REPLACEMENTS` (§12):

| Light | Dark | Ús |
|:---|:---|:---|
| `#000000` | `#adb5bd` | Línies, contorns i text de figures de línia negra |
| `#ffffff` | `#2d2d2d` | Zones blanques internes (p. ex. àrea buida de barres) |
| `#b3b3b3` | `#666666` | Gris mig de figures (p. ex. barres de `T6_tc_tc_prima`) |

**No cal afegir-les a `dark_exclusions.txt`**: el pipeline automàtic les gestiona correctament.

### Figures del projecte generades per aquest mètode

| Figura | PDF d'origen | Contingut |
|:---|:---|:---|
| `T6_amdahl` | `T6_amdahl.pdf` | Barres $t_0/t_1$, fraccions $P_x$, $s_x$ (Llei d'Amdahl) |
| `T6_tc_tc_prima` | `T6_tc_tc_prima.pdf` | Barres A/B, $t_c$ vs $t_c'$ (reducció de temps de cicle) |
| `T6_not_cmos` | `T6_not__cmos___1_0___0_1.pdf` | Porta NOT: representació funcional i CMOS |
| `T6_not_1_0` | `T6_not__cmos___1_0___0_1.pdf` | Càrrega RC, $V(t)=Vcc(1-e^{-t/RC})$ |
| `T6_not_0_1` | `T6_not__cmos___1_0___0_1.pdf` | Descàrrega RC, $V(t)=Vcc\,e^{-t/RC}$ |

### Distinció respecte a figures de nova creació

| Propietat | Figura extreta de PDF | Figura de nova creació |
|:---|:---|:---|
| Text | Traçat (corbes) | Editable, font `'Source Sans Pro', sans-serif` |
| Colors | Negre implícit → explícit (`#000000`) | Paleta del projecte (§10) |
| Edició | Inkscape (corbes) o regeneració des de PDF | Inkscape (text editable) |
| Dark | Automàtica via `REPLACEMENTS` | Automàtica via `REPLACEMENTS` |
