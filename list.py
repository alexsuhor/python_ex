import random
import string
import bisect


def for_all(x):
    total = 0
    for i in x:
        total = total + i
    return total


def capitalize_all(list):
    res = []
    for i in list:
        if i.isupper():
            res.append(i)
    return res


def nested_sum(x):
    sum = 0
    for i in x:
        nsum = 0
        for a in i:
            nsum += a
        sum += nsum
    return sum


def cumsum(x):
    a = []
    sum = 0
    for i in range(len(x)):
        a.append(x[i] + sum)
        sum += x[i]
    return a


def middle(x):
    return x[1:len(x)-1]


def chop(x):
    del x[0]
    del x[len(x)-1]


def is_sorted(x):
    if x == sorted(x):
        return True
    return False


def reverse(x):
    t = []
    for a in x:
        t = [a] + t
    return t


def is_anargam(a, b):
    if list(a) == reverse(b):
        return True
    else:
        return False


def has_duplicates(x):
    for i in range(len(x)):
        for j in x[i+1:len(x)]:
            if i == j:
                return True
    return False


def birthday():
    birth = []
    for i in range(22):
        birth.append(random.randint(1, 365))
    return birth


def paradox_checker():
    j = 0
    for i in range(100):
        t = birthday()
        if has_duplicates(t):
            j += 1
    print(j)


def words_to_list():
    file = open('words.txt')
    words = []
    for word in file:
        words.append(word)


def in_bisect(value, a):
    start = 0
    end = len(a)-1
    
    while start < end:
        middle = (start + end) // 2
        if value < a[middle]:
            end = middle
        elif value > a[middle]:
            start = middle
        else:
            return True
        
    return False


def contain(t, elem):
    index = bisect.bisect_left(t, elem)
    if index < len(t):
        return elem == t[index]
    return False


def reverse_pair():
    file = open('words.txt')
    words = []
    for word in file:
        words.append(word.strip())
    for i in words:
        cont = contain(words, string.reverse(i))
        if cont:
            print(i, string.reverse(i))


def one_to_two(word):
    first = ''
    second = ''
    for i in range(len(word)):
        if i % 2 == 0:
            first += word[i]
        else:
            second += word[i]
    return (first, second)


def one_to_three(word):
    first = ''
    second = ''
    third = ''
    for i in range(len(word)):
        if i % 3 == 0:
            first += word[i]
        elif i % 3 == 1:
            second += word[i]
        else:
            third += word[i]
    return (first, second, third)


def interlock():
    file = open('words.txt')
    words = []
    for word in file:
        words.append(word.strip())
    for i in words:
        first, second = one_to_two(i)
        if contain(words, first) and contain(words, second):
            print(i, first, second)


def tri_interlock():
    file = open('words.txt')
    words = []
    for word in file:
        words.append(word.strip())
    for i in words:
        first, second, third = one_to_three(i)
        if contain(words, first) and contain(words, second) and contain(words, third):
            print(i, first, second, third)


