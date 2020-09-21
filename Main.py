from Creador_Productos import Producto
from Creador_Pedidos import Pedido

pedido = {"Producto_A": 0, "Producto_B": 10}

partes_posibles = {"parte_1": 0, "parte_2": 0, "parte_3": 0, "parte_4": 0, "parte_5": 0}

precio_partes = {"parte_1": 2, "parte_2": 3, "parte_3": 4, "parte_4": 5, "parte_5": 100}

listado_generador_productos = {
    "Producto_A": {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 1},
    "Producto_B": {"parte_1": 1, "parte_3": 3, "parte_4": 1, "parte_5": 1},
    "Producto_C": {"parte_1": 4, "parte_2": 4, "parte_3": 3, "parte_4": 5, "parte_5": 1},
    "Producto_D": {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1},
    "Producto_E": {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 100}
}


def iniciador_productos(listado_productos):  # Devuelve una lista con los objetos de productos detallados en listado_productos
    lista_clase_productos = []
    for key in listado_productos:
        lista_clase_productos.append(Producto(key, precio_partes, listado_productos[key]))
    return lista_clase_productos


lista_de_clases = iniciador_productos(listado_generador_productos)

pedido1 = Pedido('Pedido 1', pedido, lista_de_clases, partes_posibles)

total_de_partes = pedido1.total_partes()
costo_total_pedido = pedido1.costo_pedido()


print('El pedido {} costó {} y tiene {} Partes 1, {} Partes 2, {} Partes 3, {} Partes 4, {} Partes 5'.format(pedido1.nombre, pedido1.costo_pedido(), pedido1.total_partes()['parte_1'],  pedido1.total_partes()['parte_2'],  pedido1.total_partes()['parte_3'],  pedido1.total_partes()['parte_4'],  pedido1.total_partes()['parte_5']) )
