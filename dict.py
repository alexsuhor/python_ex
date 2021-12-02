import list, pronounce

def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d


def search(d, v):
    for i in d:
        if d[i] == v:
            return i
    return -1


def invert_dict(d):
    invert = dict()
    for i in d:
        # if d[i] not in invert:
        #     invert[d[i]] = [i]
        # else:
        #     invert[d[i]].append(i)
        invert.setdefault(d[i], []).append(i)
    return invert


known = {0:0, 1:1}

def memo_fib(n):
    if n in known:
        return known[n]
    res = memo_fib(n-1) + memo_fib(n-2)
    known[n] = res
    return res


def words_to_dict():
    file = open('words.txt')
    words = {}

    for word in file:
        words[word.strip()] = word.strip()
    return words

cache = {}

def ack(m, n):
    
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        res = ack(m - 1, ack(m, n - 1))
        return res


def has_duplicates(t):
    d = {}
    
    for i in t:
        if i in d:
            return True
        else:
            d[i] = 1
    print(d)
    return False


def rotate_letter(letter, number):
    o = ord(letter) - ord('a')
    return chr((o + number) % 26 + ord('a'))


def rotate_word(word, number):
    rword = ''
    for c in word:
        rword += rotate_letter(c, number)
    return rword


def rotated_serch():
    file = open('words.txt')
    words = {}
    for w in file:
        words[w.strip()] = None
    for i in words:
        for j in range(1, 14):
            rword = rotate_word(i, j)
            if rword in words:
                print(i, rword, j)


def cartalk():
    d = pronounce.read_dictionary()
    for i in d:
        if len(i) == 5:
            one = i[1:]
            two = i[0] + i[2:]
            if one in d and two in d and d[i] == d[one] == d[two]:
                print(i, one, two)


cartalk()
