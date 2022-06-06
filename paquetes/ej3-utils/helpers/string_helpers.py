# helpers/string_helpers.py

""" Invertir una cadena de texto {@param in_str}
    Ejemplo: reverse("Hola mundo") -> "odnum aloH"
"""
def reverse(in_str):
    if in_str is None:
        return None

    out_str = ""
    for ch in in_str:
        out_str = ch + out_str
    return out_str

""" Obtener los {@param length} caracteres más a la izquierda de una cadena de texto {@param str}.
    Ejemplo: left("Hola mundo", 4) -> "Hola"
"""
def left(str, length):
    if str is None:
        return None

    if length<0:
        return ""

    if len(str)<length:
        return str

    return str[:length]

""" Obtener los {@param length} caracteres más a la derecha de una cadena de texto {@param str}.
    Ejemplo: right("Hola mundo, bienvenidos a Python", 6) -> "Python"
"""
def right(str, length):
    if str is None:
        return None

    if length<0:
        return ""

    if len(str)<length:
        return str

    return str[-length:]