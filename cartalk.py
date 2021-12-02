import string

file = open('words.txt')

def findword():
    for word in file:
        if len(word) > 5:
            end = len(word) - 6
            for i in range(end):
                if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                    print(word)


def is_palindrome(word):
    return word == string.reverse(word)


def fine_palindrom():
    for i in range(100000, 999999):
        s = str(i)
        s2 = str(i+1)
        s3 = str(i+2)
        s4 = str(i+3)
        if is_palindrome(s[2:6]) and is_palindrome(s2[1:6]) and is_palindrome(s3[1:5]) and is_palindrome(s4):
            print(i, i+1, i+2, i+3)


def reversible():
    for i in range(50):
        print('---', i, '---')
        a = 0
        s = 1
        m = s + i
        while s < 150:
            if str(m) == string.reverse(str(s)):
                print(s, m)
                a = a + 1
            s, m = s + 1, m + 1
        print('----')


reversible()