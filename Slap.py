import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix="PREFIX", description='bot')


@bot.event
async def on_ready():
    print("Hébérgé !")
    
    
slap_gifs = (
    "https://cdn.weeb.sh/images/rJs7GAttb.gif",
    "https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
    "https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif",
    "https://media.giphy.com/media/k1uYB5LvlBZqU/giphy.gif",
    "https://media.giphy.com/media/tX29X2Dx3sAXS/giphy.gif",
    "https://media.giphy.com/media/xUO4t2gkWBxDi/giphy.gif"
    )
    
  
@bot.command()
async def slap(ctx, user: discord.User):
    slap_gif = random.choice(slap_gifs)

    slap_embed = discord.Embed(
         description=f"**{ctx.author.name}** "text" **{user.name}**", color=0x048500)

    slap_embed.set_image(url=slap_gif)
    await ctx.send(embed=slap_embed)
    
bot.run("TOKEN")
