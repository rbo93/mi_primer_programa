#Ejercicio 2:
#Modifica el programa de la tabla de multiplicar para que sólo muestre los resultados cuando son múltiplos de 2.
# Numero elegido por el usuario: 3, output esperado:
#3 x 2 = 6
#3 x 4 = 12
#3 x 6 = 18
#3 x 8 = 24
#3 x 10 = 30

numero_tabla = int(input("Ingrese el numero del cual desea saber la tabla: "))
multiplos_de_dos = [2,4,6,8,10]

for multiplo in range(1, 11):
    if multiplo in multiplos_de_dos:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))