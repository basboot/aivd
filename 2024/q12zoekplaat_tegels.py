from itertools import permutations

import numpy as np
import matplotlib.pyplot as plt

# ChatGPT, fingers crossed
braille_dict = {
    # Letters A-Z
    ((1, 0), (0, 0), (0, 0)): 'A',
    ((1, 0), (1, 0), (0, 0)): 'B',
    ((1, 1), (0, 0), (0, 0)): 'C',
    ((1, 1), (0, 1), (0, 0)): 'D',
    ((1, 0), (0, 1), (0, 0)): 'E',
    ((1, 1), (1, 0), (0, 0)): 'F',
    ((1, 1), (1, 1), (0, 0)): 'G',
    ((1, 0), (1, 1), (0, 0)): 'H',
    ((0, 1), (1, 0), (0, 0)): 'I',
    ((0, 1), (1, 1), (0, 0)): 'J',
    ((1, 0), (0, 0), (1, 0)): 'K',
    ((1, 0), (1, 0), (1, 0)): 'L',
    ((1, 1), (0, 0), (1, 0)): 'M',
    ((1, 1), (0, 1), (1, 0)): 'N',
    ((1, 0), (0, 1), (1, 0)): 'O',
    ((1, 1), (1, 0), (1, 0)): 'P',
    ((1, 1), (1, 1), (1, 0)): 'Q',
    ((1, 0), (1, 1), (1, 0)): 'R',
    ((0, 1), (1, 0), (1, 0)): 'S',
    ((0, 1), (1, 1), (1, 0)): 'T',
    ((1, 0), (0, 0), (1, 1)): 'U',
    ((1, 0), (1, 0), (1, 1)): 'V',
    ((0, 1), (1, 1), (0, 1)): 'W',
    ((1, 1), (0, 0), (1, 1)): 'X',
    ((1, 1), (0, 1), (1, 1)): 'Y',
    ((1, 0), (0, 1), (1, 1)): 'Z'
}

w, g = 0, 1

stacks = {
    # "wall": "ggw", #3

    "orange": "wwwwgwgw", #8

    "red": "gwgwwgwg", #8

    "green": "wwwggwwg", #8

    "purple": "ggw" + "ggggg", #5

    "yellow": "wggwgggg", #8

    "blue": "gwwwwggw" #8
}

# cyan beginnen (like tiles)
# magenta missing ???



start = ["purple"]

circle = ["green", "yellow", "orange", "red", "blue"]



for perm_circle in permutations(circle):


    tiles = "".join([stacks[x] for x in start + list(perm_circle)])

    dots = [1 if x == 'w' else 0 for x in list(tiles)]

    # print(dots)
    #
    wall = np.flip(np.reshape(dots, (6, 8)), axis=0)
    #
    # print(wall)
    #
    # # Get the dimensions of the array

    no_errors = True
    for i in range(0, 6, 3):
        for j in range(0, 8, 2):
            c = tuple(tuple(row) for row in wall[i:i+3, j:j+2])
            if c in braille_dict:
                pass
                # print(braille_dict[c])
            else:
                # print("?")
                no_errors = False

    if no_errors:
        print("Found option")
        print(perm_circle)
        for i in range(0, 6, 3):
            for j in range(0, 8, 2):
                c = tuple(tuple(row) for row in wall[i:i + 3, j:j + 2])
                if c in braille_dict:
                    print(braille_dict[c], end="")

        rows, cols = wall.shape

        # Create the figure and axes
        fig, ax = plt.subplots()

        # Draw the grid
        for row in range(rows + 1):
            ax.plot([0, cols], [row, row], color='black', linewidth=1)  # Horizontal lines
        for col in range(cols + 1):
            ax.plot([col, col], [0, rows], color='black', linewidth=1)  # Vertical lines

        # Draw sea green background for cells with 0
        for row in range(rows):
            for col in range(cols):
                if wall[row, col] == 0:
                    rect = plt.Rectangle((col, rows - row - 1), 1, 1, color='seagreen', alpha=0.5)
                    ax.add_artist(rect)

        # Draw black circles for cells with 1
        for row in range(rows):
            for col in range(cols):
                if wall[row, col] == 1:
                    circle = plt.Circle((col + 0.5, rows - row - 0.5), 0.3, color='black')  # Adjust circle size
                    ax.add_artist(circle)

        # Set the aspect ratio and limits
        ax.set_aspect('equal')
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        ax.axis('off')  # Turn off the axes

        # Show the plot
        plt.show()


