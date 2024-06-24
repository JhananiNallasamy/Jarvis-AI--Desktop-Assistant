from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition 
import os
from playsound import playsound
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import time
import os

def translategl(query):
    speak("SURE MA'AM")
    translator = Translator()
    print(translator.detect(query))  # Debugging statement
    speak("Choose the language in which you want to translate")
    b = input("To_Lang: ")
    
    try:
        print("Query:", query)  # Debugging statement
        if query:  # Check if query is not None
            translation = translator.translate(query, src="auto", dest=b)
            translated_text = translation.text

            if translated_text:  # Check if translated_text is not None
                speak(translated_text)
            else:
                speak("Sorry, I couldn't translate your text. Please try again later.")
        else:
            speak("Sorry, I couldn't understand the text you want to translate.")
    except Exception as e:
        print("Translation Error:", e)
        speak("Sorry, I couldn't translate your text. Please try again later.")

def speak(text):
    speakgl = gTTS(text=text, lang='en', slow=False)
    speakgl.save("voice.mp3")
    playsound("voice.mp3")
    time.sleep(5)
    os.remove("voice.mp3")

# Test the translategl function
translategl("I am a girl")
