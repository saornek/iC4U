"""
Author: saornek
Date: 08/04/2023
Last Updated: 11/13/2023
Status: Testing (X Axis not tested)
Purpose: iC4U3 Door Guide Project - Give distance between a visually impaired person's hand and the door knob.
Update: Simplified calculation with 2D position values.
Notes: -
"""

# Import Libraries
import serial 

#ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

def values(x_value, y_value):
    errorCalculation = 60

    if y_value > errorCalculation:
        y_read = "UP"
    elif y_value < -errorCalculation:
        y_read = "DOWN"
    else:
        y_read = "Y AXIS OK."

# Not Tested.
    if x_value > errorCalculation:
        x_read = "LEFT"
    elif x_value < -errorCalculation:
        x_read = "RIGHT"
    else:
        x_read = "X AXIS OK."
        
