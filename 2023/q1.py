words = ["GRINT", "VERSA", "KARIG", "MALIE", "ZIJNS", "FRANK", "KREET", "PROEF", "GOZER", "JADEN", "VROED"]

letters = {}

for word in words:
    print(word[::-1])

    for c in word:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
print(letters)

chars = []
for l in letters:
    chars.append((letters[l], l))

chars.sort(reverse=True)
print(chars)

print("".join([c for i, c in chars]))
