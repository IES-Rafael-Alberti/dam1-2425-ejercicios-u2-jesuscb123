#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
"""Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
"""
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def mostrar_nivel_cantidad(puntuacion: float)->str: #El dinero recibido se multiplica por el nivel y luego se suma al dinero base.
    """
    Mostrará el nivel y la cantidad de dinero que ganará.
    Nivel	Puntuación
    Inaceptable	0.0
    Aceptable	0.4
    Meritorio	0.6 o más
    Args:
    puntuación(float): puntuación introducida por el usuario.
    dinero recibido(float): dinero que recibe según la puntuación.
    Returns:
    Una cadena de texto que indique el nivel y la cantidad de dinero recibida.
    """
    dinero_recibido = (2400 * puntuacion) + 2400
    if puntuacion == 0.0 or puntuacion < 0.4:
        return f"Tu nivel es inaceptable. La cantidad de dinero es: 2400"
    elif puntuacion == 0.4 or puntuacion < 0.6:
        return f"Tu nivel es aceptable. La cantidad de dinero es: {dinero_recibido}"
    elif puntuacion >= 0.6:
        return f"Tu nivel es meritorio. La cantidad de dinero es: {dinero_recibido}"




def introducir_puntuacion()->int:
    """
    Permite introducir una puntuación.
    Args:
    puntuacion(int): introduce una puntuación.
    Returns:
    puntuacion(int)
    """
    puntuacion_correcta = False
    while not puntuacion_correcta:
        try:
            puntuacion = float(input("Introduce tu puntuación: "))
            puntuacion_correcta = True
        except ValueError:
            print("ERROR, INTRODUCE UNA PUNTUACIÓN VÁLIDA: ")
    return puntuacion


        

def main():
    puntuacion = introducir_puntuacion()
    print(mostrar_nivel_cantidad(puntuacion))

if __name__== "__main__":
    main()