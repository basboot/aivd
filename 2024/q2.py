from collections import defaultdict
from itertools import combinations
import random

import random

wordslist = defaultdict(list)

for filename in [
                "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
                 "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
                 "./wordlists/OpenTaal-210G-flexievormen.txt",
                 # "./wordlists/english.txt",
                 # "./wordlists/test.txt",
                 ]:
    file1 = open(filename, "r")
    Lines = file1.readlines()

    for line in Lines:
        word = line.strip().upper()
        wordslist[tuple(sorted(list(word)))].append(word)

words = [
    # "KOLEN",
    # "ESSENTAK",
    # "REUK",
    # "KNOTJE",
    # "EEGA",
    # "REPOS",
    # "TRUCS",
    # "JOGDE",
    # "ELFTAL",
    # "SNIJBONEN",
    # "ALASKA",
    # "NERD",
    # "SPIER",
    "TELEVISIEGIDS",
    # "TEST",
    # "TRÈS",
    # "NEVER",
    "WINTERVINGER"
]

print(sorted(words))

print("----")

w1 = words[0]
for word1, word2 in combinations(words, 2):
    if word1 != w1:
        print("------------------")
    w12 = list(word1 + word2)
    random.shuffle(w12)
    print("".join(w12))

    if tuple(sorted(list(word1 + word2))) in wordslist:
        print("FOUND MATCH: ", end="")
        print(wordslist[tuple(sorted(list(word1 + word2)))], word1, word2)

# IETILEDEVRVISNENIGWTRGEIS
# VIERENTWINTIGDELIGSERVIES

