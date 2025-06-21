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
        word = line.strip().upper()
        if len(set(list(word))) == len(word): # no double chars
            wordslist[len(word)].append(word)

print(wordslist[11])