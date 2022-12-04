def run(inp):
    max_calories = 0
    cur_calories = 0
    for line in inp:
        if not line:
            if max_calories < cur_calories:
                max_calories = cur_calories
            cur_calories = 0
            continue
        cur_calories += int(line)
    return max_calories
