def key(word):
    return list_to_str(sorted(list(word)))


def list_to_str(t):
    s = ''
    for i in t:
        s += i
    return s


def max_len(an):
    max = 1
    f = None
    for c in an:
        if len(an[c]) > max:
            max = len(an[c])
            f = c
    return f


def anagram_sets():
    file = open('words.txt')
    words = {}
    for w in file:
        word = w.strip()
        k = key(word)
        words.setdefault(k, []).append(word)
    for i in range(len(words)):
        x = max_len(words)
        print(words.pop(x))
