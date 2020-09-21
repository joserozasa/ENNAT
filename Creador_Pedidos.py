
from Creador_Productos import Producto
from collections import Counter

def main():
    pass





class Pedido():
    def __init__(self,nombre, detalle_pedido, lista_productos, partes_posibles):
        self.nombre = nombre
        self.pedido = detalle_pedido
        self.lista_productos = lista_productos
        self. partes_posibles = partes_posibles


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
        for parte in self.partes_posibles: # Para rellenar casos donde en que producto no tiene una parte en especial
            if parte not in total_partes_dict:
                total_partes_dict[parte] = 0
        return total_partes_dict

    def info(self):
        print('El pedido {} costó ${} y tiene:'.format(self.nombre, self.costo_pedido()))
        for parte in self.partes_posibles:
            print('{} {}'.format(self.total_partes()[parte], parte))


if __name__ == '__main__':
    main()

