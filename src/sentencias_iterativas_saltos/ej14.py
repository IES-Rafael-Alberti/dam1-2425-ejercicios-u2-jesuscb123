#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

        

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
    Mientras que numero introducido no sea 0, seguirá pidiendo números y acumulandolo a la variable suma. Una vez introduzca el 0, el programa finaliza de manera controlada mostrando la suma de todos los números introducidos.
    
    """
    suma = 0
    numero = None
    while numero != 0:
        numero = introduce_numero()
        suma += numero
    print(f"Has finalizado el programa\n{suma}")






if __name__ == "__main__":
    main()