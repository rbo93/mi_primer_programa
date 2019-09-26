print("Adivina el numero del uno al 10 que estoy pensando...")
number_to_guess = 8
intentos = 1
user_number = int(input("Dime un numero: "))
if number_to_guess == user_number :
    intentos = "primer intento"
    print("En hora buena has ganado en el {}".format(intentos))
else:
    print("Has perdido")
    intentos +=1
    user_number = int(input("Dime un numero: "))
    if number_to_guess == user_number:
        print("Has ganado en {} intentos".format(intentos))
    else:
        print("Has perdido")
        intentos += 1
        user_number = int(input("Dime un numero: "))
        if number_to_guess == user_number:
            print("Has ganado en {} intentos".format(intentos))
        else:
            print("Has perdido")
            intentos += 1
            user_number = int(input("Dime un numero: "))
            if number_to_guess == user_number:
                print("Has ganado en {} intentos".format(intentos))
            else:
                print("Has perdido")
                intentos += 1
                user_number = int(input("Dime un numero: "))
                if number_to_guess == user_number:
                    intentos = "el ultimo intento"
                    print("Has ganado en {}".format(intentos))
                else:
                    print("Fallaste!! Has alcanzado el maximo de intentos que es: {}".format(intentos))