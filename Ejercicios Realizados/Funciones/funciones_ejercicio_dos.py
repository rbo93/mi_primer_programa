"""
Escribre una funcion que dado un numero y un rango (otros dos numeros),
compreube que ese numeero esta entre los dos (dentro del rango

num = 28
min = 1
max = 100
numero_en_rango(numero_a_comprobar ,minimo, maximo)

numero_en_rango(101,1,100) -> False
numero_en_rango(10,1,100) -> True
"""

# Functions

def in_range(number):
    max = 100
    min = 1
    if number <= max and number >= min:
        return True
    else:
        return False

# Program

num = int(input("Dime un numero: "))

result = in_range(num)

print(result)
if result == True:
    text = "dentro"
else:
    text = "fuera"

print("El numero se encuentra {} de rango".format(text))