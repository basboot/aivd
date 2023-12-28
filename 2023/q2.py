MUIS = "muis"
FLAMINGO = "flamingo"
EGEL = "egel"
HAAI = "haai"
KERSTMAN = "kerstman"
TELEFOON = "telefoon"
MAHJONG = "mahjong" #TODO: check orientation
BEER = "beer"
DRAAK = "draak"
LAMP = "lamp"
GIRAFFE = "giraffe"
OLIFANT = "olifant"
PARAPLU = "paraplu"
ROOS = "roos"
UIL = "uil"
COCKTAIL = "cocktail"
VLEERMUIS = "vleermuis"
JURK = "jurk"
AARDBEI = "aardbei" #TODO: check orientation
ZEBRA = "zebra"

code = [
    (MUIS, 0),
    (FLAMINGO, 1),
    (FLAMINGO, 7),
    (EGEL, 4),
    (HAAI, 0),
    (KERSTMAN, 2),
    (TELEFOON, 0),
    (MAHJONG, 1),
    (MAHJONG, 4),
    (MUIS, 7),
    (BEER, 6),
    (DRAAK, 7),
    (LAMP, 6),
    (GIRAFFE, 2),
    (DRAAK, 0),
    (FLAMINGO, 1),
    (OLIFANT, 5),
    (PARAPLU, 4),
    (MAHJONG, 4),
    (ROOS, 4),
    (DRAAK, 0),
    (UIL, 2),
    (COCKTAIL, 6),
    (VLEERMUIS, 3),
    (TELEFOON, 0),
    (UIL, 3),
    (MUIS, 6),
    (JURK, 5),
    (AARDBEI, 0),
    (GIRAFFE, 2),
    (COCKTAIL, 0),
    (MUIS, 1),
    (ZEBRA, 6),
    (ROOS, 5),
    (BEER, 6),
    (BEER, 5)
]

for word, index in code:
    print(chr(ord(word[0]) - index), end="")

print()