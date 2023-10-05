"""
Author: saornek
Date: 08/04/2023
Last Updated: 09/06/2023
Status: Testing - distance not working.
Purpose: iC4U3 Door Guide Project - Give distance between a visually impaired person's hand and the door knob.
Update: Deleted Euclidean distance calculation. Corrected object position bug. Added error calculations.
Notes: -
"""

# Import Libraries
import serial 
import math
import numpy as np
import pyzed.sl as sl

#ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

handPos = None
knobPos = None

def calculate(constantPoint, newPoint):
    x_const, y_const, z_const = constantPoint
    x_new, y_new, z_new = newPoint
    error = 0.05

    # up-down correction
    if z_new < (z_const - error):
        z_value = "U P"
    elif z_new > (z_const + error):
        z_value = "D O W N"
    else:
        z_value = "(Z) A X I S - O K A Y "

    # left-right
    if x_new < (x_const - error):
        x_value = "L E F T"
    elif x_new > (x_const + error):
        x_value = "R I G H T"
    else:
        x_value = "(X) A X I S - O K A Y "

    return z_value, x_value

def values(label, rawPosition, state):
    global handPos, knobPos

    if (objectCustomLabel == 'hand'):
        handPos = text_position
    elif objectCustomLabel == 'knob':
        knobPos = text_position
    else:
        handPos = (0,0)
        knobPos = (0,0)

    if ((objectCustomLabel == 'hand') and (state == sl.OBJECT_TRACKING_STATE.OK)):
        calculate(knobPos, handPos)
