#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

        

def introduce_numero():
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero

def main():
    suma = 0
    numero = None
    while numero != 0:
        numero = introduce_numero()
        suma += numero
    print(f"Has finalizado el programa\n{suma}")






if __name__ == "__main__":
    main()