# main3.py

# Importando nombres individuales desde los módulos del paquete
from helpers.string_helpers import reverse
from helpers.number_helpers import toFloat
from helpers.boolean_helpers import toBoolean

# usando el módulo string_helpers
frase = "Buenas noches"
frase_invertida = reverse(frase)
print(frase_invertida)

# usando el módulo number_helpers
numero_as_string = "15.15"
numero = toFloat(numero_as_string, 0)
print(numero)

# usando el módulo boolean_helpers
boolean_as_string = "true"
boolean = toBoolean(boolean_as_string)
print(boolean)






