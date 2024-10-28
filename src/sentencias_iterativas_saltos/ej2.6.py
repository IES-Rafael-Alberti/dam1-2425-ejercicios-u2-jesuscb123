#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.


def triangulo(numero):
    asterisco = "*"
    serie_asterisco = ""
    for i in range(numero + 1):
      print(serie_asterisco) 
      serie_asterisco += asterisco

        

def introduce_numero():
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero

def main():
    numero = introduce_numero()
    triangulo(numero)

if __name__ == "__main__":
    main()