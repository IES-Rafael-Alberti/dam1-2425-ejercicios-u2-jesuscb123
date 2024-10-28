#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def tabla_multiplicar():
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