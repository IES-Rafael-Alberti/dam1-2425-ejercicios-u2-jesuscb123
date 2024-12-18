#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"


def comprobar_si_coincide(contraseña_usuario: str, CONTRASEÑA_ALMACENADA: str)->str:
        """
    Comprueba si la contraseña introducida por el usuario coincide con la contraseña almacenada.
    Args:
    contraseña_usuario(str): cadena de caracteres introducida por el usuario.
    CONTRASEÑA_ALMACENADA(str): cadena de caracteres guardada.
    Returns:
    si la contraseña coincide mostrará "contraseña correcta" sino "incorrect Password!!"
    """
        try:
            if not contraseña_usuario == CONTRASEÑA_ALMACENADA:
                 raise NameError("Incorrect Password!!")
            else: 
                 return "Contraseña correcta"
        except NameError:
             return "Incorrect Password!!"

def pedir_contraseña()->str:
    contraseña_usuario = (input("Introduce una contraseña: "))
    return contraseña_usuario

def main():
    CONTRASEÑA_ALMACENADA = "contraseña"
    contraseña_usuario = pedir_contraseña()
    print(comprobar_si_coincide(contraseña_usuario, CONTRASEÑA_ALMACENADA))

if __name__ == "__main__":
    main()





