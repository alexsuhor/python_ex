def sed(pattern, new, one, two):
    two = open(two, 'w')

    for l in open(one):
        two.write(l.replace(pattern, new))
    two.close()

sed('is', 'wow', 'emma1.txt', 'emma2.txt')
