words = ["icpinpyirghi", "pmrqjghqrcpq", "uyypbccpzyyp"]

alphabet = [chr(ord('a') + i) for i in range(26)]

print(alphabet)
# hoofdletters eraf gehaald

for i in range(26):
    # create cesar table
    table = {}
    for j in range(26):
        table[alphabet[j]] = alphabet[(j + i) % 26]

    for word in words:
        decoded = [table[c] for c in word]
        print("".join(decoded), end="   ")

    print()
    pass

solutions = set()
for filename in [
                "./wordlists/OpenTaal-210G-basis-gekeurd.txt",
                 "./wordlists/OpenTaal-210G-basis-ongekeurd.txt",
                 "./wordlists/OpenTaal-210G-flexievormen.txt",
                #  "./wordlists/english.txt",
                #  "./wordlists/test.txt",
                 ]:
    file1 = open(filename, "r")
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        word = line.strip().lower()

        if len(word) == 12: # ignore single letters
            if word[3] == word[7]  and word[7] == word[-1] and word[0] and word > "kerkpraktijk" and word < "rotslijsters":
                print(word[0:4], word[4:])
                solutions.add(word)

print("--------------------")

print(len(solutions))

print(solutions)

# latentiefase
# legersterkte
# leidingdraad
# modeltheorie
# ombudsbureau
# omzettoename
# onderoverste
# oudervreugde
# planetenbaan
# postdistrict
# protesttocht
# raderdiertje
# raderwieltje
# radikalinski
# rattenstaart
# reïncarneren
# poetsextract
# koetsentocht
# licentiecode
# metroverkeer
# legeroverste
# picknickbank
# picknickplek
# racelicentie
# nieuwsbureau
# neder-betuwe
# nederboelare
# kloekmoedige
# leendiensten
# leergieriger
# lijndiensten
# maltraiteert
# medegedeelde
# miserabelste
# nagestreefde
# navelbreukje
# objectievere
# onbeschermde
# onderdeeltje
# ondersteunde
# ongecodeerde
# ongedateerde
# ongegeneerde
# ongelegenste
# opengesneden
# opgescheepte
# opgetogenere
# orkestreerde
# plantennamen
# platgestampt
# polemiseerde
# portretteert
# regenereerde
# roosvensters
# ogendienaren
# oneerbiedige
# pianosonaten
# rekestreerde
# luxeleventje
# knoeiboeltje
# ongepaneerde
# modewereldje
# pijnsignalen
# leesroosters
# racewereldje
# leesdossiers
# proefdiertje