
from Creador_Productos import Producto
from collections import Counter

def main():
    pass





class Pedido():
    def __init__(self, detalle_pedido, lista_productos):
        self.pedido = detalle_pedido
        self.lista_productos = lista_productos


    def costo_pedido(self):
        costo_total_pedido = 0
        for product in self.lista_productos:
            if product.nombre in self.pedido:
                costo_total_pedido += product.costo_producto() * self.pedido[product.nombre]
        return costo_total_pedido

    def total_partes(self):
        total_partes = {}
        temp_partes = {}
        for product in self.lista_productos:
            if product.nombre in self.pedido:
                for parte in product.q_partes:
                    temp_partes[parte] = product.q_partes[parte]
                    z = dict(Counter(temp_partes) + Counter(total_partes))
                    #print(product.q_partes[parte])
                    #print(parte)
                #print(product.q_partes)
                #print(self.pedido[product.nombre])
        print(z)


if __name__ == '__main__':
    main()

