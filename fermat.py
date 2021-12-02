def check_fermat(a, b, c, n):
    if(n > 2 and a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn`t work')


def check_values():
    b = int(input('Write the b value\n'))
    c = int(input('Write the c value\n'))
    n = int(input('Write the n value\n'))
    a = int(input('Write the a value\n'))

    check_fermat(a, b, c, n)


check_values()
