"""
Author: saornek
Date: 12/10/2023
Purpose: iC4U3 TTS for Testing
"""
from gtts import gTTS
from pygame import mixer

mixer.init()

def say(text):
    tts = gTTS(text=text, lang='en')
    audio_file = 'output.mp3'
    tts.save(audio_file)
    sound = mixer.Sound('output.mp3')
    sound.play()