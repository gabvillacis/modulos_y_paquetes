"""
TODO Quitar las funciones turn_on_lights/turn_off_lights,
dado que no están directamente relacionadas con el motor.

Replantear el ejemplo en el contexto <carro usa el motor>.
"""

def start():
    print('Motor encendido')


def turn_on_lights():
    print('Luces encendidas')


def turn_off_lights():
    print('Luces apagadas')


def stop():
    print('Motor detenido')


def run():
    print('\n')
    start()
    turn_on_lights()
    for i in range(1, 10):
        print('\ō͡≡o˞̶'*i)
    turn_off_lights()
    stop()

"""
print('Ejecutando módulo:' + __name__)
run()
"""

"""
print('El módulo ' + __name__ + ' fue importado')
"""

if __name__=='__main__':
    print('Ejecutando módulo:' + __name__)
    run()