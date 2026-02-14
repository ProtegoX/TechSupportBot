from config import BOT_TOKEN
import telebot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hi, I'm a tech support bot! \nAsk me a question and I will try to answer.")

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, "You can describe your broblem by sendning a text or an audio message.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)