#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

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

    """
    Mientras que numero introducido no sea 0, seguirá pidiendo números y acumulandolo a la variable numeros_negativos si los números son negativos y a otra variable llamada numeros positivos que sumen todos los números negativos. Una vez introzca el 0, el programa finaliza de manera controlada mostrando la suma de todos los números positivos.
    Args:
    numero: número introducido por el usuario.
    numeros_negativos: numeros negativos que se irán acumulando.
    numeros_positivos: numeros positivos que se irán acumulando.
    
    """
    numero = None
    numeros_negativos = 0
    numeros_positivos = 0
    while numero != 0:
        numero = introduce_numero()
        if numero < 0:
            numeros_negativos += numero
        else:
            numeros_positivos += numero
    print(f"Has finalizado el programa\n{numeros_positivos}")


    
if __name__ == "__main__":
    main()