import math

square_size = 45
die_area = square_size * square_size

circle_radius = 1171
wafer_diameter = circle_radius * 2

n_dies = (math.pi * ((wafer_diameter / 2) ** 2)) / die_area - (math.pi * wafer_diameter) / (math.sqrt(2 * die_area))

print(n_dies)

max_squares = circle_radius // square_size

legal_corners = set()
for i in range(-max_squares, max_squares + 1):
    for j in range(-max_squares, max_squares + 1):
        if math.sqrt((i * square_size) ** 2 + (j * square_size) ** 2) <= circle_radius:
            legal_corners.add((i, j))

n_squares = 0

for corner in legal_corners:
    i, j = corner
    is_square = True

    for di, dj in [(1, 0), (0, 1), (1, 1)]:
        if (i + di, j + dj) not in legal_corners:
            is_square = False
    if is_square:
        n_squares += 1

print(f"#squares = {n_squares}")


print(math.sqrt(1370925))