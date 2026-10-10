--[[
continguts.lua — Índex dels apunts (A1–A9) a l'HTML, com el del PDF (D-101).

Petició de l'usuari (2026-10-09): «Té sentit a la versió HTML afegir un índex de continguts
per poder tenir una visió general? (com en el PDF)». A l'HTML, la barra lateral només mostra
els capítols, i la «Taula de continguts» de cada pàgina, les seccions del capítol obert: cap
vista no mostrava les seccions de tots els temes alhora. Decisions de l'usuari: només els
apunts (A1–A9), fins a `###`, i en una pàgina pròpia entre «👋 Presentació» i «Apunts»,
`10_continguts.qmd` («📑 Continguts»).

A l'HTML, el filtre substitueix el div `#continguts-llista` de `10_continguts.qmd` per
l'índex. Per a cada capítol de `01_apunts/` dels `chapters:` de `_quarto.yml`, en l'ordre del
llibre: una capçalera `##` amb el número i el títol del capítol, i la llista de les seves
seccions `##` i `###`, amb el número que els dona l'HTML i l'enllaç a la seva àncora. Els
títols i els enllaços surten dels `.qmd`: no hi ha cap llista que mantenir a mà. Les
capçaleres dels capítols queden al primer nivell del document, perquè Pandoc només posa a la
«Taula de continguts» de la pàgina les capçaleres que no són dins d'un div.

Hi compten les mateixes capçaleres que a la «Taula de continguts» de cada pàgina: les del
primer nivell del document; les de dins dels callouts en són el títol, i les de dins d'un
altre div no hi surten. La numeració és la de Quarto: el capítol, pel lloc que ocupa entre
els capítols numerats del llibre, i les seccions, per ordre dins del capítol; una capçalera
`.unnumbered` no porta número ni en consumeix, i una `.unlisted` no hi surt. Els títols dels
capítols són un shortcode (`{{< var tema1 >}}`), que el filtre resol amb `_variables.yml`.

Al PDF, el filtre treu la capçalera `#continguts` i el div: el PDF ja té el seu índex, i la
pàgina no hi ha de deixar res. Embolcallar-la amb `.content-visible when-format="html"` no
n'hi ha prou, perquè Quarto en treu el títol del capítol i el PDF rebia igualment
`\chapter*{…}`, la línia de l'índex i el marcador (comprovat el 2026-10-09).
]]

if not quarto.doc.is_format('html') then
  return {
    Header = function(h)
      if h.identifier == 'continguts' then return {} end
    end,
    Div = function(d)
      if d.identifier == 'continguts-llista' then return {} end
    end,
  }
end

local function arrel()
  return (quarto.project and quarto.project.directory) or os.getenv('QUARTO_PROJECT_DIR') or '.'
end

local function llegeix(ruta)
  local f = io.open(arrel() .. '/' .. ruta, 'r')
  if not f then return nil end
  local s = f:read('a')
  f:close()
  return s
end

local function variables()
  local v = {}
  for linia in (llegeix('_variables.yml') or ''):gmatch('[^\n]+') do
    local clau, valor = linia:match('^([%w_]+):%s*"(.-)"')
    if clau then v[clau] = valor end
  end
  return v
end

-- Enllaç amb el número al davant del títol («1.4 Codificació…»); sense número, si no en té
local function enllac(numero, contingut, desti)
  local text = pandoc.List()
  if numero then text:extend({ pandoc.Str(numero), pandoc.Space() }) end
  text:extend(contingut)
  return pandoc.Link(text, desti)
end

-- Capçalera del capítol i llista de les seves seccions `##` i `###`
local function capitol(fitxer, font, numero)
  local doc = pandoc.read(font, 'markdown')
  local blocs = pandoc.List()
  local seccions = pandoc.List()
  local n2, n3 = 0, 0
  for _, b in ipairs(doc.blocks) do
    if b.t == 'Header' and b.level <= 3 then
      local numerada = not b.classes:includes('unnumbered')
      local llistada = not b.classes:includes('unlisted')
      local num
      if b.level == 1 then
        local id = 'continguts-' .. b.identifier:gsub('^sec%-', '')
        blocs:insert(pandoc.Header(2, { enllac(tostring(numero), b.content, fitxer) },
          pandoc.Attr(id, { 'continguts' })))
      elseif b.level == 2 then
        if numerada then n2, n3 = n2 + 1, 0; num = numero .. '.' .. n2 end
        if llistada then
          seccions:insert({ capcalera = b, num = num, subseccions = pandoc.List() })
        end
      elseif #seccions > 0 then
        if numerada then n3 = n3 + 1; num = numero .. '.' .. n2 .. '.' .. n3 end
        if llistada then
          seccions[#seccions].subseccions:insert({ capcalera = b, num = num })
        end
      end
    end
  end
  local function element(s)
    return pandoc.Plain({ enllac(s.num, s.capcalera.content, fitxer .. '#' .. s.capcalera.identifier) })
  end
  local items = pandoc.List()
  for _, s in ipairs(seccions) do
    local item = pandoc.List({ element(s) })
    if #s.subseccions > 0 then
      item:insert(pandoc.BulletList(s.subseccions:map(function(ss) return { element(ss) } end)))
    end
    items:insert(item)
  end
  if #items > 0 then
    blocs:insert(pandoc.Div(pandoc.BulletList(items), pandoc.Attr('', { 'continguts' })))
  end
  return blocs
end

function Div(el)
  if el.identifier ~= 'continguts-llista' then return nil end
  local vars = variables()
  local blocs = pandoc.List()
  local numero = 0
  for linia in (llegeix('_quarto.yml') or ''):gmatch('[^\n]+') do
    local fitxer = linia:match('^%s*file:%s*(%S+)%s*$')
    local font = fitxer and llegeix(fitxer)
    if font then
      local h1 = ('\n' .. font):match('\n# ([^\n]*)')
      if h1 and not h1:match('%.unnumbered') and not h1:match('{%-') then
        numero = numero + 1
      end
      if fitxer:match('^01_apunts/') then
        font = font:gsub('{{<%s*var%s+([%w_]+)%s*>}}', vars)
        blocs:extend(capitol(fitxer, font, numero))
      end
    end
  end
  return blocs
end
