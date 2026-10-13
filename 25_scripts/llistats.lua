--[[
llistats.lua — Al PDF, el nom del fitxer d'un llistat `#lst-` passa al peu.

Decisió de l'usuari (2026-10-13; D-117 del registre de decisions): als blocs de
codi s'hi remet amb `@lst-`, i només es numeren els llistats `#lst-`, als dos
formats. Un llistat és un div `::: {#lst-…}` amb el bloc de codi a dins i el peu
a l'última línia, com les figures.

Dins d'un callout, Quarto escriu el llistat com un `codelisting` (el del `#lst-`)
dins d'un altre (el del `filename` del bloc), i el bloc sortia amb dos números
(«Codi 1.6 …» i «Codi 1.7 RV32I»); fora dels callouts, en fa un de sol. Aquí el
`filename` surt del bloc i va al principi del peu, dins de `\ecfitxer{}`, que
`preamble.tex` escriu a sota de «Codi 2.3: …», com la barra del nom del fitxer de
l'HTML. A l'HTML no fa res.

S'executa abans que Quarto analitzi el document (`at: pre-ast` a `_quarto.yml`):
més tard, el div `#lst-` ja és un node propi de Quarto.
]]

if not quarto.doc.is_format("latex") then
  return {}
end

return {
  Div = function(div)
    if not div.identifier:match("^lst%-") then
      return nil
    end
    local peu = div.content[#div.content]
    if not peu or not (peu.t == "Para" or peu.t == "Plain") then
      return nil
    end
    local fitxer
    for _, bloc in ipairs(div.content) do
      if bloc.t == "CodeBlock" and bloc.attributes["filename"] then
        fitxer = bloc.attributes["filename"]
        bloc.attributes["filename"] = nil
        break
      end
    end
    if not fitxer then
      return nil
    end
    local nou = {
      pandoc.RawInline("latex", "\\protect\\ecfitxer{"),
      pandoc.Code(fitxer),
      pandoc.RawInline("latex", "}"),
    }
    for _, element in ipairs(peu.content) do
      table.insert(nou, element)
    end
    peu.content = nou
    return div
  end,
}
