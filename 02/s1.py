# A|X - rock     - 1
# B|Y - paper    - 2
# C|Z - scissors - 3
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# Rock defeats Scissors
# Scissors defeats Paper
# and Paper defeats Rock.

def run():
    score = 0

    with open('input.txt') as f:
        for line in map(str.strip, f):
            a, b = line.split(' ')
            if b == 'X':
                score += 1
            elif b == 'Y':
                score += 2
            elif b == 'Z':
                score += 3

            if a == 'A':
                if b == 'X':
                    score += 3
                elif b == 'Y':
                    score += 6
            elif a == 'B':
                if b == 'Y':
                    score += 3
                elif b == 'Z':
                    score += 6
            elif a == 'C':
                if b == 'Z':
                    score += 3
                elif b == 'X':
                    score += 6
    print(score)

if __name__ == '__main__':
    run()

