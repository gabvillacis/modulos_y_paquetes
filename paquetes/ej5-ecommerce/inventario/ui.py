from ..ui_utils import mostrar_menu

def mostrar_menu_inventario() -> None:
    menu_inventario = { 'A': 'AGREGAR PRODUCTO',
                        'B': 'QUITAR PRODUCTO',
                        'C': 'REGRESAR A MENÚ PRINCIPAL' }
    mostrar_menu()


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
