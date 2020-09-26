help_msg = """:
>>> Commands:
- !robin Player1 Player2 ... Player8 : Create a round robin tournament
- !bravery : Select a random fighter

Source code: https://github.com/TheRaphael0000/round_robin_discord_bot
"""


async def ssbu(message, words):
    await message.channel.send(help_msg)
