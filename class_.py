import math

def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy