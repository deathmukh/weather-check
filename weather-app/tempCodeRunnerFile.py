import requests

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=d49a677ceb774e53a90133824232707&q={city}"

r = requests.get(url)
print(r.text)