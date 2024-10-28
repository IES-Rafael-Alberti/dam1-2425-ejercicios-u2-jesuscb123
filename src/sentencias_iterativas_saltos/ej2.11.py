#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.


def mostrar_letras(palabra):
    for i in range (len(palabra) -1, -1, -1):
        letra = palabra[i] 
        print(letra)




def introducir_palabra():
    palabra = input("Introduce una palabra: ")
    return palabra



def main():
    palabra = introducir_palabra()
    mostrar_letras(palabra)

if __name__ == "__main__":
    main()