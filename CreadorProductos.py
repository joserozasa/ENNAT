def main():

    precio_partes = {"parte_1": 2, "parte_2": 3, "parte_3": 4, "parte_4": 5, "parte_5": 100 }

    q_partes_producto_A = {"parte_1": 0, "parte_2": 2, "parte_3": 3, "parte_4": 1, "parte_5": 1}
    q_partes_producto_B = {"parte_1": 0,               "parte_3": 3, "parte_4": 1, "parte_5": 1}

    Producto_A = Producto(precio_partes, q_partes_producto_A)
    Producto_B = Producto(precio_partes, q_partes_producto_B)

    print(Producto_A.costo_producto())
    print(Producto_B.costo_producto())



class Producto:

    def __init__(self, precios, q_partes):
        self.q_partes = q_partes
        self.p_partes = precios
        self.n_partes = len(q_partes)

    def compuesto_por(self):
        #print('de la Parte 1 hay: {} que cuestan {}'.format(self.q_parte1, self.p_parte1))
        pass

    def costo_producto(self):
        costo_total = 0
        for key in self.p_partes:
            if key in self.q_partes:
                costo_total += self.p_partes[key]*self.q_partes[key]
        return costo_total



if __name__ == '__main__':
    main()



