#========================
# Maze
#========================

import turtle

def draw_square():
    turtle.begin_fill()
    for turns in range(4):
        turtle.forward(1)
        turtle.left(90)
    turtle.end_fill()
        
def draw_grid(grid):
    turtle.shape("turtle")
    turtle.setworldcoordinates(0,0,10,10)
    turtle.speed(0)
    for T in range(len(grid)):
        for F in range(len(grid[T])):
            if grid[T][F] == 0:
                turtle.setpos(F,T)
                turtle.speed(0)
                turtle.delay(0)
                turtle.penup()
                draw_square()
                

    turtle.color("blue")
    turtle.penup()
    turtle.setpos(1.5,1.5)
    
    turtle.onkeypress(move_up, "Up")
    turtle.onkeypress(move_down, "Down")
    turtle.onkeypress(move_left, "Left")
    turtle.onkeypress(move_right, "Right")
    

def move_up():
    if grid1[int(turtle.ycor()) + 1][int(turtle.xcor())] != 0:
        turtle.setheading(90)
        turtle.forward(1)
    
def move_down():
    if grid1[int(turtle.ycor()) - 1][int(turtle.xcor())] != 0:
        turtle.setheading(-90)
        turtle.forward(1)
    
def move_right():
    if grid1[int(turtle.ycor())][int(turtle.xcor()) + 1] != 0:
        turtle.setheading(0)
        turtle.forward(1)
    
def move_left():
    if grid1[int(turtle.ycor())][int(turtle.xcor()) - 1] != 0:
        turtle.setheading(180)
        turtle.forward(1)


grid1 = [[0,0,0,0,0,0,0,0,0,0],
    	[0,1,0,0,0,1,1,1,1,0],
    	[0,1,0,1,1,1,0,0,1,0],
    	[0,1,1,1,0,1,0,0,1,0],
    	[0,1,0,1,0,1,1,0,0,0],
    	[0,0,1,1,1,1,0,1,1,0],
    	[0,0,1,0,0,1,1,1,0,0],
    	[0,0,1,1,1,0,0,1,0,0],
    	[0,0,1,0,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]

draw_grid(grid1)
turtle.listen()
turtle.mainloop()
 
