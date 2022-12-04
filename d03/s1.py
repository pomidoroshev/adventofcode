import string

priorities = dict(zip(string.ascii_letters, range(1, 57)))

def run(inp):
    res = 0

    for line in inp:
        mid = len(line) // 2
        a, b = line[:mid], line[mid:]
        shares = set(a) & set(b)
        res += priorities[shares.pop()]

    return res
