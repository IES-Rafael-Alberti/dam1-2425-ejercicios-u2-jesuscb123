#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


def triangulo_numerico(numero):
    serie_filas = ""
    serie_cuenta_atras = ""
    for columnas in range(1,numero + 1,2):
        for filas in range(columnas - 2, -1, -2):
            serie_cuenta_atras += str(filas) + " "
        serie_filas = f"{columnas} " + serie_cuenta_atras
        serie_cuenta_atras = ""
        print(serie_filas)


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