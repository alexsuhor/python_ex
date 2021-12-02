import turtle
import math

bob = turtle.Turtle()


def edge(t, length):
    t.fd(length)
    t.pu()
    t.lt(180)
    t.fd(length)
    t.lt(180)
    t.pd()


def shape(t, n, length):
    for i in range(n):
        edge(t, length)
        t.lt(360 / n)
    t.fd(length)
    t.lt(180 - (360 / n))
    t.fd(2 * math.pi * length / n)




shape(bob, 5, 100)

turtle.mainloop()
