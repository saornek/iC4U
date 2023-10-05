"""
Author: saornek
Date: 06/23/2023
Last Updated: 06/26/2023
Status: Tested 
Purpose: Web scrap detected object information  and export to RPi
Update: Rewritten gTTS and translate service. Also added Check and  compare system so it did not repeat same outputs.
Notes: pip install googletrans==4.0.0-rc1 gtts playsound
"""

# Import Libraries
import serial

# Import for web scrapping
from bs4 import BeautifulSoup
import requests

# Import for tts
from googletrans import Translator

# Import for TTS - TEST PURPOSES ONLY - Uncomment to test
from gtts import gTTS
from playsound import playsound

# Connect to RPi
#ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

# Connect to user client (Needs to change according to device. Write 'my user agent' on browser)
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }

# Create a translator object
translator = Translator(service_urls=['translate.google.com'])

def scrap(asin):
    yourLink = 'https://www.amazon.com.tr/dp/' + asin
    webpage = requests.get(yourLink, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    # get product title
    title = soup.find(id='productTitle').get_text().strip()
    title = translator.translate(title, src='tr', dest='en').text

    # get availability
    availabilityCheck = soup.find(id='availability').get_text().strip()
    if (availabilityCheck != None):
        if (availabilityCheck == "Stokta Yok."): #Translate from Turkish to English
            stockStatus = "Out of stock."
        else:
            stockStatus = "In stock."
    else:
        stockStatus = ""

    # get price
    priceWhole = soup.find(class_='a-price-whole').get_text().strip()
    priceFraction = soup.find(class_='a-price-fraction').get_text().strip()
    priceSymbol = soup.find(class_='a-price-symbol').get_text().strip()
    if ((priceWhole != None) and (priceFraction != None) and (priceSymbol != None)):
        priceTotal = "You can buy it for " + priceWhole + " point " + priceFraction + " turkish lira."
    else:
        priceTotal = ""
        
    productInfo = title + " is " + stockStatus + "on Amazon. " + priceTotal
    print(str(productInfo))
    say(str(productInfo))

    #ser.write(str.encode(title + "/" + stockStatus + "\n")) #comment for test purposes

prevID = ""
prevIDCount = 0

def values(id): #Do not repeat same ASIN value.
    global prevID
    global prevIDCount

    prevIDCount += 1

    if (id != prevID) and (prevIDCount >= 30): #prevIDCount gives a cooldown time for the bound boxes to create
        scrap(id)
        prevID = id
        prevIDCount = 0
    else:
        prevIDCount += 1

def say(text):
    # Create a gTTS object with the text
    tts = gTTS(text=text, lang='en')

    # Save the speech audio to a file
    audio_file = 'output.mp3'
    tts.save(audio_file)

    # Play the audio file
    playsound(audio_file)
