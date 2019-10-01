numero_tabla = int(input("Ingrese el numero del cual desea saber la tabla: "))

for multiplo in range(1,11):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))