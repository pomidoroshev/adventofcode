import string

priorities = dict(zip(string.ascii_letters, range(1, 57)))

def run(inp):
    res = 0
    tmp = []
    for i, line in enumerate(inp):
        tmp.append(line)
        if i % 3 == 2:
            shares = set(tmp[0]) & set(tmp[1]) & set(tmp[2])
            res += priorities[shares.pop()]
            tmp = []

    return res
