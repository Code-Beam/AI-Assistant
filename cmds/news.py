import requests
import datetime
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Your API key goes here
API_KEY = '357c05960668410b961ad624be136ef2'

# Today's date in ISO format
today = datetime.date.today().isoformat()

# URL for the top headlines endpoint
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}&pageSize=25&page=1&category=general&from={today}'

# Send a GET request to the News API and store the response
response = requests.get(url)

# Parse the response JSON
data = response.json()

# Print each headline to the console

if __name__ == "__main__":
    for article in data['articles']:
        print(article['title'])
        engine.say(article['title'])
        engine.runAndWait()