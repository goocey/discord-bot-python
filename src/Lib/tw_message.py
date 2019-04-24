# twitterメッセージ保持用オブジェクトクラス
class tw_message:

    def __init__(self):
        self.list = []

    # R2リストに追加
    def add_message(self, uid, mid, time):
        self.list.append({'uid': uid, 'mid': mid, 'time':time})

    # リストを返却
    def get_messages(self):
        return self.list