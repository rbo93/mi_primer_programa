
"""
Ejercicio 2

Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés

"""

colores = {"Azul":"BLue",
           "Amarillo":"Yellow",
           "Blanco":"White",
           "Negro":"Black",
           "Rojo":"Red",
           "Verde":"Gren",
           "Violeta":"Purple"}



salida = False

while not salida:
    accion = input("¿Desas consultar la traduccion de un color? SI[S] / NO[N]")

    # Consultar numero
    if accion == "S":
        color = input("Consultar traduccion del color: ")
        print(colores[color])

    elif accion == "N":
        salida = True