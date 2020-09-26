#!/usr/bin/env python

import os
import re
import systemd.daemon

import discord
from dotenv import load_dotenv

import commands


class SSBU(discord.Client):
    async def on_ready(self):
        systemd.daemon.notify("READY=1")
        print(f"{self.user} ready")

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

        if words[0] in cmds.keys():
            await cmds[words[0]](message, words)


def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    bot = SSBU()
    bot.run(token)


if __name__ == "__main__":
    main()
