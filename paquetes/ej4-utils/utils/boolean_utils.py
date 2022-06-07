# helpers/boolean_helpers.py

""" Negar un boolean {@param bool}.
    Ejemplos:
    negate(True) -> False
    negate(False) -> True
"""
def negate(bool):
    return not bool

""" Convertir una cadena de texto {@param str} a boolean.
    Ejemplos:
    toBoolean("true") -> True
    toBoolean("yes") -> True
    toBoolean("ON")-> True
    toBoolean("false)-> False
    toBoolean("OFF")-> False
"""
def toBoolean(str):
    if str is None:
        return False

    return str.lower() in ['1', 't', 'true', 'y', 'yes', 's', 'si', 'on', 'ok']