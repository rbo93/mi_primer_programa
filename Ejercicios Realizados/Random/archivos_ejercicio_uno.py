"""
Ejercicio 1
Escribe una frase aleatoria de una lista de strings cada 3 segundos.

"""
import random


# Funciones
def random_index(variable,lista):
    if variable:
        index = random.randint(0, len(text_list) - 1)
        print("Tu frase es: " + text_list[index])
    else:
        print("Que lastima. Nos vemos la proxima. Igual me has tenido que leer jeje")
    return


def ask_yes_or_no(message):
    response = None
    while response != "s" and response != "n":
        response = input(message + "[s/n]:")
    return response == "s"


def main():
    print("Te mostrare una frase aleatoria de mi lista de frases..")
    a = True
    while a:
        a = ask_yes_or_no("Quieres una frase?")
        random_index(a, text_list)


if __name__ == '__main__':
    text_list = ["Hola mundo!", "En memoria del mas...", "Perdedor", "Aca hay algo raro", "Otra frase mas para esta lista", "Ya no se me ocurre mas", "O.. si ?"]
    main()