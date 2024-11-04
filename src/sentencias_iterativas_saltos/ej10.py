#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def parimpar(num1):
    """
     indica si es par o impar. Para ello dividimos el número dado entre 2 y si el resto es igual a 0 será primo, eso hará que nos lleve a otra función creada llamada es_par_y_primo(num1). Si el resto no es igual a 0 debemos comprobar con otra función llamada es_impar_y_primo.
     Args:
     num1: número introducido por el usuario.
    """

    par = num1 % 2
    if par == 0:
      return es_par_y_primo(num1)
    else:
        return es_impar_y_primo(num1)





def es_par_y_primo(num1):
    """
    Si es par, nos llevará a la siguiente función que indica si el número dado es menor o igual a 1 o es mayor que 2, el número no es primo. Si el número es igual a 2 o mayor que 1, el número es primo.
    Args:
    num1: número introducido por el usuario.
    """
    if num1 <= 1 or num1 > 2:
        print ("El número introducido no es primo")
    else:
        if num1 == 2 or num1 > 1:
            print ("El número es primo") 





def es_impar_y_primo(num1):

    """
    Si es impar, nos llevará a la siguiente función que indica si el número dado es menor o igual que 1 el número no será primo. Sino, si el número es igual a 2 o el número es mayor que 1, tenemos que comprobar si es divisible por más de un número que no sea 1 o él mismo. Para ello he creado la función es_divisible.
    Args:
    num1: número introducido por el usuario.
    """
    if num1 <= 1:
      print ("El número introducido no es primo")
    else:
        if num1 == 2 or num1 > 1:
           es_divisible(num1)





def es_divisible(num1):

    """
    He creado un rango del 1 al 30 saltándose dos números para siempre dividirlos por números impares. Va a ir dividiendo uno por uno, cuando divide, convertirá ese int en un str para poder usar la función .find. Le he indicado que en el momento que encuentre un "."(eso indica que no será divisible debido a que no da número entero sino con decimales) salga del bucle e indique que el número es primo.
    Args:
    num1: número introducido por el usuario.
    """
    for i in range (1,30,2):
        es_divisible = num1 / i
        es_divisible_str = str(es_divisible)
    if es_divisible_str.find("."):
        print("El número es primo")
    


def main():
    num1 = int(input("introduce un número: " ))
    parimpar(num1)



if __name__ == "__main__":
    main()


