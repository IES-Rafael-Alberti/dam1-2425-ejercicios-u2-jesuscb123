from src.ejercicios_condicionales.ej10 import vegetariana
def test_vegetaria():
    assert vegetariana("tofu") == "Tu pizza es no vegetariana. Ingredientes básicos: mozzarella y tomate. Ingrediente elegido: tofu"