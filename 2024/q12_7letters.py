from telwoord import cardinal

for n in range(10, 100):
    number = cardinal(n, friendly=False)

    if len(number) == 7:
        print(number)


for n in range(100):
    number = set(list((cardinal(n, friendly=False)).upper()))

    # print(number)

    if 'O' in number and number.intersection(set(list("EAIU"))) == 0:
        print(number)


