from itertools import permutations, combinations

import random

wordslist = set()

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
        wordslist.add(word)


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
    # "BOTJURIST",
    "KLEMVAST",
    # "SPOELING",
    "VRAAGSPEL",
    "PERKDUO"]

# words_b = ["RETEGOED"]

# words_b = ["KTZSZEPERUL", "KTLSLIANRAE", "RSHFZCNNZAAE", "AETADIRILANNONTAN", "KRCANIMIRYT"]

# words_b = ["WEGHART", "MESALSPAN", "WESPSORRYGRENS"]

# for word_b in words_b:
#     print(word_b)
#     for char in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#         for word in permutations(word_b + char):
#             if word in wordslist:
#                 print("Found", word)

# words_b.sort(key=len)
for word in words_b:
    for added_letters in ['EU', 'RO', 'PA']: # ['']: #
        letters = list(word + added_letters)
        random.shuffle(letters)
        print("".join(letters), f" ({added_letters})", end='  ')
    print(f"{word}")

#
# print("---")
# for p in permutations(list(words_b[0])):
#     print("".join(p))


