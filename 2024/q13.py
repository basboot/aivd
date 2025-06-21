import random
from collections import defaultdict

word_a = ["KTZSZEPERUL", "KTLSLIANRAE", "RSHFZCNNZAAE", "AETADIRILANNONTAN", "KRCANIMIRYT"]
word_b = ["AKCIHIPSHESFYYCSLTIISJ", "EAEIATRWEINKDANRUMNKLT", "EJMGEIMGDIEP", "IENVUDIDGEASNND", "TOIRAHWFEHNSDOB"]

import trie
from unidecode import unidecode

wordtrie = trie.Trie()
n_words = 0

wordslist = defaultdict(list)
words_by_length = defaultdict(list)

for filename in [
    "./scribd/filtered-woorden2000.txt",
    # "./scribd/filtered-woorden5000.txt",
    # "./scribd/filtered-gpt_niet_zo_goed.txt",
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

        words_by_length[len(word)].append(word)

        wordslist[tuple(sorted(list(word)))].append(word)

        # wordlist.insert(word)
        n_words += 1


# def find_word(letters, tree_node, result):
#     if len(letters) == 0:
#         print(result)
#         return
#
#     for i in range(len(letters)):
#         if letters[i] in tree_node.children:
#             next_letters = letters.copy()
#             next_letters.pop(i)
#             find_word(next_letters, tree_node.children[letters[i]], result + letters[i])
#
# find_word(list(word_a[0]), wordlist.root, "")

def transpose(word, key, reverse= False):
    if reverse:
        result = ""
        sorted_key = sorted(key)
        for i in range(len(key)):
            result += word[sorted_key.index(key[i])]

        return result

    else:
        return "".join([x for _, x in sorted(zip(list(key), list(word)), reverse=reverse)])


# for word in words_by_length[11]:
#     c = transpose("KERSTPUZZEL", word)
#     if c == word_a[0]:
#         print(word)
#
#
#         # ANTICRUELTY

for word in word_b:
    if tuple(sorted(list(word))) in wordslist:
        print(f"Found: ", wordslist[tuple(sorted(list(word)))])
    shuffle_word = list(word)
    random.shuffle(shuffle_word)
    print("".join(shuffle_word))


print(transpose("kerstpuzzel", "ANTICRUELTY"))

# PSYCHISCHE AYSIJ SKILIFT



