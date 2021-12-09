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



fichero = input("ESCOGE UN NOMBRE PARA EL FICHERO>>>>")
f = open(fichero, "a+", encoding="utf-8")



printeartablero(tablero)