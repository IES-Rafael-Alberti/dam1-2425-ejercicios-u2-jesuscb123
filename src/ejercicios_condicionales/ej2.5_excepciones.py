#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def comprobar_tributar(edad: int,ingresos: int)->str:
    """
    La función tributar comparará la edad y los ingresos introducidas por el usuario. Si la edad es menor de 16 o los ingresos son menores que 1000 retornarará que no debe tributar sino retorna que debe tributar.
    Args:
    edad(int): edad introducida por el usuario.
    ingresos(int): ingresos introducidos por el usuario.
    Returns:
    Mensaje de si debe tributar o no en una cadena de texto.
    """
    if edad < 16 or ingresos < 1000:
        return "No debes tributar."
    else:
        return "Si, debes tributar."

def introducir_edad_e_ingresos()->int:
    """
    Introduce la edad y los ingresos y los transforma en int. Se mostrará un error y se pedirá la edad y los ingresos hasta que los dos sean enteros. 
    Args:
    edad(str): edad introducida por el usuario.
    ingresos(str): ingresos introducidos por el usuario.
    Returns:
    edad(int), ingresos(int)
    """
    ingresos_correctos = False
    while not ingresos_correctos:
        try:
            edad = input("Introduce tu edad: ")
            edad = int(edad)
            ingresos = input("Introduce tus ingresos mensuales: ")
            ingresos = int(ingresos)
            ingresos_correctos = True
        except ValueError:
            print("ERROR, DEBES INTRODUCIR NÚMEROS VÁLIDOS: ")
    return edad,ingresos    


def main():
    edad,ingresos = introducir_edad_e_ingresos()
    print(comprobar_tributar(edad,ingresos))

if __name__ == "__main__":
    main()