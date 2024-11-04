#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


def repetir_palabra(palabra: str)->str:
    """
    Repite la palabra introducida por el usuario 10 veces.
    Args:
    palabra(str): palabra introducida por el usuario.
    """
    for i in range(10):
        print(palabra)

def introducir_palabra():
    palabra = input("Introduce una palabra que quieras repetir: ")
    return palabra

def main():
    palabra = introducir_palabra()
    repetir_palabra(palabra)


if __name__ == "__main__":
    main()