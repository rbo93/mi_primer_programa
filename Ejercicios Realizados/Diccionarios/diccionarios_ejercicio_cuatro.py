

"""
Ejercicio 4

Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
sea la string.

mostrar_titulo_subrayado("Hola mundo")
         Hola mundo
Output = ----------
"""
def subrayado(a):
    linea = ""
    b = len(a)
    i=0
    while i != b:
        linea += "-"
        i += 1
    print(a)
    print(linea)
    return


string = input("Ingrese un texto: ")

subrayado(string)
