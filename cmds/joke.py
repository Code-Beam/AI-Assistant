import requests
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

response = requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()

if __name__ == '__main__':
    print(data["setup"])
    engine.say(data["setup"])
    engine.runAndWait()
    print(data["punchline"])
    engine.say(data["punchline"])
    engine.runAndWait()