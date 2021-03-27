import os
import discord
from dotenv import load_dotenv
from discordbot import *

load_dotenv()
DISCORDTOKEN = os.getenv('DISCORD_TOKEN')
DISCORDSERVER = os.getenv('DISCORD_GUILD')

dbot.run(DISCORDTOKEN)
