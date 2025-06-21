cypher = "VZSVZRUHIEDMSVHMSHFIZZQFDKDCDMGDSRODKUZMNMYDMNJHZR"

def ceasar(c, n):
    return chr(((ord(c) - ord('A') + n) % 26) + ord('A'))

for i in range(2):
    for c in cypher:
        print(ceasar(c, i), end="")
    print()