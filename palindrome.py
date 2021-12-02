def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    else:
        return False


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)



print(gcd(14, 28))