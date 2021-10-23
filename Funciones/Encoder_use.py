from controller import Robot, GPS
from controller import Motor
from controller import PositionSensor

robot = Robot() # Create robot object
timeStep = 32
noventaGrados = 2.3

# Inicializo en encoder

encoderIzquierdo = ruedaIzquierda.getPositionSensor()
encoderDerecho = ruedaDerecha.getPositionSensor()
encoderIzquierdo.enable(timeStep)
encoderDerecho.enable(timeStep)

# Funciones
- encoderDerecho.getValue()
- ruedaDerecha.setPosition(float(noventaGrados)) # Para deinir la posición final del encoder
- (abs(encoderDerecho.getValue())) # Para convertir el valor del encoder en absoluto