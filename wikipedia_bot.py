import telebot
import wikipedia

token = '5192952990:AAGGRlsFdt1-95FjirwKD4QlZxeekRjIE5I'
bot = telebot.TeleBot(token)

# set language for Wikipedia
wikipedia.set_lang("en")

def getwiki(s):
    try:
        wikitext=wikipedia.summary(s, sentences=2)
        # wikipedia.page(s).url --- cann't show link in telegram bot??
        return wikitext
    except Exception as e:
        return 'Wikipedia has no information about it. Please check your word again.'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f"Hi ✌️{m.chat.first_name}. Send me any word and I will find its meaning on Wikipedia")
# get message from user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# run bot
bot.polling(none_stop=True, interval=0)