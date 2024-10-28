#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

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
    numeros_negativos = 0
    numeros_positivos = 0
    while numero != 0:
        numero = introduce_numero()
        if numero < 0:
            numeros_negativos += numero
        else:
            numeros_positivos += numero
    suma += numeros_positivos
    print(f"Has finalizado el programa\n{suma}")


    
if __name__ == "__main__":
    main()