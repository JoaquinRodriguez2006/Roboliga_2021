from controller import Robot
from controller import Motor
from controller import PositionSensor
from controller import GPS

robot = Robot()

gps = robot.getDevice("gps")
timestep = 32
tilesize = 0.06
gps.enable(timestep)

robot.step(timestep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

tamañoCasilla = 6

ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

encoderIzquierdo = ruedaIzquierda.getPositionSensor()    # Encoder initialization
encoderDerecho = ruedaDerecha.getPositionSensor()
encoderIzquierdo.enable(timestep)
encoderDerecho.enable(timestep)

def avanzar(vel):
    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)

def girar(vel):
    ruedaIzquierda.setVelocity(-vel)
    ruedaDerecha.setVelocity(vel)

#def girarDer(vel):
#    ruedaIzquierda.setVelocity(vel)
#    ruedaDerecha.setVelocity(-vel)

avanzar(2)

noventaGrados = 2.3

while robot.step(timestep) != -1:
#    print ("encoder", encoderIzquierdo.getValue())
#    print (encoderDerechoValor)

    x = round(gps.getValues()[0]/tilesize - startX, 2)
    y = round(gps.getValues()[2]/tilesize - startY, 2)

    if (x <= 0.0) and (y <= -4.0):
        print ("Giremos pa")
        girar(0.5)
        print (encoderIzquierdo.getValue(), "encoder derecho: ", encoderDerecho.getValue())
        if (encoderDerechoValor + noventaGrados <= encoderDerecho.getValue()):
            print("salimos pa")
            break
    else:
        encoderDerechoValor = encoderDerecho.getValue()
        print ("no paso lo otro pa")

    print("Imprimo la posicion actual x:", x, "y:", y)



avanzar(0.5)