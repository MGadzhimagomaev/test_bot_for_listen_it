from googleapiclient.discovery import build
# YouTube API block - pulling all video names from channel
google_api_key = 'AIzaSyCDn75CAh9m0Gu8WK6nvasFMdqR-von_s0'
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'

youtube = build(youtube_api_service_name, youtube_api_version, developerKey=google_api_key, static_discovery=False)
channel_id = 'UC-hIuJj-G-5wuppUy4wQ33Q'


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


def get_best_matching_video_header(msg):
    response = search(youtube, q=msg, channelId=channel_id, maxResults=5)
    items = response.get("items")
  
    for item in items:
        try:
            kind = item['id']['kind']
            if kind == 'youtube#video':
                yt_video_id = item['id']['videoId']
        except KeyError:
            print("error")

        # get the video details
        video_response = get_video_details(youtube, id=yt_video_id)['items']
        yt_video_title = video_response[0]['snippet']['title']
        
        return yt_video_title


def get_best_matching_video_link(msg):
    response = search(youtube, q=msg, channelId=channel_id, maxResults=5)
    items = response.get("items")
    # msg = str(msg)
    # yt_video_id = None
  
    for item in items:
        try:
            kind = item['id']['kind']
            if kind == 'youtube#video':
                yt_video_id = item['id']['videoId']
        except KeyError:
            print("error")

        # get the video details
        # video_response = get_video_details(youtube, id=yt_video_id)['items']
        # yt_link = 'https://www.youtube.com/watch?v=' + video_response[0]['id']
        yt_link = 'https://www.youtube.com/watch?v=' + yt_video_id
        return yt_link

