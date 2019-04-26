from .settings import settings

# twitterメッセージ保持用オブジェクトクラス
class tw_message:

    def __init__(self):
        self.list = []
        self.data = settings.get()

    # R2リストに追加
    def add_message(self, user, screen_name, tid, created_date):
        url = self.data['TWITTER_BASE']
        print(url.format(screen_name, tid))
        self.list.append({'user': user, 'screen_name': screen_name, 'tid': tid,\
             'url': url.format(screen_name, tid), 'created_date':created_date})

    # リストを返却
    def get_messages(self):
        return self.list