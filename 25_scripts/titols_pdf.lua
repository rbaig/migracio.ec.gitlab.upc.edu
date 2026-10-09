--[[
titols_pdf.lua — Marcadors del PDF amb els títols curts del menú de l'HTML.

Al PDF, els capítols de teoria, problemes, solucions i laboratori es diuen «Tema 1:
Introducció» o «Laboratori 1: Introducció al simulador RARS», i el llistat desplegable de
marcadors en mostrava el títol sencer. El menú de l'HTML els anomena «A1 Introducció»,
«P1 Introducció», «S1 Introducció» i «L1 RARS» (`chapters:` de `_quarto.yml`), i aquests són
els que ha de mostrar el llistat (petició de l'usuari, 2026-10-04; fins al 2026-10-09, el menú
deia «T1 …» als apunts, als problemes i a les solucions, i «S1 …» al laboratori).

El filtre embolcalla el títol de cada capítol amb `\texorpdfstring{títol}{títol curt}`:
la pàgina, l'índex i la capçalera de pàgina en fan servir el primer argument, com fins
ara, i hyperref posa el segon als marcadors. Els títols curts són els `text:` de
`_quarto.yml`, de manera que no hi ha cap llista paral·lela que mantenir: per a cada
`file:` del llibre, el filtre en llegeix l'identificador de la capçalera de nivell 1
(`# {{< var tema1 >}} {#sec-tema-introduccio}`) i hi associa el `text:` que el precedeix.
Només s'hi apliquen els títols curts de la forma «A1 …», «P1 …», «S1 …» i «L1 …»; la resta de capítols
(presentació, compendi, glossari…) no canvien.

Només actua al PDF. A `_quarto.yml` s'executa `at: post-quarto`, perquè el títol del capítol
és un shortcode (`{{< var tema1 >}}`) fins que Quarto no el resol: abans, el títol llarg que
el filtre escriu al LaTeX cru sortia buit.
]]

if not quarto.doc.is_format('pdf') then
  return {}
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

-- identificador de la capçalera de nivell 1 → títol curt
local curts = {}
do
  local config = llegeix('_quarto.yml') or ''
  local text
  for linia in config:gmatch('[^\n]+') do
    local t = linia:match('^%s*%-%s*text:%s*"(.-)"%s*$')
    if t then
      text = t
    else
      local fitxer = linia:match('^%s*file:%s*(%S+)%s*$')
      if fitxer then
        if text and text:match('^[APSL]%d ') then
          local font = llegeix(fitxer)
          local id = font and (('\n' .. font):match('\n# [^\n]-{#([%w%-]+)'))
          if id then curts[id] = text end
        end
        text = nil
      end
    end
  end
end

function Header(h)
  if h.level ~= 1 then return nil end
  local curt = curts[h.identifier]
  if not curt then return nil end
  local primer = h.content[1]
  if primer and primer.t == 'RawInline' and primer.text:match('^\\texorpdfstring{') then
    return nil   -- ja fet, si el filtre hi passés dues vegades
  end
  -- Pandoc ja embolcalla amb \texorpdfstring{LaTeX}{text pla} tot títol que porti LaTeX cru,
  -- i el text pla és el del títol sense el LaTeX cru. Per això el títol llarg va dins del
  -- LaTeX cru i el curt, com a text: el text pla del títol és llavors el curt, i el resultat,
  -- \texorpdfstring{\texorpdfstring{llarg}{curt}}{curt}, dona el llarg a la pàgina, l'índex i
  -- la capçalera i el curt als marcadors.
  local llarg = pandoc.write(pandoc.Pandoc({ pandoc.Plain(h.content) }), 'latex'):gsub('%s+$', '')
  h.content = pandoc.List({
    pandoc.RawInline('latex', '\\texorpdfstring{' .. llarg .. '}{'),
    pandoc.Str(curt),
    pandoc.RawInline('latex', '}'),
  })
  return h
end
