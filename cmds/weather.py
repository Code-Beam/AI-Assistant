import json
import requests
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def weather(city):

    # API base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    # City Name
    CITY = city

    # Your API key
    API_KEY = "ab3a13c5b56d9d9af5935191138376c4"

    # updating the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"

    # Sending HTTP request
    response = requests.get(URL)

    # checking the status code of the request
    if response.status_code == 200:
        
        # retrieving data in the json format
        data = response.json()
        
        # take the main dict block
        main = data['main']
        
        # getting temperature
        temperature = main['temp']
        # getting feel like
        temp_feel_like = main['feels_like']  
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        
        # weather report
        weather_report = data['weather']
        # wind report
        wind_report = data['wind']
        
        print(f"{CITY:-^35}")
        print(f"City ID: {data['id']}")   
        print(f"Temperature: {temperature} degree celsius")
        print(f"Feels Like: {temp_feel_like} degree celsius")    
        print(f"Humidity: {humidity} percent")
        print(f"Pressure: {pressure} hPA")
        print(f"Weather Report: {weather_report[0]['description']}")
        print(f"Wind Speed: {wind_report['speed']} meters per second")
        print(f"Time Zone: {data['timezone']}")

        engine.say(f"{CITY:-^35}")
        engine.runAndWait()
        engine.say(f"City ID: {data['id']}")   
        engine.runAndWait()
        engine.say(f"Temperature: {temperature} degree celsius")
        engine.runAndWait()
        engine.say(f"Feels Like: {temp_feel_like} degree celsius")    
        engine.runAndWait()
        engine.say(f"Humidity: {humidity} percent")
        engine.runAndWait()
        engine.say(f"Pressure: {pressure} hPA")
        engine.runAndWait()
        engine.say(f"Weather Report: {weather_report[0]['description']}")
        engine.runAndWait()
        engine.say(f"Wind Speed: {wind_report['speed']} meters per second")
        engine.runAndWait()
        engine.say(f"Time Zone: {data['timezone']}")
        engine.runAndWait()

    else:
        # showing the error message
        print("Error in the HTTP request")
        engine.say("Error in the HTTP request")
        engine.runAndWait()

if __name__ == "__main__":

    ip_request = requests.get('https://api.ipify.org?format=json')
    ip_address = ip_request.json()['ip']

    # Use IP address to get user's location
    location_request_url = f'http://ip-api.com/json/{ip_address}'
    location_request = requests.get(location_request_url)
    location_data = location_request.json()

    # Extract relevant location information
    c = location_data['city']
    weather(c)