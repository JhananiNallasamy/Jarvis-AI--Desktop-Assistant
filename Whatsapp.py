import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

contacts = {
    "Amma": "+919444574449",
    "Appa": "+917904223521",
    "Vaathu": "+60 11-2691 7854"
}

def sendMessage():
    speak("Who do you want to message?")
    recipient = input("Enter contact name or number: ")
    
    if recipient in contacts:
        phone_number = contacts[recipient]
    else:
        phone_number = recipient
    
    speak("What's the message?")
    message = input("Enter the message: ")
    
    try:
        pywhatkit.sendwhatmsg(phone_number, message, time_hour=strTime, time_min=update)
        speak("Message sent successfully.")
    except Exception as e:
        speak(f"Failed to send message. Error: {str(e)}")

# Example usage
sendMessage()
