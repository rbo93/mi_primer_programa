"""
Ejercicio 2
Escribe un programa que imprima por pantalla una frase aleatoria cada segundo. La lista de frases de la que se seleccionará la frase aleatoria será distinta según el segundo en el que estemos:
– Segundos acabados en ‘0’: frases alegres
– Segundos acabados en ‘1’: nombres de muebles (silla, mesa)
– Segundos acabados en ‘2’: nombres de bebidas
– Segundos acabados en ‘3’: frases de odio
– Segundos acabados en ‘4’: nombres de comidas
– Segundos acabados en ‘5’: frases absurdas
– Segundos acabados en ‘6’: nombres de animales
– Segundos acabados en ‘7’: frases motivacionales
– Segundos acabados en ‘8’: sonidos de animales
– Segundos acabados en ‘9’: frases tristes

"""
import random
import datetime


# Funciones
def show_random_text(lists):
    number = random.randint(0, len(lists)-1)
    print(lists[number])


def time_decision():
    today = datetime.datetime.now()
    a = int(today.second)
    if a >= 60:
        a -= 60
    elif a >= 50:
        a -= 50
    elif a >= 40:
        a -= 40
    elif a >= 30:
        a -= 30
    elif a >= 20:
        a -= 20
    elif a >= 10:
        a -= 10
    return a


def main():
    # Listas

    second_zero_text = [["25 grados, sol , pileta y fulbito"], ["Estoy de vacaciones"]]
    second_one_text = [["Silla"], ["Mesa"]]
    second_two_text = [["Tequila"], ["Cerveza"]]
    second_three_text = [["Te odio"], ["Moriteeeee"]]
    second_four_text = [["Sorrentinos"], ["Hamburguesas"]]
    second_five_text = [["saco pa tu ma"], ["Inserte un ojo en la picadora de carne"]]
    second_six_text = [["Perro"], ["Gato"]]
    second_seven_text = [["No pain, no gain"], ["Tu puedes!!"]]
    second_eight_text = [["qui quiri qui"], ["cuak"]]
    second_nine_text = [["Ella me dejo"], ["Se murio tu perro"]]
    second = time_decision()

    if second == 0:
        show_random_text(second_zero_text)
    elif second == 1:
        show_random_text(second_one_text)
    elif second == 2:
        show_random_text(second_two_text)
    elif second == 3:
        show_random_text(second_three_text)
    elif second == 4:
        show_random_text(second_four_text)
    elif second == 5:
        show_random_text(second_five_text)
    elif second == 6:
        show_random_text(second_six_text)
    elif second == 7:
        show_random_text(second_seven_text)
    elif second == 8:
        show_random_text(second_eight_text)
    elif second == 9:
        show_random_text(second_nine_text)


if __name__ == '__main__':
    main()