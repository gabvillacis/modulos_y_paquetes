from acceso_datos import Producto

tab = '\t\t\t'

def capturar_comando():
    while True:
        print()
        print("Que te gustaría realizar?")
        print()
        print("  A = Agregar un producto al inventario.")
        print("  E = Eliminar un producto del inventario.")
        print("  RC = Generar reporte del inventario ordenado por código.")
        print("  RN = Generar reporte del inventario ordenado por nombre.")
        print("  RP = Generar reporte del inventario ordenado por precio.")
        print("  S = Salir.")
        print()
        comando = input("> ").strip().upper()
        if   comando == "A": return "AGREGAR"
        elif comando == "E": return "ELIMINAR"
        elif comando == "RC": return "REPORTE_ORD_POR_CODIGO"
        elif comando == "RN": return "REPORTE_ORD_POR_NOMBRE"
        elif comando == "RP": return "REPORTE_ORD_POR_PRECIO"
        elif comando == "S": return "SALIR"
        else:
            print("Comando inválido, intente de nuevo.")


def capturar_numero(mensaje):
    while True:
        try:
            return float(input(f'{mensaje} '))
        except ValueError:
            print("ERROR: Debe digitar un número válido")


def capturar_producto():
    print()
    print("-- Ingreso de Nuevo Producto --")
    codigo = input("Ingrese el código: ").strip().upper()
    nombre = input("Ingrese el nombre: ").strip()
    precio = capturar_numero("Ingrese el precio:")

    return Producto(codigo, nombre, precio)


def capturar_codigo_producto():
    print()
    codigo = input("Ingrese el código del producto: ").strip().upper()
    return codigo


def mostrar_reporte(inventario_productos):
    print()
    print('----- Reporte de Inventario -----')
    i = 1
    print('No.' + tab + 'Código' + tab + 'Nombre'.ljust(25)  + tab + 'Precio')
    for prod in inventario_productos:
        print(f'{i}{tab}{prod.codigo.ljust(6)}{tab}{prod.nombre.ljust(25)}{tab}{prod.precio}')
        i += 1
    print('---------------------------------')


def mostrar_mensaje(mensaje):
    print()
    print(mensaje)