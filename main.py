import os
from background import keep_alive #importing function for operability
import pip
pip.main(['install', 'pytelegrambotapi'])
# pip.main(['install', 'google-api-python-client'])
import telebot
import time
from youtube_video_link import get_best_matching_video

bot = telebot.TeleBot('5627699899:AAFaLVlJZoIElsGb4YYDf_a55YEJ9WnN88w')

@bot.message_handler(content_types=['text'])

def get_text_message(message):
  reply = get_best_matching_video(message.text)
  bot.send_message(message.from_user.id, reply)

keep_alive()#launching flask-server in separate stream
bot.polling(non_stop=True, interval=0) #launching bot'