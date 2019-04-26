# twitterメッセージ保持用オブジェクトクラス
class tw_message:

    def __init__(self):
        self.list = []

    # R2リストに追加
    def add_message(self, user, tid, created_date):
        self.list.append({'user': user, 'tid': tid, 'created_date':created_date})

    # リストを返却
    def get_messages(self):
        return self.list