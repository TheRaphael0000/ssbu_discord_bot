def round_robin(l):
    o = []
    if len(l) % 2 == 1:
        l.append(None)
    n = len(l)

    for i in range(n - 1):
        o.append((l[i], l[n - 1]))
        for k in range(1, int(n / 2)):
            a = (i + k) % (n - 1)
            b = (i - k) % (n - 1)
            o.append((l[a], l[b]))
    o = [i for i in o if i[0] is not None and i[1] is not None]
    return o


def create_text(r):
    text = "```\n"
    lpad = max([len(i[0]) for i in r])
    for i, ri in enumerate(r):
        text += f"{i}. {ri[0].ljust(lpad)} - {ri[1]}\n"
    text += "```"
    return text


def main():
    print(round_robin([]))
    print(round_robin(["a"]))
    print(round_robin(["0", "1", "2", "3"]))


if __name__ == '__main__':
    main()
