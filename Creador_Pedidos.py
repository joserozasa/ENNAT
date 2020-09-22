
from Creador_Productos import Producto
from collections import Counter
from Setup import precio_partes

def main():
    pass





class Pedido():
    def __init__(self,nombre, detalle_pedido, lista_productos, partes_posibles, interes):
        self.nombre = nombre
        self.pedido = detalle_pedido
        self.lista_productos = lista_productos
        self.partes_posibles = partes_posibles
        self.interes = interes


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

    def Info(self):
        print('El pedido {} costó ${} y tiene:'.format(self.nombre, self.costo_pedido()))
        for parte in self.partes_posibles:
            print('{} {}'.format(self.total_partes()[parte], parte))
        print("Esta compuesto por: ")
        for key in self.pedido:
            print("{} {}".format(self.pedido[key], key))

    def Check_Interes(self, interes):
        existe = False
        for product in self.lista_productos:
            if interes == product.tipo:
                existe = True
        if existe:
            #print("{} es una preferencia válida".format(interes))
            pass
        else:
            #print("no existe {} como preferencia".format(interes))
            pass
    def Alternativa_Interes(self):
        alternativas_de_interes = []
        for interest in self.interes:
            self.Check_Interes(interest)
            for product in self.lista_productos:
                if product.tipo == interest:
                    alternativas_de_interes.append(product)
        for product in self.pedido:
            for i in alternativas_de_interes:
                if product == i.nombre:
                    alternativas_de_interes.remove(i)
        tope_de_parte=[]
        for alternativa in alternativas_de_interes:
            max_temp = 0
            print(alternativa.nombre)
            print(alternativa.q_partes)
            for parte in alternativa.q_partes:
                max_temp = self.total_partes()[parte] // alternativa.q_partes[parte]
                tope_de_parte.append(max_temp)
        print(tope_de_parte) #Aqui quede, estaba viendo cuantas partes alternativas se podría hacer con las piezas del pedido original.
        for i in alternativas_de_interes:
            #print(i.nombre)
            pass
        if not alternativas_de_interes:
            #print("Los intereses calzan con el pedido")
            pass

def inicializador_de_productos(listado_productos):  # Devuelve una lista con los objetos de productos detallados en listado_productos
    lista_clase_productos = []
    for key in listado_productos:
        lista_clase_productos.append(Producto(key, precio_partes, listado_productos[key]["Composicion"],listado_productos[key]["Tipo"]))
        #print(listado_productos[1])
    return lista_clase_productos



if __name__ == '__main__':
    main()

