import datetime

year = int(input("Dime el año: "))
month = int(input("Dime el mes: "))
day = int(input("Dime el dia: "))


user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("Faltan {} dias y {} horas.".format(time_remaining.days, int(time_remaining.seconds/3600)))

print("Mañana es: {}".format(datetime.datetime.now() + datetime.timedelta(days=1)))

manana = datetime.datetime.now() + datetime.timedelta(days=1)
manana_medianoche = datetime.datetime(year=manana.year, month=manana.month, day=manana.day)
hoy = datetime.datetime.now()
faltante_para_manana = manana_medianoche - hoy

print("Mañana es: {}".format(manana))
print("Faltan {} horas para mañana".format(int(faltante_para_manana.total_seconds()/3600)))

# 30 del 1 de 2019
print("Mañana es {}".format(manana.strftime("%d del %m de %y")))
