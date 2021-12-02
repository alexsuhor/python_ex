def recursion(n, s):
    """
    n > 0
    s = 0
    """
    print('n =', n, end=' ')
    print('s =', s)
    if(n == 0):
        print(s)
    else:
        recursion(n-1, n+s)


recursion(-1, 0)
