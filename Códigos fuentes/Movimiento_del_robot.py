from controller import Robot
from controller import Motor
from controller import PositionSensor

#Create OBJECTS here

robot = Robot() # Create robot object
timeStep = 32   # timeStep = number of milliseconds between world updates

leftMotor = robot.getDevice("wheel1 motor")    # Motor initialization
rightMotor = robot.getDevice("wheel2 motor")
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftEncoder = leftMotor.getPositionSensor()    # Encoder initialization
rightEncoder = rightMotor.getPositionSensor()
leftEncoder.enable(timeStep)
rightEncoder.enable(timeStep)

#Start your CODE here

def avanzar(vel):
    leftMotor.setVelocity(vel)
    rightMotor.setVelocity(vel)

def g_derecha(vel):
    leftMotor.setVelocity(vel)
    rightMotor.setVelocity(-vel)

def g_izquierda(vel):
    leftMotor.setVelocity(-vel)
    rightMotor.setVelocity(vel)

