import numpy as np


def letter_to_phonepad(letter):
    phonepad = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9
    }
    return phonepad.get(letter.upper(), None)

def letter_to_scrabble_points(letter):
    scrabble_points = {
        'A': 1, 'B': 3, 'C': 5, 'D': 2, 'E': 1, 'F': 4, 'G': 3, 'H': 4, 'I': 1,
        'J': 4, 'K': 3, 'L': 3, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 2,
        'S': 2, 'T': 2, 'U': 4, 'V': 4, 'W': 5, 'X': 8, 'Y': 8, 'Z': 4
    }
    return scrabble_points.get(letter.upper(), None)


def show_numbers(s):
    if s[0] == '-':  # remove minus
        s = s[1:]
    alphabet_value = [ord(x) - ord('A') + 1 for x in list(s)]
    asci_value = [ord(x) for x in list(s)]
    phone_value = [letter_to_phonepad(x) for x in list(s)]
    scrabble_value = [letter_to_scrabble_points(x) for x in list(s)]
    positional_value = [((ord(x) - ord('A')) + 1) * (i + 1) for i, x in enumerate(list(s))]
    reversed_positional_value = [((ord(x) - ord('A')) + 1) * (len(s) - i) for i, x in enumerate(list(s))]

    print(reversed_positional_value, sum(reversed_positional_value), np.prod(reversed_positional_value), end=" | ")
    print(positional_value, sum(positional_value), np.prod(positional_value), end=" | ")
    print(scrabble_value, sum(scrabble_value), np.prod(scrabble_value),end=" | ")
    print(phone_value, sum(phone_value), np.prod(phone_value),end=" | ")
    print(alphabet_value, sum(alphabet_value), np.prod(alphabet_value),end=" | ")
    print(asci_value, sum(asci_value), np.prod(asci_value),)

# aannames:
# - volgorde letters maakt niet uit
# - er zijn meerdere combinaties die dezelfde waarde opleveren
# - precisie is vast/beperkt

# Hollywood Sign op Mount Lee in Californië
# Coordinates	34°8′2.62″N 118°19′17.73″W
# 34.134061 -118.321592
# (PRATEN, -MISLUKT)

show_numbers("PRATEN")
show_numbers("MISLUKT")

# Hollywood Sign op een heuvel in Wicklow
# County
# Coordinates: 53°05′26″N 6°36′07″W
# 53.090556 -6.601944
# (SHANDY, -WITJE).

show_numbers("SHANDY")
show_numbers("WITJE")




# (VETARM, ROKJE)
# (LISSES, DOORZAT)


# begin dit jaar (PLAYER, PINCH) => dit jaar verhuisd naar X, Y (bijbelse berg, sterke drank)

# Ariake
# More specifically, you'll find the pure while cauldron, now lit with the Olympic flame, at the Yume no Ohashi bridge
# (also known as the Olympic Promenade) connecting Ariake and Odaiba.

# Ohashi bridge
# 35°37′44″N 139°47′04″E
# 35.628889 139.784444

# With the help of the Louvre, Paris 2024 has chosen to install the Olympic Cauldron in the Jardin des Tuileries,
# in the fabulous alignment of the Louvre and its Pyramid, the La Concorde obelisk and the Champs-Elysées dominated by
# the Arc de Triomphe

# Jardin des Tuileries
# Coordinates: 48°51′50″N 2°19′34″E
# 48.863889 2.326111


