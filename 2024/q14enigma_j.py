# Note that we switched from 1 indexing to 0 indexing!!!
import re
import time
from collections import defaultdict, Counter

import trie
from unidecode import unidecode

from itertools import combinations, permutations


def do_swaps(swaps, original):
    swapped = list(original)
    for swap_from, swap_to in swaps:
        swapped[swap_from], swapped[swap_to] = swapped[swap_to], swapped[swap_from]
    return tuple(swapped)


def create_swaps(plugboard=False):
    reflector = (0, 1, 2, 3, 4, 5)
    results = set()  # use set to remove doubles

    # for plugboard swaps are not mandatory
    if plugboard:
        results.add(reflector)

    options = []
    for pair in combinations(reflector, 2):
        remaining = list(reflector)
        remaining.remove(pair[0])
        remaining.remove(pair[1])
        options.append((pair, tuple(remaining)))

    for pair, remaining in options:
        for second_pair in combinations(remaining, 2):
            third_pair = list(remaining)
            third_pair.remove(second_pair[0])
            third_pair.remove(second_pair[1])

            if plugboard:
                results.add(do_swaps([pair], reflector))
                results.add(do_swaps([pair, second_pair], reflector))
            results.add(do_swaps([pair, second_pair, third_pair], reflector))

    return results


sleutelvierkant = [
    ["O", "N", "(1|!)", "C", "S", "X"],
    ["I", "G", "L", "(3|.)", "H", "T"],
    ["(5|\")", "Z", "R", "A", "(8|,)", "D"],
    ["P", "(6|:)", "W", "E", "(2|?)", "J"],
    ["F", "K", "U", "(0| )", "Y", "Q"],
    ["(9|;)", "(7|_)", "B", "(4|')", "M", "V"]
]

legal_chars = ["O", "N", "(1|!)", "C", "S", "X", "I", "G", "L", "(3|.)", "H", "T", "(5|\")", "Z", "R", "A", "(8|,)", "D", "P", "(6|:)", "W", "E", "(2|?)", "J", "F", "K", "U", "(0| )", "Y", "Q", "(9|;)", "(7|_)", "B", "(4|')", "M", "V"]


sorted_legal_chars = sorted(legal_chars)

sorted_sleutelvierkant = []
for i in range(6):
    sorted_sleutelvierkant.append(sorted_legal_chars[i * 6: (i + 1) * 6])

print(sorted_sleutelvierkant)

# exit()

stekkerbord = (0, 1, 2, 3, 4, 5)

rotors = [
    [1, 4, 3, 5, 0, 2],
    [0, 1, 2, 3, 4, 5]
]

reflector = [4, 3, 5, 1, 0, 2]


def create_inverse(transitions):
    inverse = [0] * len(transitions)
    for i in range(len(transitions)):
        inverse[transitions[i]] = i
    return inverse


class Enigma:
    def __init__(self, sleutelvierkant, stekkerbord, rotors, reflector, start_config, wordtrie=None,
                 max_unknown_words=0):
        # load key matrix
        self.row_column_lookup = {}
        self.character_lookup = {}

        if sleutelvierkant is None:
            self.row_column_lookup = {}
            self.character_lookup = {}
        else:
            for i, characters in enumerate(sleutelvierkant):
                for j, character in enumerate(characters):
                    for c in character.replace("(", "").replace(")", "").split(
                            "|"):  # sometimes there are double characters
                        self.row_column_lookup[c] = (i, j)
                    self.character_lookup[(i, j)] = character

        # lead plugboard
        self.plugboard = {
            "forward": stekkerbord,
            "inverse": create_inverse(stekkerbord)
        }

        # rotors
        self.rotors = [{
            "forward": rotor,
            "inverse": create_inverse(rotor)
        } for rotor in rotors]

        # start config 0-5 intial rotor settings
        self.rotors_clicks = list(start_config)

        # reflector
        self.reflector = {
            "forward": reflector,
            "inverse": create_inverse(reflector)  # not really needed, just for symmetry
        }

        self.clicks = 0

        self.wordtrie = wordtrie
        if self.wordtrie is not None:
            self.current_node = wordtrie.root
        self.max_unknown_words = max_unknown_words

    def get_state(self):
        return self.clicks, self.row_column_lookup.copy(), self.character_lookup.copy()

    def set_state(self, clicks, row_column_lookup, character_lookup):
        self.clicks = clicks
        self.row_column_lookup = row_column_lookup
        self.character_lookup = character_lookup

    def propagate(self, transition, i, forward):
        return transition["forward"][i] if forward else transition["inverse"][i]

    def i_to_rotor_i(self, i, r):
        return (i + (self.rotors_clicks[r] - (self.clicks if r == 0 else self.clicks // 6))) % 6

    def rotor_i_to_i(self, i, r):
        return (i - (self.rotors_clicks[r] - (self.clicks if r == 0 else self.clicks // 6))) % 6

    def simulate_enigma(self, i, reverse=False):
        # schakelbord
        result = i
        # https://www.aivd.nl/onderwerpen/aivd-kerstpuzzel/errata
        # schakelbord aan 1 kant uit
        if reverse:
            result = self.propagate(self.plugboard, i, False)

        # rotor 1 (eventueel verdraaid)
        result = self.propagate(self.rotors[0], self.i_to_rotor_i(result, 0), True)
        result = self.rotor_i_to_i(result, 0)

        # rotor 2 (eventueel verdraaid)
        # result = self.propagate(self.rotors[1], self.i_to_rotor_i(result, 1), True)
        # result = self.rotor_i_to_i(result, 1)

        # reflector
        result = self.propagate(self.reflector, result, True)

        # rotor 2 terug
        # result = self.propagate(self.rotors[1], self.i_to_rotor_i(result, 1), False)
        # result = self.rotor_i_to_i(result, 1)

        # rotor 1 terug
        result = self.propagate(self.rotors[0], self.i_to_rotor_i(result, 0), False)
        result = self.rotor_i_to_i(result, 0)

        # schakelbord terug
        if not reverse:
            result = self.propagate(self.plugboard, result, False)  # fw or rev is same for plugboard?

        # draai aan de rotors
        self.clicks += 1

        return result

    def encode(self, message, short=True, reverse=False):
        cypher = ""
        skip = False
        for character in list(message.upper()):
            row, col = self.row_column_lookup[character]
            # print(row, col)

            enc_row, enc_col = [self.simulate_enigma(i, reverse) for i in (row, col)]
            c = self.character_lookup[(enc_row, enc_col)]

            if self.wordtrie is not None:
                # wordtrie logic
                if len(c) > 1:
                    self.current_node = self.wordtrie.root
                    skip = False
                else:
                    if not skip:
                        if c in self.current_node.children:
                            self.current_node = self.current_node.children[c]
                        else:
                            if self.max_unknown_words > 0:
                                self.max_unknown_words -= 1
                                skip = True
                            else:
                                return None

            # if len(c) > 1, reset Trie, else try to traverse the Trie if fails, break early
            # TODO: nadenken over manier om 1 of 2 onbekende woorden toe te staan

            if len(c) > 1 and short:
                c = c[1]
            cypher += c
        return cypher



message = "EEN HEEL GELUKKIG NIEUWJAAR, JOHN! DAT HET MAAR VEEL GEZONDHEID EN PUZZELPLEZIER MAG BRENGEN. EEN PERFECT KWADRAAT, DAT MOET TOCH WEL IETS BIJZONDERS WORDEN?! HOE GROOT ZOU EEN CIRKEL TROUWENS MOETEN ZIJN OM 2024 VIERKANTEN MET EEN OPPERVLAKTE 2025 ERIN TE LATEN PASSEN?"


# for reflector in create_swaps():
#     for rotor1 in permutations([0, 1, 2, 3, 4, 5]):
#         enigmini = Enigma(sorted_sleutelvierkant, (0, 1, 2, 3, 4, 5), [rotor1,
#             [0, 1, 2, 3, 4, 5]], reflector, (0, 0))
#
#         cypher = enigmini.encode(message)
#
#         if cypher.count("25") > 0 and cypher.count("24") > 0:
#             enigmini.clicks = 0  # reset
#             decoded = enigmini.encode(cypher)
#
#             print(message)
#             print(cypher)
#             print(decoded)
#             print(enigmini.row_column_lookup)
#             print(enigmini.reflector)
#             print(enigmini.rotors[0])

# EEN HEEL GELUKKIG NIEUWJAAR, JOHN! DAT HET MAAR VEEL GEZONDHEID EN PUZZELPLEZIER MAG BRENGEN. EEN PERFECT KWADRAAT, DAT MOET TOCH WEL IETS BIJZONDERS WORDEN?! HOE GROOT ZOU EEN CIRKEL TROUWENS MOETEN ZIJN OM 2024 VIERKANTEN MET EEN OPPERVLAKTE 2025 ERIN TE LATEN PASSEN?
# J0A94VJVRN06RU7F5RGWVRI85T01E8X4A8EW5ARM049ZN57RQ0VCEZJM3G3YJWW90A99FSMVC96JM9J7RHTZ9S0JYZJYO90VGE2J7UJ249UD5305T41EW5ARH8VYE4X2Y9IVCE9JA59S9EM3G3VUBRP80K0A7FRM8V950X849M3REVJYRLW0D069A0XKDJY59Z3JAVGEGFXA98B9CR7HRQWVUUNGAVGEBJARJ0A982W00QVNDAV9CR7GRJ79GE4JE65AVGE25B5JYP
# EEN0HEEL0GELUKKIG0NIEUWJAAR80JOHN10DAT0HET0MAAR0VEEL0GEZONDHEID0EN0PUZZELPLEZIER0MAG0BRENGEN30EEN0PERFECT0KWADRAAT80DAT0MOET0TOCH0WEL0IETS0BIJZONDERS0WORDEN210HOE0GROOT0ZOU0EEN0CIRKEL0TROUWENS0MOETEN0ZIJN0OM020240VIERKANTEN0MET0EEN0OPPERVLAKTE020250ERIN0TE0LATEN0PASSEN2
# {'0': (0, 0), ' ': (0, 0), '1': (0, 1), '!': (0, 1), '2': (0, 2), '?': (0, 2), '3': (0, 3), '.': (0, 3), '4': (0, 4), "'": (0, 4), '5': (0, 5), '"': (0, 5), '6': (1, 0), ':': (1, 0), '7': (1, 1), '_': (1, 1), '8': (1, 2), ',': (1, 2), '9': (1, 3), ';': (1, 3), 'A': (1, 4), 'B': (1, 5), 'C': (2, 0), 'D': (2, 1), 'E': (2, 2), 'F': (2, 3), 'G': (2, 4), 'H': (2, 5), 'I': (3, 0), 'J': (3, 1), 'K': (3, 2), 'L': (3, 3), 'M': (3, 4), 'N': (3, 5), 'O': (4, 0), 'P': (4, 1), 'Q': (4, 2), 'R': (4, 3), 'S': (4, 4), 'T': (4, 5), 'U': (5, 0), 'V': (5, 1), 'W': (5, 2), 'X': (5, 3), 'Y': (5, 4), 'Z': (5, 5)}
# {'forward': (4, 2, 1, 5, 0, 3), 'inverse': [4, 2, 1, 5, 0, 3]}
# {'forward': (3, 5, 4, 0, 1, 2), 'inverse': [3, 4, 5, 0, 2, 1]}

# J0A94VJVRN06RU7F5RGWVRI85T01E8X4A8EW5ARM049ZN57RQ0VCEZJM3G3YJWW90A99FSMVC96JM9J7RHTZ9S0JYZJYO90VGE2J7UJ249UD5305T41EW5ARH8VYE4X2Y9IVCE9JA59S9EM3G3VUBRP80K0A7FRM8V950X849M3REVJYRLW0D069A0XKDJY59Z3JAVGEGFXA98B9CR7HRQWVUUNGAVGEBJARJ0A982W00QVNDAV9CR7GRJ79GE4JE65AVGE25B5JYP

# Geen stekkerbord, een sleutelvierkant op alfabetische volgorde en maar één rotor verbonden met de reflector, want willen het jaar natuurlijk niet te moeilijk beginnen :-)



# 1370925

enigmini = Enigma(sorted_sleutelvierkant, (0, 1, 2, 3, 4, 5), [(1, 3, 7, 0, 4, 2, 5),
            [0, 1, 2, 3, 4, 5]], reflector, (0, 0))

print(enigmini.encode("J0A94VJVRN06RU7F5RGWVRI85T01E8X4A8EW5ARM049ZN57RQ0VCEZJM3G3YJWW90A99FSMVC96JM9J7RHTZ9S0JYZJYO90VGE2J7UJ249UD5305T41EW5ARH8VYE4X2Y9IVCE9JA59S9EM3G3VUBRP80K0A7FRM8V950X849M3REVJYRLW0D069A0XKDJY59Z3JAVGEGFXA98B9CR7HRQWVUUNGAVGEBJARJ0A982W00QVNDAV9CR7GRJ79GE4JE65AVGE25B5JYP"))