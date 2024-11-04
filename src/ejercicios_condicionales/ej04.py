#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.



def par_impar(num:int)->int:
    """
    Comprueba si num es par o impar. Si el resto de la división entre 2 da 0 es par sino es impar.
    Args:
    num(int): número introducido por el usuario.
    Returns:
    par o impar (str)
    """
    if (num % 2) == 0:
        return f"El número {num} es par"
    else:
        return f"El {num} es impar"
    

def comprobar_entero(num: str)->int:
    """
    Comprobará si el número introducido por el usuario es un número, si lo es, lo convierte en int.
    Args:
    edad(str): cadena de texto introducida por el usuario
    Returns: edad transformada en int.
    """
    if num.startswith("-"):
       num = num[1:]
    elif num.count(".") > 1:
        return False 
    num = num.strip()
    return num.isdigit()


def introducir_numero():
    """
    Permite al usuario introducir una cadena de texto y luego comprueba que sea un número.
    Args:
    num(str): dividendo introducido por el usuario.
    Returns:
    num(int)
    
    """
    num = input("Introduce un número para saber si es par o impar: ")
    while not comprobar_entero(num):
        num = input("Introduce un número válido: ")
    num = int(num)
    return num


def main():
    num = introducir_numero()
    print(par_impar(num))

if __name__ == "__main__":
    main()