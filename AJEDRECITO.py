from os import supports_effective_ids, terminal_size


tablero =[
    [" ",' ',' ',' ',' ',' ',' ',' '],
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

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7

uno = 7
dos = 6
tres = 5
cuatro = 4
cinco = 3
seis = 2
siete = 1
ocho = 0

printeartablero(tablero)

#posicioninicialpeonesblancos

#def moverunapieza(tablero,a,b,c,d,e,f,g,h,uno,dos,tres,cuatro,cinco,seis,siete,ocho):
    #fila = input("fila donde ESTÁ LA PIEZA QUE DESEAS MOVER >>> ")
    #columna = input("columna donde esta la pieza que quieres mover")
    #(tablero[fila])[columna] = " "
    #printeartablero(tablero)






(tablero[dos])[a] = PEÓN_BLANCO
(tablero[dos])[b] = PEÓN_BLANCO
(tablero[dos])[c] = PEÓN_BLANCO
(tablero[dos])[d] = PEÓN_BLANCO
(tablero[dos])[e] = PEÓN_BLANCO
(tablero[dos])[f] = PEÓN_BLANCO
(tablero[dos])[g] = PEÓN_BLANCO
(tablero[dos])[h] = PEÓN_BLANCO


#posicioninicialpeonesnegros
(tablero[1])[0] = PEÓN_NEGRO
(tablero[1])[1] = PEÓN_NEGRO
(tablero[1])[2] = PEÓN_NEGRO
(tablero[1])[3] = PEÓN_NEGRO
(tablero[1])[4] = PEÓN_NEGRO
(tablero[1])[5] = PEÓN_NEGRO
(tablero[1])[6] = PEÓN_NEGRO
(tablero[1])[7] = PEÓN_NEGRO

printeartablero(tablero)


#while True:
    #inicio = input("Elige la fila y la columna que desea mover")
    #inicio = inicio.split()
    #if len(inicio) == 2:
        #filaI = inicio[0]
        #columnaI = inicio[1]
        #try:
            #filaI = int(filaI)
            #columnaI = int(columnaI)
        #except:
            #pass
        #else: 
            #if filaI >= 0 and filaI < 8 and columnaI >= 0 and columnaI < 8:
                #break

#while True:
    #final = input("Elige la fila y la columna a la que desea ir")
    #final = final.split()
    #if len(final) == 2:
        #filaF = final[0]
        #columnaF = final[1]
        #try:
            #filaF = int(filaF)
            #columnaF = int(columnaI)
        #except:
            #pass
        #else:
            #if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8 and final != inicio:
                #(tablero[filaF])[columnaF] = tablero[filaI][columnaI]
                #(tablero[filaI][columnaI]) = " "
                #break


#def moverunapieza(tablero,a,b,c,d,e,f,g,h,uno,dos,tres,cuatro,cinco,seis,siete,ocho):
    #fila = input("fila donde ESTÁ LA PIEZA QUE DESEAS MOVER >>> ")
    #columna = input("columna donde esta la pieza que quieres mover")
    #(tablero[fila])[columna] = " "
    #printeartablero(tablero)



fichero = input("ESCOGE UN NOMBRE PARA EL FICHERO>>>>")
f = open(fichero, "a+", encoding="utf-8")



printeartablero(tablero)
moverunapieza(tablero,a,b,c,d,e,f,g,h,uno,dos,tres,cuatro,cinco,seis,siete,ocho)