#!/usr/bin/env python
import os
import re

import discord
from dotenv import load_dotenv

from round_robin import round_robin, create_text

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} ready')


@client.event
async def on_message(message):
    # Safety first, avoid recursive calls
    if message.author == client.user:
        return

    # Look up for message related to the bot
    words = re.split(r"\s+", message.content)
    if words[0] != "!robin":
        return

    players = words[1:]

    n = len(players)

    if n <= 0:
        msg = """:
>>> **Create a round-robin tournament for 2 to 8 players**
*Syntax : !robin Player1 Player2 ... Player8*
GitHub: https://github.com/TheRaphael0000/round_robin_discord_bot
"""
        await message.channel.send(msg)
        return

    # Upper-bound
    if n > 8 or n < 2:
        await message.channel.send("*Please specify between 2 and 8 players*")
        return

    # Create round robin
    r = round_robin(players)
    # Create text message
    t = create_text(n, r)

    # Send it
    await message.channel.send(t)

client.run(token)
