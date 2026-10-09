--[[
espai_unitats.lua — Espai que no es parteix entre un nombre i la seva unitat.

13_contrib.qmd §Criteris generals («Nombres») i D-87 del registre de decisions:
entre un nombre i la unitat (o el símbol %) hi va un espai, que no es pot
partir a final de línia: «80 %», «32 bits», «4 KiB», «2 GHz». Al font s'escriu
un espai normal, que és més llegible; aquest filtre el converteix en un espai
que no es parteix (U+00A0, que l'escriptor de LaTeX escriu com a «~») quan el
precedeix un mot que acaba en xifra i el segueix una unitat de la llista. No
toca les fórmules ($…$), on l'espai s'escriu amb «\ », ni el codi.
]]

local UNITATS = {
  ["%"] = true,
  bit = true, bits = true, byte = true, bytes = true, B = true,
  KiB = true, MiB = true, GiB = true, TiB = true,
  kB = true, KB = true, MB = true, GB = true, TB = true,
  Hz = true, kHz = true, MHz = true, GHz = true,
  s = true, ms = true, ns = true, ps = true, ["µs"] = true,
  V = true, mV = true, W = true, mW = true, J = true, nF = true, pF = true,
}

-- La unitat és el començament del mot, fins al primer caràcter que no és una
-- lletra (o «%» i «µ»), de manera que «bits,», «%)» i «GB/s» també compten.
local function es_unitat(text)
  if text:sub(1, 1) == "%" then return true end
  local u = text:match("^µ%a+") or text:match("^%a+")
  return u ~= nil and UNITATS[u] == true
end

local NBSP = "\u{00A0}"

function Inlines(inl)
  for i = 1, #inl - 2 do
    local a, sep, b = inl[i], inl[i + 1], inl[i + 2]
    if a.t == "Str" and (sep.t == "Space" or sep.t == "SoftBreak") and b.t == "Str"
       and a.text:match("%d$") and es_unitat(b.text) then
      inl[i + 1] = pandoc.Str(NBSP)
    end
  end
  return inl
end
