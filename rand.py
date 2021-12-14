import random, string, bisect

def x():
    one = 0
    zero = 0
    for i in range(1000):
        x = random.randint(0, 1)
        if x == 0:
            zero += 1
        else:
            one += 1
    print(zero, one)


def choose_from_hist(h):
    collect = []
    for i in h:
        collect += [i] * h[i]
        print(collect)
    return random.choice(collect)


def process_file(filename):
    hist = {}
    file = open(filename, encoding='utf-8')
    for line in file:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    print(t)


def diffw():
    book = process_file('emma.txt')
    dic = process_file('words.txt')
    return set(book) - set(dic)

def random_word():
    hist = process_file('emma.txt')
    words = []
    cumfreq = []
    total_freq = 0
    for word, freq in hist.items():
        words.append(word)
        total_freq += freq
        cumfreq.append(total_freq)
    r = random.randint(1, cumfreq[len(cumfreq)-1])
    index = bisect.bisect_left(cumfreq, r)
    return words[index]
    

def markov(filename):
    mmap = {}
    file = open(filename, encoding='utf-8')
    last = ''
    for line in file:
        for word in line.split():
            mmap.setdefault(last, []).append(word.lower())
            last = word
    last = random.choice(mmap)
    text = random.choice(mmap(last))
    for i in range(20):
        last = random.choice(mmap[last])
        text += ' ' + last
    print(text)


