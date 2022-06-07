# main4.py

# importando módulos desde subpaquete
from utils.string import manipulacion as string_help, validacion as valid_string_help

# usando el módulo manipulacion del subpaquete string
frase = "Buenas noches"
frase_invertida = string_help.reverse(frase)
print(frase_invertida)

# usando el módulo validacion del subpaquete string
frase = "Curso de Python"
frase_valida = valid_string_help.validate_max_length(frase, 10)
print(frase_valida)