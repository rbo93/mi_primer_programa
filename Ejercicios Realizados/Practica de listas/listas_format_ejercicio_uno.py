"""
Ejercicio 1

Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.

"""

string_usuario = input(str("Ingrese un texto: "))
string_usuario = string_usuario.replace("A", "VACA")
string_usuario = string_usuario.replace("a", "VACA")
print(string_usuario)
