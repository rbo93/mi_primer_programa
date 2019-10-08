"""
Ejercicio 3

Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.
"""
import datetime

hoy = datetime.datetime.now()
print("Fecha actual {} {}:{}".format(hoy.strftime("%d-%m-%y"), hoy.hour, hoy.minute))
print("Dime una fecha y te dire cuantas horas han pasado de ese momento")
day = int(input("Dime el dia: "))
month = int(input("Dime el mes: "))
year = int(input("Dime el año: "))
hour = hoy.hour
user_date = datetime.datetime(year=year, month=month, day=day, hour=hour)
if year <= hoy.year:
    if month < hoy.month or day < hoy.day:
        time_calculated = datetime.datetime.now() - user_date
        print("Han pasado {} horas hasta llegar a hoy: {}".format(int(time_calculated.total_seconds() / 3600),
                                                             hoy.strftime("%d-%m-%y")))
    else:
        time_calculated = user_date - datetime.datetime.now()
        print("Recien vuelvo del futuru y te informo que faltan {} horas para que se produzca la fecha indicada.".format(
            int(time_calculated.total_seconds() / 3600)))
else:
    time_calculated = user_date - datetime.datetime.now()
    print("Recien vuelvo del futuru y te informo que faltan {} horas para que se produzca la fecha indicada.".format(int(time_calculated.total_seconds() / 3600)))


