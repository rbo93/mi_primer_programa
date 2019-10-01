#Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario.
# Ejemplo:
# texto_usuario = "Hola, me llamo Nate.¿Tu como te llamas?"
# Output esperado
# espacios = 67
# puntos = 1
# comas = 1

frase_usuario = str(input("Ingrese una frase: "))

punto = "."
coma = ","
espacio = " "
n_puntos = 0
n_comas = 0
n_espacios= 0

for letra in frase_usuario:
    if letra == punto:
        n_puntos += 1
    elif letra == coma:
        n_comas += 1
    elif letra == espacio:
        n_espacios += 1

print("Espacios: {}.".format(n_espacios))
print("Puntos: {}.".format(n_puntos))
print("Comas: {}.".format(n_comas))