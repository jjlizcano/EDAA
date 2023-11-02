frase = str(input("Ingrese una frase: "))

lista_palabras = frase.split()

num_palabras = len(lista_palabras)

for i in range(num_palabras):
    if i % 2 == 0:
        print("X", end=" ")
    else:
        print(lista_palabras[i], end=" ")