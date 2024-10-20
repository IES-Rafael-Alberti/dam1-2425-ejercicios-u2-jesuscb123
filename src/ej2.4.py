#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def parimpar(num : int):
    resto = num % 2
    if resto == 0:
        return "Par"
    else:
        return "Impar"

def introducir_numero():
    flag = False
    while flag == False:
        try:
            num = input("Introduce número: ")
            num = int(num)
            flag = True
        except: 
            print("EL NÚMERO DEBE SER ENTERO: ")
    return num
        
def main():
    num = introducir_numero()
    print(parimpar(num))

if __name__ == "__main__":
    main()