from vehiculo import Vehiculo
from Coche import coche
class camioneta(coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga
    def __str__(self):
        texto="Camioneta, color: {}, de {} ruedas, de velocidad: {} km/h, cilindrada: {}, y soporta carga de hasta {}"
        return texto.format(self.color,self.ruedas,self.velocidad,self.cilindrada,self.carga)