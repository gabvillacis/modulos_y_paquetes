# time: https://docs.python.org/3/library/time.html

# importando módulo time
import time

# print(time.time())

def send_emails():
    for i in range(1000000):
        pass

inicio = time.time()
print('Inicio:', inicio)
send_emails()
fin = time.time()
print('Fin:', fin)

duracion = fin - inicio
print('Duración: ', duracion)