"""
Ejercicio 3

Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”

"""
string_usuario = str(input("Ingrese un texto, le reemplazaremos por I la vocales: "))
vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
busqueda_vocal = ""
posicion = 1

for letra in string_usuario:
    for busqueda_vocal in vocales:
        if letra == busqueda_vocal:
            string_usuario = string_usuario.replace(letra, str(posicion), 1)
            posicion += 1
print(string_usuario)