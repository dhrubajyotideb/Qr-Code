import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error recognizing your voice.")
        return ""

if name == "__main__":
    speak("Hello, I am your voice assistant. What should I call you?")
    name = listen()

    speak(f"Nice to meet you, {name}!")

    speak("How can I assist you today?")
    
    while True:
        user_input = listen()
        
        if "hello" in user_input:
            speak("Hello! How can I assist you?")
        elif "bye" in user_input:
            speak("Goodbye!")
            break
        else:
            speak("I didn't quite get that. Could you repeat?")