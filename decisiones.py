user_number = int(input("Dime un numero: "))

if user_number > 5:
    print("Tu numero es mayor que 5")
else:
    print("Tu numero es menor que 5 asi que ...")

number_to_guess = 2

if number_to_guess == user_number :
    print("Has ganado")
else:
    print("Has perdido")