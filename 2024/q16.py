# 16. Begin met de 9 en de 10 om de lussen te vinden.
# Je vindt twee letters en twee cijfers. Van letters
# binnen de lus met de twee letters moet je (om en
# om) die twee letters afhalen. Van letters binnen
# de lus met de twee cijfers (om en om) die twee
# cijfers afhalen. Samen met de (onvercijferde)
# letters buiten de twee lussen krijg je zo een
# vraag van 50 vakjes lang.

secret = "DVICOIHREONZYYZLFENBKOUKANSYONDOXPANLPFXANXFDWQLVV"
mask = "12221212011012121211103212331011131012111113333201"

key1 = list(map(lambda x: (ord(x) - ord('A') + 0), "WK")) # zero indexed
key2 = [7, 4]

print(key1, key2)

def decode_letter(letter, key):
    return chr(((ord(letter) - ord('A') - key) % 26) + ord('A'))

result = ""
k1 = 0
k2 = 0
for i, m in enumerate(mask):
    letter = secret[i]
    # print(m, letter)
    match m:
        case "0":
            result += letter
        case "1":
            next_letter = decode_letter(letter, key1[k1 % 2])
            result += next_letter
            k1 += 1
        case "2":
            next_letter = decode_letter(letter, key2[k2 % 2])
            result += next_letter
            k2 += 1
        case "3":
            next_letter = decode_letter(letter, key1[k1 % 2])
            next_letter = decode_letter(next_letter, key2[k2 % 2])
            result += next_letter
            k1 += 1
            k2 += 1

print(result)

print(k2)

message = "HOEVEELKEERZOUDEVARROODGEGEVENHEBBENBIJNEDBRAIN74?"

print(len(message))

split_lists = [list(message[i:i+10]) for i in range(0, len(message), 10)]


