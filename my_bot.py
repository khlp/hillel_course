import telebot
import wikipedia
import re

token = '5169331148:AAGOGLquSrhi05EmqXf_JWCHYz7fLWP48aU'
bot = telebot.TeleBot(token)
requests_history = {}

# set language for Wikipedia
wikipedia.set_lang("en")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов

def getwiki(s):
    try:


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f"Hi ✌️{m.chat.first_name}. Send me any word and I will find its meaning on Wikipedia")
# get message from user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# run bot
bot.polling(none_stop=True, interval=0)