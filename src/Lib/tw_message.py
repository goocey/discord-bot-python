from .settings import settings


class tw_message:
    """
    twitterメッセージ保持用オブジェクトクラス
    中身は単なるdictの配列
    DAO的なイメージで使ってください
    """
    def __init__(self):
        """インストラクタ
        Args:
            Lib.tw_message
        Return:
            None
        """
        self.list = []
        self.data = settings.get_setting()

    def add_message(self, user, screen_name, tid, created_date):
        """配列にtweet情報を追加

        Args:
            self(tw_message):
            user(str): ユーザ名
            screen_name(string): twitter_id的な(@xxx)
            tid(str): ツイートID
            created_date(str): 作成日時のはず
        """
        url = self.data['TWITTER_BASE']
        print(url.format(screen_name, tid))
        self.list.append({'user': user, 'screen_name': screen_name, 'tid': tid,\
             'url': url.format(screen_name, tid), 'created_date':created_date})

    def get_messages(self):
        """保持しているリストを返却

        Args:
            self(tw_message):
        Returns:
            List[dict,dict]: 結果あり
            List[]: 結果無し
        """
        return self.list