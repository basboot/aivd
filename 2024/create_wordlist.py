import re

filename = "gpt_niet_zo_goed.txt"

file1 = open(f"./scribd/{filename}", "r")

lines = file1.readlines()

words = set()

for line in lines:
    row = line.rstrip()

    # Regex to match words outside brackets
    pattern = r'\b(?!(?:[^\)]*\())\w+\b'

    matches = re.findall(pattern, row)

    for word in matches:
        words.add(word.upper())

words = list(words)

words.sort(key=lambda x: (len(x), x))

print(words)

with open(f"./scribd/filtered-{filename}", "w") as file:
    file.write("\n".join(words))