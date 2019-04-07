import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from pprint import pprint

# discord.py reference: https://discordpy.readthedocs.io/en/latest/api.html

bot = commands.Bot(command_prefix="!")

# 初期イベント(起動時？)
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='with fire'))
    print("Logged in as " + bot.user.name)
    print(discord.Server.name)
    print(bot.get_channel("ofuton"))

# !ofutonコマンド
@bot.command(pass_context=True)
async def ofuton(ctx):
    victim = ctx.message.mentions[0] # お布団行対象ユーザー
    channel = ctx.message.author.voice.voice_channel # 対象ユーザがいるボイスチャンネル？
    pprint(channel) # 参照OK

    ofuton_channel = ctx.get_channel("ofuton") # <=== 問題のコード
    # 以下のmove_memberは動作的に問題なさそう（create_channelで作成したChannelオブジェクトは使用可能）
    await bot.move_member(victim, ofuton_channel)

# みんなのtwitterのツイート捜索するためのテストコード
@bot.command(pass_context=True)
async def all_user(ctx):

    for member in bot.get_all_members():
        # でもねー。Memberオブジェクトって拡張的なメタデータはないっぽい。
        pprint(member)

bot.run("NTY0MTA3ODg5OTU5MjM5Njgz.XKnptg.o3AjB7ekFES8ShRdaZu7C0FCRWU")