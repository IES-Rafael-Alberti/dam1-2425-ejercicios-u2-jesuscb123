#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def tipo_impositivo(renta_anual):
    if renta_anual < 10000:
        return "5%"
    elif renta_anual >= 10000 and renta_anual < 20000:
        return "15%"
    elif renta_anual >= 20000 and renta_anual < 35000:
        return "20%"
    elif renta_anual >= 35000 and renta_anual <= 60000:
        return "30%"
    elif renta_anual > 60000:
        return "45%"

def introducir_renta():
    renta_anual = int(input("Introduce tu renta anual: "))
    return renta_anual

def main():
    renta_anual = introducir_renta()
    print(f"El tipo de imperativo que te corresponde es: {tipo_impositivo(renta_anual)}")

if __name__ == "__main__":
    main()