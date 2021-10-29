import math
from controller import Robot
from controller import Motor
from controller import PositionSensor

robot = Robot() # Create robot object
timeStep = 32   # timeStep = numero de milisegundos entre actualizaciones mundiales (del mundo)
angulo_actual = 0

#Create your objects here
ruedaIzquierda = robot.getDevice("wheel1 motor")    # Motor initialization
ruedaDerecha = robot.getDevice("wheel2 motor")
ruedaIzquierda.setPosition(float('inf'))
ruedaDerecha.setPosition(float('inf'))

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

#Gps
gps = robot.getDevice("gps")
gps.enable(timeStep)
tilesize = 0.06
robot.step(timeStep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

#Create your code here
def avanzar(vel):
    ruedaIzquierda.setVelocity(vel)
    ruedaDerecha.setVelocity(vel)

def girar(vel):
    ruedaIzquierda.setVelocity(-vel)
    ruedaDerecha.setVelocity(vel)

def rotar(angulo):
    global angulo_actual
    tiempo_anterior = 0

    #  iniciar_rotacion
    girar(0.5)  
    # Mientras no llego al angulo solicitado sigo girando  
    while (abs(angulo - angulo_actual) > 1):
        tiempo_actual = robot.getTime()
        # print("Inicio rotacion angulo", angulo, "Angulo actual:",angulo_actual)
        tiempo_transcurrido = tiempo_actual - tiempo_anterior  # tiempo que paso en cada timestep
        radsIntimestep = abs(gyro.getValues()[1]) * tiempo_transcurrido   # rad/seg * mseg * 1000
        degsIntimestep = radsIntimestep * 180 / math.pi
        print("rads: " + str(radsIntimestep) + " | degs: " + str(degsIntimestep))
        angulo_actual += degsIntimestep
        # Si se pasa de 360 grados se ajusta la rotacion empezando desde 0 grados
        angulo_actual = angulo_actual % 360
        # Si es mas bajo que 0 grados, le resta ese valor a 360
        if angulo_actual < 0:
            angulo_actual += 360
        tiempo_anterior = tiempo_actual
    print("Rotacion finalizada.")
    return True
    
while robot.step(timeStep) != -1:
    x = gps.getValues()[0]/tilesize
    y = gps.getValues()[2]/tilesize
    if rotar(90):
        print("Rotacion de 90 terminada, me detengo")
        avanzar(0)
        avanzar(2)
    if x == -5.0 and y == -1.0:
        print("Llegué, pa")
        avanzar(0)
    # Cargo el controlador para el sensor de distancia
    """distance1 = distance_sensor1.getValue()
    distance_sensor2 = robot.getDevice("distance sensor2")
    distance_sensor2.enable(timeStep)"""
    """if distance1 <= 0.05:
        avanzar(2)"""
    """distance_sensor1 = robot.getDevice("distance sensor1")
    distance_sensor1.enable(timeStep)"""