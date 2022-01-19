# datetime: https://docs.python.org/3/library/datetime.html

# importando módulo datetime
from datetime import datetime, date, time

# instanciando un objeto de tipo datetime, solo fecha
fecha = datetime(2022, 1, 18)
print(fecha)

# instanciando un objeto de tipo datetime, fecha y hora
fecha = datetime(2022, 1, 18, 19, 5, 10)
print(fecha)

# obteniendo la fecha local actual, incluyendo la hora
fecha_actual = datetime.now()
print(fecha_actual)

# obteniendo solo la hora actual
hora_actual = datetime.now().time()
print(hora_actual)

# obteniendo solo fecha local actual usando la clase date
solo_fecha = date.today()
print(solo_fecha)

# formateando una fecha: https://strftime.org/
fecha_actual = datetime.now()
print(datetime.strftime(fecha_actual, "%d-%m-%Y %H %M"))
print(datetime.strftime(fecha_actual, "%d/%m/%Y"))

# instanciando una fecha desde un string
fecha_from_string = datetime.strptime("01.2022.30", "%m.%Y.%d")
print(fecha_from_string)

