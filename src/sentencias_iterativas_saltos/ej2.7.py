#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def tabla_multiplicar()->str:
    """
    Multiplicará 1 por todos los números hasta 10, una vez llegue, pasará a ser 2 y multiplicará de nuevo hasta diez y así continuamanente hasta que llegue a 10 y pare.
    Args:
    tabla_numero: número que irá multiplicando por la iteración desde 1 hasta 10. Una vez termina de multiplicar hasta 10 se sumará 1 para que pase a ser 2 y así sucesivamente hasta 10.
    mostrar_tablas: es el que mostrará el resultado de cada multiplicación. 
    """
    tabla_numero = 1
    mostrar_tablas = 1
    for i in range (10):
        for i in range(1,10 + 1):
            mostrar_tablas = tabla_numero * i
            print(f"Tabla {tabla_numero}: {mostrar_tablas}")
            if i == 10:
                print("\n")
                tabla_numero += 1
           

def main():
    (tabla_multiplicar())

if __name__ == "__main__":
    main()