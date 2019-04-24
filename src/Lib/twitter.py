import json
import yaml
import requests
from .tw_message import tw_message

from requests_oauthlib import OAuth1Session

class twitter:

    def __init__(self):
        with open('data.yml') as file:
            token = yaml.safe_load(file)
        CK = token['CONSUMER_KEY']
        CS = token['CONSUMER_SECRET']
        AT = token['ACCESS_TOKEN']
        ATS = token['ACCESS_TOKEN_SECRET']
        self.twitter = OAuth1Session(CK, CS, AT, ATS)

    # def read(self):
    #     message = tw_message()
    #     message.add_message('luna','234242432','2019-01-01')
    #     message.add_message('luna1','234242433','2019-01-02')
    #     message.add_message('luna2','234242434','2019-01-03')
    #     return message

    # 本物コード
    # リスト読み込み
    def read_list_tl(self):
        message = tw_message()
        url = "https://api.twitter.com/1.1/lists/statuses.json" #タイムライン取得エンドポイント

        # list_id決め打ちで取得しに行く
        params ={'list_id' : 1118826235000279040, 'count': 30} #取得数
        res = self.twitter.get(url, params = params)

        if res.status_code == 200: #正常通信出来た場合
            timelines = json.loads(res.text)
            
            for line in timelines:
                message.add_message(line['user']['name'], line['id_str'], line['created_at'])
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