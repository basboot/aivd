from collections import deque

from matplotlib import pyplot as plt

from q16shingoki import plot_numbers_on_grid


black = {
    2 + 4*1j: 2,
    3 + 3*1j: 2,
    5 + 2*1j: 5,
    5 + 5*1j: 6,
}

white = {
    1 + 3*1j: 2,
    2 + 1*1j: 5,
    2 + 5*1j: 5,
    3 + 2*1j: 4,
}

# add connect options for piece
# store connect options for later use
def get_white_options(pos, length):
    return [(pos - i, pos, pos - i + length) for i in range(1, length)] + [(pos - i*1j, pos, pos - i*1j + length*1j) for i in range(1, length)]

def get_black_options(pos, length):
    return ([(pos - i, pos, pos + (length - i) * 1j) for i in range(1, length)] +
            [(pos + i, pos, pos - (length - i) * 1j) for i in range(1, length)] +
            [(pos - i, pos, pos - (length - i) * 1j) for i in range(1, length)] +
            [(pos + i, pos, pos + (length - i) * 1j) for i in range(1, length)])

def on_board(point, width, height):
    return 0 <= point.real < width and 0 <= point.imag < height

def fits_on_board(piece, board_width, board_height):
    for point in piece:
        if point.real < 0 or point.imag < 0 or point.real > board_width - 1 or point.imag > board_height - 1:
            return False
    return True

def find_all_paths(start: complex, goal: complex, used: set[complex], shape: (int, int)):
    width, height = shape

    directions = [1, -1, 1j, -1j]

    queue = deque([(start, [start])])
    all_paths = []

    while queue:
        current, path = queue.popleft()

        if current == goal:
            all_paths.append(path)
            continue

        for direction in directions:
            neighbor = current + direction
            # on board, not used (unless it is the goal), and not in current path
            if on_board(neighbor, width, height) and (neighbor not in used or neighbor == goal) and neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return all_paths


if __name__ == '__main__':
    # for option in get_black_options(0 + 0*1j, 3):
    #     print(option)
    #     print(fits_on_board(option, 5, 5))
    #
    # start = 0 + 0j
    # goal = 3 + 3j
    # used = {1 + 0j, 2 + 0j, 3 + 0j, 3 + 1j, 3 + 2j, 3 + 3j}  # Goal is in used
    # shape = (4, 4)
    #
    # paths = find_all_paths(start, goal, used, shape)
    # for i, path in enumerate(paths, 1):
    #     print(f"Path {i}: {path}")

    plot_numbers_on_grid(black, white, 5, 5)
    plt.show()