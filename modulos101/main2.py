# main2.py

# importando funciones específicas del módulo calculadora
from calculadora import sumar, restar, multiplicar, dividir

operacion = input('Ingrese la operación que desea realizar +, -, * ó /:')

if operacion in ['+', '-', '*', '/']:
    n1 = int(input('Ingrese un número: '))
    n2 = int(input('Ingrese otro número: '))

    if operacion=='+':
        # utilizando la función sumar del módulo calculadora
        r = sumar(n1, n2)
    elif operacion=='-':
        # utilizando la función restar del módulo calculadora
        r = restar(n1, n2)
    elif operacion=='*':
        # utilizando la función multiplicar del módulo calculadora
        r = multiplicar(n1, n2)
    else:
        # utilizando la función dividir del módulo calculadora
        r = dividir(n1, n2)

    print('El resultado es:', r)

else:
    print('¡Operación inválida!')