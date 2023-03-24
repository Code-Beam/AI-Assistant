import os
import speech_recognition as sr

r = sr.Recognizer()

def mic():
    
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        # listen for audio and store it in a variable
        audio = r.listen(source, 10, 15)

    # recognize speech using Google Speech Recognition
    try:
        # recognize the speech in the audio
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        return text
    except sr.UnknownValueError:
        # handle speech that couldn't be recognized
        print("Sorry, I couldn't understand what you said")
        mic()
    except sr.RequestError as e:
        # handle errors with the API
        print(f"Could not request results from Google Speech Recognition service; {e}")

while True:

    #user_input = input("Enter a command: ")
    #user_input = user_input.lower()

    user_input = mic()
    user_input = user_input.lower()

    if "record" in user_input:
        os.system("python cmds/record.py")
    if "news" in user_input:
        os.system("python cmds/news.py")
    elif "joke" in user_input:
        os.system("python cmds/joke.py")
    elif "youtube" in user_input:
        os.system("python cmds/youtube.py")
    elif "weather" in user_input:
        os.system("python cmds/weather.py")
    elif user_input == "quit":
        break
    else:
        os.system(f"python cmds/chatgpt.py {user_input}")
