import discord
import os
from discord.ext import commands
import json
import asyncio
import logging

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)

# configure logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)


channel_id = ""  # Replace with your channel ID
guild_id = ""  # Replace with your guild ID

@bot.event
async def on_ready():
    guild = bot.get_guild(int(guild_id))
    channel = guild.get_channel(int(channel_id))
    data = {}

    async for message in channel.history(limit=None, oldest_first=True):
        attachments = [attachment.url for attachment in message.attachments]
        author_avatar_url = str(message.author.avatar.url) if message.author.avatar else None
        data[str(message.id)] = {
            "author": str(message.author),
            "content": message.content,
            "timestamp": message.created_at.isoformat(),
            "attachments": attachments,
            "author_avatar_url": author_avatar_url,
        }
    
    with open('chat_data.json', 'w') as f:
        json.dump(data, f, indent=4)



bot.run("")
