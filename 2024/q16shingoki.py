import math
from collections import defaultdict

black = {
    0 + 5*1j: 6,
    1 + 4*1j: 3,
    1 + 5*1j: 4,
    2 + 3*1j: 2,
    2 + 4*1j: 3,
    3 + 2*1j: 3,
    3 + 4*1j: 3,
    4 + 2*1j: 4,
    4 + 5*1j: 4,
    5 + 5*1j: 4,
    6 + 1*1j: 5,
    7 + 0*1j: 9,
    7 + 3*1j: 3,
    8 + 0*1j: 10,
    8 + 2*1j: 2,
    9 + 4*1j: 2,
    10 + 3*1j: 3
}

white = {
    3 + 3*1j: 2,
    4 + 3*1j: 4,
    5 + 2*1j: 4,
    5 + 3*1j: 3,
    6 + 0*1j: 5,
    6 + 2*1j: 2,
    7 + 4*1j: 2,
    10 + 1*1j: 2
}

lines = {
    (0 + 5*1j, 1 + 4*1j),
    (1 + 5*1j, 4 + 5*1j),
    (2 + 4*1j, 3 + 4*1j),
    (3 + 2*1j, 3 + 3*1j),
    (4 + 2*1j, 6 + 0*1j),
    (4 + 3*1j, 5 + 2*1j),
    (5 + 2*1j, 6 + 2*1j),
    (6 + 0*1j, 6 + 1*1j),
    (5 + 5*1j, 9 + 4*1j),
    (7 + 3*1j, 7 + 4*1j),
    (7 + 3*1j, 8 + 2*1j)
}

import matplotlib.pyplot as plt
import numpy as np

def plot_numbers_on_grid(black, white, illegal_combinations):
    # Define grid dimensions
    x_lines = np.arange(0, 11)  # 10 vertical lines
    y_lines = np.arange(0, 6)   # 5 horizontal lines

    # Draw vertical and horizontal lines
    for x in x_lines:
        ax.axvline(x, color='gray', linestyle='--', linewidth=0.8)
    for y in y_lines:
        ax.axhline(y, color='gray', linestyle='--', linewidth=0.8)

    for position, value in black.items():
        x, y = position.real, position.imag
        circle = plt.Circle((x, y), 0.2, color='black', ec='black', zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, f'{value}', color='white',
                ha='center', va='center', fontsize=8, zorder=3)

    for position, value in white.items():
        x, y = position.real, position.imag
        circle = plt.Circle((x, y), 0.2, color='white', ec='black', zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, f'{value}', color='black',
                ha='center', va='center', fontsize=8, zorder=3)

    # Draw red lines from the list of tuples
    for start, end in illegal_combinations:
        x_start, y_start = start.real, start.imag
        x_end, y_end = end.real, end.imag
        ax.plot([x_start, x_end], [y_start, y_end], color='red', linewidth=1.5, zorder=1)

    # Set grid limits
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 6)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Display the plot
    plt.gca().set_aspect('equal', adjustable='box')

def add_letter_to_grid(ax, x, y, letter):
    cell_x = x + 0.5
    cell_y = y + 0.5

    # Add the letter to the grid
    ax.text(cell_x, cell_y, letter, color='black',
            ha='center', va='center', fontsize=12, zorder=4)

    # Add the letter to the grid
    ax.text(cell_x, cell_y, letter, color='black',
            ha='center', va='center', fontsize=12, zorder=4)

# Plot to check numbers
fig, ax = plt.subplots(figsize=(8, 5))
plot_numbers_on_grid(black, white, lines)

letters = [['A', 'N', 'X', 'F', 'D', 'W', 'Q', '11', '4', '?'], list("DOXPANLPFX"), list("KOUKANSYON"), list("NZYYZLFENB"), list("DVICOIHREO")]
for y, row in enumerate(letters):
    for x, letter in enumerate(row):
        add_letter_to_grid(ax, x, y, letter)

# plt.show()

different_puzzles = defaultdict(set)

# create illegal lookup both ways
for puzzle1, puzzle2 in lines:
    different_puzzles[puzzle1].add(puzzle2)
    different_puzzles[puzzle2].add(puzzle1)

# step 1, create solver




exit()

# step 2, try to solve all combinations
n_combinations = 0
for i in range(len(white) + len(black) + 1):
    n_combinations += math.comb(len(white) + len(black), i)

print(f"Number of combinations is {n_combinations}, but contains illegal (red lines) and very unlikely (small) combinations too, so can be pruned")



