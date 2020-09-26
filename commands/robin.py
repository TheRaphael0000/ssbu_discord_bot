#!/usr/bin/env python

help_msg = """:
>>> **Create a round-robin tournament for 2 to 8 players**
*Syntax : !robin Player1 Player2 ... Player8*
"""


async def robin(message, words):
    """Handling the command !robin"""
    players = words[1:]

    n = len(players)

    # Upper-bound
    if n > 8 or n < 2:
        return await message.channel.send(help_msg)

    # Create round robin
    r = round_robin(players)
    # Create text message
    t = create_text(n, r)

    # Send it
    return await message.channel.send(t)


def round_robin(l):
    """Round-robin tournament algorithm"""
    o = []
    # Add a player "None" to have an even number of players
    if len(l) % 2 == 1:
        l.append(None)
    n = len(l)

    for i in range(n - 1):
        a = l[i]
        b = l[n - 1]
        o.append((a, b))
        for k in range(1, n // 2):
            a = (i + k) % (n - 1)
            b = (i - k) % (n - 1)
            o.append((l[a], l[b]))
    # Remove None match (when playing with an odd number of players)
    o = [i for i in o if i[0] is not None and i[1] is not None]
    # Rotate by one the tournament
    o = [o[-1]] + o[:-1]
    return o


def create_text(n, r):
    """Create a monospace string for Markdown"""
    match_per_player = n - 1
    nb_round = (n * (n - 1)) // 2
    playrate = match_per_player / nb_round

    text = "```\n"
    lpad = max([len(i[0]) for i in r])
    numpad = len(str(len(r) - 1))
    line = "{:0>" + str(numpad) + "}. {:<" + str(lpad) + "} - {}\n"
    for i, ri in enumerate(r):
        text += line.format(i, ri[0], ri[1])
    text += "Playrate : {}/{} = {:.2f}\n".format(
        match_per_player, nb_round, playrate)
    text += "```"
    return text


def main():
    """Unite tests"""
    print(round_robin([]))
    print(round_robin(["a"]))
    print(round_robin(["0", "1", "2", "3"]))


if __name__ == '__main__':
    main()
