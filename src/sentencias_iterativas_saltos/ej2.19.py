#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

import time
import os


def opcion3(opcion_usuario):
    return "Se ha interrumpido la impresión. Programa finalizado."
    
def opcion2(opcion_usuario):
    return "Imprimiendo listado.."
def opcion1(opcion_usuario):
    return "El programa ha comenzado"

def introducir_opcion():
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
    opcion_usuario = 0
    while not opcion_usuario == 3:
        print("Opción 1: Comenzar programa\n Opción 2: Imprimir listado\n Opción 3: finalizar programa")
        opcion_usuario = introducir_opcion()
        if opcion_usuario == 1:
            print(opcion1(opcion_usuario))
            time.sleep(3)
            os.system("cls")
        elif opcion_usuario == 2:
            print(opcion2(opcion_usuario))
            time.sleep(3)
            os.system("cls")
    print(opcion3(opcion_usuario))



if __name__ == "__main__":
    main()

