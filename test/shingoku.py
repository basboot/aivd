import matplotlib.pyplot as plt
import numpy as np

size = 5

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xticks(np.arange(size + 1))
ax.set_yticks(np.arange(size + 1))
ax.grid(which="both", color="black", linestyle="-", linewidth=1)
ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
ax.set_frame_on(False)

# Define ball positions and colors

blacks = "2, 0, 4; 4, 1, 2; 0, 3, 5; 3, 3, 3; 0, 4, 3; 4, 5, 3"
whites = "2, 2, 2; 2, 5, 3"




# Define and draw edges

# copy paste hier de output van rgboki.py
edges_string = "edge(1,0,0,0) edge(1,4,0,4) edge(2,2,1,2) edge(2,4,1,4) edge(3,0,2,0) edge(3,2,2,2) edge(4,0,3,0) edge(5,0,4,0) edge(5,2,4,2) edge(1,1,1,0) edge(1,2,1,1) edge(3,4,3,3) edge(3,5,3,4) edge(4,2,4,1) edge(5,1,5,0) edge(5,3,5,2) edge(5,4,5,3) edge(5,5,5,4) edge(0,0,0,1) edge(0,1,0,2) edge(0,2,0,3) edge(0,4,0,5) edge(2,0,2,1) edge(2,3,2,4) edge(3,1,3,2) edge(4,3,4,4) edge(4,4,4,5) edge(0,3,1,3) edge(0,5,1,5) edge(1,3,2,3) edge(1,5,2,5) edge(2,1,3,1) edge(2,5,3,5) edge(3,3,4,3) edge(4,1,5,1) edge(4,5,5,5)"
edges = [list(map(int, edge.split(","))) for edge in edges_string.replace("edge(", "").replace(")", "").split(" ")]
for x1, y1, x2, y2 in edges:
    ax.plot([y1, y2], [size - x1, size - x2], color='black', linewidth=2)


balls = {"black": [map(int, r.split(", ")) for r in blacks.split("; ")], "white": [map(int, r.split(", ")) for r in whites.split("; ")]}
for color, positions in balls.items():
    for (x, y, n) in positions:
        ax.plot(y, size - x, 'o', color=color, markersize=20, markeredgecolor='black', markeredgewidth=2)  # Black outline
        ax.text(y, size - x, str(n), color='black' if color == 'white' else 'white', ha='center', va='center', fontsize=10)  # Number in the middle

# plt.savefig("rgboku.pdf", format="pdf", bbox_inches="tight")
plt.show()