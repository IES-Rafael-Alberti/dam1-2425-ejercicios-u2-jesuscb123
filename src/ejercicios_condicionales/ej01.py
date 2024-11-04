#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.



def comprobar_si_supera_18(edad: int, MAYOR_EDAD: int)->bool:
    
    """
    la función comprobar_si_supera_18 retornará True o False dependiendo de si es mayor o igual que 18 o no.

    Args:
    edad(int): edad introducida por el usuario.
    MAYOR_EDAD(int): edad constante, en este caso, 18.
    R
    """
    if edad >= MAYOR_EDAD:
        return True
    else:
        return False

def MENSAJE_ERROR(edad: int)->int:
    """
    Esta función mostrará el mensaje de error si la edad no es válida.

    Args:
    edad (int): Edad introducidad por el usuario.

    Returns: 
    int: Edad correcta.
    """
    edad = input("ERROR INTRODUCE UNA EDAD VALIDA: ")
    return edad

def comprobar_entero(edad: str)->int:
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
    


def introduce_edad()->str:
    edad = input("Introduce tu edad: ")
    return edad

def main():
    MAYOR_EDAD = 18
    edad = introduce_edad()
    while not comprobar_entero(edad):
        edad = MENSAJE_ERROR(edad)
    edad = int(edad)
    if comprobar_si_supera_18(edad, MAYOR_EDAD):
        print("Es mayor de 18")
    else:
        print("Es menor de 18")
    


if __name__ == "__main__":
    main()