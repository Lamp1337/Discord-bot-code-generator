import discord
import random
import string
from discord.ext import commands

client = commands.Bot(command_prefix="!", help_command=None)
TOKEN = "Your bot token"

@client.event
async def on_ready():
    print("Bot is Online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"!help"))

@client.command()
async def generatecode(ctx):
    await ctx.reply(f"Result ```{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 10))}```")

@client.command()
async def help(ctx):
    await ctx.reply("!generatecode (for generate code)")

client.run(TOKEN, bot=True)
