#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def mostrar_impares(num_entero)->str:
    """
    Muestra todos los números desde 1 hasta número introducido por el usuario dando saltos de 2 para que solo aparezcan números primos.
    Args:
    num_entero: número introducido por el usuario.
    Returns:
    serie: números separados por ",".
    """
    serie = ""
    for i in range (1,num_entero,2):
        if i == num_entero:
            serie += str(i) + "."
        else:
            serie += str(i) + "," 
    print(serie)

def comprobar_si_es_positivo(numero_entero)->bool:
    """
    Determina si un número es positivo o no.
    Args:
    número entero = número introducido por el usuario.
    Returns:
    True o False.
    """
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