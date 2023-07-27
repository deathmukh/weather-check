import requests
import json

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=d49a677ceb774e53a90133824232707&q={city}"
    r = requests.get(url)
    return json.loads(r.text)

while True:
    city = input("Enter the name of the city (or 'exit' to quit): ")

    if city() == "exit":
        break

    try:
        weatherDict = get_weather(city)
        print(f"The temperature in {city} is {weatherDict['current']['temp_c']} degree Celsius")
    except KeyError:
        print(f"Could not find weather data for {city}. Please try again.")
