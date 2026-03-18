import discord
from discord.ext import commands
from model import detect_picture

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            name = attachment.filename
            await attachment.save(f"./images/{attachment.filename}")
            await ctx.send(f"Resim '{name}' olarak kaydedildi.")
            await ctx.send(detect_picture("keras_model.h5","labels.txt",f"./images/{attachment.filename}"))

    else:
        await ctx.send("Lütfen bir dosya ekleyin.")

bot.run("TOKEN")
