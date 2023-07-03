import os
from background import keep_alive #importing function for operability
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
from youtube_video_link import get_best_matching_video_header, get_best_matching_video_link

bot = telebot.TeleBot('5627699899:AAFaLVlJZoIElsGb4YYDf_a55YEJ9WnN88w')

@bot.message_handler(content_types=['text'])

def get_text_message(message):
  video_link = get_best_matching_video_link(message.text)
  video_header = get_best_matching_video_header(message.text)
  if video_header is None:
    text = "Не найдено ни одного видео.\
    Попробуйте уточнить поисковой запрос."
  else:
    text = '<a href="'+video_link+'">'+video_header+'</a>'

  # message_entities = {MessageEntities(length=6, offset=5)}
  bot.send_message(chat_id=message.from_user.id, \
                   text=text, \
                   parse_mode='HTML'
                  )

keep_alive()#launching flask-server in separate stream
bot.polling(non_stop=True, interval=0) #launching bot'