"""
Ejercicio 1

Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.

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
hace_cinco = datetime.timedelta(days=5)

fecha_hace_cinco = hoy - hace_cinco
dia_semana = fecha_hace_cinco.weekday()
a = dia_que_es(int(dia_semana))
print("Hace 5 dias fue {} y cayo {}".format(fecha_hace_cinco.strftime("%d-%m-%y"),a))