from vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        texto=" color: {}, de {} ruedas, de velocidad: {} km/h, y cilindrada: {}"
        return texto.format(self.color,self.ruedas,self.velocidad,self.cilindrada)
    