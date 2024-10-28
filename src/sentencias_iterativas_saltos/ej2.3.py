#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def mostrar_impares(num_entero):
    serie = ""
    for i in range (1,num_entero,2):
        if i == num_entero:
            serie += str(i) + "."
        else:
            serie += str(i) + "." 
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
    mostrar_impares(numero_entero)




if __name__ == "__main__":
    main()