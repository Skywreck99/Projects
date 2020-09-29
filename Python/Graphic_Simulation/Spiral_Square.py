#========================
# Spiral Square
#========================

import math
import random
import turtle

turtle.speed(0)
def spiro(sides, numberPerRev, radius):
    len_side = radius * 2 * math.sin(180 / sides)
    countRev = 0
    while countRev < numberPerRev:
        r = random.random()
        g = random.random()
        b = random.random()
    
        turtle.color(r,g,b)
        countSide = 0
        turtle.begin_fill()
        while countSide < sides:
            turtle.forward(len_side)
            turtle.left(360/sides)
            countSide += 1
        countRev += 1
        turtle.end_fill()
        turtle.left(360/numberPerRev)
        
spiro(4, 9, 100)
