#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.



def contar_numeros_titulos(titulos_conjuntos):
    """
    Verifica si cada caracter de la variable titulos_conjuntos (que contiene todos los títulos ingresados) es un número. Si es número, lo añadirá al contador.
    Args: 
    titulos_conjuntos: todos los títulos ingresados en una sola línea.
    contador: número de veces que se ha encontrado un número en titulos_conjuntos.
    Returns:
    Contador.
    """
    contador = 0
    for caracter in titulos_conjuntos:
        if caracter.isdigit(): 
            contador += 1
    return contador


        


def introducir_titulos()->str:
    titulo = input("Libro:  ")
    return titulo


def main():
    """
    Se encarga de llamar a la función introducir_titulos y verifica si el titulo ingresado es una "/" o "*". Si ingresa una barra, se habrá leído una línea completa y mostrará cuántos números se han encontrado en esa línea. Si introduce un "*" será que ha terminado el programa y mostrará cuántas líneas completas se han leído.
    """
    titulos_conjuntos =""
    lineas_completas = 0
    titulos = introducir_titulos()
    while not titulos == "*":
        titulos_conjuntos = titulos_conjuntos + titulos + ","
        titulos = introducir_titulos()

        if titulos == "/":
            lineas_completas += 1
            contar_numeros = contar_numeros_titulos(titulos_conjuntos)
            print(f"Línea completa. Aparecen {contar_numeros} dígitos numéricos.")
            contar_numeros = 0
            titulos_conjuntos =""
    print(f"Se leyeron {lineas_completas} líneas completas.")
        




if __name__ == "__main__":
    main()