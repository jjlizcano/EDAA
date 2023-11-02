Nombres = ["Pedro", "Juan", "Diana", "Lucas", "Ana", "Diego"]
Edades = [55,70,50,49,71,35]

for i in Edades:
    if i > 60:
        print(Nombres[Edades.index(i)])
        Nombres.pop(Edades.index(i))
        Edades.pop(Edades.index(i))

for i in Nombres:
    print(i)