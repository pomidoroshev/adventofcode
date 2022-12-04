import re

def run():
    res = 0

    with open('input.txt') as f:
        for line in map(str.strip, f):
            a1, b1, a2, b2 = map(int, re.split('[,-]', line))
            if a1 <= a2 and b1 >= b2 or a2 <= a1 and b2 >= b1:
                res += 1

    print(res)

if __name__ == '__main__':
    run()
