import os
def walk1(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            print(name)


try:
    fin = open('sldkf.')
except:
    print('something went wrong')
