"""
Ejercicio 4
Modificar el programa del video. Puedes encontrar el código aquí:
https://github.com/nateacademy/prueba/blob/master/time.py

Antes de comenzar el while principal, preguntar al usuario si desea configurar una alarma, esta alarma sonara una vez al
día a la hora que el usuario decida (no hace falta tener los minutos en cuenta). También el usuario podrá decidir que
días de la semana quiere que esta alarma suene o si quiere que suene una fecha en concreto. Cuando llegue el momento
especificado en la alarma, simplemente escribir una nueva linea de texto en el archivo y en pantalla. Esto representaría
que la alarma ha sonado.

"""

from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def when_to_ring(specific_or_not):
    if not specific_or_not:
        ask = ask_yes_or_no("Quieres que suene un dia o varios de la semana?")
        if ask:
            print("Formato de dias. Ingresar solo la letra del dia L o para mas de una dia L,M,m,J,V,S,D")
            alarm_days = input("Que dias deseas que suene?: ")
            schedule_time = input("A que hora?: ")
            all_info = day_is_it(alarm_days, schedule_time)
            print("La alarma seteadas para los dias: {} a las {} hs".format(alarm_days, schedule_time))
        else:
            only_time = input("En que horario debe sonar?: ")
            print("Se seteo la alarma para la hora: {}".format(only_time))
            all_info = only_time
    else:
        day = int(input("Que dia debe sonar?:  "))
        month = int(input("De que mes?: "))
        year = int(input("De que año?: "))
        hour = int(input("A que hora?: "))
        all_info = datetime.datetime(year=year, month=month, day=day, hour=hour)
        print("alarma seteada para el dia: {} hs".format(all_info))
    return all_info


def ask_yes_or_no(message):
    response = None
    while response != "s" and response != "n":
        response = input(message + "[s/n]:")
    return response == "s"


def day_is_it(days, time):
    days_given = [[False], [False], [False], [False], [False], [False], [False], [False]]
    list_days = ["L", "M", "m", "J", "V", "S", "D"]
    coma = ","
    days_given[0] = False
    days_given[1] = False
    days_given[2] = False
    days_given[3] = False
    days_given[4] = False
    days_given[5] = False
    days_given[6] = False
    days_given[7] = time
    for letra in days:
        if letra != coma:
            if letra in list_days:
                if letra == "L":
                    days_given[0] = True
                elif letra == "M":
                    days_given[1] = True
                elif letra == "m":
                    days_given[2] = True
                elif letra == "J":
                    days_given[3] = True
                elif letra == "V":
                    days_given[4] = True
                elif letra == "S":
                    days_given[5] = True
                elif letra == "D":
                    days_given[6] = True
    print("days given {}".format(days_given))
    return days_given


def main():
    current_time = datetime.datetime.now()
    is_night = False
    alarm = 0
    alarm_configured = []
    alarm_yes_no = ask_yes_or_no("Desea configurar una alarma? ")
    if alarm_yes_no:
        alarm = True
        specific_day_yes_no = ask_yes_or_no("Quieres programar la alarma en una fecha en particular?")
        alarm_configured = when_to_ring(specific_day_yes_no)
        print(alarm_configured)
    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False
        current_time_without_minutes = datetime.datetime(year=current_time.year, month=current_time.month, day= current_time.day, hour=current_time.hour)
        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")
        if alarm:
            if type(alarm_configured) == datetime.datetime:
                if current_time_without_minutes == alarm_configured:
                    print("ALARMA DE FECHA PROGRAMADA SONANDO!!!")
            elif type(alarm_configured) == str:
                if str(current_time.hour) == alarm_configured:
                    print("ALARMA DE HORA SONANDO!!")
            elif type(alarm_configured) == list:
                index = 0
                while index <= 6:
                    if alarm_configured[index]:  # Corregir el indice, se va de rango, con el while pareciera no servir
                        if current_time.weekday() == index and str(current_time.hour) == alarm_configured[7]:
                            print("ALARMA DE DIA Y HORA SONANDO!!")
                    index += 1
        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()
