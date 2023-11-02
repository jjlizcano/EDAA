from datetime import datetime
from colorama import  Style, Fore, init
from os import system

def tituloPrincipal():
    system("clear")
    init()

    print(Fore.YELLOW, "")
    print(
"""
                                              ,----,                                                                                     
                                             ,/   .`|                                                              ,----..                
    ,---,.    ,---,          ,----..       ,`   .'  :                ,-.----.       ,---,            ,---,        /   /   \   ,-.----.    
  ,'  .' |   '  .' \        /   /   \    ;    ;     /          ,--,  \    /  \     '  .' \         .'  .' `\     /   .     :  \    /  \   
,---.'   |  /  ;    '.     |   :     : .'___,/    ,'         ,'_ /|  ;   :    \   /  ;    '.     ,---.'     \   .   /   ;.  \ ;   :    \  
|   |   .' :  :       \    .   |  ;. / |    :     |     .--. |  | :  |   | .\ :  :  :       \    |   |  .`\  | .   ;   /  ` ; |   | .\ :  
:   :  :   :  |   /\   \   .   ; /--`  ;    |.';  ;   ,'_ /| :  . |  .   : |: |  :  |   /\   \   :   : |  '  | ;   |  ; \ ; | .   : |: |  
:   |  |-, |  :  ' ;.   :  ;   | ;     `----'  |  |   |  ' | |  . .  |   |  \ :  |  :  ' ;.   :  |   ' '  ;  : |   :  | ; | ' |   |  \ :  
|   :  ;/| |  |  ;/  \   \ |   : |         '   :  ;   |  | ' |  | |  |   : .  /  |  |  ;/  \   \ '   | ;  .  | .   |  ' ' ' : |   : .  /  
|   |   .' '  :  | \  \ ,' .   | '___      |   |  '   :  | | :  ' ;  ;   | |  \  '  :  | \  \ ,' |   | :  |  ' '   ;  \; /  | ;   | |  \  
'   :  '   |  |  '  '--'   '   ; : .'|     '   :  |   |  ; ' |  | '  |   | ;\  \ |  |  '  '--'   '   : | /  ;   \   \  ',  /  |   | ;\  \ 
|   |  |   |  :  :         '   | '/  :     ;   |.'    :  | : ;  ; |  :   ' | \.' |  :  :         |   | '` ,/     ;   :    /   :   ' | \.' 
|   :  \   |  | ,'         |   :    /      '---'      '  :  `--'   \ :   : :-'   |  | ,'         ;   :  .'        \   \ .'    :   : :-'   
|   | ,'   `--''            \   \ .'                  :  ,      .-./ |   |.'     `--''           |   ,.'           `---`      |   |.'     
`----'                       `---`                     `--`----'     `---'                       '---'                        `---'       
                                                                                                                                                                                      
""")
    print(Fore.YELLOW,"                                                          a)Facturar un cliente")
    print(Fore.BLUE,"                                                          b)Facturar todos los clientes")
    print(Fore.RED,"                                                          c)Salir")




año = str(datetime.now().year)
mes = str(datetime.now().month)
dia = str(datetime.now().day)
fecha = año + "/" + mes + "/" + dia

factura = {}
datosUsuarios = {}
productos = {}

informacionFactura = []

fUsuarios = open("Usuarios.txt", "r")
informacionUsuarios = fUsuarios.readlines()
fUsuarios.close()

fProductos = open("Productos.txt", "r")
informacionProductos = fProductos.readlines()
fProductos.close()

for usuario in informacionUsuarios:
    cedula = usuario.split(":")[0]
    infoCliente = usuario.split(":")[1].split(";")
    nombre = infoCliente[0]
    productosVendidos = infoCliente[1].split(",")
    cantidad = infoCliente[2].split(",")
    noFacturaCliente = infoCliente[3].split("=")
    noFacturaCliente[1] = noFacturaCliente[-1].removesuffix("\n")
    
    datosUsuarios.setdefault(cedula, [nombre, productosVendidos, cantidad, int(noFacturaCliente[1])])


#Obteniendo productos
for producto in informacionProductos:
    lineaTexto = producto.split(":")
    valoresProducto = lineaTexto[1].split(",")
    valoresProducto[-1] = valoresProducto[-1].removesuffix("\n")

    clave = lineaTexto[0]
    valor = valoresProducto

    productos.setdefault(clave, valor)

def generarEspacios(menor:str, mayor:str):
    diferenciaEspacio = len(mayor) - len(menor)
    espacios = ""
    if(diferenciaEspacio > 0):
        for i in range(diferenciaEspacio):
            espacios += " "
    return espacios

def generarSeparador(tamaño, linea = "═"):
    lineas = ""
    for i in tamaño:
        lineas += linea
    return lineas

def construirTabla(cedulaCliente)->str:
    palabraMayor = ""
    ivaMayor = ""

    subTotal = 0
    totalIva = 0
    totalVenta = 0

    for i in datosUsuarios[cedulaCliente][1]:
        if len(productos[i][0]) > len(palabraMayor):
            palabraMayor = productos[i][0]
        valorIva = str((int(productos[i][2])*int(productos[i][1]))//100)
        if(len(valorIva) > len(ivaMayor)):
            ivaMayor = str(valorIva)

    espaciosNombre = generarEspacios("Nombre", palabraMayor)
    espaciosIva = generarEspacios("iva", ivaMayor)

    tabla = "║ Código " + "║ Nombre" + espaciosNombre + " ║ Vlr Unit" + " ║ Cantidad" + " ║ %iva" + " ║ iva" + espaciosIva +" ║ Vlr Total        ║" 
    separador = generarSeparador(tabla)
    tabla = separador + "\n" + tabla + "\n" + separador

    for i in range(len(datosUsuarios[cedulaCliente][1])):

        productoVendido = datosUsuarios[cedulaCliente][1][i]
        nombreProducto = productos[productoVendido][0]
        valorProducto = productos[productoVendido][1]
        cantidad = datosUsuarios[cedulaCliente][2][i]
        porIva = productos[productoVendido][2]
        iva = str((int(valorProducto) * int(porIva))//100)
        valorTotal = str(int(valorProducto) + int(iva))

        subTotal += int(valorProducto)
        totalIva += int(iva)

        fila = "║ " + productoVendido + generarEspacios(productoVendido, "Código ") + "║ " + nombreProducto + generarEspacios(nombreProducto, "Nombre" + espaciosNombre)+ " ║ " + valorProducto + generarEspacios(valorProducto, "Vlr Unit") +" ║ " + cantidad + generarEspacios(cantidad, "Cantidad") + " ║ " + porIva + generarEspacios(porIva, "%iva") + " ║ " + iva + generarEspacios(iva, "iva"+ espaciosIva) + " ║ " + valorTotal + generarEspacios(valorTotal, "Vlr Total        ") + "║"
        tabla += "\n" + fila + "\n" + separador
    totalVenta = subTotal + totalIva
    tabla += "\n                            Subtotal: " + str(subTotal) + "\n                            Total Iva: " + str(totalIva) + "\n                            Total Venta: " + str(totalVenta) + "\n"
    return tabla

#Generar factura para un cliente en especifico
def generarFactura(cedulaCliente:str):
    datosUsuarios[cedulaCliente][3] += 1
    noFactura = datosUsuarios[cedulaCliente][3]
    fFactura = open("factura/Factura "+ datosUsuarios[cedulaCliente][0] +"No"+ str(noFactura) +".txt","w")
    fFactura.write("                    DATOS Y PROCESOS CORPORATIVOS LTDA\n\n")
    fFactura.write("         Factura de venta No : " + str(noFactura)   + "             Fecha: " + fecha + "\n\n")
    fFactura.write("                     Nit: 890900200-1  Régimen Común" + "\n\n")
    fFactura.write("                 Cliente: " + cedulaCliente + " - " + datosUsuarios[cedulaCliente][0] + "\n")
    fFactura.write(construirTabla(cedulaCliente))
    fFactura.close()

    fFactura = open("factura/Factura "+ datosUsuarios[cedulaCliente][0] +"No"+ str(noFactura) +".txt","r")
    informacionFactura = fFactura.readlines()
    fFactura.close()
    for i in informacionFactura:
        print(i, end="")

    print("")
    fUsuarios = open("Usuarios.txt", "w")
    for i in datosUsuarios.keys():
        textoProductos = ""
        textoCantidad = ""
        for j in range(len(datosUsuarios[i][1])):
            if j < len(datosUsuarios[i][1])-1:
                textoProductos += datosUsuarios[i][1][j] + ","
                textoCantidad += datosUsuarios[i][2][j] + ","
            else:
                textoProductos += datosUsuarios[i][1][j]
                textoCantidad += datosUsuarios[i][2][j]

        fUsuarios.write(i+":"+datosUsuarios[i][0]+";"+textoProductos+";"+textoCantidad+";Factura="+str(datosUsuarios[i][3])+"\n")
    fUsuarios.close()


tituloPrincipal()
opciones = ["a", "b", "c"]
print(Fore.GREEN, "")
opcion = input("Ingrese una opción: ")
while(opcion not in opciones):
    print("Opción invalida")
    opcion = input("Ingrese una opción: ")
system("clear")

while(opcion != "c"):
    if(opcion == "a"):
        system("clear")
        print(Fore.GREEN, "Lista de clientes:")
        
        for i in datosUsuarios.keys():
            print(Fore.BLUE,i + " - " + datosUsuarios[i][0])
        
        print(Fore.GREEN, "")
        cedula = input("Ingrese la cedula del cliente: ")
        
        while(cedula not in datosUsuarios.keys()):
            system("clear")
            for i in datosUsuarios.keys():
                print(Fore.BLUE,i + " - " + datosUsuarios[i][0])
            
            print(Fore.RED, "")
            print("Cedula no encontrada")
            print(Fore.GREEN, "")
            cedula = input("Ingrese la cedula del cliente: ")
        
        system("clear")
        generarFactura(cedula)
        print(Fore.RED, "")
        print("Factura generada con éxito")
        opcion = input("Presione enter para continuar")
    
    elif(opcion == "b"):
        system("clear")
        for i in datosUsuarios.keys():
            generarFactura(i)
            print("\n\n")
        print("Facturas generadas con éxito")
    elif(opcion == "c"):
        break
    
    system("clear")
    tituloPrincipal()
    print(Fore.GREEN, "")
    opcion = input("Ingrese una opción: ")
    
    while(opcion not in opciones):
        print("Opción invalida")
        opcion = input("Ingrese una opción: ")
    