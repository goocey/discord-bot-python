import unittest
from Lib.tw_message import tw_message
from Lib.dataset.tweet import Tweet

class TestModelTweet(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        self.tweet = Tweet()
        pass

    def tearDown(self):
        # 終了処理
        pass

    # 異常パターンが入っていないよね？の確認
    # なお、全部正常確認はデータを全消し、全追加になるのでやらない。
    def test_get_all_enable_status(self):
        tw = self.tweet.get_all_enable_status()
        result = True

        for tweet in tw:
            print(tweet)
            if tweet.post_status != 0:
                result = False

        self.assertEqual(result, True)

    def test_add_values(self):
        messages = tw_message()
        messages.add_message(1,1,'2019-01-01 02:04:00')
        messages.add_message(1,2,'2019-01-02 02:04:00')
        messages.add_message(1,3,'2019-01-03 02:04:00')
        self.tweet.add_values(messages)

    def test_get_maxtimestamp_tweet(self):
        print(self.tweet.get_maxtimestamp_tweet())

    def test_get_maxtimestamp(self):
        print(self.tweet.get_maxtimestamp())
    
if __name__ == "__main__":
    unittest.main()