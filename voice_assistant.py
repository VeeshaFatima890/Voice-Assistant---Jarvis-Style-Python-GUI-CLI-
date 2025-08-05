import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import sys

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)       # Speed
engine.setProperty('volume', 1.0)     # Volume

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that. Could you repeat?")
        return "none"
    except sr.RequestError:
        speak("Speech recognition service is down.")
        return "none"

def run_jarvis():
    wish_user()
    
    while True:
        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia:")
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")
            except:
                speak("Couldn't fetch Wikipedia results.")
        
        elif "youtube" in query:
            speak("Opening YouTube...")
            pywhatkit.playonyt(query.replace("youtube", "").strip())

        elif "google" in query:
            speak("Searching Google...")
            pywhatkit.search(query.replace("google", "").strip())

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif "exit" in query or "bye" in query or "stop" in query:
            speak("Goodbye! Have a great day.")
            sys.exit()

        elif query != "none":
            speak("Sorry, I can't help with that yet.")
