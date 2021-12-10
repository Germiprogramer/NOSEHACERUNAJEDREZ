from os import supports_effective_ids, terminal_size


tablero =[
    [' ','1','2','3','4','5','6','7','8'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' '],
    ['2',' ',' ',' ',' ',' ',' ',' ',' '],
    ['3',' ',' ',' ',' ',' ',' ',' ',' '],
    ['4',' ',' ',' ',' ',' ',' ',' ',' '],
    ['5',' ',' ',' ',' ',' ',' ',' ',' '],
    ['6',' ',' ',' ',' ',' ',' ',' ',' '],
    ['7',' ',' ',' ',' ',' ',' ',' ',' '],
    ['8',' ',' ',' ',' ',' ',' ',' ',' '],
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

#def moverunapieza(tablero,a,b,c,d,e,f,g,h,uno,dos,tres,cuatro,cinco,seis,siete,ocho):
    #fila = input("fila donde ESTÁ LA PIEZA QUE DESEAS MOVER >>> ")
    #columna = input("columna donde esta la pieza que quieres mover")
    #(tablero[fila])[columna] = " "
    #(tablero[fila])[columna] = str((tablero[fila])[columna])
    #printeartablero(tablero)






(tablero[7])[1] = PEÓN_BLANCO
(tablero[7])[2] = PEÓN_BLANCO
(tablero[7])[3] = PEÓN_BLANCO
(tablero[7])[4] = PEÓN_BLANCO
(tablero[7])[5] = PEÓN_BLANCO
(tablero[7])[6] = PEÓN_BLANCO
(tablero[7])[7] = PEÓN_BLANCO
(tablero[7])[8] = PEÓN_BLANCO


#posicioninicialpeonesnegros
(tablero[2])[1] = PEÓN_NEGRO
(tablero[2])[2] = PEÓN_NEGRO
(tablero[2])[3] = PEÓN_NEGRO
(tablero[2])[4] = PEÓN_NEGRO
(tablero[2])[5] = PEÓN_NEGRO
(tablero[2])[6] = PEÓN_NEGRO
(tablero[2])[7] = PEÓN_NEGRO
(tablero[2])[8] = PEÓN_NEGRO

#posicioninicialcaballosblancos
(tablero[8])[2] = CABALLO_BLANCO
(tablero[8])[7] = CABALLO_BLANCO
#posicioninicialcaballosnegros
(tablero[1])[2] = CABALLO_NEGRO
(tablero[1])[7] = CABALLO_NEGRO
#posicioninicialalfilesblancos
(tablero[8])[3] = ALFIL_BLANCO
(tablero[8])[6] = ALFIL_BLANCO
#posicioninicialalfilesnegros
(tablero[1])[3] = ALFIL_NEGRO
(tablero[1])[6] = ALFIL_NEGRO
#posicioninicialtorresblancas
(tablero[8])[1] = TORRE_BLANCO
(tablero[8])[8] = TORRE_BLANCO
#posicioninicialtorresnegras
(tablero[1])[1] = TORRE_NEGRO
(tablero[1])[8] = TORRE_NEGRO
#posicioninicialreinablanca
(tablero[8])[4] = REINA_BLANCO
#posicioninicialreinanegra
(tablero[1])[4] = REINA_NEGRO
#posicioninicialreyblanco
(tablero[8])[5] = REY_BLANCO
#posicioninicialreynegro
(tablero[1])[5] = REY_NEGRO

def moverunapieza(tablero):
    while True:
        inicio = input("Elige la fila y la columna que desea mover. SEPARA LOS ESPACIOS")
        inicio = inicio.split()
        if len(inicio) == 2:
            filaI = inicio[0]
            columnaI = inicio[1]
            try:
                filaI = int(filaI)
                columnaI = int(columnaI)
            except:
                pass
            else: 
                if filaI >= 0 and filaI < 8 and columnaI >= 0 and columnaI < 8:
                    break
    while True:
        final = input("Elige la fila y la columna a la que desea ir")
        final = final.split()
        if len(final) == 2:
            filaF = final[0]
            columnaF = final[1]
            try:
                filaF = int(filaF)
                columnaF = int(columnaI)
            except:
                pass
            else:
                if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8 and final != inicio:
                    (tablero[filaF])[columnaF] = tablero[filaI][columnaI]
                    (tablero[filaI][columnaI]) = " "
                    break


#def moverunapieza(tablero,a,b,c,d,e,f,g,h,uno,dos,tres,cuatro,cinco,seis,siete,ocho):
    #fila = input("fila donde ESTÁ LA PIEZA QUE DESEAS MOVER >>> ")
    #columna = input("columna donde esta la pieza que quieres mover")
    #(tablero[fila])[columna] = " "
    #printeartablero(tablero)



fichero = input("ESCOGE UN NOMBRE PARA EL FICHERO>>>>")
f = open(fichero, "a+", encoding="utf-8")


printeartablero(tablero)
continuar = "si"
while continuar != "no":
    moverunapieza(tablero)
    printeartablero(tablero)
    continuar = input("deseas continuar la partida >>>> si / no")