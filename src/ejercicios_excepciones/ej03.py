#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
def mostrar_impares(num_entero: int)->str:
    """
    Muestra los números desde num_entero hasta 0. 
    Args:
    num_entero(int): número introducido por el usuario.
    serie(str): acumulará los números separasdos por ",".
    Returns:
    serie(5,4,3,2,1,0)

    """
    serie = ""
    for i in range (num_entero -1, -1, -1):
        serie += str(i) + ","
    print(serie)
        

def introducir_entero_positivo()->int:
    numero_correcto = False
    while numero_correcto == False:
        try:
            num_entero = int(input("Introduce un número entero positivo: "))
            if num_entero < 0:
                raise ValueError("ERROR, EL NÚMERO DEBE SER POSITIVO: ")
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO POSITIVO: ")
    return num_entero




def main():
    num_entero = introducir_entero_positivo()
    mostrar_impares(num_entero)


if __name__ == "__main__":
    main()