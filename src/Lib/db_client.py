import psycopg2
from .tw_message import tw_message

# DB操作用
class db_client:
    # memcache接続
    def __init__(self):

        self.db = memcache.Client({'127.0.0.1:11211'})
    
    def get_connection():
        with open('data.yml') as file:
            setting = yaml.safe_load(file)
        self.db=psycopg2.connect(setting['DATABASE'])
    
    # ツイートデータ追加
    def add_values(self, tw_message):
        for  tweet in tw_message.get_messages():
            # TODO:一度検査してなかったら追加（実装）
            # 追加条件：前回実行時刻以降　かつ　データなし

    # チャンネル投稿用ツイート抽出
    def get_enable_all_data(self):
        for  tweet in tw_message.get_messages():
            # TODO:実装
            # 未反映、指定時間以前のものを)

    # ステータス更新
    def update_status(self,id):
        for id in ids:
            # TODO:実装

    # 前回実施日時を格納
    def get_before_do_time(self):
        # TODO: 実装

    # すべてのデータをダンプ
    def get_all_values(self):
        # デバッグ用なので実装必要であれば