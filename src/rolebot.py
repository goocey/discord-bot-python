from lib.settings import settings
from discord.ext import commands
import traceback # エラー表示のためにインポート

INITIAL_COGS = [
    'cogs.rolecog'
]

class RoleBot(commands.Bot):
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_COGS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

# RoleBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    setting = settings.get_setting()
    bot = RoleBot(command_prefix='!') # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(setting['DISCORD_TOKEN']) # Botのトークン