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

    def agregar_nodo_y_desplazar(self, nodo, nuevo_nodo):
        nuevo_nodo.dir = nodo.dir
        nodo.dir = nuevo_nodo # FOTY

    def insertar_por_valor(self, valor, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)
        if self.primer_nodo is None:
            print("No existe lista a recorrer")
        else:
            nodo = self.primer_nodo

            while nodo is not None:
                nodo = nodo.dir

                if nodo.item == valor:
                    self.agregar_nodo_y_desplazar(nodo, nuevo_nodo)
                    break
                    



class Nodo:
    def __init__(self, valor):
        self.item = valor
        self.dir = None

lista = Lista()

while True:
    print("_______________________")
    print("|        Menu         |")
    print("|1. Insertar al inicio|")
    print("|2. Recorrer lista    |")
    print("|3. Insertar por valor|")
    print("|4. Salir             |")
    print("-----------------------")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        os.system("cls")
        valor = int(input("Ingrese un valor: "))
        lista.insertar_inicio(valor)
    elif opcion == 2:
        print("La lista es:")
        lista.recorrer_lista()
        print()
    
    elif opcion == 3:
        valor = int(input("Ingrese el valor a remplazar: "))
        nuevo_valor = int(input("Ingrese un nuevo valor: "))
        lista.insertar_por_valor(valor, nuevo_valor)
    elif opcion == 4:
        break
    else:
        print("Opcion incorrecta")
        # limpiar pantalla
        os.system("cls")