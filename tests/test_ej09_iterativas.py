from src.sentencias_iterativas_saltos.ej09 import comprobar_si_es_correcta
def test_comprobar_si_es_correcta():
    assert comprobar_si_es_correcta("contraseña","contraseña") == "CONTRASEÑA CORRECTA"