#========================
# Checkered Board
#========================

import turtle

turtle.ht()
turtle.penup()
turtle.setpos(-448, 448)
turtle.speed(0)


for g in range(1,9):
    if g % 2 == 0:
        turtle.right(90)
        turtle.forward(96)
        turtle.right(90)
        turtle.forward(48)
        for l in range(1,9):
            if l % 2 == 0:
                turtle.color("black")
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(48)
                    turtle.right(90)
                    turtle.forward(48)
                turtle.end_fill()
                if l < 8:
                    turtle.forward(96)
                else:
                    turtle.forward(48)
            else:
                turtle.color("red")
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(48)
                    turtle.right(90)
                    turtle.forward(48)
                turtle.end_fill()
                turtle.forward(96)
        if g < 8:
            turtle.left(90)
            turtle.forward(96)
            turtle.left(90)
            turtle.forward(48)
    else:
        for h in range(1,9):
            if h % 2 == 0:
                turtle.color("black")
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(48)
                    turtle.left(90)
                    turtle.forward(48)
                turtle.end_fill()
                if h < 8:
                    turtle.forward(96)
                else:
                    turtle.forward(48)
            else:
                turtle.color("red")
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(48)
                    turtle.left(90)
                    turtle.forward(48)
                turtle.end_fill()
                turtle.forward(96)
