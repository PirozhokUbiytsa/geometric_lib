import math

def area(r):
    '''takes a number r, returns the area of a circle of radius r'''
    if r <= 0:
        raise ValueError('radius cannot be zero or negative')
    else:
        return math.pi * r * r

def perimeter(r):
    '''takes a number r, returns the perimeter of a circle of radius r'''
    return 2 * math.pi * r
