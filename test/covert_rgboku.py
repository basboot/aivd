from numpy.random import randint

size = 50

n = {
    "red": 50,
    "green": 50,
    "blue": 10
}

board = {
    "red": [],
    "green": [],
    "blue": []
}


used = set()

for color in n:
    for _ in range(n[color]):
        i, j = randint(size + 1), randint(size + 1)

        if (i, j) not in used:
            used.add((i, j))
            board[color].append((i, j))

for color in board:
    points = "; ".join([f"{c[0]}, {c[1]}" for c in board[color]])

    print(f"{color}({points}).")
    # print(f"{color}s = \"{points}\"")

for color in board:
    points = "; ".join([f"{c[0]}, {c[1]}" for c in board[color]])

    # print(f"{color}({points}).")
    print(f"{color}s = \"{points}\"")