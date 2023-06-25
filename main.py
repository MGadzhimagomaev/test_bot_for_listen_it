import os
from background import keep_alive #importing function for operability
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time

bot = telebot.TeleBot('5627699899:AAFaLVlJZoIElsGb4YYDf_a55YEJ9WnN88w')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  bot.send_message(message.from_user.id,message.text)
# echo-func, that replies any message with simila message   

keep_alive()#launching flask-server in separate stream
bot.polling(non_stop=True, interval=0) #launching bot