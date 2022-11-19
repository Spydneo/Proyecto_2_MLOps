import mipaquete.string as strg
# from mipaquete.math import sumar

def test_strg_minusculas():
    """Comprueba que pase de mayusculas a minusculas
    """
    assert strg.minusculas("HOLA") == "hola"

def test_strg_mayusculas():
    """Comprueba que pase de minusculas a mayusculas
    """
    assert strg.mayusculas("pepe") == "PEPE"