#!/usr/bin/env python3
# Copyright 2017 Google Inc.# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Edited by Selinoid :) ;) :D <3

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import subprocess
import sys
import serial


from google.assistant.library.event import EventType

from aiy.assistant import auth_helpers
from aiy.assistant.library import Assistant
from aiy.board import Board, Led
from aiy.voice import tts
from gpiozero import PWMOutputDevice
from time import sleep

#importing these for navigation mode
import os
import navigationv2


ser = serial.Serial('/dev/ttyUSB0', 9600)
sleep(5)

#a = PWMOutputDevice(26)
#b = PWMOutputDevice(22)
#c = PWMOutputDevice(17)
#d = PWMOutputDevice(27)

a = None
b = None
c = None
d = None


def process_event(assistant, led, event):
    logging.info(event)
    if event.type == EventType.ON_START_FINISHED:
        led.state = Led.BEACON_DARK  # Ready.
        print('Say "OK, Google" then speak, or press Ctrl+C to quit...')
    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
         led.state = Led.ON  # Listening.
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
          print('You said:', event.args['text'])
          text = event.args['text'].lower()
          print('Say "OK, Google" then speak, or press Ctrl+C to quit...')
          led.state = Led.ON  # Listening.
          if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
           print('You said:', event.args['text'])
           text = event.args['text'].lower()
           if text == 'down':
            down()
           elif text == 'stop':
            stop()
           elif text == 'up':
            up()
           elif text == 'go':
            go()
           elif text == 'sit':
            sit()
           elif text == 'left':
            left()
           elif text == 'right':
            right()
           elif text == 'back':
            back()
           elif text == 'navigation mode':
            navigation()

 
def main(a_, b_, c_, d_):
    global a, b, c, d
    a = a_
    b = b_
    c = c_
    d = d_

    logging.basicConfig(level=logging.INFO)

    credentials = auth_helpers.get_assistant_credentials()
    with Board() as board, Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, board.led, event)


def down():
    print('I am laying down')
    ser.write(str.encode('D'))
    print('Done')


def up():
    print('I am standing')
    ser.write(str.encode('U'))
    print('Done')

def sit():
    print('I am siting down')
    ser.write(str.encode('S'))
    print('Done')

def go():
    print('I am going forward')
    c.value = 0.27
    a.value = 0.27
    sleep(5)
    c.value = 0
    a.value = 0
    print('Still going forward say Stop for me to stop')

def stop():
    print('I am stoping')
    c.value = 0
    a.value = 0
    b.value = 0
    d.value = 0
    print('Stoping, you can command me all the commands')

def left():
    print('Turning left')
    c.value = 0.6  
    a.value = 0.27
    ser.write(str.encode('L'))
    sleep(5)
    c.value = 0.27
    a.value = 0.27
    print('Done')

def right():
    print('Turning Right')
    c.value = 0.27 #right
    a.value = 0.6 #left
    ser.write(str.encode('R'))
    sleep(5)
    c.value = 0.27
    a.value = 0.27
    print('Done')

def back():
    print('I am going backward')
    b.value = 0.3
    d.value = 0.3
    sleep(3)
    b.value = 0
    d.value = 0
    print('Done')

def navigation():
    print("running navigationv2.py")
#   import navigationv2
#   navigationv2.main()
    os.system("python3 navigationv2.py")
    print("navigationv2.py ended")
    


if __name__ == '__main__':
    a = PWMOutputDevice(26)
    b = PWMOutputDevice(22)
    c = PWMOutputDevice(17)
    d = PWMOutputDevice(27)
    main(a, b, c, d)