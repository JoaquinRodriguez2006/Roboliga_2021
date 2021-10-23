from controller import Robot

timeStep = 32
max_velocity = 6.28
robot = Robot()

# Definimos las ruedas
wheel1 = robot.getDevice("wheel1 motor")   # Create an object to control the left wheel
wheel2 = robot.getDevice("wheel2 motor") # Create an object to control the right wheel

# Definimos su movimiento infinito
wheel1.setPosition(float("inf"))       
wheel2.setPosition(float("inf"))

# Para avanzar:
speed1 = max_velocity
speed2 = max_velocity

# Definimos las variables de avanzar
wheel1.setVelocity(speed1)              
wheel2.setVelocity(speed2)
# Esto debe ir obligatoriamente al final