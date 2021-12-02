import turtle

bob = turtle.Turtle()

for i in range(1000):
    bob.fd(10 + i)
    bob.lt(20)

turtle.mainloop()
