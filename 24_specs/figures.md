# Inventari de figures

Generat per `25_scripts/inventari_figures.py` sobre `19b9913` (2026-10-09), amb canvis no confirmats a l'arbre de treball. **No l'editeu a mà**: `make inventari` el regenera. Les comprovacions, i què vol dir cada columna, són a la capçalera de l'script.

- **87** etiquetes `#fig-`: 84 amb imatge, 6 d'elles subfigures de 3 figures, i 0 taules Markdown; i **25** imatges sense etiqueta (les del compendi i la de la llicència).
- **76** fitxers a `22_figs_originals/` i `23_figs_externes/`: 61 consumits i 15 sense consumir.
- Figures generades al pre-render: **18** de `gen_regs.py` (`__registre`), **7** de `gen_BA.py` (`__BA`), **3** de `gen_mapa.py` (`__mapa`), **2** de `gen_subrutines.py` (`__subrutina`), **14** de `gen_MC.py` (`__MC`), **3** de `gen_memoria.py` (`__memoria`).

## Figures

| Etiqueta | Lloc | Font | Origen | Callout | @ | Peu | `<desc>` |
| :--- | :--- | :--- | :--- | :--- | ---: | :--- | :--- |
| `fig-flux-compilacio` | `A1.qmd:55` | `22_figs_originals/A1_flux_compilacio.svg` | Inkscape |  | 1 | El flux de generació del programari: les quatre etapes del *toolchain* GCC. | Diagrama que mostra el flux de generació d'un programa exec… |
| `fig-picopi-fases` | `A1.qmd:224` | `22_figs_originals/A1_picopi_fases.svg` | Inkscape | `wrn-picopi` | 0 | Configuració física i fases d'ús del conjunt Host + Sonda (*Pi Debug Probe*) + Target (*P… | Quatre diagrames en una sola figura: fase de creació (el ho… |
| `fig-von-neumann` | `A1.qmd:360` | `22_figs_originals/A1_von_neumann.svg` | Inkscape |  | 1 | Arquitectura de Von Neumann: CPU (ALU, CU i Registres), Memòria principal i Sistema d'E/S… | CPU, Memòria Principal i Sistema d'E/S en disposició horitz… |
| `fig-memoria-creix-avall` | `A2.qmd:986` | `memoria.toml:A2_memoria_creix_avall` | gen_memoria.py | `imp-adrecament-a-nivell-byte` | 0 | Representació gràfica de la memòria. | Una columna de cel·les d'un byte cadascuna, amb l'adreça a … |
| `fig-big-endian` | `A2.qmd:1026` | `memoria.toml:A2_big_endian` | gen_memoria.py | `tip-endianness` | 0 | Big-endian. | Quatre bytes consecutius, de l'adreça 0x10010000 a la 0x100… |
| `fig-little-endian` | `A2.qmd:1040` | `memoria.toml:A2_little_endian` | gen_memoria.py | `tip-endianness` | 0 | Little-endian. | Quatre bytes consecutius, de l'adreça 0x10010000 a la 0x100… |
| `fig-endianness-regla-pi` | `A2.qmd:1066` | `22_figs_originals/A2_endianness_regla_pi.svg` | Inkscape | `wrn-endianness-regla-pi` | 0 | Regla mnemotècnica de la lletra grega pi (Π) per recordar l'ordenació dels bytes Little-e… | A dalt, el valor com a quatre bytes: 11, 22, 33 i 44. A l'e… |
| `fig-acces-vector` | `A2.qmd:1910` | `22_figs_originals/A2_acces_vector.svg` | SVG natiu | `tip-load-store-word` | 0 | Accés a un element d'un vector. | El vector vec en memòria, amb les adreces creixent cap aval… |
| `fig-mapa-memoria` | `A3.qmd:1021` | `mapa.toml:A3_mapa_memoria` | gen_mapa.py |  | 1 | Mapa de memòria de RARS: regions `.text`, `.data`, heap i pila, amb les adreces d'inici d… | Una columna de memòria amb les adreces creixent cap avall: … |
| `fig-func-uninivell-pila` | `A3.qmd:1385` | `mapa.toml:A3_pila_uninivell` | gen_mapa.py | `tip-func-uninivell-bloc-activacio` | 0 | Evolució del registre `sp` durant la crida i el retorn de la funció fulla `funcB`: decrei… | Tres columnes de la pila, d'adreces baixes a altes, amb sp … |
| `fig-ba-general` | `A3.qmd:1426` | `BA.toml:A3_ba_general` | gen_BA.py |  | 1 | Estructura general del bloc d'activació: variables locals al cim de la pila i registres d… | La pila, d'adreces baixes, amb sp a dalt, a adreces altes, … |
| `fig-ba-func` | `A3.qmd:1455` | `BA.toml:A3_ba_func` | gen_BA.py | `tip-exemple-variables-pila` | 0 | Bloc d'activació de la funció `func`: el vector `v` ocupa els bytes 0–9, l'alineació ocup… | Bloc d'activació de 52 bytes, d'adreces baixes (sp) a altes… |
| `fig-pila-crides-multinivell` | `A3.qmd:1506` | `mapa.toml:A3_pila_multinivell` | gen_mapa.py | `tip-exemple-pila-multinivell` | 0 | Evolució del registre `sp` durant la crida i el retorn de la funció multinivell `funcA` i… | Cinc columnes de la pila, d'adreces baixes a altes, amb sp … |
| `fig-deps-multi` | `A3.qmd:1619` | `(subfigures)` | — | `tip-exemple-multi` | 0 | Dependències de dades de la subrutina `multi`, en dues representacions. Les dades `c` i `… |  |
| `fig-deps-multi-fletxes` | `A3.qmd:1620` | `22_figs_originals/A3_deps_multi.svg` | Inkscape | `tip-exemple-multi` | 0 | Amb fletxes, de l'escriptura a l'ús. Les línies de punts separen el codi anterior i el po… | El codi de la funció multi(int a, int b, int c). Una línia … |
| `fig-deps-multi-barres` | `A3.qmd:1634` | `subrutines.toml:A3_deps_multi` | gen_subrutines.py | `tip-exemple-multi` | 0 | Amb barres de vida, de l'última escriptura a l'últim ús. La franja grisa és la crida. | Codi C de la subrutina multi, amb la crida a mcm marcada co… |
| `fig-ba-multi` | `A3.qmd:1653` | `BA.toml:A3_ba_multi` | gen_BA.py | `tip-exemple-multi` | 0 | Bloc d'activació de la subrutina `multi`: 12 bytes amb `s0`, `s1` i `ra` desats als despl… | Bloc d'activació de 12 bytes, d'adreces baixes (sp) a altes… |
| `fig-deps-exemple` | `A3.qmd:1727` | `(subfigures)` | — | `tip-exemple-exemple` | 0 | Dependències de dades de la subrutina `exemple`, en dues representacions. Les dades `c`, … |  |
| `fig-deps-exemple-fletxes` | `A3.qmd:1728` | `22_figs_originals/A3_deps_exemple.svg` | Inkscape | `tip-exemple-exemple` | 0 | Amb fletxes, de l'escriptura a l'ús. Les línies de punts separen el codi anterior i el po… | El codi de la funció exemple(int a, int b, int c), amb líni… |
| `fig-deps-exemple-barres` | `A3.qmd:1742` | `subrutines.toml:A3_deps_exemple` | gen_subrutines.py | `tip-exemple-exemple` | 0 | Amb barres de vida, de l'última escriptura a l'últim ús. Les franges grises són les cride… | Codi C de la subrutina exemple, amb les crides a f i a g ma… |
| `fig-ba-exemple` | `A3.qmd:1775` | `BA.toml:A3_ba_exemple` | gen_BA.py | `tip-exemple-exemple` | 0 | Bloc d'activació de la subrutina `exemple`: variables locals `q`, `v` i `w` als desplaçam… | Bloc d'activació de 60 bytes, d'adreces baixes (sp) a altes… |
| `fig-compilacio-separada` | `A3.qmd:1875` | `22_figs_originals/A3_compilacio_separada.svg` | Inkscape |  | 1 | Flux de compilació separada: cada mòdul es compila i assembla independentment generant un… | Diagrama que mostra el flux de compilació separada: p1.c i … |
| `fig-flux-gcc-complet` | `A3.qmd:2069` | `22_figs_originals/A3_flux_gcc_complet.svg` | SVG natiu | `wrn-flux-gcc-complet` | 0 | El flux de generació complet. | Diagrama del flux complet de generació d'un executable amb … |
| `fig-semisumador-sumador-complet` | `A4.qmd:77` | `22_figs_originals/A4_semisumador_sumador_complet.svg` | SVG natiu | `wrn-sobreeiximent-maquinari` | 1 | Semisumador i sumador complet: (a) el semisumador, amb una XOR per al bit de suma i una A… | (a) Semisumador: una porta XOR dona el bit de suma s = a xo… |
| `fig-sumador-propagacio-rossec` | `A4.qmd:94` | `22_figs_originals/A4_sumador_propagacio_rossec.svg` | SVG natiu | `wrn-sobreeiximent-maquinari` | 1 | Sumador de $n$ bits amb propagació del ròssec. El ròssec avança de dreta a esquerra, del … | Cadena de n sumadors complets, del bit de més pes (n-1, a l… |
| `fig-multiplicador-sequencial` | `A4.qmd:187` | `22_figs_originals/A4_multiplicador_sequencial.svg` | SVG natiu |  | 1 | Circuit multiplicador seqüencial. | Esquema del circuit multiplicador seqüencial: el registre M… |
| `fig-multiplicador-arbre` | `A4.qmd:249` | `22_figs_originals/A4_multiplicador_arbre.svg` | SVG natiu | `wrn-circuit-multiplicacio-combinacional` | 0 | Circuit multiplicador combinacional en arbre. | Esquema d'un multiplicador combinacional en arbre: els prod… |
| `fig-divisor-sequencial` | `A4.qmd:391` | `22_figs_originals/A4_divisor_sequencial.svg` | SVG natiu |  | 1 | Circuit divisor seqüencial amb restauració. | Esquema del circuit divisor seqüencial amb algorisme de res… |
| `fig-matriu-emmagatzematge` | `A4.qmd:518` | `22_figs_originals/A4_matriu_emmagatzematge.svg` | SVG natiu |  | 1 | Emmagatzematge de `mat[4][6]` en memòria per files. | Diagrama que mostra com una matriu mat[4][6] s'emmagatzema … |
| `fig-matriu-offset-ij` | `A4.qmd:559` | `22_figs_originals/A4_matriu_offset_ij.svg` | SVG natiu |  | 1 | Càlcul de l'adreça de `mat[i][j]`. | Diagrama que mostra com l'adreça de mat[i][j] es descompon … |
| `fig-matriu-recorreguts-strides` | `A4.qmd:844` | `22_figs_originals/A4_matriu_recorreguts_strides.svg` | SVG natiu |  | 1 | Recorreguts de matrius, `mat[4][5]` a dalt i `mat[4][4]` a baix, i els strides correspone… | Quatre diagrames mostrant els patrons de recorregut: una fi… |
| `fig-ieee754-format` | `A5.qmd:83` | `registres.toml:A5_ieee754_format_registre` | gen_regs.py |  | 1 | Disposició dels camps S, E i F en el format IEEE 754 de precisió simple (32 bits). | S(31), E(30–23), F(22–0). |
| `fig-exponent-ieee754` | `A5.qmd:132` | `22_figs_originals/A5_exponent.svg` | Inkscape |  | 1 | Correspondència entre l'exponent emmagatzemat $E_u$ (0–255) i l'exponent real $e = E_u - … | Dues rectes. La de dalt és l'exponent emmagatzemat, de 0 a … |
| `fig-recta-global` | `A5.qmd:267` | `22_figs_originals/A5_recta_global.svg` | SVG natiu |  | 1 | Recta de la coma flotant IEEE 754 (precisió simple): $\pm\infty$ i NaN als extrems ($E=25… | Dues rectes, la dels negatius a dalt i la dels positius a s… |
| `fig-taula-codificacions` | `A5.qmd:343` | `22_figs_originals/A5_taula_codificacions.svg` | exportació LO Draw |  | 1 | Mapa de codificacions IEEE 754 de precisió simple: els eixos $E$ i $F$ determinen unívoca… | Una taula de dues entrades. Les columnes són l'exponent E: … |
| `fig-recta-zoom-zero` | `A5.qmd:384` | `22_figs_originals/A5_recta_zoom_zero.svg` | Inkscape |  | 1 | Zoom al voltant del zero: $\pm 0$ i els denormals ($E=0$) omplen el buit entre el zero i … | Dues rectes al voltant del zero, la dels negatius a dalt i … |
| `fig-grs-esquema` | `A5.qmd:434` | `22_figs_originals/A5_grs_esquema.svg` | SVG natiu |  | 1 | Esquema dels bits de guarda ($G$), arrodoniment ($R$) i *sticky* ($S$) respecte de la man… | Mantissa retinguda seguida dels tres bits descartats G, R i… |
| `fig-format-r4` | `A5.qmd:875` | `registres.toml:A5_instruccio_tipus_R4` | gen_regs.py | `wrn-instruccions-fusionades` | 1 | Format d'instrucció R4 (RV32F), el de les instruccions fusionades. | fs3(31–27), funct2(26–25), fs2(24–20), fs1(19–15), funct3(1… |
| `fig-tc-tc-prima` | `A6.qmd:146` | `22_figs_originals/A6_tc_tc_prima.svg` | Inkscape | `tip-augment-freq` | 0 | Mateixos components, diferents temps de cicle. | Dos diagrames de temps amb dues etapes, A i B, de durades d… |
| `fig-amdahl` | `A6.qmd:214` | `22_figs_originals/A6_amdahl.svg` | Inkscape |  | 1 | Temps total del programa original dividit en una part optimitzada (fracció $P_{x}$) i una… | Dues barres de temps d'execució, l'original i la millorada.… |
| `fig-not-cmos` | `A6.qmd:287` | `22_figs_originals/A6_not_cmos.svg` | Inkscape | `wrn-RC` | 1 | Porta NOT, representació funcional i implementació amb CMOS. | A l'esquerra, el símbol de la porta NOT, que alimenta un ci… |
| `fig-not-1-0` | `A6.qmd:306` | `22_figs_originals/A6_not_1_0.svg` | Inkscape | `wrn-RC` | 1 | Evolució temporal de la tensió de sortida de la porta NOT quan el valor lògic de l'entrad… | A l'esquerra, la porta NOT en CMOS, que alimenta un circuit… |
| `fig-not-0-1` | `A6.qmd:323` | `22_figs_originals/A6_not_0_1.svg` | Inkscape | `wrn-RC` | 1 | Evolució temporal de la tensió de sortida de la porta NOT quan el valor lògic de l'entrad… | A l'esquerra, la porta NOT en CMOS, que alimenta un circuit… |
| `fig-gap-processador-memoria` | `A7.qmd:31` | `22_figs_originals/A7_gap_processador_memoria.svg` | SVG natiu |  | 1 | Evolució del rendiment relatiu de processadors i memòria DRAM entre 1980 i 2010 (escala l… | Gràfica de línies amb escala logarítmica que mostra la dive… |
| `fig-jerarquia-piramide` | `A7.qmd:96` | `22_figs_originals/A7_jerarquia_piramide.svg` | SVG natiu |  | 1 | La jerarquia de memòria: cada nivell conserva les dades del nivell inferior que tinguin m… | Diagrama en forma de piràmide de quatre nivells: registres,… |
| `fig-mc-organitzacio` | `A7.qmd:142` | `MC.toml:A7_mc_organitzacio` | gen_MC.py |  | 1 | Organització interna d'una memòria cau de quatre línies. Cada línia conté un bit de valid… | Taula d'una memòria cau de 4 línies, numerades de 0 a 3, am… |
| `fig-mc-numbloc-descomposicio` | `A7.qmd:177` | `22_figs_originals/A7_mc_descomposicio_bits.svg` | Inkscape | `tip-mc-numbloc` | 0 | Descomposició de l'adreça `0x100100F8` amb blocs de 16 bytes: número de bloc i desplaçame… | Descomposició dels 32 bits de l'adreça 0x100100F8 en num_bl… |
| `fig-mc-encert` | `A7.qmd:216` | `22_figs_originals/A7_mc_encert.svg` | Inkscape |  | 1 | Encert en un accés a l'adreça `0x100100F8`: la dada es transfereix directament de l'MC a … | Diagrama que mostra el flux d'un encert de memòria cau: la … |
| `fig-mc-fallada` | `A7.qmd:238` | `22_figs_originals/A7_mc_fallada.svg` | Inkscape |  | 1 | Fallada en un accés a l'adreça `0x100100F8`: el bloc es copia de l'MP a l'MC i la dada es… | Diagrama que mostra els quatre passos d'una fallada de memò… |
| `fig-cd-descomposicio-bits` | `A7.qmd:275` | `22_figs_originals/A7_cd_descomposicio_bits.svg` | Inkscape |  | 1 | Descomposició dels bits d'una adreça en etiqueta, índex i desplaçament per a una memòria … | Descomposició dels 32 bits de l'adreça 0x100100F8 en etique… |
| `fig-cd-diagrama` | `A7.qmd:308` | `MC.toml:A7_cd_diagrama` | gen_MC.py |  | 1 | Diagrama de blocs d'una lectura en una memòria cau de correspondència directa. | L'adreça es parteix en etiqueta, índex i desplaçament. L'ín… |
| `fig-assoc-conjunts-taula` | `A7.qmd:351` | `MC.toml:A7_assoc_conjunts_taula` | gen_MC.py |  | 1 | Organització d'una memòria cau associativa per conjunts de 4 conjunts i 3 vies: el bloc d… | A dalt, el bloc 1 de l'MP, bytes 4 a 7, amb les adreces en … |
| `fig-assoc-conjunts-diagrama` | `A7.qmd:369` | `MC.toml:A7_assoc_conjunts_diagrama` | gen_MC.py |  | 1 | Diagrama de blocs d'una lectura en una memòria cau associativa per conjunts de $N$ vies. | L'adreça es parteix en etiqueta, índex i desplaçament. L'ín… |
| `fig-ca-diagrama` | `A7.qmd:399` | `MC.toml:A7_ca_diagrama` | gen_MC.py |  | 1 | Diagrama de blocs d'una lectura en una memòria cau completament associativa: cal comparar… | L'adreça es parteix en etiqueta i desplaçament, sense índex… |
| `fig-lru-exemple` | `A7.qmd:466` | `MC.toml:A7_lru_exemple` | gen_MC.py | `tip-lru-exemple` | 0 | Evolució de la memòria cau associativa per conjunts de 2 vies amb reemplaçament LRU per a… | MC de 4 conjunts de 2 vies amb blocs de 4 bytes, inicialmen… |
| `fig-escriptura-dirty-bit` | `A7.qmd:500` | `MC.toml:A7_escriptura_dirty_bit` | gen_MC.py |  | 1 | Estructura d'una línia de memòria cau amb escriptura retardada: el bit de modificació $D$… | La mateixa taula de 4 línies amb una columna més, D, emmarc… |
| `fig-escriptura-estat-inicial` | `A7.qmd:559` | `(subfigures)` | — |  | 1 | Estat de la memòria cau al final de la seqüència inicial de 5 lectures, partint d'una MC … |  |
| `fig-escriptura-estat-inicial-sequencia` | `A7.qmd:560` | `MC.toml:A7_escriptura_estat_inicial` | gen_MC.py |  | 0 | Pas a pas: l'MP, cada lectura i l'estat de l'MC després de l'accés. | MC de correspondència directa de 2 línies amb blocs de 4 by… |
| `fig-escriptura-estat-inicial-traca` | `A7.qmd:576` | `MC.toml:A7_escriptura_estat_inicial_traca` | gen_MC.py |  | 0 | En forma de traça: una fila per lectura, amb el bloc que conté cada línia de l'MC després… | Taula amb una fila per lectura (bytes 0, 2, 4, 6 i 8): bloc… |
| `fig-escriptura-immediata-assignacio` | `A7.qmd:601` | `MC.toml:A7_escriptura_immediata_amb_assignacio` | gen_MC.py | `tip-escriptura-immediata-assignacio` | 0 | Escriptura immediata amb assignació: en cas d'encert s'escriu a MC i MP simultàniament; e… | Partint de l'estat inicial (línia 0: bloc 2; línia 1: bloc … |
| `fig-escriptura-immediata-sense-assignacio` | `A7.qmd:627` | `MC.toml:A7_escriptura_immediata_sense_assignacio` | gen_MC.py | `tip-escriptura-immediata-sense-assignacio` | 0 | Escriptura immediata sense assignació: en cas d'encert s'escriu a MC i MP; en cas de fall… | Partint de l'estat inicial (línia 0: bloc 2; línia 1: bloc … |
| `fig-escriptura-retardada` | `A7.qmd:654` | `MC.toml:A7_escriptura_retardada` | gen_MC.py | `tip-escriptura-retardada` | 0 | Escriptura retardada amb assignació: en cas d'encert s'escriu únicament a l'MC i es posa … | Partint de l'estat inicial amb D = 0 a les dues línies. Esc… |
| `fig-mc-politiques-resum` | `A7.qmd:676` | `22_figs_originals/A7_mc_politiques_resum__graphviz.svg` | Graphviz |  | 1 | Resum de les polítiques de memòria cau. | Un arbre que surt d'MC amb tres branques. Emplaçament: corr… |
| `fig-texe-diagrama` | `A7.qmd:815` | `22_figs_originals/A7_texe_diagrama.svg` | SVG natiu |  | 1 | Impacte d'una fallada de memòria cau en el temps d'execució: els cicles de penalització s… | Dues files de tres instruccions (lw, add, lw) etapa per eta… |
| `fig-tipus-fallades` | `A7.qmd:849` | `22_figs_originals/A7_tipus_fallades.svg` | SVG natiu |  | 1 | Taxa de fallades segons la mida de la memòria cau i el grau d'associativitat, per a un pr… | Gràfica qualitativa de la taxa de fallades en funció de la … |
| `fig-conflicte-exemple` | `A7.qmd:922` | `MC.toml:A7_conflicte_exemple` | gen_MC.py |  | 1 | Fallades de conflicte en el recorregut paral·lel de dos vectors amb una memòria cau de co… | Taula de traça dels 16 accessos de f(A, B) en una MC de cor… |
| `fig-capacitat-exemple` | `A7.qmd:961` | `MC.toml:A7_capacitat_exemple` | gen_MC.py |  | 1 | Fallades de capacitat en una memòria cau completament associativa de 4 línies amb reempla… | Taula de traça de g(V) en una MC completament associativa d… |
| `fig-multinivell-diagrama` | `A7.qmd:992` | `22_figs_originals/A7_multinivell_diagrama.svg` | SVG natiu |  | 1 | Les memòries cau multinivell redueixen la penalització de les fallades de L1: les que enc… | Tres configuracions: (a) la CPU connectada a l’MP, amb un t… |
| `fig-multinivell-multicore` | `A7.qmd:1057` | `22_figs_originals/A7_multinivell_multicore.svg` | SVG natiu |  | 1 | Jerarquia de memòries cau en un processador multinucli: L1 i L2 són privades de cada nucl… | Xip de quatre nuclis. Cada nucli té una L1 d'instruccions (… |
| `fig-i9-13900k-die` | `A7.qmd:1076` | `23_figs_externes/A7_Intel_Core_i9-13900K_Labelled_Die_Shot_800x368.jpg` | ràster |  | 1 | Fotografia del dau (bloc de sil·lici, *die*) de l'Intel Core i9-13900K (*Raptor Lake*, 20… |  |
| `fig-mv-espais` | `A8.qmd:28` | `22_figs_originals/A8_mv_espais.svg` | SVG natiu |  | 1 | Cada procés disposa d'un espai d'adreçament lògic propi i independent, de `0x00000000` a … | A banda i banda, l'espai lògic de dos processos, de 0x00000… |
| `fig-mv-jerarquia` | `A8.qmd:49` | `22_figs_originals/A8_mv_jerarquia.svg` | SVG natiu |  | 1 | Jerarquia de memòria en un computador amb memòria virtual. Els temps d'accés són ordres d… | Piràmide de quatre nivells, de dalt a baix: registres, memò… |
| `fig-mv-pagines-marcs` | `A8.qmd:92` | `22_figs_originals/A8_mv_pagines_marcs.svg` | SVG natiu |  | 3 | Números de pàgina lògica (VPN) de dos processos, a l'esquerra, i números de pàgina física… | A banda i banda, l'espai lògic de dos processos, de 0x00000… |
| `fig-mv-traduccio` | `A8.qmd:116` | `22_figs_originals/A8_mv_traduccio.svg` | SVG natiu |  | 1 | Traducció d'una adreça lògica a una adreça física: el VPN (20 bits) es tradueix a PPN (2 … | A dalt, l'adreça lògica de 32 bits, amb els números de bit … |
| `fig-mv-taula-pagines` | `A8.qmd:137` | `22_figs_originals/A8_mv_taula_pagines.svg` | SVG natiu |  | 1 | Donat un VPN, la taula de pàgines indica si la pàgina és a la memòria física (bit V) i en… | A dalt, l'adreça lògica de 32 bits: VPN, de 20 bits, i desp… |
| `fig-mv-traduccio-exemple` | `A8.qmd:185` | `22_figs_originals/A8_mv_traduccio_exemple.svg` | SVG natiu |  | 1 | Traducció de l'adreça lògica `0x00001801` mitjançant la taula de pàgines del procés 2 de … | Traducció de l'adreça lògica 0x00001801 amb la taula de pàg… |
| `fig-mv-taula-multinivell` | `A8.qmd:212` | `22_figs_originals/A8_mv_taula_multinivell.svg` | SVG natiu |  | 1 | Taula de pàgines de dos nivells (Sv32). Els 10 bits de més pes del VPN, VPN[1], indexen l… | A dalt, l'adreça lògica de 32 bits dividida en VPN[1], de 1… |
| `fig-mv-tlb-estructura` | `A8.qmd:309` | `22_figs_originals/A8_mv_tlb_estructura.svg` | SVG natiu |  | 1 | El TLB emmagatzema una còpia de les entrades de la taula de pàgines utilitzades més recen… | A l'esquerra, la taula de pàgines, a la memòria principal, … |
| `fig-mv-flux-traduccio` | `A8.qmd:373` | `22_figs_originals/A8_mv_flux_traduccio.svg` | SVG natiu |  | 2 | Flux complet de traducció d'una adreça en un sistema amb TLB i memòria virtual. A l'esque… | Diagrama de flux en tres columnes, agrupades en dues zones … |
| `fig-mv-comparticio` | `A8.qmd:430` | `22_figs_originals/A8_mv_comparticio.svg` | SVG natiu |  | 1 | Compartició d'una pàgina física entre dos processos (@tip-mv-comparticio): P1 la té assig… | A l'esquerra, les taules de pàgines de P1, a dalt, en blau,… |
| `fig-mv-pipt` | `A8.qmd:458` | `22_figs_originals/A8_mv_pipt.svg` | SVG natiu |  | 2 | Memòria cau indexada físicament (PIPT): la traducció i l'accés a la memòria cau es fan en… | Diagrama de blocs en una fila: la CPU envia l'adreça lògica… |
| `fig-mv-vipt` | `A8.qmd:491` | `22_figs_originals/A8_mv_vipt.svg` | SVG natiu |  | 1 | Memòria cau VIPT: la indexació de la memòria cau i la traducció del TLB es fan en paral·l… | La CPU genera l'adreça lògica, dividida en VPN i desplaçame… |
| `fig-mv-tlb-exemple` | `A8.qmd:590` | `22_figs_originals/A8_mv_exemple_tlb.svg` | SVG natiu |  | 1 | Traça dels cinc accessos de @tip-mv-tlb-exemple: l'estat inicial i, per a cada accés, el … | A dalt, l'estat inicial: el TLB, amb tres entrades vàlides … |
| `fig-cicle-interrupcio` | `A9.qmd:718` | `22_figs_originals/A9_cicle_interrupcio.svg` | Inkscape |  | 1 | Cicle de vida d'una interrupció: el dispositiu fa la petició mentre s'executa la instrucc… | Una línia de temps d'esquerra a dreta en tres trams: execuc… |
| `fig-ba-funcio-a` | `S3.qmd:626` | `BA.toml:S3_ba_A` | gen_BA.py |  | 1 | Bloc d'activació de la funció `A`: el vector `r` al desplaçament `+0` i l'alineació als b… | Bloc d'activació de 12 bytes, d'adreces baixes (sp) a altes… |
| `fig-ba-variancia` | `S5.qmd:755` | `BA.toml:S5_ba_variancia` | gen_BA.py |  | 1 | Bloc d'activació de `variancia`: el vector `vquadrats` al desplaçament `+0` i els registr… | Bloc d'activació de 420 bytes, d'adreces baixes (sp) a alte… |
| `fig-ba-moda` | `L3.qmd:341` | `BA.toml:L3_ba_moda` | gen_BA.py |  | 1 | Bloc d'activació de `moda`: el vector `histo` al desplaçament `+0` i els registres desats… | Bloc d'activació de 60 bytes, d'adreces baixes (sp) a altes… |
| `—` | `A2.qmd:270` | `registres.toml:compendi_registres_RIS` | gen_regs.py (COMPENDIS) | `nte-instruccions-tipus` | 0 |  |  |
| `—` | `A2.qmd:1215` | `registres.toml:A2_instruccio_tipus_R` | gen_regs.py | `nte-instruccions-Tipus-R` | 0 |  |  |
| `—` | `A2.qmd:1274` | `registres.toml:A2_instruccio_tipus_I` | gen_regs.py | `nte-instruccions-Tipus-I` | 0 |  |  |
| `—` | `A2.qmd:1295` | `registres.toml:A2_instruccio_tipus_U` | gen_regs.py | `nte-format-u` | 0 |  |  |
| `—` | `A2.qmd:1337` | `registres.toml:A2_instruccio_tipus_S` | gen_regs.py | `nte-instruccions-Tipus-S` | 0 |  |  |
| `—` | `A3.qmd:407` | `registres.toml:A3_instruccio_tipus_B` | gen_regs.py | `nte-format-b` | 0 |  |  |
| `—` | `A3.qmd:515` | `registres.toml:A3_instruccio_tipus_J` | gen_regs.py | `nte-format-j` | 0 |  |  |
| `—` | `A5.qmd:755` | `registres.toml:A5_fcsr` | gen_regs.py | `nte-fcsr` | 0 |  |  |
| `—` | `A8.qmd:76` | `22_figs_originals/A8_mv_adreca_exemple.svg` | SVG natiu |  | 0 |  |  |
| `—` | `A9.qmd:122` | `registres.toml:A9_mcause` | gen_regs.py | `nte-mcause-mes-rellevants` | 0 |  |  |
| `—` | `A9.qmd:152` | `registres.toml:A9_mepc` | gen_regs.py | `nte-mepc` | 0 |  |  |
| `—` | `A9.qmd:171` | `registres.toml:A9_mstatus` | gen_regs.py | `nte-mstatus` | 0 |  |  |
| `—` | `A9.qmd:194` | `registres.toml:A9_mtvec` | gen_regs.py | `nte-mtvec` | 0 |  |  |
| `—` | `A9.qmd:237` | `registres.toml:A9_mip` | gen_regs.py | `nte-mip-mie` | 0 |  |  |
| `—` | `A9.qmd:249` | `registres.toml:A9_mie` | gen_regs.py | `nte-mip-mie` | 0 |  |  |
| `—` | `A9.qmd:809` | `registres.toml:A9_satp` | gen_regs.py | `nte-satp` | 0 |  |  |
| `—` | `11_riscv.qmd:40` | `registres.toml:compendi_registres` | gen_regs.py (COMPENDIS) | `nte-rv-instruccions-formats-detall` | 0 |  |  |
| `—` | `11_riscv.qmd:270` | `registres.toml:A5_fcsr` | gen_regs.py | `nte-rv-fcsr` | 0 |  |  |
| `—` | `11_riscv.qmd:444` | `registres.toml:A9_mepc` | gen_regs.py | `nte-rv-mepc` | 0 |  |  |
| `—` | `11_riscv.qmd:462` | `registres.toml:A9_mstatus` | gen_regs.py | `nte-rv-mstatus` | 0 |  |  |
| `—` | `11_riscv.qmd:480` | `registres.toml:A9_mtvec` | gen_regs.py | `nte-rv-mtvec` | 0 |  |  |
| `—` | `11_riscv.qmd:508` | `registres.toml:A9_mip` | gen_regs.py | `nte-rv-mip-mie` | 0 |  |  |
| `—` | `11_riscv.qmd:520` | `registres.toml:A9_mie` | gen_regs.py | `nte-rv-mip-mie` | 0 |  |  |
| `—` | `11_riscv.qmd:565` | `registres.toml:A9_satp` | gen_regs.py | `nte-rv-satp` | 0 |  |  |
| `—` | `14_LICENSE.qmd:5` | `23_figs_externes/by-nc-sa.eu.png` | ràster |  | 0 |  |  |

## Fitxers font

| Fitxer | Ús | Origen | Amplada | `<title>` | `<desc>` | Textos | Fora de paleta | Duplicat de |
| :--- | :--- | :--- | ---: | :---: | :---: | ---: | :--- | :--- |
| `22_figs_originals/A1_flux_compilacio.svg` | A1.qmd:58, A1.qmd:65 | Inkscape | 901 | sí | sí | 20 |  |  |
| `22_figs_originals/A1_picopi_fases.svg` | A1.qmd:227, A1.qmd:234 | Inkscape | 680 | sí | sí | 39 |  |  |
| `22_figs_originals/A1_von_neumann.svg` | A1.qmd:363, A1.qmd:370 | Inkscape | 700 | sí | sí | 26 |  |  |
| `22_figs_originals/A2_acces_vector.svg` | A2.qmd:1913, A2.qmd:1920 | SVG natiu | 260 | sí | sí | 13 |  |  |
| `22_figs_originals/A2_endianness_regla_pi.svg` | A2.qmd:1069, A2.qmd:1076 | Inkscape | 285 | sí | sí | 15 |  |  |
| `22_figs_originals/A3_ba_exemple.svg` | **orfe** | Inkscape | 316 | no | no | 20 |  |  |
| `22_figs_originals/A3_ba_func.svg` | **orfe** | Inkscape | 326 | sí | sí | 11 |  |  |
| `22_figs_originals/A3_ba_general.svg` | **orfe** | Inkscape | 326 | sí | sí | 12 |  |  |
| `22_figs_originals/A3_ba_multi.svg` | **orfe** | Inkscape | 326 | no | no | 7 |  |  |
| `22_figs_originals/A3_compilacio_separada.svg` | A3.qmd:1878, A3.qmd:1885 | Inkscape | 610 | sí | sí | 13 |  |  |
| `22_figs_originals/A3_deps_exemple.svg` | A3.qmd:1731, A3.qmd:1738 | Inkscape | 340 | sí | sí | 5 |  |  |
| `22_figs_originals/A3_deps_multi.svg` | A3.qmd:1623, A3.qmd:1630 | Inkscape | 290 | sí | sí | 3 |  |  |
| `22_figs_originals/A3_flux_gcc_complet.svg` | A3.qmd:2072, A3.qmd:2079 | SVG natiu | 490 | sí | sí | 21 |  |  |
| `22_figs_originals/A3_mapa_memoria.svg` | **orfe** | Inkscape | 326 | sí | sí | 19 |  |  |
| `22_figs_originals/A3_pila_multinivell.svg` | **orfe** | Inkscape | 510 | sí | sí | 30 |  |  |
| `22_figs_originals/A3_pila_uninivell.svg` | **orfe** | Inkscape | 310 | sí | sí | 18 |  |  |
| `22_figs_originals/A4_divisor_sequencial.svg` | A4.qmd:394, A4.qmd:401 | SVG natiu | 440 | sí | sí | 16 |  |  |
| `22_figs_originals/A4_matriu_emmagatzematge.svg` | A4.qmd:521, A4.qmd:528 | SVG natiu | 680 | sí | sí | 50 |  |  |
| `22_figs_originals/A4_matriu_offset_ij.svg` | A4.qmd:562, A4.qmd:569 | SVG natiu | 680 | sí | sí | 12 |  |  |
| `22_figs_originals/A4_matriu_recorreguts_strides.svg` | A4.qmd:847, A4.qmd:854 | SVG natiu | 680 | sí | sí | 8 |  |  |
| `22_figs_originals/A4_multiplicador_arbre.svg` | A4.qmd:252, A4.qmd:259 | SVG natiu | 440 | sí | sí | 22 |  |  |
| `22_figs_originals/A4_multiplicador_sequencial.svg` | A4.qmd:190, A4.qmd:197 | SVG natiu | 420 | sí | sí | 15 |  |  |
| `22_figs_originals/A4_semisumador_sumador_complet.svg` | A4.qmd:80, A4.qmd:87 | SVG natiu | 590 | sí | sí | 24 |  |  |
| `22_figs_originals/A4_sumador_propagacio_rossec.svg` | A4.qmd:104, A4.qmd:97 | SVG natiu | 750 | sí | sí | 28 |  |  |
| `22_figs_originals/A5_exponent.svg` | A5.qmd:135, A5.qmd:142 | Inkscape | 740 | sí | sí | 24 |  |  |
| `22_figs_originals/A5_grs_esquema.svg` | A5.qmd:437, A5.qmd:444 | SVG natiu | 620 | sí | sí | 20 |  |  |
| `22_figs_originals/A5_recta_global.svg` | A5.qmd:270, A5.qmd:277 | SVG natiu | 950 | sí | sí | 86 |  |  |
| `22_figs_originals/A5_recta_zoom_zero.svg` | A5.qmd:387, A5.qmd:394 | Inkscape | 900 | sí | sí | 74 |  |  |
| `22_figs_originals/A5_taula_codificacions.svg` | A5.qmd:346, A5.qmd:353 | exportació LO Draw | 11509.377 | sí | sí | 12 |  |  |
| `22_figs_originals/A6_amdahl.svg` | A6.qmd:217, A6.qmd:224 | Inkscape | 220 | sí | sí | 15 |  |  |
| `22_figs_originals/A6_not_0_1.svg` | A6.qmd:326, A6.qmd:333 | Inkscape | 386 | sí | sí | 14 |  |  |
| `22_figs_originals/A6_not_1_0.svg` | A6.qmd:309, A6.qmd:316 | Inkscape | 386 | sí | sí | 14 |  |  |
| `22_figs_originals/A6_not_cmos.svg` | A6.qmd:290, A6.qmd:297 | Inkscape | 360 | sí | sí | 8 |  |  |
| `22_figs_originals/A6_tc_tc_prima.svg` | A6.qmd:149, A6.qmd:156 | Inkscape | 284 | sí | sí | 10 |  |  |
| `22_figs_originals/A7_capacitat_exemple_bucle_primera_passada.svg` | **orfe** | Inkscape | 800 | sí | sí | 235 |  |  |
| `22_figs_originals/A7_capacitat_exemple_bucle_segona_passada.svg` | **orfe** | Inkscape | 800 | sí | sí | 266 |  |  |
| `22_figs_originals/A7_cd_descomposicio_bits.svg` | A7.qmd:278, A7.qmd:285 | Inkscape | 545 | sí | sí | 21 |  |  |
| `22_figs_originals/A7_conflicte_exemple.svg` | **orfe** | Inkscape | 800 | sí | sí | 120 | #000000 |  |
| `22_figs_originals/A7_escriptura_estat_inicial.svg` | **orfe** | Inkscape | 800 | sí | sí | 167 | #000000 |  |
| `22_figs_originals/A7_escriptura_immediata_amb_assignacio.svg` | **orfe** | Inkscape | 800 | sí | sí | 101 | #000000 |  |
| `22_figs_originals/A7_escriptura_immediata_sense_assignacio.svg` | **orfe** | Inkscape | 800 | sí | sí | 100 | #000000 |  |
| `22_figs_originals/A7_escriptura_retardada.svg` | **orfe** | Inkscape | 800 | sí | sí | 163 | #000000 |  |
| `22_figs_originals/A7_gap_processador_memoria.svg` | A7.qmd:34, A7.qmd:41 | SVG natiu | 620 | sí | sí | 17 |  |  |
| `22_figs_originals/A7_jerarquia_piramide.svg` | A7.qmd:106, A7.qmd:99 | SVG natiu | 580 | sí | sí | 7 |  |  |
| `22_figs_originals/A7_lru_exemple.svg` | **orfe** | Inkscape | 800 | sí | sí | 237 | #000000 |  |
| `22_figs_originals/A7_mc_descomposicio_bits.svg` | A7.qmd:180, A7.qmd:187 | Inkscape | 590 | sí | sí | 18 |  |  |
| `22_figs_originals/A7_mc_encert.svg` | A7.qmd:219, A7.qmd:226 | Inkscape | 575 | sí | sí | 30 |  |  |
| `22_figs_originals/A7_mc_fallada.svg` | A7.qmd:241, A7.qmd:248 | Inkscape | 575 | sí | sí | 48 |  |  |
| `22_figs_originals/A7_mc_politiques_resum__graphviz.svg` | A7.qmd:679, A7.qmd:686 | Graphviz | 468 | sí | sí | 19 |  |  |
| `22_figs_originals/A7_multinivell_diagrama.svg` | A7.qmd:1002, A7.qmd:995 | SVG natiu | 660 | sí | sí | 22 |  |  |
| `22_figs_originals/A7_multinivell_multicore.svg` | A7.qmd:1060, A7.qmd:1067 | SVG natiu | 660 | sí | sí | 20 |  |  |
| `22_figs_originals/A7_texe_diagrama.svg` | A7.qmd:818, A7.qmd:825 | SVG natiu | 802 | sí | sí | 59 |  |  |
| `22_figs_originals/A7_tipus_fallades.svg` | A7.qmd:852, A7.qmd:859 | SVG natiu | 640 | sí | sí | 10 |  |  |
| `22_figs_originals/A8_mv_adreca_exemple.svg` | A8.qmd:76, A8.qmd:83 | SVG natiu | 680 | sí | sí | 7 |  |  |
| `22_figs_originals/A8_mv_comparticio.svg` | A8.qmd:433, A8.qmd:440 | SVG natiu | 680 | sí | sí | 109 |  |  |
| `22_figs_originals/A8_mv_espais.svg` | A8.qmd:31, A8.qmd:38 | SVG natiu | 680 | sí | sí | 49 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb.svg` | A8.qmd:594, A8.qmd:602 | SVG natiu | 680 | sí | sí | 237 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb_pas0.svg` | fotograma de `A8_mv_exemple_tlb.svg` | SVG natiu | 680 | sí | sí | 75 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb_pas1.svg` | fotograma de `A8_mv_exemple_tlb.svg` | SVG natiu | 680 | sí | sí | 76 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb_pas2.svg` | fotograma de `A8_mv_exemple_tlb.svg` | SVG natiu | 680 | sí | sí | 76 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb_pas3.svg` | fotograma de `A8_mv_exemple_tlb.svg` | SVG natiu | 680 | sí | sí | 76 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb_pas4.svg` | fotograma de `A8_mv_exemple_tlb.svg` | SVG natiu | 680 | sí | sí | 76 |  |  |
| `22_figs_originals/A8_mv_exemple_tlb_pas5.svg` | fotograma de `A8_mv_exemple_tlb.svg` | SVG natiu | 680 | sí | sí | 76 |  |  |
| `22_figs_originals/A8_mv_flux_traduccio.svg` | A8.qmd:376, A8.qmd:383 | SVG natiu | 960 | sí | sí | 57 |  |  |
| `22_figs_originals/A8_mv_jerarquia.svg` | A8.qmd:52, A8.qmd:59 | SVG natiu | 680 | sí | sí | 17 |  |  |
| `22_figs_originals/A8_mv_pagines_marcs.svg` | A8.qmd:102, A8.qmd:95 | SVG natiu | 680 | sí | sí | 41 |  |  |
| `22_figs_originals/A8_mv_pipt.svg` | A8.qmd:461, A8.qmd:468 | SVG natiu | 680 | sí | sí | 15 |  |  |
| `22_figs_originals/A8_mv_taula_multinivell.svg` | A8.qmd:215, A8.qmd:222 | SVG natiu | 680 | sí | sí | 43 |  |  |
| `22_figs_originals/A8_mv_taula_pagines.svg` | A8.qmd:140, A8.qmd:147 | SVG natiu | 680 | sí | sí | 83 |  |  |
| `22_figs_originals/A8_mv_tlb_estructura.svg` | A8.qmd:312, A8.qmd:319 | SVG natiu | 680 | sí | sí | 75 |  |  |
| `22_figs_originals/A8_mv_traduccio.svg` | A8.qmd:119, A8.qmd:126 | SVG natiu | 680 | sí | sí | 57 |  |  |
| `22_figs_originals/A8_mv_traduccio_exemple.svg` | A8.qmd:188, A8.qmd:195 | SVG natiu | 680 | sí | sí | 91 |  |  |
| `22_figs_originals/A8_mv_vipt.svg` | A8.qmd:494, A8.qmd:501 | SVG natiu | 680 | sí | sí | 22 |  |  |
| `22_figs_originals/A9_cicle_interrupcio.svg` | A9.qmd:721, A9.qmd:728 | Inkscape | 680 | sí | sí | 17 |  |  |
| `23_figs_externes/A7_Intel_Core_i9-13900K_Labelled_Die_Shot_800x368.jpg` | A7.qmd:1078 | ràster |  | no | no | 0 |  |  |
| `23_figs_externes/by-nc-sa.eu.png` | 14_LICENSE.qmd:5 | ràster |  | no | no | 0 |  |  |
| `registres.toml:A2_instruccio_tipus_R` | A2.qmd:1215, A2.qmd:1222 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A2_instruccio_tipus_I` | A2.qmd:1274, A2.qmd:1281 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A2_instruccio_tipus_S` | A2.qmd:1337, A2.qmd:1344 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A2_instruccio_tipus_U` | A2.qmd:1295, A2.qmd:1302 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A3_instruccio_tipus_B` | A3.qmd:407, A3.qmd:414 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A3_instruccio_tipus_J` | A3.qmd:515, A3.qmd:522 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A5_instruccio_tipus_R4` | A5.qmd:878, A5.qmd:885 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A5_ieee754_format_registre` | A5.qmd:86, A5.qmd:93 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A5_fcsr` | 11_riscv.qmd:270, 11_riscv.qmd:277 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_mstatus` | 11_riscv.qmd:462, 11_riscv.qmd:469 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_mtvec` | 11_riscv.qmd:480, 11_riscv.qmd:487 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_mepc` | 11_riscv.qmd:444, 11_riscv.qmd:451 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_mcause` | A9.qmd:122, A9.qmd:129 | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_mip` | 11_riscv.qmd:508, 11_riscv.qmd:515 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_mie` | 11_riscv.qmd:520, 11_riscv.qmd:527 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `registres.toml:A9_satp` | 11_riscv.qmd:565, 11_riscv.qmd:572 … | gen_regs.py |  | sí | sí | 0 |  |  |
| `BA.toml:A3_ba_exemple` | A3.qmd:1778, A3.qmd:1785 | gen_BA.py |  | sí | sí | 0 |  |  |
| `BA.toml:A3_ba_multi` | A3.qmd:1656, A3.qmd:1663 | gen_BA.py |  | sí | sí | 0 |  |  |
| `BA.toml:A3_ba_general` | A3.qmd:1429, A3.qmd:1436 | gen_BA.py |  | sí | sí | 0 |  |  |
| `BA.toml:A3_ba_func` | A3.qmd:1458, A3.qmd:1465 | gen_BA.py |  | sí | sí | 0 |  |  |
| `BA.toml:L3_ba_moda` | L3.qmd:344, L3.qmd:351 | gen_BA.py |  | sí | sí | 0 |  |  |
| `BA.toml:S3_ba_A` | S3.qmd:629, S3.qmd:636 | gen_BA.py |  | sí | sí | 0 |  |  |
| `BA.toml:S5_ba_variancia` | S5.qmd:758, S5.qmd:765 | gen_BA.py |  | sí | sí | 0 |  |  |
| `mapa.toml:A3_mapa_memoria` | A3.qmd:1024, A3.qmd:1031 | gen_mapa.py |  | sí | sí | 0 |  |  |
| `mapa.toml:A3_pila_uninivell` | A3.qmd:1388, A3.qmd:1395 | gen_mapa.py |  | sí | sí | 0 |  |  |
| `mapa.toml:A3_pila_multinivell` | A3.qmd:1509, A3.qmd:1516 | gen_mapa.py |  | sí | sí | 0 |  |  |
| `subrutines.toml:A3_deps_multi` | A3.qmd:1637, A3.qmd:1644 | gen_subrutines.py |  | sí | sí | 0 |  |  |
| `subrutines.toml:A3_deps_exemple` | A3.qmd:1745, A3.qmd:1752 | gen_subrutines.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_escriptura_estat_inicial` | A7.qmd:564, A7.qmd:572 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_escriptura_estat_inicial_traca` | A7.qmd:579, A7.qmd:586 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_escriptura_immediata_amb_assignacio` | A7.qmd:605, A7.qmd:613 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_escriptura_immediata_sense_assignacio` | A7.qmd:631, A7.qmd:639 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_escriptura_retardada` | A7.qmd:658, A7.qmd:666 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_lru_exemple` | A7.qmd:470, A7.qmd:478 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_conflicte_exemple` | A7.qmd:926, A7.qmd:934 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_capacitat_exemple` | A7.qmd:965, A7.qmd:973 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_cd_diagrama` | A7.qmd:311, A7.qmd:318 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_assoc_conjunts_diagrama` | A7.qmd:372, A7.qmd:379 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_ca_diagrama` | A7.qmd:402, A7.qmd:409 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_mc_organitzacio` | A7.qmd:145, A7.qmd:152 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_assoc_conjunts_taula` | A7.qmd:354, A7.qmd:361 | gen_MC.py |  | sí | sí | 0 |  |  |
| `MC.toml:A7_escriptura_dirty_bit` | A7.qmd:503, A7.qmd:510 | gen_MC.py |  | sí | sí | 0 |  |  |
| `memoria.toml:A2_memoria_creix_avall` | A2.qmd:989, A2.qmd:996 | gen_memoria.py |  | sí | sí | 0 |  |  |
| `memoria.toml:A2_big_endian` | A2.qmd:1029, A2.qmd:1036 | gen_memoria.py |  | sí | sí | 0 |  |  |
| `memoria.toml:A2_little_endian` | A2.qmd:1043, A2.qmd:1050 | gen_memoria.py |  | sí | sí | 0 |  |  |
| `registres.toml:compendi_registres` | 11_riscv.qmd:40, 11_riscv.qmd:47 | gen_regs.py (COMPENDIS) |  | sí | sí | 0 |  |  |
| `registres.toml:compendi_registres_RIS` | A2.qmd:270, A2.qmd:277 | gen_regs.py (COMPENDIS) |  | sí | sí | 0 |  |  |

## Avisos

### Originals amb una versió generada al llibre (es conserven, p. ex. per a les diapositives) (15)

- `22_figs_originals/A3_ba_exemple.svg`
- `22_figs_originals/A3_ba_func.svg`
- `22_figs_originals/A3_ba_general.svg`
- `22_figs_originals/A3_ba_multi.svg`
- `22_figs_originals/A3_mapa_memoria.svg`
- `22_figs_originals/A3_pila_multinivell.svg`
- `22_figs_originals/A3_pila_uninivell.svg`
- `22_figs_originals/A7_capacitat_exemple_bucle_primera_passada.svg`
- `22_figs_originals/A7_capacitat_exemple_bucle_segona_passada.svg`
- `22_figs_originals/A7_conflicte_exemple.svg`
- `22_figs_originals/A7_escriptura_estat_inicial.svg`
- `22_figs_originals/A7_escriptura_immediata_amb_assignacio.svg`
- `22_figs_originals/A7_escriptura_immediata_sense_assignacio.svg`
- `22_figs_originals/A7_escriptura_retardada.svg`
- `22_figs_originals/A7_lru_exemple.svg`
