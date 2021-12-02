import random

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


print(choose_from_hist(a))