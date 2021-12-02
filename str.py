def is_palindrom(word):
    return word == word[::-1]


def rotate_word(word, amount):
    new_word = ''

    for w in word:
        val = chr((ord(w) - ord('a') + amount) % 26 + ord('a'))
        new_word = new_word + val

    return new_word


print(rotate_word('hello', 1))
# print(chr(ord('b') + 1))