
from Creador_Pedidos import Pedido, inicializador_de_productos
from Setup import pedido, partes_posibles, precio_partes, listado_generador_productos

lista_de_clases = inicializador_de_productos(listado_generador_productos)

interes = ["Tope", "Barrera_6"]

pedido1 = Pedido('Pedido 1', pedido, lista_de_clases, partes_posibles, interes)



pedido1.Alternativa_Interes()

pedido1.Info()


