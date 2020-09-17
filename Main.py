
from CreadorProductos import Producto

input_producto = 100
pedidoA = [100,50,10]

precio_partes = {
    "p_parte1": 2,
    "p_parte2": 3,
    "p_parte3": 4,
    "p_parte4": 5
}



partes_productoA = [0, 2, 3, 1]
partes_productoB = [3, 2, 1, 0]
partes_productoC = [4, 3, 5, 6]


Producto_A = Producto(precio_partes, partes_productoA)
Producto_B = Producto(precio_partes, partes_productoB)
Producto_C = Producto(precio_partes, partes_productoC)


def valor_compra(Pedido, Producto):
    pedido = Pedido
    producto = Producto
    producto.compuesto_por()
    for i in range(len(pedido)):
        print(pedido[i])



costo_producto(Producto_A)