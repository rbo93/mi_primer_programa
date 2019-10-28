import random

class Perifericos:
    def __init__(self):
        self.numero_serie = random.randrange(100, 10000)
        self.estado = 100


class Monitor(Perifericos):
    alto = 40
    ancho = 50
    profundidad = 10
    peso = 4
    color = "negro"
    pulgadas = 27
    conectorees = ["hdmi", "dp"]
    botones = ["encendido", "menu"]
    resolucion = [2560, 1440]



moonitor1 = Monitor()
moonitor2 = Monitor()
moonitor3 = Monitor()

class Teclado(Perifericos):
    alto = 3
    ancho = 50
    profundidad = 30
    peso = 1
    color = "negro""
    numero_teclas = 74
    idioma = "es"


class TorrePC:
    alto
    ancho
    profundidad
    peso
    color
    tarjeta_grafica
    procesador
    ram
    disco_duro

