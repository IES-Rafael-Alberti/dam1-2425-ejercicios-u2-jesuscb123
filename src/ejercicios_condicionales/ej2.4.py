#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


"""
La función par_impar comparará el resto de la división entre 2. Si el resto es igual a 0 será par, sino sera impar.
"""
def par_impar(num):
    if (num % 2) == 0:
        return f"El número {num} es par"
    else:
        return f"El {num} es impar"
    

def comprobar_entero(num: str):
    if num.startswith("-"):
       num = num[1:]
    elif num.count(".") > 1:
        return False 
    num = num.strip()
    return num.isdigit()


def introducir_numero():
    num = input("Introduce un número para saber si es par o impar: ")
    while not comprobar_entero(num):
        num = input("Introduce un número válido: ")
    num = int(num)
    return num


def main():
    num = introducir_numero()
    print(par_impar(num))

if __name__ == "__main__":
    main()