# main3.py

# Importando nombres individuales desde los módulos del paquete
from utils.string_utils import reverse
from utils.number_utils import toFloat
from utils.boolean_utils import toBoolean

# usando el módulo string_utils
frase = "Buenas noches"
frase_invertida = reverse(frase)
print(frase_invertida)

# usando el módulo number_utils
numero_as_string = "15.15"
numero = toFloat(numero_as_string, 0)
print(numero)

# usando el módulo boolean_utils
boolean_as_string = "true"
boolean = toBoolean(boolean_as_string)
print(boolean)