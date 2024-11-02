#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def palabra_mas_larga(frase:str)->str:
    """
    Para la palabra que está en la variable "palabras_frase" compara el número de caracteres con la palabra mayor. Si la palabra de la lista es mayor que la palabra mayor, se sistituye por esta, sino, la palabra mayor seguirá siendo la mayor. Una vez se comprueben todas las palabras de la lista y se compare con la palabra mayor, finalizará el programa mostrando la palabra mayor junto con su número de caracteres.
    Args:
    frase: frase introducida por el usuario.
    palabras_frase: contiene la frase pero dividiendo las palabras en una lista.
    palabra_mayor: contiene la palabra con mayor número de caracteres.
    Returns:
    la palabra mayor junto con el número de caracteres.
    """
    palabras_frase = frase.split() #contiene la lista de las palabras en la frase.
    palabra_mayor = ""
    for palabra in palabras_frase:
        if len(palabra) > len(palabra_mayor):
            palabra_mayor = palabra
    print(f"La palabra más larga es: {palabra_mayor} con el número de caracteres: {len(palabra_mayor)}")

        





def introduce_frase():
    frase = input("Introduce una frase: ")
    return frase


def main():
    frase = introduce_frase()
    palabra_mas_larga(frase)



if __name__ == "__main__":
    main()