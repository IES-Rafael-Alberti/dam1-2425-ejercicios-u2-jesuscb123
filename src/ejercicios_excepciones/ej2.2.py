#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def mostrar_impares(num_entero):
    serie = ""
    for i in range (1,num_entero,2):
        serie += str(i) + ","
    print(serie)
        

def introducir_entero_positivo():
    numero_correcto = False
    while numero_correcto == False:
        try:
            num_entero = int(input("Introduce un número entero positivo: "))
            if num_entero < 0:
                raise ValueError("ERROR, EL NÚMERO DEBE SER POSITIVO: ")
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO POSITIVO: ")
    return num_entero
def main():
    num_entero = introducir_entero_positivo()
    mostrar_impares(num_entero)


if __name__ == "__main__":
    main()