# main1.py

# importando módulos desde el paquete helpers
import helpers.string_helpers
import helpers.number_helpers
import helpers.boolean_helpers

# usando el módulo string_helpers
frase = "Buenas noches"
frase_invertida = helpers.string_helpers.reverse(frase)
print(frase_invertida)

# usando el módulo number_helpers
numero_as_string = "15.15"
numero = helpers.number_helpers.toFloat(numero_as_string, 0)
print(numero)

# usando el módulo boolean_helpers
boolean_as_string = "true"
boolean = helpers.boolean_helpers.toBoolean(boolean_as_string)
print(boolean)






