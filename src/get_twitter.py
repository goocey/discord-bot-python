from Lib.twitter import Twitter
from Lib.tw_message import tw_message
from Lib.dataset.tweet import Tweet
import schedule
import time

def job():
    # 定期実行させたい処理
    print('read')
    read_twitter()

def read_twitter():
    twitter = Twitter()
    twitter.get_list_id('kokoro_discord')
    messages =  twitter.read_list_tl()
    tweet = Tweet()
    tweet.add_values(messages)

def main():
    schedule.every(10).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()