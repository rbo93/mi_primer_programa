"""
Ejercicio 3

Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

Ejemplo:

input = [1, 10, 70, 30, 50, 55]

multiplos_dos = [10, 70, 30, 50]
multiplos_tres = [30]
multiplos_cinco = [10, 70, 30, 50, 55]
multiplos_siete = [70]


"""

# Listas

numeros_usuario = []
lista_multiplos_dos = []
lista_multiplos_tres = []
lista_multiplos_cinco = []
lista_multiplos_siete = []

#Variables

input_usuario = ""
posicion = -1

#Programa

while input_usuario != 0:
    input_usuario = int(input("Dime el numero a agregar (0 para salir): "))
    numeros_usuario.append(input_usuario)
    posicion += 1

numeros_usuario[posicion] = 1

for indice in range(len(numeros_usuario)):
    numero = numeros_usuario[indice]

    if numero % 2 == 0:
        lista_multiplos_dos.append(numeros_usuario[indice])
    if numero % 3 == 0:
        lista_multiplos_tres.append(numeros_usuario[indice])
    if numero % 5 == 0:
        lista_multiplos_cinco.append(numeros_usuario[indice])
    if numero % 7 == 0:
        lista_multiplos_siete.append(numeros_usuario[indice])

print("Multiplos de 2: {}".format(lista_multiplos_dos))
print("Multiplos de 3: {}".format(lista_multiplos_tres))
print("Multiplos de 5: {}".format(lista_multiplos_cinco))
print("Multiplos de 7: {}".format(lista_multiplos_siete))
