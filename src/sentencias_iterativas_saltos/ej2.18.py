#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


def comprobar_si_es_par(numero):
    """
     indica si es par o impar. Para ello dividimos el número dado entre 2 y si el resto es 0 será par, sino será impar. Si es par, retorna el número junto con una, que se puedes se irá acumulando en otra variable. Si es impar, no mostrará nada. 
     Args:
     num1: número introducido por el usuario.
    """
    if (numero % 2) == 0:
        return f"{numero}, "
    else:
        return ""

def suma_digitos(numero):
    """
    Un rango que irá desde 1 hasta el número dado. Acumulará en la varuable suma el número todos los números desde 1 hasta el número y los irá sumando. En la variable serie, se acumula cada número de la serie desde 1 hasta el número dado.
    Args:
    numero: número introducido por el usuario.
    serie: variable que acumula los números del rango.
    suma: variable que acumula y suma todos los números del rango.
    """
    serie = ""
    suma = 0
    for i in range(1,numero + 1):
        suma += i
        serie += str(i) + " + "
    print (f"{numero} => {serie} = {suma}")




def introduce_numero():
    """
    Mientras el número no sea un entero o sea menor que 0, seguirá pidiendo un número. Una vez ingresado un entero correcto, saldrá de la función.
    Args:
    numero: número introducido por el usuario.
    """
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero



def main():
    """
    Introduce números y los lleva a otra función para sumar sus digitos, y luego comprueba si es par. Si es par los acumula en numeros_pares para mostrar luego la serie de números pares que se han ido introduciendo. Cuando se introduzca "-1" el programa finaliza mostrando los números pares que fueron introducidos.
    Args:
    numeros_pares: serie que acumula los números pares introducidos.
    numero: número introducido por el usuario.
    """
    numeros_pares = " "
    numero = introduce_numero()
    while not numero == -1:
        suma_digitos(numero)
        numeros_pares += f"{comprobar_si_es_par(numero)}"
        numero = introduce_numero()
    print(numeros_pares)
    
    





if __name__ == "__main__":
    main()