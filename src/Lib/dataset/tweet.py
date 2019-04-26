from ..model.db import session
from ..model.tweet import Tweet as tw
from datetime import datetime
from ..tw_message import tw_message
from sqlalchemy.exc import *
from sqlalchemy.sql.expression import func
from sqlalchemy import desc
import datetime


class Tweet():
    def __init__(self):
        pass

    # 投稿対象データ
    def get_all_enable_status(self):
        """投稿対象データを返却

        ステータスが0のデータ
        """
        users = session.query(tw).filter( tw.post_status == 0).all()
        return users

    def add_values(self,tweets):
        """読み取ったデータを格納します

        以下のデータは格納されません
         - tweet_idが重複しているデータ
         - created_dateが全レコードの最大値より過去日
           => つまり、後から参加した人のツイートは除外する

        Args:
            self (Tweet): 

        Returns:
            None
        """
        maxtimestamp = self.get_maxtimestamp()
        for tweet in tweets.get_messages():
            try:
                date_str = tweet['created_date'].replace(" +0000", "")
                created_date = datetime.datetime.strptime(date_str, '%c')
                if maxtimestamp is None or maxtimestamp <= created_date:
                    # 新しいデータであれば格納
                    tw_data = tw(user=tweet['user'], tid=tweet['tid'],\
                        created_date=tweet['created_date'], post_status = 0)
                    session.add(tw_data)
                    session.flush()
                    session.commit()

            except IntegrityError:
                # もうここはにぎにぎしてつぶしちゃう。
                # 発生するとしたら整合性エラーだったり、DB書き込みエラーだったりだし
                # リトライするとか正気じゃない
                session.rollback()
        session.close()

    def get_maxtimestamp(self):
        """現在保持しているレコード中、created_dateの最大値

        Args:
            self (Tweet): 

        Returns:
            String: 最大のtid
            None: 結果なし
        """
        max_timestamp = session.query(func.max(tw.created_date)).one()
        return max_timestamp[0]

    def get_maxtimestamp_tweet(self):
        """現在保持しているレコード中、created_dateが最大のtidを返却

        Args:
            self (Tweet): 

        Returns:
            String: 最大のtid
            None: 結果なし
        """
        max_timestamp = session.query(tw.tid).order_by(desc(tw.created_date)).limit(1).all()
        if len(max_timestamp) == 0:
            pass
        else:
            return max_timestamp.pop()