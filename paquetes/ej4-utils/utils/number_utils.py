# utils/number_utils.py

""" Convertir una cadena de texto {@param str} a un número entero,
    retornando un valor por defecto {@param default_value} si la conversión falla.

    Ejemplo: toInt("1259", 0) -> 1259
"""
def toInt(str, default_value):
    if str is None:
        return default_value

    try:
        return int(str)
    except ValueError:
        return default_value

""" Convertir una cadena de texto {@param str} a un número flotante,
    retornando un valor por defecto {@param default_value} si la conversión falla.

    Ejemplo: toFloat("59.25", 0) -> 59.25
"""
def toFloat(str, default_value):
    if str is None:
        return default_value

    try:
        return float(str)
    except ValueError:
        return default_value