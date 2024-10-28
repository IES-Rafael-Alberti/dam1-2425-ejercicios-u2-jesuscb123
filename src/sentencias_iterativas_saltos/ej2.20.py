#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def mostrar_coincidencia(palabra,letra):
    coindicencia = False
    for i in range(len(palabra)):
        if letra == palabra[i]:
            coindicencia = True
            print(f"La letra {letra} se encontró en la posición {i}")
        else: 
            coindicencia = False
            print(f"En la posición {i} no se encontró esta letra")
            
  



def introducir_palabra():
    palabra = input("Introduce una palabra: ")
    letra = input("Introduce una letra: ")
    return palabra, letra



def main():
    palabra,letra = introducir_palabra()
    mostrar_coincidencia(palabra,letra)
    



if __name__ == "__main__":
    main()