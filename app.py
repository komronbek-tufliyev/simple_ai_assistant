import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import shutil
import wikipedia
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your personal assistant. Hahzel 1 point 0")


def username():
    speak("What is your name?")
    name = take_command()
    if name == "None":
        speak("I didn't get that. Please try again.")
    else:
        speak(f"Welcome Mister {name}")
        columns = shutil.get_terminal_size().columns
        print("############################".center(columns))
        print("Welcome to Hahzel, Sir " + name.center(columns))
        print("############################".center(columns))
        
    speak("How can I help you, Sir?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

def open_telegram():
    path = "C:\\Users\\kamro\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
    os.startfile(path)

if __name__=="__main__":
    clear = lambda: os.system('cls')
    exit = lambda: os.system('exit()') 

    clear()
    greeting()
    username()

    print("Dasturning asosiy qismi ishga tushmoqda...") 
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'E:\\downloads\\Telegram Desktop( currently in use )'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open telegram' in query:
            open_telegram()
            speak("Opening Telegram")

        elif 'joke' in query:
            joke = str(pyjokes.get_joke())
            speak(joke)

        elif 'open vs code' in query:
            speak("Opening VS Code")
            os.system('code')

        elif 'exit' in query:
            speak("Bye Sir, have a good day.")
            exit()
        
        else:
            speak("I didn't get that. Please try again.")
            print("I didn't get that. Please try again.")
            
        continue

        speak("How can I help you, Sir?")


        
