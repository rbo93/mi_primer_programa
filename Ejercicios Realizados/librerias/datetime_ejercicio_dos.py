"""
Ejercicio 2
Crea un programa que te diga cuando falta para tu cumpleaños y que día de la semana será.
"""
# Librerias
import datetime

# Funciones
def dia_que_es(numero):
    dia = ""
    if numero == 0:
        dia = "lunes"
    elif numero == 1:
        dia = "Martes"
    elif numero == 2:
        dia = "Miercoles"
    elif numero == 3:
        dia = "Jueves"
    elif numero == 4:
        dia = "Viernes"
    elif numero == 5:
        dia = "Sabado"
    elif numero == 6:
        dia = "Domingo"
    return dia

hoy = datetime.datetime.now()
print("Fecha actual {}".format(hoy.strftime("%d-%m-%y")))
print("Te calculare cuanto falta para tu cumple...")
day = int(input("Dime el dia de de tu cumpleaños: "))
month = int(input("Dime el numero de mes de tu cumpleaños: "))

if hoy.month <= month and hoy.day <= day:
    year = hoy.year
else:
    year = hoy.year + 1

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now() + datetime.timedelta(days=1)
dia_semana = dia_que_es(user_date.weekday())

if year == hoy.year:
    print("Faltan {} dias y sera {}".format(time_remaining.days, dia_semana))
else:
    print("Faltan 1 año, {} dias y sera {}".format(time_remaining.days, dia_semana))
