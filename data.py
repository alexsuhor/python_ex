import string


def clear(word):
    w = []
    result = ''
    pattern = string.punctuation
    for i in word:
        if i not in pattern:
            w.append(i)
    for i in w:
        result += i
    print(result)
    return result


def analize():
    pattern = string.punctuation + string.whitespace + '“' + "”"
    file = open('Great leaders.txt', encoding="utf8")
    word_list = []
    dwords = {}
    for s in file:
        wl = s.lower().split()
        for i in range(len(wl)):
            wl[i] = wl[i].strip(pattern)
        word_list += (wl)
    for i in word_list:
        dwords[i] = dwords.setdefault(i, 0) + 1
    fwords = []
    max = 0
    mword = ''
    for j in range(100):
        for i in dwords:
            if dwords[i] > max:
                mword = i
                max = dwords[i]
        print(mword, max)
        dwords[mword] = 0
        max = 0

    print(fwords)
    


analize()
