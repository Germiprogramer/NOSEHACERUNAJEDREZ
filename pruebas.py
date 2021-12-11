i = 1
for i in range(5):
    i= i + 1
print(i)

print(range(i))

x = list(range(5))

print(x)

def moverunapieza(tablero):
    while True:
        filaI = input("Elige la fila de la pieza que deseas mover")
        columnaI = input("Elige la columna de la pieza que quieres mover")
        try:
            filaI = int(filaI)
            columnaI = int(columnaI)
        except:
            pass
        else: 
            if filaI >= 0 and filaI < 8 and columnaI >= 0 and columnaI < 8:
                break
    while True:
        filaF = input("Elige la fila a donde deseas mover la pieza")
        columnaF = input("Elige la columna a donde deseas mover la pieza")
        try:
            filaF = int(filaF)
            columnaF = int(columnaF)
        except:
            pass
        else:
            if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8 and (tablero[filaF])[columnaF] != tablero[filaI][columnaI]:
                (tablero[filaF])[columnaF] = tablero[filaI][columnaI]
                (tablero[filaI][columnaI]) = " "
                break


def moverunapieza(tablero):
    while True:
        inicio = input("Elige la fila y la columna que desea mover. SEPARA LOS ESPACIOS >  ")
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
        final = input("Elige la fila y la columna a la que desea ir>  ")
        final = final.split()
        if len(final) == 2:
            filaF = final[0]
            columnaF = final[1]
            try:
                filaF = int(filaF)
                columnaF = int(columnaF)
            except:
                pass
            else:
                if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8 and final != inicio:
                    (tablero[filaF])[columnaF] = tablero[filaI][columnaI]
                    (tablero[filaI][columnaI]) = " "
                    break