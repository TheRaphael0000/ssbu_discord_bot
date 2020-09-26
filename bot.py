#!/usr/bin/env python

import os
import re

import discord
from dotenv import load_dotenv

from commands.ssbu import ssbu
from commands.robin import robin
from commands.bravery import bravery

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

    commands = {
        "!ssbu": ssbu,
        "!robin": robin,
        "!bravery": bravery,
    }

    if words[0] in commands.keys():
        await commands[words[0]](message, words)

client.run(token)
