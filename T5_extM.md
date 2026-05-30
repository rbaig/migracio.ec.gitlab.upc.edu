## RISC-V RV32F (Coma Flotant de Precisió Simple)

L'extensió de coma flotant de precisió simple RV32F afegeix 32 registres de coma flotant dedicats (`f0`–`f31`), un registre de control i estat de coma flotant (`fcsr`), i un conjunt d'instruccions per a aritmètica conforme amb IEEE 754-2008. Això inclou càrregues, emmagatzematges, operacions aritmètiques, manipulacions de signe, conversions i comparacions.

El conjunt d'instruccions RV32F s'organitza en sis grups rellevants per a EC. El grup de multiplicació-addició fusionada (FMA) i la instrucció `fclass.s` queden fora de l'abast d'EC i no es tracten aquí.

---

### 1. Càrregues i emmagatzematges

Transfereixen valors de coma flotant de precisió simple (32 bits) entre memòria i registres de coma flotant. El registre de direcció base és sempre un registre enter.

**:**`flw rd, offset(rs1)`**: Carrega un valor de coma flotant de precisió simple de la direcció de memòria `rs1 + offset` al registre de coma flotant `rd`.
**:**`fsw rs2, offset(rs1)`**: Emmagatzema el valor del registre de coma flotant `rs2` a la direcció de memòria `rs1 + offset`.

 **Nota — Càrrega de constants de coma flotant**: RV32F no té instruccions amb immediat de coma flotant. Per carregar una constant com ara `1.0`, cal emmagatzemar-la a la secció `.data` i carregar-la amb `la` + `flw`:

```{.s}
.data
const_one: .float 1.0

.text
    la   t0, const_one   # Carrega l'adreça de la constant en un registre enter
    flw  ft0, 0(t0)      # Carrega 1.0 al registre de coma flotant ft0
 ```

---

### 2. Instruccions aritmètiques

Totes les instruccions aritmètiques acaben en `.s` per indicar precisió simple. No hi ha variants amb immediat; tots els operands han d'estar en registres de coma flotant.

**:**`fadd.s rd, rs1, rs2`**: Suma $rd = rs1 + rs2$
**:**`fsub.s rd, rs1, rs2`**: Resta $rd = rs1 - rs2$
**:**`fmul.s rd, rs1, rs2`**: Multiplicació $rd = rs1 \times rs2$
**:**`fdiv.s rd, rs1, rs2`**: Divisió $rd = rs1 \div rs2$
**:**`fsqrt.s rd, rs1`**: Arrel quadrada $rd = \sqrt{rs1}$
**:**`fmin.s rd, rs1, rs2`**: Valor mínim $rd = \min(rs1, rs2)$
**:**`fmax.s rd, rs1, rs2`**: Valor màxim $rd = \max(rs1, rs2)$

---

### 3. Injecció de signe i còpia de registre

Manipulen el bit de signe dels registres de coma flotant sense realitzar aritmètica.

**:**`fsgnj.s rd, rs1, rs2`**: Copia la magnitud de `rs1` i el signe de `rs2` a `rd`.
**:**`fsgnjn.s rd, rs1, rs2`**: Copia la magnitud de `rs1` i el signe invertit de `rs2` a `rd`.
**:**`fsgnjx.s rd, rs1, rs2`**: Copia la magnitud de `rs1` i la XOR dels signes de `rs1` i `rs2` a `rd`.

> **Pseudoinstrucció `fmv.s`**: La instrucció `fsgnj.s fd, fs, fs` (amb els dos registres font idèntics) copia `fs` a `fd` sense modificar el signe. RARS exposa això com la pseudoinstrucció `fmv.s fd, fs`.

Les dues instruccions següents mouen patrons de bits entre registres enters i de coma flotant **sense cap conversió**. Reinterpreten el patró de 32 bits tal qual:

**:**`fmv.w.x rd, rs1`**: Mou (copia) el registre enter `rs1` al registre de coma flotant `rd`.
**:**`fmv.x.w rd, rs1`**: Mou (copia) el registre de coma flotant `rs1` al registre enter `rd`.

---

### 4. Conversions

Converteixen entre valors de coma flotant de precisió simple i enters de 32 bits. A diferència de `fmv.w.x`/`fmv.x.w`, aquestes instruccions realitzen una conversió numèrica real.

**:**`fcvt.s.w rd, rs1`**: Converteix l'enter amb signe de 32 bits de `rs1` a coma flotant de precisió simple a `rd`.
**:**`fcvt.s.wu rd, rs1`**: Converteix l'enter sense signe de 32 bits de `rs1` a coma flotant de precisió simple a `rd`.
**:**`fcvt.w.s rd, rs1`**: Converteix el valor de coma flotant de precisió simple de `rs1` a enter amb signe de 32 bits a `rd` (trunca cap a zero).
**:**`fcvt.wu.s rd, rs1`**: Converteix el valor de coma flotant de precisió simple de `rs1` a enter sense signe de 32 bits a `rd` (trunca cap a zero).

Exemple — conversió d'`int` a `float` i de tornada:

```{.s}
# n enter és a a0; conversió a float, suma 0.5, conversió de tornada a enter
fcvt.s.w  fa0, a0          # fa0 = (float) n
la        t0, const_half
flw       ft0, 0(t0)       # ft0 = 0.5
fadd.s    fa0, fa0, ft0    # fa0 = (float) n + 0.5
fcvt.w.s  a0, fa0          # a0 = (int)(n + 0.5)  [trunca]
```

---

### 5. Comparacions

Les comparacions escriuen un resultat enter (0 o 1) a un registre **enter** `rd`. Aquest resultat es pot usar directament amb instruccions de salt enter (`beq`, `bne`).

**:**`feq.s rd, rs1, rs2`**: `rd = 1` si $rs1 = rs2$, si no `rd = 0`.
**:**`flt.s rd, rs1, rs2`**: `rd = 1` si $rs1 < rs2$, si no `rd = 0`.
**:**`fle.s rd, rs1, rs2`**: `rd = 1` si $rs1 \leq rs2$, si no `rd = 0`.

> **Comportament amb NaN**: `feq.s` retorna 0 (no igual) si algun dels operands és NaN. `flt.s` i `fle.s` també retornen 0 si algun dels operands és NaN.

Exemple — salt condicional basat en una comparació de coma flotant:

```{.s}
# if (fa0 < fa1) goto label
flt.s  t0, fa0, fa1   # t0 = 1 si fa0 < fa1
bne    t0, zero, label
```

---

### 6. Registre de control i estat de coma flotant (`fcsr`)

El `fcsr` és un CSR (registre de control i estat) de 32 bits que controla el comportament d'arrodoniment i registra els indicadors d'excepció.

| Bits   | Camp      | Descripció                                     |
| :----- | :-------- | :--------------------------------------------- |
| `31:8` | —         | Reservat (es llegeix com a 0)                  |
| `7:5`  | `frm`     | Mode d'arrodoniment                            |
| `4:0`  | `fflags`  | Indicadors d'excepció acumulats (sticky)       |

#### Modes d'arrodoniment (`frm`)

| Mnemònic | Significat                                              |
| :------- | :------------------------------------------------------ |
| `RNE`    | Arrodoneix al més proper, empats cap al parell (defecte) |
| `RTZ`    | Arrodoneix cap a zero (truncament)                      |
| `RDN`    | Arrodoneix cap avall (cap a $-\infty$)                  |
| `RUP`    | Arrodoneix cap amunt (cap a $+\infty$)                  |
| `RMM`    | Arrodoneix al més proper, empats cap a la màxima magnitud |

El mode per defecte és `RNE`, que correspon al mode per defecte d'IEEE 754.

#### Indicadors d'excepció acumulats (`fflags`)

| Bit | Mnemònic | Excepció                                                        |
| :-: | :------- | :-------------------------------------------------------------- |
| `4` | `NV`     | Operació invàlida (p. ex. $\sqrt{-1}$, $0/0$, $\infty - \infty$) |
| `3` | `DZ`     | Divisió per zero ($x/0$, $x \neq 0$)                           |
| `2` | `OF`     | Sobreeximent (exponent massa gran)                              |
| `1` | `UF`     | Subdesbordament (resultat massa petit / subnormal)              |
| `0` | `NX`     | Inexacte (el resultat s'ha arrodonit)                           |

Aquests indicadors són *sticky*: un cop activats pel maquinari, romanen actius fins que el programari els esborra. No es tracten més a EC; s'inclouen aquí per completesa.

---

## Registres de coma flotant de RISC-V i ABI (Precisió Simple)

L'ABI de coma flotant de RISC-V defineix com s'utilitzen els 32 registres de coma flotant (`f0`–`f31`) en les crides a subrutines.

### Disposició dels registres de coma flotant i noms ABI

Cada registre té una mida de 32 bits en RV32F.

| Registre      | Nom ABI       | Rol                                      | Es preserva en la crida? |
| :------------ | :------------ | :--------------------------------------- | :----------------------- |
| `f0`–`f7`     | `ft0`–`ft7`   | Temporals                                | No (caller-saved)        |
| `f8`–`f9`     | `fs0`–`fs1`   | Registres saves                          | Sí (callee-saved)        |
| `f10`–`f11`   | `fa0`–`fa1`   | Arguments / valors de retorn             | No (caller-saved)        |
| `f12`–`f17`   | `fa2`–`fa7`   | Arguments                                | No (caller-saved)        |
| `f18`–`f27`   | `fs2`–`fs11`  | Registres saves                          | Sí (callee-saved)        |
| `f28`–`f31`   | `ft8`–`ft11`  | Temporals                                | No (caller-saved)        |

### Convenció de crida

**Pas d'arguments**:

**:Fins a 8 arguments de precisió simple es passen per `fa0`–`fa7`.
**:Els arguments addicionals a partir del novè es passen per la pila.

**Valors de retorn**:

**:El valor de retorn principal va a `fa0`.
**:Un segon valor de retorn (p. ex. una estructura amb dos floats) va a `fa1`.

**Preservació de registres**:

**:**Caller-saved** (`ft0`–`ft11`, `fa0`–`fa7`): el caller ha de desar-los abans d'una crida si en necessita els valors posteriorment.
**:**Callee-saved** (`fs0`–`fs11`): el callee ha de restaurar-los abans de retornar si els ha modificat (desar-los al pròleg, restaurar-los a l'epíleg).

### Exemple de subrutina

Una subrutina fulla que calcula $f(x, y) = x \times y + 2{,}0$, usant instruccions aritmètiques bàsiques (sense FMA):

```{.s}
# --- Costat del caller ---
# Es considera que x és a fs0 i y a fs1
fmv.s   fa0, fs0            # Passa el primer argument (x) per fa0
fmv.s   fa1, fs1            # Passa el segon argument (y) per fa1
jal     ra, my_function     # Crida a la subrutina
# El resultat és ara disponible a fa0

# --- Costat de la subrutina ---
.data
const_two: .float 2.0

.text
my_function:
    # Pròleg: no s'usen registres callee-saved, res a desar

    la      t0, const_two   # Carrega l'adreça de 2.0 al registre enter t0
    flw     ft0, 0(t0)      # Carrega 2.0 al temporal ft0

    fmul.s  fa0, fa0, fa1   # fa0 = x * y
    fadd.s  fa0, fa0, ft0   # fa0 = (x * y) + 2.0

    ret                     # Retorn; el resultat és a fa0
```

---

## L'opció `-march` de GCC per a coma flotant

A EC, l'opció de referència és `-march=rv32imf`, que habilita l'ISA enter base (I), la multiplicació i divisió enteres per maquinari (M), i la coma flotant de precisió simple (F).

Les extensions `m` i `f` són independents: `f` no requereix `m`. Una opció `-march=rv32if` és vàlida i apunta a maquinari amb unitat de coma flotant però sense multiplicació/divisió entera per maquinari (el compilador emetria llavors crides a biblioteca per a `*`, `/`, `%` sobre enters). A EC sempre s'usa `-march=rv32imf`.

L'ordre canònic de les extensions estàndard en una cadena `-march` és fix:
$$\text{I} \rightarrow \text{M} \rightarrow \text{A} \rightarrow \text{F} \rightarrow \text{D} \rightarrow \text{C}$$

`rv32imf` és correcte; `rv32fmi` o `rv32fm` causarien un error del compilador.
