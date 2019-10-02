"""
Ejercicio 2

Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).

"""


lista_numeros = [110, 2, 5, 80, 220, 50 ]

print(lista_numeros)

numero_grande = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_grande:
        numero_grande = numero

print("El numero mas grande es: {}".format(numero_grande))