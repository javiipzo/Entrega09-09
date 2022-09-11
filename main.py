from Coche import coche
from vehiculo import Vehiculo
from Camioneta import camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta
def catalogar(lista):
    for x in lista:
        print(x)
def catalogar(lista,ruedas):
    x=0
    







c = coche("azul", 4, 150, 1200)
ca= camioneta("rojo", 6, 88, 1000, 2000)
b= Bicicleta("rosa", 2, "urbana")
m= Motocicleta("Negra",3, "deportiva",180, 1400)
vehiculos=[m,ca,b,c]
catalogar(vehiculos)
