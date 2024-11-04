#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


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
    return f"{numero} => {serie} = {suma}"


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