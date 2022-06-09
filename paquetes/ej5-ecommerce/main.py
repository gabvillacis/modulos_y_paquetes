import ui
from inventario.logica import InventarioService

inventario_service = InventarioService()

def main() -> None:
    while True:
        menu_principal = {  'A': 'AGREGAR PRODUCTO',
                            'B': 'QUITAR PRODUCTO',
                            'C': 'LISTAR PRODUCTOS',
                            'D': 'AÑADIR PRODUCTO AL CARRITO',
                            'E': 'QUITAR PRODUCTO DEL CARRITO',
                            'F': 'FACTURAR',
                            'G': 'SALIR' }

        ui.mostrar_menu('MENÚ PRINCIPAL', '¿Qué opción desea ejecutar?', menu_principal)
        opcion = ui.capturar_opcion_menu(menu_principal.keys())
        
        if opcion == 'A':
            ejecutar_agregar_producto()
        elif opcion == 'B':
            pass
        elif opcion == 'C':            
            pass
        elif opcion == 'D':
            pass
        elif opcion == 'E':
            pass
        elif opcion == 'F':
            pass
        else:
            break
        

def ejecutar_agregar_producto() -> None:
    producto = ui.capturar_producto()
    try:
        inventario_service.agregar_producto(producto)
        ui.mostrar_mensaje(f'El producto {producto.codigo} se agregó exitosamente.')
    except Exception as ex:
        ui.mostrar_mensaje(ex)
    

if __name__ == "__main__":
    main()