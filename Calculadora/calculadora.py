continuar = "SI"
resultado = 0
primer_numero =  0
segundo_numero = 0
operacion_realizar = ""

while continuar == "SI":
    operacion_realizar = input("Que operacion desea hacer? (multiplicar / dividir / sumar / restar): ").lower()
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))
    resultado = 0

    if operacion_realizar == "multiplicar":
        print("Se realizara la operacion {}x{}".format(primer_numero, segundo_numero))
        resultado = primer_numero * segundo_numero
    elif operacion_realizar == "dividir":
        print("Se realizara la operacion {}/{}".format(primer_numero, segundo_numero))
        resultado = primer_numero / segundo_numero
    elif operacion_realizar == "sumar":
        print("Se realizara la operacion {}+{}".format(primer_numero, segundo_numero))
        resultado = primer_numero + segundo_numero
    elif operacion_realizar == "restar":
        print("Se realizara la operacion {}-{}".format(primer_numero, segundo_numero))
        resultado = primer_numero - segundo_numero

    print("El resultado es {}".format(resultado))
    continuar = input("Si desea realizar otra operacion ingrese SI: ").upper()