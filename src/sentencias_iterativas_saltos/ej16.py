#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.



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
    Compara los numeros introducidos con el anterior. Esto se debe a que numero_mayor al inicio vale 0, pero cuando se introduce un número y el número introducido es mayor que 0, este se actualiza al número mayor. Cuando se introduce otro número, si numero mayor sigue siendo mayor que el número introducido, no se actualizará, cuando se vuelva a meter un número que si sea mayor, se volverá a actualizar. Cuando introduzca el 0 se mostrará el número mayor de todos los números introducidos.
    Args:
    numero_mayor: número que se irá actualizando con el número más grande introducido.
    numero: numero introducido por el usuario.
    """
    numero_mayor = 0
    numero = None
    while numero != 0:
        numero = introduce_numero()
        if numero > numero_mayor:
            numero_mayor = numero

    print(f"Has finalizado el programa\n {numero_mayor}")


    
if __name__ == "__main__":
    main()