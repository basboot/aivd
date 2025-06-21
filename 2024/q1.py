from collections import defaultdict
from itertools import permutations, combinations, combinations_with_replacement

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

words_a = [
    # "DRAAKJES",
    #  "DRINK",
    # "KERST",
    "KETELMAN",
    # "LEUGEN",
    # "LEZER",
    # "PECHKANS",
    # "SOS",
    # "TAMARI",
    # "TESLA",
    # "ZOEFJE"
]
words_b = [
    "BOTJURIST",
    "KLEMVAST",
    "SPOELING",
    "VRAAGSPEL",
    "PERKDUO"]

# words_b = ["RETEGOED"]
# words_b = ["KTZSZEPERUL", "KTLSLIANRAE", "RSHFZCNNZAAE", "AETADIRILANNONTAN", "KRCANIMIRYT"]
# words_b = ["WEGHART", "MESALSPAN", "WESPSORRYGRENS"]


def find_partial_match(word):
    for i in range(len(word), len(word) // 2, -1):
        for partial_word in combinations(list(word), i):
            if tuple(sorted(partial_word)) in wordslist:
                print("OPTION: ", wordslist[tuple(sorted(partial_word))])


# words_b.sort(key=len)
# for word in words_b:
#     for added_letters in ['']: # ['EU', 'RO', 'PA']: #
#         print(f">>> {word} ({added_letters})")
#         # letters = list(word + added_letters)
#         # random.shuffle(letters)
#         # print("".join(letters))
#
#         if tuple(sorted(list(word + added_letters))) in wordslist:
#             print("FOUND", wordslist[tuple(sorted(list(word + added_letters)))])
#
#         find_partial_match(word + added_letters)

#
# print("---")
# for p in permutations(list(words_b[0])):
#     print("".join(p))

for word_b in words_b:
    print(word_b)
    for char in combinations_with_replacement(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 2):
        word = word_b + "".join(char)
        if tuple(sorted(list(word))) in wordslist:
            print(f"Found: +{char}", wordslist[tuple(sorted(list(word)))])


