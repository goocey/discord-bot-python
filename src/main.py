# coding:utf-8
import discord
import asyncio
import yaml
from discord.ext import commands
from pprint import pprint

# discord.py reference: https://discordpy.readthedocs.io/en/latest/api.html

bot = commands.Bot(command_prefix="!")

# 初期イベント(起動時？)
@bot.event
async def on_ready():
    activity = discord.Game(name="with fire")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Logged in as " + bot.user.name)
    print(discord.Server.name)

# !ofutonコマンド
@bot.command(pass_context=True)
async def ofuton(ctx):
    victim = ctx.message.mentions[0] # お布団行対象ユーザー
    # channel = ctx.message.author.voice.voice_channel # 対象ユーザがいるボイスチャンネル？

    ofuton_channel = bot.get_channel(564139070918230019)  # <=== 問題のコード
    # 以下のmove_memberは動作的に問題なさそう（create_channelで作成したChannelオブジェクトは使用可能）
    await victim.move_to(ofuton_channel)

# みんなのtwitterのツイート捜索するためのテストコード
@bot.command(pass_context=True)
async def all_user(ctx):

    for member in bot.get_all_members():
        # でもねー。Memberオブジェクトって拡張的なメタデータはないっぽい。
        pprint(member)

with open('data.yml') as file:
    token = yaml.safe_load(file)

bot.run(token['token'])