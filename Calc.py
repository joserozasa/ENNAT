
from CreadorProductos import Producto

precio_partes = {
    "p_parte1": 2,
    "p_parte2": 3,
    "p_parte3": 4,
    "p_parte4": 5
}

productoA = [0, 2, 3, 1]
productoB = [3, 2, 1, 0]
productoC = [4, 3, 5, 6]


Producto_A = Producto(precio_partes, productoA)
Producto_B = Producto(precio_partes, productoB)
Producto_C = Producto(precio_partes, productoC)

print(Producto_C.compuesto_por())