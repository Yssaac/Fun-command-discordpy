import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix="=", description='Favelas')


@bot.event
async def on_ready():
    print("Hébérgé !")
    
    
hug_gifs = ( "https://media.giphy.com/media/3bqtLDeiDtwhq/giphy.gif",
    "https://media.giphy.com/media/VXP04aclCaUfe/giphy.gif",
    "https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif",
    "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
    "https://media.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif",
    "https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif",
    "https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif"
    )
    
  
@bot.command()
async def hug(ctx, user: discord.User):
    hug_gif = random.choice(hug_gifs)

    hug_embed = discord.Embed(
         description=f"**{ctx.author.name}** "text" **{user.name}**", color=0x048500)

    hug_embed.set_image(url=hug_gif)
    await ctx.send(embed=hug_embed)
