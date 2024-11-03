from src.ejercicios_condicionales.ej07 import tipo_impositivo
def test_tipo_impositivo():
    assert tipo_impositivo(10000) == "15%"