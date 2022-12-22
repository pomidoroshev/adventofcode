def calc_scentic(m, j, i):
    c1 = c2 = c3 = c4 = 1
    cur = int(m[j][i])
    _i = i + 1
    while _i < len(m[0]) - 1:
        n = int(m[j][_i])
        if n >= cur:
            break
        c1 += 1
        _i += 1

    _i = i - 1
    while _i > 0:
        n = int(m[j][_i])
        if n >= cur:
            break
        c2 += 1
        _i -= 1

    _j = j + 1
    while _j < len(m) - 1:
        n = int(m[_j][i])
        if n >= cur:
            break
        c3 += 1
        _j += 1

    _j = j - 1
    while _j > 0:
        n = int(m[_j][i])
        if n >= cur:
            break
        c4 += 1
        _j -= 1

    return c1 * c2 * c3 * c4

def run(inp):
    m = [*inp]
    max_scentic = 1
    i = j = 1
    while j < len(m) - 1:
        while i < len(m[0]) - 1:
            scentic = calc_scentic(m, j, i)
            if max_scentic < scentic:
                max_scentic = scentic
            i += 1
        j += 1
        i = 1

    return max_scentic
