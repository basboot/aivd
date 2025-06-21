secret = 74334919971195322368109

for i in range(15):
    n = secret & 127
    secret = secret >> 6
    print(n)