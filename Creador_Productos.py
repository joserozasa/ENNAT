def main():

    precio_partes = {"parte_1": 2, "parte_2": 3, "parte_3": 4, "parte_4": 5, "parte_5": 100}

    listado_generador_productos = {
        "Producto_A": {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 1},
        "Producto_B": {"parte_1": 1, "parte_3": 3, "parte_4": 1, "parte_5": 1},
        "Producto_C": {"parte_1": 4, "parte_2": 4, "parte_3": 3, "parte_4": 5, "parte_5": 1},
        "Producto_D": {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1},
        "Producto_E": {"parte_1": 1, "parte_2": 1, "parte_3": 1, "parte_4": 1, "parte_5": 100}
    }

    def iniciador_productos(
            listado_productos):  # Devuelve una lista con los objetos de productos detallados en listado_productos
        lista_clase_productos = []
        for key in listado_productos:
            lista_clase_productos.append(Producto(key, precio_partes, listado_productos[key]))
        return lista_clase_productos

    lista_clases_productos = iniciador_productos(listado_generador_productos)




class Producto:

    def __init__(self, nombre, precios, q_partes, tipo):
        self.nombre = nombre
        self.q_partes = q_partes
        self.p_partes = precios
        self.n_partes = len(q_partes)
        self.tipo = tipo

    def compuesto_por(self):
        for key in self.p_partes:
            if key in self.q_partes:
                print ("{} partes {}, que cada una cuesta ${}".format(self.q_partes[key], key, self.p_partes[key]))

    def costo_producto(self):
        costo_total = 0
        for key in self.p_partes:
            if key in self.q_partes:
                costo_total += self.p_partes[key]*self.q_partes[key]
        return costo_total

    def q_parte_x(self, nombre_parte):
        nombre_parte = nombre_parte
        try:
            print("esta producto tiene {} partes {}".format(self.q_partes[nombre_parte], nombre_parte))
        except:
            print("Esa pieza no existe o esta mal escrita")
        return self.q_partes[nombre_parte]



if __name__ == '__main__':
    main()




