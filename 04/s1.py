def run():
    res = 0

    with open('input.txt') as f:
        for line in map(str.strip, f):
            g1, g2 = line.split(',')
            a1, b1 = map(int, g1.split('-'))
            a2, b2 = map(int, g2.split('-'))
            if a1 <= a2 and b1 >= b2:
                res += 1
            elif a2 <= a1 and b2 >= b1:
                res += 1

    print(res)

if __name__ == '__main__':
    run()

