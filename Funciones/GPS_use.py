from controller import Robot, GPS

timestep = 32
tilesize = 0.06

robot = Robot()

# Se carga el GPS
gps = robot.getDevice("gps")
gps.enable(timestep)

# Definimos las coordenadas X e Y del punto de destino
destino_x = 0.0
destino_y = -4.0

# Seteamos todos los valores en 0 y cargamos la posición actual
robot.step(timestep) # Actualizo los valores de los sensores
startX = gps.getValues()[0]/tilesize # Cargo La posicion inicial
startY = gps.getValues()[2]/tilesize

while robot.step(timestep) != -1:
# Se obtiene el valor que toma el GPS y se lo divide por el tamaño de la casilla menos la posición inicial, para 
# saber cuanto nos falta recorrer
# La función "round" y el ",1" del final corresponden a un redondeo de valores. El GPS arroja muchos número y así
# los achicamos.
    x = round( gps.getValues()[0]/tilesize - startX, 1 )
    y = round( gps.getValues()[2]/tilesize - startY, 1 )