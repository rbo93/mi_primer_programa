#Ejercicio 1
#Crea un programa que encuentre el número más pequeño de una serie de números introducidos por el usuario.
# Números usuario
#numeros = [1, 2, 3, 4, 5, 6]
# Output
#mas_pequeno = 1

numeros_usuario = []
numero_del_usuario = " "

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero añadido!")

print(numeros_usuario)

numero_chico = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_chico:
        numero_chico = numero

print("El numero mas chico es: {}".format(numero_chico))