#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. 


def division(num1,num2):
    """
    Realiza la división si el divisor no es 0. Si el divisor es 0 retorna un error.
    Args:
    num1(int): dividendo introducido por el usuario.
    num2(int): divisor introducido por el usuario.
    Returns:
    el resultado de la division o el error.
    """
    if num2 == 0:
        return "ERROR, NO ES POSIBLE DIVIDIR POR 0."
    else: 
        division = num1 / num2
    return division

def comprobar_entero(edad: str):
    """
    Comprobará si el número introducido por el usuario es un número, si lo es, lo convierte en int.
    Args:
    edad(str): cadena de texto introducida por el usuario
    Returns: edad transformada en int.
    """
    if edad.startswith("-"):
       edad = edad[1:]
    elif edad.count(".") > 1:
        return False 
    edad = edad.strip()
    return edad.isdigit()

def introducir_numero()-> int:
    """
    Permite al usuario introducir una cadena de texto y luego comprueba que sea un número.
    Args:
    num1(str): dividendo introducido por el usuario.
    num2(str): divisor introducido por el usuario.
    Returns:
    num1(int), num2(int)
    
    """
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce el segundo número: "))
    return num1,num2

def main():
    num1,num2 = introducir_numero()
    division(num1,num2)
    print(division(num1,num2))
if __name__ == "__main__":
    main()