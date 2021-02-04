from time import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import smtplib
import diction
import time
from diction import *
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
    speak("What can I do for you sir?")
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail address','password')
    server.sendmail('address whom you want to send',to,content)
    server.close()
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

def taskExecution():
    while True:
        task = takeCommand()
        if 'wikipedia' in task:
            speak("Searching wikipedia....")
            task = task.replace("wikipedia","")
            results = wikipedia.summary(task,sentences = 2)
            speak(results)
        elif 'time' in task:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
        elif 'date' in task:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("The current date is")
            speak(date)
            speak(month)
            speak(year)
        elif 'google' in task:
            webbrowser.open("www.google.com")
        elif 'youtube' in task:
            webbrowser.open("www.youtube.com")
        elif 'brave' in task:
            bravepath = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"
            speak("opening brave")
            os.startfile(bravepath)
        elif 'send email' in task:
            try:
                speak("What shoul i say sir?")
                content = takeCommand()
                to = 'address whom you want to send'
                sendemail(to,content)
                speak("Email has been sent sir")
            except Exception as e:
                print(e)
                speak("Sorry sir I am not able to send this email")
        elif 'hide files'in task or 'hide all folders' in task or 'visible' in task or 'hide' in task:
                condition = takeCommand().lower()
                if 'hide' in condition:
                    os.system("attrib +h /s /d")
                    speak("sir, your files are hidden now")
                elif 'visible' in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, your files are visible now")
                elif 'leave it' in condition:
                    speak("ok sir as you wish")

        elif 'take screenshot' in task:
                speak("sir, Please tell me the name for screenshot file")
                name = takeCommand().lower()
                speak("sir please hold screen for few seconds to take the screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, screenshot is ready in file")
                    

        elif 'dictionary' in task:
            speak("Sir what would you like to search in your intelligent dictionary")
            translate(takeCommand())







            






if __name__ == "__main__":
    wismme()
    takeCommand()
    taskExecution()


