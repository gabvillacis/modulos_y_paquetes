from .modelos.inventario import Inventario
from .modelos.producto import Producto

class InventarioService:
    def __init__(self) -> None:
        self.inventario = Inventario()


    def agregar_producto(self, producto: Producto) -> None:
        producto_existente = self.inventario.buscar_producto_por_codigo(producto.codigo)
        if producto_existente == None:
            self.inventario.agregar_producto(producto)
        else:
            raise Exception(f'El producto {producto.codigo} ya existe en el inventario')


    def quitar_producto(self, producto: Producto) -> None:
        self.inventario.quitar_producto(producto)