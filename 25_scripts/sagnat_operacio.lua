--[[
sagnat_operacio.lua — Al PDF, sagnat francès a la columna «Operació» de les taules.

Petició de l'usuari (2026-10-12; D-109 del registre de decisions): a les taules
d'instruccions dels callouts RISC-V (`#nte-`) i del compendi, la descripció de
l'operació ($rd \leftarrow rs1 + SignExt(imm12)$) es parteix en dues línies
quan no hi cap, i la segona començava arran de la primera. El filtre posa
`\hangindent` a cada cel·la de la columna amb capçalera «Operació», de manera
que les línies de continuació van sagnades. A l'HTML no fa res: el navegador
no parteix la fórmula.
]]

local SAGNAT = "\\hangindent=1em\\hangafter=1 "

local function columna(tbl)
  local cap = tbl.head.rows[1]
  if not cap then return nil end
  for k, cel in ipairs(cap.cells) do
    if pandoc.utils.stringify(cel.contents) == "Operació" then return k end
  end
  return nil
end

function Table(tbl)
  if not FORMAT:match("latex") then return nil end
  local k = columna(tbl)
  if not k then return nil end
  for _, cos in ipairs(tbl.bodies) do
    for _, fila in ipairs(cos.body) do
      local cel = fila.cells[k]
      local primer = cel and cel.contents[1]
      if primer and (primer.t == "Plain" or primer.t == "Para") then
        primer.content:insert(1, pandoc.RawInline("latex", SAGNAT))
      end
    end
  end
  return tbl
end
