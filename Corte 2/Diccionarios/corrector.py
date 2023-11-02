import os

corrector = {}
f = open("corrector.txt","r") # "r" es para leer el archivo
x = f.readlines() # el método readlines toma el archivo que está en f y lo estructura en una lista renglón por renglón
lista1 = []

for i in x:
    lista1 = i.split(":")
    lista1[1] = lista1[1].replace("\n","") # elimina el caracter de salto de línea
    lista2 = lista1[1].split(",")
    corrector.setdefault(lista1[0],lista2) # lista1[0] es la llave y lista2 es el valor

f.close()

# hago una lista de los valores y otra de las llaves
valores = list(corrector.values())
llaves = list(corrector.keys())

frase = input("Escribe una frase: ")
l1 = frase.split(" ")

for i in valores:
    for j in l1:
        if j in i: # si la palabra incorrecta está en la lista de valores
            pregunta = input("¿Quieres corregir " + j + "? (s/n): ")
            if pregunta == "s":
                l1[l1.index(j)] = llaves[valores.index(i)] # la reemplazo por la llave correspondiente
            
print("\nFrase final: ")
for i in l1: # aquí ya está la frase corregida	
    print(i, end=" ")