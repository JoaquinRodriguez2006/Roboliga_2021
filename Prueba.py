from controller import Robot
import math
timeStep = 32            # Set the time step for the simulation
max_velocity = 6.28      # Set a maximum velocity time constant
# Make robot controller instance
robot = Robot()

# Define the wheels 
wheelm1 = robot.getDevice("wheel1 motor")   # Create an object to control the left wheel
wheelm2 = robot.getDevice("wheel2 motor") # Create an object to control the right wheel

# Set the wheels to have infinite rotation 
wheelm1.setPosition(float("inf"))       
wheelm2.setPosition(float("inf"))

# Set encoders and rotation
encoderderecho = wheelm2.getPositionSensor()
encoderizquierdo = wheelm1.getPositionSensor()
encoderderecho.enable(timeStep)
encoderizquierdo.enable(timeStep)
rotacion = 0
rotacion = 2.3 # 90' 

# Define distance sensors
s5 = robot.getDevice("distance sensor1")   # adelante izquierda
s7 = robot.getDevice("distance sensor2")   # costado izquierda
s0 = robot.getDevice("distance sensor3")   # adelante derecha
s2 = robot.getDevice("distance sensor4")   # costado derecha

# Cargo controlador del gyrosocopo
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)

# Enable distance sensors N.B.: This needs to be done for every sensor
s5.enable(timeStep)
s7.enable(timeStep)
s0.enable(timeStep)
s2.enable(timeStep)
start = robot.getTime()

# Variables
angulo_actual = 0

def avanzar(vel):
    speed1 = vel
    speed2 = vel

def girar_derecha(vel):
    speed1 = vel
    speed2 = -vel

def girar_izquierda(vel):
    speed1 = -vel
    speed2 = vel

def quieto():
    speed1 = 0
    speed2 = 0
    
while robot.step(timeStep) != -1:
    speed1 = max_velocity
    speed2 = max_velocity
    wheelm1.setVelocity(speed1)              
    wheelm2.setVelocity(speed2)