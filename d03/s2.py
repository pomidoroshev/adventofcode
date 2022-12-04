import string

priorities = dict(zip(string.ascii_letters, range(1, 57)))

def run():
    res = 0
    tmp = []
    with open('input.txt') as f:
        for i, line in enumerate(map(str.strip, f)):
            tmp.append(line)
            if i % 3 == 2:
                shares = set(tmp[0]) & set(tmp[1]) & set(tmp[2])
                res += priorities[shares.pop()]
                tmp = []

    print(res)

if __name__ == '__main__':
    run()

