
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import requests

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"
        return query

def search_web(query):
    search_result = pywhatkit.search(query.lstrip('search '))
    return search_result

def get_wiki_summary(query):
    summary = wikipedia.summary(query.lstrip('wikipedia '), sentences=2)
    return summary

if __name__ == "__main__":
    while True:
        query = listen().lower()
        if 'hello' in query:
            speak('Hello! How can I assist you?')
        elif 'search' in query:
            search_result = search_web(query)
            speak('Here are the search results:')
            speak(search_result)
        elif 'wikipedia' in query:
            summary = get_wiki_summary(query)
            speak('Here is the summary from Wikipedia:')
            speak(summary)
        elif 'exit' in query:
            speak('Goodbye!')
            break