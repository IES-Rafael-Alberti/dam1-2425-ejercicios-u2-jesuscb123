#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def primo_o_no(numero,primos):
    """
    Verifica si el número introducido es primo o no. Irá dividiendo el número por cada número hasta el número introducido, si el resto es 0 sumará a divisores ya que si es divisible por ese número. Si cuando termine de dividir por todo el rango, encuentra que solo tiene dos divisores será primo, sino es que no lo es.
    Args:
    numero: número introducido por el usuario.
    primos: contador de números primos totales.
    """
    divisores = 0
    for i in range(1,numero + 1):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        primos += 1
    return primos


def introduce_numero()->int:
    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return numero

def main():
    """
    Permite el flujo del programa, mientras que no se introduzca un 0, el programa seguirá pidiendo números y evaluando si es primo o no.
    
    """
    primos = 0
    numero = introduce_numero()
    while not numero == 0:
        primos = primo_o_no(numero,primos)
        numero = introduce_numero()
    print(primos)
if __name__ == "__main__":
    main()


