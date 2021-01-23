from time import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
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
    server.login('anandparth06124@gmail.com','Parth&jaia')
    server.sendmail('anandparth06124@gmail.com',to,content)
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
        if 'time' in task:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
        if 'date' in task:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("The current date is")
            speak(date)
            speak(month)
            speak(year)
        if 'google' in task:
            webbrowser.open("www.google.com")
        if 'youtube' in task:
            webbrowser.open("www.youtube.com")
        if 'brave' in task:
            bravepath = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"
            speak("opening brave")
            os.startfile(bravepath)
        if 'send email' in task:
            try:
                speak("What shoul i say sir?")
                content = takeCommand()
                to = 'anandparth06124@gmail.com'
                sendemail(to,content)
                speak("Email has been sent sir")
            except Exception as e:
                print(e)
                speak("Sorry sir I am not able to send this email")









            






if __name__ == "__main__":
    wismme()
    takeCommand()
    taskExecution()

    #speak("Subscribe to Learn Coding With fun")

