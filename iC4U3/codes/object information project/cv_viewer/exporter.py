import serial
import math

ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3)

def values(ID, label, raw_position, raw_velocity):
    #print(ID, label, raw_position, raw_velocity)
    position = positionCal(raw_position)
    velocity = velocityCal(raw_velocity)

    sendSentence = "ID:" + str(ID) + "I see a " + str(label) + " in my " + str(position) + "/ at a speed of " + str(velocity)
    ser.write(str.encode(sendSentence + "\n"))
    
def positionCal(rawPos):
    pos = rawPos[0]
    if pos >= 0.25:
        return "right"
    elif pos <= -0.1:
        return "left"
    else:
        return "in front"

def velocityCal(rawVel):
    vel = (int(rawVel[0])^2 + int(rawVel[1])^2 + int(rawVel[2])^2)
    if vel <= 0:
        return 0
    else:
        return round(math.sqrt(vel), 1)
