#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. 

def division(num1,num2):
    if num2 == 0:
        return "ERROR, NO ES POSIBLE DIVIDIR POR 0."
    else: 
        division = num1 / num2
    return division


def introducir_numero()-> int:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce el segundo número: "))
    return num1,num2

def main():
    num1,num2 = introducir_numero()
    division(num1,num2)
    print(division(num1,num2))
if __name__ == "__main__":
    main()