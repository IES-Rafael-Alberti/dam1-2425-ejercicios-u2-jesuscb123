#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


def eco(frase_usuario: str):
        lista_palabras = frase_usuario.split()
        for eco in (lista_palabras):
             return f"{eco}... {eco}..."
        

def introducir_palabra():
        frase_usuario = input("Introduce una frase o di salir para acabar: ")
        return frase_usuario
       
    


def main():
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

