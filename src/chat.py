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
from Lib.dataset.tweet import Tweet
from Lib.model.tweet import Tweet as tw
from Lib.model.db import session
from Lib.settings import settings

class Chat(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as')
        channel = discord.utils.get(self.get_all_channels(),  guild__name='test' ,name='tweet')
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task(channel))

    async def my_background_task(self, channel):
        await client.wait_until_ready()
        # await client.wait_for('ready')
        print('background_task')
            
        tw = Tweet()
        print(channel)
        while True:
            for tweet in tw.get_all_enable_status():
                await channel.send(tweet.url)
                tweet.post_status=1
                session.flush()
                session.commit()
                await asyncio.sleep(1)
            await asyncio.sleep(10)

setting = settings.get()
client = Chat()
client.run(setting['DISCORD_TOKEN'])