#!/usr/bin/env python

"""
Author: saornek
Date: 08/04/2022
Last Updated: 08/13/2022
Status: working
Purpose: Created for IC4U3 - Mecanum motor control with Adafruit TB6612
Notes: Mecanum Movements Inspired by https://www.researchgate.net/profile/Jin-Gang-Jiang-2/publication/307868549/figure/fig2/AS:713745810599936@1547181670156/Fig-5-Top-view-of-turning-principle-of-Mecanum-wheel.png
"""

import time
from MotorLib import *

#Motor(IN1,IN2,PWM,STANDBY,(Reverse polarity?))
frontLeft = Motor(17,27,22,8,False)
frontRight = Motor(26,6,13,8,False)
backLeft = Motor(12,5,24,8,False)
backRight = Motor(11,10,9,8,False)

def stop():
    print("IC4U Stop.")
    frontLeft.stop();
    backLeft.stop();
        
    frontRight.stop();
    backRight.stop();
        
def forward(speed):
    print("IC4U Forward.")
    frontLeft.forward(speed);
    backLeft.forward(speed);
        
    frontRight.forward(speed);
    backRight.forward(speed);
        
def backward(speed):
    print("IC4U Backward.")
    frontLeft.backward(speed);
    backLeft.backward(speed);
        
    frontRight.backward(speed);
    backRight.backward(speed);
        
def crabLeft(speed):
    print("IC4U Crab Left.")
    frontLeft.backward(speed);
    backLeft.forward(speed);
        
    frontRight.forward(speed);
    backRight.backward(speed);
        
def crabRight(speed):
    print("IC4U Crab Right.")
    frontLeft.forward(speed);
    backLeft.backward(speed);
        
    frontRight.backward(speed);
    backRight.forward(speed);
                
def fullTurnLeft(speed):
    print("IC4U Full Turn Left")
    frontLeft.backward(speed);
    backLeft.backward(speed);
        
    frontRight.forward(speed);
    backRight.forward(speed);
        
def fullTurnRight(speed):
    print("IC4U Full Turn Right")
    frontLeft.forward(speed);
    backLeft.forward(speed);
        
    frontRight.backward(speed);
    backRight.backward(speed);
