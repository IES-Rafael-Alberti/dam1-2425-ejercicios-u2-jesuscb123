#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

def acumula_impares(contar_impares):
    contar_impares += 1
    return contar_impares


def acumula_pares(contar_pares):
    contar_pares += 1
    return contar_pares



def digitos_pares_impares(numero):
    for i in (str(numero)):
        i = int(i)
        if (i % 2) == 0:
            acumula_pares(numero)
            print(f"{i} par")
        else:
            acumula_impares(numero)
            print(f"{i} impar")
            



def introducir_numero():
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            if numero < 0:
                raise ValueError("ERROR, INTRODUCE UN NÚMERO POSITIVO:")
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÑUMERO ENTERO VÁLIDO: ")
    return numero
        


def main():
    contar_pares = 0
    contar_impares= 0
    numero = introducir_numero()
    while not numero == 0:
        contar_pares = acumula_pares(contar_pares)
        contar_impares = acumula_impares(contar_impares)
        numero = introducir_numero()
    print(f"El número de pares es {contar_pares} y el número de impares es {contar_impares}")
    

    



    


if __name__ == "__main__":
    main()
