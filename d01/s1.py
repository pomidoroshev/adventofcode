def run():
    max_calories = 0
    cur_calories = 0
    with open('input.txt') as f:
        for line in map(str.strip, f):
            if not line:
                if max_calories < cur_calories:
                    max_calories = cur_calories
                cur_calories = 0
                continue
            cur_calories += int(line)
    print(max_calories)

if __name__ == '__main__':
    run()
