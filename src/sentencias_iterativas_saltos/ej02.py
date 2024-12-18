#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def muestra_años(edad: int)->str:
    """
    Muestra la serie de años cumplidos desde 1 hasta la edad introducida separados por ",".
    Args:
    Edad: número introducido por el usuario.
    Returns:
    Serie: número de años separados por ",".
    """
    serie = ""
    for i in range(1,edad + 1):
        if i == edad: 
            serie += str(i) + "."
        else:
            serie += str(i) + ","
    print(serie)

def introducir_edad():
    edad = int(input("Introduce tu edad: "))
    return edad

def main():
    edad = introducir_edad()
    muestra_años(edad)



if __name__ == "__main__":
    main()