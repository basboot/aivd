from collections import Counter

file1 = open('straattaal.txt', 'r')
lines = file1.readlines()

words = []
for line in lines:
    word, _ = line.rstrip().split("\t")
    words.append((len(word), word))

words.sort()
for _, word in words:
    if len(word) == 4 and (word[1] == word[2] and word[0] != word[3]):
        print(word)

# https://www.stoppestennu.nl/chattaal-afkortingen-whatsapp-kenniscentrum-online-pesten


import random

code = "IFFQ JZJ FKLSCH",  "IFFQ DD GIIHR GGK ZH FGKS",  "IFFQ JZJ JGRFHQ LM",  "KGZA"

substitutions = {}
for i in range(26):
    substitutions[chr(ord('A') + i)] = chr(ord('A') + i)

substitutions[" "] = " "

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Characters")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 40)

# Calculate positions for the characters
char_positions = []
x, y = 20, 100  # Starting position
spacing = 30    # Space between characters

x_offsets = [140, 0, 90, 300]

for i, line in enumerate(code):
    for j, char in enumerate(line):
        for n in range(2):
            char_surface = font.render(char, True, BLACK)
            char_rect = char_surface.get_rect(topleft=(x + spacing * j + x_offsets[i], y + (spacing + 10) * i + n * 200))
            char_positions.append(((i, j, n), char_rect))

sub_counts = Counter(substitutions.values())

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw characters
    for position, char_rect in char_positions:
        i, j, n = position
        if n == 0:
            char = substitutions[code[i][j]]
            if sub_counts[char] > 1:
                color = (255, 0, 0)
            else:
                color = (0, 0, 0)
            char_surface = font.render(char, True, color)
            screen.blit(char_surface, char_rect.topleft)
        else:
            char = code[i][j]
            char_surface = font.render(char, True, (125, 125, 125))
            screen.blit(char_surface, char_rect.topleft)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a character was clicked
            mouse_pos = event.pos
            for position, char_rect in char_positions:
                i, j, n = position
                if char_rect.collidepoint(mouse_pos):
                    print(f"Character at {position} clicked, is: {code[i][j]}")

                    # update
                    current_sub = substitutions[code[i][j]]
                    new_sub = chr((((ord(current_sub) - ord('A')) + 1) % 26) + ord('A'))
                    substitutions[code[i][j]] = new_sub

                    sub_counts = Counter(list(substitutions.values()))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Shuffle")
                new_subs = list(range(26))
                random.shuffle(new_subs)
                for i in range(26):
                    substitutions[chr(ord('A') + i)] = chr(ord('A') + new_subs[i])


# Quit Pygame
pygame.quit()
sys.exit()
