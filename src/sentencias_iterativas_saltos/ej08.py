#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


def triangulo_numerico(numero):
    filas_mostradas = ""
    serie_filas = ""
    for columnas in range(1,numero + 1,2):
        if columnas == 1:
            print(columnas)
        else:
            for filas in range(columnas - 2, -1, -2):
            


def introduce_numero():

    """
    Mientras el número no sea un entero, seguirá pidiendo un número. Una vez ingresado un entero correcto, saldrá de la función.
    Args:
    numero: número introducido por el usuario.
    """
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero

def main():
    numero = introduce_numero()
    triangulo_numerico(numero)
if __name__ == "__main__":
    main()