class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None
        self.ant = None

def insertar_inicio(self, valor):
    if self.primer_nodo is None:
        self.insertar_vacia(valor)
        return
    else:
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.sig = self.primer_nodo
        nuevo_nodo.ant = nuevo_nodo
        self.primer_nodo = nuevo_nodo

def insertar_final(self, valor):
    if self.primer_nodo is None:
        self.insertar_vacia(valor)
        return
    
def recorrer_lista(self):
    if self.primer_nodo is None:
        print("No existe lista a recorrer")
        return
    else:
        n = self.primer_nodo
        while n is not None:
            print(n.valor)
            n = n.sig
    

    n = self.primer_nodo
    while n.sig is not None:
        n = n.sig
    nuevo_nodo = Nodo(valor)
    n.sig = nuevo_nodo
    nuevo_nodo.ant = n