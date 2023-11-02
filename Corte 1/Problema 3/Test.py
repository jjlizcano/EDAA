import random
import time

print("1. Caso promedio \n2. Mejor caso \n3. Peor caso")

option = int(input("Opcion: "))
while option < 1 or option > 3:
    print("1. Caso promedio \n2. Mejor caso \n3. Peor caso")
    option = int(input("Opcion: "))

n = int(input("Ingrese el tamaño del vector: "))
while n < 0:
    n = input("Ingrese el tamaño del vector: ")

start = time.time()

vector = []

if option == 1:
    for i in range(n):
        vector.append(random.randint(0, 2000))
        print(vector[i])

elif option == 2:
    for i in range(800):
        vector.append(random.randint(1, n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(n/5, 2*n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(2*n/5, 3*n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(3*n/5, 4*n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(4*n/5, n))
        print(vector[i])

elif option == 3:
    for i in range(n//5): 
        vector.append(random.randint(1601, 2000))
        print(vector[i])

    for i in range(n//5):
        vector.append(random.randint(1201, 1600))
        print(vector[i])
    for i in range(n//5):
        vector.append(random.randint(801, 1200))
        print(vector[i])

    for i in range(n//5):
        vector.append(random.randint(401, 800))
        print(vector[i])

    for i in range(n//5):
        vector.append(random.randint(1, 400))
        print(vector[i])

# función para encontrar la posición de la partición
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

quickSort(vector, 0, len(vector) - 1) # llamada a la función quickSort

for i in range(len(vector)):
    print(vector[i])

end = time.time()

print("Tiempo de ejecucion: ", end - start)