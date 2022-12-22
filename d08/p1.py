from pprint import pp

def run(inp):
    m = [*inp]
    coords = set()

    # top
    j = 0
    i = 0
    max_in_row = -1
    while i < len(m[0]):
        while j < len(m):
            t = int(m[j][i])
            if t <= max_in_row:
                coords.add((j, i))
            else:
                max_in_row = t
            j += 1
        i += 1
        j = 0
        max_in_row = -1

    # bottom
    j = len(m) - 1
    i = 0
    max_in_row = -1
    while i < len(m[0]):
        while j > 0:
            t = int(m[j][i])
            if t > max_in_row:
                max_in_row = t
                if (j, i) in coords:
                    coords.remove((j, i))
            j -= 1
        i += 1
        j = len(m) - 1
        max_in_row = -1

    # left
    j = 0
    i = 0
    max_in_row = -1
    while j < len(m):
        while i < len(m[0]):
            t = int(m[j][i])
            if t > max_in_row:
                max_in_row = t
                if (j, i) in coords:
                    coords.remove((j, i))
            i += 1
        j += 1
        i = 0
        max_in_row = -1

    # right
    j = 0
    i = len(m[0]) - 1
    max_in_row = -1
    while j < len(m):
        while i > 0:
            t = int(m[j][i])
            if t > max_in_row:
                max_in_row = t
                if (j, i) in coords:
                    coords.remove((j, i))
            i -= 1
        j += 1
        i = len(m[0]) - 1
        max_in_row = -1

    return len(m[0]) * len(m) - len(coords)