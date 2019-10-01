#Ejercicio 3:
#Crea un programa que muestre por pantalla la tabla de multiplicar de un número introducido por el usuario, pero invertida, comenzando desde el 10.
# Numero elegido por el usuario: 2, output esperado:
#2 x 10 = 20
#2 x 9 = 18
#2 x 8 = 16
#2 x 7 = 14
#2 x 6 = 12
#2 x 5 = 10
#2 x 4 = 8
#2 x 3 = 6
#2 x 2 = 4
#2 x 1 = 2

numero_tabla = int(input("Ingrese el numero del cual desea saber la tabla: "))
multiplo = 10

while multiplo != 0:
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))
    multiplo -= 1