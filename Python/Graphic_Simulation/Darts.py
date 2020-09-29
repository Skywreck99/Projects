#========================
# Darts
#========================

import turtle
import random

turtle.ht()
turtle.pu()
turtle.speed(0)
darts = 0
dartsC = 0

while darts < 1000:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    turtle.goto(x*150, y*150)
    
    # Checks if the darts are inside the circle
    if x**2 + y**2 <= 1:
        turtle.color("green")
        dartsC += 1
    else:
        turtle.color("red")
    turtle.dot(5)
    darts += 1

print((dartsC/darts) * 4)
