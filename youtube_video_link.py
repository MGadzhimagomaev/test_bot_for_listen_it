from googleapiclient.discovery import build
# YouTube API block - pulling all video names from channel
google_api_key = 'AIzaSyCDn75CAh9m0Gu8WK6nvasFMdqR-von_s0'
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'

youtube = build(youtube_api_service_name, youtube_api_version, developerKey=google_api_key, static_discovery=False)
channel_id = 'UC-hIuJj-G-5wuppUy4wQ33Q'

#to pull video details - f.e. title or statisticts
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

# returns dictionary containing pair of video title and a link to it
def get_best_matching_video_title_w_link(msg):
    response = search(youtube, q=msg, channelId=channel_id, maxResults=10)
    items = response.get("items")
    yt_video_title_dict = {}

    for item in items:
        try:
            kind = item['id']['kind']
            if kind == 'youtube#video':
                yt_video_id = item['id']['videoId']
                # get the video link
                yt_link = 'https://www.youtube.com/watch?v=' + yt_video_id
                video_response = get_video_details(youtube, id=yt_video_id)['items']
                yt_video_title = video_response[0]['snippet']['title']
                yt_video_title_dict.update({yt_video_title: yt_link})
        except KeyError:
            print("error")

    return yt_video_title_dict