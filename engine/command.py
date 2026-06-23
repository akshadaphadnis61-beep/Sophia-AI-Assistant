import time
import eel
import pyttsx3
import speech_recognition as sr
from engine.ai import ask_ai

from engine.features import *

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    engine = pyttsx3.init()

@eel.expose
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")

        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print("Listen Error:", e)
            return ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")

        print("User said:", query)
        eel.DisplayMessage(query)

        return query.lower()

    except Exception as e:
        print("Recognition Error:", e)
        return ""



@eel.expose
def stopAssistant():
    stop_speaking()

def start_listening():
    while True:
        query = takeCommand()

        if not query:
            continue

        print("Query:", query)

        # process query here
@eel.expose
def allCommands(query=None):
    print("allCommands called")
    print("Query received:", query)
 
    if not query:
      query = takeCommand()
     

    if not query:
        return

    print("Query:", query)

    if "open" in query:
        openCommand(query)
        eel.ShowHood()

    elif "youtube" in query:
        PlayYoutube(query)
        eel.ShowHood()

    elif "search" in query:
        GoogleSearch(query)
        eel.ShowHood()

    elif "time" in query:
        current = tellTime()
        speak(f"The time is {current}")
        eel.ShowHood()

    elif "who is" in query:
        result = WikiSearch(query.replace("who is", ""))
        speak(result)
        eel.ShowHood()

    else:
         answer = ask_ai(query)
         print(answer)
         speak(answer)
         speak("anything else i can help")
         eel.ShowHood()
         