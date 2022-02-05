import wikipedia
wikipedia.set_lang("en")
print(wikipedia.page("culture").categories[0])


import telebot
import requests, json

token = '5169331148:AAGOGLquSrhi05EmqXf_JWCHYz7fLWP48aU'
bot = telebot.TeleBot(token)
requests_history = {}

def get_weather(city):
    weather_map = {'rain': '⛈', 'sun': '🌞', 'fog': '🌫', 'snow': '❄'}
    weather_responce = requests.request('GET',
                                        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=290e116e45216d44eb680ac8a3adba2f&units=metric')
    if weather_responce.status_code != 200:
        return 'unknown'
    else:
        weather_json = weather_responce.json()
        if weather_json['weather'][0]['id'] < 600:
            weather_icon = weather_map['rain']
        elif 600 >= weather_json['weather'][0]['id'] < 700:
            weather_icon = weather_map['snow']
        elif 700 >= weather_json['weather'][0]['id'] < 800:
            weather_icon = weather_map['fog']
        else:
            weather_icon = weather_map['sun']
        current_weather = f'''Current weather in {city}:
      Temperatue: {weather_json['main']['temp']}
      Feels like: {weather_json['main']['feels_like']}
      {weather_icon}
      '''
        return current_weather

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, f"Привет ✌️{message.chat.first_name}")

@bot.message_handler(regexp=".*")
def any_message(message):
  print(message)
  current_history = requests_history.get(message.from_user.id, [])
  current_history.append(message.text)
  requests_history[message.from_user.id] = current_history
  bot.send_message(message.chat.id, get_weather(message.text))

bot.infinity_polling()