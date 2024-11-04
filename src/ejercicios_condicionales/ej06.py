#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


def grupo(nombre,sexo: str)->str:
    """
    Comprueba si la letra inicial del nombre es menor que "m" y el sexo es igual a "mujer", retornará un mensaje que diga que está en el grupo A.
    Si la letra inicial es mayor que n y el sexo es "hombre, retornará un mensaje que diga que está en el grupo B. Si no cumple ninguna de estas condiciones, estará en el grupo B.
    Args:
    nombre(str): nombre introducido por el usuario.
    sexo(str): sexo introducido por el usuario.
    Returns:
    grupo A, Grupo B.
    """
    letra_inicial = nombre[0]
    if letra_inicial < "m" and sexo == "mujer":
        return "Grupo A"
    elif letra_inicial > "n" and sexo == "hombre":
        return "Grupo A"
    else:
        return "Grupo B"
 
def nombre_sexo():
    """
    Permite introducir el sexo y el nombre
    returns:
    nombre en minúsculas y sexo en minúsculas.
    """
    nombre = input("Introduce un nombre: ")
    sexo = input("Introduce tu sexo: ")
    return nombre.lower(),sexo.lower()


def main():
    nombre,sexo = nombre_sexo()
    print(grupo(nombre,sexo))



if __name__ == "__main__":
    main()