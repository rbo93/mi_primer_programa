"""
Ejercicio 1

Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”.
"""

# Metodo 4

numeros = [1, 2, 3, 4, 5, 6, 7 , 8 ,9 , 10, 11, 12, 14, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):
    if numeros[indice] % 3 == 0 and numeros[indice] % 5== 0:
        numeros[indice] = "Bazinga"
    elif numeros[indice] % 3 == 0:
        numeros[indice] = "Fizz"
    elif numeros[indice] % 5 == 0:
        numeros[indice] = "Buzz"

print(numeros)