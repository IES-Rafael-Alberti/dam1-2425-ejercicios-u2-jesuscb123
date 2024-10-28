#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


def comprobar_si_es_par(numero):
    if (numero % 2) == 0:
        return numero




def suma_digitos(numero):
    serie = ""
    suma = 0
    for i in range(1,numero + 1):
        suma += i
        serie += str(i) + " + "
    print (f"{numero} => {serie} = {suma}")




def introduce_numero():
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            if numero == -1:
                numero = str(numero)
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero



def main():
    numero = introduce_numero()
    while not numero == "-1":
        suma_digitos(numero)
        if comprobar_si_es_par:
            
        numero = introduce_numero()
        
    





if __name__ == "__main__":
    main()