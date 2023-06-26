import os
from background import keep_alive #importing function for operability
import pip
pip.main(['install', 'pytelegrambotapi'])
pip.main(['install', 'google-api-python-client'])
import telebot
import time
from googleapiclient.discovery import build

bot = telebot.TeleBot('5627699899:AAFaLVlJZoIElsGb4YYDf_a55YEJ9WnN88w')

#YouTube API block - pulling all video names from channel
google_api_key = 'AIzaSyCDn75CAh9m0Gu8WK6nvasFMdqR-von_s0'
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'

youtube = build(youtube_api_service_name, youtube_api_version, developerKey=google_api_key, static_discovery=False)
channel_id = '@ListenIT_channel'

# request = youtube.search().list(
#   part='id',
#   channelId=channel_id,
#   type='video',
#   order='date'
# )

def get_video_details(youtube, **kwargs):
    return youtube.videos().list(
        part="snippet,contentDetails,statistics",
        **kwargs
    ).execute()

def search(youtube, **kwargs):
    return youtube.search().list(
        part="snippet",
        **kwargs
    ).execute()


    # print the video details
    # print_video_infos(video_response)
    # print("="*50)

# def import_channel_videos(channel_id):
#     request = youtube.search().list(part='id', type='video', channelId=channel_id, maxResults=50)
#     response = request.execute()
    # video_ids = [item['id']['videoId'] for item in response['items']]
    # video_details = get_video_details(video_ids)
    # for item in video_details:
    #     video = Video(id=item['id'], title=item['snippet']['title'], description=item['snippet']['description'], published_at=item['snippet']['publishedAt'], thumbnail=item['snippet']['thumbnails']['default']['url'])
    #     session.add(video)
    # session.commit()

# def get_video_details(video_ids):
#     request = youtube.videos().list(part='snippet', id=','.join(video_ids))
#     response = request.execute()
#     return response['items']

# response = import_channel_videos(channel_id)

# channel_details = request.execute()

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  
# echo-func, that replies any message with similar message  
  # bot.send_message(message.from_user.id,'What do you mean by "'+message.text+'"?')
  # response = search(youtube, q=message.text, maxResults=1)
  # items = response.get("items")
  # for item in items:
      # get the video ID
      # video_id = item["id"]["videoId"]
      # get the video details
      # video_response = get_video_details(youtube, id=video_id)
    
# checking youtube api data
  bot.send_message(message.from_user.id,message.text) 

keep_alive()#launching flask-server in separate stream
bot.polling(non_stop=True, interval=0) #launching bot'