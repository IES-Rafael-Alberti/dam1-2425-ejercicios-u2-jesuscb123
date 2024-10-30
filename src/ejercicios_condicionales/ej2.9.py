 #Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def cuanto_pagas(edad_cliente: int)->str:
    """
    Compara la edad introducida por el cliente:
    Si es menor de 4 años indica para él es gratis.
    Si es mayor de 4 años pero menor o igual de 18 tendrá que pagar 5€
    Si es mayor de 18 la entrada son 10€
    Args:
    edad_cliente(int): edad introducida por el usuario.
    Returns:
    Mensajes de cuanto debe pagar según su edad.
    """
    if edad_cliente < 4:
        return "PA TI GRATI PISHA"
    elif edad_cliente >= 4 and edad_cliente <= 18:
        return "pagas 5€"
    elif edad_cliente > 18:
        return "pagas 10€"

def introduce_edad(): 
    """
    Permite introducir la edad. Si la edad no es un entero imprimirá un error hasta que no se introduzca un número entero correcto.
    Args:
    edad_cliente: introducir la edad.
    Returns:
    edad_cliente(int)
    """
    edad_correcta = False
    while not edad_correcta:
        try:
            edad_cliente = int(input("Introduce tu edad: "))
            edad_correcta = True
        except ValueError:
            print("ERROR, INTRODUCE UNA EDAD CORRECTA: ")
    return edad_cliente




def main():
    edad_cliente = introduce_edad()
    print(cuanto_pagas(edad_cliente))

if __name__ == "__main__":
    main()