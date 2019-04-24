from Lib.twitter import twitter
from Lib.tw_message import tw_message
from Lib.db_client import db_client

def main():
    memcache = db_client()

    twitter = twitter()
    twitter.get_list_id('kokoro_discord')
    messages =  twitter.read_list_tl()
    db_client.add_values(messages)

