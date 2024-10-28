


def comprobar_entero(num_entero):
        try:
            num_entero = int(num_entero)
            print(f"El número {num_entero} es entero") 
        except ValueError:
             print("ERROR: EL NÚMERO NO ES UN ENTERO")
        

def introducir_numero():
    num = input("Introduce un número entero: ")
    return num



def main():
    num_entero = introducir_numero()
    comprobar_entero(num_entero)






if __name__ == "__main__":
    main()