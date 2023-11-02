m200 = int(input("Cantidad de monedas de 200 disponibles: "))
m100 = int(input("Cantidad de monedas de 100 disponibles: "))
m50 = int(input("Cantidad de monedas de 50 disponibles: "))

vueltos = int(input("Ingrese valor a devolver: "))
v200 = 0
v100 = 0
v50 = 0

if vueltos//200 <= m200:
    v200 = vueltos//200
else:
    v200 = m200

if (vueltos - v200*200)//100 <= m100:
    v100 = m100
else:
    v100 = vueltos%200//100

if (vueltos - v200*200 - v100*100)//50 <= m50:
    v50 = (vueltos - v200*200 - v100*100)//50
else:
    v50 = m50

if v200*200 + v100*100 + v50*50 == vueltos:
    print("Se deben dar:", v200, "monedas de $200,", v100, "monedas de $100 y", v50, "monedas de $50")
else:
    print("No se pueden dar vueltos")