from utils import imprimir
from sbox import crear_sbox


def sub_bytes(estado, sbox):
    for i in range(4):
        for j in range(4):
            byte = estado[i][j]
            fila = (byte >> 4) & 0x0F
            columna = byte & 0x0F
            estado[i][j] = sbox[fila][columna]


def main():
    estado = [
        [0x19, 0xa0, 0x9a, 0xe9],
        [0x3d, 0xf4, 0xc6, 0xf8],
        [0xe3, 0xe2, 0x8d, 0x48],
        [0xbe, 0x2b, 0x2a, 0x08]
    ]

    print("Estado antes de SubBytes:")
    imprimir(estado)

    sbox = crear_sbox()
    sub_bytes(estado, sbox)

    print("\nEstado después de SubBytes:")
    imprimir(estado)


if __name__ == "__main__":
    main()
