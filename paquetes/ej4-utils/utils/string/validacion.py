# string/validacion.py

""" Validar que una cadena de texto {@param str} cumpla un mínimo de caracteres {@param min_length}
    Ejemplo: validate_min_length("Hola mundo", 3) -> True
"""
def validate_min_length(str, min_length):
    if str is None:
        return False

    return len(str)>=min_length

""" Validar que una cadena de texto {@param str} cumpla un máximo de caracteres {@param max_length}
    Ejemplo: validate_max_length("Hola", 4) -> True
"""
def validate_max_length(str, max_length):
    if str is None:
        return False

    return len(str)<=max_length