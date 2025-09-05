TAM_TABLERO = 8

tablero = [["." for _ in range(TAM_TABLERO)] for _ in range(TAM_TABLERO)]

pos_reina = (3, 2)

posiciones_bloqueadas = [(6, 3), (1, 2), (5, 4)]

tablero[pos_reina[0]][pos_reina[1]] = "R"
for bloqueo in posiciones_bloqueadas:
    tablero[bloqueo[0]][bloqueo[1]] = "X"

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

def contar_movimientos_reina():
    fila, col = pos_reina
    movimientos = 0
    direcciones = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    
    for d_fila, d_col in direcciones:
        nueva_fila, nueva_col = fila + d_fila, col + d_col
        while 0 <= nueva_fila < TAM_TABLERO and 0 <= nueva_col < TAM_TABLERO:
            if (nueva_fila, nueva_col) in posiciones_bloqueadas:
                break 
            tablero[nueva_fila][nueva_col] = "*"
            movimientos += 1
            nueva_fila += d_fila
            nueva_col += d_col
    
    return movimientos

movimientos_reina = contar_movimientos_reina()
mostrar_tablero()
print("La reina puede moverse a", movimientos_reina, "casillas.")
