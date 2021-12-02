file = open('words.txt')

# for word in file:
#     if(len(word.strip()) > 19):
#         print(word)


def has_no_e(word):
    for let in word:
        if let == 'e':
            return False
    return True


def word_without_e():
    w = 0
    ne = 0
    for word in file:
        w = w + 1
        if has_no_e(word):
            print(word)
            ne = ne + 1
    percent = ne / (w / 100)
    print('all: ', w, 'without "e": ', ne, 'percent: ', percent)


def avoids(word, letters):
    for let in letters:
        if let in word:
            return False
    return True


def prompt_forbidden():
    letters = input('Enter forbidden letters:\n')

    for word in file:
        if avoids(word, letters):
            print(word)


def uses_only(word, letters):
    for letter in word:
        if not (letter in letters):
            return False
    return True


def uses_all(word, letters):
    for let in letters:
        if not (let in word):
            return False
    return True


def vowels():
    w = 0
    for word in file:
        if uses_all(word, 'aeiouy'):
            print(word)
            w = w + 1
    print(w)


def is_abecedarian(word):
    last = word[0]
    for let in word:
        if let < last:
            return False
        last = let
    return True


def abec():
    c = 0
    for word in file:
        if is_abecedarian(word.strip()):
            print(word)
            c = c + 1
    print(c)


abec()
