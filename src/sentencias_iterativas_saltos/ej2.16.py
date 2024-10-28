#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.



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
    numero_mayor = 0
    numero = None
    while numero != 0:
        numero = introduce_numero()
        if numero > numero_mayor:
            numero_mayor = numero

    print(f"Has finalizado el programa\n {numero_mayor}")


    
if __name__ == "__main__":
    main()