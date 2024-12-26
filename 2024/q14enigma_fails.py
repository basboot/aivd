# Check possible options

# print("14B: stekkerbord", len(create_swaps(True)))
# print("reflector", len(create_swaps()))
# print("rotor", math.factorial(6))
# print("14C: twee rotors en een reflector", math.factorial(6) ** 2 * len(create_swaps()))
# print("14D: sleutelvierkant", math.factorial(36))
# print("14E: sleutelvierkant, twee rotors en een reflector",
#       math.factorial(36) * math.factorial(6) ** 2 * len(create_swaps()))
#
# print(math.factorial(6) * math.factorial(6))

# exit()

legal_chars = ["O", "N", "(1|!)", "C", "S", "X", "I", "G", "L", "(3|.)", "H", "T", "(5|\")", "Z", "R", "A", "(8|,)", "D", "P", "(6|:)", "W", "E", "(2|?)", "J", "F", "K", "U", "(0| )", "Y", "Q", "(9|;)", "(7|_)", "B", "(4|')", "M", "V"]

# Genetic algorithm to find lettervierkant based on different fitness functions

def ioc(t):
    letter_counts = Counter(t)
    non_alpha = -sum([v for k, v in letter_counts.items() if not k.isalpha()])
    return sum(ni * (ni - 1) for ni in letter_counts.values())/len(t) + non_alpha


# Example frequency distribution of Dutch letters (uppercase)
dutch_letter_freq = {
    'E': 18.91, 'N': 10.03, 'A': 7.49, 'T': 6.79, 'I': 6.50,
    'R': 6.41, 'O': 6.06, 'D': 5.93, 'S': 3.73, 'L': 3.57,
    'G': 3.40, 'V': 2.85, 'H': 2.38, 'K': 2.25, 'M': 2.21,
    'U': 1.99, 'J': 1.50, 'W': 1.52, 'Z': 1.39, 'B': 1.24,
    'P': 1.14, 'C': 0.61, 'F': 0.55, 'X': 0.03, 'Y': 0.03, 'Q': 0.01
}

# Common bigrams (uppercase)
common_bigrams = {'IJ', 'AA', 'OO', 'EE', 'UI', 'EU', 'SCH'}


# Fitness function
def fitness_letter_level_uppercase(string):
    # Ensure the string is uppercase
    string = string.upper()

    # 1. Letter frequency match
    letter_count = Counter(string)
    total_letters = sum(letter_count[char] for char in dutch_letter_freq)
    frequency_score = 0
    if total_letters > 0:
        for letter, expected_freq in dutch_letter_freq.items():
            observed_freq = letter_count[letter] / total_letters
            frequency_score += 1 - abs(observed_freq - expected_freq / 100)  # Reward closeness to expected frequency
        frequency_score /= len(dutch_letter_freq)  # Normalize

    # 2. Bigram score
    bigram_score = 0
    for bigram in common_bigrams:
        bigram_score += string.count(bigram)
    bigram_score /= max(len(string) - 1, 1)  # Normalize by possible bigrams

    # 3. Valid character penalty
    valid_chars = set(dutch_letter_freq.keys())
    invalid_chars = sum(1 for char in string if char not in valid_chars)
    penalty = invalid_chars / len(string) if string else 1  # Penalize invalid characters

    # Final score (weights can be adjusted)
    total_score = (0.5 * frequency_score + 0.4 * bigram_score - 0.1 * penalty)
    return max(total_score, 0)  # Ensure score is non-negative


# Fitness function
def fitness_dutch(sentence):

    words_in_sentence = re.findall(r'\b[a-zA-Z]+\b', sentence)

    # 1. Dictionary matching
    word_match_score = sum(1 for word in words_in_sentence if word in dutch_words) / len(
        words_in_sentence) if words_in_sentence else 0

    # 2. Character distribution
    common_patterns = ['IJ', 'SCH', 'AA', 'OO', 'UI', 'EU', 'IK', 'EN']
    char_pattern_score = sum(sentence.count(pattern) for pattern in common_patterns) / len(sentence) if sentence else 0

    # # 3. Basic grammatical structure heuristic
    # # Example: Verbs are often in the second position in a clause
    # verb_like_words = {"is", "zijn", "heb", "heeft", "kan", "kun", "moet"}  # Example list of Dutch verbs
    # grammar_score = 1 if any(word in verb_like_words for word in words_in_sentence[1:2]) else 0

    # 4. Length and spacing
    average_word_length = sum(len(word) for word in words_in_sentence) / len(
        words_in_sentence) if words_in_sentence else 0
    length_score = 1 if 3 <= average_word_length <= 10 else 0  # Typical Dutch word length range

    # Combine scores
    total_score = (0.2 * word_match_score +
                   0.3 * char_pattern_score +
                   # 0.2 * grammar_score +
                   0.3 * length_score)

    return total_score


# Example frequency distribution of Dutch letters (uppercase)
dutch_letter_freq = {
    'E': 18.91, 'N': 10.03, 'A': 7.49, 'T': 6.79, 'I': 6.50,
    'R': 6.41, 'O': 6.06, 'D': 5.93, 'S': 3.73, 'L': 3.57,
    'G': 3.40, 'V': 2.85, 'H': 2.38, 'K': 2.25, 'M': 2.21,
    'U': 1.99, 'J': 1.50, 'W': 1.52, 'Z': 1.39, 'B': 1.24,
    'P': 1.14, 'C': 0.61, 'F': 0.55, 'X': 0.03, 'Y': 0.03, 'Q': 0.01
}

# Common bigrams (uppercase)
common_bigrams = {'IJ', 'AA', 'OO', 'EE', 'UI', 'EU', 'SCH'}

# Common trigrams (uppercase)
common_trigrams = {
    'ING', 'EER', 'SCH', 'ERE', 'OOR', 'REN', 'ERD', 'TER', 'STE', 'AAR', 'VOO',
    'AAN', 'GES', 'EST', 'CHT', 'GER', 'PRO', 'BES', 'EID', 'TEN', 'DER', 'KEN',
    'HEI', 'PLA', 'PER', 'ERI', 'DEN', 'END', 'LEN', 'PRE', 'BEL', 'GEN', 'TIE',
    'ELD', 'ELE', 'ISC', 'NDE', 'BER', 'AND', 'GRO', 'ERS', 'GEP', 'ESC', 'ENT',
    'BED', 'EDE', 'OED', 'PEN', 'LIN', 'VOL', 'STI', 'LĲK', 'TIG', 'TEL', 'ENS',
    'ROE', 'VER', 'BEK', 'ORT', 'LOE', 'IST', 'ARD', 'GEV', 'TTE', 'NEN', 'ATI',
    'GRA', 'EVE', 'KER', 'POL', 'RIN', 'IER', 'ETE', 'GEL', 'RAA', 'ART', 'LOO',
    'LAN', 'LLE', 'SSE', 'BEV', 'ROO', 'EKE', 'OND', 'GEW', 'KKE', 'RIE', 'NNE',
    'PAR', 'TIS', 'ACH', 'NGE', 'ANT', 'SEN', 'AST', 'DIG', 'LAA', 'ANS', 'ANG',
    'BLO'
}


# Fitness function
def fitness_letter_level_with_trigrams(string):
    # Ensure the string is uppercase
    string = string.upper()

    # 1. Letter frequency match
    letter_count = Counter(string)
    total_letters = sum(letter_count[char] for char in dutch_letter_freq)
    frequency_score = 0
    if total_letters > 0:
        for letter, expected_freq in dutch_letter_freq.items():
            observed_freq = letter_count[letter] / total_letters
            frequency_score += 1 - abs(observed_freq - expected_freq / 100)  # Reward closeness to expected frequency
        frequency_score /= len(dutch_letter_freq)  # Normalize

    # 2. Bigram score
    bigram_score = 0
    for bigram in common_bigrams:
        bigram_score += string.count(bigram)
    bigram_score /= max(len(string) - 1, 1)  # Normalize by possible bigrams

    # 3. Trigram score
    trigram_score = 0
    for trigram in common_trigrams:
        trigram_score += string.count(trigram)
    trigram_score /= max(len(string) - 2, 1)  # Normalize by possible trigrams

    # 4. Valid character penalty
    valid_chars = set(dutch_letter_freq.keys())
    invalid_chars = sum(1 for char in string if char not in valid_chars)
    penalty = invalid_chars / len(string) if string else 1  # Penalize invalid characters

    # Final score (weights can be adjusted)
    total_score = (0.4 * frequency_score + 0.3 * bigram_score + 0.2 * trigram_score - 0.1 * penalty)
    return max(total_score, 0)  # Ensure score is non-negative


# Example frequency distribution of Dutch letters (uppercase)
dutch_letter_freq = {
    'E': 18.91, 'N': 10.03, 'A': 7.49, 'T': 6.79, 'I': 6.50,
    'R': 6.41, 'O': 6.06, 'D': 5.93, 'S': 3.73, 'L': 3.57,
    'G': 3.40, 'V': 2.85, 'H': 2.38, 'K': 2.25, 'M': 2.21,
    'U': 1.99, 'J': 1.50, 'W': 1.52, 'Z': 1.39, 'B': 1.24,
    'P': 1.14, 'C': 0.61, 'F': 0.55, 'X': 0.03, 'Y': 0.03, 'Q': 0.01
}

# Common bigrams (uppercase)
common_bigrams = {'IJ', 'AA', 'OO', 'EE', 'UI', 'EU', 'SCH'}

# Common trigrams (uppercase)
common_trigrams = {
    'ING', 'EER', 'SCH', 'ERE', 'OOR', 'REN', 'ERD', 'TER', 'STE', 'AAR', 'VOO',
    'AAN', 'GES', 'EST', 'CHT', 'GER', 'PRO', 'BES', 'EID', 'TEN', 'DER', 'KEN',
    'HEI', 'PLA', 'PER', 'ERI', 'DEN', 'END', 'LEN', 'PRE', 'BEL', 'GEN', 'TIE',
    'ELD', 'ELE', 'ISC', 'NDE', 'BER', 'AND', 'GRO', 'ERS', 'GEP', 'ESC', 'ENT',
    'BED', 'EDE', 'OED', 'PEN', 'LIN', 'VOL', 'STI', 'LĲK', 'TIG', 'TEL', 'ENS',
    'ROE', 'VER', 'BEK', 'ORT', 'LOE', 'IST', 'ARD', 'GEV', 'TTE', 'NEN', 'ATI',
    'GRA', 'EVE', 'KER', 'POL', 'RIN', 'IER', 'ETE', 'GEL', 'RAA', 'ART', 'LOO',
    'LAN', 'LLE', 'SSE', 'BEV', 'ROO', 'EKE', 'OND', 'GEW', 'KKE', 'RIE', 'NNE',
    'PAR', 'TIS', 'ACH', 'NGE', 'ANT', 'SEN', 'AST', 'DIG', 'LAA', 'ANS', 'ANG',
    'BLO'
}

# Dutch Index of Coincidence (approximate)
dutch_ic = 0.068


# Function to calculate the Index of Coincidence
def calculate_ic(string):
    string = string.upper()
    letter_count = Counter(char for char in string if char.isalpha())
    N = sum(letter_count.values())
    if N <= 1:
        return 0  # Avoid division by zero for short strings
    ic = sum(f * (f - 1) for f in letter_count.values()) / (N * (N - 1))
    return ic


# Fitness function
def fitness_with_ic(string):
    # Ensure the string is uppercase
    string = string.upper()

    # 1. Letter frequency match
    letter_count = Counter(string)
    total_letters = sum(letter_count[char] for char in dutch_letter_freq)
    frequency_score = 0
    if total_letters > 0:
        for letter, expected_freq in dutch_letter_freq.items():
            observed_freq = letter_count[letter] / total_letters
            frequency_score += 1 - abs(observed_freq - expected_freq / 100)  # Reward closeness to expected frequency
        frequency_score /= len(dutch_letter_freq)  # Normalize

    # 2. Bigram score
    bigram_score = 0
    for bigram in common_bigrams:
        bigram_score += string.count(bigram)
    bigram_score /= max(len(string) - 1, 1)  # Normalize by possible bigrams

    # 3. Trigram score
    trigram_score = 0
    for trigram in common_trigrams:
        trigram_score += string.count(trigram)
    trigram_score /= max(len(string) - 2, 1)  # Normalize by possible trigrams

    # 4. Index of Coincidence
    ic = calculate_ic(string)
    ic_score = 1 - abs(ic - dutch_ic) / dutch_ic  # Reward closeness to Dutch IC

    # # 5. Valid character penalty
    # valid_chars = set(dutch_letter_freq.keys())
    # invalid_chars = sum(1 for char in string if char not in valid_chars)
    # penalty = invalid_chars / len(string) if string else 1  # Penalize invalid characters

    words_in_sentence = re.findall(r'\b[a-zA-Z]+\b', string)

    # 1. Dictionary matching
    word_match_score = sum(1 for word in words_in_sentence if word in dutch_words and len(word) > 4) / len(
        words_in_sentence) if words_in_sentence else 0

    # Final score (weights can be adjusted)
    total_score = (0.3 * frequency_score + 0.25 * bigram_score + 0.2 * trigram_score + 0.15 * ic_score + word_match_score * 0.25)
    return max(total_score, 0)  # Ensure score is non-negative


def get_random_sleutelvierkant():
    new_sleutelvierkant = legal_chars.copy()
    random.shuffle(new_sleutelvierkant)
    return np.reshape(new_sleutelvierkant, (6, 6))

def mix_sleutelvierkant(sv1, sv2):
    unused = set(legal_chars)
    new_sv = np.empty((6, 6), dtype='U10')
    for i in range(6):
        for j in range(6):
            # TODO: mutate?
            if sv1[i, j] == sv2[i, j] and sv1[i, j] in unused and random.random() < 0.5:
                new_sv[i, j] = sv1[i, j]
                unused.remove(sv1[i, j])
                continue
            if sv1[i, j] in unused and sv2[i, j] in unused and random.random() < 0.3:
                use = sv1[i, j] if random.random() > 0.5 else sv2[i, j]
                new_sv[i, j] = use
                unused.remove(use)
                continue
            if sv1[i, j] in unused and random.random() < 0.3:
                new_sv[i, j] = sv1[i, j]
                unused.remove(sv1[i, j])
                continue
            if sv2[i, j] in unused and random.random() < 0.3:
                new_sv[i, j] = sv2[i, j]
                unused.remove(sv2[i, j])
                continue
            # random fallback
            use = random.choice(tuple(unused))
            new_sv[i, j] = use
            unused.remove(use)

    # print(new_sv)
    return new_sv



cypher_d = "7RBNG4ACEK83YHUZLODARRHEZ3WT8URC4EC3XAQR448CW7NZK434K977B36D7ZEZRBU6PK" + \
           "CCXDSUC4E6QXZ7FZRVYOCEJK3N8AOTEUR44O6Q6AJH4UZ4ONAB8RUEGHEAZPULMBO7RBIQ" + \
           "UTKW78JJCWMKWOCSH6O73YONBV644CEDABR44CDYLR7HUUEC2XS6HIU7L03NBRLJ3CCUP"



# Checked: all configs give same solution :-)
for reflector, rotors in solutions_c:
    enigmini = Enigma(sleutelvierkant, (0, 1, 2, 3, 4, 5), rotors, reflector, (0, 0))
    message = enigmini.encode(cypher_d, True)
    print(message)
    break # only need one



N_POPULATION = 100
N_SURVIVORS = 20
N_CHILDREN = 50

population = [get_random_sleutelvierkant() for _ in range(100)]



for _ in range(1000000):
    results = []
    for gene in population:

        enigmini = Enigma(gene, (0, 1, 2, 3, 4, 5), rotors, reflector, (0, 0))
        message = enigmini.encode(cypher_d, True)
        # print(message)

        fitness = fitness_with_ic(message)

        results.append((fitness, gene, message))

    results.sort(key=lambda x: x[0], reverse=True) # max fitness first

    next_population = []
    for i in range(N_SURVIVORS):
        next_population.append(results[i][1])

    for i in range(N_CHILDREN):
        next_population.append(mix_sleutelvierkant(results[int(random.random() * N_SURVIVORS)][1], results[int(random.random() * N_SURVIVORS)][1]))

    for i in range(N_POPULATION - N_SURVIVORS - N_CHILDREN):
        next_population.append(get_random_sleutelvierkant())

    population = next_population

    print("fitness: ", results[0][0])
    print(results[0][2]) # show best current

exit()


def show_message(m):
    print(m[0:70])
    print(m[71:140])
    print(m[140:])

show_message(message)


# Manual checking, based in wrong assumptions that it has become a substitution cypher

letter_freq = Counter(message)

print("Different chars", len(letter_freq.keys()))
print(letter_freq)

print(Counter([message[i] + message[i + 1] for i in range(len(message) - 1)]))

print(Counter([message[i: i + 2] for i in range(len(message) - 2)]))

print(Counter([message[i: i + 3] for i in range(len(message) - 3)]))

# meer dan 3 is uniek

print(len(message))

# 209 tekens, omdat het waarschijnlijk weer een liedje is verwacht ik weer niet te lange woorden
# de e, n en a het meeste voor gemiddeld.


# Z waarschijnlijk geen spatie
# D geen spatie, V ook niet (want einde regel)

# options = list('DZHQF6N3MKYLC')
# values  = list('enati rodslgv')
#
# searching = False
# for val in permutations(values) if searching else [values]:
#     next_message = message
#     for subs_from, subs_to in zip(options, val):
#         next_message = next_message.replace(subs_from, subs_to)
#
#     show_message(next_message)

# find space

for space_option in letter_freq.keys():
    next_message = message.replace(space_option, " ").replace("\n", " ")
    wordlengths = Counter([len(x) for x in next_message.split(" ")])
    print(wordlengths, max(wordlengths.keys()))




def find_word(cypher, substitutions, used, position, current_node, word, words):
    if current_node.is_end:
        if len(word) > len(substitutions) + 1:
            words.add(word)

    if position == len(cypher):
        return words

    if cypher[position] in substitutions:
        if substitutions[cypher[position]] in current_node.children: # go on
            return find_word(cypher, substitutions, used, position + 1, current_node.children[substitutions[cypher[position]]], word + substitutions[cypher[position]], words)
        else:
            return words
    else:
        for letter in current_node.children:
            if letter in used:
                continue # cannot have different subs
            else:
                next_sub = substitutions.copy()
                next_sub[cypher[position]] = letter
                words = find_word(cypher, next_sub, used.union({letter}), position + 1, current_node.children[letter], word + letter, words)


        return words

letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

# "aplrlaoqkl"
for startpos in range(len(message)):
    print(f"", sorted(list(find_word(message, {}, set(), startpos, wordlist.root, "", set())), key=len, reverse=True))




# def find_substitutions(cypher, substitutions, used, alpha_count, non_alpha_count, position, current_node, wordtrie, message):
#     print(message)
#     if position == len(cypher):
#         print("FOUND")
#         print(substitutions)
#         return substitutions
#     if cypher[position] in substitutions:
#         if substitutions[cypher[position]] in current_node.children: # go on
#             return find_substitutions(cypher, substitutions, used, alpha_count + 1, 0, position + 1, current_node.children[substitutions[cypher[position]]], wordtrie, message + substitutions[cypher[position]])
#         else:
#             return None
#     else:
#         # this is not efficient, we should use children and think of something for the non alpha's
#         for letter in letters:
#             if letter == cypher[position]:
#                 continue # cannot map on self
#             if letter not in used and (letter in current_node.children or (current_node.is_end and letter.isnumeric())):
#                 if letter.isnumeric() and (alpha_count < 2 or non_alpha_count > 3): # ignore single letters, and avoid 3 digits
#                     pass
#                 else:
#
#                     next_sub = substitutions.copy()
#                     next_sub[cypher[position]] = letter
#
#                     next_node = current_node.children[letter] if letter in current_node.children else wordtrie.root
#
#                     result = find_substitutions(cypher, next_sub, used.union({letter}), 0 if not letter.isalpha() else alpha_count + 1, 0 if letter.isalpha() else non_alpha_count + 1, position + 1, next_node, wordtrie, message + letter)
#
#                     if result is not None:
#                         return result
#         return None

#  print(m[0:70])
#     print(m[71:140])
#     print(m[140:])

# find_substitutions(cypher_d[140:], {}, set(), 0, 0, 0, wordlist.root, wordlist, "")



# 14B IK(0| )KEN(0| )GEEN(0| )ANDERE(0| )LANDEN(8|,)(0| )ZELFS(0| )AL(0| )BEN(0| )IK(0| )ER(0| )GEWEEST(3|.) (3, 2, 1, 0, 5, 4)

# 14C ALS(0| )ER(0| )EEN(0| )WEDSTRIJD(0| )ZOU(0| )ZIJN(0| )VOOR(0| )FRUIT(3|.)(0| )EN(0| )ZE(0| )DEELDEN(0| )MEDAILLES(0| )UIT(3|.)


