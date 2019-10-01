import os
var = os.name

intento = ""
cantidad_de_intentos = 0

print("El JUGADOR 1 debera ingresar el numero a adivinar, el JUGADOR 2 tendra intentos infinitos hasta acertar. Con la S podra terminar el juego ")

numero_adivinar = input("JUGADOR 1, ingrese el numero a adivinar: ")
os.system("cls")

while intento != "S" and intento != "G" :
    intento = input("JUGADOR 2, ingrese el numero que cree que eligio el JUGADOR 1: ")
    cantidad_de_intentos += 1
    if intento == numero_adivinar:
        print("ADIVINASTE!!!")
        print("Lo lograste en {} intentos".format(cantidad_de_intentos))
        intento = "G"

if intento == "S":
    intento = "El JUGADOR 2 ha desertado."
    print("Juego finalizado. Ha ganado el JUGADOR 1. {} El numero a advinar era:{}".format(intento, numero_adivinar))
elif intento == "G":
    print("Juego finalizado. Ha ganado el JUGADOR 2")