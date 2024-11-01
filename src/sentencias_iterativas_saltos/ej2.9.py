#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
CONTRASEÑA_ALMACENADA = "contraseña"



def comprobar_si_es_correcta(contraseña_usuario,CONTRASEÑA_ALMACENADA: str)->str:
    """
    Comprueba si la contraseña introducida por el usuario coincidice con la contraseña almacenada. Si no coincide mostrará un error hasta que introduzca la que coincide.
    Args:
    contrasela_usuario: contraseña introducida por el usuario.
    CONTRASEÑA_ALMACENADA: contraseña que se almacena para comparar si coincide o no.
    """
    while contraseña_usuario != CONTRASEÑA_ALMACENADA:
        contraseña_usuario = input("ERROR, LA CONTRASEÑA NO ES CORRECTA, VUELVE A INTENTARLO: ")
    return "CONTRASEÑA CORRECTA"



def introducir_contraseña():
    contraseña_usuario = input("Introduce la contraseña: ")
    return contraseña_usuario





def main():
    contraseña_usuario = introducir_contraseña()
    print(comprobar_si_es_correcta(contraseña_usuario,CONTRASEÑA_ALMACENADA))


if __name__ == "__main__":
    main()