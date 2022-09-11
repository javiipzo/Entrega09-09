from vehiculo import Vehiculo
from Bicicleta import Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        texto="Motocicleta, color: {}, de {} ruedas, tipo {} y de velocidad: {} km/h, y cilindrada: {}"
        return texto.format(self.color,self.ruedas,self.tipo,self.velocidad,self.cilindrada)
