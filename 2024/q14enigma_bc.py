# Note that we switched from 1 indexing to 0 indexing!!!
import time
from collections import defaultdict, Counter

import trie
from unidecode import unidecode

wordlist = trie.Trie()
n_words = 0

blacklist = {"06", "1E", "3D", "AB", "ABC", "ABCES", "ABCOUDE", "ABCS"}

for filename in [
    "./scribd/filtered-woorden2000.txt",
    "./scribd/filtered-woorden5000.txt",
    "./scribd/filtered-gpt_niet_zo_goed.txt",
    # "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
    # "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
    # "./wordlists/OpenTaal-210G-flexievormen.txt",
    # "./wordlists/english.txt",
    # "./wordlists/test.txt",
]:
    file1 = open(filename, "r")
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        # to upper, no diacritics
        word = unidecode(line.strip().upper())

        # skip single letter words
        if len(word) < 2:
            continue

        if word in blacklist:
            continue

        if not word.isalpha(): # 100-tal 1E etc.
            continue

        wordlist.insert(word)
        n_words += 1

# add combinations
numbers = [
    "0", #spatie
    # "10", # !
    # "20", # ?
    "30", # .
    # "4", #'
    # "5", #"
    # "60", #:
    #7 _
    "80", #,
    # "90", #;
]

for n in numbers:
    wordlist.insert(n)

print(f"{n_words} in trie")

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

stekkerbord = (0, 1, 2, 3, 4, 5)

rotors = [
    [1, 4, 3, 5, 0, 2],
    [2, 0, 4, 5, 1, 3]
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
        result = self.propagate(self.rotors[1], self.i_to_rotor_i(result, 1), True)
        result = self.rotor_i_to_i(result, 1)

        # reflector
        result = self.propagate(self.reflector, result, True)

        # rotor 2 terug
        result = self.propagate(self.rotors[1], self.i_to_rotor_i(result, 1), False)
        result = self.rotor_i_to_i(result, 1)

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



# message = "DEZE VOORBEELDTEKST IS VERCIJFERD MET DE ENIGMINI!"
# cypher = "KRY8D1D37CRLE9NS906LJ4D1KVT2ZDL4KHU86LF8D5AC1OYMJE"
#
# setting = (0, 0)

# print("Voorbeeld")
# enigmini = Enigma(sleutelvierkant, stekkerbord, rotors, reflector, setting)
# print(enigmini.encode(message))
#
# print("Voorbeeld, reverse test")
# enigmini = Enigma(sleutelvierkant, stekkerbord, rotors, reflector, setting)
# print(enigmini.encode(cypher, False))

# # ander stekkerbord
# print("B")
# cypher_b = "UCXOMDTVHMAXJCO6PKSJJ5P4Y18EMYUO2KOGDM31QXT31SEV8JH116"
#
# enigmini = Enigma(sleutelvierkant, (3, 2, 1, 0, 5, 4), rotors, reflector, (0, 0))
# print(enigmini.encode(cypher_b, False))


# andere reflector(s?) en rotoren
# print("C")
cypher_c = "0ULW2BHR3SJALF5P2FWCYONLHPFW7YZN84UPQWNKMTYIEYTYN2QE63SJBLFV6SQE9Y27E2"
#
# 7776000 opties
# for reflector in create_swaps():
#     print("R:", reflector)
#     for rotor1 in permutations((0, 1, 2, 3, 4, 5)):
#         for rotor2 in permutations((0, 1, 2, 3, 4, 5)):
#             enigmini = Enigma(sleutelvierkant, (3, 2, 1, 0, 5, 4), [rotor1, rotor2], reflector, (0, 0), wordlist, 0)
#             message = enigmini.encode(cypher_c, False)
#
#             if message is not None:
#                 character_sequences = re.findall(r'[a-zA-Z]+', message)
#                 long_words = list(filter(lambda w: len(w) > 4, character_sequences))
#
#                 if len(long_words) > 2:
#                     print("solution", reflector, rotor1, rotor2)

# print(cypher_c)


# # Test if encryption works with plugboard
# enigmini = Enigma(sleutelvierkant, (0, 1, 2, 3, 4, 5), [(2, 4, 1, 0, 3, 5), (3, 1, 5, 0, 4, 2)], (4, 2, 1, 5, 0, 3), (0, 0))
# cypher = enigmini.encode("DIT IS EEN TEST", True, reverse=True)
#
# enigmini = Enigma(sleutelvierkant, (0, 1, 2, 3, 4, 5), [(0, 2, 5, 4, 1, 3), (4, 5, 3, 1, 2, 0)], (1, 0, 4, 5, 2, 3), (0, 0))
#
# for c in list(cypher):
#     message = enigmini.encode(c, True)
#     print(message, end="-")
#
#
# enigmini = Enigma(sleutelvierkant, (0, 1, 2, 3, 4, 5), [(0, 2, 5, 4, 1, 3), (4, 5, 3, 1, 2, 0)], (1, 0, 4, 5, 2, 3), (0, 0))
# message2 = enigmini.encode(cypher, True)
#
# # 89NWINF4CSWNCNI
#
# print(">>", cypher)
# print("<<", message)
# print("<<", message2)


# reflector, rotors
solutions_c = [
    ((1, 0, 4, 5, 2, 3), [(0, 2, 5, 4, 1, 3), (4, 5, 3, 1, 2, 0)]),
    ((1, 0, 4, 5, 2, 3), [(1, 3, 0, 5, 2, 4), (0, 4, 5, 3, 1, 2)]),
    ((1, 0, 4, 5, 2, 3), [(2, 4, 1, 0, 3, 5), (2, 0, 4, 5, 3, 1)]),
    ((1, 0, 4, 5, 2, 3), [(3, 5, 2, 1, 4, 0), (1, 2, 0, 4, 5, 3)]),
    ((1, 0, 4, 5, 2, 3), [(4, 0, 3, 2, 5, 1), (3, 1, 2, 0, 4, 5)]),
    ((1, 0, 4, 5, 2, 3), [(5, 1, 4, 3, 0, 2), (5, 3, 1, 2, 0, 4)]),
    ((4, 2, 1, 5, 0, 3), [(0, 2, 5, 4, 1, 3), (5, 0, 4, 2, 3, 1)]),
    ((4, 2, 1, 5, 0, 3), [(1, 3, 0, 5, 2, 4), (1, 5, 0, 4, 2, 3)]),
    ((4, 2, 1, 5, 0, 3), [(2, 4, 1, 0, 3, 5), (3, 1, 5, 0, 4, 2)]),
    ((4, 2, 1, 5, 0, 3), [(3, 5, 2, 1, 4, 0), (2, 3, 1, 5, 0, 4)]),
    ((4, 2, 1, 5, 0, 3), [(4, 0, 3, 2, 5, 1), (4, 2, 3, 1, 5, 0)]),
    ((4, 2, 1, 5, 0, 3), [(5, 1, 4, 3, 0, 2), (0, 4, 2, 3, 1, 5)]),
    ((5, 3, 4, 1, 2, 0), [(0, 2, 5, 4, 1, 3), (3, 4, 2, 0, 1, 5)]),
    ((5, 3, 4, 1, 2, 0), [(1, 3, 0, 5, 2, 4), (5, 3, 4, 2, 0, 1)]),
    ((5, 3, 4, 1, 2, 0), [(2, 4, 1, 0, 3, 5), (1, 5, 3, 4, 2, 0)]),
    ((5, 3, 4, 1, 2, 0), [(3, 5, 2, 1, 4, 0), (0, 1, 5, 3, 4, 2)]),
    ((5, 3, 4, 1, 2, 0), [(4, 0, 3, 2, 5, 1), (2, 0, 1, 5, 3, 4)]),
    ((5, 3, 4, 1, 2, 0), [(5, 1, 4, 3, 0, 2), (4, 2, 0, 1, 5, 3)]),
    ((2, 3, 0, 1, 5, 4), [(0, 2, 5, 4, 1, 3), (2, 3, 1, 5, 0, 4)]),
    ((2, 3, 0, 1, 5, 4), [(1, 3, 0, 5, 2, 4), (4, 2, 3, 1, 5, 0)]),
    ((2, 3, 0, 1, 5, 4), [(2, 4, 1, 0, 3, 5), (0, 4, 2, 3, 1, 5)]),
    ((2, 3, 0, 1, 5, 4), [(3, 5, 2, 1, 4, 0), (5, 0, 4, 2, 3, 1)]),
    ((2, 3, 0, 1, 5, 4), [(4, 0, 3, 2, 5, 1), (1, 5, 0, 4, 2, 3)]),
    ((2, 3, 0, 1, 5, 4), [(5, 1, 4, 3, 0, 2), (3, 1, 5, 0, 4, 2)]),
    ((2, 5, 0, 4, 3, 1), [(0, 2, 5, 4, 1, 3), (1, 2, 0, 4, 5, 3)]),
    ((2, 5, 0, 4, 3, 1), [(1, 3, 0, 5, 2, 4), (3, 1, 2, 0, 4, 5)]),
    ((2, 5, 0, 4, 3, 1), [(2, 4, 1, 0, 3, 5), (5, 3, 1, 2, 0, 4)]),
    ((2, 5, 0, 4, 3, 1), [(3, 5, 2, 1, 4, 0), (4, 5, 3, 1, 2, 0)]),
    ((2, 5, 0, 4, 3, 1), [(4, 0, 3, 2, 5, 1), (0, 4, 5, 3, 1, 2)]),
    ((2, 5, 0, 4, 3, 1), [(5, 1, 4, 3, 0, 2), (2, 0, 4, 5, 3, 1)]),
    ((4, 5, 3, 2, 0, 1), [(0, 2, 5, 4, 1, 3), (0, 1, 5, 3, 4, 2)]),
    ((4, 5, 3, 2, 0, 1), [(1, 3, 0, 5, 2, 4), (2, 0, 1, 5, 3, 4)]),
    ((4, 5, 3, 2, 0, 1), [(2, 4, 1, 0, 3, 5), (4, 2, 0, 1, 5, 3)]),
    ((4, 5, 3, 2, 0, 1), [(3, 5, 2, 1, 4, 0), (3, 4, 2, 0, 1, 5)]),
    ((4, 5, 3, 2, 0, 1), [(4, 0, 3, 2, 5, 1), (5, 3, 4, 2, 0, 1)]),
    ((4, 5, 3, 2, 0, 1), [(5, 1, 4, 3, 0, 2), (1, 5, 3, 4, 2, 0)])
]

cypher_d = "7RBNG4ACEK83YHUZLODARRHEZ3WT8URC4EC3XAQR448CW7NZK434K977B36D7ZEZRBU6PK" + \
           "CCXDSUC4E6QXZ7FZRVYOCEJK3N8AOTEUR44O6Q6AJH4UZ4ONAB8RUEGHEAZPULMBO7RBIQ" + \
           "UTKW78JJCWMKWOCSH6O73YONBV644CEDABR44CDYLR7HUUEC2XS6HIU7L03NBRLJ3CCUP"



# Checked: all configs give same solution :-)
for reflector, rotors in solutions_c:
    enigmini = Enigma(sleutelvierkant, (0, 1, 2, 3, 4, 5), rotors, reflector, (0, 0))

    # rc_lookup = {'7': (0, 0), '0': (3, 3), 'R': (0, 1), '1': (1, 2), 'B': (0, 2), '2': (2, 5), 'N': (0, 3), '3': (1, 5),
    #          'G': (0, 4), '4': (3, 0), 'A': (0, 5), '5': (4, 2), 'C': (1, 0), '6': (3, 2), 'E': (1, 1), 'K': (1, 3),
    #          '8': (4, 0), 'Y': (1, 4), 'H': (2, 0), '9': (5, 4), 'U': (2, 1), 'Z': (2, 2), 'D': (3, 5), 'L': (2, 3),
    #          'O': (2, 4), 'F': (5, 2), 'W': (4, 1), 'T': (5, 3), 'M': (4, 4), 'X': (5, 0), 'Q': (5, 1), 'I': (4, 3),
    #          'P': (5, 5), 'S': (4, 5), 'V': (3, 1), 'J': (3, 4)}
    # c_lookup = {(0, 0): '7', (3, 3): '0', (0, 1): 'R', (1, 2): '1', (0, 2): 'B', (2, 5): '2', (0, 3): 'N', (1, 5): '3',
    #            (0, 4): 'G', (3, 0): '4', (0, 5): 'A', (4, 2): '5', (1, 0): 'C', (3, 2): '6', (1, 1): 'E', (1, 3): 'K',
    #            (4, 0): '8', (1, 4): 'Y', (2, 0): 'H', (5, 4): '9', (2, 1): 'U', (2, 2): 'Z', (3, 5): 'D', (2, 3): 'L',
    #            (2, 4): 'O', (5, 2): 'F', (4, 1): 'W', (5, 3): 'T', (4, 4): 'M', (5, 0): 'X', (5, 1): 'Q', (4, 3): 'I',
    #            (5, 5): 'P', (4, 5): 'S', (3, 1): 'V', (3, 4): 'J'}
    # #
    #
    # enigmini.row_column_lookup = rc_lookup
    # enigmini.character_lookup = c_lookup
    # message = enigmini.encode(cypher_d, True)
    # print(message)
    #
    # enigmini.clicks = 0
    # message = enigmini.encode(message, True)
    # print("<", message)
    # print(">", cypher_d)
    break # only need one
# exit()

enigmini_test = Enigma(sleutelvierkant, (0, 1, 2, 3, 4, 5), solutions_c[0][1], solutions_c[0][0], (0, 0))

def show_message(m):
    print(m[0:70])
    print(m[71:140])
    print(m[140:])

show_message(cypher_d)


# kunnen simulate gebruiken
# eerst zonder wordtrie proberen

# !!!
# row_column_lookup[c] = (i, j)
# character_lookup[(i, j)] = character


# enigmini contains correct settings now

letters = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class Solution:
    def __init__(self):
        self.char_to_row_column_lookup = {} # lookup row and column for char
        self.row_column_to_character_lookup = {} # lookup char for row and column

    def is_used(self, c):
        return c in self.char_to_row_column_lookup

    def all_legal_chars(self):
        for c in letters:
            if c in self.char_to_row_column_lookup:
                continue # cannot use same letter twice

            yield c

    def all_legal_positions(self):
        for i in range(6):
            for j in range(6):
                if (i, j) in self.row_column_to_character_lookup:
                    continue
                yield i, j

    def use(self, c, row, column):
        assert c not in self.char_to_row_column_lookup, "something went wrong, trying to use char a second time"
        assert (row, column) not in self.row_column_to_character_lookup, "something went wrong, trying to use pos a second time"

        self.char_to_row_column_lookup[c] = (row, column)  # lookup row and column for char
        self.row_column_to_character_lookup[(row, column)] = c  # lookup char for row and column

    def un_use(self, c, row, column):
        assert c in self.char_to_row_column_lookup, "something went wrong, trying to remove unused char"
        assert (row, column) in self.row_column_to_character_lookup, "something went wrong, trying to remove empty pos"

        self.char_to_row_column_lookup.pop(c)
        self.row_column_to_character_lookup.pop((row, column))

    def __repr__(self):
        return f"row_column_lookup = {self.char_to_row_column_lookup}\ncharacter_lookup = {self.row_column_to_character_lookup}"


def try_m(enigmini: Enigma, position, cypher, solution: Solution, tree_node, tree_root, m, length_last_word, result):
    if m.isnumeric() and position == 0:
        return # forbid non alfa at pos 0

    #
    # # with wordtrie
    #
    # # continue word
    # if m in tree_node.children and m.isnumeric() != result:
    #     crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_node.children[m], tree_root, length_last_word + 1, result)
    #
    # # start new word if possible
    # if tree_node.is_end and m in tree_root.children:
    #     # next_result = result.copy(
    #     # next_result.append(length_last_word + 1)
    #     crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_root.children[m], tree_root, 0, not result)
    #
    #
    #
    # # # pattern 2-10 alpha, 1-2 non alpha
    # if m.isalpha():
    #     if result == "alpha":
    #         if length_last_word < 10:
    #             crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_node, tree_root, length_last_word + 1,
    #                                   "alpha")
    #     if result == "num":
    #         crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_node, tree_root,
    #                                   1,
    #                                   "alpha")
    # else:
    #     if m == "0": # only spaces
    #         if result == "alpha":
    #             if length_last_word > 1:
    #                 crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_node, tree_root,
    #                                       1,
    #                                       "num")
            # if result == "num":
            #     if length_last_word < 2:
            #         crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_node, tree_root,
            #                               length_last_word + 1,
            #                               "num")

    # TODO: find better way to invalidate solutions!

    next_result = result

    crack_sleutelvierkant(enigmini, position + 1, cypher, solution, tree_node, tree_root,
                          0, next_result)


def find_all_m(enigmini: Enigma, position, cypher, solution: Solution, tree_node, tree_root, length_last_word, result):
    c = cypher[position]
    enigmini.clicks = position * 2 # we want to be able to solve out of order
    row_c, col_c = solution.char_to_row_column_lookup[c]
    row_m, col_m = enigmini.simulate_enigma(row_c), enigmini.simulate_enigma(col_c)

    if (row_m, col_m) in solution.row_column_to_character_lookup:
        m = solution.row_column_to_character_lookup[(row_m, col_m)]
        # nothing changed in solution
        try_m(enigmini, position, cypher, solution, tree_node, tree_root, m, length_last_word, result)
    else:
        for m in solution.all_legal_chars():
            # add to solution
            solution.use(m, row_m, col_m)

            try_m(enigmini, position, cypher, solution, tree_node, tree_root, m, length_last_word, result)

            # cleanup changes
            solution.un_use(m, row_m, col_m)

    return False

max_depth = 0

def is_c_possible(enigmini, c, m, position, solution: Solution):
    enigmini.clicks = position * 2  # we want to be able to solve out of order
    row_c, col_c = solution.char_to_row_column_lookup[c]
    row_m, col_m = enigmini.simulate_enigma(row_c), enigmini.simulate_enigma(col_c)

    if (row_m, col_m) in solution.row_column_to_character_lookup:
        # mapping must be correct
        return solution.row_column_to_character_lookup[(row_m, col_m)] == m, row_m, col_m
    else:
        # or mapping must be possible
        return m not in solution.char_to_row_column_lookup, row_m, col_m


def fix_partial_solution(enigmini, current_fix, fixed_positions, cypher, solution: Solution):
    if current_fix == len(fixed_positions):
        yield solution

    else:

        position, m = fixed_positions[current_fix]
        c = cypher[position]

        if solution.is_used(c):
            # no change needed check m
            if is_c_possible(enigmini, c, m, position, solution):
                yield from fix_partial_solution(enigmini, current_fix + 1, fixed_positions, cypher, solution)
        else:
            for row, col in solution.all_legal_positions():
                solution.use(c, row, col)
                # check m
                is_option, row_m, col_m = is_c_possible(enigmini, c, m, position, solution)
                if is_option:
                    if m not in solution.char_to_row_column_lookup:
                        solution.use(m, row_m, col_m)
                        yield from fix_partial_solution(enigmini, current_fix + 1, fixed_positions, cypher, solution)
                        solution.un_use(m, row_m, col_m)
                    else:
                        yield from fix_partial_solution(enigmini, current_fix + 1, fixed_positions, cypher, solution)
                # remove
                solution.un_use(c, row, col)



def crack_sleutelvierkant(enigmini, position, cypher, solution: Solution, tree_node, tree_root, length_last_word, result):
    global max_depth
    if position > max_depth:
        max_depth = position
        enigmini_test.clicks = 0
        for i in range(position):
            r, c = solution.char_to_row_column_lookup[cypher[i]]
            r, c = enigmini_test.simulate_enigma(r), enigmini_test.simulate_enigma(c)
            print(solution.row_column_to_character_lookup[(r, c)], end="")
        print()
    if position < max_depth - 10:
        max_depth = position

    if position == len(cypher):
        # full cypher in sleutelvierkant
        print(solution)
        enigmini_test.clicks = 0
        for i in range(position):
            r, c = solution.char_to_row_column_lookup[cypher[i]]
            r, c = enigmini_test.simulate_enigma(r), enigmini_test.simulate_enigma(c)
            print(solution.row_column_to_character_lookup[(r, c)], end="")
        print()
        exit()
        return


    c = cypher[position]

    if solution.is_used(c):
        # no change needed check m
        find_all_m(enigmini, position, cypher, solution, tree_node, tree_root, length_last_word, result)
    else:
        for row, col in solution.all_legal_positions():
            solution.use(c, row, col)
            # check m
            find_all_m(enigmini, position, cypher, solution, tree_node, tree_root, length_last_word, result)
            # remove
            solution.un_use(c, row, col)




# TODO: meet diepte van resultaat
# TODO: sta onbekende woorden toe

s = Solution()

i = 0
for s in fix_partial_solution(enigmini, 0, [(3, "0"), (6, "0"), (9, "0"), (len(cypher_d) - 1, "3")], cypher_d, s):
    print(i)
    i += 1
    print(s)
    break


print(time.time())
wordlist.root.is_end = False # avoid empty words
crack_sleutelvierkant(enigmini, 0, cypher_d, s, wordlist.root, wordlist.root, 0, True)


# print("".join(sorted(list(set(list(cypher_d))))))


enigmini.row_column_lookup = {'7': (0, 0), 'A': (3, 3), 'R': (0, 1), 'B': (1, 2), 'C': (3, 5), 'N': (0, 2), 'D': (1, 0), 'G': (0, 3), 'E': (3, 1), '4': (0, 4), 'F': (4, 3), 'H': (2, 1), 'I': (1, 3), 'J': (5, 5), 'K': (0, 5), '8': (1, 1), '3': (1, 4), 'L': (3, 0), 'Y': (1, 5), 'M': (5, 3), 'U': (2, 0), 'Z': (2, 2), 'O': (2, 3), 'P': (4, 0), 'Q': (5, 4), 'W': (2, 4), 'S': (4, 2), 'T': (2, 5), 'V': (5, 1), 'X': (3, 2), '9': (3, 4), '2': (5, 2), '6': (4, 1), '5': (4, 4), '1': (4, 5), '0': (5, 0)}
enigmini.character_lookup = {(0, 0): '7', (3, 3): 'A', (0, 1): 'R', (1, 2): 'B', (3, 5): 'C', (0, 2): 'N', (1, 0): 'D', (0, 3): 'G', (3, 1): 'E', (0, 4): '4', (4, 3): 'F', (2, 1): 'H', (1, 3): 'I', (5, 5): 'J', (0, 5): 'K', (1, 1): '8', (1, 4): '3', (3, 0): 'L', (1, 5): 'Y', (5, 3): 'M', (2, 0): 'U', (2, 2): 'Z', (2, 3): 'O', (4, 0): 'P', (5, 4): 'Q', (2, 4): 'W', (4, 2): 'S', (2, 5): 'T', (5, 1): 'V', (3, 2): 'X', (3, 4): '9', (5, 2): '2', (4, 1): '6', (4, 4): '5', (4, 5): '1', (5, 0): '0'}

message_d = enigmini.encode(cypher_d)



# TODO:
# werkt een oplossing van d voor alle c's hetzelfde? ja
# zijn restrictie r/c redundant?
# kloppen de restricties voor een oplossing?
# maak function om sleutelvierkant te maken van lookup





