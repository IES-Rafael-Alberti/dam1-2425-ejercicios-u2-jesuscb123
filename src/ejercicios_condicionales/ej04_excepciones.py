#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def parimpar(num : int)->str:
    """
    Comprueba si num es par o impar. Si el resto de la división entre 2 da 0 es par sino es impar.
    Args:
    num(int): número introducido por el usuario.
    Returns:
    par o impar (str)
    """
    resto = num % 2
    if resto == 0:
        return "Par"
    else:
        return "Impar"

def introducir_numero():
    """
    Permite al usuario introducir una cadena de texto y luego comprueba que sea un número.
    Args:
    num(str): dividendo introducido por el usuario.
    Returns:
    num(int)
    
    """
    numero_correcto = False
    while not numero_correcto:
        try:
            num = input("Introduce número: ")
            num = int(num)
            numero_correcto = True
        except ValueError: 
            print("EL NÚMERO DEBE SER ENTERO: ")
    return num
        
def main():
    num = introducir_numero()
    print(parimpar(num))

if __name__ == "__main__":
    main()

    