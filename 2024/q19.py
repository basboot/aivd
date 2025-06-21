import re

import trie

wordset = set()
wordlist = trie.Trie()


letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for filename in [
                "./wordlists/troonrede.txt",
                "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
                 "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
                 "./wordlists/OpenTaal-210G-flexievormen.txt",
                 # "./wordlists/english.txt",
                 # "./wordlists/test.txt",
                 ]:
    file1 = open(filename, "r")
    Lines = file1.readlines()

    for line in Lines:
        words = re.findall(r'\b\w+\b', line)

        for word in words:
            word = word.upper()

            wordset.add(word)
            wordlist.insert(word)

            if len(word) != 9:
                continue

            if word[4] != word[7]:
                continue

            if len(set(list(word))) != 8:
                continue

            print(word)

# 10 letterwoord
# Beginletter is slotletter
# 3 6 8 zelfde letter vermoedelijk E
# Loop eens langs je woordenlijst je


symbols = (BRUG, BLAUWE_P, ZOETERMEER, GEEL_RECHTS, DERTIG,
 WIT_OMLAAG, GEEL_BOCHT_RECHTS, GELE_P, INVOEGEN, ANDEHALVE_METER,
 GEEL_LINKS, VLUCHT_ROUTE, WIT_OMHOOG, TUNNEL, ROOD_LINKS,
 GROEN_BOCHT_RECHTS, GROEN_BOCHT_LINKS, VALLENDE_STENEN, ROOD_RECHTS) = range(19)

words = [
    [BRUG, BLAUWE_P, BLAUWE_P, ZOETERMEER],
    [GEEL_RECHTS, DERTIG, WIT_OMLAAG, GEEL_BOCHT_RECHTS, GELE_P] + [INVOEGEN, ANDEHALVE_METER, GELE_P, GEEL_LINKS],
    [VLUCHT_ROUTE, WIT_OMHOOG, WIT_OMHOOG, TUNNEL],
    [ZOETERMEER, ROOD_LINKS, BLAUWE_P, GROEN_BOCHT_RECHTS, GROEN_BOCHT_LINKS, BLAUWE_P, VALLENDE_STENEN, BLAUWE_P, ROOD_RECHTS, ZOETERMEER]
]


def substitution(word, substitutions):
    return "".join([substitutions[x] if x in substitutions else '?' for x in word])

def show_solution(substitutions, file, console=False):
    subs = " ".join([substitution(word, substitutions) for word in words])
    file.write(f"{subs}\n")
    if console:
        print(subs)

def try_substitutions(word_pos, letter_pos, substitutions, used, tree_node, file):
    if word_pos == len(words):
        print("FOUND")
        show_solution(substitutions, file, True)
        return

    current_word = words[word_pos]

    if letter_pos == len(current_word):
        if tree_node.is_end:
            try_substitutions(word_pos + 1, 0, substitutions, used, wordlist.root, file)
            if word_pos > 1:
                show_solution(substitutions, file)
        else:
            return
    else:
        current_letter = current_word[letter_pos]
        if current_letter in substitutions:
            if substitutions[current_letter] in tree_node.children:
                try_substitutions(word_pos, letter_pos + 1, substitutions, used, tree_node.children[substitutions[current_letter]], file)
            else:
                return
        else:
            for letter in letters:
                if letter in used or letter not in tree_node.children:
                    continue # do not use twice, and only use legal options
                else:
                    # try sub
                    next_substitutions = substitutions.copy()
                    next_used = used.copy()

                    next_substitutions[current_letter] = letter
                    next_used.add(letter)

                    try_substitutions(word_pos, letter_pos + 1, next_substitutions, next_used, tree_node.children[letter], file)



s = {}#{BRUG: 'W', BLAUWE_P: 'E', ZOETERMEER: 'S', VLUCHT_ROUTE: 'V', WIT_OMHOOG: 'O', TUNNEL: 'R'}
used = set(s.values())
with open("q19.txt", "w") as file:
    try_substitutions(0, 0, s, set(), wordlist.root, file)