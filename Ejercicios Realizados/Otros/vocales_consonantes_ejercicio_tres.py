#Ejercicio 3:
#Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario.
# Ejemplo:
#texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"
# Output esperado
#vocales = ['o', 'a', 'e', 'a', 'o', 'a', 'e', 'u', 'o', 'o', 'e', 'a', 'a']

texto_usuario = str(input(("Ingrese un texto: ").lower()))
vocales = ["a", "e", "i", "o", "u"]
lista_vocales = []

for letra in texto_usuario:
    if letra in vocales:
        lista_vocales.append(letra)

print("Vocales en la frase, en el orden que aparecen = {}".format(lista_vocales))