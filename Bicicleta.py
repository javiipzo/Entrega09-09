from vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

    def __str__(self):
        texto="Bicicleta, color: {}, de {} ruedas y tipo {}"
        return texto.format(self.color,self.ruedas,self.tipo)