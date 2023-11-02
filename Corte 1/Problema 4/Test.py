import random
import time

def partition(array, low, high):
    pivot = array[high] # seleccionamos el último elemento como pivote
    i = low - 1 # índice del elemento más pequeño

    for j in range(low, high): # recorremos el array
        if array[j] <= pivot: # si el elemento actual es menor o igual al pivote
            i += 1 # incrementamos el índice del elemento más pequeño
            array[i], array[j] = array[j], array[i] # intercambiamos los elementos
    
    array[i + 1], array[high] = array[high], array[i + 1] # intercambiamos el pivote con el elemento más pequeño

    return i + 1 # retornamos la posición en la que la partición divide el array

def quickSort(array, low, high): # función para ordenar el array
    if low < high:
        pi = partition(array, low, high) # encontramos la posición de la partición en la que el elemento más pequeño está en la izquierda y el más grande en la derecha

        quickSort(array, low, pi - 1) # llamada recursiva en la parte izquierda del array
        quickSort(array, pi + 1, high) # llamada recursiva en la parte derecha del array


n = int(input("Tamaño del vector: "))

start = time.time()

vector = []
count = 0
under_prom = 0
vector_under_prom = []

for i in range(n):
        vector.append(random.randrange(0, 10, 2))
        count += vector[i]

prom = count/n

for i in vector:
        if vector[i] < prom:
                under_prom += 1
                vector_under_prom.append(vector[i])

print("Números menores al promedio:", vector_under_prom)

if under_prom < n//2:
    quickSort(vector_under_prom, 0, len(vector_under_prom) - 1)

end = time.time()

print("Vector ordenado, tiempo:", end - start)