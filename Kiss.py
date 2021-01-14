import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix="PREFIX", description='bot')


@bot.event
async def on_ready():
    print("Hébérgé !")
    
    
Kiss_gifs = (
    "https://media.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
    "https://media.giphy.com/media/wOtkVwroA6yzK/giphy.gif",
    "https://media.giphy.com/media/zkppEMFvRX5FC/giphy.gif",
    "https://media.giphy.com/media/sS7Jac8n7L3Ve/giphy.gif",
    "https://media.giphy.com/media/uAvMPK3narqc8/giphy.gif",
    "https://media.giphy.com/media/jR22gdcPiOLaE/giphy.gif"
    )
    
  
@bot.command()
async def kiss(ctx, user: discord.User):
    Kiss_gif = random.choice(Kiss_gifs)

    kiss_embed = discord.Embed(
         description=f"**{ctx.author.name}** "text" **{user.name}**", color=0x048500)

    kiss_embed.set_image(url=Kiss_gif)
    await ctx.send(embed=kiss_embed)
    
    bot.run("TOKEN")
