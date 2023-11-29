import telebot

import methods

TOKEN= '6589015019:AAF7XvRp-T24jrtkgqeLAav4Liuj4GGHCLQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,"привет!")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text.lower()=="Привет":
        bot.send_message(message.chat.id,methods.greed())
    elif message.text.lower()=="как дела?":
        bot.send_message(message.chat.id,methods.how_are_you())

if __name__=="__main__":
      bot.polling(none_stop=True, interval=0)