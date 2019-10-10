import datetime
import random

# Constantes

AVERAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20

# Funciones


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")


def ask_yes_or_no(message):
    response = None
    while response != "s" and response != "n":
        response = input(message + "[s/n]:")
    return response == "S"


print_with_underscores("¡Averigua cuanto te queda de vida!")
print("Completa esta encuesta para saber cuanto tiempo te queda de vida")

birth_date = input("Cual es tu fecha de nacimiento [dd/mm/yy]")
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%y")
year_lost = 0

if ask_yes_or_no("Fumas?"):
    year_lost += SMOKER_PENALIZATION
if ask_yes_or_no("Bebes?"):
    year_lost += DRINKER_PENALIZATION
if not ask_yes_or_no("Haces deporte?"):
    year_lost += SEDENTARY_PENALIZATION

base_lifespan = random.randint(AVERAGE_LIFESPAN/2, AVERAGE_LIFESPAN)

lifespan = AVERAGE_LIFESPAN - year_lost
death_day = birth_date - datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("La fecha de tu muerte sera: {}, y te quedan {} dias.".format(death_day.strftime("%d/$m/%y"), days_to_death))