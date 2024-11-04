#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def comprobar_si_coincide(contraseña_usuario: str, CONTRASEÑA_ALMACENADA: str)->str:
    """
    Comprueba si la contrasña introducida por el usuario coincide con la contraseña almacenada.
    Args:
    contraseña_usuario(str): cadena de caracteres introducida por el usuario.
    CONTRASEÑA_ALMACENADA(str): cadena de caracteres guardada.
    returns:
    str
    """
    if contraseña_usuario == CONTRASEÑA_ALMACENADA:
        return "Contraseña correcta"
    else: 
       return "Contraseña incorrecta"

def pedir_contraseña()->str:
    """
    Pide la contraseña al usuario.
    returns:
    contraseña_usuario: contrasñea introducida por el usuario.
    """
    contraseña_usuario = (input("Introduce una contraseña: "))
    return contraseña_usuario

def main():
    CONTRASEÑA_ALMACENADA = "contraseña"
    contraseña_usuario = pedir_contraseña()
    print(comprobar_si_coincide(contraseña_usuario, CONTRASEÑA_ALMACENADA))

if __name__ == "__main__":
    main()