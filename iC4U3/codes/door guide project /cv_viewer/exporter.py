"""
Author: saornek
Date: 08/04/2023
Last Updated: 11/30/2023
Status: Working.
Purpose: iC4U3 Door Guide Project - Give distance between a visually impaired person's hand and the door knob.
Update: Cleaned and formatted. Horizontal and Vertical Correction Working.
Notes:
For testing purposes used the pygame.mixer library for audio output as it doesn't freeze the camera output.
"""

# Import Libraries
import serial
from time import sleep

# Import for TTS - TEST PURPOSES ONLY - Uncomment to test
from gtts import gTTS
from pygame import mixer

mixer.init()
#ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

prev_y_read = ""
prev_x_read = ""
sayStatus = 0
repeatBlock = 0

def values(x_value, y_value):
    global y_read, x_read
    global prev_y_read, prev_x_read
    global sayStatus, repeatBlock
    errorCalculation = 60
    
    # Y-AXIS Calculation (Up-Down)
    if y_value > errorCalculation:
        y_read = "UP"
    elif y_value < -errorCalculation:
        y_read = "DOWN"
    else:
        y_read = "Y AXIS OK"

    if (y_read != prev_y_read) and (y_read != "Y AXIS OK") and (sayStatus == 0):
        say(y_read)
        sayStatus = 1
    elif (y_read == "Y AXIS OK") and (sayStatus == 1):
        sayStatus = 2
    prev_y_read = y_read

    # X-AXIS Calculation (Left-Right)
    if x_value > errorCalculation:
        x_read = "LEFT"
    elif x_value < -errorCalculation:
        x_read = "RIGHT"
    else:
        x_read = "X AXIS OK" 

    if (x_read != prev_x_read) and (x_read != "X AXIS OK") and (sayStatus == 2):
        say("Your hand is correct vertically. " + x_read)
        sayStatus = 3
        prev_x_read = x_read
    elif (x_read != prev_x_read) and (x_read == "X AXIS OK") and (sayStatus == 3):
        say("Your hand is correct horizontaly. Your hand should be on the knob. You are ready to open the door.")
        sayStatus = 4
        prev_x_read = x_read

    return str("Y AXIS: " + y_read + " / X AXIS: " + x_read)    
    # print("Y AXIS:", y_read, "X AXIS", x_read) #Uncomment to test.

def say(text):
    # Create a gTTS object with the text
    tts = gTTS(text=text, lang='en')

    # Save the speech audio to a file
    audio_file = 'output.mp3'
    tts.save(audio_file)

    # Play the audio file
    sound = mixer.Sound('output.mp3')
    sound.play()
