""" 
Este módulo tiene dos funciones que convierten cadenas en mayúscula o minúscula.
"""
def minusculas(text):
    """
    Convierte la cadena recibida en minúsculas

    Args:
        text (string): cadena de texto a transformar

    Returns:
        string: Devuelve la cadena convertida en minúsculas
    
    Ejemplo:
    ========
    >>> from mipaquete.string import minusculas
    >>> minusculas("PEPE")
    'pepe'
    """
    return text.lower()

def mayusculas(text):
    """
    Convierte la cadena recibida en mayúsculas

    Args:
        text (string): cadena de texto a transformar

    Returns:
        string: Devuelve la cadena convertida en mayúsculas
    
    Ejemplo:
    ========
    >>> from mipaquete.string import mayusculas
    >>> mayusculas("Juan")
    'JUAN'
    """
    return text.upper()