def start():
    print('Motor encendido')

def stop():
    print('Motor detenido')

def run():
    print('\n')
    start()
    for i in range(1, 10):
        print('\ō͡≡o˞̶'*i)
    stop()


print('Ejecutando módulo:' + __name__)
run()


"""
print('El módulo ' + __name__ + ' fue importado')
"""

""" if __name__=='__main__':
    print('Ejecutando módulo:' + __name__)
    run() """