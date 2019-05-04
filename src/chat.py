# coding:utf-8
import discord
import asyncio
import yaml
import time
import os
from discord.ext import commands
from pprint import pprint
from discord import TextChannel, VoiceChannel
import threading
from lib.dataset.tweet import Tweet
from lib.model.tweet import Tweet as tw
from lib.model.db import session
from lib.settings import settings

class Chat(discord.Client):
    """discordでtweet情報を流すためのクラス
    """

    def __init__(self, *args, **kwargs):
        """初期処理
        """
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        """ログイン完了辺りで呼ばれるコールバック

        Args:
            self(Chat):
        """
        print('Logged in as')
        # チャンネル取得
        channel = discord.utils.get(self.get_all_channels(),  guild__name=setting['SERVER'] ,name=setting['TWEET_CHANNEL'])
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task(channel))

    async def my_background_task(self, channel):
        await client.wait_until_ready()
        # await client.wait_for('ready')
        print('background_task')

        tw = Tweet()
        print(channel)

        # とにかく繰り返す
        # 多分このタスク自体をずっと繰り返すというやり方があるはずなのだけど分からないので
        while True:
            for tweet in tw.get_all_enable_status():
                session.begin()
                await channel.send(tweet.url)
                tweet.post_status=1
                session.commit()
                await asyncio.sleep(1)
            await asyncio.sleep(10)

setting = settings.get_setting()
client = Chat()
client.run(setting['DISCORD_TOKEN'])
