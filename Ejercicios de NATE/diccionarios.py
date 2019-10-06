"""
Guia telefonica

¿Que quieres hacer? [Añadir numero [A] / Consultar numero[C]]:

Vamos a añadir un numero de telefono:
-------------------------------------
Nombre: Nate
Numero: 666666666888

Consultar numero:
--------------------------------------
De quien quieres saber el numero: Nate
666666666888


"""

salida = False
agenda = dict()
while not salida:
    accion = input("¿Que quieres hacer? [Añadir numero [A] / Consultar numero[C]] / Salir[S] ")
    # Añadir numero
    if accion == "A":
        print("Vamos a añadir un numero de telefono")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda[nombre] = numero
    # Consultar numero
    elif accion == "C":
        print("Consultar numero: ")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])
    elif accion == "S":
        salida = True