import discord
import os
import subprocess
from discord import app_commands
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
Token = os.getenv('Token')
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if message.attachments:
            wget = f"wget {message.attachments[0].url}"
            subprocess.call(wget.split())
            # 画像を開く
            image = Image.open(message.attachments[0].filename)
            # 画像の幅と高さを取得する
            width, height = image.size
            # 画像を水平方向に反転する
            mirrored_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
            # 元の画像と反転した画像を並べた新しい画像を作成する
            new_image = Image.new("RGB", (width * 2, height))
            new_image.paste(image, (0, 0))
            new_image.paste(mirrored_image, (width, 0))
            # 新しい画像を保存する
            new_image.save("ryoume.png")
            file = discord.File("ryoume.png")
            await message.reply(file=file)
        else:
            return


client.run("MTA1ODQ0NTI4Nzc2MjQzMjA4MQ.GtVJVD.dJknTYOzhzhSB9-pWFIF8Qw_9dIsKl3EP62Ds0")
