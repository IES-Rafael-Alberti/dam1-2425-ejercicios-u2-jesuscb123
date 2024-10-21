#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def comprobar_tributar(edad,ingresos):
    if edad < 16 or ingresos < 1000:
        return "No debes tributar."
    else:
        return "Si, debes tributar."

def introducir_edad_e_ingresos():
    flag = False
    while flag == False:
        try:
            edad = input("Introduce tu edad: ")
            edad = int(edad)
            ingresos = input("Introduce tus ingresos mensuales: ")
            ingresos = int(ingresos)
            flag = True
        except ValueError:
            print("ERROR, DEBES INTRODUCIR NÚMEROS VÁLIDOS: ")
    return edad,ingresos    


def main():
    edad,ingresos = introducir_edad_e_ingresos()
    print(comprobar_tributar(edad,ingresos))

if __name__ == "__main__":
    main()