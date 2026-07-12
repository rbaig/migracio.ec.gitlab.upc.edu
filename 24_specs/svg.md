# SVG specs — EC

Figures de referència:
- Mapa de memòria: `auto_figs/T3_mapa_memoria_light.svg`
- Bloc d'activació: `auto_figs/T3_ba_general_light.svg`

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

**Excepcions:**

- **Registres de bits** (`gen_regs.py`): `W = 2 + total_bits × 22 + 2` px (708 px per a 32 bits). `width="100%"` igual.
- **BA i mapes de memòria** *(pendent de migrar a `estreta`)*: marges fixos `sup=inf=10 px`, `esq=76 px`, `dret=10 px`; `w_rect=230 px`; `W=316 px`. Vegeu `TODO.md` per al pla de migració.

---

## 3. Escala i alçades

> **Nota:** Els valors numèrics de coordenades i dimensions de les seccions §3–§11 corresponen al canvas actual de les figures de BA i mapes de memòria (`w_rect=230`, `W=316 px`). S'actualitzaran quan s'executi la migració a classe `estreta` (340 px); vegeu `TODO.md`.

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

**Excepció — zona d'un sol bloc** (p. ex. `ra`, alineació simple):
- Un sol `<rect>` amb stroke sòlid, ratlles i text centrat.
- O un sol `<rect>` amb vores verticals discontínues si la mida no és múltiple de 4.

### Sub-rect sòlid

```xml
<rect x="{x_rect}" y="{y}" width="{w_rect}" height="{h}"
      fill="{fill}" stroke="{stroke}" stroke-width="1"/>
```

Porta **ratlles indicadores** als costats esquerre i dret (vegeu §6). Valors de `x_rect` i `w_rect`: vegeu §5.

### Sub-rect mig (discontíu)

```xml
<rect x="{x_rect}" y="{y}" width="{w_rect}" height="{h}" fill="{fill}" stroke="none"/>
<line x1="{x_rect}"          y1="{y}" x2="{x_rect}"          y2="{y+h}"
      stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>
<line x1="{x_rect+w_rect}"   y1="{y}" x2="{x_rect+w_rect}"   y2="{y+h}"
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
    # Figures extretes de PDF (text traçat, vegeu §15)
    ('#000000', '#adb5bd'),  # línies i text negre implícit → gris clar
    ('rgb(0, 0, 0)', '#adb5bd'),  # negre en notació funcional (export draw.io)
    ('#ffffff', '#2d2d2d'),  # fons blanc de zones internes → gris molt fosc
    ('#b3b3b3', '#666666'),  # gris mig (p. ex. barres de tc/tc') → gris fosc llegible
    ('#f8d0d3', '#3d1a1e'),  # Miss zona bloc (vermell clar → fosc)
    ('#dc3545', '#f07080'),  # Miss zona bloc stroke
    ('#c8ebd8', '#1a3328'),  # Hit zona bloc (verd clar → fosc)
    ('#198754', '#70c898'),  # Hit zona bloc stroke
    # Artefacte Inkscape: color de la graella d'edició (<inkscape:grid color=...>),
    # invisible al render. Entrada identitat perquè no es reporti com a desconegut.
    ('#0099e5', '#0099e5'),
    # Colors llegat de figures natives (T1, T3, T6, T7; pendents de migrar a la paleta §10)
    ('#cc0000', '#ff6b6b'),  # T3_deps_*: resultats intermedis (vegeu §14)
    ('#0b449a', '#90bfff'),  # T7_mc_fallada: blau fosc → blau clar
    ('#185fa5', '#7db8e8'),  # T1_von_neumann: blau mig
    ('#1a5276', '#85c1e9'),  # T1_flux_compilacio: blau petroli fosc
    ('#4a90b8', '#7cc0e8'),  # T1_flux_compilacio: blau acer
    ('#333333', '#cccccc'),  # T3_ba_func: text gris molt fosc
    ('#4d4d4d', '#bbbbbb'),  # T3 BA/mapa memòria: text gris fosc
    ('#7d6d6c', '#b5a8a6'),  # T7_mc_fallada: gris marronós
    ('#888780', '#a5a49c'),  # T1: stroke gris càlid
    ('#999999', '#777777'),  # T6_amdahl: gris mig (fill)
    ('#dee2e6', '#495057'),  # T4/T7: vores gris clar (Bootstrap gray-300 → gray-700)
    ('#e6f1fb', '#173349'),  # T1_von_neumann: fons blau molt clar
    ('#e8f4f8', '#16333d'),  # T1_flux_compilacio: fons cian molt clar
    # Figures externes LO Draw / draw.io (T7): text traçat saturat → pastel clar
    ('#0000ff', '#6699ff'),  # text/línies blau pur
    ('#ff0000', '#ff7070'),  # text/línies vermell pur
    ('#00ff00', '#55dd55'),  # text/línies verd pur
    ('#2eff2e', '#55dd55'),  # verd brillant (draw.io)
    ('#2b5190', '#8fb3e8'),  # stroke blau fosc (gràfic tipus de fallades)
    ('#4273c5', '#9bbdf2'),  # blau mig (gràfic tipus de fallades)
    # Figures externes LO Draw / draw.io (T7): fons de cel·la clars → foscos apagats
    ('#8080ff', '#2e2e5c'),  # fons violeta-blau
    ('#b3b3ff', '#3a3a70'),  # fons lavanda
    ('#80ff80', '#1e4d1e'),  # fons verd clar
    ('#90c490', '#3a5f3a'),  # fons verd mig
    ('#ccffcc', '#1a3a1a'),  # fons verd molt clar
    ('#d3e8d3', '#243a24'),  # fons verd grisós
    ('#dfecf7', '#1c2e3f'),  # fons blau clar
    ('#ffff00', '#665f00'),  # fons groc (realçat)
    ('#ffff80', '#4d4700'),  # fons groc clar
    ('#ffff9a', '#544e10'),  # fons groc pàl·lid
    ('#ff6666', '#5c2626'),  # fons vermell mig (T7_lru_roger draw.io)
    ('#ff8080', '#4d1f1f'),  # fons vermell clar
    ('#ffe0d1', '#3d2a20'),  # fons taronja clar
    ('#ffe9e2', '#3d2a24'),  # fons taronja-rosat clar
    ('#ffebe0', '#3d2c20'),  # fons taronja pàl·lid
    ('#fff0ec', '#382723'),  # fons taronja-rosat molt pàl·lid
]
```

Els colors dins els marcadors `<polygon fill="...">` també es substitueixen automàticament → les puntes adopten el color dark correcte.

---

## 14. Notes operatives sobre figures específiques

Les variants dark de totes les figures es generen automàticament (vegeu §13).

**Figures de dependències de dades** (`T3_deps_*`): el color `#cc0000` (resultats intermedis i usos posteriors a la crida) forma part de la taula de substitució dark (§13) amb l'equivalent `#ff6b6b`; la variant dark es genera automàticament.

**Colors llegat**: diverses figures natives (T1, T3, T6, T7) usen colors fora de la paleta §10, incorporats a la taula §13 perquè la variant dark es generi correctament. Quan aquestes figures es migrin a la paleta §10, les entrades corresponents de §13 (bloc «Colors llegat») es podran retirar.

---

## 15. Figures extretes de PDFs existents

Algunes figures del projecte provenen de PDFs originals (material docent anterior) i es generen amb el script Python `25_scripts/extract_pdf_figure.py` (o equivalent), que fa servir `pymupdf` i `text_as_path=True`.

### Característiques tècniques

- **Text traçat**: el text es converteix a corbes de Bézier. No és editable com a text, però és totalment portable (sense dependència de fonts instal·lades al sistema). Per editar el text cal partir del PDF original i regenerar.
- **Negre implícit fet explícit**: el SVG generat afegeix `fill="#000000" stroke="none"` a l'element `<svg>` arrel. Això fa que el negre per defecte (heretat implícitament per tots els paths i formes sense color explícit) sigui substituïble per `gen_dark.py` com qualsevol altre color de la paleta.
- **Fons verd eliminat**: el color `#d9ffd9` (realçat del visor de PDFs) s'elimina durant l'extracció.

### Generació de la variant dark

Les figures extretes de PDF **es generen automàticament** per `gen_dark.py` com la resta de figures, gràcies a les tres entrades específiques de la taula `REPLACEMENTS` (§13):

| Light | Dark | Ús |
|:---|:---|:---|
| `#000000` | `#adb5bd` | Línies, contorns i text de figures de línia negra |
| `#ffffff` | `#2d2d2d` | Zones blanques internes (p. ex. àrea buida de barres) |
| `#b3b3b3` | `#666666` | Gris mig de figures (p. ex. barres de `T6_tc_tc_prima`) |

**El pipeline automàtic gestiona correctament totes les figures extretes de PDF**: no cal cap configuració addicional.

### Figures del projecte generades per aquest mètode

| Figura | PDF d'origen | Contingut |
|:---|:---|:---|
| `T6_amdahl` | `T6_amdahl.pdf` | Barres $t_0/t_1$, fraccions $P_x$, $s_x$ (Llei d'Amdahl) |
| `T6_tc_tc_prima` | `T6_tc_tc_prima.pdf` | Barres A/B, $t_c$ vs $t_c'$ (reducció de temps de cicle) |
| `T6_not_cmos` | `T6_not__cmos___1_0___0_1.pdf` | Porta NOT: representació funcional i CMOS |
| `T6_not_1_0` | `T6_not__cmos___1_0___0_1.pdf` | Càrrega RC, $V(t)=Vcc(1-e^{-t/RC})$ |
| `T6_not_0_1` | `T6_not__cmos___1_0___0_1.pdf` | Descàrrega RC, $V(t)=Vcc\,e^{-t/RC}$ |

