import random
import time

n = int(input("Tamaño del vector: "))

while n <= 0:
    print("Tamaño inválido")
    n = int(input("Tamaño del vector: "))

inicio = time.time()

vector = []
pares = 0

for i in range(n):
    vector.append(random.randint(1, 1000))

    if vector[i] % 2 == 0:
        pares += 1

print("Porcentaje de pares:", pares*100/n)

fin = time.time()

print("Tiempo:", fin-inicio)