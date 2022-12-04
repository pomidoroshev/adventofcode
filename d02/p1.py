# A|X - rock     - 1
# B|Y - paper    - 2
# C|Z - scissors - 3
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# Rock defeats Scissors
# Scissors defeats Paper
# and Paper defeats Rock.

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'Y': 3,
        'Z': 6,
        'X': 0,
    },
    'C': {
        'Z': 3,
        'X': 6,
        'Y': 0,
    }
}

def run(inp):
    score = 0

    for line in inp:
        a, b = line.split(' ')
        score += scores[b]
        score += scores[a][b]

    return score
