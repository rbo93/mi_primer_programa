"""
Ejercicio 1

Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.

"""

salida = False
agenda = dict()

while not salida:
    accion = input("¿Que quieres hacer? Añadir fecha[A] / Consultar numero[C]] / Salir[S]" )
    # Añadir fecha
    if accion == "A":
        print("Vamos a añadir un año de nacimiento")
        nombre = input("Nombre: ")
        year = input("Años de nacimiento: ")
        agenda[nombre] = year
    # Consultar numero
    elif accion == "C":
        print("Consultar año de nacimiento: ")
        nombre = input("De quien quieres saber el año de nacimiento:  ")
        print(agenda[nombre])

    elif accion == "S":
        salida = True