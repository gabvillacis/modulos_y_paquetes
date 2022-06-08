def mostrar_mensaje(mensaje: str) -> None:
    print()
    print(mensaje)


def capturar_numero(instruccion: str) -> float:
    while True:
        try:
            return float(input(f'{instruccion} >> '))
        except ValueError:
            print('Debe digitar un número válido. Intente de nuevo.')


def mostrar_menu(titulo: str, instruccion: str, menu: dict) -> None:    
    print()
    print(titulo.upper())
    print()
    print(instruccion)
    print()

    for key, value in menu.items():
        print(f' {key} = {value}')    

        
def capturar_opcion_menu(opciones_permitidas: list) -> str:
    while True:
        opcion = input('Ingrese la opción >> ').strip().upper()

        if opcion not in opciones_permitidas:
            print('Opción inválida. Las opciones permitidas son: [' + ', '.join(opciones_permitidas) + ']. Intente de nuevo!')
            continue
        else:
            return opcion