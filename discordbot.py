import os
import discord
from dotenv import load_dotenv
from wordlist import *

dbot = discord.Client()

@dbot.event
async def on_ready():
    server_count = 0

    print(f'{dbot.user} has connected to Discord!')

    for server in dbot.guilds:
        print(f"- {server.id} (name: {server.name})")
        server_count += 1
        print(f"RippanBOT is in {server_count} discord servers")

@dbot.event
async def on_message(message):
    #DONT RESPOND TO SELF MSG
    if message.author == dbot.user: return
    if message.author.bot: return

    if any((word in message.content) for word in welcome_words):
        await message.channel.send(f"Hello {message.author.mention}")
        print(f"Discord Bot: Hello {message.author.name}")

    elif any((word in message.content) for word in banned_words):
        await message.channel.send(f"WARNING! {message.author.mention} stop using that word!, message removed")
        await message.delete()
        print(f"Discord Bot: Removed message containing the word {message.content} from user {message.author.name} in channel {message.channel.name}")

