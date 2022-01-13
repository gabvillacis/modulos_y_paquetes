class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'(Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio})'


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto_por_codigo(self, codigo_producto):
        for producto in self.productos:
            if producto.codigo == codigo_producto:
                return producto
        return None

    def quitar_producto(self, producto):
        self.productos.remove(producto)