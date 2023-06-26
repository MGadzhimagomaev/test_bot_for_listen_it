import requests
import json
class YTstats:
    def __init__(self, google_api_key, channel_id):
        self.google_api_key = google_api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.google_api_key}'
        # print(url)

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # print(data)
        try:
            data = data["items"][0]["statistics"]
        except:
            data = None
        self.data_statistics = data
        return data

    def get_channel_video_data(self):
        #get video ids
        channel_videos = self._get_channel_videos(limit=5)
        #get video statistics

    def _get_channel_videos(self, limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.google_api_key}&channelId={self.channel_id}&part=id&order=date'
        if limit is not None and isinstance(limit, int):
            url += '&maxResults=' + str(limit)
        print(url)

    # def dump(self):
    #     if self.channel_statistics is None:
    #         return
    #
    #     channel_title = "ListenIT"
    #     channel_title = channel_title.replace(" ","_").lower()
    #     file_name = channel_title + '.json'
    #     with open(file_name, 'w') as f: