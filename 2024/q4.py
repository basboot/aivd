import random
from itertools import permutations

words = [
    "DEMIWATER", # wim
    "JAKOB", #bok
    "LENTEJAS", #jet
    "PAASMALEN", #aap, #lam
    "PRASEODYMIUM", # does
    "RINGTOON", #noot
    "SUZANNE", #zus
    "TENUETJE", #teun
    "THRILLSEEKER", #kees
    "TOKOHOUDER"] #hok

random.shuffle(words)

# words.sort(key=len)
for word in words:
    print(word)

    for w in permutations(word, 3):
        print("".join(w))

    exit()

# aas