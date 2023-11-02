numeros_perfectos = []

for i in range(1, 10):
    suma_perfecto = 0
    for j in range (1, i//2 + 1):
        if i % j == 0:
            suma_perfecto += j
    if suma_perfecto == i:
        numeros_perfectos.append(i)

print(numeros_perfectos)

clave = input("Ingrese una clave de 3 digitos: ")
dig1 = "0"
dig2 = "0"
dig3 = "0"
prueba = dig1 + dig2 + dig3



print("La clave es: " + dig1 + dig2 + dig3)