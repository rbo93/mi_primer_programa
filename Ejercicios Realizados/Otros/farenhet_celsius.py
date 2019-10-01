temperatura_farenheit = int(input("Ingrese la temperatura en grados Farenheit, y te la devolvere en Celsius: "))

celsius = str((temperatura_farenheit-32) / 1.8)
tipo = type(celsius)

print("{} °C , el tipo de variable indicada es: {}".format(celsius, tipo))

