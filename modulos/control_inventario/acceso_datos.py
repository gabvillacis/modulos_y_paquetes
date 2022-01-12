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

items = []
productos = []
ubicaciones = []

def obtener_items():
    global items
    return items

def obtener_productos():
    global productos
    return productos

def obtener_ubicaciones():
    global ubicaciones
    return ubicaciones

def agregar_item(codigo_producto, codigo_ubicacion):
    global items
    items.append((codigo_producto, codigo_ubicacion))

def quitar_item(codigo_producto, codigo_ubicacion):
    global items
    for i in range(len(items)):
        _codigo_prod, _codigo_ubic = items[i]
        if _codigo_prod == codigo_producto and _codigo_ubic == codigo_ubicacion:
            del items[i]
            return True
    return False

def inicializar_productos(productos):
    global productos
    products = productos

def set_locations(locations):
    """ Set the (currently hardwired) list of inventory locations.
        Each item in the 'locations' list should be a (code, description)
        tuple, where 'code is the code for an inventory location, and
        'description' is a string describing that location so that the user
        knows where it is.
    """
    global _locations
    _locations = locations