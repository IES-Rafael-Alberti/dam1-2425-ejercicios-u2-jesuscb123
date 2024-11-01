#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.


def descuento (total: float)->float:
    descuento = total * 0.10
    total_descontado = total - descuento 
    return total_descontado

def total_a_pagar(compras: int,numero: int)->int:
    total = compras + numero
    return total


def introduce_numero()->int:
    numero_correcto = False
    while not numero_correcto:
        try:
            compras = float(input("Introduce un número: "))
            if compras < 0:
                raise ValueError("ERROR, DEBE SER UN NÚMERO POSITIVO")
            numero_correcto = True
        except ValueError:
            print("ERROR, INTRODUCE UN NÚMERO ENTERO.")
    return compras


def main():
    total = 0
    compras = None
    while compras != 0:
        compras = introduce_numero()
        total = total_a_pagar(compras,total)
    if total >= 1000:
        total_con_descuento = descuento(total)
        print(f"El total a pagar es {total_con_descuento}")
    else:
        print(f"El total a pagar es {total}")
    



    
if __name__ == "__main__":
    main()



