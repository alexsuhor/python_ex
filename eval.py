while True:
    val = 0
    code = input('> ')
    if code == 'done':
        print(val)
        break
    else:
        val = eval(code)
        print(val)
    