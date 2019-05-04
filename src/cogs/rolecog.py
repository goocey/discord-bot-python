from discord.ext import commands # Bot Commands Frameworkのインポート
from lib.settings import settings
import discord.ext.commands.errors
import discord
import pprint

# コグとして用いるクラスを定義。
class RoleCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        self.role_list = settings.get_role_list()
        self.role_help = settings.get_role_help()

    # メインとなるroleコマンド
    @commands.group()
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')
   
    # 指定したユーザーに指定した役職を付与する。
    @role.command()
    async def add(self, ctx, role: discord.Role):
        if str(role) not in self.role_list:
            await ctx.send('指定可能なロール外です。')
            return None

        if role in ctx.guild.roles:
            await ctx.author.add_roles(role)

        await ctx.message.delete()
        await ctx.send('役割を適用したよ。' + str(role))

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command()
    async def remove(self, ctx, role: discord.Role):
        if str(role) not in self.role_list:
            await ctx.send('指定可能なロール外です。')
            return None

        if role in ctx.guild.roles:
            await ctx.author.remove_roles(role)

        await ctx.message.delete()
        await ctx.send('役割を除外したよ。' + str(role))

    @role.command()
    async def help(self, ctx):
        list_str = "\n".join(self.role_list)
        message = "\n".join(self.role_help)
        message += "\n\n＜役職一覧＞\n" + list_str
        await ctx.send(message)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(RoleCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。