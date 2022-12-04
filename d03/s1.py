import string

priorities = dict(zip(string.ascii_letters, range(1, 57)))

def run():
    res = 0

    with open('input.txt') as f:
        for line in map(str.strip, f):
            mid = len(line) // 2
            a, b = line[:mid], line[mid:]
            shares = set(a) & set(b)
            res += priorities[shares.pop()]

    print(res)

if __name__ == '__main__':
    run()

