


def burbuja(a:list):
    """
    Cuenta cada dígito de la lista de la variable a. Con un bucle for con rango desde 0 hasta n - 1 y otro de i + 1 hasta n. Comparará el número de la lista con el siguiente, si el primero número es mayor que el siguiente, se intercambia.
    Args:
    a: lista de números.
    Returns: 
    Lista actualizada.
    """
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                temp = a[i]
                a [i] = a [j]
                a [j] = temp
    return a

def main():
    a = [8,3,1,19,14]
    print(burbuja(a))



if __name__ == "__main__":
    main()