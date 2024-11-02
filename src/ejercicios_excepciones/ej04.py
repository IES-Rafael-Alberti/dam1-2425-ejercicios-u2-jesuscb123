#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.


def comprobar_entero(num_entero:str)->str:
        """
        Comprueba si lo que ha introducido el usuario en la función "introducir_numero()" es un entero.
        Args:
        num_entero(str): numero en str introducido por el usuario. Si es un número, lo convierte a entero.
        Returns
        mensaje si es entero o no.
        """
        try:
            num_entero = int(num_entero)
            return f"El número {num_entero} es entero"
        except ValueError:
             return "ERROR: EL NÚMERO NO ES UN ENTERO"
        

def introducir_numero():
    num = input("Introduce un número entero: ")
    return num



def main():
    num_entero = introducir_numero()
    print(comprobar_entero(num_entero))






if __name__ == "__main__":
    main()