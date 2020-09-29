from turtle import *

from random import randint
mylist = ["red", "orange", "yellow", "green", "blue", "purple"]


def rand_color():
    return mylist[randint(0, len(mylist) - 1)]

class Shape:
    def __init__(self, x = 0, y = 0, color = ""):
        self.x = x
        self.y = y
        self.color = color
        self.fill = False

    def set_color(self,string):
        self.color = rand_color()
        
    def get_color(self):
        return self.color()

    def __str__(self):
        return "loc: " + "(" + str(self.x) + ", " + str(self.y) + ") , " + "color: " + str(self.color)

    def draw(self, turtle):
        setpos(self.x, self.y)

class Circle(Shape):
    def __init__(self, x = 0, y = 0, r = 10):
        self.x = x
        self.y = y
        self.r = r
        Shape.__init__(self, x, y, rand_color())

    def __str__(self):
        "loc: " + "(" + str(self.x) + ", " + str(self.y) + ") , " + "color: " + str(self.color) + ", rad: " + str(self.r)

    def draw(self, turtle):
        turtle.penup()
        turtle.setpos(self.x, self.y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.r)
        turtle.end_fill()

class Ring(Circle):
    def __init__(self, x, y, out_rad, in_rad):
        Circle.__init__(self, x, y, out_rad)
        self.in_rad = in_rad

    def __str__(self):
        "loc: " + "(" + str(self.x) + ", " + str(self.y) + ") , " + "color: " + str(self.color) + ", rad: " + str(self.r)

    def draw(self, turtle):
        turtle.penup()
        turtle.setpos(self.x, self.y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.r)
        turtle.end_fill()
                                    
        turtle.penup()
        turtle.setpos(self.x, self.y+self.r-self.in_rad)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(self.in_rad)
        turtle.end_fill()
        
class Rectangle(Shape):
    def __init__(self, x, y, width = 20, height = 20):
        Shape.__init__(self, x, y, rand_color())
        self.width = width
        self.height = height
        
    def __str__(self):
        return "loc: (" + str(self.x) + ", " + str(self.y) + ") , color: " + str(self.color) + ", w: " + str(self.width) + ", h: " + str(self.height)
    
    def draw(self, t):
        t.penup()
        t.setpos(self.x, self.y)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)
        
    
class Display:
    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()
        self.elements = list()
        self.turtle.speed(0)
        self.turtle.ht()
        self.screen.onclick(self.mouse_event)
        self.screen.listen()
    
    def add(self, Shape):
        self.elements.append(Shape)
        
    def remove(self, Shape):
        self.elements.remove(Shape)
        self.turtle.clear()
        
    def mouse_event(self, x, y):
        rad = randint(10, 50)
        rad1 = randint(10, 50)
        if (randint(1, 50) % 2 == 0):
            shape = Circle(x, y-rad, rad)
            self.add(shape)
            shape.draw(self.turtle)
        else:
        #elif (randint(1, 50) % 3 == 1):
            shape = Ring(x, y-rad, rad, randint(1, rad-1))
            self.add(shape)
            shape.draw(self.turtle)
            '''
        else:
            shape = Rectangle(x-rad1/2, y-rad/2, rad1, rad)
            self.add(shape)
            shape.draw(self.turtle)'''
            
   
        
            
    
        


