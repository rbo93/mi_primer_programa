def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, ¿Estas seguro? SI/NO: ".format(dato_usuario))
        if seguro.lower() == "si":
            confirmacion = True
    return dato_usuario

nombre = input_con_confirmacion("Como te llamas?: ")
print("Has confirmado que te llamas: ".format(nombre))

numero = input_con_confirmacion("Dime un numero: ")
print("Has confirmado que te llamas: ".format(numero))

