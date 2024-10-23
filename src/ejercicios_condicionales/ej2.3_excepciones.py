#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. 

              
def division(num1,num2):
    try:
        division = num1 / num2
    except ZeroDivisionError:
        return "ERROR, NO ES POSIBLE DIVIDIR ENTRE 0 "
    return division          
    

def introduce_numero():
    num_incorrecto = False
    while not num_incorrecto:
        try:
            num1 = input("Introduce un número: ")
            num1 = int(num1)
            num2 = input("Introduce un número: ")
            num2 = int(num2)
            num_incorrecto = True
        except ValueError:
            print("ERROR!!! Introduce un número válido.")
    return num1,num2
    
            

def main():
    num1,num2 = introduce_numero()
    print(division(num1,num2))



if __name__ == "__main__":
    main()