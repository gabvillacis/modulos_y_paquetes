from acceso_datos import Inventario, Producto
import interfaz_usuario as ui
import reporte as rep

def main():

    inventario = Inventario()
    inventario.agregar_producto(Producto('PROD1', 'Auto Kia Rio R', 19999.99))
    inventario.agregar_producto(Producto('PROD2', 'Licencia Pycharm', 80.99))
    inventario.agregar_producto(Producto('PROD3', 'Celular Samsung A10', 499.99))
    inventario.agregar_producto(Producto('PROD4', 'Laptop HP Pavilion', 1750.00))

    while True:
        comando = ui.capturar_comando()
        if comando == "SALIR":
            break

        elif comando == "AGREGAR":
            producto = ui.capturar_producto()
            inventario.agregar_producto(producto)
            ui.mostrar_mensaje("Producto agregado exitosamente al inventario.")

        elif comando == "ELIMINAR":
            codigo_producto = ui.capturar_codigo_producto()
            producto_seleccionado = inventario.buscar_producto_por_codigo(codigo_producto)
            if producto_seleccionado is None:
                ui.mostrar_mensaje(f"El producto con código: {codigo_producto} no existe.")
            else:
                inventario.quitar_producto(producto_seleccionado)
                ui.mostrar_mensaje("Producto eliminado exitosamente del inventario.")

        elif comando == "REPORTE_ORD_POR_CODIGO":
            inventario_productos_ord = rep.generar_inventario_ordenado_por_codigo(inventario.productos)
            ui.mostrar_reporte(inventario_productos_ord)

        elif comando == "REPORTE_ORD_POR_NOMBRE":
            inventario_productos_ord = rep.generar_inventario_ordenado_por_nombre(inventario.productos)
            ui.mostrar_reporte(inventario_productos_ord)

        elif comando == "REPORTE_ORD_POR_PRECIO":
            inventario_productos_ord = rep.generar_inventario_ordenado_por_precio(inventario.productos)
            ui.mostrar_reporte(inventario_productos_ord)

if __name__ == "__main__":
    main()