#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def mostrar_impares(num_entero: int)->str:
    """
    Muestra solo los números impares desde 1 hasta el número introducido por el usuario separados por ",".
    Args:
    serie(str): serie donde se irán acumulando los números impares.
    num_entero(int): número entero que introduce el usuario.
    Returns:
    serie(str):(número introducido = 5: 1,3.)
    """
    serie = ""
    for i in range (1,num_entero,2):
        serie += str(i) + ","
    print(serie)
        

def introducir_entero_positivo():
    num_entero = int(input("Introduce un número entero positivo: "))
    return num_entero


def main():
    num_entero = introducir_entero_positivo()
    mostrar_impares(num_entero)


if __name__ == "__main__":
    main()