# Matriz bidimensional
matriz = [[5, 2, 8],
          [3, 9, 1],
          [7, 4, 6]]


def ordenar_fila(matriz, fila):
    """
    Ordena una fila específica de la matriz en orden ascendente utilizando Bubble Sort.

    Parámetros:
    matriz (list): La matriz bidimensional.
    fila (int): El índice de la fila a ordenar.
    """
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]


# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
for fila in matriz:
    print(fila)
