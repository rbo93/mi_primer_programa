"""
Escribre un programa que encuentre el numero mas grande entre 3 numeros


"""
# Functions

def solicite_numbers(ask):
    user_numbers = []
    number = input(ask)
    while len(user_numbers) < 3:
        while not number.isdigit():
            number = input(ask)
        user_numbers.append(int(number))
        number = ""
        print("Numero añadido!")
    return user_numbers

def max_of_three_numbers(list):

    max = list[0]
    for numero in list:
        if numero > max:
            max = numero
    return max


# Program

number_list = solicite_numbers("Dime un numero:  ")
result = max_of_three_numbers(number_list)
print("El numero mas grande entre {} es: {}".format(number_list, result))

