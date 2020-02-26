# bot.py
import os

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
    if message.author == client.user:
        return
    # Look up for message related to the bot
    words = message.content.split(" ")
    if words[0] != "!robin":
        return

    players = words[1:]

    # Lower-bound
    if len(players) <= 1:
        await message.channel.send("*Create a round-robin tournament for the given players (space separated)\nSyntax : !robin p1 p2 ... p8*\nhttps://github.com/TheRaphael0000/round_robin_discord_bot")
        return

    # Upper-bound
    if len(players) >= 8:
        await message.channel.send("*Please specify 8 or less players*")
        return

    # Create round robin
    r = round_robin(players)
    # Create text message
    t = create_text(r)

    # Send it
    await message.channel.send(t)

client.run(token)
