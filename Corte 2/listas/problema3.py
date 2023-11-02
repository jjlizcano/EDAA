codigos = [1,2,3,4,5]
nombres = ["agua","gaseosa","saviloe","Mr Tea","Red Bull"]
precios = [1000,2000,1500, 2500, 4000]

def menu():
    print("Menú princpipal")
    print("-----------------------")
    print("Código | Nombre | Precio")
    for i in codigos:
        print(i, " | ", nombres[codigos.index(i)], " | ", precios[codigos.index(i)])

menu()
can_pro = int(input("Cantidad de productos a facturar: "))

while can_pro <= 0:
    print("La cantidad de productos debe ser mayor a 0")
    can_pro = int(input("Cantidad de productos a facturar: "))

while can_pro > 5:
    print("La cantidad de productos debe ser menor a 5")
    can_pro = int(input("Cantidad de productos a facturar: "))

total = 0

for i in range(can_pro):
    cod_pro = int(input("Código del producto: "))
    while cod_pro not in codigos:
        print("El código no existe")
        cod_pro = int(input("Código del producto: "))
    can_com = int(input("Cantidad del producto a comprar: "))
    while can_com <= 0:
        print("La cantidad debe ser mayor a 0")
        can_com = int(input("Cantidad del producto a comprar: "))
    total += precios[codigos.index(cod_pro)] * can_com

print("El total a pagar es: ", total)

    