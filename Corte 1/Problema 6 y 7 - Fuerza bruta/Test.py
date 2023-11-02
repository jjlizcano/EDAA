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

intentos = 0


for i in range(0, 10):
    dig1 = str(i)
    for j in range(0, 10):
        dig2 = str(j)
        for k in range(0, 10):
            dig3 = str(k)
            intentos += 1
            if clave == dig1 + dig2 + dig3:
                break
        if clave == dig1 + dig2 + dig3:
            break
    if clave == dig1 + dig2 + dig3:
        break           

print("La clave es: " + dig1 + dig2 + dig3, "Intentos: " + str(intentos))