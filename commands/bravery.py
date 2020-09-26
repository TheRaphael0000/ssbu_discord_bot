#!/usr/bin/env python

import random
from .fighters import fighters


async def bravery(message, words):
    """Handling the command !bravery"""
    fighter = get_random_fighter()
    return await message.channel.send(f"Your fighter is {fighter} !")


def get_random_fighter():
    return random.choice(fighters)


def main():
    """Unite tests"""
    print(get_random_fighter())
    print(get_random_fighter())
    print(get_random_fighter())


if __name__ == '__main__':
    main()
