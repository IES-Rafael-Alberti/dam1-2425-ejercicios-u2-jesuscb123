#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. 

              
def division(num1: int,num2: int)->int:
    """
    Realiza la división si el divisor no es 0. Si el divisor es 0 retorna un error.
    Args:
    num1(int): dividendo introducido por el usuario.
    num2(int): divisor introducido por el usuario.
    Returns:
    el resultado de la division o el error.
    """
    try:
        division = num1 / num2
    except ZeroDivisionError:
        return "ERROR, NO ES POSIBLE DIVIDIR ENTRE 0 "
    return division          
    

def introduce_numero()->int:
    """
    Permite al usuario introducir una cadena de texto y luego comprueba que sea un número.
    Args:
    num1(str): dividendo introducido por el usuario.
    num2(str): divisor introducido por el usuario.
    Returns:
    num1(int), num2(int)
    
    """
    num_incorrecto = False
    while not num_incorrecto:
        try:
            num1 = input("Introduce un número: ")
            num1 = int(num1)
            num2 = input("Introduce un número: ")
            num2 = int(num2)
            num_incorrecto = True
        except ValueError:
            print("ERROR!!! Introduce un número válido.")
    return num1,num2
    
            

def main():
    num1,num2 = introduce_numero()
    print(division(num1,num2))



if __name__ == "__main__":
    main()