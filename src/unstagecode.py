# 使われなかったコード
# お布団行は不要だそうだTT
# !ofutonコマンド
@bot.command(pass_context=True)
async def ofuton(ctx):
    victim = ctx.message.mentions[0] 
    ofuton_channel = bot.get_channel(564139070918230019)
    # 移動
    await victim.move_to(ofuton_channel)
