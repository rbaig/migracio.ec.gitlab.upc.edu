--[[
versio.lua — El commit renderitzat, al costat de la data de publicació.

Petició de l'usuari (2026-10-02): el hash curt del commit, entre parèntesis, després de la
data de «Publicat» de l'HTML i a la portada del PDF, amb «-dirty» si l'arbre té canvis no
confirmats. Així qui llegeix una còpia sap de quin estat del repositori surt.

El hash el dona `git describe --always --dirty --abbrev=7 --exclude='*'`: `--exclude='*'`
fa que no hi surti cap etiqueta (les de `revisio-externa/…`, si n'hi ha), només el hash. Si
no hi ha git o el directori no és un clon, el filtre no fa res i la data surt sola.

- HTML: la data només és a la portada (`index.qmd`), en un `<p class="date">` que Quarto
  formata a partir de `book.date`; el filtre hi afegeix el hash amb un fragment de JavaScript
  al final de la pàgina, perquè el text de la data no passa pel document de Pandoc.
- PDF: defineix `\eccommit` al preàmbul, i `preamble.tex` el posa a `\date{}`.

S'executa des de qualsevol camí de render (`make render`, `make render-complet`, `quarto
render` i el CI), perquè és un filtre de `_quarto.yml` i no un pas del Makefile.
]]

local function arrel()
  return (quarto.project and quarto.project.directory) or os.getenv('QUARTO_PROJECT_DIR') or '.'
end

local function commit()
  local p = io.popen('git -C "' .. arrel() .. '" describe --always --dirty --abbrev=7 --exclude="*" 2>/dev/null')
  if not p then return nil end
  local h = p:read('l')
  p:close()
  if h and h:match('^%x+') then return h end
  return nil
end

function Meta(meta)
  if quarto.doc.is_format('html') then
    local entrada = (quarto.doc.input_file or ''):gsub('\\', '/')
    if not entrada:match('/index%.qmd$') and entrada ~= 'index.qmd' then return nil end
    local h = commit()
    if not h then return nil end
    quarto.doc.include_text('after-body',
      '<script>document.querySelectorAll("p.date").forEach(function (p) {'
      .. ' p.textContent = p.textContent.trim() + " (' .. h .. ')"; });</script>')
  elseif quarto.doc.is_format('pdf') then
    local h = commit()
    if not h then return nil end
    quarto.doc.include_text('in-header', '\\newcommand{\\eccommit}{' .. h .. '}')
  end
  return nil
end
