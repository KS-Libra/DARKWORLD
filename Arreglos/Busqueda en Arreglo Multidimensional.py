# Definir la matriz bidimensional
matriz = [[5, 2, 8],
          [3, 9, 1],
          [7, 6, 4]]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"El valor {valor} se encontró en la posición ({i}, {j}).")
                return
    print(f"El valor {valor} no se encontró en la matriz.")

# Ejemplo de uso
buscar_valor(matriz, 9)
buscar_valor(matriz, 7)

