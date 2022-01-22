import requests, json
import os
city_name = input("Enter city name : ")

#api_key = 'e7b584346f23143bbedc4bcded85ae63'
#url = "http://api.openweathermap.org/data/2.5/weather?"
#complete_url = url + "&q=" + city_name + "appid=" +api_key
complete_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.environ.get("api_kye")}'

response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    print(x["main"]["temp"])
    print(x["main"]["pressure"])
    print(x["wind"]["speed"])
    print(x["wind"]["deg"])
else:
    print(" City Not Found ")