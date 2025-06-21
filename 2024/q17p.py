# The latitude of Easter Island,
# Chile is -27.114410, and the longitude is -109.425270.
# Easter Island, Chile is located at Chile country in the Islands
# place category with the gps coordinates of
# 27° 6' 51.8760'' S and 109° 25' 30.9720'' W.

# -270652 -1092531

# gps_positions = [(dms_to_decimal("270719", -1), dms_to_decimal("1092056", -1))]

# TODO: woorden met juiste aantal letters en geen dubbelen,
#  sortering van getal zelf, moet gelijk zijn aan sorteren getal aan de hand van woord

from collections import defaultdict
from itertools import combinations
import random

import random

wordslist = defaultdict(list)

for filename in [
                # "./wordlists/troonrede.txt",
                "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
                 # "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
                 # "./wordlists/OpenTaal-210G-flexievormen.txt",
                 # "./wordlists/english.txt",
                 # "./wordlists/test.txt",
                 ]:
    file1 = open(filename, "r")
    Lines = file1.readlines()

    for line in Lines:
        word = line.strip().upper()
        if not word.isalpha():
            continue
        if len(set(list(word))) == len(word): # no double chars
            wordslist[len(word)].append(word)

# print(wordslist[11])


def find_possible_words(dms_lat, dms_lon):
    results = []
    for word_lat in wordslist[len(dms_lat)]:
        for word_lon in wordslist[len(dms_lon)]:
        # print(list(word))
        # print(list(dms))

            sorted_by_alpha = [num for _, num in sorted(zip(list(word_lat + word_lon), list(dms_lat + dms_lon)))]
            sorted_by_num = sorted(dms_lat + dms_lon)

            if sorted_by_alpha == sorted_by_num:
                results.append(f"{word_lat} {word_lon}")

    return results

print(find_possible_words("270719", "1092052"))


