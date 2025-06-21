# copy paste hier de output van rgboku_creator.lp
balls = "red(1,1) blue(5,1) blue(5,7) blue(5,8) blue(5,9) red(2,1) red(4,1) red(4,7) red(4,8) red(4,9) red(6,1) red(6,7) red(6,8) red(6,9) red(1,0) red(2,0) red(4,0) red(4,10) red(5,0) red(5,10) green(0,1) green(0,2) green(0,5) green(0,6) green(0,7) green(0,9) green(1,10) green(2,10) green(5,5) green(6,4) green(6,5) green(8,10) green(3,0) green(6,0) green(8,0) green(9,0) green(10,1) green(10,2) green(10,7) green(10,8) red(0,0) red(0,10) red(10,0) red(10,10)"



board = {
    "red": [],
    "green": [],
    "blue": []
}

for ball in balls.split(" "):
    color, location = ball.replace(")", "").split("(")
    i, j = list(map(int, location.split(",")))
    board[color].append((i, j))



print("copy paste dit in rgboku.lp")
for color in board:
    points = "; ".join([f"{c[0]}, {c[1]}" for c in board[color]])

    print(f"{color}({points}).")

print("copy paste dit in rgboki.py")
for color in board:
    points = "; ".join([f"{c[0]}, {c[1]}" for c in board[color]])

    # print(f"{color}({points}).")
    print(f"{color}s = \"{points}\"")