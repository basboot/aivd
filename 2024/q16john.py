


alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def add(x,y):

    return alfabet[(alfabet.index(x)+alfabet.index(y)) % 26]

def sub(x,y):

    return alfabet[(alfabet.index(x)-(alfabet.index(y) + 1)) % 26]

def shift(x,n):

    return alfabet[(alfabet.index(x) + n) % 26]



zin = "DVICOIHREONZYYZLFENBKOUKANSYONDOXPANLPFXANXFDWQEVV"
msk = "12221212011012121211103212331011131012111113333201"

# zin2 = ""
# msk2 = ""
# for j in range(10):
#     for i in range(5):
#         zin2 += zin[i * 10 + j]
#         msk2 += msk[i * 10 + j]
#
# print(zin2, msk2)
#
# # exit()
#
# zin = zin2
# msk = msk2




key1 = "WK"
key2 = "GD" #74
keylen1 = len(key1)
keylen2 = len(key2)



SINGLE_TEXT, BOTH_TEXT, ALL = 0, 1, 2

def decode(mode=SINGLE_TEXT):
    result = ""

    k1 = 0
    k2 = 0
    k3 = 0

    k0 = 0

    for i,letter in enumerate(zin):

        match int(msk[i]):

            case 0:
                result += letter # no cypher
                k0 += 1

            case 1:
                k = (k1 + k3)
                if mode == BOTH_TEXT:
                    k += k2
                if mode == ALL:
                    k += k2 + k0
                l = sub(letter,key1[k%keylen1])
                result += l
                k1 = (k1+1)

            case 2:
                k = (k2 + k3)
                if mode == BOTH_TEXT:
                    k += k1
                if mode == ALL:
                    k += k1 + k0
                l = sub(letter,key2[k%keylen2])
                result += l
                k2 = (k2+2)

            case 3:
                k = (k1 + k3)
                if mode == BOTH_TEXT:
                    k += k2
                if mode == ALL:
                    k += k2 + k0
                l = sub(letter,key1[k% keylen1])
                k = (k2 + k3)
                if mode == BOTH_TEXT:
                    k += k1
                if mode == ALL:
                    k += k1 + k0
                m = sub(l,key2[k% keylen2])
                result += m
                k3 += 1

    return result

print(decode())

# HAEYKJQWKCVLPDFJBMCCGWOKTMWOILWUUBMXDXPKPHRR