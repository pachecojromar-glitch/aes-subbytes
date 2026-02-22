def dimension(matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas


def imprimir(A):
    f, c = dimension(A)
    for i in range(f):
        print("| ", end="")
        for j in range(c):
            print("{:>4} |".format(hex(A[i][j])), end="")
        print("")
