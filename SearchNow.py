import speech_recognition   #For recognizing speech input from the microphone.
import pyttsx3              #For text-to-speech conversion and audio output.
import pywhatkit            #For performing Google searches and playing YouTube videos.
import wikipedia            #For fetching information from Wikipedia.
import webbrowser           #For opening URLs in the default web browser.


def takeCommand():
    r = speech_recognition.Recognizer()                  #Initializes a Recognizer object r from speech_recognition.
    with speech_recognition.Microphone() as source:      #Opens the microphone (Microphone context manager) to capture audio (source).
        print("Listening.....")                          
        r.pause_threshold = 1                            #Sets pause_threshold (seconds of non-speaking audio before a phrase is considered complete) 
        r.energy_threshold = 300                         #energy_threshold (minimum audio energy to consider for capturing speech).
        audio = r.listen(source,0,4)                     #Captures audio using r.listen(source, 0, 4) (listens for up to 4 seconds or until silence is detected).
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')     #Uses recognize_google to convert the captured audio into text (query) using the English (India) language.
        print(f"You Said: {query}\n")                           #Prints the recognized query and returns it.

    except Exception as e:
        print("Say that again")                                  
        return "None"                                           #If speech recognition fails (raises an exception), it prints an error message and returns "None".
    return query

query = takeCommand().lower()                                   #Calls the takeCommand() function to capture user input and converts it to lowercase (lower() method).
                                                                #This query variable will be used to determine what action to perform based on the user's voice command.

engine = pyttsx3.init("sapi5")                                  #Initializes the engine using init("sapi5"), which uses the Microsoft Speech API.
voices = engine.getProperty("voices")                           #engine.getProperty("voices") is a method in pyttsx3 that fetches the list of available voice profiles from the initialized TTS engine (engine).
engine.setProperty("voice", voices[0].id)                       #setProperty("voice", voices[0].id) sets the voice property of the engine to the first voice in the voices list. Each voice object has an id attribute that uniquely identifies it.
engine.setProperty("rate",170)                                  #setProperty("rate", 170) sets the speaking rate of the engine to 170 words per minute. This adjusts how fast or slow the text is spoken.

def speak(audio):                                               #speak() Function:
                                                                # Purpose: Converts text (audio) into speech and speaks it aloud.
    
    
    engine.say(audio)                                           #to queue the text to be spoken.
    engine.runAndWait()                                         #blocks execution until all currently queued commands are processed and the speech is completed.

def searchGoogle(query):                                        #searchGoogle(query) Function:
                                                                # Purpose: Searches Google for the provided query and speaks the summary using pywhatkit and wikipedia libraries.


    if "google" in query:                                       #Checks if "google" is in the query (indicating a Google search request).       
        import wikipedia as googleScrap                         #Imports wikipedia as googleScrap to use its summary() function.
        query = query.replace("jarvis","")                      #Cleans the query string by removing specific keywords ("jarvis", "google search", "google").
        query = query.replace("google search","")               #Cleans the query string by removing specific keywords ("jarvis", "google search", "google").
        query = query.replace("google","")                      #Cleans the query string by removing specific keywords ("jarvis", "google search", "google").
        speak("This is what I found on google")                 

        try:
            pywhatkit.search(query)                             #Uses pywhatkit.search() to perform the Google search.
            result = googleScrap.summary(query,1)               #Retrieves a summary of the search results using googleScrap.summary() and speaks it.
            speak(result)                                       

        except:
            speak("No speakable output available")              #Handles exceptions if no speakable output is available.

def searchYoutube(query):
    if "youtube" in query:                                      #Checks if "youtube" is in the query (indicating a YouTube search request).
        speak("This is what I found for your search!")          
        query = query.replace("youtube search","")                        #Cleans the query string by removing specific keywords ("youtube search", "youtube", "jarvis").
        query = query.replace("youtube","")                               #Cleans the query string by removing specific keywords ("youtube search", "youtube", "jarvis").
        query = query.replace("jarvis","")                                #Cleans the query string by removing specific keywords ("youtube search", "youtube", "jarvis").
        web  = "https://www.youtube.com/results?search_query=" + query    #Constructs the YouTube search URL (web).
        webbrowser.open(web)                                              #Opens the search results URL in the default web browser (webbrowser.open(web)).
        pywhatkit.playonyt(query)                                         #Plays the top result using pywhatkit.playonyt(query).
        speak("Done, Ma'am")                                                # Speaks "Done, Ma'am" to indicate completion.

def searchWikipedia(query):
    if "wikipedia" in query:                                              #Checks if "wikipedia" is in the query (indicating a Wikipedia search request).
        speak("Searching from wikipedia....")                             
        query = query.replace("wikipedia","")                             #Cleans the query string by removing specific keywords ("wikipedia", "search wikipedia", "jarvis").
        query = query.replace("search wikipedia","")                      #Cleans the query string by removing specific keywords ("wikipedia", "search wikipedia", "jarvis").
        query = query.replace("jarvis","")                                #Cleans the query string by removing specific keywords ("wikipedia", "search wikipedia", "jarvis").
        results = wikipedia.summary(query,sentences = 2)                  #Retrieves a summary of the search results using wikipedia.summary() with sentences=2 (returns the first two sentences).
        speak("According to wikipedia..")                                 #Speaks "According to Wikipedia.." followed by the summary.
        print(results)                                                    #Prints the summary to the console.
        speak(results)                                                    #Speaks "According to Wikipedia.." followed by the summary.
