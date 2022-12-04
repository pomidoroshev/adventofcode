import re

def run(inp):
    res = 0

    for line in inp:
        a1, b1, a2, b2 = map(int, re.split('[,-]', line))
        if a1 <= b2 and b1 >= a2:
            res += 1

    return res
