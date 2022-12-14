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

scores = {
    'X': 0,
    'Y': 3,
    'Z': 6,
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2,
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3,
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1,
    }
}

def run(inp):
    score = 0

    for line in inp:
        a, b = line.split(' ')
        score += scores[b]
        score += scores[a][b]

    return score
