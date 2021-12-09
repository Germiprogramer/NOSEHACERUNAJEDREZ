tablero =[
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ']
]

def printeartablero(tablero):
    contador_indice = 0
    for tablero[contador_indice] in tablero:
        print(tablero[contador_indice])
        contador_indice += 1

REY_BLANCO = chr(0x2654)
REINA_BLANCO = chr(0x2655)
TORRE_BLANCO = chr(0x2656)
ALFIL_BLANCO = chr(0x2657)
CABALLO_BLANCO = chr(0x2658)
PEÓN_BLANCO = chr(0x2659)

REY_NEGRO = chr(0x265A)
REINA_NEGRO = chr(0x265B)
TORRE_NEGRO = chr(0x265C)
ALFIL_NEGRO = chr(0x265D)
CABALLO_NEGRO = chr(0x265E)
PEÓN_NEGRO = chr(0x265F)

#posicioninicialpeonesblancos
PB1y = 6
PB1x = 0
(tablero[PB1y])[PB1x] = PEÓN_BLANCO

def mov_peonblanco1(PB1y, PB1x, tablero):
    pb1 = input("A DÓNDE DESEAS MOVER EL PEON BLANCO?")

mov_peonblanco1(PB1y, PB1x, tablero)

(tablero[6])[1] = PEÓN_BLANCO
(tablero[6])[2] = PEÓN_BLANCO
(tablero[6])[3] = PEÓN_BLANCO
(tablero[6])[4] = PEÓN_BLANCO
(tablero[6])[5] = PEÓN_BLANCO
(tablero[6])[6] = PEÓN_BLANCO
(tablero[6])[7] = PEÓN_BLANCO


#posicioninicialpeonesnegros
(tablero[1])[0] = PEÓN_NEGRO
(tablero[1])[1] = PEÓN_NEGRO
(tablero[1])[2] = PEÓN_NEGRO
(tablero[1])[3] = PEÓN_NEGRO
(tablero[1])[4] = PEÓN_NEGRO
(tablero[1])[5] = PEÓN_NEGRO
(tablero[1])[6] = PEÓN_NEGRO
(tablero[1])[7] = PEÓN_NEGRO









fichero = input("ESCOGE UN NOMBRE PARA EL FICHERO>>>>")
f = open(fichero, "a+", encoding="utf-8")



printeartablero(tablero)