"""
Author: saornek
Purpose: Extra process zed object detection data and export to RPi
Notes: -
"""
#import libraries
import serial
import math

ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

def values(label, response):

  # process values
  
  #send values to RPi
  ser.write(str.encode(value + "\n")) #comment for test purposes
