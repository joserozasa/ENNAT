from Creador_Productos import Producto
from Creador_Pedidos import Pedido
from Setup import pedido, partes_posibles, precio_partes, listado_generador_productos




def inicializador_de_productos(listado_productos):  # Devuelve una lista con los objetos de productos detallados en listado_productos
    lista_clase_productos = []
    for key in listado_productos:
        lista_clase_productos.append(Producto(key, precio_partes, listado_productos[key]))
    return lista_clase_productos


lista_de_clases = inicializador_de_productos(listado_generador_productos)

pedido1 = Pedido('Pedido 1', pedido, lista_de_clases, partes_posibles)

pedido1.info()


