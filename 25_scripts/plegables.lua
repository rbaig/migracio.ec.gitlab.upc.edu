--[[
plegables.lua — Exemples i solucions plegables a l'HTML (pilot de T1, 2026-10-09).

Decisió de l'usuari (2026-10-09): «Fes T1 com a pilot» de la petició «Exemples i
solucions plegables a l'HTML» (TODO.md). Dues coses:

1. Un div `.resposta` (dins d'un exemple `#tip-`) es converteix, a l'HTML, en un
   `<details>` plegat amb el resum «Mostra la solució», perquè l'estudiant pugui
   intentar l'exemple abans de veure'n la resposta. Al PDF, el contingut queda
   igual, sense el div.
2. Cada enunciat `#exr-tN-<slug>` d'un tema pilot que té solució
   (`#sol-tN-<slug>` a `03_solucions/`) rep al final la remissió
   `@sol-tN-<slug>` («Solució N.M», amb l'enllaç), generada aquí perquè cap `.qmd` no l'hagi de
   mantenir a mà.

S'executa abans que Quarto analitzi el document (`at: pre-ast` a `_quarto.yml`):
més tard, els divs `#exr-` ja són nodes propis de Quarto, i la remissió que
s'hi afegeix l'ha de resoldre el `crossref`.
]]

local PILOT = { t1 = true }   -- temes on s'afegeix la remissió a la solució

local solucions = nil

local function carrega_solucions()
  if solucions then return end
  solucions = {}
  local dir = "."
  if quarto and quarto.project and quarto.project.directory then
    dir = quarto.project.directory
  end
  for i = 1, 9 do
    local f = io.open(dir .. "/03_solucions/S" .. i .. ".qmd", "r")
    if f then
      local text = f:read("a")
      f:close()
      for id in text:gmatch("{#(sol%-t%d+%-[%w%-]+)") do
        solucions[id] = true
      end
    end
  end
end

function Div(el)
  if el.classes:includes("resposta") then
    if quarto.doc.is_format("html") then
      local blocks = { pandoc.RawBlock("html",
        '<details class="resposta"><summary>Mostra la solució</summary>') }
      for _, b in ipairs(el.content) do table.insert(blocks, b) end
      table.insert(blocks, pandoc.RawBlock("html", "</details>"))
      return blocks
    end
    return el.content
  end

  local tema, slug = el.identifier:match("^exr%-(t%d+)%-(.+)$")
  if tema and PILOT[tema] then
    carrega_solucions()
    local sol = "sol-" .. tema .. "-" .. slug
    if solucions[sol] then
      local cite = pandoc.Cite({ pandoc.Str("@" .. sol) },
        { pandoc.Citation(sol, "NormalCitation") })
      el.content:insert(pandoc.Para({ pandoc.Emph({ cite }) }))
      return el
    end
  end
end
