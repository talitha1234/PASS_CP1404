"""
Generate a random encryption dictionary and encode a
message from the user then decode it back to the original
message using dictionary comprehension.
"""

import random

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def main():
    plain_to_cypher = generate_code()

    print(f"The secret code is: \n{plain_to_cypher}")
    user_text = input("Message to encode: ")

    cypher_text = encode(plain_to_cypher, user_text)
    print(f"Coded message: {cypher_text}")
    decode_text = decode(plain_to_cypher, cypher_text)
    print(f"Decoded message: {decode_text}")


def generate_code():
    keys = ALPHABET.copy()
    values = keys.copy()
    random.shuffle(values)
    return dict(zip(keys, values))


def encode(plain_to_cypher, plain_text):
    plain_text = plain_text.upper()
    return "".join(plain_to_cypher[letter] if (letter in plain_to_cypher.keys()) else letter for letter in plain_text)


def decode(plain_to_cypher, cypher_text):
    cyper_to_plain = {cypher: plain for plain, cypher in plain_to_cypher.items()}
    return "".join(cyper_to_plain[letter] if (letter in cyper_to_plain.keys()) else letter for letter in cypher_text)


main()
