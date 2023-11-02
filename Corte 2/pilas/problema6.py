import random

def asignar_categoria(i):
    if mesa[i] == 1:
        mesa[i] = "A"
    elif mesa[i] == 2:
        mesa[i] = "B"
    else:
        mesa[i] = "C"

def hay_variedad():
    return "A" in mesa and "B" in mesa and "C" in mesa

def generar_libros():
    for i in range(n):
        mesa.append(random.randint(1, 3))
        asignar_categoria(i)



mesa = []
biblioteca = []

n = int(input("Ingrese un numero: "))

while not isinstance(n, int): # Validación de entrada
    n = int(input("Ingrese un número entero: "))

generar_libros()

while n < 2:
    n = int(input("Ingrese un número mayor a 1: "))
    generar_libros()

while hay_variedad() == False: # Tiene que haber al menos un libro de cada categoría
    generar_libros()


# El primer libro "C" que encuentre será el último en la biblioteca
for i in range(len(mesa)):
    if mesa[i-1] == "C":
        biblioteca.append(mesa[i-1])
        mesa.pop(i-1)
        break

# El último libro en el mesa será un "A"
for i in range(len(mesa)):
    if mesa[i-1] == "A":
        mesa[i-1], mesa[len(mesa)-1] = mesa[len(mesa)-1], mesa[i-1]
        break

# Finalmente, se agregan los libros restantes a la biblioteca
for i in range(len(mesa)):
    biblioteca.append(mesa[0])
    mesa.pop(0)

print("Biblioteca:", biblioteca)