import os
import hashlib

def find_all_mp3(begin):
    songs = []
    for root, dirs, files in os.walk(begin):
        for s in files:
            _, ext = os.path.splitext(s)
            if ext == '.mp3':
                songs.append(root + s)
    return songs


def find_duplicates(top):
    songs = find_all_mp3(top)
    files = {}

    for s in songs:
        res = top + s
        file = open(s, 'rb').read()
        hash = hashlib.md5(file).hexdigest()
        files.setdefault(hash, []).append(s)
    for f in files:
        if len(files[f]) > 1:
            print(files[f])


find_duplicates('D:\\Python\\mp3\\')
