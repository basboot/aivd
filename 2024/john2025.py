import re
from collections import defaultdict

# AY E A AE A IIO O A E O A O EE EEY EIOU I A IE

# words = "best wishes happy newyear good health every"
#
# word_vowels = re.sub(r'[^AEIOUY\s]', '', words.upper())
# print(word_vowels)
# exit()
#

words = defaultdict(list)


for filename in [
    # "./scribd/filtered-woorden2000.txt",
    # "./scribd/filtered-woorden5000.txt",
    # "./scribd/filtered-gpt_niet_zo_goed.txt",
    # "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
    # "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
    # "./wordlists/OpenTaal-210G-flexievormen.txt",
    # "./wordlists/english.txt",
    # "./wordlists/english_common1000.txt",
    "./wordlists/english_common5000.txt",
    # "./wordlists/test.txt",
]:
    file1 = open(filename, "r")
    lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in lines:
        word = line.rstrip().upper()
        # john version
        # word_vowels = re.sub(r'[^AEIOUY\s]', '', word)

        # normal version
        word_vowels = re.sub(r'[^AEIOU\s]', '', word)


        words[word_vowels].append(word)

# print(words)

#

#for john_vowel in "AY E A AE A IIO O A E O A O EE EEY EIOU I A IE".split(" "):
for john_vowel in "O OI I OA AY IE I".split(" "):
    print("--------")
    print(john_vowel)
    print("--------")
    print(sorted(words[john_vowel]))
