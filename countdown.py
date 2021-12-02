import math


def sqrt(a):
    x = 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x


i = 1
while i < 10:
    print(float(i), end='\t\t')
    print(sqrt(i), end='\t\t')
    print(math.sqrt(i), end='\t\t')
    print(abs(sqrt(i) - math.sqrt(i)))
    i = i + 1