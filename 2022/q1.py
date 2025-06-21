#1a
import random
import itertools


def first_last(words):
    print("### first - last ###")
    for i in range(0, 7, 3):
        for word in words:
            print(word[i], end='')
        print()

    print("### first - last ###")


words = ['KITTENS', 'EXCERPT', 'ROEROMS', 'SPEKVET', 'TYPETJE', 'STERKER', 'TOPSTUK', 'ECHTERE', 'ROOSTER']

for word in words:
    #print(len(word))
    # value = 0
    # letters = {}
    # for c in word:
    #     if c in letters:
    #         letters[c]+= 1
    #     else:
    #         letters[c]=1
    # print(letters)

    print(word[0], end = ' ')
print()
# 1b

first_last(words)

words = ['KLIEDER', 'ENTREES', 'RITSELT', 'SYSTEEM', 'TERMINI', 'MARINES', 'IJSSTUK', 'STEKKIE', ]

first_last(words)


for word in words:
    #print(len(word))
    # value = 0
    # letters = {}
    # for c in word:
    #     if c in letters:
    #         letters[c]+= 1
    #     else:
    #         letters[c]=1
    # print(letters)

    #print(value)
    print(word[0], end = ' ')
print()

first_last(words)
# 1c

# https://www.geeksforgeeks.org/trie-insert-and-search/
# Python program for insert and search
# operation in a Trie

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = {}

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = key[level]

            # if current character is not present
            if not index in pCrawl.children:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key, no_end=False):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return no_end or pCrawl.isEndOfWord


tr = Trie()

for file_name in ['./opentaal-wordlist-master/elements/basiswoorden-gekeurd.txt',
                  './opentaal-wordlist-master/elements/basiswoorden-ongekeurd.txt',
                  './opentaal-wordlist-master/elements/flexies-ongekeurd.txt',
                  './opentaal-wordlist-master/elements/wordlist-ascii.txt']:
    file1 = open(file_name, 'r')
    lines = file1.readlines()

    for line in lines:
        key = line.strip()
        # we only need 7 letter uppercase words
        if len(key) != 7:
            continue
        # if not key.isalpha():
        #     continue
        key = key.upper()

        tr.insert(key)

words = ['BGNJMKY', 'BMLBCPQ', 'ECZYYLB', 'EYLENYB', 'IYLBCCJ',
         'JYQQGLE', 'QJGBGLE', 'YEMEGCI']

solutions = []

def check_word(word, letter_map, node, words, used):

    if len(word) == 0:
        # end
        if node.isEndOfWord: # or True
            if len(words) == 0:
                solutions.append(letter_map)
                return None
            else:
                return check_word(words[0], letter_map, tr.root, words[1:], used)
        else:
            return None

    letter = word[0]

    #
    # # trick to check multiple
    # if letter == '_':
    #     if node.isEndOfWord:
    #         return check_word(word[1:], letter_map, t.root)
    #     else:
    #         return False

    # mapping exist
    if letter in letter_map:
        if letter_map[letter] in node.children:
            return check_word(word[1:], letter_map, node.children[letter_map[letter]], words, used)
        else:
            return None

    # new mapping
    for child in node.children:
        # skip existing
        if letter in letter_map:
            continue
        if child in used:
            continue
        letter_map_copy = letter_map.copy()
        used_copy = used.copy()
        letter_map_copy[letter] = child
        used_copy[child] = True
        # print(child)
        result = check_word(word[1:], letter_map_copy, node.children[child], words, used_copy)
        if result is not None:
            return result

    return None


letter_map = {}
node = tr.root
result = check_word(words[0], letter_map, node, words[1:], {})
print(result)

def decrypt(word, letter_map, single=None):
    if single is not None:
        print(letter_map[word[single]], end='')
    else:
        for l in word:
            if l in letter_map:
                print(letter_map[l], end='')
            else:
                print('-', end='')
        print()


print(solutions)
for solution in solutions:
    for word in words:
        decrypt(word, solution)
    print("**")
    for word in words:
        decrypt(word, solution, 0)
    print()
    for word in words:
        decrypt(word, solution, 6)
    print()
    print("**")

# letters = ['D', 'D', 'G', 'G', 'K', 'L', 'S', 'A']
# random.shuffle(letters)
# for l in letters:
#     print(l)

words = ['B--J--Y', 'B--B--Q', 'E--Y--B', 'E--E--B', 'I--B--J',
         'J--Q--E', 'Q--B--E', 'Y--E--I', 'B??I??B']

# other approach
words_permutations = list(itertools.permutations(words[1:]))

print(len(words_permutations), "permutations")

def check_chars(a, b, c):
    chars_to_check = [a, b, c]

    # ? don;t need to be checked
    if '?' in chars_to_check:
        chars_to_check.remove('?')

    if len(chars_to_check) == 0:
        return True

    legal_char = chars_to_check.pop(0)

    for c in chars_to_check:
        if c != legal_char:
            return False


    return True

def check_sequence(words):
    # find first seq in second
    for offset in range(1, 9):
        # print("off", offset)
        for offset2 in range(1, 9):
            seq_found = True
            for position in range(9):
                first_letter = words[position][0]
                second_letter = words[(position + offset) % 9][6]
                middle_letter = words[(position + offset2) % 9][3]

                # TODO: fix
                if check_chars(first_letter, second_letter, middle_letter):
                    # print("OK")
                    if first_letter == '?':
                        words[position] = second_letter * 7
                    pass
                else:
                    seq_found = False
                    break
        if seq_found:
            print("FOUND", offset)
            print(words)
            return words
    return None


perm_solutions = set()
for words_permutation in words_permutations:
    s = check_sequence(list((words[0],) + words_permutation))
    if s is not None:
        t = ""
        for w in s:
            t = t + w[0]
        perm_solutions.add(t)

print("#", len(perm_solutions))

def check_kerst(word, offset):
    pass
    kerst_map = {}
    kerst = 'kerst'
    for i in range(5):
        kerst_map[word[(i + offset) % 9]] = kerst[i]

    for i in range(9):
        l = word[(i + offset) % 9]
        if l in kerst_map:
            print(kerst_map[l], end='')
        else:
            print("*", end='')
    print(" <- ", word)

    # extra
    for word in ['BGNJMKY', 'BMLBCPQ', 'ECZYYLB', 'EYLENYB', 'IYLBCCJ',
         'JYQQGLE', 'QJGBGLE', 'YEMEGCI', '???????']:
        decrypt(word, kerst_map)
    print("********")

def check_string(word):
    different = set()
    for i in range(15):
        if word[i % 9] in different:
            different = set()
        different.add(word[i % 9])

        if len(different) > 4:
            #print("FOUND: ", len(different))
            check_kerst(word, i - 4)
            #return True
    return False

kerst_solutions = set()
for pm in perm_solutions:
    #print(pm)
    if check_string(pm):
        kerst_solutions.add(pm)

print("@@", len(kerst_solutions))


# kerstke*k <-  BYIJEBQEE
# kerst*erk <-  BYIJEBQQE
# kerst*k*r <-  BJEIQYBYE

# solution = {'B': '-', 'G': '-', 'N': '-', 'J': '?', 'M': '-', 'K': '-',
#             'Y': 'S', 'L': '-', 'C': '-', 'P': '-', 'Q': 'K', '-': '-',
#             'Z': '-', 'I': 'T', 'E': 'E'}


# for word in words:
#     decrypt(word, solution)
# print("********")


# 1d

# words = ['WARANDA', 'STAMHOUDERS', 'HULPSTOFFEN', 'RITSIJZERS', 'ASGATEN']

# for solution in solutions:
#     for word in words:
#         decrypt(word, solution)
#     print("********")

#

# kerstenen
# kerstkoek
# kerstkoor
# kerstrede
# kerstroos
# kerstster
# kerststuk
# kerstweek
# kerstweer


# kerstbals
# kerstblok
# kerstboek
# kerstboom
# kerstdorp
# kerstende
# kerstenen
# kerstfilm
# kerstgala
# kerstgave
# kersthits
# kerstiger
# kerstigst
# kerstkilo
# Kerstkind
# kerstklok
# kerstkoek
# kerstkoor
# kerstkrib
# kerstlied
# kerstlint
# kerstmaal
# kerstmenu
# kerstmuts
# kerstpost
# kerstrede
# kerstroos
# kerstshow
# kerstspel
# kerststal
# kerstster
# kerststol
# kerststuk
# kersttijd
# kersttimp
# kersttips
# kersttooi
# kersttulp
# kerstvuur
# kerstweek
# kerstweer
# kerstwens
# kerstzang




