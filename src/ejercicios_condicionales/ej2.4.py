#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def par_impar(num):
    if (num % 2) == 0:
        return f"El número {num} es par"
    else:
        return f"El {num} es impar"
    
def introducir_numero():
    num = int(input("Introduce un número para saber si es par o impar: "))
    return num


def main():
    num = introducir_numero()
    print(par_impar(num))

if __name__ == "__main__":
    main()