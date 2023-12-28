import re
from collections import deque
from copy import deepcopy

import networkx as nx
import matplotlib.pyplot as plt

BLACK, YELLOW, GREEN, ORANGE, LIGHT_BLUE, DARK_BLUE, PINK, RED = 0, 1, 2, 3, 4, 5, 6, 7
puzzle = {
    BLACK : [(0, 0)],
    YELLOW : [(1, 2), (2, 9), (9, 9), (9, 16), (14,15), (15, 15), (15, 7), (7, 8), (7, 9), (8, 9), (15, 19), (19, 15), (15, 22)],
    GREEN : [(3, 9), (9, 4), (9, 14), (14, 19), (23, 19), (19, 9)],
    ORANGE : [(3, 22), (22, 9), (9, 9), (9, 17), (15, 14), (14, 11), (11, 15)],
    LIGHT_BLUE : [(4, 14), (14, 10), (10, 6), (6, 18), (18, 19), (5, 15), (15, 5), (13, 16), (20, 13), (16, 4), (25, 14)],
    DARK_BLUE : [(21, 10), (10, 19), (21, 15), (15, 19), (16, 15), (15, 8), (8, 15)],
    PINK : [(6, 9), (9, 9), (9, 22), (22, 23), (23, 19), (21, 15), (15, 22)],
    RED : [(14, 10), (10, 6), (6, 11), (11, 12), (12, 15), (15, 10), (10, 21), (16, 13), (13, 15)]
}



starts = {
    BLACK: [],
    YELLOW: [],
    GREEN: [],
    ORANGE: [],
    LIGHT_BLUE: [],
    DARK_BLUE: [],
    PINK: [],
    RED: []
}

# TODO: avoid solving (0, 0)

G = {}
for network in puzzle:
    G[network] = nx.DiGraph()
    for edge in puzzle[network]:
        from_node, to_node = edge
        if from_node not in G[network]:
            G[network].add_node(from_node)
        if to_node not in G[network]:
            G[network].add_node(to_node)
        G[network].add_edge(from_node, to_node)

for network in puzzle:
    # print(G[network])
    # nx.draw(G[network])
    # plt.show()

    for node in G[network].nodes:
        if len(list(G[network].predecessors(node))) == 0:
            # print(f"found start at {node}, color {network}")
            starts[network].append(node)

print(starts)

# create tries
from trie import Trie

wordlist = Trie()

# Using readlines()

def has_only_letters(tested_string):
    match = re.match("^[a-z]*$", tested_string)
    return match is not None

n_words = 0

for filename in [
                "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
                 "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
                 "./wordlists/OpenTaal-210G-flexievormen.txt",
                 #"./wordlists/english.txt",
                 # "./wordlists/test.txt",
                 ]:
    file1 = open(filename, "r")
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        word = line.strip().lower()

        if len(word) == 1: # ignore single letters
            continue

        # if not has_only_letters(word):
        #     continue

        wordlist.insert(word)
        n_words += 1

print(f"{n_words} in trie")
# 345186
# 345152 don't allow len 1
# 328793 don't allow others


# try to find words from all starts

def map_char(n, char_map, c):
    assert n not in char_map["mapping"], "mapping already exists for node"

    if c not in char_map["used"] and c.isalpha(): # can mapping be created? (ignore non alpha)
        # create copy for backtracking
        char_map = deepcopy(char_map) # TODO: check if deepcopy is needed

        char_map["used"].add(c)
        char_map["mapping"][n] = c
        return c, char_map, True
    else:
        return c, char_map, False # desired mapping not possible


# string (tree), tile (node), existing mappings, trie (node)
def get_options(G, node, char_map, trie_node):
    options = []

    # if already mapped: try
    if node in char_map["mapping"]:
        if char_map["mapping"][node] in trie_node.children:
            # ok!
            options.append((char_map, trie_node.children[char_map["mapping"][node]]))
        else: # not ok, but maybe start a new word
            if trie_node.is_end and char_map["mapping"][node] in wordlist.root.children:
                # start and end possible, ok!
                options.append((char_map, wordlist.root.children[char_map["mapping"][node]]))
    else:
        # if not already mapped: try all mappings, and try word end if possible

        for c in trie_node.children:
            c, char_map_copy, mapping_possible = map_char(node, char_map, c)
            if not mapping_possible:
                continue
            else:
                # mapping possible
                options.append((char_map_copy, trie_node.children[char_map_copy["mapping"][node]]))

        if trie_node.is_end:
            for c in wordlist.root.children:
                c, char_map_copy, mapping_possible = map_char(node, char_map, c)
                if not mapping_possible:
                    continue
                else:
                    # mapping possible
                    options.append((char_map_copy, wordlist.root.children[char_map_copy["mapping"][node]]))

    return options # [(char_map, next_node)]



def dfs(strings, mappings):

    stack = deque()

    stack.append((strings, mappings))

    while len(stack) > 0:
        strings, mappings = stack.pop()

        if len(strings) == 0: # > after last minute, stop
            print("FOUND")
            return mappings

        # explore first in list
        G, stringnode, trienode = strings[0]
        # print(G, stringnode, trienode)

        # check all possible mappings
        options = get_options(G, stringnode, mappings, trienode)
        for next_mapping, next_trienode in options:
            # TODO: this will fail if any string can end in a loop!

            # if the string ends and this is a word end, we have a solution and do not have to explore any further
            if len(G[stringnode]) == 0 and next_trienode.is_end:
                stack.append((strings[1:], next_mapping))
            else:
                # else explore other paths # avoid endless loops, not needed will be solved by trie
                for next_stringnode in G[stringnode]:
                    next_strings = [(G, next_stringnode, next_trienode)] + strings[1:]
                    stack.append((next_strings, next_mapping))

            # stack.append()


wordlist.root.is_end = False # avoid empty words

# print(dfs([(G[YELLOW], starts[YELLOW][0], wordlist.root), (G[ORANGE], starts[ORANGE][0], wordlist.root)], {"used": set(), "mapping": {}}))

strings = []
for color in starts:
    for start_node in starts[color]:
        strings.append((G[color], start_node, wordlist.root))

print(dfs(strings, {"used": set(), "mapping": {}}))


#
# try_words(G[YELLOW], starts[YELLOW][0], {"used": set(), "mapping": {}})
#
# print(wordlist.root)

# c, a, f = map_char(1, {"used": set(), "mapping": {}}, "a")
# print(a)
# print(map_char(2, a, "a"))

# for next_mapping, next_node in get_options(G[YELLOW], starts[YELLOW][0], {"used": set(), "mapping": {}}, wordlist.root):
#     print(get_options(G[YELLOW], starts[YELLOW][0], next_mapping, wordlist.root))
