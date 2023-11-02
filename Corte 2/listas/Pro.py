import os


class Lista:
    def __init__(self):
        Lista.primer_nodo = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.dir = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def recorrer_lista(self):
        if self.primer_nodo is None:
            print("No existe lista a recorrer")
        else:
            nodo = self.primer_nodo
            while nodo is not None:
                print(nodo.item)
                nodo = nodo.dir
    def buscar_valor(self, valor):
        contador = 0
        if self.primer_nodo is None:
            print("No existe lista a recorrer")
        else:
            nodo = self.primer_nodo
            while nodo is not None:
                if nodo.item == valor:
                    print("El valor existe y esta en la posicion: ", contador)
                    break
                else:
                    contador = contador + 1
                nodo = nodo.dir


            
                    



class Nodo:
    def __init__(self, valor):
        self.item = valor
        self.dir = None

lista = Lista()
lista.insertar_inicio(1)
lista.insertar_inicio(2)
lista.insertar_inicio(3)
lista.insertar_inicio(4)
lista.recorrer_lista()
lista.buscar_valor(3)