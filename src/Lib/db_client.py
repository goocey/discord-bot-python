import psycopg2
import yaml
from .tw_message import tw_message

# DB操作用
class db_client:
    db = ""

    # memcache接続
    def __init__(self):
        with open('data.yml') as file:
            self.setting = yaml.safe_load(file)
        self.get_connection()

    def __del__(self):
        self.cur.close()

    def get_connection(self):
        if (type(self.db) is not 'connection'):
            self.db = psycopg2.connect(self.setting['DATABASE'])

        self.cur = self.db.cursor()
        print('get_connect')

        # これもしかしたら動かないかも。(コネクション管理はこんなに簡単じゃないはず)

    # ツイートデータ追加
    def add_values(self, tw_message):
        self.get_connection()
        for tweet in tw_message.get_messages():
            pass

    # チャンネル投稿用ツイート抽出
    def get_enable_all_data(self):
            pass

    # ステータス更新
    def update_status(self,ids):
        for id in ids:
            # TODO:実装
            pass

    # 前回実施日時を格納
    def get_before_do_time(self):
        # TODO: 実装
        pass

    # すべてのデータをダンプ
    def get_all_values(self):
        # デバッグ用なので実装必要であれば
        pass