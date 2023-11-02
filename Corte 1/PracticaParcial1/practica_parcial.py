import random
n = int(input("Longitud del vector: "))
X = n//4
vector = []

for i in range(n):
    vector.append(random.randint(1, 100))

for i in range(n):
    for j in range(n-1):
        if vector[j] > vector[j+1]:
            aux = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = aux

print(vector)

for i in range(X):
    n = len(vector)
    vector.pop(0)
    vector.pop(n-2)

print(vector)