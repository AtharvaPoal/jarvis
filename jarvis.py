import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    except Exception as e:
        print("Please say again!")
        return "None"
    return query

def greeting():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")


if __name__=="__main__":
    greeting()
    speak("this is your desktop assistant ")
    speak("how may i help you")
    speak("to exit any time say thank you")
    end=False
    while not end:
        query=take_command().lower()
        if 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            print(results)
        elif 'open geeksforgeeks' in query:
            speak("Opening youtube")
            webbrowser.open("geeksforgeeks.com")
        elif 'time' in query:
            str_time=datetime.datetime.now().strftime("%H:%M:%S")
            s="The time is"+str_time
            speak(s)
        elif 'movies' in query:
            movies_dir="E:\\Movies"
            movies=os.listdir(movies_dir)
            speak("Select movie number to play from the given list")
            print(movies)
            query=int(take_command())
            os.startfile(os.path.join(movies_dir,movies[query]))
        elif 'old photos' in query:
            photos_dir="E:\\Old Photos\\Home"
            photos=os.listdir(photos_dir)
            os.startfile(os.path.join(photos_dir,photos[0]))
        elif 'play songs' in query:
            song_dir="E:\\old songs\\A"
            songs=os.listdir(song_dir)
            query=int(take_command())
            os.startfile(os.path.join(song_dir,songs[query]))
        elif 'khichdi' in query:
            tv_dir="F:\\TV Series\\Khichdi"
            khichdi=os.listdir(tv_dir)
            speak("Episode number of khichdi")
            query=int(take_command())
            os.startfile(os.path.join(tv_dir,khichdi[query]))
        elif 'rafi' in query:
            webbrowser.open("https://www.youtube.com/watch?v=uMWRl5c1brI")
        elif 'kishore kumar' in query:
            webbrowser.open("https://www.youtube.com/watch?v=0iN6O3-8mLY")
        elif 'college portal' in query:
            webbrowser.open("http://portal.medicaps.ac.in/accsoft2/Studentlogin.aspx")
        elif 'name' in query:
            speak("My name is jarvis")
        elif 'thank you' in query:
            speak("Welcome")
            end=True
