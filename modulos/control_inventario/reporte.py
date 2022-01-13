def generar_inventario_ordenado_por_codigo(inventario_productos):
    return sorted(inventario_productos, key=lambda prod: prod.codigo)

def generar_inventario_ordenado_por_nombre(inventario_productos):
    return sorted(inventario_productos, key=lambda prod: prod.nombre)

def generar_inventario_ordenado_por_precio(inventario_productos):
    return sorted(inventario_productos, key=lambda prod: prod.precio)