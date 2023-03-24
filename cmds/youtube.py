import pywhatkit as kit
import sys
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def play_youtube_video(video):
    video_url = kit.playonyt(video)

r = sr.Recognizer()

def mic():
    global text
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Search For Youtube Video...")
        # listen for audio and store it in a variable
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # recognize the speech in the audio
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        return text
    except sr.UnknownValueError:
        # handle speech that couldn't be recognized
        print("Sorry, I couldn't understand what you said")
    except sr.RequestError as e:
        # handle errors with the API
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":

    

    query = mic()
    play_youtube_video(query)
    print("Playing video: "+query)
    engine.say("Playing video: "+query)
    engine.runAndWait()