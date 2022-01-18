# time: https://docs.python.org/3/library/time.html

# importando módulo time
import time

# print(time.time())

def send_emails():
    for i in range(10000):
        pass

inicio = time.time()
send_emails()
fin = time.time()

duracion = fin - inicio
print(duracion)