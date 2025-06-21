import matplotlib.pyplot as plt
import numpy as np

size = 100

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xticks(np.arange(size + 1))
ax.set_yticks(np.arange(size + 1))
ax.grid(which="both", color="black", linestyle="-", linewidth=1)
ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
ax.set_frame_on(False)

# Define ball positions and colors

# copy paste hier de output van convert_rgboku.py
reds = "1, 1; 2, 1; 4, 1; 4, 7; 4, 8; 4, 9; 6, 1; 6, 7; 6, 8; 6, 9; 1, 0; 2, 0; 4, 0; 4, 10; 5, 0; 5, 10; 0, 0; 0, 10; 10, 0; 10, 10"
greens = "0, 1; 0, 2; 0, 5; 0, 6; 0, 7; 0, 9; 1, 10; 2, 10; 5, 5; 6, 4; 6, 5; 8, 10; 3, 0; 6, 0; 8, 0; 9, 0; 10, 1; 10, 2; 10, 7; 10, 8"
blues = "5, 1; 5, 7; 5, 8; 5, 9"


balls = {"red": [map(int, r.split(", ")) for r in reds.split("; ")], "green": [map(int, r.split(", ")) for r in greens.split("; ")], "blue": [map(int, r.split(", ")) for r in blues.split("; ")]}
for color, positions in balls.items():
    for (x, y) in positions:
        ax.plot(x, y, 'o', color=color, markersize=10)

# Define and draw edges

# copy paste hier de output van rgboki.py
edges_string = "edge(1,3,0,3) edge(1,4,0,4) edge(2,2,1,2) edge(2,9,1,9) edge(3,2,2,2) edge(3,4,2,4) edge(3,5,2,5) edge(3,8,2,8) edge(4,4,3,4) edge(4,5,3,5) edge(5,2,4,2) edge(5,5,4,5) edge(5,8,4,8) edge(6,3,5,3) edge(6,5,5,5) edge(6,6,5,6) edge(6,8,5,8) edge(6,10,5,10) edge(7,3,6,3) edge(7,5,6,5) edge(7,6,6,6) edge(8,3,7,3) edge(8,6,7,6) edge(8,8,7,8) edge(8,10,7,10) edge(9,4,8,4) edge(9,5,8,5) edge(9,8,8,8) edge(9,10,8,10) edge(10,10,9,10) edge(0,1,0,0) edge(0,2,0,1) edge(0,3,0,2) edge(1,5,1,4) edge(1,6,1,5) edge(1,7,1,6) edge(1,8,1,7) edge(1,9,1,8) edge(2,1,2,0) edge(2,4,2,3) edge(3,3,3,2) edge(4,8,4,7) edge(4,10,4,9) edge(5,1,5,0) edge(5,9,5,8) edge(5,10,5,9) edge(7,2,7,1) edge(7,8,7,7) edge(7,10,7,9) edge(8,4,8,3) edge(9,6,9,5) edge(9,7,9,6) edge(9,9,9,8) edge(0,4,0,5) edge(0,5,0,6) edge(0,6,0,7) edge(0,7,0,8) edge(0,8,0,9) edge(0,9,0,10) edge(1,0,1,1) edge(1,2,1,3) edge(2,5,2,6) edge(2,6,2,7) edge(2,8,2,9) edge(3,7,3,8) edge(4,0,4,1) edge(4,2,4,3) edge(4,3,4,4) edge(5,1,5,2) edge(5,3,5,4) edge(5,6,5,7) edge(5,7,5,8) edge(6,1,6,2) edge(6,7,6,8) edge(6,9,6,10) edge(7,4,7,5) edge(8,1,8,2) edge(8,5,8,6) edge(9,2,9,3) edge(9,3,9,4) edge(10,0,10,1) edge(10,1,10,2) edge(10,2,10,3) edge(10,3,10,4) edge(10,4,10,5) edge(10,5,10,6) edge(10,6,10,7) edge(10,7,10,8) edge(10,8,10,9) edge(10,9,10,10) edge(0,0,1,0) edge(0,10,1,10) edge(1,1,2,1) edge(1,10,2,10) edge(2,0,3,0) edge(2,3,3,3) edge(2,7,3,7) edge(2,10,3,10) edge(3,0,4,0) edge(3,10,4,10) edge(4,1,5,1) edge(4,7,5,7) edge(4,9,5,9) edge(5,0,6,0) edge(5,1,6,1) edge(5,4,6,4) edge(5,7,6,7) edge(5,9,6,9) edge(6,0,7,0) edge(6,2,7,2) edge(6,4,7,4) edge(7,0,8,0) edge(7,1,8,1) edge(7,7,8,7) edge(7,9,8,9) edge(8,0,9,0) edge(8,2,9,2) edge(8,7,9,7) edge(8,9,9,9) edge(9,0,10,0)"
edges = [list(map(int, edge.split(","))) for edge in edges_string.replace("edge(", "").replace(")", "").split(" ")]
for x1, y1, x2, y2 in edges:
    ax.plot([x1, x2], [y1, y2], color='black', linewidth=2)

plt.savefig("rgboku.pdf", format="pdf", bbox_inches="tight")
