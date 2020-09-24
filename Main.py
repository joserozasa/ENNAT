
from Creador_Pedidos import Pedido, inicializador_de_productos
from Setup import partes_posibles, listado_generador_productos
from Input_Cliente import interes, nombre_pedido, pedido
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='DebugLog.log')
logging.debug("----------------------------INICIO PROGRAMA------------------------------------------")

lista_de_clases = inicializador_de_productos(listado_generador_productos)

pedido1 = Pedido(nombre_pedido, pedido, lista_de_clases, partes_posibles, interes)

pedido1.calculo_q_alternativas()

#pedido1.Info()


