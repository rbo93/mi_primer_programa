"""
Dada la lista de enteros:

Vamos a sustituir los multiplos de 3 por un Fizz
Y los multiplos de 5 por un Buzz

En el caso de q sean multiplos de 3 y 5 reemplazaremos por FizzBuzz
"""
numeros = [1, 2, 3, 4, 5, 6, 7 , 8 ,9 , 10, 11, 12, 14, 20, 15, 30, 60, 70]

#Metodo 1

for indice in range(len(numeros)):
    numero = numeros[indice]
    valor = ""

    if numero % 3 == 0 :
        valor += "Fizz"

    if numero % 5 == 0:
        valor += "Buzz"

    if valor != "":
       numeros[indice] = valor

print(numeros)


# Metodo 2

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

        if numero % 3 == 0:
            numeros[indice] += "Fizz"

        if numero % 5 == 0:
            numeros[indice] += "Buzz"

print(numeros)


# Metodo 3

for indice in range(len(numeros)):
    if numeros[indice] % 3 == 0 or numeros[indice] % 5 == 0:
        valor_a_sustituir = ""

        if numeros[indice] % 3 == 0:
            valor_a_sustituir += "Fizz"

        if numeros[indice] % 5 == 0:
            valor_a_sustituir += "Buzz"

        numeros[indice] = valor_a_sustituir
print(numeros)



