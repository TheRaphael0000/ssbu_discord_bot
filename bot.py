#!/usr/bin/env python

import os
import re
import systemd.daemon

import discord
from dotenv import load_dotenv

import commands


class SSBUActivity(discord.Activity):
    def __init__(self, nb_guilds):
        super().__init__(
            name=f"Super Smash Bros. Ultimate (on {nb_guilds} servers)",
            type=discord.ActivityType.playing
        )


class SSBUBot(discord.Client):
    async def on_ready(self):
        nb_guilds = len(self.guilds)
        game = SSBUActivity(nb_guilds)
        status = discord.Status.online
        await self.change_presence(activity=game, status=status)
        print(f"{self.user} ready, connected on {nb_guilds} servers")
        systemd.daemon.notify("READY=1")

    async def on_message(self, message):
        # Safety first, avoid recursive calls
        if message.author == self.user:
            return

        # Look up for message related to the bot
        words = re.split(r"\s+", message.content)

        cmds = {
            "!ssbu": commands.ssbu,
            "!robin": commands.robin,
            "!bravery": commands.bravery,
        }

        if words[0] in cmds:
            await cmds[words[0]](message, words)


def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    bot = SSBUBot()
    try:
        bot.run(token)
    except:
        bot.close()


if __name__ == "__main__":
    main()
