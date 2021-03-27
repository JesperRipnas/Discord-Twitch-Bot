import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from wordlist import *

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    server_count = 0

    print(f'{bot.user} has connected to Discord!')

    for server in bot.guilds:
        print(f"- {server.id} (name: {server.name})")
        server_count += 1
        print(f"RippanBOT is in {server_count} discord servers")

@bot.event
async def on_message(message):
    #DONT RESPOND TO SELF MSG
    if message.author == bot.user: return
    if message.author.bot: return

    if any((word in message.content) for word in welcome_words):
        await message.channel.send(f"Hello {message.author.mention}")
        print(f"Discord Bot: Hello {message.author.name}")

    elif any((word in message.content) for word in banned_words):
        await message.channel.send(f"WARNING! {message.author.mention} stop using that word!, message removed")
        await message.delete()
        print(f"Discord Bot: Removed message containing the word {message.content} from user {message.author.name} in channel {message.channel.name}")
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    print('pong')
    await ctx.send('Pong!')

@bot.command()
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit=amount)
