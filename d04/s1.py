import re

def run(inp):
    res = 0

    for line in inp:
        a1, b1, a2, b2 = map(int, re.split('[,-]', line))
        if a1 <= a2 and b1 >= b2 or a2 <= a1 and b2 >= b1:
            res += 1

    return res
