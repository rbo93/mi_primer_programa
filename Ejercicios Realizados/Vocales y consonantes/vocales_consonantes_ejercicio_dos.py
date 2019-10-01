#Ejercicio 2:
#Crea un programa que sea capaz de contar la cantidad de letras mayúsculas en una string introducida por el usuario.
 # Ejemplo:
#texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"
# Output esperado
#mayusculas = 3

# El metodo mas facil seria ingresar en un string todas las letras del abecedario en MAYUSCULAS y comparar

# Metodo mas acertado que he conseguido, leyendo mas documentacion

texto_usuario = str(input("Ingrese un texto: "))
n_mayusculas = 0

for letra in texto_usuario:
    if letra.isupper() == True:
        n_mayusculas += 1

print(("Mayusculas: {}").format(n_mayusculas))