from lib.twitter import Twitter
from lib.tw_message import tw_message
from lib.dataset.tweet import Tweet
import schedule
import time

def read_twitter():
        twitter = Twitter()
        twitter.get_list_id('kokoro_discord')
        messages =  twitter.read_list_tl()
        tweet = Tweet()
        tweet.add_values(messages)

def main():
        count=10
        read_twitter()
        time.sleep(count)
        schedule.every(count).minutes.do(read_twitter)
        while True:
                schedule.run_pending()
                time.sleep(1)

if __name__ == "__main__":
    main()
