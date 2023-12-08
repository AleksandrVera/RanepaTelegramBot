import telebot

import methods

import config

bot = telebot.TeleBot(config.TOKEN)
#создаем объект телебот с указанным токеном

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,"привет!")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text.lower()=="привет":
        bot.send_message(message.chat.id,methods.greet())
    elif message.text.lower().replace(' ','').strip('?')=="какдела":
        bot.send_message(message.chat.id,methods.how_are_you())

if __name__=="__main__":
      bot.polling(none_stop=True, interval=0)