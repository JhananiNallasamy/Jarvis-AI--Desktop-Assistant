# ========================================================IMPORT PACKAGES===============================================================================================================================================================================================================================================
import os
import pyttsx3          # text-to-speech conversion library in Python.
import speech_recognition    #speech_recognition library, which provides easy access to several speech recognition APIs.
import requests                 #requests is a popular Python library used for making HTTP requests. It simplifies the process of sending HTTP requests and processing the responses.
                                # With requests, you can send GET, POST, PUT, DELETE, and other types of HTTP requests to web servers.
from bs4 import BeautifulSoup        #BeautifulSoup is a Python library (bs4 stands for Beautiful Soup 4) used for parsing HTML and XML documents, extracting data from them, and navigating through their content. 
                                     # It provides various methods and features to scrape data from web pages by parsing the HTML structure.
import datetime  # Import datetime module for working with dates and times
import pyautogui  #used for automating mouse and keyboard actions. It can control the mouse and keyboard to automate tasks, such as moving the mouse, clicking, typing, and taking screenshots.
import random     #used to generate random numbers. It can produce random integers, floating-point numbers, and even randomly select elements from a list.
import webbrowser #The webbrowser module provides a high-level interface to open web pages in a browser. It can be used to open URLs in the default web browser or specific browsers.
from plyer import notification #The plyer.notification module allows for sending desktop notifications. It can display system notifications with titles, messages, and icons.

import pygame  #for writing video games. It includes computer graphics and sound libraries. It provides functionality for creating games and multimedia applications.
import os.path  #provides functions for interacting with the file system. It includes functions to manipulate file paths, such as joining paths, checking for file existence, and getting file properties.
from pygame import mixer #for loading and playing sounds. It allows for audio playback and control within games and multimedia applications.
import speedtest  #for testing internet bandwidth using Speedtest.net's servers. It can measure download, upload speeds, and ping times.
import torch #a library for machine learning and deep learning developed by Facebook's AI Research lab (FAIR). It provides a wide range of tools for building and training neural networks.
from requests import get #from requests import get
from hugchat import hugchat #hugchat is likely a library for interacting with the Hugging Face chat models or similar AI chat services. It could be used to integrate chatbot functionalities into applications.




# ========================================================PASSWORD PROTECTION===========================================================================================================================================================================================================================================


for i in range(3):           #This sets up a loop that will iterate up to 3 times. The variable i will take on values 0, 1, and 2 during these iterations. The purpose of this loop is to give the user three attempts to enter the correct password.
    a = input("Enter Password to open Jarvis :- ")  #This prompts the user to enter a password. The input function reads a line from the input (usually the keyboard), converts it to a string, and assigns it to the variable a.
    pw_file = open("password.txt","r")  #This opens a file named "password.txt" in read mode ("r"). The variable pw_file now holds a file object that can be used to read the contents of the file.
    pw = pw_file.read() #This reads the entire content of the file "password.txt" and assigns it to the variable pw. Presumably, this file contains the correct password.
    pw_file.close()  #closes the file "password.txt". It is a good practice to close files after they are no longer needed to free up system resources.
    if (a==pw):
        print("WELCOME MA'AM ! PLZ SPEAK [GET UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

# ========================================================GUI OF JARVIS=====t======================================================================================================================================================================================================================================


from INTRO import play_gif   #This line imports the function play_gif from a module named INTRO.
play_gif


# ========================================================SPEAK FUNCTION================================================================================================================================================================================================================================================


engine = pyttsx3.init("sapi5")  #Initializes the pyttsx3 engine with the Microsoft Speech API (sapi5), which is commonly available on Windows platforms.
voices = engine.getProperty("voices") #Retrieves the available voices for the speech synthesis engine.
engine.setProperty("voice", voices[0].id) #Sets the voice property to the first voice in the voices list.
rate = engine.setProperty("rate",170)  #Sets the speaking rate of the engine to 170 words per minute.



def speak(audio):
    engine.say(audio)  #engine.say(audio): This line instructs the pyttsx3 engine (engine) to speak out the audio input passed to the speak() function.
    engine.runAndWait()  #engine.runAndWait(): This method blocks while processing all currently queued commands. It ensures that the speech is spoken synchronously with the function call, meaning the program waits until all text has been spoken before continuing execution.



def takeCommand():
    r = speech_recognition.Recognizer()   #Creates an instance of the Recognizer class from the speech_recognition module, which provides methods to recognize speech from audio sources.
    with speech_recognition.Microphone() as source:  #Uses the microphone (Microphone() context manager) as the audio source for capturing speech input.
        print("Listening.....")  #Prints a message indicating that the program is listening for speech input.
        r.pause_threshold = 1    #Sets the pause threshold to 1 second. This is the maximum amount of silence that can occur before the recognizer considers a phrase complete.
        r.energy_threshold = 300  #Sets the energy threshold for ambient noise levels. It helps filter out noise below this level.
        audio = r.listen(source,0,4) #Captures audio input from the microphone (source) and listens for up to 4 seconds (timeout=4). The 0 parameter adjusts for ambient noise suppression.



    try:         #This block of code attempts to execute the following statements. If any exceptions occur during the execution of these statements, they will be caught by the except block.
        print("Understanding..")   #Prints a message indicating that the program is processing and trying to understand the captured audio.
        query  = r.recognize_google(audio,language='en-in')  #query = r.recognize_google(audio, language='en-in'): Uses the recognize_google() method from the Recognizer instance (r) to recognize the speech in the captured audio input.
                                                             # audio: The captured audio input from the microphone.
                                                             # language='en-in': Specifies the language code for English (India) as the language of the speech to be recognized.
                                                             # The recognized speech is stored in the query variable.



        print(f"You Said: {query}\n")    #Prints the recognized speech (query) to the console, indicating what the user said.
    except Exception as e:             # If an exception occurs during the execution of the try block (e.g., if speech recognition fails or encounters an error), Python jumps to this block to handle the exception.
        print("Say that again")        #Prints a message indicating that the program couldn't understand the speech input and asks the user to repeat.
        return "None"                  # If an exception occurs, the function returns the string "None" to indicate that no valid speech input was recognized.
    return query                       # If no exceptions occur and the speech is successfully recognized, the function returns the query variable containing the recognized speech.


# ========================================================ALARM FUNCTION================================================================================================================================================================================================================================================

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# ===========================================================CHATBOT===================================================================================================================================================================================================================================================
def chatbot(query):
    user_input = query.lower()
    chatbot_instance = hugchat.ChatBot(cookie_path="cookies.json")
    conversation_id = chatbot_instance.new_conversation()  # Initialize a new conversation
    response = chatbot_instance.chat(user_input)
    print(response)
    return response


# ========================================================GREET FUNCTION================================================================================================================================================================================================================================================



# Starts an infinite loop (while True:) where it continuously listens for user input (query = takeCommand().lower()).
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()     # Calls the takeCommand() function to capture a command from the user and converts it to lowercase (lower() method).
        if "get up" in query:
            from GreetMe import greetMe      #Imports the greetMe function from the GreetMe module. This likely handles the initial greeting or activation sequence for the AI assistant.
            greetMe()                        #Calls the greetMe function to perform actions such as greeting the user or initializing the assistant.

            while True:                    #while True:: Starts another infinite loop within the if "get up" in query: block, indicating that the assistant is now actively listening for subsequent commands after waking up.
                query = takeCommand().lower()       #Captures a new command from the user.
                if "go to sleep" in query:          #if "go to sleep" in query:: Checks if the string "go to sleep" is present in the query.
                    speak("Ok Ma'am , You can call me anytime")   #Uses the speak() function to verbally confirm to the user that the assistant is going to sleep mode. 
                    break                           #Exits the inner while True: loop, returning the program control to the outer loop where it resumes listening for "get up" command.


# =========================================================CHANGE PASSWORD==============================================================================================================================================================================================================================================================


                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done ma'am ")
                    speak(f"Your new password is{new_pw}")
                    
# =========================================================SCHEDULE MY DAY==============================================================================================================================================================================================================================================================

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

# =========================================================SHOW MY SCHEDULE USING DESKTOP NOTIFICATION==============================================================================================================================================================================================================================================================

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )
                


                    

#========================================================================IPL SCORE================================================================================================================================================================================================================================================================================== 

                # elif "ipl score" in query:
                #     from plyer import notification  #pip install plyer
                #     import requests #pip install requests
                #     from bs4 import BeautifulSoup #pip install bs4
                #     url = "https://www.cricbuzz.com/"
                #     page = requests.get(url)
                #     soup = BeautifulSoup(page.text,"html.parser")
                #     team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                #     team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                #     team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                #     team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                #     a = print(f"{team1} : {team1_score}")
                #     b = print(f"{team2} : {team2_score}")

                #     notification.notify(
                #         title = "IPL SCORE :- ",
                #         message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                #         timeout = 15
                #     )

# ==================================================================PLAY A GAME==========================================================================================================================================================================================================================================================

                elif "play a game" in query:
                    from game import game_play
                    game_play()

# ==================================================================SCREENSHOT FUNCTION==================================================================================================================================================================================================================================================                

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

# ==================================================================CLICK A PHOTO==================================================================================================================================================================================================================================================

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")


# ==================================================================TRANSLATE==================================================================================================================================================================================================================================================



                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)   


# ============================================================OPEN ANY APP USING JARVIS================================================================================================================================================================================================================================================

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 

# ============================================================INTERNET SPEED================================================================================================================================================================================================================================================


                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                
# =========================================================CONVERSATIONS==============================================================================================================================================================================================================================================================

                elif "hello" in query:            #Checks if the string "hello" is present in the query (the user's spoken command).
                    speak("Hello Ma'am, how are you ?")   #Uses the speak() function to have the assistant greet the user and ask how they are doing 
                elif "i am fine" in query:        #Checks if the string "i am fine" is present in the query.
                    speak("that's great, Ma'am")    #Responds positively to the user indicating they are fine.
                elif "how are you" in query:      #Checks if the string "how are you" is present in the query.
                    speak("Perfect, Ma'am")         #Responds with a positive affirmation that the assistant is doing well.
                elif "thank you" in query:        #Checks if the string "thank you" is present in the query.
                    speak("you are welcome, Ma'am") #Responds with a polite acknowledgment to the user's gratitude.


#=========================================================================PLAYLIST====================================================================================================================================================================================================================================================
                elif "tired" in query:
                    speak("Playing your favourite songs, Ma'am")
                    a = (1, 2, 3)  # You can choose any number of songs (I have only chosen 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://youtu.be/rd1bbljtpds?si=MVFTVDJT3HgkUuWe")
                    elif b == 2:
                        webbrowser.open("https://youtu.be/KUN5Uf9mObQ?si=8_GiGKdgCsUs8e_j")                    
                    elif b == 3:
                        webbrowser.open("https://youtu.be/HfMTwkVQohM?si=TWIiH586Q8CLnl5O")
                                                                                                                                                


# ============================================================FULLY AUTOMATE YOUTUBE CONTROLS===========================================================================================================================================================================================================================================
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, Ma'am")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, Ma'am")
                    volumedown()

#========================================================OPEN AND CLOSE APPS============================================================================================================================================================================================================================================================
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)    

#========================================================YOUTUBE, WIKIPEDIA AND GOOGLE SEARCH==========================================================================================================================================================================================================================================

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

#====================================================================NEWS=======================================================================================================================================================================================================================================================                

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

#====================================================================CALCULATOR=======================================================================================================================================================================================================================================================                

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
#====================================================================WHATSAPP AUTOMATION#====================================================================#====================================================================#====================================================================#================================
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

#====================================================================TEMPERATURE=======================================================================================================================================================================================================================================================                
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

# #=========================================================================SET AN ALARM#=============================================================================================================================================================================================================================#======================

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,Ma'am")


#=========================================================================TIME===============================================================================================================================================================================================================================================================
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Ma'am, the time is {strTime}")


                elif "jarvis" in query:
                    print("yes ma'am ")
                    speak("yes ma'am")

                elif "type" in query:
                    query = query.replace("type", "")
                    pyautogui.typewrite(f"{query}",0.1)   
# =====================================================================HOTWARD DIRECTION====================================================================================================================================================================================================================================================
                elif "finally sleep" in query:
                    speak("Going to sleep,Ma'am")
                    exit() 


#=========================================================================REMINDER==========================================================================================================================================================================================================================================================
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")  # Remove "remember that" from the query
                    rememberMessage = rememberMessage.replace("jarvis", "")  # Remove "jarvis" from the query (if present)
                    speak("You told me " + rememberMessage)  # Speak back the message that was remembered
                    with open("Remember.txt", "a") as remember:  # Open the file in append mode
                       remember.write(rememberMessage + "\n")  # Write the remembered message to the file

                
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())
                    
                    
#==================================================================SHUT DOWN THE SYSTEM============================================================================================================================================================================================================================================ 
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
# ============================================Custom responses for specific queries===============================================================================================================================================================================================================================================
                elif "who are you" in query:  # Answer for "Who are you?"
                    speak("My name is Jarvis. I am your desktop assistant. Feel free to ask for help.")
                elif "who made you" in query: # Answer for "Who made you?"
                    speak("I was made by Jhanani, a final year BTECH AI student from Velammal Engineering College")
                elif "what are you doing" in query:  # Answer for "Who made you?"
                    speak("I'm here to help you mam")
                elif "did you eat" in query:
                    speak("I don't eat since I'm not a biological entity and don't have a physical form! I'm here 24/7 ready to assist with any questions or topics you'd like to discuss. What's on your mind today?")
                elif "where are you?" in query:
                    speak("As a desktop Assistant, I exist in your laptop, providing responses and information whenever you interact with me.")

# ============================================IP ADDRESS==============================================================================================================================================================================================================================================================================
                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    query = query.replace("jarvis","")
                    speak(f"your IP address is {ip}")
                
# ================================================CHATBOT==============================================================================================================================================================================================================================================================================

                else:
                    response = chatbot(query)
                    speak(response)






                




