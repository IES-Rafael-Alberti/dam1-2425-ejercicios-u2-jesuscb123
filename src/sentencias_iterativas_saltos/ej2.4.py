#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


def mostrar_cuenta_atras(numero_entero):
    serie = f"{numero_entero},"
    while (numero_entero) > 0:
            numero_entero = numero_entero - 1
            if numero_entero > 0:
                serie += str(numero_entero) + ","
            else:
                 serie += str(numero_entero) + "."
    print(serie)




def comprobar_si_es_positivo(numero_entero):
    if numero_entero < 0:
        return False
    return True

def introduce_numero():
     numero_entero = int(input("Introduce un número entero positivo: "))
     while not comprobar_si_es_positivo(numero_entero):
         numero_entero = int(input("ERROR, Introduce un número entero positivo: "))
     return numero_entero

def main():
    numero_entero = introduce_numero()
    mostrar_cuenta_atras(numero_entero)


if __name__ == "__main__":
    main()