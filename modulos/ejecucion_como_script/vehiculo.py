import motor

def rodar():
    motor.encender()
    i = 1
    while(i<=10):
        motor.acelerar()
        i+=1

def detener():
    i = 10
    while(i>=0):
        motor.desacelerar()
        i-=1
    motor.apagar()

def main():
    rodar()
    detener()

if __name__ == '__main__':
    main()