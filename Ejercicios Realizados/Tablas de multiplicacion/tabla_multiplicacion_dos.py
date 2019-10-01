#Ejercicio 1
#Modifica el programa de la tabla de multiplicar para que vaya del 5 al 15 en lugar del 1 al 10.
# Numero elegido por el usuario: 2, output esperado:
#2 x 5 = 10
#2 x 6 = 12
#2 x 7 = 14
#2 x 8 = 16
#2 x 9 = 18
#2 x 10 = 20
#2 x 11 = 22
#2 x 12 = 24
#2 x 13 = 26
#2 x 14 = 28
#2 x 15 = 30

numero_tabla = int(input("Ingrese el numero del cual desea saber la tabla: "))

for multiplo in range(5,16):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))