# aritmética de fechas con timedelta: https://docs.python.org/es/3/library/datetime.html#timedelta-objects
# y relativedelta: https://dateutil.readthedocs.io/en/stable/relativedelta.html

# %%
# importando módulo datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# %%
# generando el objeto datetime con la fecha de fin de año
fecha_fin_anio = datetime.strptime("2022-12-31", "%Y-%m-%d")
print(fecha_fin_anio)

# %%
# obteniendo la fecha actual
fecha_actual = datetime.now()
print(fecha_actual)

# %%
# calculando la diferencia de días entre 2 fechas
delta = fecha_fin_anio-fecha_actual
print(delta)
print(f"Días: {delta.days}")
print(f"Segundos: {delta.seconds}")

print(f"Delta total en segundos: {delta.total_seconds()}")

# %%
# calculando diferencia entre fechas utilizando timedeltas, ej. 1
fecha1 = datetime(2021, 5, 31)
fecha2 = fecha1 + timedelta(1)
print(fecha1)
print(fecha2)

# %%
# calculando diferencia entre fechas utilizando timedeltas, ej. 2
fecha1 = datetime(2021, 5, 31, 19, 50)
fecha2 = fecha1 + timedelta(days=1, hours=2, minutes=5, seconds=10)
print(fecha1)
print(fecha2)

# %%
# calculando diferencia entre fechas utilizando relativedelta
fecha1 = datetime.now()
fecha2 = datetime(2022, 11, 21) # inicio mundial

delta_para_mundial = relativedelta(fecha2, fecha1)
print(f'El mundial está a: {delta_para_mundial.years} años, {delta_para_mundial.months} meses y {delta_para_mundial.days} días')
# %%
