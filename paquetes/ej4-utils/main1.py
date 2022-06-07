# main1.py

# importando módulos desde el paquete utils
import utils.string_utils
import utils.number_utils
import utils.boolean_utils

# usando el módulo string_utils
frase = "Buenas noches"
frase_invertida = utils.string_utils.reverse(frase)
print(frase_invertida)

# usando el módulo number_utils
numero_as_string = "15.15"
numero = utils.number_utils.toFloat(numero_as_string, 0)
print(numero)

# usando el módulo boolean_utils
boolean_as_string = "true"
boolean = utils.boolean_utils.toBoolean(boolean_as_string)
print(boolean)