# realizando aritmética de fechas

from datetime import datetime, timedelta

# generando el objeto datetime con la fecha de fin de año
fecha_fin_anio = datetime.strptime("2022-12-31", "%Y-%m-%d")
print(fecha_fin_anio)

# obteniendo la fecha actual
fecha_actual = datetime.now()
print(fecha_actual)

# calculando la diferencia de días entre 2 fechas
delta = fecha_fin_anio-fecha_actual
print(delta)
print(f"Días: {delta.days}")
print(f"Segundos: {delta.seconds}")

print(f"Delta total en segundos: {delta.total_seconds()}")


# utilizando timedeltas
fecha1 = datetime(2021, 5, 31)
fecha2 = fecha1 + timedelta(1)
print(fecha1)
print(fecha2)

fecha1 = datetime(2021, 5, 31, 19, 50)
fecha2 = fecha1 + timedelta(days=1, hours=2, minutes=5, seconds=10)
print(fecha1)
print(fecha2)