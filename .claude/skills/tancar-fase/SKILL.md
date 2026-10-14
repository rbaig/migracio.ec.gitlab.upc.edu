---
name: tancar-fase
description: Tanca una fase del pla de treball de CLAUDE.md o una entrada del TODO.md executada: l'entrada a l'arxiu, el recompte, la fila del pla, la D-n si canvia una regla, i un sol commit amb push. La invoca l'usuari.
disable-model-invocation: true
---

# Tancar una fase

Les regles són a `CLAUDE.md` (§Pla de treball, §Flux de treball), a la capçalera de `TODO.md`, a la de `24_specs/arxiu_todo.md` (D-91 del registre de decisions) i a la del registre de decisions. Aquí només hi ha l'ordre de la feina i les comprovacions; no en copiïs cap regla.

1. **Comprova que és feta.** Cada punt de l'entrada del `TODO.md` (i de l'historial retallat, si n'hi ha) té el seu commit o la línia actual que ho mostra. El que no es troba no es dona per fet: es pregunta. Si són molts punts, un subagent (`general-purpose`, Sonnet) en fa la taula.
2. **Les declaracions de l'usuari** que hi consten («tancat», «ho dono per bo») es registren literals, no es verifiquen (D-63 del registre de decisions).
3. **L'entrada surt del `TODO.md`** i hi deixa la fila a `24_specs/arxiu_todo.md` §Entrades retirades → Executades (o Caduques per mesura, o Duplicades): títol amb la data de registre i de retirada, el motiu amb els commits, i on en queda còpia (`git show <commit d'abans>:TODO.md`). Si en queda un pendent, és una entrada nova, amb l'ordre que el mesura.
4. **El recompte de la capçalera del `TODO.md`** i el repartiment per secció, amb les dues ordres de la capçalera; el motiu del recompte diu quina entrada surt i quina entra. `comprova.py` atura el commit si no quadra.
5. **La fila de `CLAUDE.md §Pla de treball`** surt de la taula; el rang de fases fetes del paràgraf de sobre s'actualitza.
6. **El missatge del commit** porta el que abans anava a l'historial del registre (retirat a la fase 10a, D-122): la descripció que tenia la fila, les decisions de l'usuari, què s'ha verificat i amb què, les branques comprovades i què han de saber els equips de revisió.
7. **Una regla nova o canviada** porta la seva D-n (el número següent, a la secció que toca), en el mateix commit, i la guia hi enllaça.
8. **Les xifres** que publiques (al `TODO.md`, al registre, al missatge del commit) les mesures abans amb la skill `escombrada`, amb l'ordre que les reprodueix.
9. **Un sol commit i push.** Només els fitxers del tancament: si l'arbre de treball té canvis d'una altra feina, no van al commit.
