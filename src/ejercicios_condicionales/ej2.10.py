#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
"""
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
"""
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def no_vegetariana(elige_ingrediente):
    elige_ingrediente = input("Elige un ingrediente: pimiento, tofu: ")
    print(f"Tu pizza es vegetariana. Ingredientes básicos: mozzarella y tomate. Ingrediente elegido: {elige_ingrediente}")

def vegetariana(elige_ingrediente):
        elige_ingrediente = input("Elige un ingrediente: pimiento, tofu: ")
        print(f"Tu pizza es no vegetariana. Ingredientes básicos: mozzarella y tomate. Ingrediente elegido: {elige_ingrediente}")
    

def vegetariano_o_no():
    respuesta_usuario = input("Elige un tipo de pizza pizza: Vegetariana o no vegetariana: ")
    respuesta_usuario = respuesta_usuario.lower()
    while not respuesta_usuario == "vegetariana" or respuesta_usuario == "no vegetariana":
         respuesta_usuario = input("ERROR, ELIGE UN TIPO DE PIZZA CORRECTO: ")
         respuesta_usuario = respuesta_usuario.lower()
    return respuesta_usuario

def main():
    respueta_usuario = vegetariano_o_no()
    if respueta_usuario == "vegetariana":
        vegetariana(respueta_usuario)
    elif respueta_usuario == "no vegetariana":
        no_vegetariana(respueta_usuario)
       

    
    

if __name__ == "__main__":
    main()




