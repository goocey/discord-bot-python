import json
import requests
from requests_oauthlib import OAuth1Session
from .tw_message import tw_message
from .dataset.tweet import Tweet
from Lib.settings import settings


class Twitter:
    """twitterAPI通信処理
    """
    def __init__(self):
        """初期処理
        Args:
            self(Lib.twitter):
        Return:
            None
        """
        token = settings.get()
        CK = token['CONSUMER_KEY']
        CS = token['CONSUMER_SECRET']
        AT = token['ACCESS_TOKEN']
        ATS = token['ACCESS_TOKEN_SECRET']
        self.twitter = OAuth1Session(CK, CS, AT, ATS)

    def read_list_tl(self):
        """リストのタイムライン読み込み
        
        Args:
            self(Lib.Twitter):
        Returns:
            
        """
        message = tw_message()
        url = "https://api.twitter.com/1.1/lists/statuses.json" #タイムライン取得エンドポイント

        # list_id決め打ちで取得しに行く
        params = {'list_id' : 1118826235000279040, 'count': 200} #取得数

        tweet = Tweet()
        tid = tweet.get_maxtimestamp_tweet()
        if tid is not None:
            params['since_id'] = tid
        print(params)
        res = self.twitter.get(url, params = params)

        if res.status_code == 200: #正常通信出来た場合
            timelines = json.loads(res.text)
            
            for line in timelines:
                message.add_message(line['user']['name'], line['user']['screen_name'],\
                    line['id_str'], line['created_at'])
            return message
        else: #正常通信出来なかった場合
            raise requests.exceptions.ConnectionError

    # リストID取得 list_idを単に取るだけ、実際のbotでは使わない。
    def get_list_id(self, list_name):
        message = tw_message()
        url = "https://api.twitter.com/1.1/lists/list.json"

        # params = {'user_id': user_name}
        params = {}
        res = self.twitter.get(url, params = params)
        if res.status_code == 200: #正常通信出来た場合
            data = json.loads(res.text)
            for line in data:
                if line['full_name'] == "@kokoro_discord/list":
                    print(line['id_str'])
        else: #正常通信出来なかった場合
            raise requests.exceptions.ConnectionError