#Ejercicio 3
# Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.

lista_inicial = [2, "a", 3, 5, "basdsa", 85, "hola", 4.2, 5.2]
lista_enteros = []
lista_strings = []

for dato in lista_inicial:
    if type(dato) == type(str(dato)):
        lista_strings.append(dato)
    elif type(dato) == type(int(dato)):
        lista_enteros.append(dato)

print("Lista strings: {}".format(lista_strings))
print("Lista enteros: {}".format(lista_enteros))