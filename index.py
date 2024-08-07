import telebot
import requests
from settings import *
bot = telebot.TeleBot(tg_token)

@bot.message_handler(commands=['find'])
def send_welcome(message):
	post_user = requests.get(f"http://127.0.0.1:5000/{message.text.split(' ')[1]}/")
	bot.reply_to(message, post_user)

bot.infinity_polling()