#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

import time
import os


def introducir_opcion():
    """
    Mientras el número no sea un entero o sea menor que 0 o mayor que 3, seguirá pidiendo un número. Una vez ingresado un entero correcto, saldrá de la función.
    Args:
    numero: número introducido por el usuario.
    """
    opcion_correcta = False
    while not opcion_correcta:
        try:
            opcion_usuario = int(input("introduce una opción: "))
            if opcion_usuario < 0 or opcion_usuario > 3:
                raise ValueError("ERROR, ELIGE UNA OPCIÓN CORRECTA: ")
            opcion_correcta = True
        except ValueError:
            print("ERROR, INTRODUCE UNA OPCIÓN CORRECTA: \nOpción 1: Comenzar programa\n Opción 2: Imprimir listado\n Opción 3: finalizar programa ")
    return opcion_usuario
    


def main():

    """
    Te permite elegir entre 3 opciones. Si el usuario introduce la opción 1: comenzará el programa, si introduce 2: imprimirá listado y si elige 3: el programa finaliza de manera controlada indicando que el programa habrá terminado.
    Args:
    opcion_usuario: número que introduce el usuario indicando la opción elegida.
    """
    opcion_usuario = 0
    while not opcion_usuario == 3:
        print("Opción 1: Comenzar programa\n Opción 2: Imprimir listado\n Opción 3: finalizar programa")
        opcion_usuario = introducir_opcion()
        if opcion_usuario == 1:
            print("El programa ha comenzado.")
            time.sleep(3)
            os.system("cls")
        elif opcion_usuario == 2:
            print("Imprimiendo listado...")
            time.sleep(3)
            os.system("cls")
    print("El programa ha finalizado.")



if __name__ == "__main__":
    main()

