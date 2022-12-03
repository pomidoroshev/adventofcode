# A - rock     - 1
# B - paper    - 2
# C - scissors - 3

# X - lose
# Y - draw
# Z - win

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
                score += 0
            elif b == 'Y':
                score += 3
            elif b == 'Z':
                score += 6

            if a == 'A':  # rock
                if b == 'X':  # lose, choose scissors
                    score += 3
                elif b == 'Y':  # draw, choose rock
                    score += 1
                else:  # win, choose paper
                    score += 2
            elif a == 'B':  # paper
                if b == 'X':  # lose, choose rock
                    score += 1
                elif b == 'Y':  # draw, choose paper
                    score += 2
                else:  # win, choose scissors
                    score += 3
            elif a == 'C':  # scissors
                if b == 'X':  # lose, choose paper
                    score += 2
                elif b == 'Y':  # draw, choose scissors
                    score += 3
                else:  # win, choose rock
                    score += 1
    print(score)

if __name__ == '__main__':
    run()

