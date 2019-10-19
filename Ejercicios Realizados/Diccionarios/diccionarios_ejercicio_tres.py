
def busca_palabras(palabras, diccionario):
    if "Hola" == palabras:
        diccionario["Hola"] += 1
    elif "como" == palabras:
        diccionario["como"] += 1
    elif "estas" == palabras:
        diccionario["estas"] += 1
    elif "amigo" == palabras:
        diccionario["amigo"] += 1
    return


string = "Hola Hola como estas amigo amigo amigo"
apariciones_palabras = {"Hola": 0, "como": 0, "estas": 0, "amigo": 0}
lista_de_palabras = []
palabra = ""
i = 0
# podria haber una lista de las keys de apariciones_palabras y en la funcion recorrer la lista y pregutnar
for index in string:
    if index != " ":
        palabra += index
    else:
        lista_de_palabras.append(palabra)
        palabra = ""
f = len(lista_de_palabras)
while i <= f - 1:
    busca_palabras(lista_de_palabras[i], apariciones_palabras)
    i += 1

print(lista_de_palabras)
print(apariciones_palabras)
