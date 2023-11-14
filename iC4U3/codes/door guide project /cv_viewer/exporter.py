"""
Author: saornek
Date: 08/04/2023
Last Updated: 11/14/2023
Status: Working
Purpose: iC4U3 Door Guide Project - Give distance between a visually impaired person's hand and the door knob.
Update: Simplified calculation with 2D position values. Added return, so the directions can be printed to the screen.
Notes: Next step voice commands.
"""

# Import Libraries
import serial 

#ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

def values(x_value, y_value):
    global y_read
    errorCalculation = 60

    if y_value > errorCalculation:
        y_read = "UP"
    elif y_value < -errorCalculation:
        y_read = "DOWN"
    else:
        y_read = "Y AXIS OK."

    if x_value > errorCalculation:
        x_read = "LEFT"
    elif x_value < -errorCalculation:
        x_read = "RIGHT"
    else:
        x_read = "X AXIS OK."

    return str("Y AXIS: " + y_read + " / X AXIS: " + x_read)
        
