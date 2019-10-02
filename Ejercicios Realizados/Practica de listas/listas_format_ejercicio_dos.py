"""
Ejercicio 2

Crear un programa que le repita al usuario todo lo que dice pero con todas las vocales cambiadas por i.

"""

string_usuario = str(input("Ingrese un texto, le reemplazaremos por I la vocales: "))
vocales = ["a", "A", "e", "E", "I", "o", "O", "u", "U"]
busqueda_vocal = ""
output_string = ""

for letra in string_usuario:
    for busqueda_vocal in vocales:
        if letra == busqueda_vocal:
            string_usuario = string_usuario.replace(letra, "i")

print(string_usuario)