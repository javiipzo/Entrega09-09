from Coche import Coche
from vehiculo import Vehiculo
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta
def catalogarN(lista):
    for x in lista:
        print(type(x).__name__,x)

def catalogar(lista,ruedas):
    x=0
    for y in lista:
        if (y.ruedas == ruedas):
            x+=1
    print ("Se han encontrado {} vehículos con {} ruedas:".format(x,ruedas))
    for y in lista:
        if (y.ruedas == ruedas):
            print (type(y).__name__,y)


c = Coche("azul", 4, 150, 1200)
ca= Camioneta("rojo", 4, 88, 1000, 2000)
b= Bicicleta("rosa", 2, "urbana")
m= Motocicleta("Negra",2, "deportiva",180, 1400)
vehiculos=[m,ca,b,c]
catalogar(vehiculos,4)
