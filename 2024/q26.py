n1 = 143264571461416565
n2 = 35713232273726475

o1 = int(str(n1), 8)
o2 = int(str(n2), 8)

print(o1, o2)

def to_text(n, bit7=False):
    result = []
    while n > 0:
        i = n & (0b11111111 if not bit7 else 0b1111111)
        # print(i)
        n = n >> (8 if not bit7 else 7)

        result.append(chr(i))

    result.reverse()
    return "".join(result)

print(to_text(o1), to_text(o2))
print(to_text(n1), to_text(n2))
print(to_text(o1), to_text(o2, True))
print(to_text(n1), to_text(n2, True))







