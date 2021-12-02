import polygon
import math


def skip(t, size):
    t.pu()
    t.fd(size)
    t.pd()


def up_rigth(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size / 2)
    t.rt(90)


def down_left(t, size):
    t.fd(size)
    t.rt(90)
    t.fd(size / 2)
    t.rt(90)


def draw_a(t, size):
    up_rigth(t, size)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.rt(180)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.lt(90)


def draw_b(t, size):
    up_rigth(t, size)
    down_left(t, size)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.lt(90)


def draw_c(t, size):
    up_rigth(t, size)
    t.pu()
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.pd()
    t.fd(size/2)


def draw_d(t, size):
    polygon.arc(t, size/2, 180)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.pu()
    t.fd(size/2)


def draw_f(t, size):
    up_rigth(t, size)
    t.pu()
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.pd()
    t.fd(size/2)
    t.pu()
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.fd(size / 2)


def draw_e(t, size):
    up_rigth(t, size)
    t.pu()
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.pd()
    t.fd(size/2)
    t.pu()
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.pd()
    t.fd(size / 2)


def draw_g(t, size):
    up_rigth(t, size)
    t.pu()
    t.fd(size/2)
    t.rt(90)
    t.pd()
    t.fd(size/4)
    t.rt(180)
    t.fd(size/4)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size / 2)
    t.rt(180)
    t.fd(size / 2)


def draw_h(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.pu()
    t.fd(size/2)
    t.pd()
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size / 2)
    t.rt(180)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.lt(90)


def draw_i(t, size):
    t.pu()
    t.fd(size/4)
    t.pd()
    t.lt(90)
    t.fd(size)
    t.lt(180)
    t.fd(size)
    t.pu()
    t.lt(90)
    t.fd(size / 4)


def draw_j(t, size):
    t.fd(size/2)
    t.lt(90)
    t.fd(size)
    t.rt(180)
    t.fd(size)
    t.lt(90)


def draw_k(t, size):
    t.pu()
    t.fd(size/2)
    t.lt(90)
    t.pd()
    polygon.arc(t, size/2, 90)
    t.rt(180)
    polygon.arc(t, size / 2, 90)
    t.lt(90)
    t.pu()
    t.fd(size/2)
    t.lt(90)
    t.pd()
    t.fd(size)
    t.lt(90)
    t.pu()
    t.fd(size/2)


def draw_l(t, size):
    t.lt(90)
    t.fd(size)
    t.lt(180)
    t.fd(size)
    t.lt(90)
    t.fd(size/2)


def draw_m(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.pu()
    t.fd(size/4)
    t.rt(90)
    t.pd()
    t.fd(size)
    t.rt(180)
    t.fd(size)
    t.lt(90)
    t.pu()
    t.fd(size/4)
    t.pd()


def draw_n(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size/4)
    t.rt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size/4)
    t.lt(90)
    t.fd(size)
    t.rt(180)
    t.fd(size)
    t.lt(90)


def draw_o(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.fd(size/2)


def draw_p(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.fd(size / 2)
    t.rt(90)
    t.pu()
    t.fd(size/2)
    t.lt(90)
    t.pd()


def draw_q(t, size):
    draw_o(t, size)
    t.lt(135)
    t.fd(size/4)
    t.rt(180)
    t.fd(size / 4)
    t.lt(45)


def draw_r(t, size):
    draw_p(t, size)
    t.lt(135)
    t.fd(size / 2)
    t.rt(180)
    t.fd(size / 2)
    t.lt(45)


def draw_s(t, size):
    t.fd(size/2)
    t.lt(90)
    t.fd(size / 2)
    t.lt(90)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.rt(90)
    t.fd(size / 2)
    t.rt(90)
    t.pu()
    t.fd(size)
    t.lt(90)


def draw_t(t, size):
    t.pu()
    t.fd(size/4)
    t.pd()
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size/4)
    t.lt(180)
    t.fd(size/2)
    t.rt(90)
    t.pu()
    t.fd(size)
    t.lt(90)


def draw_u(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.pu()
    t.fd(size/2)
    t.rt(90)
    t.pd()
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(180)
    t.fd(size/2)


def draw_v(t, size):
    t.lt(90)
    t.pu()
    t.fd(size)
    t.pd()
    t.rt(90)
    t.rt(75)
    t.fd(size * 1.05)
    t.lt(150)
    t.fd(size * 1.05)
    t.rt(75)
    t.rt(90)
    t.pu()
    t.fd(size)
    t.lt(90)


def draw_w(t, size):
    t.pu()
    t.fd(size/2)
    t.lt(90)
    t.fd(size)
    t.pd()
    t.lt(90)
    draw_m(t, size)
    t.rt(180)
    t.pu()
    t.fd(size/2)
    t.rt(90)
    t.fd(size)
    t.lt(90)


def draw_x(t, size):
    t.pu()
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.pd()
    t.rt(45)
    t.fd(math.sqrt(size**2 * 2))
    t.lt(45)
    t.lt(90)
    t.pu()
    t.fd(size)
    t.pd()
    t.lt(90)
    t.lt(45)
    t.fd(math.sqrt(size**2 * 2))
    t.lt(45)
    t.lt(90)
    t.pu()
    t.fd(size)


def draw_y(t, size):
    t.pu()
    t.lt(90)
    t.fd(size)
    t.pd()
    t.rt(90)
    t.rt(45)
    t.fd(math.sqrt((size/2)**2 * 2))
    t.lt(90)
    t.fd(math.sqrt((size/2)**2 * 2))
    t.rt(180)
    t.fd(math.sqrt((size/2)**2 * 2))
    t.lt(45)
    t.fd(size/2)
    t.lt(90)
    t.pu()
    t.fd(size/2)


def draw_z(t, size):
    t.pu()
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.pd()
    t.fd(size)
    t.rt(90)
    t.rt(45)
    t.fd(math.sqrt(size**2 * 2))
    t.lt(90)
    t.lt(45)
    t.fd(size)
