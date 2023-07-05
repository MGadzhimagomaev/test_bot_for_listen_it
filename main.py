import os
from background import keep_alive #importing function for operability
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
from youtube_video_link import get_best_matching_video_title_w_link

bot = telebot.TeleBot('5627699899:AAFaLVlJZoIElsGb4YYDf_a55YEJ9WnN88w')

@bot.message_handler(content_types=['text'])
def welcome(message):
  if message.text == '/start':
    sent_msg = bot.send_message(message.chat.id, "Привет! Введи поисковой запрос.")
  else:
    find_yt_video(message) #Next message will call the name_handler function
    
def find_yt_video(message):
  yt_video_title_dict = get_best_matching_video_title_w_link(message.text)
  if not yt_video_title_dict:
    text = "Не найдено ни одного видео. Попробуй уточнить поисковой запрос."
    bot.send_message(chat_id=message.from_user.id, \
                      text=text
                      )
  else:
    for title, link in yt_video_title_dict.items():
        text = '<a href="'+link+'">'+title+'</a>'

        bot.send_message(chat_id=message.from_user.id, \
                         text=text, \
                         parse_mode='HTML'
                        )

keep_alive()#launching flask-server in separate stream
bot.polling(non_stop=True, interval=0) #launching bot'