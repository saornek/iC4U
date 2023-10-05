#!/usr/bin/env python3


#google assistant libraries
import logging
import platform
import subprocess
import sys

from google.assistant.library.event import EventType

from aiy.assistant import auth_helpers
from aiy.assistant.library import Assistant
from aiy.board import Board, Led

from aiy.voice import tts

#googlemaps libraries
import googlemaps
from datetime import datetime
from time import sleep

#geocoder library
import geocoder

#full code
import os
import threading

stop = threading.Event()

gmaps = googlemaps.Client(key='Client Key')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

#getting the current location
myloc = geocoder.ip('me')


def process_event(assistant, led, event):
    logging.info(event)
    if event.type == EventType.ON_START_FINISHED:
        led.state = Led.BEACON_DARK  # Ready.
        tts.say("Where would you like to go?")
        print("Where would you like to go?")
        sleep(0.5)
        print('Say "OK, Google" then speak, or press Ctrl+C to quit...')
        sleep(1.5)
        tts.say("Okay Google")
        print("Say the hotword pleasee")
    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        led.state = Led.ON  # Listening.
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        destination = event.args['text'].lower()
        print(destination)
        print(myloc.latlng)
        now = datetime.now()

        directions_result = gmaps.directions(myloc.latlng,
                                     destination,
                                     mode="walking",
                                     departure_time=now)

        b = [str(item) for item in directions_result]

        for c in b:
            split_lines = c.split(",")

        search_keywords=['html_instructions']

        dct = {}
        for sentence in split_lines:
            dct[sentence] = sum(1 for word in search_keywords if word in sentence)
            
        best_sentences = [key for key,value in dct.items() if value == max(dct.values())]

        result = "\n".join(best_sentences)



        cleaned = result.replace("</b>", "")
        cleaned = cleaned.replace("<b>", "")
        cleaned = cleaned.replace('<div style="font-size:0.9em">', "")
        cleaned = cleaned.replace("steps", "")
        cleaned = cleaned.replace("</div>", "")
        cleaned = cleaned.replace("html_instructions", "")
        cleaned = cleaned.replace("'", "")
        cleaned = cleaned.replace(":", "")
        cleaned = cleaned.replace("legs", "")
        cleaned = cleaned.replace("[", "")
        cleaned = cleaned.replace("{", "")
        cleaned = cleaned.replace("}", "")
        cleaned = cleaned.replace("]", "") 
        print(cleaned)
        tts.say(cleaned,speed=65)

#       os.system("python3 ic4ucodes.py")
        stop.set()
    

        assistant.stop_conversation()
    elif event.type == EventType.ON_END_OF_UTTERANCE:
        led.state = Led.PULSE_QUICK  # Thinking.
    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        led.state = Led.BEACON_DARK  # Ready.
    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    logging.basicConfig(level=logging.INFO)

    credentials = auth_helpers.get_assistant_credentials()
    with Board() as board, Assistant(credentials) as assistant:
        for event in assistant.start():
            print("got an event")
            process_event(assistant, board.led, event)
            print("processed event")
            if stop.is_set():
                print("breaking")
                break
            print("asst finished")
        print("navigation mode is done")
            



    


if __name__ == '__main__':
    main()
