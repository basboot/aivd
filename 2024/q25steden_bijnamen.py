from collections import Counter

from unidecode import unidecode

file1 = open('wikisteden.txt', 'r')
file1 = open('alabama.txt', 'r')
file1 = open('newyork.txt', 'r')

lines = file1.readlines()

options = []
for line in lines:
    if len(line.split(" - ")) != 2: # ignore
        print("Incorrect format: ", line.rstrip())
        continue

    city, nicknames = line.rstrip().split(" - ")
    for nickname in nicknames.split(", "):
        options.append((city, nickname))


# Als AMSTERDAM + MOKUM geschreven kan worden als AADEKORSTU, en ROTTERDAM + POORT VAN EUROPA als ADMNOOPPTUV, wat zijn dan de volgende letterverzamelingen?
# AILNSSTTU
# ACEIKLMORRSTWYZ AADDEEIMNPRSTW DDEEEELMNOPST AAABCDEGHJLLMMNNORRRTTTTV

answers = {
    "AILNSSTTU", "ACEIKLMORRSTWYZ", "AADDEEIMNPRSTW", "DDEEEELMNOPST", "AAABCDEGHJLLMMNNORRRTTTTV"
}

def add_descriptions(desc1, desc2):
    # to upper, remove diacritics
    desc1 = unidecode(desc1.upper())
    desc2 = unidecode(desc2.upper())

    c1 = Counter(desc1)
    c2 = Counter(desc2)

    chars = list(desc1 + desc2)
    chars = set(chars)
    chars = list(chars)
    chars.sort()

    result = []
    for c in chars:
        if not c.isalnum():
            continue

        count1 = 0 if c not in c1 else c1[c]
        count2 = 0 if c not in c2 else c2[c]
        diff = abs(count1 - count2)

        for i in range(diff):
            result.append(c)

    answer = "".join(result)

    return answer, answer in answers




print(add_descriptions("AMSTERDAM", "MOKUM"))
print(add_descriptions("ROTTERDAM", "POORT VAN EUROPA"))

for city, nickname in options:
    result, correct = add_descriptions(city, nickname)
    if correct:
        print(city, nickname, result)
    else:
        pass
        # print(city, nickname, result)

# Antwerpen Diamantstad AADDEEIMNPRSTW
# Leiden Sleutelstad AILNSSTTU
# Zoetermeer Sweet Lake City ACEIKLMORRSTWYZ

# "DDEEEELMNOPST", "AAABCDEGHJLLMMNNORRRTTTTV"

# extra lijsten:
# https://pendulumedu.com/general-awareness/nicknames-of-world-cities?srsltid=AfmBOorSrqkQoqXoaBDZrM2u3cdMxVqSZdJgPJQY985opoU1yVlK93yQ

# importing the module
import wikipedia
from bs4 import BeautifulSoup


# finding result for the search
# sentences = 2 refers to numbers of line
result = wikipedia.page('List_of_city_nicknames_in_the_United_States')


soup = BeautifulSoup(result.html(), "html.parser")

wiki_links = []
for li in soup.find_all("li"):
    a = li.find("a", href=True)
    if a and a["href"].startswith("/wiki/List_of"):
        wiki_links.append(a["href"].replace("/wiki/", ""))

for item in wiki_links:
    print(">>>", item)
    exit()
    result = wikipedia.page(item)

    print(result.html())
    exit()
