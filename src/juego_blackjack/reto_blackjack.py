

BARAJA_CARTAS = ["A234567890JKQ"]


def jugador_1(pide_carta):
    Jugador_1 = False
    parar = False
	cartas_jugador = ""
	while not parar:
		pide_carta = pedir_carta()
	    cartas_jugador += pide_carta + ","
	    if pide_carta == "parar":
	        print(f"Has parado con: {cartas_jugador}")
	    Jugador_1 = True
	    parar = True
	    else: 
            cartas_jugador += pide_carta + ","

def pedir_carta():
    pide_carta = input("Pide tu carta o para diciendo parar: ")
    return pide_carta


def main():
	pide_carta = pedir_carta()
	jugador1_ha_terminado = False
	while not jugador1_ha_terminado:
		jugador_1()
		
	
			
		
		


if __name__ == "__main__":
	main()