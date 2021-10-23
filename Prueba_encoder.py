from controller import Robot
import time
timeStep = 32            # Set the time step for the simulation
max_velocity = 6.28      # Set a maximum velocity time constant
nothing = 0
# Make robot controller instance
robot = Robot()

# Define the wheels 
wheel1 = robot.getDevice("wheel1 motor")   # Create an object to control the left wheel
wheel2 = robot.getDevice("wheel2 motor") # Create an object to control the right wheel

# Set the wheels to have infinite rotation 
wheel1.setPosition(float("inf"))       
wheel2.setPosition(float("inf"))

# Set encoders and rotation
encoderderecho = wheel2.getPositionSensor()
encoderizquierdo = wheel1.getPositionSensor()
encoderderecho.enable(timeStep)
encoderizquierdo.enable(timeStep)
rotacion = 0
rotacion = 2.3 # 90' 

# Define distance sensors
s5 = robot.getDevice("ps5")   # adelante izquierda
s7 = robot.getDevice("ps7")   # costado izquierda
s0 = robot.getDevice("ps0")   # adelante derecha
s2 = robot.getDevice("ps2")   # costado derecha

# Enable distance sensors N.B.: This needs to be done for every sensor
s5.enable(timeStep)
s7.enable(timeStep)
s0.enable(timeStep)
s2.enable(timeStep)
start = robot.getTime()


def avanzar(vel):
    speed1 = vel
    speed2 = vel

def girar_derecha(vel):
    speed1 = vel
    speed2 = -vel

def girar_izquierda():
    speed1 = -vel
    speed2 = vel

def quieto():
    speed1 = nothing
    speed2 = nothing

while robot.step(timeStep) != -1:
    speed1 = max_velocity
    speed2 = max_velocity
    w = encoderderecho.getValue()
    b = w
    if w<rotacion:
        print("avanzar")
        speed1 = -max_velocity
        speed2 = max_velocity
        if w >= rotacion:
            time.sleep(10)

    """if (s7.getValue() > 0.1 and s0.getValue() > 0.1): # Pregunta si ve algo con alguno de los sensores de adelante. En ese caso, avanza.
        avanzar(max_velocity)
        print("avanzar")
    else:
        turn_left_on_place()
        print("derecha")"""

    
    # if (s7.getValue() < 0.1 and s0.getValue() < 0.1): # Si detecta algo con los sensores de adelante, pregunta si ve algo con los sensores de los costados
    # if (s2.getValue() < 0.1):
    #     girar_derecha(vel)

    # if (s5.getValue() < 0.1):
    #    girar_izquierda(vel)

    # Set the wheel velocity 
    wheel1.setVelocity(speed1)              
    wheel2.setVelocity(speed2)