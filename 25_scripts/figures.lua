--[[
figures.lua — Filtre de Quarto per a les figures d'`auto_figs/` (fase 7c, bloc 12).

1. Text alternatiu (decisió 6 de la fase 7c): el `<desc>` de l'SVG n'és la font de
   veritat, i el filtre el copia a l'atribut `fig-alt` de la imatge, que Quarto escriu
   com a `alt` a l'HTML. Si el `.qmd` ja porta un `fig-alt`, es respecta. El peu
   (*caption*) es queda al `.qmd`.
2. Mida a l'HTML (decisió de l'usuari, 2026-10-06; `24_specs/svg.md §2`): cada imatge
   es mostra a l'amplada del seu `viewBox` per un factor únic, ESCALA, de manera que el
   text de totes les figures té la mateixa mida (11 px a l'SVG, uns 15 px a la pantalla).
   La classe `img-fluid` de Quarto les encongeix fins a l'amplada de la columna en un
   visor estret. Les imatges amb `{width=…}` o `{height=…}` al `.qmd` es respecten. Al
   PDF no s'hi toca: hi va a la mida del `viewBox`, com fins ara.
3. Figures dinàmiques: el div `.fig-dinamica` rep `data-amplada`, l'amplada dels
   fotogrames (que pot no ser la de la figura estàtica), i `figures_dinamiques.html`
   l'aplica als `<img>` que crea.

Llegeix els SVG d'`auto_figs/`, que el pre-render ja ha escrit quan s'executa el filtre.
]]

local ESCALA = 1.4

local function arrel()
  return (quarto.project and quarto.project.directory) or os.getenv('QUARTO_PROJECT_DIR') or '.'
end

local ENTITATS = { lt = '<', gt = '>', quot = '"', apos = "'", amp = '&' }

local memoria = {}
local function llegeix(src)
  local ruta = arrel() .. '/' .. src:gsub('^/', '')
  if memoria[ruta] == nil then
    local f = io.open(ruta, 'r')
    if not f then
      memoria[ruta] = false
    else
      local s = f:read('a')
      f:close()
      local desc = s:match('<desc[^>]*>(.-)</desc>')
      if desc then
        desc = desc:gsub('%s+', ' '):gsub('^ ', ''):gsub(' $', ''):gsub('&(%a+);', ENTITATS)
      end
      local w = s:match('viewBox="%s*[-%d.]+[%s,]+[-%d.]+[%s,]+([%d.]+)')
      memoria[ruta] = { desc = desc, w = tonumber(w) }
    end
  end
  return memoria[ruta] or nil
end

local function amplada(w)
  return tostring(math.floor(w * ESCALA + 0.5)) .. 'px'
end

function Image(img)
  if not img.src:match('auto_figs/.*%.svg$') then return nil end
  local info = llegeix(img.src)
  if not info then return nil end
  local canvi = false
  if info.desc and info.desc ~= '' and not img.attributes['fig-alt'] then
    img.attributes['fig-alt'] = info.desc
    canvi = true
  end
  if info.w and quarto.doc.is_format('html') and not img.attributes['width'] and not img.attributes['height'] then
    img.attributes['width'] = amplada(info.w)
    canvi = true
  end
  if canvi then return img end
end

function Div(div)
  if not div.classes:includes('fig-dinamica') or not quarto.doc.is_format('html') then return nil end
  local src
  div:walk({ Image = function(im) src = src or im.src end })
  local base, sufix = (src or ''):match('^(.*)__(%a+)_light%.svg$')
  if not base then return nil end
  local info = llegeix(base .. '_pas0__' .. sufix .. '_light.svg')
  if info and info.w then
    div.attributes['data-amplada'] = tostring(math.floor(info.w * ESCALA + 0.5))
    return div
  end
end
