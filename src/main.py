# coding:utf-8
import discord
import asyncio
import yaml
from discord.ext import commands
from pprint import pprint

bot = commands.Bot(command_prefix="!")

# 初期イベント
@bot.event
async def on_ready():
    activity = discord.Game(name="with fire")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Logged in as " + bot.user.name)


# twitterの情報を登録する
@bot.command(pass_context=True)
async def registry_twitter(ctx):
    reg_account = ctx.message.mentions[0]
    message = ctx.message.content
    twitter_account = message.split("  ")[1]
    
    f = open('twitter.yml', mode="a")
    data = reg_account.name + ": " + twitter_account
    f.write(str(data))

# twitterの情報を表示する
@bot.command(pass_context=True)
async def display_twitter(ctx):
    dis_account = ctx.message.mentions[0]

    f = open('twitter.yml')
    twitter = yaml.safe_load(f)

    await ctx.channel.send(twitter[dis_account.name])

with open('data.yml') as file:
    token = yaml.safe_load(file)

bot.run(token['token'])