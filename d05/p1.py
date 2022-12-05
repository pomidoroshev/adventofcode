import re

strip = False

def run(inp):
    stacks = [[], [], [], [], [], [], [], [], []]

    filling = True
    for line in inp:
        if not line.strip():
            filling = False
            for s in stacks:
                s.reverse()
            continue
        if filling:
            for i, s in enumerate(stacks):
                if len(line) >= i*4+3 and line[i*4] == '[':
                    s.append(line[i*4+1])
        else:
            parts = line.strip().split(' ')
            num = int(parts[1])
            from_ = int(parts[3])
            to = int(parts[5])
            for _ in range(num):
                c = stacks[from_-1].pop()
                stacks[to-1].append(c)

    return ''.join(x[-1] for x in stacks)
