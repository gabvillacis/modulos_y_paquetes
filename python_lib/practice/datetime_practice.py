# %%
# importando módulos datetime y relativedelta
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

# %%
# 1. Determine el número de días entre 2020-07-21 y 2020-12-31.
fecha1 = date(2020, 7, 21)
fecha2 = date(2020, 12, 31)

delta = fecha2 - fecha1
print(delta.days)

# %%
# 2. Determine el número de días que faltan hasta el final del presente año.
fecha1 = date.today()
fecha2 = date(2022, 12, 31)

delta = fecha2 - fecha1
print(delta)

# %%
# 3. Usando la función strptime() convierta las siguientes cadenas de texto a fechas:
# - '3 March 1995'
# - '3/9/1995'
# - '21-07-2021'

fecha1 = datetime.strptime("3 March 1995", "%d %B %Y")
print(fecha1)

fecha2 = datetime.strptime("3/9/1995", "%d/%m/%Y")
print(fecha2)

fecha3 = datetime.strptime("21/07/2021", "%d/%m/%Y")
print(fecha3)

# %%
# 4. Usando la función strftime() formatee la fecha: 2021-04-20 11:30:00 a los siguientes formatos:
# - 2021-04-20
# - 20-04-2021
# - 20/04/21 11:30
# - 11:30:00

fecha = datetime.strptime("2021-04-20 11:30:00", "%Y-%m-%d %H:%M:%S")
print(fecha)

print(datetime.strftime(fecha, "%Y-%m-%d"))
print(datetime.strftime(fecha, "%d-%m-%Y"))
print(datetime.strftime(fecha, "%d/%m/%y %H:%M"))
print(datetime.strftime(fecha, "%H:%M:%S"))

# %%
# 5. Partiendo de la fecha 2021-01-01 00:00:00, obtener las siguientes:
# - desplazada por 7 días
# - desplazada por 30 días y 4 horas
# - desplazada por -4 minutos
# - desplazada por 1 día, 3 horas y 10 minutos

fecha = datetime(2021, 1, 1)

fecha1 = fecha + timedelta(days=7)
print(f'Fecha {fecha} desplazada 7 días es: {fecha1}')

fecha2 = fecha + timedelta(days=30, hours=4)
print(f'Fecha {fecha} desplazada 30 días y 4 horas: {fecha2}')

fecha3 = fecha + timedelta(minutes=-4)
print(f'Fecha {fecha} desplazada -4 minutos: {fecha3}')

fecha4 = fecha + timedelta(days=1, hours=3, minutes=10)
print(f'Fecha {fecha} desplazada 1 día, 3 horas y 10 minutos: {fecha4}') 


# %%
#Permitir ingresar por teclado la edad actual de una persona, y:
# - Calcule su edad actual
# - Identifique la generación a la cual pertenece: Builders, Baby Boomers, Generación X, Generación Y (Millenials), Generación Z ó Generación α

respuesta = input('Cual es su fecha nacimiento? (dd-mm-aaaa) >')

fecha_nacimiento = datetime.strptime(respuesta, '%d-%m-%Y')

edad = relativedelta(datetime.now(), fecha_nacimiento)

print(f"Edad: {edad.years} años, {edad.months} meses y {edad.days} días")

anio_nacimiento = fecha_nacimiento.year
print(f'Año de nacimiento: {anio_nacimiento}')

if anio_nacimiento<1946:
    generacion = 'BUILDER'
elif anio_nacimiento >= 1946 and anio_nacimiento<=1964:
    generacion = 'BABY BOOMER'
elif anio_nacimiento >= 1965 and anio_nacimiento<=1979:
    generacion = 'GENERACION X'
elif anio_nacimiento >= 1980 and anio_nacimiento<=1994:
    generacion = 'MILLENIAL'
elif anio_nacimiento >= 1995 and anio_nacimiento<=2009:
    generacion = 'GENERACION Z'
else: 
    generacion = 'GENERACION α'

print(f'Generación: {generacion}')
# %%
