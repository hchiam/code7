# The "Code 7 Project" info & posts:  http://hchiam.blogspot.ca/2016/06/code-7-project-github-blog.html
# Problem 3 from:  http://blog.smartbear.com/programming/7-silly-programming-challenges-to-do-for-fun/
# Turtle info, basics:  https://opentechschool.github.io/python-beginners/en/simple_drawing.html
# Turtle info, functions:  https://docs.python.org/3/library/turtle.html

import turtle

# initialize
x = 0
y = -100

# define a function to do the recursive stuff:
def recursiveStuff( setLevel=1, x=0, y=-100, r=90, w=10, length=150 ):
    level = setLevel
    # account for if user enters 0 instead of 1
    if level <= 0:
        level = 1
    # limit speed
    if level > 9:
        print("Limiting to 9 levels due to speed limitations")
        level = 9
    # update positions for next line
    x,y = drawLine(x,y,r,w,length)
    if level > 1:
        level -= 1
        #x += 0
        #y += 10
        #r += 60
        w /= 1.5
        length /= 1.5
        recursiveStuff(level, x, y, r+60, w, length) # recursive call with updated parameters
        recursiveStuff(level, x, y, r-45, w, length) # recursive call with updated parameters

# define a function to draw a line segment:
def drawLine(x,y,rotation,width,length):
    turtle.penup()
    turtle.goto(x,y)
    turtle.width(width)
    turtle.setheading(rotation)
    turtle.pendown()
    turtle.forward(length)
    return turtle.position()

# the part of the program that "interacts" with the user:
levels = 7 # (set to 7 levels) <-- TRY CHANGING THIS TO ANY NUMBER FROM 1 TO 9
turtle.hideturtle()
turtle.speed(0) # this makes it go at full speed
turtle.goto(x,y) # go to starting position
turtle.pencolor("dark green")
turtle.dot(50)
recursiveStuff(levels)
print("Drawing complete!")
