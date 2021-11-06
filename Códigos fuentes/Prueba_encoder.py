from controller import Robot
import time
import math
timeStep = 32            # Set the time step for the simulation
max_velocity = 6.28      # Set a maximum velocity time constant
angulo_actual = 0
angulo = 90
# Make robot controller instance
robot = Robot()

# Define the wheels 
wheel1 = robot.getDevice("wheel1 motor")   # Create an object to control the left wheel
wheel2 = robot.getDevice("wheel2 motor") # Create an object to control the right wheel

# Set the wheels to have infinite rotation 
wheel1.setPosition(float("inf"))       
wheel2.setPosition(float("inf"))

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

# Set encoders and rotation
encoderderecho = wheel2.getPositionSensor()
encoderizquierdo = wheel1.getPositionSensor()
encoderderecho.enable(timeStep)
encoderizquierdo.enable(timeStep)
rotacion = 0
rotacion = 2.3 # 90' 

# Define distance sensors
s5 = robot.getDevice("distance sensor1")   # adelante izquierda
s7 = robot.getDevice("distance sensor2")   # costado izquierda
s0 = robot.getDevice("distance sensor3")   # adelante derecha
s2 = robot.getDevice("distance sensor4")   # costado derecha

# Enable distance sensors N.B.: This needs to be done for every sensor
s5.enable(timeStep)
s7.enable(timeStep)
s0.enable(timeStep)
s2.enable(timeStep)
start = robot.getTime()

def avanzar(vel):
    global speed1
    global speed2
    speed1 = vel
    speed2 = vel

def girar_derecha(vel):
    global speed1
    global speed2
    speed1 = vel
    speed2 = -vel

def girar_izquierda(vel):
    global speed1
    global speed2
    speed1 = -vel
    speed2 = vel

def quieto():
    global speed1
    global speed2
    speed1 = 0
    speed2 = 0

def rotar(angulo):
    global angulo_actual
    global speed1
    global speed2
    print("Empieza el giro")
    tiempo_anterior = 0
    #  iniciar_rotacion
    speed1 = max_velocity
    speed2 = -max_velocity
    # Mientras no llego al angulo solicitado sigo girando con una precision de 1 grado 
    while (abs(angulo - angulo_actual) > 1):
        speed1 = max_velocity
        speed2 = -max_velocity
        tiempo_actual = robot.getTime()
        # print("Inicio rotacion angulo", angulo, "Angulo actual:",angulo_actual)
        tiempo_transcurrido = tiempo_actual - tiempo_anterior  # tiempo que paso en cada timestep
        radsIntimestep = abs(gyro.getValues()[1]) * tiempo_transcurrido   # rad/seg * mseg * 1000
        degsIntimestep = radsIntimestep * 180 / math.pi     # Convierto radianes a grados
        print("rads: " + str(radsIntimestep) + " | degs: " + str(degsIntimestep))
        angulo_actual += degsIntimestep
        # Si se pasa de 360 grados se ajusta la rotacion empezando desde 0 grados
        angulo_actual = angulo_actual % 360
        # Si es mas bajo que 0 grados, le resta ese valor a 360
        if angulo_actual < 0:
            angulo_actual += 360
        tiempo_anterior = tiempo_actual
        robot.step(timeStep)
    print("Rotacion finalizada.")
    avanzar(0)
    return True

while robot.step(timeStep) != -1:
    print("PS5:",s5.getValue())
    print("PS0:",s0.getValue())
    if (s5.getValue() > 0.1) and (s0.getValue() > 0.1):
        avanzar(max_velocity/4)
        print("Avanza")
    if (s5.getValue() < 0.1) and (s0.getValue() < 0.1):
        rotar(90)
        print("Retrocede")
    # Set the wheel velocity 
    wheel1.setVelocity(speed1)
    wheel2.setVelocity(speed2)