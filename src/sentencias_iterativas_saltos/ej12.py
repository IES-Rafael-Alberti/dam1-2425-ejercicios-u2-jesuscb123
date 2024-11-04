#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.



def mostrar_letra(palabra,letra: str):
    """
    Cuenta el número de veces que encuentra la letra introducida en la palabra introducida. 
    Args:
    letra_coincide: almacena el número de veces que encuentra la letra en la palabra.
    palabra: palabra introducida por el usuario.
    letra: letra introducida por el usuario.
    """
    letra_coincide = palabra.count(letra)
    print(letra_coincide)

def introducir_palabra():
    palabra = input("Introduce una palabra: ")
    letra = input("Introduce una letra: ")
    return palabra, letra



def main():
    palabra,letra = introducir_palabra()
    mostrar_letra(palabra,letra)



if __name__ == "__main__":
    main()