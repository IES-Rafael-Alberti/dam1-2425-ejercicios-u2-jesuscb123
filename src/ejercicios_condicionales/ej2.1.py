#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def comprobar_si_supera_18(edad, MAYOR_EDAD):
    if edad >= MAYOR_EDAD:
        return True
    else:
        return False
    
def MENSAJE_ERROR(edad):
    edad = input("ERROR INTRODUCE UNA EDAD VALIDA: ")
    return edad

def comprobar_entero(edad: str):
    if edad.startswith("-"):
       edad = edad[1:]
    elif edad.count(".") > 1:
        return False 
    edad = edad.strip()
    return edad.isdigit()
    


def introduce_edad():
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