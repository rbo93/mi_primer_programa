#Ejercicio 1
# Dada una lista de strings, devolver una lista con el largo de cada string.


lista_string = ["asdsa", "hola", "an", "a", "ghlijfglhflkhjfgl"]
lista_largo_string = []

for dato in lista_string:
    lista_largo_string.append(len(dato))

print(lista_largo_string)
