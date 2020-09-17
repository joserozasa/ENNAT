def main():
    precio_partes = {
        "p_parte1": 2,
        "p_parte2": 3,
        "p_parte3": 4,
        "p_parte4": 5
    }

    productoA = [0, 2, 3, 1]
    productoB = [3, 2, 1, 0]

    Producto_A = Producto(precio_partes, productoA)
    Producto_B = Producto(precio_partes, productoB)

    print(Producto_A.compuesto_por())
    print(Producto_B.compuesto_por())



class Producto:

    def __init__(self, precios, q_partes):
        self.q_parte1 = q_partes[0]
        self.q_parte2 = q_partes[1]
        self.q_parte3 = q_partes[2]
        self.q_parte4 = q_partes[3]
        self.p_parte1 = precios['p_parte1']
        self.p_parte2 = precios['p_parte2']
        self.p_parte3 = precios['p_parte3']
        self.p_parte4 = precios['p_parte4']

    def compuesto_por(self):
        print('de la Parte 1 hay: {} que cuestan {}'.format(self.q_parte1, self.p_parte1))
        print('de la Parte 2 hay: {} que cuestan {}'.format(self.q_parte2, self.p_parte2))
        print('de la Parte 3 hay: {} que cuestan {}'.format(self.q_parte3, self.p_parte3))
        print('de la Parte 4 hay: {} que cuestan {}'.format(self.q_parte4, self.p_parte4))



if __name__ == '__main__':
    main()



