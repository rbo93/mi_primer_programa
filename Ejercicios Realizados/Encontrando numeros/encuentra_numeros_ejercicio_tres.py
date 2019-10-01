#Ejercicio 3:
#Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario (media = suma de todos los numeros / numero de numeros )
# Números usuario
#numeros = [11, 21, 3, 42, 3, 2]
# Output
#media = 13.666666666666666

media = 0
suma_numeros= 0
cantidad_numeros = 0
a = 0
numeros_usuario = []
salida = "SI"
numero_del_usuario = " "

while salida == "SI":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero añadido!")
    salida = input("Desea añadir otro numero? SI :").upper()

print("Numeros ingresados: {}".format(numeros_usuario))

for a in numeros_usuario:
    suma_numeros += a
    cantidad_numeros += 1

media = suma_numeros/cantidad_numeros

print("Cantidad de numeros listados: {}".format(cantidad_numeros))
print("La media es: {}".format(media))