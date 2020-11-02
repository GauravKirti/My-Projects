import pyttsx3
import datetime
import webbrowser
import os
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 150) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time is")
    print(time)
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today is")
    print(f"Today is {date}/{month}/{year}")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back sir!")
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Sam at your service. How can I help you?")
    
def takeCommand():
    query = input("Please type your command: ")
    return query
    
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "quit" in query or "stop" in query:
            speak("Quitting! Bye-Bye Sir. Hope to serve you soon!")
            quit()
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif "chrome" in query:
            os.system("chrome")
        elif "editor" in query or "notepad" in query or "text editors" in query:
            os.system("notepad")
        elif "wikipedia" in query:
            print("Searching.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak("Found the following information at wikipedia")
            speak(result)
            print(result)
        elif "remember" in query:
            speak("Tell the thing to remember")
            data = takeCommand()
            speak("You said to remember"+data)
            remember = open("data.txt", 'w')
            remember.write(data)
            remember.close()
        else:
            print("Could not understand.")
            speak("Please try again")