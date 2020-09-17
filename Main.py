
from Creador_Productos import Producto
from Creador_Pedidos import Pedido


pedido = {"Producto_A": 100, "Producto_C": 3}

precio_partes = {"parte_1": 2, "parte_2": 3, "parte_3": 4, "parte_4": 5, "parte_5": 100 }

listado_generador_productos = {
        "Producto_A" : {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 1},
        "Producto_B" : {"parte_1": 1, "parte_3": 3, "parte_4": 1, "parte_5": 1},
        "Producto_C" : {"parte_1": 4, "parte_2": 4, "parte_3": 3, "parte_4": 5, "parte_5": 1},
        "Producto_D" : {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1},
        "Producto_E" : {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 100}
        }
def iniciador_productos(listado_productos):  # Devuelve una lista con los objetos de productos detallados en listado_productos
    lista_clase_productos = []
    for key in listado_productos:
        lista_clase_productos.append(Producto(key, precio_partes, listado_productos[key]))
    return lista_clase_productos
lista_de_clases = iniciador_productos(listado_generador_productos)





pedido1 = Pedido(pedido, lista_de_clases)

dict = pedido1.total_partes()

print(dict)