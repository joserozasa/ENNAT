def main():

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




