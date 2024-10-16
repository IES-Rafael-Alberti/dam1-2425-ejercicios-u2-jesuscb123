#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def comprobar_si_coincide(contraseña_usuario, CONTRASEÑA_ALMACENADA):
    if contraseña_usuario == CONTRASEÑA_ALMACENADA:
        return True
    else: 
        False

def pedir_contraseña(contraseña_usuario):
    contraseña_usuario = (input("Introduce una contraseña: "))
    return contraseña_usuario

def main():
    contraseña_usuario = None
    CONTRASEÑA_ALMACENADA = "contraseña"
    contraseña_usuario = pedir_contraseña(contraseña_usuario)
    if not comprobar_si_coincide(contraseña_usuario,CONTRASEÑA_ALMACENADA):
        print("No coincide")
    else: 
        print ("Si coincide")

if __name__ == "__main__":
    main()