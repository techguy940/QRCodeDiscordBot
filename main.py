import discord
from discord.ext import commands
import qrcode
import io

TOKEN = "Bot Token"
PREFIX = "!"

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

@bot.event
async def on_ready():
  print("Ready")

@bot.command()
async def qr(ctx, *, data):
  if ctx.author.bot: return
  q = qrcode.make(data)
  arr = io.BytesIO()
  q.save(arr, format="PNG")
  arr.seek(0)
  await ctx.send(file=discord.File(fp=arr, filename="image.png"))

bot.run(TOKEN)
