""" Este módulo contiene operaciones básicas aritméticas """

def sumar(a, b):
    """Esta funció realizar la operación aritmética de suma

    Args:
        a (int): primer operando
        b (int): segundo operando

    Returns:
        int: resultado de la suma
    
    Ejemplo
    ========
    >>> import mipaquete.math as math
    >>> math.sumar(9, 9)
    18
    """
    return a+b

def restar(a, b):
    """Esta funció realizar la operación aritmética de resta

    Args:
        a (int): primer operando
        b (int): segundo operando

    Returns:
        int: resultado de la resta
    
    Ejemplo
    ========
    >>> import mipaquete.math as math
    >>> math.restar(19, 9)
    10
    """
    return a-b

def multiplicar(a, b):
    """Esta funció realizar la operación aritmética de multiplicación

    Args:
        a (int): primer operando
        b (int): segundo operando

    Returns:
        int: resultado de la multiplicación
    
    Ejemplo
    ========
    >>> import mipaquete.math as math
    >>> math.multiplicar(5, 5)
    25
    """
    return a*b


