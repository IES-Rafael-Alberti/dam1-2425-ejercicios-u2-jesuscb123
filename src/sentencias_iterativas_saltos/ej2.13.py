#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


def eco(frase_usuario: str):
        """
        Repite la frase del usuario como si fuera un eco.
        Args:
        frase_usuario: frase introducida por el usuario.
        """
        return f"{frase_usuario}... {frase_usuario}..."
        

def introducir_palabra():
        frase_usuario = input("Introduce una frase o di salir para acabar: ")
        return frase_usuario
       
    


def main():
    """
    Organiza el flujo del programa, mientras que el usuario no introduzca la palabra "salir" seguirá el flujo repitiendose el eco. Una vez que introduzca salir el programa finalizará de forma controlada.
    """
    frase_usuario = introducir_palabra()
    salir = False
    while not salir: 
        print(eco(frase_usuario))
        frase_usuario = introducir_palabra()
        if frase_usuario == "salir":
              salir = True
              print("Has finalizado el programa del ECO.")



if __name__ == "__main__":
    main()

