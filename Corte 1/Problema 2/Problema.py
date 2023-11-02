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
    for i in range(800):
        vector.append(random.randint(4*n/5, n))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(3*n/5, 4*n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(2*n/5, 3*n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(n/5, 2*n/5))
        print(vector[i])
    for i in range(800):
        vector.append(random.randint(1, n/5))
        print(vector[i])

for i in range(len(vector)):
    for j in range(len(vector) - 1):
        if vector[j] > vector[j + 1]:
            aux = vector[j]
            vector[j] = vector[j + 1]
            vector[j + 1] = aux

for i in range(len(vector)):
    print(vector[i])

end = time.time()

print("Tiempo de ejecucion: ", end - start)