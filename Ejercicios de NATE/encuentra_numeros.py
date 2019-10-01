numeros_usuario = []
numero_del_usuario = " "

while len(numeros_usuario) < 10:
    while not numeros_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero añadido!")

print(numeros_usuario)

numero_grande = numeros_usuario[0]

for numero in numeros_usuario:
    if numero > numero_grande:
        numero_grande = numero

print("El numero mas grande es: {}",format(numero_grande))