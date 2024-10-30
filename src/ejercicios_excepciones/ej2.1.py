#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def comprobar_validez(edad: int)-> bool:
    """
    Si la edad es negativa o mayor de 125 saldrá un error.
    Args:
    edad(int): edad introducida por el usuario.
    """
    if edad < 0 or edad > 125:
        raise ValueError("La edad debe ser un número positivo") 
    elif edad == 0:
        raise ValueError("La edad debe ser un número positivo mayor que 0")

def mostrar_años_cumplidos(edad: int)->int:
    """
    Muestra los años desde 1 hasta la edad que tiene.
    Args:
    edad(int): número introducido por el usuario.
    """
    for i in range(1,edad + 1):
        if i == edad:
            print(i)
        else:
            print(i, end=",")

def introducir_edad():
    """
    Permite introducir la edad. Si la edad no es un entero imprimirá un error hasta que no se introduzca un número entero correcto.
    Unaa vez introduce la edad, llama a la función comprobar_validez() para asegurarse que cumple los requisitos establecidos en dicha función.
    Args:
    edad: introducir la edad.
    Returns:
    edad(int)
    """
    edad_correcta = False
    while not edad_correcta:
        try:
            edad = None
            edad = input("Introduce tu edad: ")
            edad = int(edad)
            comprobar_validez(edad)
            edad_correcta = True
        except ValueError as e:
            if edad is None:
                print("ERROR, INTRODUCE UN NÚMERO VÁLIDO:")
            else:
                print(f"ERROR, {e}")
    return edad
    

def main():
    edad = introducir_edad()
    mostrar_años_cumplidos(edad)

if __name__ == "__main__":
    main()