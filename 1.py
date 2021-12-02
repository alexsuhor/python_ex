import turtle
import math

bob = turtle.Turtle()

edge = 40

def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)


def polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)


def circle(t, r):
    polygon(t, 2 * math.pi * r / edge, edge)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def leaf(t, r, angle):
    t.rt(angle / 2)
    arc(t, r, angle)
    t.lt(180 - angle)
    arc(t, r, angle)
    t.lt(180 - angle)
    t.lt(angle / 2)


def flower(t, n, angle):
    for i in range(n):
        leaf(bob, 50, angle)
        bob.lt(360 / n)


def edge(t, length):
    t.fd(length)
    t.pu()
    t.lt(180)
    t.fd(length)
    t.lt(180)
    t.pd()


def shape(t, l, n):
    polygon(t, l, n)
    t.lt((n - 2) * 180 / n / 2)
    t.pu()
    r = l / (2 * math.sin(math.radians(180 / n)))
    print(r)
    t.fd(r)
    t.pd()
    t.lt(180)
    for i in range(n):
        edge(t, r)
        t.lt(360 / n)



shape(bob, 200, 7)

turtle.mainloop()