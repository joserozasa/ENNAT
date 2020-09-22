
pedido = {"Producto_A": 1, "Producto_E": 1}  # Detalle de la cantidad de cada producto en el pedido


partes_posibles = {"parte_1": 0, "parte_2": 0, "parte_3": 0, "parte_4": 0, "parte_5": 0} # Solo actualizar cuando se agrega una nueva parte a los productos

precio_partes = {"parte_1": 2, "parte_2": 3, "parte_3": 4, "parte_4": 5, "parte_5": 100} # Solo actualizar cuando se agrega una nueva parte a los productos

listado_generador_productos = {
    "Producto_A": {"Composicion" : {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 1},"Tipo" : "Barrera_1"},
    "Producto_B": {"Composicion" : {"parte_1": 2, "parte_2": 2, "parte_3": 2, "parte_4": 2, "parte_5": 2},"Tipo" : "Barrera_2"},
    "Producto_C": {"Composicion" : {"parte_1": 2 },"Tipo" : "Tope"},
    "Producto_D": {"Composicion" : {"parte_1": 4, "parte_2": 4, "parte_3": 4, "parte_5": 4},"Tipo" : "Tope"},
    "Producto_E": {"Composicion" : {"parte_1": 6, "parte_2": 6, "parte_3": 6, "parte_4": 6, "parte_5": 6},"Tipo" : "Barrera_3"},

}
