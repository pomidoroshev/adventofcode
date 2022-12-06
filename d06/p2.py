import re

def run(inp):
    for line in inp:
        i = 0
        while i < len(line) - 14:
            if len(set(line[i:i+14])) < 14:
                i += 1
                continue
            return i + 14
