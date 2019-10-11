"""
Ejercicio 3
Crea un programa que pregunte al usuario que adivine un numero del 1 al 10, pero ese numero se va a generar aleatoriamente. Hacer esperar al usuario 3 segundos antes de dar la respuesta.

"""
import random
from time import sleep


def generate_number():
    number = random.randint(1, 10)
    print(number)
    return number


def ask_number(message):
    response = 0
    while response == 0:
        response = input(message)
    return response


def is_or_not(number, number_two):
    response = False
    sleep(3)
    if number == int(number_two):
        print("Has adivinado!!!")
        response = True
    return response


def main():
    print("Estoy pensando un numero")
    number_generated = generate_number()
    attemp = input("Dime un numero: ")
    a = is_or_not(number_generated, attemp)
    while a != True:
        attemp = ask_number("Has fallado!! Otro intento: ")
        a = is_or_not(number_generated, attemp)


if __name__ == '__main__':
    main()
