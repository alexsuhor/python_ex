def reverse(str):
    i = len(str) - 1
    line = ''
    while i >= 0:
        line = line + str[i]
        i = i - 1
    return line
