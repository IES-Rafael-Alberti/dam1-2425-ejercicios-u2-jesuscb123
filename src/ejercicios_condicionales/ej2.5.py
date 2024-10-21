#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def tributar(edad,ingresos):
    if edad < 16 or ingresos < 1000:
        return "No debes tributar"
    else:
        return "Debes tributar"


def introducir_edad_ingresos():
    edad = int(input("Introduce tu edad: "))
    ingresos = int(input("Introduce tus ingresos mensales: "))
    return edad,ingresos


def main():
    edad,ingresos = introducir_edad_ingresos()
    print(tributar(edad,ingresos))

if __name__ == "__main__":
    main()