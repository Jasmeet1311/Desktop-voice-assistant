import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #object creation
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    """ speak method will speak the inputted text"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """wishme will greet you first and then give introduction about
    itself."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    
    speak("I am  Elza    Please tell how may I help you?")
def nextTask():
    speak("I am ready to perform my next task")

def takeCommand():
    """It takes microphone input from the user and return a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        r.pause_threshold = 1
        r.energy_threshold=100
        r.adjust_for_ambient_noise(source,duration=0.5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__ =="__main__":
    wishme()
    while 1:
        nextTask()
        query = takeCommand().lower()
        # Logic for executing task based on the query

        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow"  in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir ='F:\\My Music\\Fav song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
            print(strtime)
        elif "open code" in query:
            code_path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif "open chrome" in query:
            code_path ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code_path) 
        elif "quit" in query:
            exit()

