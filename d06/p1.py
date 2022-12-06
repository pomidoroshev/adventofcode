import re

def run(inp):
    for line in inp:
        i = 0
        while i < len(line) - 4:
            if len(set(line[i:i+4])) < 4:
                i += 1
                continue
            return i + 4
