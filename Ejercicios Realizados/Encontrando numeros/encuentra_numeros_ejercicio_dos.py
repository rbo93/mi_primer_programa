# Ejercicio 2:
#Crea un programa que cuente los elementos de la lista de números introducida por el usuario. Está prohibido utilizar la función len() para resolver el problema.
# Números usuario
#numeros = [11, 21, 3, 42, 3, 2]
# Output
#largo_lista = 6

numeros_usuario = []
numero_del_usuario = " "
salida = "SI"

while salida == "SI":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero añadido!")
    salida = input("Desea añadir otro numero? SI :").upper()
print(numeros_usuario)
b = 0
for a in numeros_usuario:
    b += 1

print("La cantidad de numero de numeros ingresados es: {}".format(b))