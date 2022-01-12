# https://github.com/PacktPublishing/Modular-Programming-with-Python/tree/master/chapter-2


# acceso_datos.py
#
# Almacenamos nuestros datos en tres variables globales:
#
#   'items'
#       La lista del inventario actual de items. Cada elemento en esta lista
#       es una tupla (codigo_producto, codigo_ubicacion).
#
#
#   'productos'
#       La lista de productos que se pueden añadir al inventario. Cada elemento en esta lista
#       es una tupla (codigo, descripcion, cantidad_deseada), donde 'codigo' es el código que
#       identifica al producto, 'descripcion' es una cadena que describe el producto y
#       'cantidad_deseada' es la cantidad de elementos que el usuario desea mantener en el inventario.
#
#
#   'ubicaciones'
#       La lista de ubicaciones donde se puede almacenar el inventario. Cada elemento en esta lista
#       es una tupla (codigo, descripcion), donde 'codigo' es el código para una ubicación del inventario
#       y 'descripcion' es una cadena que describe esa ubicación, de tal manera que el usuario sepa dónde está.

_items = []
_productos = []
_ubicaciones = []

def obtener_items():
    global _items
    return _items

def get_productos():
    global _productos
    return _productos

def set_productos(productos):
    global _productos
    _products = productos
    
def get_ubicaciones():
    global _ubicaciones
    return _ubicaciones

def set_ubicaciones(ubicaciones):
    global _ubicaciones
    _ubicaciones = ubicaciones

def agregar_item(codigo_prod, codigo_ubic):
    global _items
    _items.append((codigo_prod, codigo_ubic))

def quitar_item(codigo_prod, codigo_ubic):
    global _items
    for i in range(len(_items)):
        codigo_producto, codigo_ubicacion = _items[i]
        if codigo_producto == codigo_prod and codigo_ubicacion == codigo_ubic:
            del _items[i]
            return True
    return False
