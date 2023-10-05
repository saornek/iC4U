#!/usr/bin/env python3

"""
Author: saornek
Date: 06/18/2022
Last Updated: 09/24/2022
Status: tested - worked
Purpose: Created for IC4U3 - IC4U Assistant
Notes: Using Google Assistant Api - https://developers.google.com/assistant/sdk/reference/rpc
"""

""" LIBRARIES """
import logging
import serial

from aiy.board import Board
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import audio
from aiy.voice import tts

from TB6612Library import *
import MecanumLib as ic4uMotors

arduinoSer = serial.Serial("/dev/ttyUSB0", 9600) #Connect to Arduino via serial with an baudrate of 9600

hotwords = ["okay ic4u", "okay i see for you", "hey ic4u", "hey i see for you"] #Make an hotword/wakeword list. Ex: "Okay Google."

""" MAIN FUNCTION """
def assistant():
    logging.basicConfig(level=logging.DEBUG)
    client = CloudSpeechClient()
    with Board() as board:
        while True:   
            logging.info('Say the hotword.')
            text = client.recognize(language_code='en-US',hint_phrases=None) #Start Mic for hotword.
            if text is None:
                logging.info('You said nothing.')
                continue
            logging.info('You said: "%s"' % text)
            text = text.lower()
            logging.info('Say a keyword.')
            if text in hotwords: #Check if Hotword was used.
                audio.play_wav('voiceActivated.wav')
                text = client.recognize(language_code='en-US',hint_phrases=None) #Start Mic for command/question.
                text = text.lower()
                logging.info('You said: "%s"' % text)
                if text is None:
                    logging.info('You said nothing.')
                    continue
                elif text in hotwordMappings: #Check if there is a function binded to the word.
                    hotwordMappings[text]() #do the function binded to the word.
                    break
            else:
                continue

""" ACTION FUNCTIONS """
def sitFunction():
    print("Sitting.")
    arduinoSer.write(str.encode("S"))

def downFunction():
    print("Laying Down")
    arduinoSer.write(str.encode("D"))

def upFunction():
    print("Stand Up.")
    arduinoSer.write(str.encode("U"))   

def forwardFunction():
    tts.say("I am going Forward.")
    ic4uMotors.robotMovements.forward(80)

def backwardFunction():
    tts.say("I am going backward.")
    ic4uMotors.robotMovements.backward(80)

def stopFunction():
    tts.say("I stopped.")
    ic4uMotors.robotMovements.stop()

def leftFunction():
    tts.say("I am moving to the left.")
    ic4uMotors.robotMovements.crabLeft(100)

def rightFunction():
    tts.say("I am moving to the right.")
    ic4uMotors.robotMovements.crabRight(100)

def navigateFunction():
    print("navigate") 
    #Code Here

hotwordMappings = {
    'sit' : sitFunction,
    'down' : downFunction,
    'up' : upFunction,
    'forward' : forwardFunction,
    'backward' : backwardFunction,
    'stop' : stopFunction,
    'left' : leftFunction,
    'right' : rightFunction,
    'navigation' : navigateFunction }

while True:
    assistant()
