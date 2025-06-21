cypher = "DVICOIHRONYYZLFENBKUKANSYODOXPALPFXANXFDWQ" # #11, ?
msk =    "12221212011012121211103212331011131012111113333"
puzzle = "/|||/|/|///|/|/|///X|/|XX////X//|/////XXXX" # |/



secrets = {"/": "WERLDKAMIONSCHPBFGJQTUVXYZ", "|": "VIERNZTGABCDFHJKLMOPQSUWXY"} # / , |
counters = {"/": 0, "|": 0}


def ceasar(c, n):
    return chr(((ord(c) - ord('A') + n) % 26) + ord('A'))


def decode(c, secret):
    if secret == "X":
        return "-"#decode(decode(c, "/"), "|")
    else:
        s = secrets[secret].index(c)

        result = chr(s + ord('A'))

        counters[secret] += 1

        return result

for i, c in enumerate(cypher):
    print(decode(c, puzzle[i]), end="")

print()
