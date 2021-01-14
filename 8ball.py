import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix="PREFIX", description='bot')


@bot.event
async def on_ready():
    print("Hébérgé !")
    
    
eight_ballx = ["yes","no","text","text"]
    
  
@bot.command(name ='8ball')
async def eight_ball(ctx, *, text):
    Eball = random.choice(eight_ballx)
    await ctx.send(f"{Eball}")

    
bot.run("TOKEN")
