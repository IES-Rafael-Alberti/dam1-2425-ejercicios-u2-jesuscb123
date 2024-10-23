 #Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def cuanto_pagas(edad_cliente):
    if edad_cliente < 4:
        return "PA TI GRATI PISHA"
    elif edad_cliente >= 4 and edad_cliente <= 18:
        return "pagas 5€"
    elif edad_cliente > 18:
        return "pagas 10€"

def introduce_edad(): 
    edad_correcta = False
    while not edad_correcta:
        try:
            edad_cliente = int(input("Introduce tu edad: "))
            edad_correcta = True
        except ValueError:
            print("ERROR, INTRODUCE UNA EDAD CORRECTA: ")
    return edad_cliente




def main():
    edad_cliente = introduce_edad()
    print(cuanto_pagas(edad_cliente))

if __name__ == "__main__":
    main()