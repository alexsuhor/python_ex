import turtle

t = turtle.Turtle()


def koch(t, x):
    if(x < 10):
        t.fd(x)
        return
    koch(t, x/4)
    t.lt(90)
    koch(t, x/4)
    t.rt(90)
    koch(t, x/4)
    t.rt(90)
    koch(t, x/4)
    koch(t, x/4)
    t.lt(90)
    koch(t, x/4)
    t.lt(90)
    koch(t, x/4)
    t.rt(90)
    koch(t, x/4)


koch(t, 100)
t.rt(90)
koch(t, 100)
t.rt(90)
koch(t, 100)
t.rt(90)
koch(t, 100)
t.rt(90)

turtle.mainloop()