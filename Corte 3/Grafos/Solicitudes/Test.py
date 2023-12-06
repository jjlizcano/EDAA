from dijsktra import *

archivo_cargado = False
solicitudes = []
tiempo_total = 0
usuarios = 0

def mostrar_menu():
    print("""
    Opciones:
    1. Agregar archivo
    2. Calcular total de dias requeridos para todos los documentos
    3. Estadística de las oficinas
    4. Estadística por número de solicitudes de usuario
    5. Salir
    """)

def cargar_archivo():
        a_info_solicitud = open("solicitudes.txt", "r")
        info_solicitud = a_info_solicitud.readlines()
        a_info_solicitud.close()

        for linea in info_solicitud:
            info_linea = linea.split(",")
            info_linea[2] = info_linea[2].replace("\n", "")
            solicitudes.append(info_linea)

def calcular_tiempo(destino):
    tiempo, prev = dijkstra(g, "A", destino)
    return tiempo

edges = [
        ("A", "B", 3),
        ("A", "C", 1),
        ("B", "D", 1),
        ("B", "G", 5),
        ("C", "D", 2),
        ("C", "F", 5),
        ("D", "F", 2),
        ("D", "E", 4),
        ("E", "H", 1),
        ("E", "G", 2),
        ("F", "H", 1)
        ]

g = build_graph(edges)

while True:
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        cargar_archivo()
        archivo_cargado = True
        print("\nArchivo cargado con éxito")

    elif not archivo_cargado:
        print("\nNo se ha cargado ningún archivo")

    elif opcion == 2:
        print()
        usuarios = []

        for usuario in solicitudes:
            if usuario[1] not in usuarios:
                a_ticket = open("A" + usuario[1] + ".txt", "a")
                a_ticket.write("Usuario: " + usuario[2])

                for solicitud in solicitudes:
                    tiempo_solicitud = 0

                    if solicitud[1] == usuario[1]:
                        a_ticket.write("\n\nDestino del documento: " + solicitud[0])

                        tiempo_solicitud += calcular_tiempo(solicitud[0])
                        a_ticket.write("\nTiempo de envio: " + str(tiempo_solicitud) + " dia(s)")
                
                a_ticket.close()
                usuarios.append(usuario[1])

            tiempo_total += calcular_tiempo(usuario[0])
        print("\nDias totales requeridos:", tiempo_total)

    elif opcion == 3:
        print()
        oficinas_destino = ["B","C","D","E","F","G","H"]

        for oficina in oficinas_destino:
            solicitudes_oficina = 0

            for solicitud in solicitudes:
                if solicitud[0] == oficina:
                    solicitudes_oficina += 1

            print("La oficina", oficina, "recibirá", solicitudes_oficina, "solicitudes")
    
    elif opcion == 4:
        print()
        usuarios = []

        for usuario in solicitudes:
            num_solicitudes = 0

            if usuario[1] not in usuarios:
                for solicitud in solicitudes:
                    if solicitud[1] == usuario[1]:
                        num_solicitudes += 1
                
                usuarios.append(usuario[1])
        
                print("El usuario", usuario[1], "ha realizado", num_solicitudes, "solicitudes")

    elif opcion == 5:
        break

    else:
        print("\nOpción inexistente")
