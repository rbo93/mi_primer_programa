"""
Modificaciones:

1) Preguntar que si o que no tenga opcion a veces

si dice a veces la penalizacion es la mitad / listo

2) Dia de la semana que va a morir

3) Agregar mas parametros interesantes con penalidades, ej enfermedad  pero con tope de penalizacion /listo

4) cambiar valores de penalizacion por mas bajos / listo


"""

import datetime
import random

# Constantes

AVERAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 4
DRINKER_PENALIZATION = 3
SEDENTARY_PENALIZATION = 2
DIABETES_PENALIZATION = 5

# Funciones
def day_it_is(numero):
    day = ""
    if numero == 0:
        day = "lunes"
    elif numero == 1:
        day = "Martes"
    elif numero == 2:
        day = "Miercoles"
    elif numero == 3:
        day = "Jueves"
    elif numero == 4:
        day = "Viernes"
    elif numero == 5:
        day = "Sabado"
    elif numero == 6:
        day = "Domingo"
    return day


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")


def ask_yes_no_sometimes(message):
    response = None
    while response != "si" and response != "no" and response != "eventualmente":
        response = input(message + "[si/no/eventualmente]:")
    return response


print_with_underscores("¡Averigua cuanto te queda de vida!")
print("Completa esta encuesta para saber cuanto tiempo te queda de vida")

birth_date = input("Cual es tu fecha de nacimiento [dd/mm/yy]")
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%y")
year_lost = 0

question = ask_yes_no_sometimes("Fumas?")
if question == "si":
    year_lost += SMOKER_PENALIZATION
elif question == "eventualmente":
    year_lost += (SMOKER_PENALIZATION/2)

question = ask_yes_no_sometimes("Bebes?")
if question == "si:":
    year_lost += DRINKER_PENALIZATION
elif question == "eventualmente":
    year_lost += (DRINKER_PENALIZATION/2)

question = ask_yes_no_sometimes("Haces deporte?")
if question == "no":
    year_lost += SEDENTARY_PENALIZATION
elif question == "eventualmente":
    year_lost += (SEDENTARY_PENALIZATION/2)

question = ask_yes_no_sometimes("Tienes diabetes?")
if question == "si:":
    year_lost += DIABETES_PENALIZATION
elif question == "eventualmente":
    year_lost += (DIABETES_PENALIZATION/2)

base_lifespan = random.randint(AVERAGE_LIFESPAN/2, AVERAGE_LIFESPAN)
lifespan = AVERAGE_LIFESPAN - year_lost
death_day = birth_date - datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()
week_day = day_it_is(death_day.weekday())

print("La fecha de tu muerte sera:{} {}, y te quedan {} horas.".format(week_day, death_day.strftime("%d/$m/%y"), days_to_death))





