numero_inicial = 10

while numero_inicial > 0:
    print(numero_inicial)
    numero_inicial -= 1

numero_inicial = 10

while numero_inicial > 0:
    if numero_inicial % 2 == 0:
        print("Este numero es par: {}".format(numero_inicial))
    else:
        print("Este numero es impar: {}".format(numero_inicial))
    numero_inicial -= 1