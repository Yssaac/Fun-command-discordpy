import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix="PREFIX", description='bot')


@bot.event
async def on_ready():
    print("Hébérgé !")
    
    
punch_gifs = (
    "https://media.giphy.com/media/1Bgr0VaRnx3pCZbaJa/giphy.gif",
    "https://media.giphy.com/media/upT3Tbwupcbok/giphy.gif",
    "https://media.giphy.com/media/MZqLlWvzkkMCc/giphy.gif",
    "https://media.giphy.com/media/11HeubLHnQJSAU/giphy.gif",
    "https://cdn.weeb.sh/images/rJHLDT-Wz.gif",
    "https://media.giphy.com/media/d7xeroaNIt2wwg3yHY/giphy.gif"
    )
    
  
  @bot.command()
async def punch(ctx, user: discord.User):
    punch_gif = random.choice(punch_gifs)

    punch_embed = discord.Embed(
         description=f"**{ctx.author.name}** "text" **{user.name}**", color=0x048500)

    punch_embed.set_image(url=punch_gif)
    await ctx.send(embed=punch_embed)
  
  
bot.run("TOKEN")
