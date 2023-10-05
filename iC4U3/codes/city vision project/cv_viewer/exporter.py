"""
Author: saornek
Date: 06/19/2023
Status: New Update Not Tested
Last Updated: 06/23/2023
Purpose: Find Traffic Light Color + Export detected object values to RPi
Update: Error rate added to green color.
Notes:
"""

import serial
import math

import cv2
import numpy as np

#ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

def values(label, response):
    
    foundLabel = label

    responseDict = {
        #General ones
        "info": "It is a " + label + ".",
        "warn": "There is a " + label + " in your way.",
        "hello": "Hello " + label,
        "stop": "There is a " + label + " in your way. We are stopping.",
        "sit": "There is a " + label + " in your way. We need to wait.",
        #Custom ones.
        "water": "We are close to " + label + "!",
    }

    foundResponse = response
    print(responseDict[response])

    #print(ID, label, raw_position, raw_velocity) #uncomment for test purposes
    #print(label, response) #uncomment for test purposes

def detectColor(path):
    # Load the image
    image = cv2.imread(path)

    # Define the color ranges for detection (in HSV)
    errorRate = 20  # Adjust the error rate as per your requirement

    green_lower = (40 - errorRate, 50, 50)
    green_upper = (80 + errorRate, 255, 255)

    colorRanges = [
        [green_lower, green_upper],
        [(0, 50, 50), (20, 255, 255)]  # Red color range
    ]

    # Define the minimum brightness threshold
    minBrightnessThresh = 130  # Example: 100

    # Convert the image from BGR to HSV color space
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    result = []
    

    # Detect color brightness for each color range
    for colorRange in colorRanges:
        # Define the lower and upper boundaries for the color range
        lowerColor = np.array(colorRange[0])
        upperColor = np.array(colorRange[1])

        # Threshold the image to get only the specified color
        colorMask = cv2.inRange(hsvImage, lowerColor, upperColor)

        if np.any(colorMask):
            # Calculate the brightness of the color
            brightnessValues = hsvImage[:, :, 2]
            colorBrightness = np.mean(brightnessValues[colorMask > 0])
        else:
            colorBrightness = 0

        # Check if the color brightness is greater than the minimum brightness threshold
        if colorBrightness > minBrightnessThresh:
            result.append(True)
        else:
            result.append(False)

    if result[0] == True:
        #print("The traffic light for cars is green. We should wait.") #this will be sent to RPi
        return "GREEN"
    elif result[1] == True:
        #print("The traffic light for cars is red. We can pass.") #this will be sent to RPi
        return "RED"
    
    return "YELLOW"
