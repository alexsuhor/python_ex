import math
import copy
import turtle
from pprint import pprint

def distance_between_points(a, b):
    print(a.x, a.y, "/", b.x, b.y)
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def move_rectangle(rect, dx, dy):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2


class Point:
    """
    x, y is a number
    """

class Circle:
    """
    center is a Point
    radius is a number
    """

class Rect:
    """
    a is a Point
    width and height are numbers
    """

c = Circle()
c.center = Point()
c.center.x = 100
c.center.y = 100
c.radius = 100

p = Point()
p.x = 226
p.y = 100


rect = Rect()
rect.a = Point()
rect.a.x = 220
rect.a.y = 100
rect.width = 185
rect.height = 185


def point_in_circle(circle, point):
    return distance_between_points(circle.center, point) <= circle.radius


def rect_in_circle(circle, rect):
    first = rect.a
    second = rect.a
    second.x += rect.width
    third = rect.a
    third.y += rect.height
    fourth = rect.a
    fourth.x += rect.width
    fourth.y += rect.height
    return point_in_circle(circle, first) and point_in_circle(circle, second) and point_in_circle(circle, third) and point_in_circle(circle, fourth)


def rect_circle_overlap(circle, rect):
    first = copy.copy(rect.a)
    second = copy.copy(rect.a)
    second.x += rect.width
    third = copy.copy(rect.a)
    third.y += rect.height
    fourth = copy.copy(rect.a)
    fourth.x += rect.width
    fourth.y += rect.height
    res = point_in_circle(circle, first) or point_in_circle(circle, second) or point_in_circle(circle, third) or point_in_circle(circle, fourth)
    return res


def draw_rect(turtle, rect):
    turtle.fd(rect.width)
    turtle.rt(90)
    turtle.fd(rect.height)
    turtle.rt(90)
    turtle.fd(rect.width)
    turtle.rt(90)
    turtle.fd(rect.height)


def draw_circle(turt, circle):
    import turtles
    turtles.circle(turt, circle.radius)


class Time:
    """
    attributes: hour, minute, second
    """

t1 = Time()
t1.hour = 1
t1.minute = 27
t1.second = 38

def time(h, m, s):
    _t = Time()
    _t.hour = h
    _t.minute = m
    _t.second = s
    return _t

def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    return t1.hour * 3600 + t1.minute * 60 + t1.second < t2.hour * 3600 + t2.minute * 60 + t2.second


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def increment(time, seconds):
    t = copy(time)
    time.second += seconds
    min, sec = divmod(time.second, 60) 
    time.second = sec
    time.minute += min
    hour, min = divmod(time.minute, 60) 
    time.minute = min
    time.hour += hour
    return t


def time_to_int(time):
    minute = time.hour * 60 + time.minute
    second = minute * 60 + time.second
    return second

print(time_to_int(t1))
