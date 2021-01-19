from time import time
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def wismme():
    hour = int(datetime.datetime.now().hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%H:%M:%S")

    if hour>=6 and hour<12:
        speak("Good Morning sir")
    if hour>=12 and hour<18:
        speak("Good Afternoon sir")
    if hour>=18 and hour<24:
        speak("Good Evening sir")
    speak(date)
    speak(month)
    speak(year)
    speak(Time)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        task = r.recognize_google(audio,language = 'en-in')
        print(f"Sir said:{task}")
    except Exception as e:
        print(e)
        return"None"
    task = task.lower()
    return task




if __name__ == "__main__":
    wismme()
    takeCommand()
    speak("Subscribe to Learn Coding With fun")
