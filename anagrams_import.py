import anagram_sets as anag
import dbm
import pickle


def store_anagrams():
    anagrams = anag.all_anagrams('words.txt')
    shelf = dbm.open('anagrams', 'c')
    for i in anagrams:
        shelf[i] = pickle.dumps(anagrams[i])


def read_anagrams(word):
    shelf = dbm.open('anagrams')

    return pickle.loads(shelf[anag.signature(word)])


print(read_anagrams('beard'))
