# Inventari de figures

Generat per `25_scripts/inventari_figures.py` sobre `722c522` (2026-10-03). **No l'editeu a mà**: `make inventari` el regenera. Les comprovacions, i què vol dir cada columna, són a la capçalera de l'script.

- **78** etiquetes `#fig-` (75 amb imatge; la resta són taules Markdown), i **9** imatges sense etiqueta (les del compendi i la de la llicència).
- **92** fitxers a `22_figs_originals/` i `23_figs_externes/`: 59 consumits i 33 orfes. A més, **18** figures generades per `gen_regs.py`.

## Figures

| Etiqueta | Lloc | Font | Origen | Callout | @ | Peu | `<desc>` |
| :--- | :--- | :--- | :--- | :--- | ---: | :--- | :--- |
| `fig-flux-compilacio` | `A1.qmd:55` | `22_figs_originals/T1_flux_compilacio.svg` | Inkscape |  | 1 | El flux de generació del programari: les quatre etapes del *toolchain* GCC. | Diagrama que mostra el flux de generació d'un programa exec… |
| `fig-picopi-fases` | `A1.qmd:224` | `22_figs_originals/T1_picopi_fases.svg` | Inkscape | `wrn-picopi` | 0 | Configuració física i fases d'ús del conjunt Host + Sonda (*Pi Debug Probe*) + Target (*P… | Quatre diagrames en una sola figura: fase de creació (el ho… |
| `fig-von-neumann` | `A1.qmd:358` | `22_figs_originals/T1_von_neumann.svg` | Inkscape |  | 0 | Arquitectura de Von Neumann: CPU (ALU, CU i Registres), Memòria principal i Sistema d'E/S… | CPU, Memòria Principal i Sistema d'E/S en disposició horitz… |
| `fig-compendi-registres` | `A2.qmd:265` | `registres.toml:compendi_registres_RIS` | gen_regs.py (COMPENDIS) | `nte-instruccions-tipus` | 0 | Formats d'instrucció RV32I (tipus R, I i S). | Formats d'instrucció R, I i S de RISC-V RV32I en un sol dia… |
| `fig-memoria-creix-avall` | `A2.qmd:965` | `(taula Markdown)` | — | `imp-adrecament-a-nivell-byte` | 0 | Representació gràfica de la memòria. |  |
| `fig-big-endian` | `A2.qmd:1004` | `(taula Markdown)` | — | `tip-endianness` | 0 | Big-endian |  |
| `fig-little-endian` | `A2.qmd:1014` | `(taula Markdown)` | — | `tip-endianness` | 0 | Little-endian |  |
| `fig-endianness-regla-pi` | `A2.qmd:1036` | `22_figs_originals/T2_endianness_regla_pi.svg` | Inkscape | `wrn-endianness-regla-pi` | 0 | Regla mnemotècnica de la lletra grega pi (Π) per recordar l'ordenació dels bytes Little-e… |  |
| `fig-typeR` | `A2.qmd:1184` | `registres.toml:T2_instruccio_tipus_R` | gen_regs.py | `nte-instruccions-Tipus-R` | 0 | Format d'instrucció tipus R, registre (RV32I). | funct7(31–25), rs2(24–20), rs1(19–15), funct3(14–12), rd(11… |
| `fig-typeI` | `A2.qmd:1246` | `registres.toml:T2_instruccio_tipus_I` | gen_regs.py | `nte-instruccions-Tipus-I` | 0 | Format d'instrucció tipus I, immediat (RV32I). | imm[11:0](31–20), rs1(19–15), funct3(14–12), rd(11–7), opco… |
| `fig-typeU` | `A2.qmd:1270` | `registres.toml:T2_instruccio_tipus_U` | gen_regs.py | `nte-format-u` | 0 | Format d'instrucció tipus U, immediat superior (RV32I). | imm[31:12](31–12), rd(11–7), opcode(6–0). |
| `fig-typeS` | `A2.qmd:1329` | `registres.toml:T2_instruccio_tipus_S` | gen_regs.py | `nte-instruccions-Tipus-S` | 0 | Format d'instrucció tipus S, *store* (RV32I). | imm[11:5](31–25), rs2(24–20), rs1(19–15), funct3(14–12), im… |
| `fig-acces-vector` | `A2.qmd:1902` | `22_figs_originals/T2_acces_vector.svg` | SVG natiu | `tip-load-store-word` | 0 | Accés a un element d'un vector. |  |
| `fig-typeB` | `A3.qmd:401` | `registres.toml:T3_instruccio_tipus_B` | gen_regs.py | `nte-format-b` | 0 | Format d'instrucció tipus B, *branch* (RV32I). | imm[12,10:5](31–25), rs2(24–20), rs1(19–15), funct3(14–12),… |
| `fig-typeJ` | `A3.qmd:509` | `registres.toml:T3_instruccio_tipus_J` | gen_regs.py | `nte-format-j` | 0 | Format d'instrucció tipus J, *jump* (RV32I). | imm[20,10:1,11,19:12](31–12), rd(11–7), opcode(6–0). |
| `fig-mapa-memoria` | `A3.qmd:1023` | `22_figs_originals/T3_mapa_memoria.svg` | Inkscape |  | 0 | Mapa de memòria de RARS: regions `.text`, `.data`, heap i pila, amb les adreces d'inici d… |  |
| `fig-func-uninivell-pila` | `A3.qmd:1384` | `22_figs_originals/T3_func_uninivell_pila.svg` | SVG natiu | `tip-func-uninivell-bloc-activacio` | 0 | Evolució de l'`sp` durant la crida i retorn de `funcB`. Reserva i alliberament del BA (de… |  |
| `fig-ba-general` | `A3.qmd:1425` | `22_figs_originals/T3_ba_general.svg` | Inkscape |  | 0 | Estructura general del bloc d'activació: variables locals al cim de la pila i registres d… |  |
| `fig-ba-func` | `A3.qmd:1454` | `22_figs_originals/T3_ba_func.svg` | Inkscape | `tip-exemple-variables-pila` | 0 | Bloc d'activació de la funció `func`: el vector `v` ocupa els bytes 0–9, l'alineació ocup… |  |
| `fig-pila-crides-aniuades` | `A3.qmd:1505` | `22_figs_originals/T3_pila_crides_aniuades.svg` | SVG natiu | `tip-exemple-pila-multinivell` | 0 | Evolució de la pila durant les crides aniuades de `funcA` i `funcB`. El registre `sp` dec… |  |
| `fig-deps-multi` | `A3.qmd:1616` | `22_figs_originals/T3_deps_multi.svg` | SVG natiu | `tip-exemple-multi` | 0 | Dependències de dades de la subrutina `multi`. La línia de punts separa el codi anterior … |  |
| `fig-ba-multi` | `A3.qmd:1639` | `22_figs_originals/T3_ba_multi.svg` | Inkscape | `tip-exemple-multi` | 0 | Bloc d'activació de la subrutina `multi`: 12 bytes amb `s0`, `s1` i `ra` desats als offse… |  |
| `fig-deps-exemple` | `A3.qmd:1713` | `22_figs_originals/T3_deps_exemple.svg` | SVG natiu | `tip-exemple-exemple` | 0 | Dependències de dades de la subrutina `exemple`. Les línies de punts separen el codi ante… |  |
| `fig-ba-exemple` | `A3.qmd:1756` | `22_figs_originals/T3_ba_exemple.svg` | Inkscape | `tip-exemple-exemple` | 0 | Bloc d'activació de la subrutina `exemple`: variables locals `q`, `v` i `w` als offsets `… |  |
| `fig-compilacio-separada` | `A3.qmd:1854` | `22_figs_originals/T3_compilacio_separada.svg` | Inkscape |  | 0 | Flux de compilació separada: cada mòdul es compila i assembla independentment generant un… | Diagrama que mostra el flux de compilació separada: p1.c i … |
| `fig-flux-gcc-complet` | `A3.qmd:2048` | `22_figs_originals/T3_flux_gcc_complet.svg` | SVG natiu | `wrn-flux-gcc-complet` | 0 | El flux de generació complet. | Diagrama del flux complet de generació d'un executable amb … |
| `fig-semisumador-sumador-complet` | `A4.qmd:77` | `22_figs_originals/T4_semisumador_sumador_complet.svg` | script (gen_T4_sumador.py) | `wrn-sobreeiximent-maquinari` | 1 | Semisumador i sumador complet: (a) el semisumador, amb una XOR per al bit de suma i una A… | (a) Semisumador: una porta XOR dona el bit de suma s = a xo… |
| `fig-sumador-propagacio-rossec` | `A4.qmd:94` | `22_figs_originals/T4_sumador_propagacio_rossec.svg` | script (gen_T4_sumador.py) | `wrn-sobreeiximent-maquinari` | 1 | Sumador de $n$ bits amb propagació del ròssec. El ròssec avança de dreta a esquerra, del … | Cadena de n sumadors complets, del bit de més pes (n-1, a l… |
| `fig-multiplicador-sequencial` | `A4.qmd:187` | `22_figs_originals/T4_multiplicador_sequencial.svg` | SVG natiu |  | 0 | Circuit multiplicador seqüencial. | Esquema del circuit multiplicador seqüencial: el registre M… |
| `fig-multiplicador-arbre` | `A4.qmd:249` | `22_figs_originals/T4_multiplicador_arbre.svg` | SVG natiu | `wrn-circuit-multiplicacio-combinacional` | 0 | Circuit multiplicador combinacional en arbre. | Esquema d'un multiplicador combinacional en arbre: els prod… |
| `fig-divisor-sequencial` | `A4.qmd:391` | `22_figs_originals/T4_divisor_sequencial.svg` | SVG natiu |  | 0 | Circuit divisor seqüencial amb restauració. | Esquema del circuit divisor seqüencial amb algorisme de res… |
| `fig-matriu-emmagatzematge` | `A4.qmd:518` | `22_figs_originals/T4_matriu_emmagatzematge.svg` | SVG natiu |  | 0 | Emmagatzematge de `mat[4][6]` en memòria per files. | Diagrama que mostra com una matriu mat[4][6] s'emmagatzema … |
| `fig-matriu-offset-ij` | `A4.qmd:559` | `22_figs_originals/T4_matriu_offset_ij.svg` | SVG natiu |  | 0 | Càlcul de l'adreça de `mat[i][j]`. | Diagrama que mostra com l'adreça de mat[i][j] es descompon … |
| `fig-matriu-recorreguts-strides` | `A4.qmd:846` | `22_figs_originals/T4_matriu_recorreguts_strides.svg` | SVG natiu |  | 0 | Recorreguts de matrius, `mat[4][5]` a dalt i `mat[4][4]` a baix, i els strides correspone… | Quatre diagrames mostrant els patrons de recorregut: una fi… |
| `fig-ieee754-format` | `A5.qmd:83` | `registres.toml:T5_ieee754_format_registre` | gen_regs.py |  | 0 | Disposició dels camps S, E i F en el format IEEE 754 de precisió simple (32 bits). | S(31), E(30–23), F(22–0). |
| `fig-exponent-ieee754` | `A5.qmd:132` | `22_figs_originals/T5_exponent.svg` | Inkscape |  | 1 | Correspondència entre l'exponent emmagatzemat $E_u$ (0–255) i l'exponent real $e = E_u - … |  |
| `fig-recta-global` | `A5.qmd:267` | `22_figs_originals/T5_recta_global.svg` | SVG natiu |  | 1 | Recta de la coma flotant IEEE 754 (precisió simple): $\pm\infty$ i NaN als extrems ($E=25… |  |
| `fig-taula-codificacions` | `A5.qmd:341` | `22_figs_originals/T5_taula_codificacions.svg` | exportació LO Draw |  | 0 | Mapa de codificacions IEEE 754 de precisió simple: els eixos $E$ i $F$ determinen unívoca… |  |
| `fig-recta-zoom-zero` | `A5.qmd:382` | `22_figs_originals/T5_recta_zoom_zero.svg` | Inkscape |  | 1 | Zoom al voltant del zero: $\pm 0$ i els denormals ($E=0$) omplen el buit entre el zero i … |  |
| `fig-grs-esquema` | `A5.qmd:432` | `22_figs_originals/T5_grs_esquema.svg` | SVG natiu |  | 0 | Esquema dels bits de guarda ($G$), arrodoniment ($R$) i *sticky* ($S$) respecte de la man… | Mantissa retinguda seguida dels tres bits descartats G, R i… |
| `fig-fcsr` | `A5.qmd:751` | `registres.toml:T5_fcsr` | gen_regs.py | `nte-fcsr` | 0 | Camps del registre `fcsr` (RV32F). | Reservat(31–8), RM(7–5), NV(4), DZ(3), OF(2), UF(1), NX(0). |
| `fig-format-r4` | `A5.qmd:876` | `registres.toml:T5_instruccio_tipus_R4` | gen_regs.py | `wrn-instruccions-fusionades` | 1 | Format d'instrucció R4 (RV32F), el de les instruccions fusionades. | fs3(31–27), funct2(26–25), fs2(24–20), fs1(19–15), funct3(1… |
| `fig-tc-tc-prima` | `A6.qmd:146` | `22_figs_originals/T6_tc_tc_prima.svg` | extreta de PDF | `tip-augment-freq` | 0 | Mateixos components, diferents temps de cicle. |  |
| `fig-amdahl` | `A6.qmd:214` | `22_figs_originals/T6_amdahl.svg` | extreta de PDF |  | 1 | Temps total del programa original dividit en una part optimitzada (fracció $P_{x}$) i una… |  |
| `fig-not-cmos` | `A6.qmd:287` | `22_figs_originals/T6_not_cmos.svg` | extreta de PDF | `wrn-RC` | 1 | Porta NOT, representació funcional i implementació amb CMOS. |  |
| `fig-not-1-0` | `A6.qmd:306` | `22_figs_originals/T6_not_1_0.svg` | extreta de PDF | `wrn-RC` | 1 | Evolució temporal de la tensió de sortida de la porta NOT quan el valor lògic de l'entrad… |  |
| `fig-not-0-1` | `A6.qmd:323` | `22_figs_originals/T6_not_0_1.svg` | extreta de PDF | `wrn-RC` | 1 | Evolució temporal de la tensió de sortida de la porta NOT quan el valor lògic de l'entrad… |  |
| `fig-gap-processador-memoria` | `A7.qmd:31` | `22_figs_originals/T7_gap_processador_memoria.svg` | SVG natiu |  | 1 | Evolució del rendiment relatiu de processadors i memòria DRAM entre 1980 i 2010 (escala l… | Gràfica de línies amb escala logarítmica que mostra la dive… |
| `fig-jerarquia-piramide` | `A7.qmd:96` | `22_figs_originals/T7_jerarquia_piramide.svg` | SVG natiu |  | 0 | La jerarquia de memòria: cada nivell conserva les dades del nivell inferior que tinguin m… | Diagrama en forma de piràmide de quatre nivells: registres,… |
| `fig-mc-organitzacio` | `A7.qmd:142` | `22_figs_originals/T7_mc_organitzacio.svg` | SVG natiu |  | 0 | Organització interna d'una memòria cau de quatre línies. Cada línia conté un bit de valid… | Taula d'una memòria cau amb 4 línies, mostrant les columnes… |
| `fig-mc-encert` | `A7.qmd:205` | `22_figs_originals/T7_mc_encert.svg` | Inkscape |  | 0 | Encert en un accés a l'adreça `0x100100F8`: la dada es transfereix directament de la MC a… | Diagrama que mostra el flux d'un encert de memòria cau: la … |
| `fig-mc-fallada` | `A7.qmd:228` | `22_figs_originals/T7_mc_fallada.svg` | Inkscape |  | 0 | Fallada en un accés a l'adreça `0x100100F8`: el bloc es copia de la MP a la MC i la dada … | Diagrama que mostra els quatre passos d'una fallada de memò… |
| `fig-cd-descomposicio-bits` | `A7.qmd:266` | `22_figs_originals/T7_cd_descomposicio_bits.svg` | Inkscape |  | 0 | Descomposició dels bits d'una adreça en etiqueta, índex i offset per a una memòria cau de… | Descomposició dels 32 bits de l'adreça 0x100100F8 en etique… |
| `fig-cd-diagrama` | `A7.qmd:300` | `23_figs_externes/T7_cd_diagrama.svg` | exportació LO Draw |  | 1 | Diagrama de blocs d'una lectura en una memòria cau de correspondència directa. |  |
| `fig-assoc-conjunts-taula` | `A7.qmd:343` | `22_figs_originals/T7_assoc_conjunts_taula.svg` | Inkscape |  | 0 | Organització d'una memòria cau associativa per conjunts de 4 conjunts i 3 vies: el bloc d… | Estructura d'una MC associativa per conjunts de 4 conjunts … |
| `fig-assoc-conjunts-diagrama` | `A7.qmd:362` | `23_figs_externes/T7_assoc_conjunts_diagrama.svg` | exportació LO Draw |  | 1 | Diagrama de blocs d'una lectura en una memòria cau associativa per conjunts de $N$ vies. |  |
| `fig-ca-diagrama` | `A7.qmd:393` | `22_figs_originals/T7_ca_diagrama.svg` | Inkscape |  | 1 | Diagrama de blocs d'una lectura en una memòria cau completament associativa: cal comparar… | Tres diagrames en una sola figura: configuració física (Hos… |
| `fig-lru-exemple` | `A7.qmd:460` | `22_figs_originals/T7_lru_exemple.svg` | Inkscape | `tip-lru-exemple` | 0 | Evolució de la memòria cau associativa per conjunts de 2 vies amb algorisme LRU per a la … | Seqüència de 5 Load des d'una MC inicialment buida. Misses … |
| `fig-escriptura-dirty-bit` | `A7.qmd:492` | `22_figs_originals/T7_escriptura_dirty_bit.svg` | Inkscape |  | 0 | Estructura d'una línia de memòria cau amb escriptura retardada: el bit de modificació $D$… | Taula d'una memòria cau amb 4 línies, mostrant les columnes… |
| `fig-escriptura-estat-inicial` | `A7.qmd:551` | `22_figs_originals/T7_escriptura_estat_inicial.svg` | Inkscape |  | 0 | Estat de la memòria cau al final de la seqüència inicial de 5 lectures, partint d'una MC … | Seqüència de 5 Load des d'una MC inicialment buida. Misses … |
| `fig-escriptura-immediata-assignacio` | `A7.qmd:574` | `22_figs_originals/T7_escriptura_immediata_amb_assignacio.svg` | Inkscape | `tip-escriptura-immediata-assignacio` | 0 | Escriptura immediata amb assignació: en cas d'encert s'escriu a MC i MP simultàniament; e… | Write-through amb write-allocate. Accés 1 (Store byte 10): … |
| `fig-escriptura-immediata-sense-assignacio` | `A7.qmd:598` | `22_figs_originals/T7_escriptura_immediata_sense_assignacio.svg` | Inkscape | `tip-escriptura-immediata-sense-assignacio` | 0 | Escriptura immediata sense assignació: en cas d'encert s'escriu a MC i MP; en cas de fall… | Write-through sense write-allocate. Hit: escriu en MP i MC.… |
| `fig-escriptura-retardada` | `A7.qmd:623` | `22_figs_originals/T7_escriptura_retardada.svg` | Inkscape | `tip-escriptura-retardada` | 0 | Escriptura retardada amb assignació: en cas d'encert s'escriu únicament a la MC i es posa… | Write-back amb write-allocate. Mostra el bit dirty (D) i el… |
| `fig-mc-politiques-resum` | `A7.qmd:643` | `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` | Graphviz |  | 1 | Resum de les polítiques de memòria cau. |  |
| `fig-texe-diagrama` | `A7.qmd:783` | `22_figs_originals/T7_texe_diagrama.svg` | Inkscape |  | 1 | Impacte d'una fallada de memòria cau en el temps d'execució: els cicles de penalització s… | Tres diagrames en una sola figura: configuració física (Hos… |
| `fig-conflicte-exemple` | `A7.qmd:863` | `22_figs_originals/T7_conflicte_exemple.svg` | Inkscape |  | 0 | Fallades de conflicte en el recorregut paral·lel de dos vectors amb una memòria cau de co… | Figura 6.28. Els arrays A i B mapegen al mateix conjunt (ín… |
| `fig-capacitat-exemple-bucle-primera-passada` | `A7.qmd:900` | `22_figs_originals/T7_capacitat_exemple_bucle_primera_passada.svg` | Inkscape |  | 0 | Fallades de capacitat — primera passada ($i=0\ldots6$): Cold Miss fins que la MC queda pl… | Primera passada del bucle sobre V[0..15]. Cold Miss i Hits … |
| `fig-capacitat-exemple-bucle-segona-passada` | `A7.qmd:915` | `22_figs_originals/T7_capacitat_exemple_bucle_segona_passada.svg` | Inkscape |  | 0 | Fallades de capacitat — segona passada: Cold Miss continuades ($i=7\ldots15$) i Capacity … | Continuació: Cold Miss fins omplir la MC amb blocs 4-7, i C… |
| `fig-i9-13900k-die` | `A7.qmd:1002` | `23_figs_externes/T7_Intel_Core_i9-13900K_Labelled_Die_Shot_800x368.jpg` | ràster |  | 1 | Fotografia del dau (bloc de sil·lici, *die*) de l'Intel Core i9-13900K (*Raptor Lake*, 20… |  |
| `fig-mv-flux-traduccio` | `A8.qmd:267` | `22_figs_originals/T8_mv_flux_traduccio.svg` | Inkscape |  | 1 | Flux complet de traducció d'una adreça en un sistema amb TLB i memòria virtual. | Tres diagrames en una sola figura: configuració física (Hos… |
| `fig-ei-mcause` | `A9.qmd:112` | `registres.toml:T9_mcause` | gen_regs.py | `nte-mcause-mes-rellevants` | 0 | Camps del registre `mcause` (Int. = Interrupt). | Int.(31) [Interrupt]: 1=interrupció, 0=excepció. Exception … |
| `fig-ei-mepc` | `A9.qmd:145` | `registres.toml:T9_mepc` | gen_regs.py | `nte-mepc` | 0 | Camps del registre `mepc`. | El registre mepc (32 bits) conté l'adreça de la instrucció … |
| `fig-ei-mstatus` | `A9.qmd:167` | `registres.toml:T9_mstatus` | gen_regs.py | `nte-mstatus` | 0 | Camps del registre `mstatus` (RV32). | SD(31), WPRI(30–23), TSR(22), TW(21), TVM(20), MXR(19), SUM… |
| `fig-ei-mtvec` | `A9.qmd:193` | `registres.toml:T9_mtvec` | gen_regs.py | `nte-mtvec` | 0 | Camps del registre `mtvec`. | base(31–2): adreça base del gestor. mode(1–0): 0=directe, 1… |
| `fig-ei-mip` | `A9.qmd:239` | `registres.toml:T9_mip` | gen_regs.py | `nte-mip-mie` | 0 | Camps del registre `mip`. | MEIP(11), SEIP(9), MTIP(7), STIP(5), MSIP(3), SSIP(1); rest… |
| `fig-ei-mie` | `A9.qmd:254` | `registres.toml:T9_mie` | gen_regs.py | `nte-mip-mie` | 0 | Camps del registre `mie`. | MEIE(11), SEIE(9), MTIE(7), STIE(5), MSIE(3), SSIE(1); rest… |
| `fig-cicle-interrupcio` | `A9.qmd:730` | `22_figs_originals/T9_cicle_interrupcio.svg` | Inkscape |  | 0 | Cicle de vida d'una interrupció: el dispositiu fa la petició mentre s'executa la instrucc… |  |
| `fig-ei-satp` | `A9.qmd:819` | `registres.toml:T9_satp` | gen_regs.py | `nte-satp` | 0 | Camps del registre `satp` en mode SV32. | MODE(31): activa la traducció. ASID(30–22): identificador d… |
| `—` | `11_riscv.qmd:40` | `registres.toml:compendi_registres` | gen_regs.py (COMPENDIS) | `nte-rv-instruccions-formats-detall` | 0 |  |  |
| `—` | `11_riscv.qmd:270` | `registres.toml:T5_fcsr` | gen_regs.py | `nte-rv-fcsr` | 0 |  |  |
| `—` | `11_riscv.qmd:418` | `registres.toml:T9_mepc` | gen_regs.py | `nte-rv-mepc` | 0 |  |  |
| `—` | `11_riscv.qmd:436` | `registres.toml:T9_mstatus` | gen_regs.py | `nte-rv-mstatus` | 0 |  |  |
| `—` | `11_riscv.qmd:454` | `registres.toml:T9_mtvec` | gen_regs.py | `nte-rv-mtvec` | 0 |  |  |
| `—` | `11_riscv.qmd:472` | `registres.toml:T9_mip` | gen_regs.py | `nte-rv-mip-mie` | 0 |  |  |
| `—` | `11_riscv.qmd:484` | `registres.toml:T9_mie` | gen_regs.py | `nte-rv-mip-mie` | 0 |  |  |
| `—` | `11_riscv.qmd:529` | `registres.toml:T9_satp` | gen_regs.py | `nte-rv-satp` | 0 |  |  |
| `—` | `14_LICENSE.qmd:5` | `23_figs_externes/by-nc-sa.eu.png` | ràster |  | 0 |  |  |

## Fitxers font

| Fitxer | Ús | Origen | Amplada | `<title>` | `<desc>` | Textos | Fora de paleta | Duplicat de |
| :--- | :--- | :--- | ---: | :---: | :---: | ---: | :--- | :--- |
| `22_figs_originals/T1_flux_compilacio.svg` | A1.qmd:58, A1.qmd:65 | Inkscape | 901 | sí | sí | 20 | #1a5276 #4a90b8 #e8f4f8 |  |
| `22_figs_originals/T1_picopi_fases.svg` | A1.qmd:227, A1.qmd:234 | Inkscape | 680 | sí | sí | 39 | #888780 |  |
| `22_figs_originals/T1_von_neumann.svg` | A1.qmd:361, A1.qmd:368 | Inkscape | 700 | sí | sí | 26 | #185fa5 #888780 #e6f1fb |  |
| `22_figs_originals/T2_acces_vector.svg` | A2.qmd:1905, A2.qmd:1912 | SVG natiu | 260 | no | no | 13 |  |  |
| `22_figs_originals/T2_endianness_regla_pi.svg` | A2.qmd:1039, A2.qmd:1046 | Inkscape | 680 | no | no | 15 |  |  |
| `22_figs_originals/T3_ba_exemple.svg` | A3.qmd:1759, A3.qmd:1766 | Inkscape | 316 | no | no | 20 |  |  |
| `22_figs_originals/T3_ba_func.svg` | A3.qmd:1457, A3.qmd:1464 | Inkscape | 326 | no | no | 11 | #333333 #4d4d4d |  |
| `22_figs_originals/T3_ba_general.svg` | A3.qmd:1428, A3.qmd:1435 | Inkscape | 326 | no | no | 12 | #4d4d4d |  |
| `22_figs_originals/T3_ba_multi.svg` | A3.qmd:1642, A3.qmd:1649 | Inkscape | 326 | no | no | 7 |  |  |
| `22_figs_originals/T3_compilacio_separada.svg` | A3.qmd:1857, A3.qmd:1864 | Inkscape | 610 | sí | sí | 13 |  |  |
| `22_figs_originals/T3_deps_exemple.svg` | A3.qmd:1716, A3.qmd:1723 | SVG natiu | 560 | no | no | 5 |  |  |
| `22_figs_originals/T3_deps_multi.svg` | A3.qmd:1619, A3.qmd:1626 | SVG natiu | 520 | no | no | 3 |  |  |
| `22_figs_originals/T3_flux_gcc_complet.svg` | A3.qmd:2051, A3.qmd:2058 | SVG natiu | 490 | sí | sí | 21 |  |  |
| `22_figs_originals/T3_func_multinivell_pila.png` | **orfe** | ràster |  | no | no | 0 |  |  |
| `22_figs_originals/T3_func_uninivell_pila.svg` | A3.qmd:1387, A3.qmd:1394 | SVG natiu | 310 | no | no | 19 |  |  |
| `22_figs_originals/T3_mapa_memoria.svg` | A3.qmd:1026, A3.qmd:1033 | Inkscape | 326 | no | no | 19 | #4d4d4d |  |
| `22_figs_originals/T3_pila_crides_aniuades.svg` | A3.qmd:1508, A3.qmd:1515 | SVG natiu | 450 | no | no | 34 |  |  |
| `22_figs_originals/T4_divisor_sequencial.svg` | A4.qmd:394, A4.qmd:401 | SVG natiu | 440 | sí | sí | 16 |  |  |
| `22_figs_originals/T4_matriu_emmagatzematge.svg` | A4.qmd:521, A4.qmd:528 | SVG natiu | 680 | sí | sí | 50 | #dee2e6 |  |
| `22_figs_originals/T4_matriu_offset_ij.svg` | A4.qmd:562, A4.qmd:569 | SVG natiu | 680 | sí | sí | 12 | #dee2e6 |  |
| `22_figs_originals/T4_matriu_recorreguts_strides.svg` | A4.qmd:849, A4.qmd:856 | SVG natiu | 680 | sí | sí | 8 |  |  |
| `22_figs_originals/T4_multiplicador_arbre.svg` | A4.qmd:252, A4.qmd:259 | SVG natiu | 440 | sí | sí | 22 |  |  |
| `22_figs_originals/T4_multiplicador_sequencial.png` | **orfe** | ràster |  | no | no | 0 |  |  |
| `22_figs_originals/T4_multiplicador_sequencial.svg` | A4.qmd:190, A4.qmd:197 | SVG natiu | 420 | sí | sí | 15 |  |  |
| `22_figs_originals/T4_semisumador_sumador_complet.svg` | A4.qmd:80, A4.qmd:87 | script (gen_T4_sumador.py) | 590 | sí | sí | 24 |  |  |
| `22_figs_originals/T4_sumador_propagacio_rossec.svg` | A4.qmd:104, A4.qmd:97 | script (gen_T4_sumador.py) | 750 | sí | sí | 28 |  |  |
| `22_figs_originals/T5_coma_flotant_exponent__drawio.svg` | **orfe** | Inkscape | 740 | no | no | 24 | #000000 #ff0000 |  |
| `22_figs_originals/T5_coma_flotant_racionals__drawio.svg` | **orfe** | Inkscape | 1640 | no | no | 170 | #000000 |  |
| `22_figs_originals/T5_exponent.svg` | A5.qmd:135, A5.qmd:142 | Inkscape | 740 | no | no | 24 | #000000 |  |
| `22_figs_originals/T5_grs_esquema.svg` | A5.qmd:435, A5.qmd:442 | SVG natiu | 620 | sí | sí | 20 | #000000 |  |
| `22_figs_originals/T5_ieee754_format_registre.svg` | **orfe** | SVG natiu | 708 | sí | sí | 8 |  |  |
| `22_figs_originals/T5_recta_global.svg` | A5.qmd:270, A5.qmd:277 | SVG natiu | 950 | sí | no | 86 | #000000 |  |
| `22_figs_originals/T5_recta_global__org.svg` | **orfe** | SVG natiu | 1820 | sí | no | 93 | #000000 |  |
| `22_figs_originals/T5_recta_zoom_zero.svg` | A5.qmd:385, A5.qmd:392 | Inkscape | 900 | sí | no | 74 | #000000 |  |
| `22_figs_originals/T5_recta_zoom_zero__org.svg` | **orfe** | SVG natiu | 1360 | sí | no | 56 | #000000 |  |
| `22_figs_originals/T5_taula_codificacions.svg` | A5.qmd:344, A5.qmd:351 | exportació LO Draw | 11509.377 | no | no | 12 | #000000 |  |
| `22_figs_originals/T6_amdahl.svg` | A6.qmd:217, A6.qmd:224 | extreta de PDF | 220 | no | no | 38 | #000000 #999999 |  |
| `22_figs_originals/T6_amdahl_mod.svg` | **orfe** | Inkscape | 220 | no | no | 42 | #000000 #999999 |  |
| `22_figs_originals/T6_not_0_1.svg` | A6.qmd:326, A6.qmd:333 | extreta de PDF | 386 | no | no | 14 | #000000 |  |
| `22_figs_originals/T6_not_1_0.svg` | A6.qmd:309, A6.qmd:316 | extreta de PDF | 386 | no | no | 14 | #000000 |  |
| `22_figs_originals/T6_not_cmos.svg` | A6.qmd:290, A6.qmd:297 | extreta de PDF | 360 | no | no | 8 | #000000 |  |
| `22_figs_originals/T6_tc_tc_prima.svg` | A6.qmd:149, A6.qmd:156 | extreta de PDF | 284 | no | no | 10 | #000000 #b3b3b3 |  |
| `22_figs_originals/T7_assoc_conjunts_taula.svg` | A7.qmd:346, A7.qmd:353 | Inkscape | 800 | sí | sí | 76 | #000000 |  |
| `22_figs_originals/T7_ca_diagrama.svg` | A7.qmd:396, A7.qmd:403 | Inkscape | 680 | sí | sí | 1 | #ff0000 | `22_figs_originals/T7_texe_diagrama.svg` `22_figs_originals/T8_mv_flux_traduccio.svg` `22_figs_originals/TODO.svg` |
| `22_figs_originals/T7_capacitat_exemple.svg` | **orfe** | Inkscape | 800 | sí | sí | 392 |  |  |
| `22_figs_originals/T7_capacitat_exemple_bucle_primera_passada.svg` | A7.qmd:903, A7.qmd:910 | Inkscape | 800 | sí | sí | 235 |  |  |
| `22_figs_originals/T7_capacitat_exemple_bucle_segona_passada.svg` | A7.qmd:918, A7.qmd:925 | Inkscape | 800 | sí | sí | 266 |  |  |
| `22_figs_originals/T7_cd_descomposicio_bits.svg` | A7.qmd:269, A7.qmd:276 | Inkscape | 545 | sí | sí | 19 |  |  |
| `22_figs_originals/T7_cd_diagrama.svg` | **orfe** | exportació LO Draw | 14155.209 | no | no | 9 | #000000 #0000ff #ccffcc #ff0000 #ff8080 #ffe9e2 #fff0ec | `23_figs_externes/T7_cd_diagrama.svg` |
| `22_figs_originals/T7_conflicte_exemple.svg` | A7.qmd:866, A7.qmd:873 | Inkscape | 800 | sí | sí | 120 | #000000 |  |
| `22_figs_originals/T7_escriptura_dirty_bit.svg` | A7.qmd:495, A7.qmd:502 | Inkscape | 520 | sí | sí | 20 |  |  |
| `22_figs_originals/T7_escriptura_dirty_bit__.svg` | **orfe** | Inkscape | 400 | sí | sí | 7 |  |  |
| `22_figs_originals/T7_escriptura_estat_inicial.svg` | A7.qmd:554, A7.qmd:561 | Inkscape | 800 | sí | sí | 167 | #000000 |  |
| `22_figs_originals/T7_escriptura_immediata_amb_assignacio.svg` | A7.qmd:577, A7.qmd:584 | Inkscape | 800 | sí | sí | 101 | #000000 |  |
| `22_figs_originals/T7_escriptura_immediata_sense_assignacio.svg` | A7.qmd:601, A7.qmd:608 | Inkscape | 800 | sí | sí | 100 | #000000 |  |
| `22_figs_originals/T7_escriptura_retardada.svg` | A7.qmd:626, A7.qmd:633 | Inkscape | 800 | sí | sí | 163 | #000000 |  |
| `22_figs_originals/T7_gap_processador_memoria.svg` | A7.qmd:34, A7.qmd:41 | SVG natiu | 620 | sí | sí | 17 | #dee2e6 |  |
| `22_figs_originals/T7_jerarquia_piramide.svg` | A7.qmd:106, A7.qmd:99 | SVG natiu | 580 | sí | sí | 7 |  |  |
| `22_figs_originals/T7_lru_exemple.svg` | A7.qmd:463, A7.qmd:470 | Inkscape | 800 | sí | sí | 237 | #000000 |  |
| `22_figs_originals/T7_mc_descomposicio_bits.svg` | **orfe** | Inkscape | 590 | sí | sí | 18 |  |  |
| `22_figs_originals/T7_mc_encert.svg` | A7.qmd:208, A7.qmd:215 | Inkscape | 575 | sí | sí | 29 | #000000 |  |
| `22_figs_originals/T7_mc_fallada.svg` | A7.qmd:231, A7.qmd:238 | Inkscape | 575 | sí | sí | 48 | #000000 #0b449a #7d6d6c |  |
| `22_figs_originals/T7_mc_organitzacio.svg` | A7.qmd:145, A7.qmd:152 | SVG natiu | 520 | sí | sí | 15 |  |  |
| `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` | A7.qmd:646, A7.qmd:653 | Graphviz | 459 | sí | no | 19 |  |  |
| `22_figs_originals/T7_tecnologies_memoria.svg` | **orfe** | SVG natiu | 680 | sí | sí | 24 |  |  |
| `22_figs_originals/T7_texe_diagrama.svg` | A7.qmd:786, A7.qmd:793 | Inkscape | 680 | sí | sí | 1 | #ff0000 | `22_figs_originals/T7_ca_diagrama.svg` `22_figs_originals/T8_mv_flux_traduccio.svg` `22_figs_originals/TODO.svg` |
| `22_figs_originals/T8_mv_flux_traduccio.svg` | A8.qmd:270, A8.qmd:277 | Inkscape | 680 | sí | sí | 1 | #ff0000 | `22_figs_originals/T7_ca_diagrama.svg` `22_figs_originals/T7_texe_diagrama.svg` `22_figs_originals/TODO.svg` |
| `22_figs_originals/T9_cicle_interrupcio.svg` | A9.qmd:733, A9.qmd:740 | Inkscape | 680 | no | no | 17 |  |  |
| `22_figs_originals/TODO.svg` | **orfe** | Inkscape | 680 | sí | sí | 1 | #ff0000 | `22_figs_originals/T7_ca_diagrama.svg` `22_figs_originals/T7_texe_diagrama.svg` `22_figs_originals/T8_mv_flux_traduccio.svg` |
| `23_figs_externes/T7_Intel_Core_i9-13900K_Labelled_Die_Shot_800x368.jpg` | A7.qmd:1004 | ràster |  | no | no | 0 |  |  |
| `23_figs_externes/T7_assoc_conjunts_diagrama.png` | **orfe** | ràster |  | no | no | 0 |  |  |
| `23_figs_externes/T7_assoc_conjunts_diagrama.svg` | A7.qmd:365, A7.qmd:372 | exportació LO Draw | 10583.334 | no | no | 0 |  |  |
| `23_figs_externes/T7_assoc_conjunts_diagrama__net__.png` | **orfe** | ràster |  | no | no | 0 |  |  |
| `23_figs_externes/T7_assoc_conjunts_taula.svg` | **orfe** | exportació LO Draw | 14287.501 | no | no | 40 | #000000 #0000ff #8080ff #fff0ec |  |
| `23_figs_externes/T7_capacitat_exemple.svg` | **orfe** | exportació LO Draw | 14287.501 | no | no | 209 | #000000 #0000ff #00ff00 #8080ff #90c490 #b3b3b3 #b3b3ff #ff0000 #ff8080 #ffe0d1 #ffff80 |  |
| `23_figs_externes/T7_cd_diagrama.svg` | A7.qmd:303, A7.qmd:310 | exportació LO Draw | 14155.209 | no | no | 9 | #000000 #0000ff #ccffcc #ff0000 #ff8080 #ffe9e2 #fff0ec | `22_figs_originals/T7_cd_diagrama.svg` |
| `23_figs_externes/T7_conflicte_exemple.svg` | **orfe** | exportació LO Draw | 14287.501 | no | no | 87 | #000000 #0000ff #00ff00 #8080ff #90c490 #b3b3b3 #b3b3ff #ff8080 #ffe0d1 #ffff80 |  |
| `23_figs_externes/T7_escriptura_dirty_bit.svg` | **orfe** | exportació LO Draw | 11641.668 | no | no | 4 | #000000 #fff0ec |  |
| `23_figs_externes/T7_escriptura_estat_inicial.svg` | **orfe** | exportació LO Draw | 14287.5 | no | no | 114 | #000000 #8080ff #80ff80 #ff8080 #ffff00 #ffff80 |  |
| `23_figs_externes/T7_escriptura_immediata_amb_assignacio.svg` | **orfe** | exportació LO Draw | 14287.501 | no | no | 59 | #000000 #8080ff #80ff80 #ffff00 #ffff80 | `23_figs_externes/T7_escriptura_immediata_assignacio.svg` |
| `23_figs_externes/T7_escriptura_immediata_assignacio.svg` | **orfe** | exportació LO Draw | 14287.501 | no | no | 59 | #000000 #8080ff #80ff80 #ffff00 #ffff80 | `23_figs_externes/T7_escriptura_immediata_amb_assignacio.svg` |
| `23_figs_externes/T7_escriptura_immediata_sense_assignacio.svg` | **orfe** | exportació LO Draw | 14287.5 | no | no | 66 | #000000 #8080ff #80ff80 #ffff00 #ffff80 |  |
| `23_figs_externes/T7_escriptura_retardada.svg` | **orfe** | exportació LO Draw | 14287.5 | no | no | 124 | #000000 #8080ff #80ff80 #ff8080 #ffff00 #ffff80 |  |
| `23_figs_externes/T7_lru_exemple.svg` | **orfe** | exportació LO Draw | 14287.5 | no | no | 167 | #000000 #0000ff #8080ff #80ff80 #ff8080 #ffff80 |  |
| `23_figs_externes/T7_lru_roger___drawio.svg` | **orfe** | draw.io | 765 | no | no | 0 | #000000 #121212 #2eff2e #ff6666 |  |
| `23_figs_externes/T7_mc_exemple_descomposicio_32bits.svg` | **orfe** | exportació LO Draw | 13229.168 | no | no | 13 | #000000 #fff0ec |  |
| `23_figs_externes/T7_multinivell_diagrama.svg` | **orfe** | exportació LO Draw | 14022.917 | no | no | 24 | #000000 #ffebe0 |  |
| `23_figs_externes/T7_multinivell_multicore.svg` | **orfe** | exportació LO Draw | 14287.5 | no | no | 26 | #000000 #0000ff #d3e8d3 #ffebe0 |  |
| `23_figs_externes/T7_texe_diagrama____error____.svg` | **orfe** | exportació LO Draw | 12964.584 | no | no | 53 | #000000 #d3e8d3 |  |
| `23_figs_externes/T7_tipus_fallades_percentage____no_inclosa_pero_interessant____.svg` | **orfe** | exportació LO Draw | 13229.167 | no | no | 14 | #000000 #2b5190 #4273c5 #dfecf7 #ff0000 #ffff9a |  |
| `23_figs_externes/T7_tres_c_barres_light____error____.svg` | **orfe** | exportació LO Draw | 15081.25 | no | no | 29 | #000000 |  |
| `23_figs_externes/by-nc-sa.eu.png` | 14_LICENSE.qmd:5 | ràster |  | no | no | 0 |  |  |
| `registres.toml:T2_instruccio_tipus_R` | A2.qmd:1187, A2.qmd:1194 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T2_instruccio_tipus_I` | A2.qmd:1249, A2.qmd:1256 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T2_instruccio_tipus_S` | A2.qmd:1332, A2.qmd:1339 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T2_instruccio_tipus_U` | A2.qmd:1273, A2.qmd:1280 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T3_instruccio_tipus_B` | A3.qmd:404, A3.qmd:411 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T3_instruccio_tipus_J` | A3.qmd:512, A3.qmd:519 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T5_instruccio_tipus_R4` | A5.qmd:879, A5.qmd:886 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T5_ieee754_format_registre` | A5.qmd:86, A5.qmd:93 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T5_fcsr` | 11_riscv.qmd:270, 11_riscv.qmd:277 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_mstatus` | 11_riscv.qmd:436, 11_riscv.qmd:443 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_mtvec` | 11_riscv.qmd:454, 11_riscv.qmd:461 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_mepc` | 11_riscv.qmd:418, 11_riscv.qmd:425 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_mcause` | A9.qmd:115, A9.qmd:122 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_mip` | 11_riscv.qmd:472, 11_riscv.qmd:479 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_mie` | 11_riscv.qmd:484, 11_riscv.qmd:491 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:T9_satp` | 11_riscv.qmd:529, 11_riscv.qmd:536 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:compendi_registres` | 11_riscv.qmd:40, 11_riscv.qmd:47 | gen_regs.py (COMPENDIS) |  | sí | sí | 0 |  |  |
| `registres.toml:compendi_registres_RIS` | A2.qmd:268, A2.qmd:275 | gen_regs.py (COMPENDIS) |  | sí | sí | 0 |  |  |

## Avisos

### Colors fora de la paleta (`svg.md §10` i `§16`) (32)

- `22_figs_originals/T1_flux_compilacio.svg`: #1a5276 #4a90b8 #e8f4f8
- `22_figs_originals/T1_picopi_fases.svg`: #888780
- `22_figs_originals/T1_von_neumann.svg`: #185fa5 #888780 #e6f1fb
- `22_figs_originals/T3_ba_func.svg`: #333333 #4d4d4d
- `22_figs_originals/T3_ba_general.svg`: #4d4d4d
- `22_figs_originals/T3_mapa_memoria.svg`: #4d4d4d
- `22_figs_originals/T4_matriu_emmagatzematge.svg`: #dee2e6
- `22_figs_originals/T4_matriu_offset_ij.svg`: #dee2e6
- `22_figs_originals/T5_exponent.svg`: #000000
- `22_figs_originals/T5_grs_esquema.svg`: #000000
- `22_figs_originals/T5_recta_global.svg`: #000000
- `22_figs_originals/T5_recta_zoom_zero.svg`: #000000
- `22_figs_originals/T5_taula_codificacions.svg`: #000000
- `22_figs_originals/T6_amdahl.svg`: #000000 #999999
- `22_figs_originals/T6_not_0_1.svg`: #000000
- `22_figs_originals/T6_not_1_0.svg`: #000000
- `22_figs_originals/T6_not_cmos.svg`: #000000
- `22_figs_originals/T6_tc_tc_prima.svg`: #000000 #b3b3b3
- `22_figs_originals/T7_assoc_conjunts_taula.svg`: #000000
- `22_figs_originals/T7_ca_diagrama.svg`: #ff0000
- `22_figs_originals/T7_conflicte_exemple.svg`: #000000
- `22_figs_originals/T7_escriptura_estat_inicial.svg`: #000000
- `22_figs_originals/T7_escriptura_immediata_amb_assignacio.svg`: #000000
- `22_figs_originals/T7_escriptura_immediata_sense_assignacio.svg`: #000000
- `22_figs_originals/T7_escriptura_retardada.svg`: #000000
- `22_figs_originals/T7_gap_processador_memoria.svg`: #dee2e6
- `22_figs_originals/T7_lru_exemple.svg`: #000000
- `22_figs_originals/T7_mc_encert.svg`: #000000
- `22_figs_originals/T7_mc_fallada.svg`: #000000 #0b449a #7d6d6c
- `22_figs_originals/T7_texe_diagrama.svg`: #ff0000
- `22_figs_originals/T8_mv_flux_traduccio.svg`: #ff0000
- `23_figs_externes/T7_cd_diagrama.svg`: #000000 #0000ff #ccffcc #ff0000 #ff8080 #ffe9e2 #fff0ec

### Duplicats byte a byte (3)

- `22_figs_originals/T7_ca_diagrama.svg` = `22_figs_originals/T7_texe_diagrama.svg` = `22_figs_originals/T8_mv_flux_traduccio.svg` = `22_figs_originals/TODO.svg`
- `22_figs_originals/T7_cd_diagrama.svg` = `23_figs_externes/T7_cd_diagrama.svg`
- `23_figs_externes/T7_escriptura_immediata_amb_assignacio.svg` = `23_figs_externes/T7_escriptura_immediata_assignacio.svg`

### Etiquetes `#fig-` dins d'un callout `#nte-` (15)

- `fig-compendi-registres` (A2.qmd:265, `nte-instruccions-tipus`)
- `fig-typeR` (A2.qmd:1184, `nte-instruccions-Tipus-R`)
- `fig-typeI` (A2.qmd:1246, `nte-instruccions-Tipus-I`)
- `fig-typeU` (A2.qmd:1270, `nte-format-u`)
- `fig-typeS` (A2.qmd:1329, `nte-instruccions-Tipus-S`)
- `fig-typeB` (A3.qmd:401, `nte-format-b`)
- `fig-typeJ` (A3.qmd:509, `nte-format-j`)
- `fig-fcsr` (A5.qmd:751, `nte-fcsr`)
- `fig-ei-mcause` (A9.qmd:112, `nte-mcause-mes-rellevants`)
- `fig-ei-mepc` (A9.qmd:145, `nte-mepc`)
- `fig-ei-mstatus` (A9.qmd:167, `nte-mstatus`)
- `fig-ei-mtvec` (A9.qmd:193, `nte-mtvec`)
- `fig-ei-mip` (A9.qmd:239, `nte-mip-mie`)
- `fig-ei-mie` (A9.qmd:254, `nte-mip-mie`)
- `fig-ei-satp` (A9.qmd:819, `nte-satp`)

### Etiquetes `#tbl-` dins d'un callout `#nte-` (2)

- `tbl-tipus-alineacio` (A2.qmd:1069)
- `tbl-syscalls-rars` (A9.qmd:543)

### Figures consumides com a exportació (`__extern_`) (2)

- `23_figs_externes/T7_assoc_conjunts_diagrama.svg`
- `23_figs_externes/T7_cd_diagrama.svg`

### Figures del cos del text sense cap remissió `@` (24)

- `fig-von-neumann` (A1.qmd:358)
- `fig-mapa-memoria` (A3.qmd:1023)
- `fig-ba-general` (A3.qmd:1425)
- `fig-compilacio-separada` (A3.qmd:1854)
- `fig-multiplicador-sequencial` (A4.qmd:187)
- `fig-divisor-sequencial` (A4.qmd:391)
- `fig-matriu-emmagatzematge` (A4.qmd:518)
- `fig-matriu-offset-ij` (A4.qmd:559)
- `fig-matriu-recorreguts-strides` (A4.qmd:846)
- `fig-ieee754-format` (A5.qmd:83)
- `fig-taula-codificacions` (A5.qmd:341)
- `fig-grs-esquema` (A5.qmd:432)
- `fig-jerarquia-piramide` (A7.qmd:96)
- `fig-mc-organitzacio` (A7.qmd:142)
- `fig-mc-encert` (A7.qmd:205)
- `fig-mc-fallada` (A7.qmd:228)
- `fig-cd-descomposicio-bits` (A7.qmd:266)
- `fig-assoc-conjunts-taula` (A7.qmd:343)
- `fig-escriptura-dirty-bit` (A7.qmd:492)
- `fig-escriptura-estat-inicial` (A7.qmd:551)
- `fig-conflicte-exemple` (A7.qmd:863)
- `fig-capacitat-exemple-bucle-primera-passada` (A7.qmd:900)
- `fig-capacitat-exemple-bucle-segona-passada` (A7.qmd:915)
- `fig-cicle-interrupcio` (A9.qmd:730)

### Figures que consumeixen el placeholder (`TODO.svg`) (3)

- `22_figs_originals/T7_ca_diagrama.svg`
- `22_figs_originals/T7_texe_diagrama.svg`
- `22_figs_originals/T8_mv_flux_traduccio.svg`

### Figures ràster (1)

- `23_figs_externes/T7_Intel_Core_i9-13900K_Labelled_Die_Shot_800x368.jpg`

### Fitxers font orfes (cap `.qmd` no els consumeix) (33)

- `22_figs_originals/T3_func_multinivell_pila.png`
- `22_figs_originals/T4_multiplicador_sequencial.png`
- `22_figs_originals/T5_coma_flotant_exponent__drawio.svg`
- `22_figs_originals/T5_coma_flotant_racionals__drawio.svg`
- `22_figs_originals/T5_ieee754_format_registre.svg`
- `22_figs_originals/T5_recta_global__org.svg`
- `22_figs_originals/T5_recta_zoom_zero__org.svg`
- `22_figs_originals/T6_amdahl_mod.svg`
- `22_figs_originals/T7_capacitat_exemple.svg`
- `22_figs_originals/T7_cd_diagrama.svg`
- `22_figs_originals/T7_escriptura_dirty_bit__.svg`
- `22_figs_originals/T7_mc_descomposicio_bits.svg`
- `22_figs_originals/T7_tecnologies_memoria.svg`
- `22_figs_originals/TODO.svg`
- `23_figs_externes/T7_assoc_conjunts_diagrama.png`
- `23_figs_externes/T7_assoc_conjunts_diagrama__net__.png`
- `23_figs_externes/T7_assoc_conjunts_taula.svg`
- `23_figs_externes/T7_capacitat_exemple.svg`
- `23_figs_externes/T7_conflicte_exemple.svg`
- `23_figs_externes/T7_escriptura_dirty_bit.svg`
- `23_figs_externes/T7_escriptura_estat_inicial.svg`
- `23_figs_externes/T7_escriptura_immediata_amb_assignacio.svg`
- `23_figs_externes/T7_escriptura_immediata_assignacio.svg`
- `23_figs_externes/T7_escriptura_immediata_sense_assignacio.svg`
- `23_figs_externes/T7_escriptura_retardada.svg`
- `23_figs_externes/T7_lru_exemple.svg`
- `23_figs_externes/T7_lru_roger___drawio.svg`
- `23_figs_externes/T7_mc_exemple_descomposicio_32bits.svg`
- `23_figs_externes/T7_multinivell_diagrama.svg`
- `23_figs_externes/T7_multinivell_multicore.svg`
- `23_figs_externes/T7_texe_diagrama____error____.svg`
- `23_figs_externes/T7_tipus_fallades_percentage____no_inclosa_pero_interessant____.svg`
- `23_figs_externes/T7_tres_c_barres_light____error____.svg`

### Peus que no acaben en punt (2)

- `fig-big-endian` (A2.qmd:1004)
- `fig-little-endian` (A2.qmd:1014)

### SVG consumits sense `<desc>` (el text alternatiu) (24)

- `22_figs_originals/T2_acces_vector.svg`
- `22_figs_originals/T2_endianness_regla_pi.svg`
- `22_figs_originals/T3_ba_exemple.svg`
- `22_figs_originals/T3_ba_func.svg`
- `22_figs_originals/T3_ba_general.svg`
- `22_figs_originals/T3_ba_multi.svg`
- `22_figs_originals/T3_deps_exemple.svg`
- `22_figs_originals/T3_deps_multi.svg`
- `22_figs_originals/T3_func_uninivell_pila.svg`
- `22_figs_originals/T3_mapa_memoria.svg`
- `22_figs_originals/T3_pila_crides_aniuades.svg`
- `22_figs_originals/T5_exponent.svg`
- `22_figs_originals/T5_recta_global.svg`
- `22_figs_originals/T5_recta_zoom_zero.svg`
- `22_figs_originals/T5_taula_codificacions.svg`
- `22_figs_originals/T6_amdahl.svg`
- `22_figs_originals/T6_not_0_1.svg`
- `22_figs_originals/T6_not_1_0.svg`
- `22_figs_originals/T6_not_cmos.svg`
- `22_figs_originals/T6_tc_tc_prima.svg`
- `22_figs_originals/T7_mc_politiques_resum__graphviz.svg`
- `22_figs_originals/T9_cicle_interrupcio.svg`
- `23_figs_externes/T7_assoc_conjunts_diagrama.svg`
- `23_figs_externes/T7_cd_diagrama.svg`

### SVG consumits sense `<title>` (21)

- `22_figs_originals/T2_acces_vector.svg`
- `22_figs_originals/T2_endianness_regla_pi.svg`
- `22_figs_originals/T3_ba_exemple.svg`
- `22_figs_originals/T3_ba_func.svg`
- `22_figs_originals/T3_ba_general.svg`
- `22_figs_originals/T3_ba_multi.svg`
- `22_figs_originals/T3_deps_exemple.svg`
- `22_figs_originals/T3_deps_multi.svg`
- `22_figs_originals/T3_func_uninivell_pila.svg`
- `22_figs_originals/T3_mapa_memoria.svg`
- `22_figs_originals/T3_pila_crides_aniuades.svg`
- `22_figs_originals/T5_exponent.svg`
- `22_figs_originals/T5_taula_codificacions.svg`
- `22_figs_originals/T6_amdahl.svg`
- `22_figs_originals/T6_not_0_1.svg`
- `22_figs_originals/T6_not_1_0.svg`
- `22_figs_originals/T6_not_cmos.svg`
- `22_figs_originals/T6_tc_tc_prima.svg`
- `22_figs_originals/T9_cicle_interrupcio.svg`
- `23_figs_externes/T7_assoc_conjunts_diagrama.svg`
- `23_figs_externes/T7_cd_diagrama.svg`

### Text en gris de traç (`#adb5bd`) (2)

- `22_figs_originals/T4_multiplicador_arbre.svg` (3)
- `22_figs_originals/T5_recta_zoom_zero.svg` (2)

### `textLength` (rsvg-convert no l'implementa) (5)

- `22_figs_originals/T6_amdahl.svg` (38)
- `22_figs_originals/T6_not_0_1.svg` (13)
- `22_figs_originals/T6_not_1_0.svg` (13)
- `22_figs_originals/T6_not_cmos.svg` (8)
- `22_figs_originals/T6_tc_tc_prima.svg` (5)
