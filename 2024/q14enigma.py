from itertools import product

message = "-10--000-0-0-0--0-10--0101----10-101000000"

message = "-01--111-1-1-1--1-01--1010----01-010111111" # inverted




def generate_permutations(input_string):
    if len(input_string) != 7:
        raise ValueError("Input string must be of length 7.")

    # Find the positions of all '-' characters in the string
    dash_positions = [i for i, char in enumerate(input_string) if char == '-']

    # Generate all possible combinations of '0' and '1' for the '-' positions
    replacements = list(product('01', repeat=len(dash_positions)))

    permutations = []

    for replacement in replacements:
        # Convert the input string to a list for mutability
        temp = list(input_string)

        # Replace each '-' with the corresponding value in the replacement tuple
        for pos, value in zip(dash_positions, replacement):
            temp[pos] = value

        # Join the list back into a string and add to permutations
        permutations.append(''.join(temp))

    return permutations

for i in range(0, len(message), 7):
    print([chr(int(binary_string, 2)) for binary_string in generate_permutations(message[i:i + 7])])
    # break