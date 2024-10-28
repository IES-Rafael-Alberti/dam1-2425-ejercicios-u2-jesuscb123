#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

"""
# Formula para calcular El capital tras un año.
cantidad *= 1 + interest / 100
# En donde:
# - cantidad: Cantidad a invertir
# - interest: Interes porcentual anual 
"""

def calcular_capital(inversion,interes_anual,n_anos):
    inversion *= 1 + interes_anual / 100
    año = 0
    for i in range (n_anos): 
        inversion_total_anos = inversion * año
        año += 1
        print (f"Año: {año}: {inversion_total_anos}")


def pedir_inversion_n_anos():
    inversion = int(input("Introduce tu cantidad a invertir: "))
    interes_anual = int(input("Introduce tu interés anual: "))
    n_anos = int(input("Introduce número de años: "))
    return inversion,interes_anual,n_anos

def main():
    inversion,interes_anual,n_anos = pedir_inversion_n_anos()
    calcular_capital(inversion,interes_anual,n_anos)



if __name__ == "__main__":
    main()