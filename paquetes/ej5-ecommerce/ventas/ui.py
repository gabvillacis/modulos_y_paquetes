from ..ui_utils import mostrar_menu

def mostrar_menu_ventas() -> None:
    menu_inventario = { 'A': 'LISTAR PRODUCTOS',
                        'B': 'AÑADIR PRODUCTO AL CARRITO',
                        'C': 'QUITAR PRODUCTO DEL CARRITO',
                        'D': 'REGRESAR A MENÚ PRINCIPAL' }
    mostrar_menu()

