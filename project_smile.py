from re import A, M
from typing import Any, Text

alphabet = 'abcdefghijklmnopqrstuvwxyz '
smiles = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣',
          '🥲', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍',
          '🥰', '😘', '😗', '😏', '😒', '😕', '😢', '😑',
          '🙄', '😤', '🤭']
vocabulary = dict(zip(alphabet, smiles))


def comp_key(text, key):
    list_text = list(text)
    list_key = list(key)

    list_complete_key = []
    for i in range(len(list_text)):
        modular_z = i % len(key)
        list_complete_key.append(list_key[modular_z])
    return list_complete_key


def cypher(text, key):

    list_text = list(text)
    list_key = list(key)

    # /completed key generation
    # completed_key = comp_key(text, key)

    # /generate cypher
    cypher_text = ''

    block_size = len(key)
    row_size = len(text) // len(key)
    if (row_size == 0) or ((len(text) % len(key)) > 0):
        row_size += 1

    # /create 2d array
    matrix = [['x'] * block_size for _ in range(row_size)]
    # print(matrix)

    lm = 0
    for i in range(row_size):
        for j in range(block_size):
            if lm < len(list_text):
                matrix[i][j] = list_text[lm]
                lm += 1
            else:
                break

    # print(f'Matrix: {matrix}')

    # /create cyphertext
    for i in range(block_size):
        for j in range(row_size):
            cypher_text += str(matrix[j][i])
    print(f'Cyphertext: {cypher_text}')

    # /change to smiles
    smile_text = ''
    for i in cypher_text:
        smile_text += vocabulary[i]

    return smile_text


def decypher(smile_text, key):
    # /change back to text format
    cypher_text = ''
    for i in smile_text:
        a = list(vocabulary.keys())[list(vocabulary.values()).index(i)]
        cypher_text += str(a)
    # print(f'Cypher in 75: {cypher_text}')

    # /from cypher to plain
    list_plain = []

    block_size = len(key)
    row_size = len(cypher_text) // len(key)
    if (row_size == 0) or ((len(cypher_text) % len(key)) > 0):
        row_size += 1

    matrix = [['x'] * block_size for _ in range(row_size)]
    lm = 0
    for i in range(block_size):
        for j in range(row_size):
            matrix[j][i] = cypher_text[lm]
            lm += 1

    # print(matrix)

    # /to sting
    plain_text = ''
    for i in range(row_size):
        for j in range(block_size):
            plain_text += str(matrix[i][j])

    return plain_text


def main():
    text = input('text: ').lower()
    key = input('key: ')

    # key = str(int(key) + int(key) * 178776262627777 % 234567)

    # completed_key = comp_key(text, key)
    cyphered = cypher(text, key)
    decyphered = decypher(cyphered, key)

    # print(f'Completed key: {completed_key}')
    print(f'Output: {cyphered}')
    print(
        f'Decyphered text: {decyphered}')


if __name__ == '__main__':
    main()
