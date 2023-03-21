#Main file
import discord
import comms
from discord.ext import commands 


client = commands.Bot(intents=discord.Intents.default(), command_prefix='!')

@client.event
async def on_ready():
    print('D´Arby getting ready to gamble')

client.run('MTA4NzUyMDg2MTA4MDI2NDc3NA.G983Ol.Beg8HamjPIkzIAN0F466DYjn3ntkznaeMIPnE0')