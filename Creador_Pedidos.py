from Creador_Productos import Producto
from collections import Counter
from Setup import precio_partes
import logging




def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='DebugLog.log')


class Pedido:
    def __init__(self, nombre, detalle_pedido, lista_productos, partes_posibles, interes):
        self.nombre = nombre
        self.pedido = detalle_pedido
        self.lista_productos = lista_productos
        self.partes_posibles = partes_posibles
        self.interes = interes if interes is not None else []

    def costo_pedido(self):
        costo_total_pedido = 0
        for product in self.lista_productos:
            if product.nombre in self.pedido:
                costo_total_pedido += product.costo_producto() * self.pedido[product.nombre]
        return costo_total_pedido

    def total_partes(self):

        total_partes = {}
        for product in self.lista_productos:
            if product.nombre in self.pedido:
                temp_partes = {}
                for parte in product.q_partes:
                    temp_partes[parte] = product.q_partes[parte] * self.pedido[product.nombre]
                total_partes = Counter(total_partes)
                temp_partes = Counter(temp_partes)
                total_partes = total_partes + temp_partes
        total_partes_dict = dict(total_partes)
        for parte in self.partes_posibles:  # Para rellenar casos donde en que producto no tiene una parte en especial
            if parte not in total_partes_dict:
                total_partes_dict[parte] = 0
        return total_partes_dict

    def info(self):
        print('El pedido {} costó ${} y tiene:'.format(self.nombre, self.costo_pedido()))
        for parte in self.partes_posibles:
            print('{} {}'.format(self.total_partes()[parte], parte))
        print("Esta compuesto por: ")
        for key in self.pedido:
            print("{} {}".format(self.pedido[key], key))

    def check_interes(self, interes):
        existe = False
        for product in self.lista_productos:
            if interes == product.tipo:
                existe = True
        if existe:
            logging.info("{} es una preferencia valida".format(interes))
            pass
        else:
            logging.info("No existe {} como preferencia".format(interes))
            print("No existe {} como preferencia".format(interes))
            pass

    def alternativa_interes(self):
        alternativas_de_interes = []
        for interest in self.interes: # Junta en una lista el tipo de interes, eliminando los productos que vienen con el pedido
            self.check_interes(interest)
            for product in self.lista_productos:
                if product.tipo == interest:
                    logging.debug("Alternativa {} agregada porque es tipo {}".format(product.nombre, product.tipo))
                    alternativas_de_interes.append(product)
        for product in self.pedido: #elimina de la lista de alternativas que son parte del pedido
            for i in alternativas_de_interes:
                if product == i.nombre:
                    logging.debug("{} removida, esta dentro del pedido".format(i.nombre))
                    alternativas_de_interes.remove(i)
        if not alternativas_de_interes:
            logging.debug("No hay alternativas de interes")
        else:
            for i in alternativas_de_interes:   #Para DEBUG
                logging.debug("{} queda como alternativa de interes".format(i.nombre))
        return alternativas_de_interes

    def calculo_q_alternativas(self):
        alternativas_de_interes = self.alternativa_interes()
        tope_de_parte = {}
        for alternativa in alternativas_de_interes:
            tope_de_parte[alternativa.nombre] = None
            for key in alternativa.q_partes:
                logging.info("El {} tiene {} de {}".format(alternativa.nombre, alternativa.q_partes[key], key))
                logging.info("El pedido tiene {} de la parte {}, se pueden formar {} {}".format(self.total_partes()[key], key, self.total_partes()[key]/alternativa.q_partes[key], alternativa.nombre))
                max_temp = self.total_partes()[key] // alternativa.q_partes[key]
                if not tope_de_parte[alternativa.nombre] or tope_de_parte[alternativa.nombre] > max_temp:
                    tope_de_parte[alternativa.nombre] = max_temp
        print("Con el {} se pueden crear:".format(self.nombre)) if tope_de_parte else print("No se pueden formar otros productos")
        for product in tope_de_parte:
            print("{} {}".format(tope_de_parte[product], product))
            logging.info("{} {}".format(tope_de_parte[product], product))
        return tope_de_parte




def inicializador_de_productos(
        listado_productos):  # Devuelve una lista con los objetos de productos detallados en listado_productos
    lista_clase_productos = []
    for key in listado_productos:
        lista_clase_productos.append(
            Producto(key, precio_partes, listado_productos[key]["Composicion"], listado_productos[key]["Tipo"]))
        # print(listado_productos[1])
    return lista_clase_productos


if __name__ == '__main__':
    main()
