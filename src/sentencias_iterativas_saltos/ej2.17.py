#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


def suma_digitos(numero):
    serie = ""
    suma = 0
    for i in range(1,numero + 1):
        suma += i
        serie += str(i) + " + "
    return f"{numero} => {serie} = {suma}"


def introduce_numero():
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            numero_correcto = True
            if numero < 0:
                raise ValueError("ERROR, INTRODUCE UN NÚMERO POSITIVO: ")
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero

def main():
    numero = introduce_numero()
    print(suma_digitos(numero))
if __name__ == "__main__":
    main()