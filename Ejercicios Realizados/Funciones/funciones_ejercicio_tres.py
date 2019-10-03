"""
Escribe una funcion que reciba una lista de numeros y te devuelva otra pero solo con los pares

devolver_pares([1,2,3,4,5,6])
Output [2, 4, 6]


"""

# Functions

def devolver_pares(lista):
    new_list = []
    for index in range(len(lista)):
        if lista[index] % 2 == 0:
            new_list.append(lista[index])
    return new_list

# Global variables, list definitions

lista_numeros = [1, 2, 3, 4, 5, 6]
lista_pares = []

# Program

lista_pares = devolver_pares(lista_numeros)

print("Estos son los numeros pares: {}".format(lista_pares))