# Instruccions per a figures de memòria i bloc d'activació — EC

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

| Zona | `fill` | `stroke` / text |
|:---|:---|:---|
| Reservada / espai lliure | `#f8f9fa` | `#adb5bd` / `#6c757d` |
| Alineació | `#f8f9fa` | `#adb5bd` / `#6c757d` |
| `.text` | `#f8d7da` | `#842029` |
| `.data` | `#cfe2ff` | `#084298` |
| Heap | `#d1e7dd` | `#0a3622` |
| Pila | `#fff3cd` | `#664d03` |
| Variables locals (BA) | `#cfe2ff` | `#084298` |
| Registres segurs (BA) | `#d1e7dd` | `#0a3622` |
| `ra` desat (BA) | `#fff3cd` | `#664d03` |

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

Aplicar les substitucions de paleta light → dark:

```python
replacements = [
    ('#f8f9fa','#3d3d3d'), ('#adb5bd','#888'),
    ('#6c757d','#adb5bd'), ('#343a40','#fff'),
    ('#cfe2ff','#1a3a5c'), ('#084298','#90bfff'),
    ('#d1e7dd','#1a3a2a'), ('#0a3622','#90d4aa'),
    ('#fff3cd','#3a2e00'), ('#664d03','#ffd966'),
    ('#f8d7da','#3a1a1e'), ('#842029','#f1a8ae'),
]
```

Els colors dins els marcadors `<polygon fill="...">` també es substitueixen
automàticament → les puntes adopten el color dark correcte.

---

## 13. Figures afectades per aquests patrons

| Figura | Tipus | Notes |
|:---|:---|:---|
| `T3_mapa_memoria` | Mapa de memòria | Figura de referència del conveni |
| `T3_ba_general` | BA genèric | Figura de referència del model de BA |
| `T3_ba_func` | BA de `func` | v (char×10), alineació, w (int×10) |
| `T3_ba_multi` | BA de `multi` | s0, s1, ra |
| `T3_ba_exemple` | BA de `exemple` | q, v, w, alineació, s0, s1, s2, ra |
| `T3_func_uninivell_pila` | Pila dinàmica | Evolució de sp |
| `T3_pila_crides_aniuades` | Pila dinàmica | Crides aniuades funcA/funcB |
